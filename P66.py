file_1 = "text1.txt"
file = open (file_1 , "r+")
print(f"{file.readline()}\n")
print(f"{file.readline()}\n")
print(f"{file.readline()}\n")
print(f"{file.readline()}\n")
file.close()