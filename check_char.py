str1="aaabbbccczzzr"
char=str1[0]
print(char)
count=0
output=""
for ch in str1:
    if ch==char:
        count=count+1
    else:
        output=output+str(count)+ch
        count=1
        char=ch
output=output+str(count)+ch
print(output)

