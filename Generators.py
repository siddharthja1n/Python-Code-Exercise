# Generators in Python
# CWH Tut
# Fibonacci and factorial using generators



def fibonaccI(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

def factoriaL(n):
    a = 1
    for i in range(1, n+1):
        yield a*i
        a = a*i

num = int(input("Enter a number: "))

print("Factorial")
fac = factoriaL(num)
for i in fac:
    print(i)
    
print("Fibonacci")
fib = fibonaccI(num)
for i in fib:
    print(i)