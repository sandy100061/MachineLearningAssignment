L1=[int(num) for num in input().split(" ")]
W_kg=[]
for i in L1:
    W_kg.append(round(i / 2.205, 2))
print ("Values are:",W_kg)