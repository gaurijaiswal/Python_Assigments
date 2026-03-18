import pandas as pd

# Read CSV file
df = pd.read_csv("books.csv")

# a) Print complete report
print("Complete Books Report:\n", df)

# b) Books by given author
author = input("Enter author name: ")
print("\nBooks by Author:\n", df[df['author'] == author])

# c) Books by publishing house
pub = input("Enter publishing house: ")
print("\nBooks by Publisher:\n", df[df['publishing_house'] == pub])

# d) Cheapest & costliest book titles
print("\nCheapest Book:\n", df[df['price'] == df['price'].min()]['title'])
print("Costliest Book:\n", df[df['price'] == df['price'].max()]['title'])

# e) Sort by publication year
print("\nSorted by Year:\n", df.sort_values(by='publication_year'))