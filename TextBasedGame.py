####
#####FUNCTIONS AND PROMPTS
####
import os
import platform

if platform.system() == 'Windows':
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')


def text_art(room_id):
    if room_id == 1:
        flight_deck_title()
    if room_id == 2:
        navigation_room_title()
    if room_id == 3:
        dining_hall_title()
    if room_id == 4:
        greenhouse_title()
    if room_id == 5:
        cargo_bay_title()
    if room_id == 6:
        crew_quarters_title()
    if room_id == 7:
        science_deck_title()
    if room_id == 8:
        decompression_chambers_title()
    if room_id == 9:
        engine_room_title()
    if room_id == 10:
        hardware_storage_title()
    if room_id == 11:
        escape_pod_bay_title()
    return


def room_print(room_id):
    global initial_visit
    room_flavor = {
        1: {
            'initial text': """
        The captain and XO have long since fled, and text scrolls 
        maddeningly across the darkened consoles. An ANALYSIS TOOL 
        still sits on the captain's command post, which may help you 
        get an edge on whatever is tearing away at the pulse engine.
        """,
            'standard text': """
        It is a desolate scene in the command area. You ponder briefly 
        on the horrible stillness of space, while you stare out into 
        the void through the large glass flight windows -- comparing 
        the uneasy blackness to the chaos inside the Daedalus."""
                },
        2: {
            'initial text': """ 
        The navigation instruments are humming, some whirring to an
        extreme degree. Some small fires have broken out as the
        electronics have degraded as the ship's power system has been
        thrown in to a frenzy. You avoid the disarray as best you can,
        searching for a TOOL KIT you believe you remember hiding from
        your deck mate earlier in the voyage.
            """,
            'standard text': """
        The fires have started to die down, and now little stirs in the
        navigation area, other than the persistent whirring from the
        slowly dying nav computers.
            """
        },
        3: {
            'initial text': """ 
        Your initial reaction is to wretch at the mixing smells of food
        half eaten, and of various piles of trash strewn about the room.
        There are rumbling sounds coming from the walls, and you try to
        make your way through the space without slipping on the debris.
        Perhaps there are some MEAL RATIONS in the storage that haven't
        gone bad or been plundered.
            """,
            'standard text': """
        You remember back to a meal you had here last week, just after 
        leaving the last asteroid, with the simple hope of a great haul
        and a fat pay check. A far cry from your current state of
        survival --- You hear an alarming growl and hurriedly make your
        way.
            """
            },
        4: {
                'initial text': """
        The air here is still earthy and serene. The reinforced glass
        ceiling along with the surrounding lush green vegetation grant 
        a softening to the harsh view of the unnending void. Though 
        the sounds of the chaos outside persist, you rest for a moment, 
        taking in the small peace offered. There is a strange SPACE
        LARVA crawling around under the foliage. You think about taking
        it, but why would you need that?
                """,
                'standard text': """
        Though a pleasant space here in the garden, you don't linger
        for long, afraid you will not get back up onto your search.
                """
            },
        5: {
            'initial text': """ 
        The bulky, industrial area of the cargo bay is still jam packed
        with several tons of metallic crates, mostly containing raw
        materials from the recent mining haul -- you hear a moan of pain
        from the other side of the large room. It is a fellow crew mate,
        suffering under the weight of a crate. They can't speak, but
        you let them know you'll try to bring help -- one of the most
        hopeless promises you've ever made. Strewn about on the ground
        nearby are some SONIC EXPLOSIVES. Hmm, as long as that creature
        doesn't like 120+ decibal blasts, it could be a good distraction.
            """,
            'standard text': """
        More crates have fallen since you were last here, causing the
        formerly orderly and antiseptic space to mirror the insanity of
        the rest of the ship. The sound of your dying friend has ceased,
        however. You press on, unwilling to look back.
            """
            },
        6: {
                'initial text': """ 
        You awaken suddenly, the sound of metallic crashing and banging
        coming from seemingly all around. You can't quite recall how
        long you've been asleep, but something bad is happening. You get
        yourself up as quickly as you can, and try to find someone, but
        it appears most of your fellow crew mates have fled. 
            However, you can hear someone sobbing in the corner 
        behind a bunk. They have their face in their hands, and are 
        shaking slightly. You try to get some information, but all they 
        can say is "Monster...eating the engine...ate everybody." You 
        gulp, trying not to think about the details behind the muttered 
        words. They add in, "The last pod is damaged, and the engine....
        the engine..." Just as your crew mate starts to meander off into
        despair once more, the alarm starts to blair, and
        the harsh robotic voice announces that the self-destruct system
        has been activated.
                                    (ಠ_ಠ)
            So the basic mission is clear, make your way to the escape
        pod bay...except the only way there is through the engine room,
        where apparently the monster is devouring the plasma engine.
            Unsure of the details, you just know you must move forward,
        and prepare yourself for the confrontation with this creature,
        or at least die trying to survive...
                """,
                'standard text': """
        The beds have been stripped and strewn about, most goods have
        been stripped from the drawers and lockers. All that's left
        here are memories of quiet moments the Daedalus will never
        experience again.
                """
            },
        7: {
            'initial text': """
        The science deck is still fairly clean and secured. It oozes 
        with a cluster of interesting tech in a tall transparent 
        encasing. Rumor was that the science unit was funded by 
        government a government dark research unit, or the mob. You had
        no real opinion, but were interested in seeing if the ADVANCED
        SPACESUIT was still being stored here.
            """,
            'standard text': """
        The science room is eerily still, and you can't shake the
        feeling that the area is just too untouched given the disaster
        in the rest of the Daedalus.
            """
            },
        8: {
            'initial text': """
        The decompression chambers are stacked like an accordian on 
        either side of the ship, but one of them seems to have been
        heavily damaged, and that door is completely closed. The area
        is extremely dangerous, as it is hard to tell how long the doors
        will hold against the vaccuum. On your way past, you notice an
        ODD BLOB OF SPACE JELLY. Part of you fears the jelly, but part
        of you longs to touch the strange object.
            """,
            'standard text': """
        The area is only getting worse, and there is a strong, high-
        pitched whistling sounding all around as you pass. You don't
        think its at all wise to linger.
            """
            },
        9: {
            'initial text': """
        This is the engine room. The lights are all out except for the
        the plasmatic electricity sparking from the gigantic blob. It 
        devours the engine, the energy, and seems to hunger endlessly.
            """,
            'standard text': """ """ 
            },
        10: {
            'initial text': """
        The hardware storage is still well stocked, though there are 
        plenty of missing tools, probably grabbed at the last minute
        either for ad-hoc repairs or for weapons to ward off the
        creature. If you are lucky, you may find a MINING INTERFACE, a
        versatile long or short range laser that may also be useful
        for fighting off space monsters.
            """,
            'standard text': """ 
        Your inner tech-head comes alive here, but there's not really
        enough time to plan your next hobby project.
            """
        },
        11: {
            'initial text': """
        You have finally made it to the escape pods, and just like your
        friend said, the last pod is flashing a red light on its readout
        with a warning and error message. Luckily, you still have the
        login to the system's backend, and access the interface. The 
        pod program was written in Python, so you should be good to go
        after some quick debugging! 
            So long space monster -- you're on to brighter pastures!
            """,
            'standard text': """ """
            }
            }
    print("You've entered the...")
    text_art(room_id)
    if initial_visit[room_id] == 1:
        print(room_flavor[room_id]['initial text'])
        initial_visit.update({room_id: 0})
    elif initial_visit[room_id] == 0:
        print(room_flavor[room_id]['standard text'])
    return


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
    if len(dc) < 1:
        choice = 'invalid'
        action = 'invalid'
    elif len(dc) == 1:
        choice = 'invalid'
        action = dc[0]
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
        return action, choice, new_rid, status, inventory, meltdown_warn

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


