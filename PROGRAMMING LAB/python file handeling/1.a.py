file = open("file3.txt", "w")
file.write("hello world!\nwelcome to python programing\nThank you")
file.close()
list = []
file = open("file3.txt", "r")
list = [line.strip() for line in file]
file.close()
print(list)