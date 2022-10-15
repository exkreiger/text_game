from room_flavor import room_print
from item_flavor import print_item
from endings import confrontation, meltdown
from prompts import starting_prompt, prompting, help_prompt
from text_art import print_invalid, print_warning
from tables import *


def choice_prompt(current_rid, inventory):
    print()
    print('\\\\current_room: ', room_ids[current_rid].upper())
    print("\\\\forward ⬆️ . port ⬅️ . starboard ➡️ . aft ⬇️")
    print('\\\\inventory: ', inventory, '\n')
    dirty_choice = input('What would you like to do?\n>>$ ')
    pre_state = (dirty_choice, current_rid, inventory)
    return pre_state

# returns action, choice, new_rid, status, inventory, meltdown_warn
def make_state(pre_state):
    global countdown
    countdown -= .35
    dc = pre_state[0].lower().split()
    current_rid = pre_state[1]
    # return inits
    inventory = pre_state[2]
    if len(dc) <= 1:
        choice = 'invalid'
        action = 'invalid'
    else:
        choice = dc[1]
        action = dc[0]
    new_rid = current_rid
    status = 0
    meltdown_warn = 0

    if countdown <= 0: 
        status = -6

    elif  (countdown >= 7.55 and countdown <= 7.8)\
            or (countdown >= 4.4 and countdown <= 4.7)\
            or (countdown >= 1.6 and countdown <= 1.94):
        meltdown_warn = 1

    elif dc[0] in actions['help']:
        status = 8

    elif dc[0] in actions['move']:
        directions_list = list(rooms[current_rid]['directions'].keys())
        if dc[1] in directions_list:
            status = 1
            new_rid = rooms[current_rid]['directions'][dc[1]]
            action = 'move'
            choice = dc[1]
            if new_rid == 9:
                if (len(inventory) < 6):
                    status = -5
                else:
                    status = -4
        else:
            status = 10

    elif dc[0] in actions['grab']:
        item = list(rooms[current_rid]['item'].keys())[0]
        item_avail = rooms[current_rid]['item'][item]
        if dc[1] in item.split() and item_avail == 1:
            status = 2 
            new_rid = current_rid
            action = 'grab'
            choice = list(rooms[current_rid]['item'].keys())[0]
            inventory.append(item)
            if 'space larva' in inventory\
                    and 'odd blob of space jelly' in inventory:
                status = -7
        else:
            status = 0
    else:
        status = 3

    return action, choice, new_rid, status, inventory, meltdown_warn


def prompt(current_rid, inventory):
    return make_state(choice_prompt(current_rid, inventory))


def meltdown_warning(meltdown_warn):
    if 7.55 <= countdown <= 7.8:
        clear()
        print_warning()
        print("""
            WARNING: PLASMA ENGINE EMERGENCY SELF-DESTRUCT IMMINENT
                SYSTEMS AT 80%
                """)
        input('<<PRESS ENTER TO PROCEED>>')
        meltdown_warn = 0
    elif 4.4 <= countdown <= 4.7:
        clear()
        print_warning()
        print(  """
            WARNING: PLASMA ENGINE EMERGENCY SELF-DESTRUCT IMMINENT
                SYSTEMS AT 50%
                """)
        input('<<PRESS ENTER TO PROCEED>>')
        meltdown_warn = 0
    elif 1.6 <= countdown <= 1.94:
        clear()
        print_warning()
        print(  """
            WARNING: PLASMA ENGINE EMERGENCY SELF-DESTRUCT IMMINENT
                SYSTEMS AT 20%
                """)
        input('<<PRESS ENTER TO PROCEED>>')
        meltdown_warn = 0
    return meltdown_warn


if __name__ == '__main__':
    # defaults for first state
    # testing use, keeping
    defaults = [6,[], 10, 0]

    room_id = defaults[0]
    inventory = defaults[1]
    countdown = defaults[2]
    meltdown_warn = defaults[3]

    # intro prints
    starting_prompt()
    room_print(room_id)
    # make_state
    action, choice, room_id, status_code, inventory, meltdown_warn \
         = prompt(room_id, inventory)
    being_polite = 1 
    #BEGIN GAME LOOP
    # the status is not an ending state
    while status_code > 0:
        clear()
        if being_polite == 1 and len(inventory) == 6:
            print("""
        You have enough items for a good chance at fighting the monster.
                        Head AFT for the ENGINE ROOM.
        ________________________________________________________________
            """)
            being_polite = 0
        #debug mode
        # """
        print('action :', action)
        print('choice :', choice)
        print('room_id :', room_id)
        print('status_code: ', status_code)
        print('inventory :', inventory)
        print('meltdown_warn :', meltdown_warn)
        print('countdown :', countdown)
        # """
        # check the meltdown warning first
        if meltdown_warn == 1:
            meltdown_warn = meltdown_warning()
            continue

        # status 1 - moving rooms - valid direction
        if status_code == 1: 
            room_print(room_id)
            action, choice, room_id, status_code, inventory, meltdown_warn \
                 = prompt(room_id, inventory)
            continue
        
        # status 10 - moving rooms, invalid direction
        elif status_code == 10:
            room_item = list(rooms[room_id]['item'].keys())[0]
            room_name = room_ids[room_id]
            item_present = rooms[room_id]['item'][room_item]
            print_invalid()
            print("There's nowhere to go in that direction...\n")
            if item_present == 1:
                print("The {} still has something of value...{}"\
                        .format(room_name.upper(), room_item.upper()))
            action, choice, room_id, status_code, inventory, meltdown_warn \
                 = prompt(room_id, inventory)
            continue

        # status 2 - grabbing an item - available
        elif status_code == 2:
            print_item(room_id, inventory) 
            action, choice, room_id, status_code, inventory, meltdown_warn \
                 = prompt(room_id, inventory)
            continue

        # status 9 - grabbing an item - unavailable
        elif status_code == 9:
            print_invalid()
            print('You already have the item in your inventory...')
            action, choice, room_id, status_code, inventory, meltdown_warn \
                 = prompt(room_id, inventory)
            continue

        # status 3 - invalid input
        elif status_code == 3:
            print_invalid()
            print('You are understandably stressed...your mind must be jumbled')
            action, choice, room_id, status_code, inventory, meltdown_warn \
                 = prompt(room_id, inventory)
            continue
                
        # status 8 - help prompt
        elif status_code == 8:
            help_prompt()
            action, choice, room_id, status_code, inventory, meltdown_warn \
                 = prompt(room_id, inventory)
            continue

    # the status is an ending state 
    while status_code < 0:
        
        # status -4 - you win the battle
        # status -5 - you lose the battle
        # status -7 - bonus ending
        if status_code == -4 or status_code == -7 or status_code == -5:
            confrontation(status_code)
            break
        # status -6 - the engine melts down
        elif status_code == -6:
            meltdown()
            break




test = """
rid = 7
inv = []
dc = 'take spacesuit'
dct = (dc, rid, inv)
#print(choice_prompt(1, []))
#print(make_state(choice_prompt(rid, inv)
print(make_state(dct))
"""

