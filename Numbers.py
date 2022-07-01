'''1. Go back to your solution from ex_print_and_var question 3 
and use the input operator to let the user define the inputs for the text.
'''


'''
first_name = input('What is your first name? :')
last_name= input('What is your last name? :')
course = input('What course are you attending? :')
candidates = input('How many people are attending? :')

print(
f'''Your name is {first_name.capitalize()}, with last name 
{last_name.capitalize()}. I am participating in the course 
{course.lower()} and there are {candidates} candidates taking the course.'''
)'''


'''2. Createacalculator:
a. Make a program called my_sum.py. Use the “input” operation in
python, and let the user specify two input, sum them together, and print the result. Double check that the math is correct.
hint: make sure that the type of the values is float before adding them together.'''

A = input('Give me a number:')
B = input('Give me another number:')

Print(A.format(float)+B.format(float))