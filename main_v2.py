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


def make_state(pre_state):
    global countdown
    countdown -= .35
    dc = pre_state[0].lower().split()
    current_rid = pre_state[1]
    # return inits
    inventory = pre_state[2]
    choice = dc[1]
    action = dc[0]
    new_rid = current_rid
    status = -1
    meltdown_warn = 0

    if countdown <= 0: 
        status = 6

    elif (7.66 <= countdown <= 7.8)\
            or (4.5 <= countdown <= 4.66)\
            or (1.7 <= countdown <= 1.86):
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

    return action, choice, new_rid, status, inventory, meltdown_warn


def prompt(current_rid, inventory):
    return make_state(choice_prompt(current_rid, inventory))


def meltdown_warning():
    global meltdown_warn
    if 7.66 <= countdown <= 7.8:
        clear()
        print_warning()
        print("""
            WARNING: PLASMA ENGINE EMERGENCY SELF-DESTRUCT IMMINENT
                SYSTEMS AT 80%
                """)
    elif 4.5 <= countdown <= 4.66:
        clear()
        print_warning()
        print(  """
            WARNING: PLASMA ENGINE EMERGENCY SELF-DESTRUCT IMMINENT
                SYSTEMS AT 50%
                """)
    elif 1.7 <= countdown <= 1.86:
        clear()
        print_warning()
        print(  """
            WARNING: PLASMA ENGINE EMERGENCY SELF-DESTRUCT IMMINENT
                SYSTEMS AT 20%
                """)
    meltdown_warn = 1
    return


if __name__ == '__main__':
    countdown = 10
    meltdown_warn = 0
    room_id = 6
    inventory = []
    #make_state
    action, choice, room_id, status_code, inventory, meltdown_warn \
         = prompt(room_id, inventory)
    print('action: ', action)
    print('choice: ', choice)
    print('room_id(next):', room_id)
    print('status_code', status_code)
    print('inventory', inventory)
    print('meltdown_warn', meltdown_warn)

    # while - the status is not an ending state

    # while - the status is an ending state


test = """
rid = 7
inv = []
dc = 'take spacesuit'
dct = (dc, rid, inv)
#print(choice_prompt(1, []))
#print(make_state(choice_prompt(rid, inv)
print(make_state(dct))
"""