def print_item(room_id, inventory):
    global rooms
    # below line is perfect
    item = list(rooms[room_id]['item'].keys())[0]
    rooms[room_id]['item'][item] = 0
    # printing the flavor text
    print(item.upper(), ":", item_flavor[room_id][item])
    return inventory


def confrontation(status_code):
    if status_code == -7:
        clear()
        print(bonus)
        print()
        print_the_end_winning()
    elif status_code == -4:
        clear()
        engine_room_title()
        print(winning)
        room_print(11)
        print()
        print_the_end_winning()
    elif status_code == -5:
        clear()
        engine_room_title()
        room_print(9)
        print(losing)
        print_the_end_losing()
    return


def meltdown():
    clear()
    print(melting)
    print_the_end_losing()
    return

####
#####TABLES AND TEXT
####
ending_rooms = ['confrontation', 'meltdown', 'bonus', 'engine room']
no_item_rooms = [6, 9, 11]

actions = {
    'move': ['move', 'go', 'head'], 
    'grab': ['grab', 'get', 'take'],
    'invalid': 'invalid',
    'help': ['help', 'h', 'man', '?']
    }

game_status = {
    1: 'moving rooms - valid direction',
    2: 'grabbing item - available',
    3: 'invalid input',
    -4: 'confrontation - win',
    -5: 'confrontation - lose',
    -6: 'meltdown ending',
    -7: 'bonus ending',
    8: 'helping',
    9: 'grabbing item - unavailable',
    10: 'moving rooms - invalid direction'
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
                },
            'item': {
                'just kidding lol': 1
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
            'item': {
                'nothing': 1
                }
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
initial_visit = {
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 1,
    6: 1,
    7: 1,
    8: 1,
    9: 1,
    10: 1,
    11: 1
}

bonus = """ 
        You feel a rustling on your person as the strange blob of space
        goo stirs. It crawls towards the wriggling forms of the larva,
        and very suddenly devours them with a gaping maw seemingly
        hidden under layers of gellish goop. It growls and sparks as
        soon as it has consumed the little critters, their remains 
        still visible through the transparent flesh of the creature.
            You see that it is not only growling, but growing, and you
        back away slowly, trying not let your impending fear turn to 
        terror. While the creature whirs, growls, and transforms into a
        huge blob of gelatin, with teeth and with claws, you hear a
        crashing from the other direction, and you hide under an 
        overturned table, praying this will save you.
            Appearing from behind a destroyed wall is another creature,
        similar to this one, though about a quarter again as large.
        You realize, this must have been the creature from the engine
        room. Was this its offspring.
            The two blob aliens butt heads, the larger one making soft, 
        wet sounds you swear sound like cats cooing. They remain close
        and the smaller one gets on the back of the larger, and they
        absorb into one another, and begin floating to the hatch above
        them. Amazingly, their body seeps through the structure of the 
        steel frame of the ship, and beyond the small hatch window, you 
        can see the strange creature floating out into space, seemingly
        alone in the void, although not as alone as it would appear.
                                   
                          ( 。・_・。)人(。・_・。 )
"""

winning = """ 
        The moment of truth has come.
        There is no light, but the sparks flying from the center of the
        engine, where the huge blob of a creature is gnawing and
        gnashing at the hot and energy rich plasma core. You scan it
        with the analysis tool, it comes up short, but you think there
        could be a good moment of distraction if you fling a well timed
        sonic explosive...except the creature has already spotted you,
        and it growls in terror as it wriggles its way toward you,
        flashing its large teeth folded deep in its torso of colored goo.
            You throw an explosive in panic, unsure of the outcome of it
        as you flee in the other direction. The blob catches it in its 
        huge mouth, and with anticipation you wait for the triumphant 
        splat. But the splat does not come, instead there is only a 
        slight thud and the creature belches...you remember it was 
        eating nuclear plasma a minute ago, and it all makes sense.
            You're able to briefly outrun the creature, and you hide
        behind an overturned table. You are near the decompression 
        chambers. You ready aim of the mining interface, setting the
        beam to pierce. The creature eeks closer, angry, loud, crawling
        over all debree and leaving an acidic trail in its wake. It is
        now or never, and you take your shot. Zapp, bang. How is that
        possible? The creature is unaffected. The beam seemingly goes 
        right through it. It is more angry now, and it rushes toward you.
        In a panic, you pull down the visor of your helmet on your space
        suit and blast the chamber doors. VVVWWWWWoooooooossssshhhhhh
        The vaccuum of space is immediate, and the creature is pulled
        out into the outer darkness.
            You crawl past the next set of lockable doors, and establish
        a new vaccuum in the ship, and breath a sigh of relief. It took
        almost everything, but you may be safe to leave, if you can just 
        get a pod working.
                                    (>‿◠)✌          
"""

losing = """ 
        Your presence alerts the creature, but you don't have the 
        adequate equipment to fight the it, and are quickly devoured 
        and processed as space sludge.
"""

melting = """
        WARNING: ENGINE SYSTEMS AT 0%, PREPARE FOR PLASMATIC MELTDOWN
        10, 9, 8 ....

        The alarm for the countdown timer has begun, and you have failed
        to defeat the creature and escape the ship.
        You imagine what it will be like to turn into particles just as
        the ship explodes.
"""

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
####
#####ASCII ART
####
def flight_deck_title():
    print(" _      ___   __       ___     _    _   _     ")
    print("|_  |    |   /__  |_|   |     | \  |_  /   |/ ")
    print("|   |_  _|_  \_|  | |   |     |_/  |_  \_  |\\")
    return


def navigation_room_title():
    print("             ___  __     ___ ___  _         _   _   _       ")
    print("|\ |  /\ \  / |  /__  /\  |   |  / \ |\ |  |_) / \ / \ |\/| ")
    print("| \| /--\ \/ _|_ \_| /--\ |  _|_ \_/ | \|  | \ \_/ \_/ |  | ")
    return


def dining_hall_title():
    print(" _  ___      ___       __                 ")
    print("| \  |  |\ |  |  |\ | /__  |_|  /\  |  |  ")
    print("|_/ _|_ | \| _|_ | \| \_|  | | /--\ |_ |_ ")
    return


def greenhouse_title():
    print(" __  _   _  _           _       __  _ ")
    print("/__ |_) |_ |_ |\ | |_| / \ | | (_  |_ ")
    print("\_| | \ |_ |_ | \| | | \_/ |_| __) |_ ")
    return


def cargo_bay_title():
    print(" _       _   __  _    _          ")
    print("/   /\  |_) /__ / \  |_)  /\ \_/ ")
    print("\_ /--\ | \ \_| \_/  |_) /--\ | ")


def crew_quarters_title():
    print(" _  _   _          _            _ ___ _  _   __ ")
    print("/  |_) |_ \    /  / \ | |  /\  |_) | |_ |_) (_  ")
    print("\_ | \ |_  \/\/   \_X |_| /--\ | \ | |_ | \ __) ")
    return


def science_deck_title():
    print(" __  _ ___  _       _  _   _   _  _    ")
    print("(_  /   |  |_ |\ | /  |_  | \ |_ /  |/ ")
    print("__) \_ _|_ |_ | \| \_ |_  |_/ |_ \_ |\ ")
    return


def decompression_chambers_title():
    print(" _   _  _  _        _   _   _  __  __ ___  _        ")
    print("| \ |_ /  / \ |\/| |_) |_) |_ (_  (_   |  / \ |\ |  ")
    print("|_/ |_ \_ \_/ |  | |_  | \ |_ __) __)__|__\_/ | \|  ")
    print("                /  |_|  /\  |\/| |_) |_ |_) (_   ")
    print("                \_ | | /--\ |  | |_) |_ | \ __)")
    return


def engine_room_title():
    print(" _       __ ___       _   _   _   _       ")
    print("|_ |\ | /__  |  |\ | |_  |_) / \ / \ |\/| ")
    print("|_ | \| \_| _|_ | \| |_  | \ \_/ \_/ |  |")
    return


def hardware_storage_title():
    print("          _   _              _   _   __ ___ _   _        __  _ ")
    print("|_|  /\  |_) | \ \    / /\  |_) |_  (_   | / \ |_)  /\  /__ |_ ")
    print("| | /--\ | \ |_/  \/\/ /--\ | \ |_  __)  | \_/ | \ /--\ \_| |_")
    return


def escape_pod_bay_title():
    print(" _  __  _       _   _   _   _   _   ")
    print("|_ (_  /   /\  |_) |_  |_) / \ | \  ")
    print("|_ __) \_ /--\ |   |_ _|   \_/ |_/  ")
    print("                  |_)  /\ \_/    ")
    print("                  |_) /--\ | ")
    return


def print_the_end_losing():
    print(""" 
            __ __|   |   |   ____|       ____|    \  |   __ \  
               |     |   |   __|         __|       \ |   |   | 
               |     ___ |   |            |      |\  |   |   | 
              _|    _|  _|  _____|      _____|  _| \_|  ____/  
                             (THE END) """)
    return

def print_the_end_winning():
    print("""
         ████████ ██   ██ ███████     ███████ ███    ██ ██████  
            ██    ██   ██ ██          ██      ████   ██ ██   ██ 
            ██    ███████ █████       █████   ██ ██  ██ ██   ██ 
            ██    ██   ██ ██          ██      ██  ██ ██ ██   ██ 
            ██    ██   ██ ███████     ███████ ██   ████ ██████  
    """)
    return


def print_invalid():
    print("""
            ██ ███    ██ ██    ██  █████  ██      ██ ██████  
            ██ ████   ██ ██    ██ ██   ██ ██      ██ ██   ██ 
            ██ ██ ██  ██ ██    ██ ███████ ██      ██ ██   ██ 
            ██ ██  ██ ██  ██  ██  ██   ██ ██      ██ ██   ██ 
            ██ ██   ████   ████   ██   ██ ███████ ██ ██████ 
    """)
    return


def print_title():
    print(""" 
██████╗  █████╗ ███████╗██████╗  █████╗ ██╗     ██╗   ██╗███████╗                                                              
██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██║     ██║   ██║██╔════╝                                                              
██║  ██║███████║█████╗  ██║  ██║███████║██║     ██║   ██║███████╗                                                              
██║  ██║██╔══██║██╔══╝  ██║  ██║██╔══██║██║     ██║   ██║╚════██║                                                              
██████╔╝██║  ██║███████╗██████╔╝██║  ██║███████╗╚██████╔╝███████║                                                              
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝                                                              
██████╗ ██╗███████╗ █████╗ ███████╗████████╗███████╗██████╗                                                                    
██╔══██╗██║██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗                                                                   
██║  ██║██║███████╗███████║███████╗   ██║   █████╗  ██████╔╝                                                                   
██║  ██║██║╚════██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗                                                                   
██████╔╝██║███████║██║  ██║███████║   ██║   ███████╗██║  ██║                                                                   
╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                                                                   
      ____    ___ _  _ ___    ____ ___  _  _ ____ _  _ ___ _  _ ____ ____ 
      |__|     |   \/   |     |__| |  \ |  | |___ |\ |  |  |  | |__/ |___ 
      |  |     |  _/\_  |     |  | |__/  \/  |___ | \|  |  |__| |  \ |___ 
                              (DAEDALUS DISASTER)
                                  (a txt adventure)
            """)
    return


def print_warning():
    print(""" 
        ██     ██  █████  ██████  ███    ██ ██ ███    ██  ██████  ██ ██ ██ 
        ██     ██ ██   ██ ██   ██ ████   ██ ██ ████   ██ ██       ██ ██ ██ 
        ██  █  ██ ███████ ██████  ██ ██  ██ ██ ██ ██  ██ ██   ███ ██ ██ ██ 
        ██ ███ ██ ██   ██ ██   ██ ██  ██ ██ ██ ██  ██ ██ ██    ██          
         ███ ███  ██   ██ ██   ██ ██   ████ ██ ██   ████  ██████  ██ ██ ██
            """)
    return
####
####_MAIN__
####
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
        
        print('status_code', status_code)
        
        if being_polite == 1 and len(inventory) == 6:
            print("""
        ________________________________________________________________
        
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
        You must be stressed, because that didn't make any sense  ( -_-) """)
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
