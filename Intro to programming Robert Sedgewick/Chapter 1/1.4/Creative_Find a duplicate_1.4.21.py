#Find a duplicate. Given an array of n elements with each element between 
#1 and n, compose a code fragment to determine whether there are any duplicates. 
#You do not need to preserve the contents of the given array, but do not use an extra 
#array

#1.4.29

a = [1, 5, 1, 3]
found = False
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            found = True 
            break 
    if found:
        break 
if found:
    print('There\'s a duplicate.')
else:
    print('No duplicate')

