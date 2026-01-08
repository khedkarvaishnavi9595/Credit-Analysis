import pandas as pd

# Step 1: Read the Excel file
df = pd.read_excel("Credit.xlsx")

# Step 2: Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Step 3: Remove duplicate rows
df = df.drop_duplicates()

# Step 4: Handle missing values
# Drop rows where all values are completely missing
df = df.dropna(how="all")

# Fill remaining missing values
df = df.fillna("Not Available")

# Step 5: Remove extra spaces from text columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# Step 6: Save cleaned data to a new Excel file
df.to_excel("Credit_Cleaned.xlsx", index=False)

print("Credit.xlsx cleaned successfully and saved as Credit_Cleaned.xlsx")
