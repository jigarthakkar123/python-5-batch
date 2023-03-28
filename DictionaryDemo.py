d={109:"Nisarg",112:"Kunjan",899:"Kevin",478:"Jaydeep",453:"Sagar"}

print(d)
d1=d.copy()
print(d1)
print(d.get(112))
print(d[899])
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(109))
print(d)
print(d.popitem())
d2={323:"Manya",545:"Mahek",765:"Ronik",333:"Raj"}
d.update(d2)
print(d)
d[577]="Sid"
print(d)

for i in d:
    print(i," : ",d[i])
