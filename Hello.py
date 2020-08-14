fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
di = dict()
time = []
for line in fh:
    line = line.strip()
    if not line.startswith('From '): continue
    count += 1
    words = line.split()
    time = words[-2].split(":")
#    print(time)

    if time[0] not in di:
        di[time[0]] = 1

    else:
        di[time[0]] += 1
#print(di)



di_items = di.items()
sorted_di = sorted(di_items)


for k,v in sorted_di:
    print(k,v)

