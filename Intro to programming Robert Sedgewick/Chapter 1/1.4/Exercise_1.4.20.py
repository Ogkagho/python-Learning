#Run experiments to validate this calculation simulating n dice throws, keeping 
#track of the frequencies of occurrence of each value when you compute the sum 
#of two random integers between 1 and 6. How large does n have to be before your 
#empirical results match the exact results to three decimal places?

#1.4.20
#Dice simulation
import stdarray


throws = int(input())

sums = stdarray.create1D(13, 0)

for t in range(throws):
    dice_1 = random.randrange(1, 7)
    dice_2 = random.randrange(1, 7)
    sum1 = dice_2 + dice_1 
    sums[sum1] += 1 

for i in range(2, 13):
    sums[i] /= throws
    
probabilities = stdarray.create1D(13, 0.0) 
for i in range(1, 7): 
    for j in range(1, 7): 
        probabilities[i+j] += 1.0 
for k in range(2, 13): 
    probabilities[k] /= 36

compare = stdarray.create1D(13, 0)

for i in range(13):
    compare[i] = abs(sums[i] - probabilities[i])

