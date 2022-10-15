import os
import platform

if platform.system() == 'Windows':
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

ending_rooms = ['confrontation', 'meltdown', 'bonus', 'engine room']
no_item_rooms = [6, 9, 11]

actions = {
    'move': ['move', 'go', 'head'], 
    'grab': ['grab', 'get', 'take'],
    'invalid': 'invalid'
        }

game_status = {
    1: 'moving rooms',
    2: 'grabbing item',
    3: 'invalid input',
    4: 'confrontation',
    5: 'meltdown ending',
    6: 'bonus ending',
    7: 'meltdown warning'
        }

room_ids = {
    1: 'flight deck',
    2: 'navigation room',
    3: 'dining hall',
    4: 'greenhouse',
    5: 'cargo bay',
    6: 'crew quarters',
    7: 'science deck',
    8: 'decompression chambers',
    9: 'engine room',
    10: 'hardware storage',
    11: 'escape pod bay'
}

rooms = {
        1: {
            'directions': {
                'aft': 3
                },
            'item': {
                'analysis tool': 1,
                }
            },
        2: {
            'directions': {
                'starboard': 3
                },
            'item': {
                'tool kit': 1,
                }
            },
        3: {
            'directions': {
                'forward': 1,
                'port': 2,
                'aft': 6,
                'starboard': 4
                },
            'item': {
                'meal rations': 1,
                }
            },
        4: {
            'directions': {
                'port': 3,
                'aft': 7 
                },
            'item': {
                'space larva': 1,
                },
            },
        5: {
            'directions': {
                'starboard': 6
                },
            'item': {
                'sonic explosives': 1
                }
            },
        6: {
            'directions': {
                'forward': 3,
                'port': 5,
                'aft': 9,
                'starboard': 7
                }
            },
        7: {
            'directions': {
                'forward': 4,
                'port': 6,
                'aft': 10,
                'starboard': 8 
                },
            'item': {
                'advanced spacesuit': 1,
                }
            },
        8: {
            'directions': {
                'port': 7
                },
            'item': {
                'odd blob of space jelly': 1,
                }
            },
        9: {
            'directions': {
                'aft': 11
                },
            },
        10: {
            'directions': {
                'forward': 7,
                'port': 9
                },
            'item': {
                'mining interface': 1,
                },
            },
        11: {
            'item': {
                'ending': 1
                }
            }
}
