#testing read file
with open("e11.txt", "r") as my_file:
    for i in range(0, 20):
        print my_file.readline()
