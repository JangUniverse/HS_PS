n=input()
k=int(n[1])*10+int(n[0])
print(((k*2)%100))
if ((k*2)%100)<=50:
    print("GOOD")  
else:
    print("OH MY GOD")   