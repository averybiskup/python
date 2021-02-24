import csv

path = '../../personal/money.csv'

# with open(path, 'w') as s:
    # write = csv.writer(s, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # write.writerow(['John Smith', 'Accounting', 'November'])
    # write.writerow(['Erica Meyers', 'IT', 'March'])


with open(path, 'r') as s:
    reader = csv.DictReader(s)

    line_count = 0
    for row in reader:
        print(row['name'])
