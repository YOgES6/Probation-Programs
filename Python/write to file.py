y=open("find1.txt", "w")
p=input("Enter text: ")
y.write(p)
print("\nDone well...")
print("Text written in the specified file...\n\n")
y=open("find1.txt", "r")
print(y.read())
y.close()

