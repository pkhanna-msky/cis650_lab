largest = 0
for _ in range(5):
    next_input = int(input('Enter a positve number: '))
    if next_input > largest:
        largest = int(next_input)
        print('The largest number is: ' , largest)

largest = -99
for _ in range(5):
    next_input = int(input('Enter a positve number: '))
    if next_input > largest:
        largest = int(next_input)
        print('The largest number is: ' , largest)

    smallest = -99
for _ in range(5):
    next_input = int(input('Enter a positve number: '))
    if next_input > smallest:
        largest = int(next_input)
        print('The smallest number is: ' , smallest)    