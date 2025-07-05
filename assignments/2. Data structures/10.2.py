# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by
#  hour of the day for each of the messages. You can pull the hour out from the 'From ' line by 
# finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hourscount = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        hour = words[5].split(":")[0]
        hourscount[hour] = hourscount.get(hour,0) + 1

for x,y in sorted(hourscount.items()):
    print(x,y)
        