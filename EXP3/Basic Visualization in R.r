# Experiment No. 3: Basic Visualization in R

# Aim
To create and understand different basic graphs and visualizations using R programming.

# Description
R is a programming language commonly used for statistical calculations, data processing, and graphical representation. 
It provides built-in graph functions and also supports visualization packages like ggplot2. The base graphics system in R makes it easy to learn the basic concepts of data visualization.
Graphs help users examine and understand data before carrying out further analysis.
Line graphs represent changes over a sequence, bar charts compare different categories, pie charts illustrate proportions,
scatter plots represent relationships between numerical values, and histograms show how numerical data is distributed.
This experiment includes five simple visualization programs developed using base R functions.
Each program illustrates a specific graph type and explains how to create data vectors, provide values to graph functions, and include suitable titles and labels.
These basic techniques can also be used when working with larger datasets and more advanced visualization tools.

# Uses
- Helps examine statistical information.
- Compares values across different categories.
- Identifies changes and trends in data.
- Shows relationships between numerical variables.
- Examines the distribution of numerical values.
- Presents analytical information graphically.

# Algorithm
1. Create the required R vectors.
2. Select a suitable visualization function.
3. Pass the data to the graph function.
4. Add title and axis labels.
5. Execute the R program.
6. Observe and interpret the graph.

# Program 1: Line Graph

x <- c(1, 2, 3, 4, 5)
y <- c(10, 15, 12, 18, 20)

plot(x, y, type="o",
     main="Line Graph",
     xlab="X Values",
     ylab="Y Values")


# Program 2: Bar Chart

subjects <- c("Python", "Java", "R", "Tableau", "SQL")
marks <- c(85, 78, 82, 90, 88)

barplot(marks,
        names.arg=subjects,
        main="Marks by Subject",
        xlab="Subject",
        ylab="Marks")


# Program 3: Pie Chart

values <- c(35, 25, 20, 20)
labels <- c("Python", "Java", "R", "Tableau")

pie(values,
    labels=labels,
    main="Technology Usage")


# Program 4: Scatter Plot

hours <- c(1, 2, 3, 4, 5, 6)
marks <- c(45, 50, 58, 65, 72, 80)

plot(hours, marks,
     main="Study Hours vs Marks",
     xlab="Study Hours",
     ylab="Marks",
     pch=19)


## Program 5: Histogram

marks <- c(45, 50, 52, 55, 58, 60, 62, 65,
           68, 70, 72, 75, 78, 80, 82, 85,
           88, 90)

hist(marks,
     breaks=5,
     main="Distribution of Marks",
     xlab="Marks",
     ylab="Frequency")


## Libraries / Functions Used

- plot() – used to draw line graphs and scatter plots.
- barplot() – represents categorical data using bars.
- pie() – displays data as proportional circular sectors.
- hist() – illustrates the frequency distribution of numerical data.
- Base R graphics – provides built-in visualization functions without installing additional packages.

# Result
Thus, five types of graphs, namely line graph, bar chart, pie chart, scatter plot, and histogram, were generated successfully using the built-in visualization functions of R.
