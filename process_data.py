import pandas as pd
import os

# 1. Load the three CSV files from the 'data' folder
df1 = pd.read_csv('./data/daily_sales_data_0.csv')
df2 = pd.read_csv('./data/daily_sales_data_1.csv')
df3 = pd.read_csv('./data/daily_sales_data_2.csv')

# Combine all three into one massive dataframe
all_data = pd.concat([df1, df2, df3])

# 2. Filter for only "Pink Morsels"
pink_morsels = all_data[all_data['product'].str.lower() == 'pink morsel'].copy()

# 3. Create the 'sales' column (quantity * price)
# First, remove the '$' from the price column and turn it into a float (decimal number)
pink_morsels['price'] = pink_morsels['price'].str.replace('$', '').astype(float)

# Multiply them!
pink_morsels['sales'] = pink_morsels['quantity'] * pink_morsels['price']

# 4. Keep only the requested columns: Sales, Date, and Region
final_data = pink_morsels[['sales', 'date', 'region']]

# 5. Export this final formatted data to a new CSV file
final_data.to_csv('formatted_data.csv', index=False)
print("Data processing complete! Saved to formatted_data.csv")