s=input()
result=int(s[0])

#1
# for i in range(1,len(s)):
#     if result*int(s[i])>result+int(s[i]):
#         result=result*int(s[i])
#     else:
#         result=result+int(s[i])

# print(result)

#2
for i in range(1, len(s)):
    num = int(s[i])
    result = max(result + num, result * num)

print(result)