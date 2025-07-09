# Program to extract the numbers in a file and calculate the sum of numbers using reqular expressions.
# Using sample1.txt and actual1.txt

import re

file_name = input("Enter the file name: ")

# fh = open(file_name)

# listnums= re.findall('[0-9]+', fh.read())

# total = 0
# for num in listnums:
#     total = total + int(num)

# print(total, len(listnums))

print(sum([int(x) for x in re.findall('[0-9]+', open(file_name).read())]))