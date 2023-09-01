lst=['1001','0011','0101','1011','1101','1111']
converted=[]
for i in lst:
    d=int(i,2)
    converted.append(d)
converted.sort()
print(converted)
while len(converted)>2:
    i=0
    converted.append(converted[i]+converted[i+1])
    converted.remove(converted[i])
    converted.remove(converted[i])
    converted.sort()
print(f'The two digits left in the list are = {converted}')
lstdiff = converted[1]-converted[0]
print(f"The least difference is = {lstdiff}")
