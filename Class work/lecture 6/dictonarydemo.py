d={124:"akshay",890:"aarohi",997:"hamza",545:"rishil",890:"milin"}

print(d)
d[124]="uday"
print(d)
print(d[890])
#d.clear()
#print(d)
d1=d.copy()
print(d1)
print(d.get(997))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(545))
print(d)
print(d.popitem())
print(d)
d2={345:"shivam",678:"nirmal",789:"jay",889:"krishna"}
d.update(d2)
print(d)

for i in d:
    print(i," : ",d[i])
