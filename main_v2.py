from room_flavor import room_print
from item_flavor import print_item
from endings import confrontation, meltdown
from prompts import starting_prompt, prompting, help_prompt
from text_art import print_invalid, print_warning
from tables import *

#if __name__ == '__main__':
countdown = 10
room_id = 6
inventory = []
#make_state
action, choice, room_id, status_code, inventory \
        = make_state(choice_prompt(room_id, inventory))
#check the status and apply the edge actions for endings, 
#otherwise continue on


#NOTE - TIMER IS GETTING DECD IN CHOICE FIX --- I DONT CARE
# TODO - below, redef of prompting() to return the raw choice
# then adding make_state() which will clean the choice, returning tokens
# in tuple for (choice = 'direction/item', action = code for action

def choice_prompt(current_rid, inventory):
    print()
    print('\\\\current_room: ', room_ids[current_rid].upper())
    print("\\\\forward ⬆️ . port ⬅️ . starboard ➡️ . aft ⬇️")
    print('\\\\inventory: ', inventory, '\n')
    dirty_choice = input('What would you like to do?\n>>$ ')
    return dirty_choice, current_rid, inventory

def make_state(dirty_choice):
    #TODO - check choice list, assign action code via arg 0 in dc,
    # assign choice via rest of args in dc
    #return 2 strings in tuple 'choice'
    global countdown
    countdown -= .35
    print(countdown)
    dc = dirty_choice[0].lower().split()
    print(dc)
    current_rid = dirty_choice[1]
    # return inits
    inventory = dirty_choice[2]
    choice = dc[1]
    action = dc[0]
    new_rid = current_rid
    status = 0
    #NOTE -no, inst choice tuple at bottom
    #choice = 0 = get/move/invalid, 1=dir/item, 3= new room id, 4= status


    if countdown <= 0: 
        status = 6
    #elif check if there is a direct confrontation in eng room
    #elif check for meltdown warning
        #elif check for meltdown is happening
    #elif check inventory - bonus ending
    elif dc[0] in actions['move']:
        directions_list = list(rooms[current_rid]['directions'].keys())
        if dc[1] in directions_list:
            status = game_status[1]
            new_rid = rooms[current_rid]['directions'][dc[1]]
            action = 'move'
            choice = dc[1]

            if new_rid == 9:
                if (len(inventory) < 6):
                    status = 5
                else:
                    status = 4

    elif dc[0] in actions['grab']:
        item = list(rooms[current_rid]['item'].keys())[0]
        if dc[1] in item.split():
            status = 2 
            new_rid = current_rid
            action = 'grab'
            choice = list(rooms[current_rid]['item'].keys())[0]
            inventory.append(item)

            if 'space larva' and 'odd blob of space jelly' in inventory:
                status = 7
    else:
        status = 3
        
    return action, choice, new_rid, status, inventory

def prompt(current_rid, inventory):
    return make_state(prompting(current_rid, inventory))

rid = 7
inv = []
dc = 'take spacesuit'
dct = (dc, rid, inv)
#print(choice_prompt(1, []))
#print(make_state(choice_prompt(rid, inv)
print(make_state(dct))
