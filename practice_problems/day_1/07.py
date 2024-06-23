n = int(input("Enter the number of terms you want to print: "))
n1 = 0
n2 = 1
l1 = []
if (n >= 1):
    l1.append(n1)
if (n >= 2):
    l1.append(n2)
for i in range (n-2):
    l1.append((l1[i]+l1[i+1]))
print(l1)