from collections import Counter
import re


longFile = "D:/Java/JavaHomework_2/python.html"
shortFile = "D:/data.txt"
ultraLongFile = "D:/data1.txt"

f = open(shortFile, 'r')

for lines in f.readlines():
    words = lines.split()
    print Counter(words).most_common()[0]

f.close()
