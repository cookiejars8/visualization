Python Visualization 1: Average Auto Theft Rate in Toronto (2014–2025)

# Software Used

This visualization was created using Python in Visual Studio Code. I used pandas for data cleaning and restructuring, and matplotlib to generate the line chart. A virtual environment was used to manage dependencies and ensure consistency.

# Intended Audience

The intended audience includes Toronto residents, students, journalists, and policymakers interested in understanding crime trends over time. The visualization is designed to be accessible to a general audience.

# Message

This visualization shows how the average auto theft rate across Toronto neighbourhoods changed from 2014 to 2025. The main message is that auto theft rates increased significantly after 2020, peaked around 2023, and declined slightly afterward. The chart highlights that crime trends shift over time rather than remaining constant.

# Design Considerations

I used a line chart because it is appropriate for time-series data. Circular markers were added to clearly indicate individual years. The gridlines were kept light to assist interpretation without distracting from the data. I included a descriptive title and clearly labeled axes, specifying that the rate is per 100,000 residents to avoid confusion with raw counts. I avoided unnecessary colors or decorative elements to maintain clarity.

# Reproducibility

The visualization is fully reproducible because all data cleaning, reshaping, and calculations were done in Python code. The dataset is publicly available through Toronto Open Data. The script reshapes the dataset from wide to long format, calculates yearly averages, and saves the final plot as a PNG file. A virtual environment ensures that the required libraries can be reinstalled and the project recreated.

# Accessibility

To support accessibility, I used clear labels, readable font sizes, and high contrast between text and background. The visualization does not rely on color to distinguish categories, reducing barriers for colorblind users. The chart is simple and can be described verbally if needed.

# Impacted Communities

Neighbourhoods experiencing higher auto theft rates may be affected by how this data is interpreted. Policymakers and law enforcement may use this information for resource allocation. Because crime data can contribute to stigma, the visualization presents trends neutrally without emphasizing specific neighbourhoods.

# Feature Selection

The dataset includes multiple crime categories and both raw counts and rates. I chose to focus only on auto theft and to use rate variables rather than raw counts to account for differences in population size across neighbourhoods. Other crime types and geometry data were excluded to maintain focus.

# Underwater Labour

Significant background work included identifying relevant columns, reshaping the dataset, cleaning missing values, calculating averages, troubleshooting the Python environment, and testing different chart formats before selecting the final design.