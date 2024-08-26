#DMOJ problem ccc02j2, AmeriCanadian
string = input()

while string != 'quit!':
    if len(string) >= 4 and string[len(string)-2:] == 'or' and string[len(string)-3] not in 'aeiouy':
        print(string[:-2] + 'our')
    else:
        print(string)
    string = input()
