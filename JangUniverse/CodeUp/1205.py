a, b = map(int, input().split())
s = a+b
e = abs(a-b)
x = a * b
p = a / b
q = a**b
r = b**a
c = b / a
#배운거: print(f"{value:.2f}")   # 출력: 3.10 ← 이런 게 "강제로 자리수 고정 출력"
print(f"{max(s, e, x, p, q, r, c):.6f}")