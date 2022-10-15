#TODO - WHAT HAPPENS IF YOU ARRIVE AT THE ENGINE ROOM?
from room_flavor import room_print
from item_flavor import print_item
from endings import confrontation, meltdown
from prompts import starting_prompt, prompting, help_prompt
from tables import *
from text_art import print_invalid, print_warning

if __name__ == '__main__':
    inventory = []
    current_room_id = 6
    current_room = room_ids[current_room_id]
    countdown = 10.0

    starting_prompt(current_room_id, inventory)
    clear()

    room_print(current_room_id)
    choice, current_room, current_room_id = prompting(current_room, current_room_id, inventory)

    while current_room not in ending_rooms:
        countdown -= .35
        # TODO - check if this is working
        if choice == 'help':
            clear()
            help_prompt()
            # this is the sample of the new prompting()
            choice, current_room, current_room_id = prompting(current_room, current_room_id, inventory)
      
        elif 7.66 <= countdown <= 7.8:
            clear()
            print_warning()
            print(  """
                WARNING: PLASMA ENGINE EMERGENCY SELF-DESTRUCT IMMINENT
                    SYSTEMS AT 80%
                    """)
            choice, current_room, current_room_id = prompting(current_room, current_room_id, inventory)

        elif 4.5 <= countdown <= 4.66:
            clear()
            print_warning()
            print(  """
                WARNING: PLASMA ENGINE EMERGENCY SELF-DESTRUCT IMMINENT
                    SYSTEMS AT 50%
                    """)
            choice, current_room, current_room_id = prompting(current_room, current_room_id, inventory)

        elif 1.7 <= countdown <= 1.86:
            clear()
            print_warning()
            print(  """
                WARNING: PLASMA ENGINE EMERGENCY SELF-DESTRUCT IMMINENT
                    SYSTEMS AT 20%
                    """)
            choice, current_room, current_room_id = prompting(current_room, current_room_id, inventory)

        elif countdown <= 0:
            current_room = 'meltdown'
            clear()
            meltdown(current_room, countdown)

        # possibbly adding this elif to inner of prompting()
        elif current_room_id == 9 and current_room == 'confrontation':
            clear()
            confrontation(current_room, inventory)

        elif (rooms[4]['item']['space larva'] == 0) and \
             (rooms[8]['item']['odd blob of space jelly'] == 0):
            current_room = 'bonus'
            clear()
            confrontation(current_room, inventory)

        elif choice in rooms[current_room_id]['directions'] \
                and rooms[current_room_id]['directions'] != 9:
            clear()
            room_print(current_room_id)
            choice, current_room, current_room_id = prompting(current_room, current_room_id, inventory)

        # ensure the item is correct item and it is not in inventory
        # and it is still available in the room
        # let function handle printing and inventory acquisitino
        elif choice in list(rooms[current_room_id]['item'].keys())[0].split():
            choice = list(rooms[current_room_id]['item'].keys())[0]
            if rooms[current_room_id]['item'][choice] == 1:
                # current_room_id = rooms[current_room_id]['directions'][choice]
                # current_room = room_ids[current_room_id]
                grabbed_item = rooms[current_room_id]['item'][choice]
               # inventory.append(grabbed_item)
               # rooms[current_room_id]['item'][choice] = 0
                clear()
                print_item(current_room_id, inventory)
                choice, current_room, current_room_id = prompting(current_room, current_room_id, inventory)
            else:
                clear()
                print_invalid()
                print('Please enter another choice:\n')
                choice, current_room, current_room_id = prompting(current_room, current_room_id, inventory)
        else:
            clear()
            print_invalid()
            print('Please enter another choice:\n')
            choice, current_room, current_room_id = prompting(current_room, current_room_id, inventory)
