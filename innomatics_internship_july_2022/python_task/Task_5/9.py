import re
n = int(input())
for i in range(n):
    name, email = input().split(' ')
    check = re.match(r'<[a-zA-Z][\w\.-]*@[a-zA-Z]*\.[a-zA-Z]{1,3}>', email)
    if check:
        print(name, email)