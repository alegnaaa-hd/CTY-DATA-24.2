
def somme_kaylin(n):
    if n < 0:
        return n + somme_kaylin(n + 1)
    elif n > 0:
        return n + somme_kaylin(n-1)
    else:
        return 0
    
def factorial_for_loop(n):
    if n < 0:
        n = n * (-1)
    result = 1
    for i in range(2,n+1):
        result = result * i
    return result 

def somme(n):
    if n < 0:
        return somme(n * (-1))
    elif n == 0:
        return 0
    else:
        return n + somme(n-1)
def fact(n):

    # print("Computing factorial of ", n)
    if n < 0:
        print("Can't do it")
    elif n == 0 or n== 1:
        return 1
    else:
        return n * fact(n-1)
def fibonacci_alec(n):
    if n==0  or 1:
        if n == 0:
            return 0
        else:
            return 1
    else:
        return fibonacci_alec(n-1) + fibonacci_alec(n-2)
print("Factorial of -1 is ", fact(-1))


