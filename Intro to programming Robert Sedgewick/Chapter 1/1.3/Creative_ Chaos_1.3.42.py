#Chaos
#Compose a program to study the following simple model for population growth, which might be applied to study fish in a pond, bacteria in a test 
#tube, or any of a host of similar situations. We suppose that the population ranges 
#from 0 (extinct) to 1 (maximum population that can be sustained). If the popula
#tion at time t is x, then we suppose the population at time t + 1 to be rx(1-x), where 
#the parameter r, known as the fecundity parameter, controls the rate of growth. 
#Start with a small population—say, x = 0.01—and study the result of iterating the 
#model, for various values of r. For which values of r does the population stabilize at 
#x = 1 - 1/r ? Can you say anything about the population when r is 3.5? 3.8? 5?

#1.3.42

x = 0.01 #float(input('Enter: '))
r = float(input('Enter: '))
t = 0
stabilize = 1 - 1/r
#and t < 70
while x > 0 and x <=1:
    x = r*x*(1-x)
    print(x)
    if abs(x - stabilize) < 1e-8:
        print(r)
        break
    t += 1
    
#Note; interesting things happen for those values
