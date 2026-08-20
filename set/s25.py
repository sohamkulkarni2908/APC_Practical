user1 = {"Nikhil", "Rehan", "Nisarg", "Siddhant"}
user2 = {"Nisarg", "Siddhant", "Pravin", "Chetan"}

print("Mutual friends:", user1 & user2)
print("Friends unique to User 1:", user1 - user2)
print("Friends unique to User 2:", user2 - user1)
print("Total unique friends:", user1 | user2)