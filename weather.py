import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raw = {
    "Date": [
        "2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04", "2026-04-05",
        "2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10",
        "2026-04-11", "2026-04-12", "2026-04-13", "2026-04-14", "2026-04-15",
        "2026-04-03" 
    ],
    "City": [
        "islamabad", " Lahore ", "KARACHI", "Islamabad", "lahore",
        "Karachi", " islamabad", "Lahore", "KARACHI", "Islamabad",
        "lahore", "Karachi", "Islamabad", "LAHORE", "Karachi",
        "Karachi"
    ],
    "Temperature": [
        "28C", "32C", "35C", "29C", "33C",
        "36C", "27C", "31C", "34C", "30C",
        "33C", "36C", "28C", "32C", "35C",
        "35C"
    ],
    "Humidity": [
        55.0, np.nan, 70.0, 58.0, 60.0,
        np.nan, 52.0, 65.0, 72.0, 56.0,
        61.0, 68.0, 54.0, np.nan, 71.0,
        70.0
    ],
    "Condition": [
        "sunny", " Rainy", "CLOUDY ", "Sunny", "rainy",
        "cloudy", "sunny", "Sunny", "Rainy", "Cloudy",
        "sunny", "Cloudy", "Rainy", "Sunny", "cloudy",
        "CLOUDY "
    ]
}

df = pd.DataFrame(raw)

df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()
df["Temperature"] = df["Temperature"].str.replace("C", "", regex=False).astype(float)
df["Date"] = pd.to_datetime(df["Date"])

print(f"Rows before dropping duplicates: {len(df)}")
df = df.drop_duplicates()
print(f"Rows after dropping duplicates: {len(df)}")

median_humidity = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(median_humidity)
print(f"Missing Humidity filled with median: {median_humidity}")

df_encoded = pd.get_dummies(df, columns=["Condition"], dtype=int)
print("Encoded Condition columns sample:")
print(df_encoded.filter(like="Condition_").head())

condition_counts = df["Condition"].value_counts()
print("Condition counts:")
print(condition_counts)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(df["Date"], df["Temperature"], marker="o", color="crimson", linestyle="-")
axes[0, 0].set_title("Temperature Over Time")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (°C)")
axes[0, 0].tick_params(axis='x', rotation=45)
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].scatter(df["Humidity"], df["Temperature"], color="purple", s=70, alpha=0.8)
axes[0, 1].set_title("Temperature vs. Humidity")
axes[0, 1].set_xlabel("Humidity (%)")
axes[0, 1].set_ylabel("Temperature (°C)")
axes[0, 1].grid(True, alpha=0.3)

corr = round(df["Temperature"].corr(df["Humidity"]), 2)
print(f"Correlation (Temperature, Humidity): {corr}")

axes[1, 0].pie(condition_counts.values, labels=condition_counts.index, autopct="%1.1f%%", startangle=90, colors=["#ff9999","#66b3ff","#99ff99"])
axes[1, 0].set_title("Weather Condition Share")

axes[1, 1].hist(df["Temperature"], bins=5, color="teal", edgecolor="white")
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (°C)")
axes[1, 1].set_ylabel("Frequency")
axes[1, 1].grid(axis="y", alpha=0.3)

fig.suptitle("Weather Overview", fontsize=16)
plt.tight_layout()
plt.savefig("weather_dashboard.png")
plt.show()