s = input()
def palidrom(s):
    return s == s[::-1]
found = False
for i in range(4):
    temp = s[:i] + s[i+1:]
    if palidrom(temp):
        print(s[:i])
        print(s[i+1:])
        print (temp)
        found = True
        break
print("YES" if found else "NO")