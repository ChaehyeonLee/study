import re

datafile = open('regex_sum_83497.txt').read()

sum = 0

stuff = re.findall('[0-9]+', datafile)

for digit in stuff:
    sum += int(digit)

print(sum)