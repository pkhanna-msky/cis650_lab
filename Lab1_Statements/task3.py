name = input('What is your name?')
if len(name) > 0:
    print('Hello ', name)
else:
    print('Enter your name, please!')

name = input('Enter your name?')
if len(name) > 0:
    print('Hello' , name)
else:
    print('Enter your name, please!')

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

if len(first_name)>0 and len(last_name)>0:
    print('Hello, ', first_name, last_name)
    print('Both entries must be non-blank')
else:
    print('Hello' , first_name, last_name)