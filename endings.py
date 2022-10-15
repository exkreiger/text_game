from room_flavor import *
from text_art import *

def confrontation(room, inventory):
    if 'space larva' in inventory and 'odd blob of space jelly' in inventory:
        print(bonus)
        print()
        print_the_end_winning()
    elif len(inventory) >= 6 and room in ending_rooms:
        engine_room_title()
        room_print(9)
        print(winning)
        room_print(11)
        print()
        print_the_end_winning()
    else:
        engine_room_title()
        room_print(9)
        print(losing)
        print_the_end_losing()
    return


def meltdown(room, countdown):
    if countdown <= 0 and room in ending_rooms:
        print(melting)
        print_the_end_losing()
    else:
        print('There is still time before the Daedalus destructs...')
    return



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
                You have arrived at the engine room, where you see the 
                horrendous creature eating the pure energy from the plasma 
                engine, roaring and tearing at the fabric of the ship. Your 
                presence alerts the creature, but you don't have the adequate 
                equipment to fight the it, and are quickly devoured and 
                processed as space sludge.
"""

melting = """
                WARNING: ENGINE SYSTEMS AT 0%, PREPARE FOR PLASMATIC MELTDOWN
                10, 9, 8 ....

                The alarm for the countdown timer has begun, and you have failed
                to defeat the creature and escape the ship.
                You imagine what it will be like to turn into particles just as
                the ship explodes.
"""

