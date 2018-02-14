import csv
int_list = []
final_list = []
with open('Demo.csv','rb') as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        int_list.append(map(int, row))

for i in int_list:
    final_list.append(i[1])
print final_list