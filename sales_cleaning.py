import pandas as pd

# ==========================
# STEP 1: LOAD DATASET
# ==========================

df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")

# ==========================
# STEP 2: DATA PROFILING
# ==========================

print("===== MISSING VALUES BEFORE CLEANING =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

print("\n===== DATA TYPES BEFORE CLEANING =====")
print(df.dtypes)

# ==========================
# STEP 3: HANDLE MISSING VALUES
# ==========================

# Fill missing Age values with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing City values with Unknown
df["City"] = df["City"].fillna("Unknown")

# ==========================
# STEP 4: REMOVE DUPLICATES
# ==========================

df = df.drop_duplicates()

# ==========================
# STEP 5: CONVERT DATE FORMAT
# ==========================

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# ==========================
# STEP 6: FEATURE ENGINEERING
# ==========================

# Create Month column
df["Month"] = df["Order_Date"].dt.month_name()

# Create Year column
df["Year"] = df["Order_Date"].dt.year

# Create Age Group column
bins = [0, 18, 30, 45, 60, 100]

labels = [
    "Teen",
    "Young Adult",
    "Adult",
    "Middle Age",
    "Senior"
]

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)

# ==========================
# STEP 7: VERIFY CLEANING
# ==========================

print("\n===== MISSING VALUES AFTER CLEANING =====")
print(df.isnull().sum())

print("\n===== DATA TYPES AFTER CLEANING =====")
print(df.dtypes)

print("\n===== COLUMN NAMES =====")
print(df.columns)

print("\n===== FIRST 5 ROWS =====")
print(df.head())

# ==========================
# STEP 8: SAVE CLEANED DATASET
# ==========================

df.to_excel(
    "Cleaned_Sales_Dataset.xlsx",
    index=False
)

print("\nDataset cleaned successfully!")
print("File saved as Cleaned_Sales_Dataset.xlsx")