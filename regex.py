import re
fhandle = open('sum.txt')

add = 0

for line in fhandle :
    numlist = []
    numlist = re.findall('[0-9]+',line)
    for num in numlist :
        num = int(num)
        add = add + num

print(add)

def sum(list) :
    add = 0
    for item in list :
        item = int(item)
        add = add + item
    return add

print(sum(re.findall('[0-9]+',open('sum.txt').read())))

print()
input("Press any key to continue........")
