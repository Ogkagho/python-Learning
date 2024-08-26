#DMOJ problem ccc06j1, Canadian Calorie Counting
#Don't put prompts for DMOJ

burger = int(input('Enter: '))
sideOrder = int(input('Enter: '))
drinks = int(input('Enter: '))
dessert = int(input('Enter: '))

totalCalories = 0

if burger == 1:
    totalCalories += 461
elif burger == 2:
    totalCalories += 431
elif burger == 3:
    totalCalories += 420
else:
    totalCalories += 0 

if sideOrder == 1:
    totalCalories += 100
elif sideOrder == 2:
    totalCalories += 57
elif sideOrder == 3:
    totalCalories += 70
else:
    totalCalories += 0

if drinks == 1:
    totalCalories += 130
elif drinks == 2:
    totalCalories += 160
elif drinks == 3:
    totalCalories += 118
else:
    totalCalories += 0

 
if dessert == 1:
    totalCalories += 167
elif dessert == 2:
    totalCalories += 266
elif dessert == 3:
    totalCalories += 75
else:
    totalCalories += 0

print(totalCalories)

