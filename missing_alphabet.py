'''find the missing letter from the given sentence'''
s=input()
a="abcdefghijklmnopqrstuvwxyz"
ans=''
for i in a:
    if i not in s:
        ans=ans+i
print(ans)
