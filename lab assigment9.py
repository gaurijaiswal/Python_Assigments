import pandas as pd

# Create DataFrame
data = {
    'State': ['Maharashtra', 'Gujarat', 'UP', 'Karnataka', 'Tamil Nadu'],
    'Area': [307713, 196024, 243286, 191791, 130058],
    'Population': [124000000, 70000000, 240000000, 68000000, 75000000]
}

df = pd.DataFrame(data)

# a) Complete info
print(df)

# b) Largest area
print("\nState with Largest Area:", df.loc[df['Area'].idxmax(), 'State'])

# c) Largest population
print("State with Largest Population:", df.loc[df['Population'].idxmax(), 'State'])

# d) Population density
df['Density'] = df['Population'] / df['Area']
print("\nWith Density:\n", df)

# e) Highest density
print("\nHighest Density State:", df.loc[df['Density'].idxmax(), 'State'])