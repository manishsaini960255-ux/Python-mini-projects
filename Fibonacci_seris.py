num = int(input("Enter number of terms:"))

a = 0
b = 1
i = 1

while i <= num:
    
    print(a)
    c = a+b
    b = a
    a = c
    i += 1
    
    