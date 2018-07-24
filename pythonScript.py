from collections import Counter
import itertools

longFile = "D:/Java/JavaHomework_2/python.html"
shortFile = "D:/data.txt"
ultraShortFile = "D:/data1.txt"

f = open(ultraShortFile, 'r')

arr = []

for lines in f.readlines():
    words = lines.split()
    for word in words:
        arr.append(word)

print Counter(arr).most_common()[0]


f.close()
