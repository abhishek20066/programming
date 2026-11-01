l = [56,64,32,11,78,6]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
      l[j],l[i]=l[i],l[j]
print(l)
        