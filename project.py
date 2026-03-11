import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("cloud_jobs.csv")

# Show the full data
print("Job Data:")
print(df)

# Count cloud platforms
cloud_counts = df["Cloud"].value_counts()
print("\nCloud Platform Counts:")
print(cloud_counts)

# Count skills
skill_counts = df["Skill"].value_counts()
print("\nSkill Counts:")
print(skill_counts)

# Count roles
role_counts = df["Role"].value_counts()
print("\nRole Counts:")
print(role_counts)

# Make cloud chart
cloud_counts.plot(kind="bar")
plt.title("Cloud Platform Demand")
plt.xlabel("Cloud Platform")
plt.ylabel("Number of Jobs")
plt.show()

# Make skill chart
skill_counts.plot(kind="bar")
plt.title("Top Technical Skills")
plt.xlabel("Skill")
plt.ylabel("Number of Jobs")
plt.show()