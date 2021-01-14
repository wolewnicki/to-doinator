import random
from functools import reduce
from csv_parser import parse_csv

def display_todo_list ():
    print('What would you like to today? ')
    csv_to_parse = input('Please enter a list separated by commmas> ')
    randomized_list = random_list(parse_csv(csv_to_parse))
    displayed_list = formatted_list(randomized_list)

    for item in displayed_list:
        print(item)
        
    
def random_list (list):
    random.shuffle(list)

    return list

def formatted_list(randomed):
    first_item = f'First, you should {randomed[0]}'
    randomed = list(map(lambda item: f'Then, you should {item}', randomed[1:]))
    randomed.insert(0, first_item)
    return randomed
    
display_todo_list()
input()