def caliculate(a: int):
    return a**2
print("power of the value a=",caliculate(6))

def power_n(a: int):
    i=0
    n=int(input("enter the value of n"))
    while i<=n:
        power=a**i
        i=i+1
    return power
print("the value of a to the power of n is=",power_n(5))