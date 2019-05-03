import csv


def validate(num: int):
    num = list(num)
    if len(num) == 16:
        last_num = num[15]
        num.pop(15)
        num = num[:: - 1]
        odds = num[0:15:2]
        even = num[1:15:2]
        o = 0
        for i in odds:
            odds[o] = int(odds[o])
            odds[o] *= 2
            if int(odds[o]) >= 10:
                odds[o] = int(odds[o]) - 9
                o += 1
            else:
                o += 1
        oddadd = int(odds[0]) + int(odds[1]) + int(odds[2]) + int(odds[3]) + int(odds[4]) + int(odds[5]) + int(odds[6])\
            + int(odds[7])
        evenadd = int(even[0]) + int(even[1]) + int(even[2]) + int(even[3]) + int(even[4]) + int(even[5]) + int(even[6])
        allnum = oddadd + evenadd
        if int(allnum) % 10 is int(last_num):
            return True
        else:
            return False
    return False


with open("Book1.csv", "r") as old_csv:
    with open("File.csv", "w") as new_csv:
        with open("FakeFile.csv", "w") as fake_csv:
            reader = csv.reader(old_csv)
            writer = csv.writer(new_csv)
            writer2 = csv.writer(fake_csv)
            print("Processing...")

            for row in reader:
                old_number = row[0]
                if validate(old_number) is True:
                    writer.writerow(row)
                if validate(old_number) is False:
                    writer2.writerow(row)
print("Done!")
