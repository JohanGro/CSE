import csv

items = {}

with open("SalesRecords.csv", "r") as old_csv:
    print("Writing...")
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        if row[0] == 'Region':
            continue
        object_sold = row[2]
        profits = row[13]
        if object_sold in items:
            items[object_sold] += float(profits)
        else:
            items[object_sold] = float(profits)
print(sorted(items.values()))
