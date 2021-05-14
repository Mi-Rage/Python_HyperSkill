import random

friends_list = list()
lucky_friend = ""

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
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_mode = True if input() == "Yes" else False
    if lucky_mode:
        lucky_friend = random.choice(friends_list)
        print(f"{lucky_friend} is the lucky one!")
        each_bill = round(total_bill / (num_of_people - 1), 2)
    else:
        print("No one is going to be lucky")
        each_bill = round(total_bill / num_of_people, 2)
    friends_dict = {name: each_bill for name in friends_list}
    if lucky_mode:
        friends_dict[lucky_friend] = 0

    print(friends_dict)
