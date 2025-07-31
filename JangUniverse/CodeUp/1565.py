n, m = map(int, input().split())
def gcd(p,q):
    if p == 0:
        return q
    else:
        return gcd(q%p, p)

def lcm(p, q):
    x = gcd(p, q)
    return int(p/x)*int(q/x)*x

print(lcm(n,m))