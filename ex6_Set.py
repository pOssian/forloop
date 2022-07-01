'''
SET

d. Since Ash’s memory is going bad, Help him and create a program that takes a 
user input (using the python input operator), where the user can type a Pokémon name 
and then the program should print out if the Pokémon is already in the captured tuple or not.
also print the total number of Pokémon in the captured tuple, 
as well as the number of unique Pokémon.
'''


from operator import countOf


captured = 'Pikachu', 'Pidgey', 'Abra', 'Pidgey', 'Eevee', 'Pidgey'

pokemon = input('Pokemon name?: ')

if pokemon in captured:
    print(captured.count(pokemon))
    print(captured)
else :
    print('No such pokemon in the list.')
