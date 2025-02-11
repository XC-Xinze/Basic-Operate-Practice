user=[]
if user:
    for users in user:
        if users == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {users}, thank you for logging in again')
else:
    print('We need to find some users!')

current_users = ['admin', 'user1', 'user2', 'user3', 'user4']
new_users = ['user1', 'user2', 'user5', 'user6', 'user7']
for users in new_users:
    if users in current_users:
        print(f'{users} is already taken, please enter a new username')
    else:
        print(f'{users} is available')