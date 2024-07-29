
'''
Trying out input and output in python
'''
name = input('Enter your name')
print("this is", name)

number = int(input('Enter your roll no'))
print(" your id is ", number)


with open('output.txt', 'a') as file:
    print("Hello", "this is me", name, "my number is ",number, sep=' - ', end='.\n', file=file)
