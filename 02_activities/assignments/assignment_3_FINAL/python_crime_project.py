# connecting data to the project
import pandas as pd
from pathlib import Path

# get the folder this file is in (more reliable)
base_folder = Path(__file__).resolve().parent

# go into the data folder
file_path = base_folder / "data" / "neighbourhood-crime-rates - 4326.csv"

# quick check so you get a clear error if the file path is wrong
if not file_path.exists():
    print("ERROR: file not found here:", file_path)
    raise SystemExit

# read the csv file
df = pd.read_csv(file_path)

print("File loaded.")
print("Total rows and columns:", df.shape)

# find all the auto theft rate columns
auto_rate_columns = []

for column in df.columns:
    if "AUTOTHEFT_RATE_" in column:
        auto_rate_columns.append(column)

# keep only neighbourhood name and those columns
df_auto = df[["AREA_NAME"] + auto_rate_columns]

# change from wide format to long format
auto_long = df_auto.melt(
    id_vars="AREA_NAME",
    var_name="Year",
    value_name="AutoTheftRate"
)

# remove the text part so we only keep the year number
auto_long["Year"] = auto_long["Year"].str.replace("AUTOTHEFT_RATE_", "")
auto_long["Year"] = auto_long["Year"].astype(int)

# drop any missing values just in case
auto_long = auto_long.dropna()

print(auto_long.head())
print("Year range:", auto_long["Year"].min(), "-", auto_long["Year"].max())
print("Total rows after reshaping:", len(auto_long))

# NEXT PART IS VISUALIZATION
import matplotlib.pyplot as plt

# calculate the average auto theft rate per year
average_by_year = auto_long.groupby("Year")["AutoTheftRate"].mean()

print("\nAverage Auto Theft Rate per Year:")
print(average_by_year)

# make the plot
plt.figure(figsize=(8, 5))

plt.plot(
    average_by_year.index,
    average_by_year.values,
    marker="o",
    linewidth=2
)

plt.title("Average Auto Theft Rate in Toronto (2014–2025)", fontsize=12)
plt.xlabel("Year")
plt.ylabel("Auto Theft Rate (per 100,000 residents)")

plt.grid(alpha=0.3)
plt.tight_layout()

# save the image into the same folder as the script
output_path = base_folder / "python_auto_theft_trend.png"
plt.savefig(output_path, dpi=300)
print("Saved plot to:", output_path)

# show the plot
plt.show()