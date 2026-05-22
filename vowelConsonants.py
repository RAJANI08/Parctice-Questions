str=input("Enter the string; ").lower()

l=["a","e","i","o","u"]
count=0         # vowels count
count1=0        # consonants count
flag=True

for i in range(len(str)):   # to consider only alphabets
    if(not(ord(str[i])>=97 and ord(str[i])<=123)):         
          flag=False
          break
    else:        
        if str[i] in l:
            count=count+1
        else:
            count1=count1+1
if(flag==True):
    print("vowels", count)
    print("consonants", count1)
else:
    print("please enter alphabets only")