friends_names = ['Jay', 'Brit', 'Tom', 'Phil']
friends_names1 = ['Mike', 'Brad', 'Terry', 'Sandy']
msg = 'You are invited to the party on saturday.'
friends_names.extend(friends_names1)

for index in range(2):
    friends_names.append(input('Enter names: '))

for name in friends_names:
    second_invite = f'{name.title()}!  {msg}'
    print(second_invite)
