name1="joshua nikhil"
name2= "hyfutfkvvgn"

name3=[]
name4=[]

for i in range (0,len(name1)):
    name3.append(name1[i])
print(name3)

for j in range (0,len(name2)):
    name4.append(name2[j])
print(name4)

for i in range (0,len(name3)):
    for j in range(len(name4)):
        if name3[i]==name4[j]:
            name3[i]=' '
            name4[j]=' '

print(name3)
c=[]
d=[]
a=list(name3)
print(a)
print(list(name4)) 
b=list(name4)  
for i in range (0,len(a)):
    print(a[i])
    if(a[i]==' '):
        c.append(i)
count = 0
for i in c:
    if(count>0):
        i = i - count
    print(i)
    a.pop(i)
    count = count+1

for i in range (0,len(b)):
    if(b[i]==' '):
        d.append(i)
count = 0
for i in d:
    if(count>0):
        i = i - count
    b.pop(i)
    count=count+1

print(a)
print(b)
count=len(a)+len(b)
print(count)

result=['FRIEND','LOVER','AFFECTION','MARRIAGE','ENEMY','SISTER']
 
while len(result) > 1:
        print(len(result))
        # store that index value from
        # where we have to perform slicing.
        split_index = (count % len(result) - 1)
 
        # this steps is done for performing
        # anticlock-wise circular fashion counting.
        if split_index >= 0:
 
            # list slicing
            right = result[split_index + 1:]
            left = result[: split_index]
 
            # list concatenation
            result = right + left
 
        else:
            result = result[: len(result) - 1]
            print(result)
 
    # print final result
print("Relationship status :", result[0])
