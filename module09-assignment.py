# Module 9 Assignment: Introduction to Data Analysis with Pandas
# GlobalTech Sales Analysis

import pandas as pd
import numpy as np
from io import StringIO

print("=" * 60)
print("GLOBALTECH QUARTERLY SALES ANALYSIS")
print("=" * 60)

# ----- USE THE FOLLOWING CODE TO SIMULATE A CSV FILE (DO NOT MODIFY) -----


csv_content = """Date,Region,Store,Category,Product,Units,Unit_Price,Total_Sales,Promotion
2024-01-15,North America,NA001,Smartphones,PhoneX,12,899.99,10799.88,No
2024-01-18,Europe,EU002,Computers,LaptopPro,8,1299.99,10399.92,Yes
2024-01-20,Asia,AS001,Audio,WirelessEarbuds,25,149.99,3749.75,No
2024-01-22,North America,NA002,Wearables,SmartWatch,15,249.99,3749.85,No
2024-01-25,Latin America,LA001,Smartphones,PhoneX,7,899.99,6299.93,Yes
2024-01-27,Europe,EU001,Accessories,PhoneCase,35,24.99,874.65,No
2024-01-30,Asia,AS002,Smartphones,PhoneSE,18,499.99,8999.82,No
2024-02-02,North America,NA001,Computers,LaptopPro,6,1299.99,7799.94,No
2024-02-05,Europe,EU002,Wearables,SmartWatch,20,249.99,4999.80,Yes
2024-02-08,North America,NA003,Audio,WirelessEarbuds,30,149.99,4499.70,Yes
2024-02-10,Asia,AS001,Accessories,ChargingCable,45,19.99,899.55,No
2024-02-12,Latin America,LA001,Computers,TabletBasic,12,399.99,4799.88,No
2024-02-15,North America,NA002,Smartphones,PhoneSE,14,499.99,6999.86,No
2024-02-18,Europe,EU001,Audio,BlueSpeaker,22,79.99,1759.78,Yes
2024-02-20,Asia,AS002,Wearables,FitnessTracker,28,129.99,3639.72,No
2024-02-22,North America,NA001,Accessories,PhoneCase,50,24.99,1249.50,Yes
2024-02-25,Latin America,LA002,Smartphones,PhoneX,9,,8099.91,No
2024-02-28,Europe,EU002,Computers,LaptopBasic,10,899.99,8999.90,No
2024-03-02,North America,NA003,Wearables,FitnessTracker,,129.99,2599.80,Yes
2024-03-05,Asia,AS001,Smartphones,PhoneSE,15,499.99,7499.85,No
2024-03-08,Europe,EU001,Accessories,ChargingCable,60,19.99,1199.40,Yes
2024-03-10,North America,NA002,Computers,TabletPro,7,599.99,4199.93,No
2024-03-12,Latin America,LA001,Audio,WirelessEarbuds,18,149.99,2699.82,No
2024-03-15,North America,NA001,Wearables,SmartWatch,12,249.99,2999.88,No
2024-03-18,Europe,EU002,Smartphones,PhoneX,11,899.99,9899.89,Yes
2024-03-20,Asia,AS002,Computers,LaptopPro,6,1299.99,7799.94,No
2024-03-22,North America,NA001,Audio,BlueSpeaker,25,79.99,1999.75,No
2024-03-25,Latin America,LA002,Accessories,PhoneCase,40,,999.60,No"""

sales_data_csv = StringIO(csv_content)
# ----- END OF SIMULATION CODE -----


# ============================================================
# TODO 1: Load and Explore the Dataset
# ============================================================

# 1.1 Load the dataset
sales_df = pd.read_csv(sales_data_csv)

# 1.2 First 5 rows
print("\n--- First 5 Rows ---")
print(sales_df.head())

# 1.3 DataFrame info
print("\n--- DataFrame Info ---")
print(sales_df.info())

# 1.4 Dimensions
print(f"\n--- Dimensions: {sales_df.shape[0]} rows x {sales_df.shape[1]} columns ---")

# 1.5 Summary statistics
print("\n--- Summary Statistics ---")
print(sales_df.describe())


# ============================================================
# TODO 2: Column Selection and Basic Analysis
# ============================================================

# 2.1 Select Product, Units, Total_Sales columns
print("\n--- Product / Units / Total_Sales ---")
print(sales_df[['Product', 'Units', 'Total_Sales']])

# 2.2 Total units sold
total_units = sales_df['Units'].sum()

# 2.3 Total revenue
total_revenue = sales_df['Total_Sales'].sum()

# 2.4 Average unit price
avg_unit_price = sales_df['Unit_Price'].mean()


# ============================================================
# TODO 3: Row Selection and Filtering
# ============================================================

# 3.1 North America only
na_sales = sales_df[sales_df['Region'] == 'North America']

# 3.2 Units > 20
high_volume_sales = sales_df[sales_df['Units'] > 20]

# 3.3 PhoneX on promotion
phonex_promo = sales_df[(sales_df['Product'] == 'PhoneX') & (sales_df['Promotion'] == 'Yes')]

