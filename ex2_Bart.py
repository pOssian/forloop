### Day2 Python

from pyparsing import line_end


my_name =r''' 
___           ___           ___           ___           ___           ___     
     /\  \         /\  \         /\__\         /\  \         /\__\         /\  \    
    /::\  \       /::\  \       /::|  |        \:\  \       /:/  /        /::\  \   
   /:/\:\  \     /:/\:\  \     /:|:|  |         \:\  \     /:/  /        /:/\ \  \  
  /::\~\:\  \   /:/  \:\  \   /:/|:|  |__       /::\  \   /:/  /  ___   _\:\~\ \  \ 
 /:/\:\ \:\__\ /:/__/ \:\__\ /:/ |:| /\__\     /:/\:\__\ /:/__/  /\__\ /\ \:\ \ \__\
 \/__\:\/:/  / \:\  \ /:/  / \/__|:|/:/  /    /:/  \/__/ \:\  \ /:/  / \:\ \:\ \/__/
      \::/  /   \:\  /:/  /      |:/:/  /    /:/  /       \:\  /:/  /   \:\ \:\__\  
       \/__/     \:\/:/  /       |::/  /     \/__/         \:\/:/  /     \:\/:/  /  
                  \::/  /        /:/  /                     \::/  /       \::/  /   
                   \/__/         \/__/                       \/__/         \/__/    '''
                   
                   
                   
print(my_name)

first_name = 'pontus'
last_name = 'ossian'
course = 'Data Engineering'
candidates = '9'

print(
f'''my name is {first_name.capitalize()}, with last name 
{last_name.capitalize()}. I am participating in the course 
{course.lower()} and there are {candidates} candidates taking the course.'''
)

punishment_text = 'I will not teach others to fly\n'
number_of_repetition = 10
print(punishment_text * number_of_repetition)

# Mess with Bart, by writing code that removing the word “not” in
#“punishment_text”, and changing the word “good” with “bad”
# before its printed out. remove

print(punishment_text.replace('others','everyone').replace('not','') * number_of_repetition)
