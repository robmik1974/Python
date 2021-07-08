"""Bill Splitter calculates the bill value amoung friends joining the party"""

import random, sys
try:
    number = int(input("Enter the number of friends joining (including you): \n"))
except (TypeError, ValueError):
    print("No one is joining for the party")
else:
    print()
    if number > 0:
        print("Enter the name of every friend (including you), each on a new line:")
        friends = dict.fromkeys([input() for n in range(number)], 0)
        print()
        try:
            bill_value = float(input("Enter the total bill value: \n"))
        except ValueError:
            print("Please provide bill value correctly next time")
            sys.exit()
        print()
        result = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        if result == "Yes":
            list_of_users = [key for key in friends]
            lucky_one = random.choice(list_of_users)
            friends.pop(lucky_one)
            print()
            print(f'{lucky_one} is the lucky one!')
            bill_value = round((bill_value / (number - 1)), 2)
            friends = {key : bill_value for key in friends}
            friends[lucky_one] = round(0, 2)
            print()
            print(friends)
        else:
            print()
            print('No one is going to be lucky')
            bill_value = round((bill_value / number), 2)
            friends = {key : bill_value for key in friends}
            print()
            print(friends)
    else:
        print()
        print("No one is joining for the party")
