import random
import reduce from functools
import csv_parser

def display_todo_list ():
    print('What would you like to today? ')
    csv_to_parse = input('Please enter a list separated by commmas> ')
    displayed_list = random_list(csv_parser.parse_csv(csv_to_parse))
    formatted_list(displayed_list)
        
    
def random_list (list):
    random.shuffle(list)
    print(list)
    return list

def formatted_list(list):
    reduce()
    
display_todo_list()
# First, do piano
# Then, do guitar
# Then, 