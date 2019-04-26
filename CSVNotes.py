import csv


def validate(num: str):
    first_num = int(num[0])
    second_num = int(num[1])
    if first_num in (0, 2, 4, 6, 8):
        if second_num in (1, 3, 5, 7, 9):
            return True
    return False
#  with open("Book1.csv", "r") as old_csv:
#   reader = csv.reader(old_csv)
#    for row in reader:
#        old_number = int(row[0]) + 1
#        print(old_number)


with open("Book1.csv", "r") as old_csv:
    with open("MyNewFile.csv", "w") as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)
        print("OK")
