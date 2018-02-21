import csv
int_list = []
final_list = []
with open('marks_list.csv','rb') as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        int_list.append(map(int, row))

for i in int_list:
    final_list.append(i[1])

topper = max(final_list)

for itr in range(len(final_list)):
    if final_list[itr] == topper:
        final_list[itr] = 1
    else:
        topper = topper - 1
        print topper
print final_list