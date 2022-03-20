# write your code here
import random
print("Enter the number of friends joining (including you):")
friendno = int(input())
friends = {}
if friendno <= 0 or not type(int):
    print("\nNo one is joining for the party")
    exit()
print("\nEnter the name of every friend (including you), each on a new line:")
for x in range(0, friendno):
    friends[input()] = 0

print("\nEnter the total bill value:")
bill = int(input())



print("Do you want to use the 'Who is lucky?' feature? Write Yes/no:")
decision = input()
if decision == "Yes" or decision == "yes":
    luckyy = random.choice(list(friends.keys()))
    print(luckyy + " is the lucky one!")
    for k, v in friends.items():
        friends[k] = round(float(bill) / int(friendno-1), 2)
    friends[luckyy] = 0
    print(friends)
else:
    print("No one is going to be lucky")
    for k, v in friends.items():
        friends[k] = round(float(bill) / int(friendno), 2)
    print(friends)
