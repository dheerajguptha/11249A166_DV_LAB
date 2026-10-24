# Experiment No. 6: Data Aggregation and Statistical Functions in Tableau

# Aim:
To carry out data aggregation and use statistical functions in Tableau to analyze data more effectively.

# Description:
This experiment uses the pandas library in Python to perform data aggregation and statistical calculations similar to those available in Tableau.
The sales dataset is loaded from a CSV file, and the total, average, minimum, and maximum values of the Sales column are calculated.
The dataset is also grouped according to Category to determine the total sales of each category.
These calculations help summarize the data and make it easier to understand before creating visualizations in Tableau.

# Algorithm:
1. Launch Tableau Public.
2. Connect to the dataset.
3. Drag the needed fields onto Rows and Columns.
4. Apply aggregation functions (SUM, AVG, MIN, MAX) to the measures.
5. Use statistical measures to summarize the data.
6. Study the results and save the workbook.

# Program (Python):

import pandas as pd
df = pd.read_csv("SalesData.csv")
print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
print("Minimum Sales:", df["Sales"].min())
print("Maximum Sales:", df["Sales"].max())
print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum())

# Sample Output:

Total Sales: 115000
Average Sales: 19166.666666666668
Minimum Sales: 3000
Maximum Sales: 55000

Sales by Category:
Category
Electronics    78000
Furniture      37000
Name: Sales, dtype: int64

# Result:
Thus, aggregation and statistical calculations were performed successfully on the sales dataset.
The total, average, minimum, and maximum sales values, along with category-wise sales totals, were obtained for further analysis and visualization in Tableau.
