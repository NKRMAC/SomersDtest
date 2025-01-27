import pandas as pd
import numpy as np
from scipy.stats import somersd

gen = False

def manual_somers_d(x, y):
    # Initialize counts
    C = 0
    D = 0
    T_Y = 0

    # Calculate concordant, discordant pairs and ties in X and Y
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] < x[j] and y[i] < y[j]:
                C += 1
            elif x[i] > x[j] and y[i] > y[j]:
                C += 1
            elif x[i] < x[j] and y[i] > y[j]:
                D += 1
            elif x[i] > x[j] and y[i] < y[j]:
                D += 1
            elif y[i] == y[j] and x[i] != x[j]:
                T_Y += 1

    # Calculate Somers' D
    return (C - D) / (C + D + T_Y)


if gen:
    # Generate data
    np.random.seed(0)
    x = np.random.rand(1000) * 1.1
    y = np.random.rand(1000) * 1.1

    # Adjust y to achieve Somers' D of 0.5
    y = np.where(x > 0.5, y + 0.5, y)
    y = np.clip(y, 0, 1.1)  # Ensure y is within the range [0, 1.1]

    # Create DataFrame
    df = pd.DataFrame({'x': x, 'y': y})

    # Define custom bins and labels
    bins = [0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1]
    labels = [str(i) for i in range(1, 13)]

    # Group x and y
    df['x_group'] = pd.cut(df['x'], bins=bins, labels=labels, include_lowest=True).cat.codes
    df['y_group'] = pd.cut(df['y'], bins=bins, labels=labels, include_lowest=True).cat.codes
    df['y_binarized'] = pd.cut(df['y'], bins=[0, 0.6, 1.1], labels=[0, 1], include_lowest=True).cat.codes

    # Save DataFrame to CSV
    df.to_csv('somersd.csv', index=False)
else:
    # Load data from CSV
    df = pd.read_csv('somersd.csv')

# Calculate Somers' D on grouped data
grouped_somers_d = somersd(df['x_group'], df['y_group'])
print(f"Somers' D on grouped data: {grouped_somers_d.statistic}")
print(f"Manual Somers' D: {manual_somers_d(df['x_group'], df['y_group'])}")

print("And now with binary target")

# Calculate Somers' D on binary target
binary_somers_d = somersd(df['x_group'], df['y_binarized'])
print(f"Somers' D on binary target: {binary_somers_d.statistic}")
print(f"Manual Somers' D: {manual_somers_d(df['x_group'], df['y_binarized'])}")

print("Reversing the polarity...")
binary_somers_d = somersd(df['y_binarized'], df['x_group'])
print(f"Somers' D on binary target: {binary_somers_d.statistic}")
print(f"Manual Somers' D: {manual_somers_d(df['y_binarized'], df['x_group'])}")

