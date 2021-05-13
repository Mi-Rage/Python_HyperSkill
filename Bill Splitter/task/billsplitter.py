friends_list = list()

print("Enter the number of friends joining (including you)")
num_of_people = int(input())

if num_of_people <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_of_people):
        friends_list.append(input())
    print("Enter the total bill value:")
    total_bill = int(input())
    each_bill = round(total_bill / num_of_people, 2)
    friends_dict = {name: each_bill for name in friends_list}
    print(friends_dict)
