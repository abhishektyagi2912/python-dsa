n = int(input("Enter the value of n: "))
a = int(input("Enter the value of a: "))
d = int(input("Enter the value of d: "))

i = 1
while i < n+1:
   v = 1/(a + (i - 1) * d)
   print(v, end=" ")
   i = i + 1
