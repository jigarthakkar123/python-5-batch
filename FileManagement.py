file=open("tops1.txt","w")
file.write("This is file management demo using python.")
file.close()
print("File Written Successfully")
print("***********************************************************")

file=open("tops1.txt","r")
print(file.read())
file.close()
print("***********************************************************")

file=open("tops1.txt","a")
file.write("\nNow this file is appended.")
file.close()
print("File Appended Successfully")
print("***********************************************************")

file=open("tops1.txt","r")
print(file.read())
file.close()
print("***********************************************************")

file=open("tops2.txt","w+")
file.write("This is file w+ mode using python for read/write data.")
print(file.tell())
file.seek(20)
print(file.read())
file.close()
print("***********************************************************")





