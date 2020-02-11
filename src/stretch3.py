from math import ceil

def prime(n):
    iterations = 0
    if n <= 1:
        return False
    
    for x in range(2, int(ceil(n / 2)) + 1):
        for y in range(2, x + 1):
            print(x,y)
            iterations += 1
            if x * y == n:
                return (False, iterations)
            
            if x * y > n:
                break
                
    return (True, iterations)
     
     
n = int(input("Enter a number: "))
result = prime(n)
print(f"is prime: {result[0]} iterations: {result[1]}")