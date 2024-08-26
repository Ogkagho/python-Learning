#Wind chill

#1.2.22

temp = float(input('Enter the temperature: '))
speed = float(input('Enter the speed: '))

while abs(temp) > 50 or (speed > 120 or speed < 3):
    if abs(temp) > 50:
        print('The program only works for absolute values of temperature ', end="")
        print(' greater than 50')
    else:
        print("The program only works for absolute values of speed ", end=" ")
        print("less than 120 and greater then 3")
    
    print("Re-enter the values")
    temp = float(input('Enter the temperature: '))
    speed = float(input('Enter the speed: '))

w = 35.74 + 0.6215 * temp + (0.4275*temp - 35.75)*(speed**0.16)

print("The wind chill is ", w)
