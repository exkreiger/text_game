from room_flavor import room_print
from item_flavor import print_item
from endings import confrontation, meltdown
from prompts import starting_prompt, prompting, help_prompt
from text_art import print_invalid, print_warning
from tables import *

#if __name__ == '__main__':






#NOTE - TIMER IS GETTING DECD IN CHOICE FIX --- I DONT CARE
# TODO - below, redef of prompting() to return the raw choice
# then adding choice_fix() which will clean the choice, returning tokens
# in tuple for (choice = 'direction/item', action = code for action

def prompting(current_room_id, inventory):
    print()
    print('\\\\current_room: ', room_ids[current_room_id].upper())
    print("\\\\forward ⬆️ . port ⬅️ . starboard ➡️ . aft ⬇️")
    print('\\\\inventory: ', inventory, '\n')
    dirty_choice = input('What would you like to do?\n>>$ ')
    return dirty_choice, current_room_id, inventory

def choice_fix(dirty_choice):
    #TODO - check choice list, assign action code via arg 0 in dc,
    # assign choice via rest of args in dc
    #return 2 strings in tuple 'choice'
    global countdown
    countdown -= .35
    dc = dirty_choice[0].lower().split()
    cr_id = dirty_choice[1]
    inventory = dirty_choice[2]
    #NOTE -no, inst choice tuple at bottom
    #choice = 0 = get/move/invalid, 1=dir/item, 3= new room id, 4= status
    if dc[0] in actions['move']:
        directions_list = rooms[cr_id]['directions']
        if dc[1] in directions_list:
            status = 1
    elif dc[0] in actions['grab']:
        item = list(rooms[current_room_id]['item'])
        if dc[1] in item:
            status = 2 
    #elif check timer
    #elif check inventory - bonus ending
    #elif check for meltdown warning
        #elif check for meltdown is happening
    #elif check if there is a direct confrontation in eng room
    #else if choice sucks, invalid try again
    return choice, status

def prompt(current_room_id, inventory):
    return choice_fix(prompting(current_room_id, inventory))

print(prompting(1, []))

