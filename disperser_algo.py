A=["x","y","z","x","y","t","x"]
D={}
ref=[]
for a in A:
    	if a not in ref:
            ref.append(a)
            D.update({a:1})
    	else:
            t=D.get(a)
            t += 1
            D.update({a:t})
print(D)
