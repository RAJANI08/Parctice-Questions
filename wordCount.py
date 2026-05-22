str="apple banana apple mango banana apple"

l=str.split(" ") # list 

##########  list to dictionary ##############

key=[]
for i in range(len(l)):
    key.append((l[i],l.count(l[i])))

d=dict(key)
print(d)


##########  using dictionary ##############


d1={}

for i in range(len(l)):
    d1[l[i]]=l.count(l[i])

print(d1)