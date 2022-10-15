from tables import *

item_flavor = {
        1: {
            'analysis tool': """
A shiny buzzing gadget that looks half broken. It may or may not work, but if
it does it could give you insight into the creature's weaknesses.
            """
            },
        2: {
            'tool kit': """ 
An eclectic sack of mostly generic, but several specific tools. There may be
enough here to fix the pod, if you ever make it there that is.
            """
            },
        3: {
            'meal rations': """ 
Some less than appetizing freeze dried meals. Won't go bad if you get ejected
into space, and may keep you alive for month in the pod, if the smell doesn't
attract the monster.
            """
            },
        4: {
            'space larva': """ 
Strange little creatures. They look like green maggots, except about five times
bigger, and with little faces...very creepy.
            """
            },
        5: {
            'sonic explosives': """ 
Unassuming little grey balls of metal...except they'll make as much sound as 
a barrel of dynamite once detonated. Hoping to spook the creature with these 
puppies.
            """                
            },
        7: {
            'advanced spacesuit': """ 
A very cutting edge suit made out of top-secret nano material with a really
looking fiber pattern. If you don't damage it too much, and survive all this,
it'll be worth enough to buy your own ship.
            """ 
            },
        8: {
            'odd blob of space jelly': """ 
The blob of goo wriggles and squirms up your arm, definitely with a mind of its
own. Even though it looks like a jello mold, you would also say it was pretty 
cute (ㅅꈍ ˘ ꈍ)
            """
            },
        10: {
            'mining interface': """ 
You're quite familiar with the mining interface. Its a powerful all purpose
demolition laser, held like a minigun and basically much mor deadly, only 
legal since it's sanctioned for mining operations only...except for today.
            """
            }
        }


def print_item(room_id, inventory):
    global rooms
    # below line is perfect
    item = list(rooms[room_id]['item'].keys())[0]
    rooms[room_id]['item'][item] = 0
    # printing the flavor text
    print(item_flavor[room_id][item])
    inventory.append(list(item_flavor[room_id].keys())[0])
    return inventory