# 3.4 February 2024 sales
feb_sales = sales_df[sales_df['Date'].str.contains('2024-02')]


# ============================================================
# TODO 4: Advanced Filtering and Analysis
# ============================================================

# 4.1 Best product by total sales
best_product = sales_df.groupby('Product')['Total_Sales'].sum().idxmax()

# 4.2 Total sales by region, sorted descending
sales_by_region = sales_df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)

# 4.3 Average units sold per category
avg_units_by_category = sales_df.groupby('Category')['Units'].mean()

# 4.4 Promotion comparison
promoted     = sales_df[sales_df['Promotion'] == 'Yes']
not_promoted = sales_df[sales_df['Promotion'] == 'No']

promo_comparison = {
    'promo_avg_sales':        promoted['Total_Sales'].mean(),
    'no_promo_avg_sales':     not_promoted['Total_Sales'].mean(),
    'promo_total_revenue':    promoted['Total_Sales'].sum(),
    'no_promo_total_revenue': not_promoted['Total_Sales'].sum()
}


# ============================================================
# TODO 5: Missing Value Detection
# ============================================================

# 5.1 Missing value counts
missing_counts = sales_df.isnull().sum()

# 5.2 Missing value percentages
missing_percentages = (sales_df.isnull().sum() / len(sales_df)) * 100


# ============================================================
# TODO 6: Business Insights
# ============================================================

# 6.1 Top category by region
top_categories_by_region = (
    sales_df.groupby(['Region', 'Category'])['Total_Sales']
    .sum()
    .groupby(level='Region')
    .idxmax()
    .apply(lambda x: x[1])
)

# 6.2 Average unit price per category
avg_price_by_category = sales_df.groupby('Category')['Unit_Price'].mean()

# 6.3 Product revenue analysis
product_totals = sales_df.groupby('Product')['Total_Sales'].sum()
product_revenue_analysis = pd.DataFrame({
    'total_revenue': product_totals,
    'percentage':    (product_totals / total_revenue) * 100
})


# ============================================================
# TODO 7: Generate Analysis Report
# ============================================================

print("\n" + "=" * 60)
print("GLOBALTECH Q1 2024 SALES ANALYSIS REPORT")
print("=" * 60)

# 7.1 Overall performance
avg_sale_value = total_revenue / len(sales_df)
print("\nOverall Performance:")
print(f"- Total Revenue: ${total_revenue:,.2f}")
print(f"- Total Units Sold: {int(total_units)}")
print(f"- Average Sale Value: ${avg_sale_value:,.2f}")

# 7.2 Regional performance
print("\nRegional Performance:")
for region, sales in sales_by_region.items():
    print(f"{region}: ${sales:,.2f}")

# 7.3 Category performance
print("\nCategory Performance:")
for category in avg_units_by_category.index:
    avg_units = avg_units_by_category[category]
    avg_price = avg_price_by_category[category]
    print(f"{category}: Avg Units: {avg_units:.1f}, Avg Price: ${avg_price:.2f}")

# 7.4 Promotion effectiveness
print("\nPromotion Effectiveness:")
print(f"- Promoted Items Avg Sale: ${promo_comparison['promo_avg_sales']:,.2f}")
print(f"- Non-Promoted Items Avg Sale: ${promo_comparison['no_promo_avg_sales']:,.2f}")
print(f"- Revenue from Promotions: ${promo_comparison['promo_total_revenue']:,.2f}")

# 7.5 Data quality
columns_with_missing = missing_counts[missing_counts > 0].index.tolist()
total_missing = int(missing_counts.sum())
print("\nData Quality Report:")
print(f"- Missing Values Found: {columns_with_missing}")
print(f"- Total Missing Entries: {total_missing}")

# 7.6 Recommendations
print("\nKEY BUSINESS RECOMMENDATIONS:")

# Recommendation 1
top_region = sales_by_region.idxmax()
print(f"\n1. Double down on {top_region}.")
print(f"   With ${sales_by_region[top_region]:,.2f} in Q1 revenue, {top_region} is the")
print("   strongest market. Prioritise inventory replenishment and localised")
print("   marketing campaigns here to sustain and grow this lead.")

# Recommendation 2
lift = promo_comparison['promo_avg_sales'] - promo_comparison['no_promo_avg_sales']
direction = "higher" if lift > 0 else "lower"
print(f"\n2. Aim to refine promotion strategy the  promoted items averaged ${abs(lift):,.2f} {direction}")
print("   per transaction than non-promoted ones. Run targeted promotions on")
print("   high-margin categories (Computers, Smartphones) rather than blanket")
print("   discounting to protect margins while driving volume.")

# Recommendation 3
print(f"\n3. Fix data quality gaps before the next reporting cycle.")
print(f"   {total_missing} missing entries were detected in {columns_with_missing}.")
print("   Missing Unit_Price data prevented us from getting accurate margin analysis, and missing")
print("   Units data skewed the volume metrics. Aim to implement point-of-sale validation to")
print("   ensure that all fields are captured at the time of transaction.")
