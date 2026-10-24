# Experiment No. 9: Creating Basic Dashboards in Tableau

#Aim:
To build a basic dashboard in Tableau by combining several visualizations into a single interactive view.

#Description:
A dashboard is a collection of visualizations displayed together on a single screen. 
It allows users to examine different aspects of a dataset simultaneously, compare results, and obtain an overall understanding of business performance.
In Tableau, individual charts are created in separate worksheets before being placed together in a dashboard.
Interactive features such as filters and dashboard actions can also be included to help users explore data and observe changes across visualizations.

#Uses:
1. Displaying multiple charts in a single view.
2. Tracking important performance indicators (KPIs).
3. Analysing sales across categories and regions.
4. Enabling interactive data exploration.
5. Communicating analytical findings to decision makers.

#Algorithm:
1. Start Tableau Public.
2. Connect to the required dataset (Excel/CSV).
3. Create the individual charts, each on its own worksheet.
4. Click the New Dashboard tab at the bottom.
5. Drag the worksheets from the left pane onto the dashboard canvas.
6. Add filters and interactive elements such as dashboard actions.
7. Arrange and resize the layout, and add titles and legends as needed.
8. Save or publish the dashboard.

#Program:

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("sales_data.csv")
data.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()
data.groupby("Region")["Sales"].sum().plot(
    kind="pie", autopct="%1.1f%%")
plt.title("Sales by Region")
plt.ylabel("")
plt.show()
plt.plot(data["Quantity"], data["Sales"])
plt.title("Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.show()

#Libraries Used
- **Pandas:** Used to load the dataset and summarize sales information by category and region.
- **Matplotlib:** Helps generate the bar chart, pie chart, and line graph.
- **Tableau:** Used to combine individual worksheets into an interactive dashboard.

#Sample Output
The program generates three graphical representations of the sales dataset:

1.Bar Chart: Displays total sales for each category.
2.Pie Chart: Represents the distribution of sales across different regions.
3.Line Chart:Shows the relationship between quantity and sales.

#Result:
Thus, the process of creating a basic Tableau dashboard using multiple visualizations was studied, and the corresponding charts were generated successfully using Python.
