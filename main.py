number1 = int(input("What's the number 1? "))
number2 = int(input("What's the number 2? "))

def gcd(p,q):
    r = p%q
    if(r == 0):
        return q
    return gcd(q,r)

_gcd = gcd(number1,number2)

def lcm(p,q):
    return _gcd*(p/_gcd)*(q/_gcd)

print(lcm(number1,number2))