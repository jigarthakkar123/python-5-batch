import random

data=open("data.txt","w")
for i in range(10):
    num=random.randint(1,1000)
    data.write(str(num)+",")
data.close()

data=open("data.txt","r")
odd=open("odd.txt","w")
even=open("even.txt","w")
prime=open("prime.txt","w")

l=data.read().split(",")[:-1]
for i in l:
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")
        for j in range(3,int(int(i)/2)+1,2):
            if int(i)%j==0:
                break
        else:
            prime.write(i+",")
            
data.close()
even.close()
odd.close()
prime.close()

print("Data File Content")
file=open("data.txt","r")
print(file.read())
file.close()

print("Even File Content")
file=open("even.txt","r")
print(file.read())
file.close()

print("Odd File Content")
file=open("odd.txt","r")
print(file.read())
file.close()

print("Prime File Content")
file=open("prime.txt","r")
print(file.read())
file.close()
