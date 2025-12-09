import pandas as pd
import numpy as np

data = {
    'Name': ['Ali', 'Ahmad', 'Sara', 'Reza', 'Narges'],
    'Age': [25, 30, 22, 35, 28],
    'Height': [174, 191, 168, 178, 159],
    'Weight': [69, 88, 65, 94, 57],
    'Gender': ['Male', 'Male', 'Female', 'Male', 'Female'],
    'Hobby': ['Music', 'Sports', 'Movies', 'History', 'Travel'],
    'City': ['Tehran', 'Shiraz', 'Esfahan', 'Tabriz', 'Mashhad'],
    'Education': ['Bachelor', 'Master', 'PhD', 'Bachelor', 'Master'],
    'MaritalStatus': ['Single', 'Married', 'Single', 'Married', 'Single']
}

df = pd.DataFrame(data)

print("=" * 60)
print("DATA")
print("=" * 60)
print(df.to_string(index=False))
print("\n" + "=" * 60)
print("STATISTICAL RESULTS")
print("=" * 60)


print("\n1. MEAN AND MEDIAN:")
print("-" * 30)
for col in ['Age', 'Weight']:
    mean_val = df[col].mean()
    median_val = df[col].median()
    print(f"{col}:")
    print(f"  Mean: {mean_val:.2f}")
    print(f"  Median: {median_val:.2f}")

# 2. Mode for Height, Gender, and Education
print("\n2. MODE:")
print("-" * 30)
for col in ['Height', 'Gender', 'Education']:
    modes = df[col].mode()
    print(f"{col}:")
    if len(modes) == 1:
        print(f"  Mode: {modes.iloc[0]}")
    else:
        print(f"  Multiple modes: {', '.join(map(str, modes.tolist()))}")

# 3. Range for Age, Height, and Weight
print("\n3. RANGE:")
print("-" * 30)
for col in ['Age', 'Height', 'Weight']:
    data_min = df[col].min()
    data_max = df[col].max()
    data_range = data_max - data_min
    print(f"{col}:")
    print(f"  Min: {data_min}")
    print(f"  Max: {data_max}")
    print(f"  Range: {data_range}")

# 4. Variance and Standard Deviation
print("\n4. VARIANCE AND STANDARD DEVIATION:")
print("-" * 30)
for col in ['Age', 'Height', 'Weight']:
    var_val = df[col].var(ddof=1)
    std_val = df[col].std(ddof=1)
    print(f"{col}:")
    print(f"  Variance: {var_val:.4f}")
    print(f"  Standard Deviation: {std_val:.4f}")

# 5. Quartiles
print("\n5. QUARTILES:")
print("-" * 30)
for col in ['Age', 'Height', 'Weight']:
    q1 = df[col].quantile(0.25)
    q2 = df[col].quantile(0.50)
    q3 = df[col].quantile(0.75)
    print(f"{col}:")
    print(f"  First Quartile (Q1): {q1:.2f}")
    print(f"  Second Quartile (Q2/Median): {q2:.2f}")
    print(f"  Third Quartile (Q3): {q3:.2f}")

# 6. Interquartile Range (IQR)
print("\n6. INTERQUARTILE RANGE (IQR):")
print("-" * 30)
for col in ['Age', 'Height', 'Weight']:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    print(f"{col}:")
    print(f"  Q1: {q1:.2f}")
    print(f"  Q3: {q3:.2f}")
    print(f"  IQR: {iqr:.2f}")

print("\n" + "=" * 60)
print("CALCULATION COMPLETED")
print("=" * 60)