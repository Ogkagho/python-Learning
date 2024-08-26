#DMOJ problem ccc00s1 Slot Machines
n = int(input())

slot1Prev = int(input())
slot2Prev = int(input())
slot3Prev = int(input())
slot1 = True
slot2 = False
slot3 = False

MarthaPlay = 0

while n > 0:
    MarthaPlay += 1
    n -= 1
    if slot1:
        slot1Prev += 1
        if slot1Prev % 35 == 0:
            n += 35
        slot1 = False
        slot2 = True
    elif slot2:
        slot2Prev += 1
        if slot2Prev % 100 == 0:
            n += 60
        slot2 = False
        slot3 = True
    elif slot3:
        slot3Prev += 1
        if slot3Prev % 10 == 0:
            n += 9
        slot3 = False
        slot1 = True 
    
print('Martha plays', MarthaPlay ,'times before going broke.')
