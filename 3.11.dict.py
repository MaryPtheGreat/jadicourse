from collections import OrderedDict

# Read the number of votes
n = int(input())

# Initialize an empty list to store the countries
countries = []

# Read the countries and add them to the list
for _ in range(n):
    country = input().strip().lower()
    countries.append(country)

# Use OrderedDict to store the count of votes for each country
votes_count = OrderedDict()

# Count the votes for each country
for country in countries:
    votes_count[country] = votes_count.get(country, 0) + 1

# Sort the items alphabetically and print the count of votes for each country
for country, count in sorted(votes_count.items()):
    print(f"{country} {count}")

