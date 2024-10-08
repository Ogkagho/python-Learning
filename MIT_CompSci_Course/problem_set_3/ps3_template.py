
# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'



### the following procedure you will use in Problem 3

def subStringMatchExact(targString, keyString):
    points = ()
    s = 0   #initial start 0 
    while s != -1:  #ensures loop terminates if s is larger than targetstring
        s = targString.find(keyString, s) #finds index of substring occurrence 
        points += (s,)
        if s == -1:
            points = points[0:-1]
            return points 
        s += 1   #moves start to the next index, based on previous found index

def constrainedMatchPair(firstMatch, secondMatch, length):
    tu = ()
    for i in firstMatch:
        if i + length + 1 in secondMatch:
            tu += (i,)
    return tu 

 

def subStringMatchOneSub(key, target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0, len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print('breaking key', key, 'into', key1, key2)
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target, key1)
        match2 = subStringMatchExact(target, key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1, match2, len(key1))
        allAnswers = allAnswers + filtered
        print('match1', match1)
        print('match2', match2)
        print('possible matches for', key1, key2, 'start at', filtered)
    return allAnswers

# Example calls to test the function
print(subStringMatchOneSub(key11, target1))
print(subStringMatchOneSub(key12, target2))



    







            



