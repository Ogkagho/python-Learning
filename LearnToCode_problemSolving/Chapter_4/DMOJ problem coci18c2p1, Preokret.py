#DMOJ problem coci18c2p1, Preokret

#solution not to my liking, will try again

teamA = int(input())
teamAsec = [0.0]*(teamA+1)
sum1 = 0
for i in range(1,teamA+1):
    teamAsec[i] = int(input())
    sum1 += teamAsec[i]
    if sum1 < 1440:
        pointsA = i
    
teamB = int(input())
teamBsec = [0.0]*(teamB+1)
sum1 = 0
for i in range(1,teamB+1):
    teamBsec[i] = int(input())
    sum1 += teamBsec[i]
    if sum1 < 1440:
        pointsB = i

print(pointsA + pointsB)

pointA = 0
pointB = 0 
turnAround = -1
time = 0
if teamAsec[1] < teamBsec[1]:
    currentleader = 'A'
else:
    currentleader = 'B'
    
while time <= 2880:
    if time in teamAsec:
        pointA += 1
    if time in teamBsec:
        pointB += 1 
        
    if pointA > pointB and currentleader != 'A':
        currentleader = 'A'
        turnAround += 1
    if pointB > pointA and currentleader != 'B':
        currentleader = 'B'
        turnAround += 1
        
    if pointA > pointB:
        currentleader = 'A'
    elif pointA < pointB:
        currentleader = 'B'
    else:
        currentleader = None
    

    time += 1 

print(turnAround)

