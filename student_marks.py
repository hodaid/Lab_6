import pandas as pd
import matplotlib.pyplot as plt

raw = {
    "Name": [" ali", "SARA ", "bilal", " Ayesha", "HAMZA", "zain ", "Noor", " usman "],
    "Marks": ["72", "85", "absent", "64", "90", "78", "81", "69"]
}

df = pd.DataFrame(raw)

df["Name"] = df["Name"].str.strip().str.title()


df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)


print("Cleaned Student Marks DataFrame:")
print(df)

plt.figure(figsize=(7, 4))
plt.bar(df["Name"], df["Marks"], color="skyblue", edgecolor="steelblue")
plt.title("Student Marks Bar Plot")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("marks_bar.png")
plt.show()