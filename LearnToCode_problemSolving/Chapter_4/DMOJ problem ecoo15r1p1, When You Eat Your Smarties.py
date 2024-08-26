#DMOJ problem ecoo15r1p1, When You Eat Your Smarties
string = input()
time = 0
handfulRed = 0
handfulOrange = 0 
handfulGreen = 0
handfulYellow = 0
handfulPink = 0
handfulViolet = 0
handfulBrown = 0
handfulBlue = 0
while string != 'end of box':
    if string == 'red':
        handfulRed += 1
    elif string == 'blue':
        handfulBlue += 1 
    elif string == 'brown':
        handfulBrown += 1 
    elif string == 'pink':
        handfulPink += 1 
    elif string == 'violet':
        handfulViolet += 1 
    elif string == 'orange':
        handfulOrange += 1 
    elif string == 'yellow':
        handfulYellow += 1 
    elif string == 'green':
        handfulGreen += 1
    string = input()

time = 13*(math.ceil(handfulBlue/7)) + 13*(math.ceil(handfulBrown/7)) + 13*(math.ceil(handfulGreen/7)) + 13*(math.ceil(handfulPink/7)) \
    + 16*handfulRed + 13 *(math.ceil(handfulOrange/7)) + 13*(math.ceil(handfulViolet/7)) + 13*(math.ceil(handfulYellow/7))
print(time)
