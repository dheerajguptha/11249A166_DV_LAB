# Experiment No. 2: Data Visualization Using Python

# Aim:
To create different types of charts using Python and the Matplotlib library for visualizing data effectively.

# Description:
Data visualization is a technique of presenting information in graphical form to make it easier to understand. Python's Matplotlib library supports various charts,
including line charts, bar charts, pie charts, scatter plots, and histograms, which help represent and interpret data clearly.

# Algorithm:
1. Import the Matplotlib library.
2. Create lists for the required X and Y values.
3. Select the appropriate chart type.
4. Add the chart title and axis labels.
5. Display the chart using the show() function.

# Program 1: Line Chart

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 15, 12, 18, 20]
plt.plot(x, y)
plt.title("Line Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# Program 2: Bar Chart

import matplotlib.pyplot as plt
x = ["A", "B", "C", "D", "E"]
y = [10, 15, 12, 18, 20]
plt.bar(x, y, color="skyblue")
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Program 3: Pie Chart

import matplotlib.pyplot as plt
labels = ["A", "B", "C", "D", "E"]
values = [10, 15, 12, 18, 20]
plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()

# Program 4: Scatter Plot

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 15, 12, 18, 20]
plt.scatter(x, y, color="red")
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# Program 5: Histogram

import matplotlib.pyplot as plt
data = [10, 12, 15, 15, 18, 20, 20, 22, 25, 25, 28, 30]
plt.hist(data, bins=5, color="orange", edgecolor="black")
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# Result:
Thus, different types of graphical representations were created and displayed successfully using Python and the Matplotlib library.
