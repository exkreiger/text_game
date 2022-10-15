from room_flavor import room_print
from text_art import *
from tables import rooms, room_ids



def starting_prompt():
    print_title()    
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
        <<To navigate around the ship, enter GO [direction] in the prompt.

                    forward ⬆️  . port ⬅️  . starboard ➡️  . aft ⬇️)
            """)
    print("""
        <<To grab an item, enter GRAB [item] in the prompt.
            """)
    print("""
        <<To see the commands again, enter HELP in the prompt.
            """)
    return


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
        return action, choice, new_rid, status, inventory, meltdown_warn

    if  (countdown >= 7.55 and countdown <= 7.8)\
            or (countdown >= 4.4 and countdown <= 4.7)\
            or (countdown >= 1.6 and countdown <= 1.94):
        meltdown_warn = 1

    if action in actions['help']:
        status = 8

    elif action in actions['move']:
        directions_list = list(rooms[current_rid]['directions'].keys())
        if choice in directions_list:
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

    elif action in actions['grab']:
        item = list(rooms[current_rid]['item'].keys())[0]
        item_avail = rooms[current_rid]['item'][item]
        if choice in item.split() and item_avail == 1:
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
