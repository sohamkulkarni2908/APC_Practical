morning = {"Nikhil", "Siddhant", "Nisarg", "Soham"}
afternoon = {"Nisarg", "Nikhil", "Rehan", "Shubham"}

print("Present in both session:", morning & afternoon)
print("Only in morning session:", morning - afternoon)
print("Only in afternoon session:", afternoon - morning)
print("Present in at least one session:", morning | afternoon)