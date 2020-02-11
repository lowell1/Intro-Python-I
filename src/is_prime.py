from math import ceil

def prime(n):
    if n <= 1:
        return False
    
    for x in range(2, int(ceil(n / 2)) + 1):
        if n % x == 0:
            return False
                
    return True
     
     
n = int(input("Enter a number: "))
result = prime(n)
print(f"{n} is prime" if result else f"{n} is composite")