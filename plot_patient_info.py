import json
from datetime import datetime
import matplotlib.pyplot as plt

# Replace this with loading from a file if you prefer
with open("patientdata.json") as f:
    data = json.load(f)

# Extract and process the data
tracking = data["Patient Tracking"]

# Prepare lists for dates and scores
dates = []
scores = []

for entry in tracking:
    timestamp = entry["Timestamp"]
    date_only = datetime.strptime(timestamp, "%Y-%m-%d %H:%M").date()
    dates.append(date_only)
    scores.append(entry["Throat Pain Score"])

# Plotting
plt.figure(figsize=(10,6))
plt.plot(dates, scores, marker='o', linestyle='-')
plt.title("Throat Pain Score Over Time")
plt.xlabel("Date")
plt.ylabel("Throat Pain Score")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
