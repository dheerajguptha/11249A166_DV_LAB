# Experiment No. 7: Creating Scatter Plots and Maps in Tableau

# Aim:
To create scatter plots and map-based visualizations using Tableau.

# Description:
A scatter plot is a graphical representation used to examine the relationship between two numerical variables.
Tableau also supports map visualizations using geographical information such as cities, states, countries, and regions.
These graphical techniques help users recognize data patterns, detect clusters and unusual observations, and examine business performance across different locations.

# Uses:
- Examining the relationship between numerical data.
- Detecting groups, patterns, and unusual values.
- Comparing sales figures with quantity.
- Representing location-based data visually.
- Evaluating business performance across regions.

# Algorithm:
1. Open Tableau Public.
2. Connect to the required dataset.
3. Identify geographical and numerical fields.
4. Drag the required numerical fields to Columns and Rows.
5. Select Scatter Plot from the Show Me panel.
6. For map visualization, use geographical fields such as City or Region.
7. Analyze the visualization and save the workbook.

# Program:

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("sales_map_data.csv")
plt.scatter(data["Sales"], data["Quantity"])
plt.xlabel("Sales")
plt.ylabel("Quantity")
plt.title("Scatter Plot: Sales vs Quantity")
plt.show()

# Sample CSV File

City,Region,Sales,Quantity
Hyderabad,South,55000,2
Delhi,North,20000,3
Mumbai,West,30000,4
Chennai,South,25000,2
Kolkata,East,15000,5
Bangalore,South,40000,3

# Libraries Used

1. Pandas: Helps read the CSV file and organize the sales data for analysis.
2. Matplotlib: Provides functions to draw and display the scatter plot.

# Result:
Thus, scatter plot and map-based visualization techniques were explored using the sales dataset.
The scatter plot was created successfully using Python, and the dataset's geographical fields can be used to create maps in Tableau.
