friends_dict = dict()

print("Enter the number of friends joining (including you)")
num_of_people = int(input())

if num_of_people <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_of_people):
        name = input()
        friends_dict[name] = 0
    print(friends_dict)
