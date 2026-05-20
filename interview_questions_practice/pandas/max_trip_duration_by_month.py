import pandas as pd
from datetime import datetime

data = {
    "id" : ["id01234","id01434","id13234"],
    "vendor_id" : [3,4,3],
    "pickup_datetime" : [datetime(2016,6,6,6,6,20),datetime(2016,6,9,6,6,20),None],
    "dropoff_datetime" : [datetime(2016,6,6,8,0,0),datetime(2016,6,9,6,7,20),datetime(2016,7,6,3,6,10)]
}

df = pd.DataFrame(data)

df.dropna(subset=["pickup_datetime","dropoff_datetime"], inplace=True)

df["pickup_month"] = df["pickup_datetime"].dt.to_period("M") # Pandas provide one come accessor for all time related operations.

df = df.loc[((df["dropoff_datetime"] - df["pickup_datetime"]).dt.total_seconds().groupby(by = df["pickup_month"]).idxmax()), ["pickup_month","id"]]

print(df)

# Problem Statement

# You are given taxi trip data containing:

# trip id
# pickup_datetime
# dropoff_datetime

# Tasks:

# Remove rows where either pickup or dropoff datetime is missing.
# Extract the pickup month from pickup datetime.
# Calculate trip duration.
# For each month, find the trip having the maximum duration.
# Return:
# pickup month
# trip id