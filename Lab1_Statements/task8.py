alphabets='abcdefghijklmnopqrstuvwxyz'
while True:
    user_entry = input('Enter a letter (or blank to exit): ')
    if user_entry == '':
        break
    else:
        position = alphabets.find(user_entry)
        if position == -1:
            print(f'{user_entry} is at position {position}')

alphabets='abcdefghijklmnopqrstuvwxyz'
while True:
    user_entry = input('Enter a letter or blank to exit: ')
    if user_entry == '':
        break
    else:
        position = alphabets.find(user_entry)
        if position == -1:
            print(f'{user_entry} is not at position {position}')
        else:
            print(f'{user_entry} is at position {position}')
            