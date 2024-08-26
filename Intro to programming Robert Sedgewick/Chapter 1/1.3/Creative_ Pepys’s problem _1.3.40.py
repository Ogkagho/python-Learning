#Pepys's problem
#In 1693 Samuel Pepys asked Isaac Newton which is more 
#likely: getting 1 at least once when rolling a fair die six times or getting 1 at least 
#twice when rolling it 12 times. Compose a program that could have provided New
#ton with a quick answer

#1.3.40


#How many times to run the simulation
n = int(input('Enter: '))
six = 0
twelve = 0
for i in range(n+1):
    ones6 = 0
    for j in range(6):
        if random.randrange(1, 7) == 1:
            ones6 += 1
            if ones6 == 1:
                six += 1
                break
    
    ones12 = 0
    for j in range(12):
        if random.randrange(1, 7) == 1:
            ones12 += 1 
            if ones12 == 2:
                twelve += 1
                break
    
prob6 = 100 * (six / n)
prob12 = 100 * (twelve / n)

stdio.writeln('Getting 1 at least once when rolling a fair die six times: ' 
              + str(prob6) + '%')
stdio.writeln('Getting 1 at least once when rolling a fair die twelve times: ' 
              + str(prob12) + '%')
