introstring=input("enter your introduction")
ccount=0
wcount=1
for i in introstring:
    ccount=ccount+1
    if(i== ' '):
        wcount=wcount+1
print("number of character in the string")
print(ccount)

print("number of words in the string")
print(wcount)


