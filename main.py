from room_flavor import room_print
from item_flavor import print_item
from endings import confrontation, meltdown
from prompts import *
from text_art import print_invalid, print_warning
from tables import *



if __name__ == '__main__':
    # defaults for first state
    # testing use, keeping
    defaults = [6,[], 10, 0]

    room_id = defaults[0]
    inventory = defaults[1]
    countdown = defaults[2]
    meltdown_warn = defaults[3]

    # 1-off for reminder to fight the monster
    being_polite = 1 

    # intro prints
    starting_prompt()
    room_print(room_id)
    # make_state
    action, choice, room_id, status_code, inventory, meltdown_warn \
         = prompt(room_id, inventory)

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
            continue

        # check the meltdown warning first
        if meltdown_warn == 1:
            meltdown_warn = meltdown_warning(meltdown_warn)
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
            print("""
        You must be stressed, because that didnt make any sense  ( -_-) """)
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
        if status_code == -6:
            meltdown()
            break
