source = input("Enter cells: ")
print("---------")
for i in range(0, len(source), 3):
    print("| {0} {1} {2} |".format(source[i], source[i+1], source[i+2]))
print("---------")
