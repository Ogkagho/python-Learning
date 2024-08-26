#Birthday problem. Suppose that people continue to enter an empty room 
#until a pair of people share a birthday. On average, how many people will have to 
#enter before there is a match? Run experiments to estimate the value of this quan
#tity. Assume birthdays to be uniform random integers between 0 and 364.

#1.4.36
#Birthday problem
import random 

trials = int(input())
count1= 0
for t in range(trials):
    count = 0
    birthdays = [0]*365
    while sum(birthdays) < 364:
        r = random.randrange(1, 365)
        birthdays[r] += 1 
        count += 1
        if birthdays[r] == 2:
            break 
    if 2 in birthdays:
        count1 += count 

print(count1/trials)

