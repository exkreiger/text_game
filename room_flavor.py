from text_art import *
from tables import *

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
                it appears most of your fellow crew mates have fled. However, 
                you can hear someone sobbing in the corner behind a bunk. They 
                have their face in their hands, and are shaking slightly. 
                You try to get some information, but all they can say is
                "Monster...eating the engine...ate everybody." You gulp,
                trying not to think about the details behind the muttered words.
                They add in, "The last pod is damaged, and the engine....the
                engine..." Just as your crew mate starts to meander off into
                despair once more, the alarm starts to blair, and
                the harsh robotic voice announces that the self-destruct system
                has been activated.
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
                    So long space goops -- you're on to brighter pastures!
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
