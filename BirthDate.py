   # Create a dictionary to store friends' names and their birthdays  
birthdays = {}  

# Input the names and birthdays  
for _ in range(3):  
    name = input("Enter your friend's name: ")  
    birthday = input("Enter their birthday (e.g., YYYY-MM-DD): ")  
    birthdays[name] = birthday  

# Print the birthdays  
print("\nFriends' birthdays:")  
for name, birthday in birthdays.items():  
    print(f"{name}: {birthday}")  
