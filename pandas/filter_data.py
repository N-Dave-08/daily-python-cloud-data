import pandas as pd

# Sample data as a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'Los Angeles', 'Chicago', 'New York']}
df = pd.DataFrame(data)

# Add 'Senior' column
df['Senior'] = df['Age'] >= 30

# Filter rows where Age > 28
filtered_df = df[(df['Senior'] == True)]

# Print the filtered DataFrame
print(filtered_df)

# Print the shape of the filtered DataFrame
print(filtered_df.shape)