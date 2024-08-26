#DMOJ problem ccc20j2, Epidemiology

p = int(input()) #condition, when a total of more than p have the disease
hadDiseaseDay0 = int(input()) #had the disease Day 0
infect = int(input()) # how many people each person infects 
i = 0  #day 0
TotalhadDisease = hadDiseaseDay0

while TotalhadDisease <= p:
    i += 1
    TotalhadDisease += hadDiseaseDay0*infect**i
    
print(i)
