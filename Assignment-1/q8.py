f1 = open("file1.txt", "r")
f2 = open("file3.txt", "w")

data = f1.read()
f2.write(data)

f1.close()
f2.close()

print("File copied successfully")
