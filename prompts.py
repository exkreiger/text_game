from room_flavor import room_print
from text_art import *
from tables import rooms, room_ids



def starting_prompt(current_room_id, inventory):
    print_title()    
    print()
    print()
    print(""" 
    Welcome aboard the Daedalus. You find yourself in a dire situation. The 
    ship has been overwhelmed by a strange creature from unknown origins, and 
    warning lights are flashing as the ship prepares for a self-destruct 
    sequence. 
            """)
    print("""
    Make your way around the ship to gather the materials you need to defeat 
    the space creature...
            """)
    help_prompt()
    c = ''
    while c != 'start':
        print('(When you are ready to start, enter START)\n')
        c = input('>>$ ').lower().split()[0]
        if c == 'help':
            help_prompt()
    return


def help_prompt():
    print("""
        (To navigate around the ship, enter a direction in the prompt to 
        explore: forward ⬆️ . port ⬅️ . starboard ➡️ . aft ⬇️)
            """)
    print("""
        (To grab an item, enter the item name in the prompt.)
            """)
    print("""
        (To see the commands again, enter "help" in the prompt.)
            """)
    return


def prompting(current_room, current_room_id, inventory):
    print()
    print('\\\\current_room: ', room_ids[current_room_id].upper())
    print("\\\\forward ⬆️ . port ⬅️ . starboard ➡️ . aft ⬇️")
    print('\\\\inventory: ', inventory, '\n')
    choice = input('What would you like to do?\n>>$ ').lower().split(' ')[0]


    if choice in rooms[current_room_id]['directions'] \
            and rooms[current_room_id]['directions'][choice] != 9:
        next_id = rooms[current_room_id]['directions'][choice]
        next_room = room_ids[next_id]
    elif choice in rooms[current_room_id]['directions'] \
            and rooms[current_room_id]['directions'][choice] == 9:
        next_id = rooms[current_room_id]['directions'][choice]
        next_room = 'confrontation'
    else:
        next_id = current_room_id
        next_room = current_room

    return choice, next_room, next_id
