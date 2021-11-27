# The script of the game goes in this file.

#Test: Custom Text Tags
#Registering channel for ambient noise (Fire, rain)
init python:
    renpy.music.register_channel("ambient1","sfx",True,tight=True)
    renpy.music.register_channel("ambient2","sfx",True,tight=True)
#     def xpos_tag(tag, argument, contents):
#
#         size = int(argument) * 20
#
#         return [
#                 (renpy.TEXT_TAG, u"size={}".format(size)),
#             ] + contents + [
#                 (renpy.TEXT_TAG, u"/size"),
#             ]
#
#     config.custom_text_tags["xpos"] = xpos_tag

# ===== List of all persistent variables

#Number of times the game has been played
define persistent.timesPlayed = 0

# Default player name (persistent)
init:
    default persistent.povname = "Charlie"

init python:
    def name_func(newstring):
        store.persistent.povname = newstring

default persistent.nameSet = False

define pov = Character("[persistent.povname]")

# Default player name (non persistent)
define povname = ""

#Protagonist pronouns
define he = "he"
define He = "He"
define his = "his"
define His = "His"
define him = "him"
define Him = "Him"
define Hes = "He's"
define hes = "he's"

#persistent pronouns
default persistent.he = "he"
default persistent.He = "He"
default persistent.his = "his"
default persistent.His = "His"
default persistent.him = "him"
default persistent.Him = "Him"
default persistent.Hes = "Hes"
default persistent.hes = "hes"

#Act 1, Chapter 1 - the 3 Godfathers
define firstManWho = False
define secondManWho = False
define thirdManWho = False
define godfather = "none"

#The intro menu with questions
define introHappy = False
define introNeighbours = False

#Act 1, Chapter 2: The road to the village
#How many pitiful Noooo's have you shouted
define pitiful = 1
#Did you keep the pig?
define pig = False
#Have you seen the mushroom utter the password for her house?
define mushroomPassword = False
#Have you seen the mushroom's cavern?
define mushroomCavernSeen = False
#How far have you gotten with each character?
define mushroomArc = 0
define thiefArc = 0
define toadArc = 0
define witchArc = 0

#Mushroom stuff
#Have the mushroom threatened to curse you?
define mushroomCurse = False
define mushroomConfuse = False
define mushroomTea = False
define mushroomAllThis = False
define mushroomIntruding = False
define mushroomBody = False
define mushroomCurseChat = False
#Has the master thief stolen from you?
define stuffStolen = False

#=====Act 2, Chapter 1: The Village Feast
define foodLook = False

#Conversation topics with the toad
define toadFeast = False
define toadLong = False
#define toadDecline = False
define toadConvo2Spoke = False
define toadHelp = False
define banquetChat = False
define toadThief = False
define toadFind = False
define toadStole = False
define toadStole2 = False

#Conversation topics with the villagers
define villagersPlan = False
define villagersCatch = False
define villagersEscape = False
define villagersWitch = False

#Each villager's conversation tree
#TK: Add multiple of these for each run
define gloommongerChat = 0
define goosemongerChat = 0
define sparrowherderChat = 0
define hunterChat = 0
define mayorChat = 0
define wellChat = 0
define pigChat =0

#Random chances
define sparrowherderRand = renpy.random.randint(1,2)
define pig2Rand = renpy.random.randint(1,6)
define wellRand = renpy.random.randint(1,3)

#=====Act 2, chapter 2: The Thief
#What you trapped the chest with
define chest = ""
#Conversation topics with the thief
define thiefWrong = False
define thiefChestCake = False
define thiefFam = False
define thiefLimb = False
define thiefHobbies = False
define thiefPet = False
define thiefDream = False
define thiefNightmare = False
define thiefLike = False
define thiefDislike = False
define thiefCroc = False
define thiefHelp = False
#the number of conversation options picked so far
define ThiefConvo3Options = 0
#Scraggs McKenzie conversation
define scraggsBoys = False
define scraggsMusical = False
define scraggsBoys = False
#did you tell the thief to keep it short
define thiefShort = False
#Did you refuse to go with the devil
define devilRefused = False

#Options during the fight with the mushroom
define mushroomFight = False
define mushroomGems = False
define mushroomRun = False
#Options in the Goblin Train
define goblinSit = False
define goblinLook = False
define goblinDrink = False
define goblinCelebrate = False
define goblinFood = False
define thiefPlace = False


#=====Act 2, chapter 2: The Toad
define puddleLook = False
define puddleStick = False
define toadSad = False


#=====Act 2, chapter 3: The Witch
#Conversation topics with the witch
define witchTea = False
define witchMeeting = False
define witchGodfather = False
define witchFestival = False
define witchPlace = False

#===== Act 3 - The Thief Finale
define thiefJunior = False
define thiefApprentice = False

#=====Act 3 - The Witch Finale with The Devil
#Grandma's questions
define witchFree = False
define escapeGodfather = False
define escapeHell = False
define cureWitch = False
define hollowFeeling = False
define villageRich = False
#Number of questions asked
define dgAsked = 0

#Act 3 - The Toad Finale with Brildebrogue Chippingham
#First conversation with the Toad in his house.
define toadCave = False
define toadWhere = False
define toadBasement = False

#Have you visited each tower?
define firstTower = False
define secondTower = False
define thirdTower = False
define fourthTower = False
define fifthTower = False
define sixthTower = False
#Have you visited each tower a second time?
define firstTower2 = False
define secondTower2 = False
define thirdTower2 = False
define fourthTower2 = False
define fifthTower2 = False
define sixthTower2 = False
#How many times have you run away from Brildebrogue in the escape scene
define escapeB = 0

#The final encounter with Death on the witch's path
define deathMessengers = False
define deathGoodbye = False

#Act 3 - The Mushroom finale
#Conversation options
define mushroomPlace = False
define mushroomImprisoned = False
define mushroomMyself = False
define mushroomFood = False
define mushroomPerson = False
define mushroomMoss = False
define mushroomFeast = False
define mushroomEmbassy = False
define mushroomPale = False
define mushroomDeathTale = False


###==== Defining all images
#The position to show the background illustrations
init:
    $ artPos = Position(xpos=0.5, xanchor=0.5, ypos=35, yanchor=0)

##====Full Screen Images
image cover = "cover.png"
image cover5 = "cover-5.png"
image cover6 = "cover-6.png"
image cover9= "cover-9.png"
image cover11= "cover-11.png"
image cover14= "cover-14.png"
image title = "title.png"
#image credits = "acknowledgements.png"

##====GUI Elements
image firelight animated:
    "firelight-1.png"
    pause 0.1
    "firelight-2.png"
    pause 0.1
    "firelight-3.png"
    pause 0.1
    "firelight-2.png"
    pause 0.1
    repeat

##====Backgrounds
image treesbg= "Backgrounds/trees.png"
image nightbg= "Backgrounds/night.png"
image nightgodbg= "Backgrounds/nightgod.png"
image cottagebg= "Backgrounds/cottage.png"
image forestbg= "Backgrounds/forest.png"
image darkforestbg= "Backgrounds/darkForest.png"
image sunbg= "Backgrounds/sun.png"
image winterbg= "Backgrounds/winter.png"
image darkForestbg= "Backgrounds/darkForest.png"
image darkForest2bg= "Backgrounds/darkForest2.png"

image manorintbg= "Backgrounds/manor-int.png"
image hellbg= "Backgrounds/hell.png"

image townfeastbg= "Backgrounds/town-feast.png"
image townoutbg= "Backgrounds/town-out.png"
image treecanopybg= "Backgrounds/tree-canopy.png"

##====Names
image witchName= "Names/witch.png"
image thiefName= "Names/thief.png"
image toadName= "Names/toad.png"
image mushroomName= "Names/mushroom.png"
image mushroom2Name= "Names/mushroom2.png"
image mushroom3Name= "Names/mushroom3.png"
image mushroom4Name= "Names/mushroom4.png"
image mumName= "Names/mum.png"
image wibName= "Names/wib.png"
image miwName= "Names/miw.png"
image mirName= "Names/mir.png"
image mysName= "Names/mys.png"
image youName= "Names/you.png"
image dgName= "Names/dg.png"
image bcName= "Names/bc.png"
image hName= "Names/h.png"
image gmName= "Names/gm.png"
image wellName= "Names/well.png"
image scName= "Names/sc.png"
image boysName= "Names/boys.png"
image mayName= "Names/may.png"
image goName= "Names/go.png"
image shName= "Names/sh.png"
image egName= "Names/eg.png"
image townName= "Names/town.png"
image echidnaName= "Names/echidna.png"
image echidna2Name= "Names/echidna2.png"
image somName= "Names/som.png"
image mysFrogName= "Names/mysFrog.png"
image batName= "Names/bat.png"
image ratName="Names/rat.png"
image cockatooName="Names/cockatoo.png"
image crowshrikeName="Names/crowshrike.png"
image thiefMumName="Names/thiefmum.png"
image goblin1Name="Names/goblin1.png"
image goblin2Name="Names/goblin2.png"
image goblin3Name="Names/goblin3.png"
image goblin4Name="Names/goblin4.png"
image goblinqueenName="Names/goblinqueen.png"
image skinmaskName="Names/sm.png"
image p1Name="Names/p1.png"
image p2Name="Names/p2.png"
image p3Name="Names/p3.png"

##====Frippery
image sword="sword.png"
image hand= "gui/hand.png"
image dot= "gui/dot.png"
image tornPage1="tornPage1.png"
image tornPage1bg="tornPage1-bg.png"

image tornPage2="tornPage2.png"
image tornPage2bg="tornPage2-bg.png"

image tornPage3="tornPage3.png"
image tornPage3bg="tornPage3-bg.png"

image stamp="stamp.png"


# ===== Characters
define w = Character("{image=witchName}{alt}The Witch:{/alt}")
define t = Character("{image=thiefName}{alt}The Thief:{/alt}")
define f = Character("{image=toadName}{alt}The Toad:{/alt}")
define m = Character("{image=mushroomName}{alt}The Mushroom:{/alt}")
define m2 = Character("{image=mushroom2Name}{alt}The Mushroom:{/alt}")
define m3 = Character("{image=mushroom3Name}{alt}The Mushroom:{/alt}")
define m4 = Character("{image=mushroom4Name}{alt}The Mushroom:{/alt}")
define mum = Character("{image=mumName}{alt}Mum:{/alt}")
define miw = Character("{image=miwName}{alt}The Man Clad in White:{/alt}")
define mir = Character("{image=mirName}{alt}The Man Clad in Red:{/alt}")
define wib = Character("{image=wibName}{alt}The Woman Clad in Black:{/alt}")
define mys = Character("{image=mysName}{alt}Mysterious and possibly magical old woman:{/alt}")
define pov = Character("{image=youName}{alt}You:{/alt}")
define dg = Character("{image=dgName}{alt}The Devil's Sooty Grandmother:{/alt}")
define bc = Character ("{image=bcName}{alt}Brildebrogue Chippingham:{/alt}")
define h = Character("{image=hName}{alt}The Hunter:{/alt}")
define gm = Character("{image=gmName}{alt}The Old Gloom-monger:{/alt}")
define well = Character("{image=wellName}{alt}The Thing in the Well:{/alt}")
define sc = Character("{image=scName}{alt}Scraggs McKenzie, the Banksia Bounty Hunter:{/alt}")
define boys = Character("{image=boysName}{alt}The Boys:{/alt}")
define may = Character("{image=mayName}{alt}The Mayor:{/alt}")
define go = Character("{image=goName}{alt}The Young Goose-Girl:{/alt}")
define sh = Character ("{image=shName}{alt}The Sparrow-Herder:{/alt}")
define eg = Character ("{image=egName}{alt}The Enigmatic Gentleman:{/alt}")
define town = Character ("{image=townName}{alt}The Entire Town:{/alt}")
define echidna = Character ("{image=echidnaName}{alt}Echidna (which happened to be passing by at just that moment):{/alt}")
define echidna2 = Character ("{image=echidna2Name}{alt}Echidna (now holding a large sack):{/alt}")
define som = Character ("{image=somName}{alt}The Strange (and crooked) Old Man:{/alt}")
#Note: blank character for particular scenes where I need it (eg to preserve the hand on brildebrogue chippingham's manor
define blank = Character ("")
define mysFrog = Character ("{image=mysfrogName}{alt}Mysterious (yet inexplicably handsome) Frog:{/alt}")
define bat = Character ("{image=batName}{alt}The Bat:{/alt}")
define rat = Character ("{image=ratName}{alt}The Rat:{/alt}")
define cockatoo = Character ("{image=cockatooName}{alt}The Black Cockatoo:{/alt}")
define crowshrike = Character ("{image=crowshrikeName}{alt}The Crow-Shrike:{/alt}")
define thiefmum = Character ("{image=thiefMumName}{alt}The Thief's Mother:{/alt}")
define goblin1 = Character ("{image=goblin1Name}{alt}Goblin:{/alt}")
define goblin2 = Character ("{image=goblin2Name}{alt}Goblin:{/alt}")
define goblin3 = Character ("{image=goblin3Name}{alt}Goblin:{/alt}")
define goblin4 = Character ("{image=goblin4Name}{alt}Goblin:{/alt}")
define goblinQueen = Character ("{image=goblinqueenName}{alt}The Goblin Queen:{/alt}")
define sm = Character ("{image=skinmaskName}{alt}The Skin Mask:{/alt}")
define p1 = Character ("{image=p1Name}{alt}The First Pig:{/alt}")
define p2 = Character ("{image=p2Name}{alt}The Second Pig:{/alt}")
define p3 = Character ("{image=p3Name}{alt}The Third Pig:{/alt}")

###==== Defining all Audio

## Sound effects
define audio.pageFlip = "audio/page-flip.mp3"
define audio.rain = "audio/rain.wav"
define audio.fire = "audio/fire.mp3"

#screen music_screen:
    #show firelight animated onlayer over_screens zorder 99
    #zorder 99
    #$ renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True)
    #$ renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True)
    #python:
    #       renpy.music.play("audio/rain.wav", fadeout=10.0, fadein=15.0)

# The game starts here.

#Splashscreen - The front cover of the book that appears before the main menu.

label before_main_menu: #splashscreen - changed to before_main_menu so it always displays
    scene black
    show firelight animated onlayer over_screens zorder 99
    #Shows a random cover each time. 13.32% chance of a variant cover.
    $randomCover = renpy.random.randint(1, 30)
    if randomCover <=22:
        show cover with dissolve
    elif randomCover ==23 or randomCover == 24:
        show cover14 with dissolve
    elif randomCover ==25 or randomCover == 26:
        show cover5 with dissolve
    elif randomCover ==27 or randomCover == 28:
        show cover6 with dissolve
    elif randomCover ==29 or randomCover == 30:
        show cover9 with dissolve
    #$ renpy.music.play("audio/rain.wav", fadein=0.5, channel="music", loop=True)
    #$ renpy.music.play("audio/wildlife.wav", fadein=0.5, channel="ambient1", loop=True)
    $renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True)
    #with Pause(5)
    ""
    play sound pageFlip
    show title
    ""
    #with Pause(5)
    #show screen music_screen
    #Ambient rain loop
    #play music rain loop volume fadein 1.0
    #Ambient fireplace sounds loop
    #play audio fire loop volume 0.5 fadein 1.0

    play sound pageFlip
    if persistent.nameSet == False:
        call screen contents
    else:
        #$povname = persistent.povname
        #Using the persistent character info to define the temporary pronouns
        #This is really just done so that I don't need to write [persistent.he] every time I use a pronoun
        define he = persistent.he
        define He = persistent.He
        define his = persistent.his
        define His = persistent.His
        define him = persistent.him
        define Him = persistent.Him
        define Hes = persistent.Hes
        define hes = persistent.hes
        define povname = persistent.povname
        #show screen main_menu
        #$renpy.set_return_stack([])
        #$renpy.set_return_stack([])
        #$renpy.pop_call()
        return
        #$renpy.full_restart()

#Before main menu: Making sure the animated firelight always displays
# label before_main_menu:
#     show firelight animated onlayer over_screens zorder 99
#     $renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True)
#     #$ renpy.music.play("audio/wildlife.wav", fadein=0.5, channel="ambient1", loop=True)
#
#     return


label after_load:
    play sound pageFlip
    #$ renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True)
    #$ renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True)
    #$ renpy.music.play("audio/wildlife.wav", fadein=0.5, channel="ambient1", loop=True)
    $renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True)
    return

label start:
    show firelight animated onlayer over_screens zorder 99
    #$ renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True)
    $ renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True)
    #$ renpy.music.play("audio/wildlife.wav", fadein=0.5, channel="ambient1", loop=True)

    label chapter1:
        scene bg page
        show treesbg at artPos
        "This maybe happened, or maybe did not."
        "The time is long past, and much is forgot."
        "Back in the old days, when wishing worked, your mother had twelve children and had to work night and day just to feed them."
        "When you were born as the thirteenth, she had no idea what to do. She took you up in her arms and ran into the darkness of the forest, promising that she would ask the first man she met to be your Godfather."
        "In the darkness of the forest, she may or may not have met a man in white."
        "(Is anything certain these days?)"
        "His right hand held a dove. His other hand held a gun. His other hand held a crisp dollar bill. His other hand held a pillar of fire."
        "His suit was perfect. His face was too bright to look upon. He already knew what was on her mind."
        miw "Poor woman. Let me be the Godfather."
        miw "I shall hold this child, and make sure that [hes] happy on this Earth for the rest of [his] days."

    label firstMan:
            show hand onlayer transient:
                yalign 0.7#0.743
                xalign 0.5
            menu:
                miw "I will only ask one thing: [He] must work hard, and earn every dollar, and obey me above all else."
                #"{image=sword}{space=15}If she said yes, turn to page 13.": #"Yes.":
                #"{image=dot}{space=10}If she said yes, turn to page 13.": #"Yes.":
                "If she said yes, turn to page 13.": #"Yes.":
                    miw "As I have foreseen."
                    "He bowed down and placed His great hand upon you, leaving His mark on your right hand."
                    miw "You will name [him] [povname]."
                    if he == "they":
                        miw "I will come for the child the moment [he] turn eighteen. Keep [him] safe for me until then."
                    else:
                        miw "I will come for the child the moment [he] turns eighteen. Keep [him] safe for me until then."
                    mum "Alright. Make sure you're there for the christening."
                    show hand onlayer transient:
                        yalign 0.71#0.743
                        xalign 0.5
                    "But He was already gone.{vspace=200}{i}In your notes, write down that {b}You are the Godchild of the King of Kings.{/b}{/i}"
                    $godfather = "White"
                    jump chapter2
                "If she said no, turn to page 14." if firstManWho:#"No."
                    mum "Then I don't want you as the Godfather. You give to the rich, and take from the poor. You are no Lord of mine."
                    "(She said this foolish thing, with no understanding of how wisely the Lord distributes wealth and poverty.)"
                    "Then she turned away from Him and ran into the forest."
                    jump secondMan1
                "If she asked the mysterious figure who He was, turn to page 11." if not firstManWho:#"Who are you?"
                    miw "I am your dear Lord."
                    $firstManWho = True
                    jump firstMan

    label secondMan1:
        "In the deeper darkness of the forest, she may or may not have met a man all in red."
        "(Can we be sure of anything but the greatness of G-d?)"
        "All the jewels of the earth fell from His right hand, and all the pleasures of the world fell from His left, and His other hand held all the wonders of the universe, and His other hand held a fat cigar, and His other hand held a long knife black as coal dust, and His other hand held the most intoxicating spices, such that the King of Kings would cry to taste them, and His other hand held a single dead rose, and His other hand was in his pocket and out of view."
        mir "Poor woman. Let me be the Godfather."
        mir "I'll make sure the child needs nothing, and wants everything. [He] will live in wealth and comfort for all of [his] days, and devour only the richest meats for every meal."
        label secondMan2:
            show hand onlayer transient:
                yalign 0.71#0.743
                xalign 0.5
            menu:
                mir "I only have one condition: [He] must promise to obey no master, and scorn the rule of law, and do as [he] wilt every day of [his] life."
                "If she said yes, turn to page 21.":#"Yes.":
                    mum "Beggars can't be choosers, I suppose."
                    mir "Excellent!"
                    "He let out a great shrieking cackle and placed His mark upon you."
                    mir "You will name [him] [povname]."
                    if he == "they":
                        mir "I will come for the child the moment [he] turn eighteen. Keep [him] safe for me until then."
                    else:
                        mir "I will come for the child the moment [he] turns eighteen. Keep [him] safe for me until then."
                    mum "Alright. Just make sure you're there for the christening on sunday."
                    show hand onlayer transient:
                        yalign 0.71#0.743
                        xalign 0.5
                    "But He was already gone.{vspace=200}{i}In your notes, write down that {b}You are the Devil's Godchild.{/b}{/i}"
                    $godfather = "Red"
                    jump chapter2
                "If she said no, turn to page 16." if secondManWho:
                    mum "Then I don't want you as the Godfather. You lie, and cheat, and lead good people astray."
                    "She turned away from him, and raced deeper into the forest."
                    jump thirdMan1
                "If she asked the mysterious figure who He was, turn to page 18." if not secondManWho:
                    mir "Why, I am the Devil Himself."
                    $secondManWho = True
                    jump secondMan2
    label thirdMan1:
        "In the deepest darkness of the forst, she may or may not have met a handsome woman."
        "(What can any of us be certain of, except that the mercies of the Almighty are vaster than the deepest ocean and more numerous than all the pebbles on the land?)"
        "She was broken-limbed and clad all in black. She had no hands."
        wib "Poor woman. Let me be the Godmother."
        wib "The child will have nothing. [He] will need nothing."

        label thirdMan2:
            show hand onlayer transient:
                yalign 0.68#0.743
                xalign 0.5
            menu:
                wib "[He] need make no promises. I have no demands."
                "If she said yes, turn to page 17.":
                    mum "You're just the right one. You take rich and poor without distinction."
                    wib "You did not have a choice."
                    "In one swoop She bowed down and placed Her mark upon you."
                    wib "You will name [him] [povname]."
                    if he == "they":
                        wib "The moment [he] turn eighteen, [he] will be mine."
                    else:
                        wib "The moment [he] turns eighteen, [he] will be mine."
                    wib "Keep [him] safe for me until I come for [him]. I will send three messengers before me, to announce my arrival. "
                    mum "Alright. Make sure you're there for the christening on sunday."
                    show hand onlayer transient:
                        yalign 0.77#0.743
                        xalign 0.5
                    "But She was already leaving. She sunk into the earth with Her long, broken legs trailing behind her, until she was swallowed up whole.{vspace=160}{i}In your notes, write down that {b}You are Death's Godchild.{/b}{/i}"
                    $godfather = "Black"
                    jump chapter2
                "If she said no, turn to page 25." if thirdManWho:
                    mum "I don't want you as the Godmother. You take men before it is their time."
                    wib "You should have thought of that sooner."
                    wib"There is no-one else left to take [him]."
                    "In one swoop She bowed down and placed Her mark upon you."
                    wib "You will name [him] [povname]."
                    if he == "they":
                        wib "The moment [he] turn eighteen, [he] will be mine."
                    else:
                        wib "The moment [he] turns eighteen, [he] will be mine."
                    wib "Keep [him] safe for me until I come for [him]. I will send three messengers before me, to announce my arrival. "
                    mum "Alright then. Beggars can't be choosers. Make sure you're there for the christening on sunday."
                    show hand onlayer transient:
                        yalign 0.77#0.743
                        xalign 0.5
                    "But She was already leaving. She sunk into the earth with Her long, broken legs trailing behind her, until she was swallowed up whole.{vspace=160}{i}In your notes, write down that {b}You are Death's Grandchild.{/b}{/i}"
                    $godfather = "Black"
                    jump chapter2
                "If she asked the mysterious figure who She was, turn to page 18." if not thirdManWho:
                    mum "I don't know you."
                    wib "Everybody knows me."
                    "She tilted her head so that the moonlight fell on it, and your mother saw that it was true. It was Lady Death herself."
                    $thirdManWho = True
                    jump thirdMan2
    scene bg rainforest

# Act 1, Chapter 2: The Path
label chapter2:
    if godfather == "White":
        "And so you grew up as a kind and well-mannered child, and you made your mother proud."
        "You went to church every Sunday, and worked hard every day of your life, and every day you gave thanks to the invisible hand of the free market. All the neighbours smiled and said \"That one has the mark of G-d on [him].\""
        "Your Godfather was as good as His word. He appeared at church for the christening, and blessed you."
        "You soon found luck was always in your favour, and everyone took to calling you \"Fortune's Favourite\"."
    elif godfather == "Red":
        "And so you grew up as a wild and willful child, and your drove your mother to distraction with your wickededness."
        "You obeyed no laws and no masters, and you roamed heedlessly across the hills and dales, cackling wildly and throwing mud in your wake, and all the neighbours said \"That one has the Devil's mark on [him],\" and shut their doors."
        "This so grieved your mother that she fell down dead."
        #"Your Godfather was as good as His word, although He could only watch the christening from outside the church window."
        "In spite of this, you still did not mend your wicked ways. Your ill deeds were rewarded, for you soon found that you could scarcely trip over a stone without unearthing precious diamonds and gems, and you became rich beyond the dreams of avarice."
    elif godfather == "Black":
        "And so you grew up as a solemn and quiet child, and you made your mother sick with worry with your gloomy ways."
        "You ate very little, and said even less, and every night you would stalk quietly through the forest shadows or sit for long hours watching insects crawl in stagnant ponds, and all the neighbours said \"That one has the mark of Death on [him],\" and shut their doors."
    if godfather == "Red":
        "You lived with your twelve siblings in a house on stilts on the banks of a muddy river in a vast rainforest."
    else:
        "Your mother loved you very much, and you lived with her and your twelve siblings in a house on stilts on the banks of a muddy river in a vast rainforest."

    label introMenu:
        show hand onlayer transient:
            yalign 0.68#0.743
            xalign 0.5
        menu:
            "You woke every morning to the chorus of birds, and fell asleep every evening to the roaring of crickets."
            "If you want know about your neighbours, turn to page 26." if not introNeighbours:
                $introNeighbours = True
                "Ah! In fact, this river and all the woods around it were owned by a wise mushroom ambassador, who had owned these lands since before anyone could remember."
                "She was often away brokering trade agreements and peace treaties and delicate alliances between the many trees and plants and old warring ferns of the forest, who were always butting heads over one thing or another."
                "But every now and then, on cold clear nights, you could see her walking through the depths of the forest with her white veil and delicate waves of silver spores drifting behind her."
                "She allowed your family to live on the river and use her lands, under one condition."
                m "Ask not of what concerns you not, lest you hear what pleases you not."
                "Your family accepted her wishes, and so you let each other be."
                jump introMenu
            "If you wonder whether you were happy there, turn to page 19." if not introHappy:
                $introHappy = True
                if godfather == "Red":
                    "Well, it was a rich house, and you had everything you could ever want and more. But still, sometimes you would get a hollow feeling inside you, and walk out of the house to stare into the dark woods beyond."
                else:
                    "Well, it was a happy house. But still, sometimes you would get a hollow feeling inside you, and walk out of the house to stare into the dark woods beyond."
                "No matter how many people were around you, you felt like something was missing."
                "Every year, on the day before your birthday, the village would throw a great festival for no reason anyone could name. On these nights you always felt sad and strange."
                "You would avoid the festival and stare deep into the woods all through the night."
                jump introMenu
            "To continue the story, turn to page 34.":
                if godfather == "Black":
                    "Alas, all too soon, the eve of your 18th birthday arrived. You set about in wild terror, for you knew that your Godmother would own your immortal soul as as soon as the clock struck midnight."
                    "You had no doubt that She would soon send Her three messengers for you, and then take you down to the kingdom of ruin forever."
                else:
                    "Alas, all too soon, the eve of your 18th birthday arrived. You set about in wild terror, for you knew that your Godfather would come to take you away as soon as the clock struck midnight, and you had no wish to leave just yet."
    if godfather == "Red":
        "The closer the hour grew, the more frantic you became. You knew you would soon pay dearly for all your years of wicked indolence."
        pov "I know. I'll go to the village festival this eve. There will be travellers there from all over this haunted land. Surely one of them will know how to save me from my terrible fate."
        "You gathered up your coinpurse, along with some bread and meat for the journey, and resolved to travel until you found a way to escape the Devil."
    else:
        mum "You must go to the festival, my child. There will be travellers there from all over this wild earth. Surely one of them will know how to save you from this terrible fate."
        "She gave you a thick coinpurse, and some bread and meat for the journey."
        mum "Go! But be careful of strangers, and do not leave the path."
        mum "A terrible {color=#f00}wolf{/color} lurks out there, in the space between the trees."
    "And so you took up your belongings and strode on down the road to the festival."
    "The twilight set in, and the crickets and cicadas all around you set about with their chattering and squabbling, and the evening birds began to laugh and trill, and you could feel the wet cool mist of the rainforest settle around you."
    "The crooked old water-dragons looked sideways at you and plotted their long, slow schemes."
    "A small turtle saw you coming and fled into the water with a plop."

    # Act 1, Chapter 3: The Mushroom.
    #You follow the mushroom and find a bunch of mushroom clones
    "As you walked down the road, you saw the wise mushroom moving through the deep darkness of the trees, her pale spores flowing in a train behind her."
    show hand onlayer transient:
        yalign 0.7#0.743
        xalign 0.5
    menu:
        "In her left hand she held a small lantern, and in her right hand she held a crooked knife stained green."
        #TK: Include extra options if you have different grandparents (eg a wicked option if your godfather is the devil
        "If you followed her, turn to page 25.":
            "You left the path and followed her from a distance."
            "She walked into the towering buttress roots of an ancient fig and cut the vines and swamp flowers from it to reveal a small blue door, inlaid with precious sapphires and intricate engravings."
            show hand onlayer transient:
                yalign 0.73#0.743
                xalign 0.5

            m "Gorge, guzzle, gulp and grab; never shall this wound scab.{vspace=160}{i}In your notes, write down that you {b}know the password.{/b}{/i}"
            $mushroomPassword = True
            show hand onlayer transient:
                yalign 0.72#0.743
                xalign 0.5
            menu:
                "With this, the door opened before her, and she vanished inside immediately."
                "If you entered the door, turn to page 26.":
                    $mushroomArc +=1
                    $mushroomCavernSeen = True
                    "You quickly snuck inside before the door closed behind you."
                    #TK: Double check my descriptions on the heat - is it consistently hot rainforest sweaty weather
                    "Inside you were shocked to find the tree completely hollow. A great cavern was formed inside it, cold as ice despite the heat outside."
                    "The floor of the cavern was piled with rubies and sapphires and glinting emeralds and solid gold pieces, larger than your fist."
                    "All across the room you saw lush silks and pillars of precious metals of every type, and riches that would turn the king of kings green with envy."
                    "The glimmering magenta smoke of incense rolled across the room and coated it all in a dark haze, smelling of the most incredible spices and herbs and enchanting odours."
                    m "Oh darling, what are you doing back again?"
                    "The Mushroom popped up, startling you."
                    m "I'm sure I remember telling you quite clearly never to darken my door again."
                    "She looked off to the side."
                    m "Yes, I'm just telling them now. One moment."
                    m "Have some common courtesy, darling, please. I don't barge into your house looking wild and dishevelled and try to steal the untold riches of your domain, do I?"
                    m "Not without an invitation, at least."
                    label mushroomWater:
                        show hand onlayer transient:
                            yalign 0.63#0.743
                            xalign 0.5
                        menu:
                            m "Out with it, then. What do you want?"
                            "If you asked for some water, turn to page 33." if mushroomTea:
                                pov "Just some water would be nice, please."
                                m "{i}Water?{/i} Really? How... conventional."
                                m "I have to confess, I thought better of you, darling."
                                pov "What's wrong with water?"
                                m "Oh, nothing, nothing. It's fine. If you're into that sort of thing."
                                m "It's just a bit... derivative, isn't it? A bit played out."
                                m "You know, \"I'm a big dumb humanoid, I love digesting liquids in order to sustain my bodily functions, dah de dah de dah\", etc, etc. Is that really the type of harmful stereotype we want to play into?"
                                m "What are we really trying to {i}say{/i} here?"
                                pov "Uh... I can drink something else-"
                                m "No no, don't push yourself, it's fine. We can't all be innovators."
                                m "I'll go get the water. Please, have a seat and relax."
                                #A dark look across her face
                                m "But do not, under any circumstances, go into the basement."
                                "She waved to a small, black door set into the bark of the tree."
                                "An ominous glow shone through the crack beneath it. The wood was marked with strange and terrible sigils. You heard a low whispering beyond."
                                #She immediately brightens up with a smile and a jingle.
                                m "Be right back."
                                jump basement
                            "If you asked about \"The you with the mask\", turn to page 31." if mushroomTea and not mushroomBody:
                                m "I'm sorry darling, it's been a long day already. I don't have time to explain your body to you."
                                m "Again."
                                $mushroomBody = True
                                jump mushroomWater
                            "If you told the mushroom you've never been here before, turn to page 29." if not mushroomConfuse:
                                m "Darling, you're confused, you're babbling, you're all over the place, please, you're a mess. More so than usual, even."
                                m "You were here just a minute ago. The you with the mask and the long legs."
                                m "Perhaps you should sit down and take a moment."
                                m "Can I get you anything? Decaying plant matter? It's all the rage back home."
                                $mushroomConfuse = True
                                $mushroomTea = True
                                jump mushroomWater
                            "If you enquired about the untold riches of her domain (with the gleam of avarice in your heart) turn to page 30." if not mushroomAllThis:
                                "She looked vaguely around the glittering splendor before you."
                                m "Oh, this?"
                                "She dismissed the mountains of jewels with a wave of her hand."
                                m "I told you. All the wealth of the world falls to us in the end."
                                $mushroomAllThis = True
                                jump mushroomWater
                            "If you apologised for intruding and swore to make amends, turn to page 35." if not mushroomIntruding:
                                m "Darling, an apology is as good to me as a beard to a turtle-dove."
                                m "But no, don't worry about it, it's fine, really, completely fine."
                                $mushroomIntruding = True
                                jump mushroomWater
                    label basement:
                        show hand onlayer transient:
                            yalign 0.67#0.743
                            xalign 0.5
                        menu:
                            "She left the room, trusting your kindness and good nature."
                            "If you immediately disobeyed the mushroom and opened the basement door (in accordance with your wicked nature) turn to page 52.":
                                "Of course you opened the basement door."
                                "Within, you saw a most terrible sight."
                                "Seven mushroom corpses hung in the room, dripping black ichor, each being feasted upon by a fat blue-tongued lizard."
                                "Every one of them was identical to the lady Mushroom herself."
                                pov "W-what is this?"
                                m "Fool!"
                                "The mushroom appeared from the earth before you with a terrible crash."
                                m "You have asked about what concerns you not, and so you will hear what pleases you not!"
                                $mushroomCurse = True
                                m "I gave you fair warning, darling. Now all your milk will spoil, all your bread will burn, your socks will always be wet, and you will live in torment for the rest of your days!"
                                pov "Noooooooo!"
                                m "Don't say I didn't tell you so."
                                "You cried out and set about wailing and tearing your clothes and beating yourself upon the ground in pitiful anguish."
                                pov "Please, Lady Mushroom, spare me your curse. If you do, I will tell you a story, the likes of which would cause you to go white with astonishment if you were to hear it."
                                m "Ha! Please."
                                m "I've talked with the ferns, who saw the dinosaurs rise and fall."
                                m "I am one with the mosses and lichens of the land who are even older still. I have talked to ancient trees who saw the great fires and the great floods and still stand."
                                show hand onlayer transient:
                                    yalign 0.7#0.743
                                    xalign 0.5
                                menu:
                                    m "What could you possibly tell me that I don't already know?"
                                    "If you told her about the festival, turn to page 4.":
                                        pov "I'm on my way to the festival, and there will be people there from all over this great earth. Surely one of them will have a story you haven't heard before."
                                    "If you told her about your Godparent, turn to page 62.":
                                        if godfather == "White":
                                            pov "I'm seeking a way to escape being taken by my Godfather, the Almighty Lord. Surely the story of my adventure will be unique enough for you."
                                        elif godfather == "Red":
                                            pov "I'm seeking a way to escape my Godfather, Lucifer. Surely the story of my adventure will be unique enough for you."
                                        elif godfather == "Black":
                                            pov "I'm seeking a way to escape my Godmother, Annihilation. Surely the story of my adventure will be unique enough for you."
                                "The Mushroom grew quiet as she thought over your proposal, and you prayed to the Most High (May He watch over us always) to deliver you from this terrible situation."
                                m "Very well, dear. I'll let you go."
                                m "But be warned: If you fail to return to me this very night with the story you have promised me, then your punishment will be as tenfold."
                                m "You will be fated to trip over a stone and into the ocean and drown, and when you die, your ghost will come back as a wild dog, and harry your mother and father all day and all night, nipping at their heels until they both fall into deep wells and turn into terrible black fish that will lie forever there at the bottom of those wells, moaning weakly and cursing their ungrateful child who has brought them such woe and devastation."
                                #m "All your spoons will stick in your drawers, and your eggs will hatch into foul geese, and your bowls and furniture will roll away down the hills, so that you will have nothing to do but sit on the floor and eat cold porridge with your hands and curse the day you ever decided to cross a mushroom!"
                                pov "Noooooooo!"
                                "She struck the ground. It opened before her and she disappeared into it instantly."
                                "You set about beating yourself and rolling around the floor in even more pitiful devastation and horror than before, tears streaming from your eyes at this terrible curse."
                                "Thus you went on your way to the festival, fretting and worrying all the while."
                                if godfather == "Black":
                                    "Now you had two burdens: To escape the grip of your Godmother, and to find a story that could satisfy the disdainful Mushroom."
                                else:
                                    "Now you had two burdens: To escape the grip of your Godfather, and to find a story that could satisfy the disdainful Mushroom."
                                "\"Never again,\" you cried to yourself, \"Will I ask of what concerns me not!\""
                                jump thief1
                            "If you sat patiently and waited for your tea, turn to page 86.":
                                "In an unlikely turn of events, you sat there and waited patiently, paying no mind to the mysterious door."
                                "(Some protagonist you turned out to be.)"
                                "Soon, the mushroom returned with a cup of water. You took a sip and then coughed violently."
                                pov "Um, excuse me... this is full of compost."
                                m "Yes of course, darling. It's the latest thing."
                                m "It's rich. It's bold. It's avant-guarde. It may not be what you {i}want{/i} right now, but it is what you {i}need{/i}."
                                m "So, what brings you back here?"
                                if godfather == "White":
                                    "You told her of the terrible dilemma with your Godfather, our Dear Lord."
                                elif godfather == "Red":
                                    "You told her of the terrible dilemma with your Godfather, Old Nick."
                                elif godfather == "Black":
                                    "You told her of the terrible dilemma with your Godmother, who rides a pale horse."
                                m "Hmm. Quite the story, darling."
                                m "I must say, you could certainly work on the pacing. And I think the obvious analogy you've drawn for 13th century France and the fragmentation of the Carolingian Empire was a tad heavy-handed. But it's a good start."
                                if godfather == "Black":
                                    m "I know a bit about pale-faced Death. Her house is not far from here. Perhaps -"
                                    "A large grandfather clock in the corner suddenly chimed, and she looked up with a start."
                                    m "Oh dear. Time marches on, even for me."
                                    m "I'm sorry to be so rude but I'd better be off. Come back after the festival, and I may be able to help."
                                    m "Please take care of yourself, dear. All of yourself."
                                    "And before you could reply to this strange remark, she took your cup and ushered you out of the door in an instant."
                                    "You took up your bag and set off down the road once more."
                                    jump thief1
                                else:
                                    m "I'm afraid I don't know if I can help. I know a little about pale-faced Death, but I've never met your godfather."
                                    "A large grandfather clock in the corner suddenly chimed, and she looked up with a start."
                                    m "Oh dear. Time marches on, even for me."
                                    m "I'm sorry to be so rude but I'd better be off. Come back after the festival, and I may be able to help."
                                    m "Please take care of yourself, dear. All of yourself."
                                    "And before you could reply to this strange remark, she took your cup and ushered you out of the door in an instant."
                                    "You took up your bag and set off down the road once more."
                                    jump thief1
                    #"But in the center of the room you saw the most astonishing thing of all."
                    #"Looming over the whole cavern were 3 great pillars of twisted wood and oozing sap."
                    #"In the middle of the pillars writhed 3 figures, gaunt and frail: A pale and shivering Golden Wattle, a crooked Banksia seed, and a fiery Kangaroo Paw."
                    #"The Mushroom took her knife and cut small pieces from her red cap, feeding it to the figures."
                    #"As she did so you saw her weep and wail bitterly, crying out aloud at her misfortune."
                    #INSERT: CHOICE
                "If you went back to the path, turn to page 28.":
                    "You rushed back to the path, worried at any moment that you might be seen."
                    "\"Thank goodness,\" you thought to yourself, \"that I know not to ask of what concerns me not! That could led me to some kind of dangerous and magical adventure.\""
                    "And so you continued on down the path, giving thanks to our Lord for your natural good sense."
                    jump thief1
        "If you ignored her and followed the path like an honest christian, turn to page 42.":
            "You ignored her and kept on walking down the path, just as your mother taught you."
            jump thief1

    # Act 1, Chapter 4: The Thief.
    label thief1:
        "As you were walking down the road thusly, you came upon an old beggar-woman."
        "Her eyes were blind, and her back was crooked in 5 directions at once, and her hair floated all around her head like twisting grey fog, and she hobbled about with only the aid of an old cane to help her along."
        mys "Ho, young traveller."
        show hand onlayer transient:
            yalign 0.72#0.743
            xalign 0.5
        menu:
            mys "Might you lend a hand for a frail old woman? The woods are dark tonight, and I thought I heard howling from the space between the trees."
            #TK: Include option to kick over the old woman if you're the devil child
            "If you help the old woman, turn to page 73.":
                $thiefArc +=1
                $stuffStolen = True
                "You took the old woman's arm to support her weight."
                mys "FOOOOOL!"
                "In a flash her clothes tore asunder, and her mask fell to the ground, and you saw it was all nothing but a disguise."
                "In her stead stood the cunning and terrible form of the Master Thief!"
                #"They were neither tall nor short, neither fat nor thin, neither pale nor tan."
                "They wore a midnight cloak across their back and a cunning look on their sly face."
                t "That's right, it's me! Back again to steal your heart and tear this land asunder!"
                t "No law shall stand, no judge shall know peace and no cop shall sleep easy in their bed at night, for as long as my legs can run!"
                "And with a shout of laughter they demonstrated this, running their long legs into the forest and out of sight."
                "As soon as you tried to chase them you discovered that your clothes had been stolen off your back and replaced with origami paper replicas. Your belt was now a strip of seaweed, your socks were old moss, and you were wearing someone else's shoes."
                label thiefChase:
                    show hand onlayer transient:
                        yalign 0.68#0.743
                        xalign 0.5
                    menu:
                        "Despair gripped you as you tripped over your mismatched shoes."
                        "If you chased after them anyway, turn to page 37.":
                            "You chased after the mocking laughter of the Master Thief, following the shadowy figure as they shed disguises, wigs, belts, and the old cane."
                            "Finally, you caught up to the figure in a forest clearing, and grabbed it tight."
                            if godfather == "White":
                                pov "Now you will face your just punishment, sure as the heavens declare the glory of G-d."
                            elif godfather == "Red":
                                pov "You wretched fool. You should never have tried to out-do me in wickedness."
                            else:
                                pov "I have my grip on you now, sure as Death has Her hand on us all."
                            "You threw the figure to the ground, laughing in triumph."
                            "But as soon as you did so, you realised it was nothing but a pig, wearing a wig and the raggedy cloak of the old woman."
                            "The Master Thief was gone."
                            label thiefchase2:
                                show hand onlayer transient:
                                    yalign 0.69#0.743
                                    xalign 0.5
                                menu:
                                    "Seeing your misfortune, the pig oinked at you sorrowfully and nuzzled you for comfort."
                                    "If you kept the pig, turn to page 53.":
                                        "You picked up the pig and held it under the crook of your arm."
                                        "From that day on he would always be your loyal friend and ally, and the two of you would get through more scrapes and misadventures than I have time to relate tonight."
                                        $pig = True
                                    "If you let the pig run free and wild, as nature intended, turn to page 8.":
                                        "With sorrow, you removed the cloak and wig, and gave the pig his freedom."
                                        "He oinked joyfully and fled off into the night. From there, he joined with the wild bush pigs, and founded a great kingdom that was as a scourge upon the earth."
                                        "Cruel indeed was the pig king, and countless innocents fell before his terrible iron hooves."
                                        "In the years to come, you would curse your impetuous decision to let that devil-pig free many times."
                                        "But that is a story for another day."
                                    "If you shouted \"Noooooooooooo!\" more pitifully than ever before, turn to page 48."  if pitiful == 4:
                                        pov "{b}{i}NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                        OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                        OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                        OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                        OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                        OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                        OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!{/b}{/i}"
                                        $pitiful +=1
                                        jump thiefchase2
                        "If you shouted \"Noooooooooooo!\" pitifully, turn to page 45." if pitiful == 1:
                            pov "Noooooooooooo!"
                            $pitiful +=1
                            jump thiefChase
                        "If you shouted \"Noooooooooooo!\" again, even more pitifully, turn to page 46." if pitiful == 2:
                            pov "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!"
                            $pitiful +=1
                            jump thiefChase
                        "If you shouted \"Noooooooooooo!\" again, as pitifully as one can shout, turn to page 47."  if pitiful == 3:
                            pov "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                            OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                            OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                            OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                            OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                            OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                            OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!"
                            $pitiful +=1
                            jump thiefChase
                        "If you let them go, turn to page 27.":
                            "You walked sorrowfully back to the road, cursing the devil for your misfortune."
                show hand onlayer transient:
                    yalign 0.8#0.743
                    xalign 0.5
                "As you trudged back to the road you discovered that all of your coins had been stolen and replaced with I.O.U.'s, the bread was now nothing but crumbs, and the meat had been replaced with a live possum with a label on it saying \"Ham\". It bit you and fled into the trees.{vspace=100}{i}In your notes, write down that {b}Your things have been stolen.{/b}{/i}"
                if godfather == "White":
                    "And so you set about wailing and beating the ground and tearing at your paper clothes, crying out saying \"Oh Lord, how could you treat your servant thus?\""
                    "After a long time you drew yourself up from the ground and spoke to the trees."
                    pov "Hear me now, Thief. With the Lord as my witness, I will not rest until you see justice."
                if godfather == "Red":
                    "And so you set about wailing and beating the ground and tearing at your paper clothes, crying out saying \"Oh my Lord and Master, the Father of Lies, how could you forsake me? I, who have outdone all others in wickedness, and served you faithfully in evil for all these long years?\""
                    "After a long time you drew yourself up from the ground and spoke to the trees."
                    pov "Hear me now, Thief. My godfather is the Devil, and my blood runs with nothing but spite, and I will not rest until the Prince of Darkness fastens His hands around your ankles and drags you straight down to hell where you belong."
                if godfather == "Black":
                    "And so you set about wailing and beating the ground and tearing at your paper clothes, crying out saying \"Lady Death, take me now!\""
                    "After a long time you drew yourself up from the ground and spoke to the trees."
                    pov "Hear me now, Thief. My godmother is the end of all things, and I will not rest until you have been dragged down into Her icy waters where you belong."
                "But there was nothing to be done for now, and so you tightened your seaweed around your waist and set off once more for the festival, vowing vengeance upon the Master Thief."
            "If you refuse to aid her, turn to page 44.":
                pov "I'm sorry ma'am, but I cannot help you. I've been told not to talk to strangers."
                "\"Bah!\" cried the older woman, and stomped her foot on the ground."
                "In a flash her clothes tore asunder, and her grey hair fell to the ground, and you saw it was all nothing but a disguise."
                "In front of you stood the cunning and terrible form of the Master Thief!"
                "They had long, long legs and thin dextrous fingers that twisted in arcane motions around them."
                "They wore a flowing midnight cloak across their back and a cunning look across their sly face."
                t "You may have outwitted me this time, but I'll get you yet!"
                t "No law shall stand, no magistrate shall know peace and no cop shall sleep easy in their bed at night, for as long as my legs can run!"
                "And with a click of their heels they rushed away into the shadows of the woods."
                "\"Praise the Lord,\" you said to yourself, \"that I know not to help mysterious old women!\""
                "(A wise habit. Once you've given someone a hand, they'll take your arm.)"
                "And so you continued on down the path, giving thanks to our Lord for your natural good sense."

    # Chapter 1, Part 5: The Toad.

    "As you walked down the road, sweating in the warmth of the summer night, you heard a great clattering of hooves behind you, and turned to see four horses pulling a magnificent golden carriage."
    "The horses were pure white, with intricate porcelain and shining bridles made of fine-spun ropes laced with gold."
    "The carriage door was open to show a curtain of lush red silk, and behind the curtain you could see the shadow of a lean and graceful figure of noble bearing."

    eg "Hold!"

    "A rich, low voice like dark mahogany came from behind the curtains, showing the distinctive tones of one of good breeding and character. The horses slowed to walk beside you."
    "A slender hand holding a long cigarette holder emerged from the curtains and beckoned to you."
    "From inside the curtain you could smell rich spices, incense and thyme."
    "You felt a cool breeze across your face from inside the carriage, and saw the shadow of the man inside swilling a glass of brandy in his other hand."
    show hand onlayer transient:
        yalign 0.63#0.743
        xalign 0.5
    #Change: More impact from this choice. More mysterious and interesting sounding locations.
    menu:
        eg "Where are you headed, fellow traveler?"
        "If you told him about the festival, turn to page 12.":
            eg "Why, that's exactly where I'm going!"
        "If you said \"The Glass Mountains\", turn to page 61.":
            eg  "Nonsense! There's no reason to be travelling that way."
            eg "I am heading to the village festival. You should join me."
        "If you said \"The road of Pins and the road of Needles\", turn to page 61.":
            eg  "Nonsense! There's no reason to be travelling that way."
            eg "I am heading to the village festival. You should join me."
        "If you said \"The space between the trees\", turn to page 61.":
            eg "Nonsense! There's no reason to be travelling that way."
            eg "I am heading to the village festival. You should join me."
        "If you said nothing, turn to page 57.":
            eg "Now now, no need to be shy."
            eg "I am heading to the village festival. You should join me."
    eg "Come, ride along in my carriage, and we shall get there twice as fast."
    if pig:
        "Your pig oinked at the carriage suspiciously."
    show hand onlayer transient:
        yalign 0.7#0.743
        xalign 0.5
    menu:
        eg "This is no night to be walking out alone. Haven't you heard there's {color=#f00}something{/color} in these woods?"
        "If you accepted the lift, turn to page 54.":
            $toadArc +=1
            "You reached up to take the gentleman's hand, and he whisked you into the carriage."
            "The moment you were through the curtain you realised something was wrong."
            "Instead of the graceful and elegant nobleman you expected, you discovered a small, ugly cane toad."
            "The incense you smelled was nothing but the reek of dirt and mud, the brandy was nothing but pondscum, the gleaming carriage was just a rotten old squash, and the graceful arm that beckoned you from behind the curtain was nothing but a wooden prop the toad held in his swollen hand."
            "You turned to run, but it was too late. With a clap, the toad commanded his steeds."
            f "Prickle! Crawl! Shudder and Wink! Be off at once. We have a festival to get to!"
            "The brilliant white horses tore off their clothes and revealed themselves to be a crow-shrike, a rat, a bat and an old black cockatoo."
            "They cackled and gibbered to each other as they raced off down the road with you, bumping and rolling and pulling apart pinecones and causing terrible devastation as they went."
            #Change: ADD CHOICE
            show hand onlayer transient:
                yalign 0.66#0.743
                xalign 0.5
            menu:
                f "Well, are you impressed?"
                "If you asked the gentleman his name, turn to page 58.":
                    f "I am Brildebrogue Chippingham, and I have never failed at anything in my life."
                    f "No doubt you've heard of me."
                "If you flattered the toad, turn to page 63.":
                    pov "Absolutely, sir. I'm stunned."
                    f "As is natural."
                    f "I find it's better to conceal my true beauty from the common-folk."
                    f "Were they to see the incandescent beauty of my true visage at first sight, I dare say they would fall to their knees and wail in shock, so transfixed would they be."
                    f "I would never be able to get anywhere without them pawing at me and offering me their baked goods and falling about in ecstasy, you know how these people are."
                    f "But you, I believe, have sufficient grace to withstand my true beauty."
                "If your notes say that {b}You are the Devil's Godchild{/b}, turn to page 65." if godfather=="Red":
                    $toadStole = True
                    pov "Sir, you've made one mistake. Never tangle with the spawn of the Devil."
                    "With a single motion you stole all the valuables you could grab and lept from the lept from the moving carriage like a holy terror, tumbling onto the road below."
                    f "What the - stop! Thief!"
                    "But it was too late. You were already away and running into the woods, laughing with impish glee."
                    show hand onlayer transient:
                        yalign 0.743#0.743
                        xalign 0.5
                    "You looked down at your haul and found that you'd managed to swipe a lovely emerald broach in the shape of a dragonfly.{vspace=170}{i}In your notes, write down that {b}You have an Emerald Brooch.{/b}{/i}"
                    "You hid it in your pocket and went on your way."
                    jump chapter6
            show hand onlayer transient:
                yalign 0.67#0.743
                xalign 0.5
            menu:
                f "So, what brings you travelling this way?"
                "If you told the toad about your Godparent, turn to page 67.":
                    if godfather == "Red":
                        pov "I'm searching for a way to escape my Godfather, the King of Kings."
                        pov "He will be here to take me away at midnight, and I have no wish to leave."
                        f "A sticky situation indeed!"
                        f "I have talked with the Lord many times, of course."
                        show tornPage1 onlayer screens zorder 101
                        show tornPage1bg onlayer screens zorder 99
                        f "Why, just the other day He said to me, He said Brildebrogue! How did I ever manage to make one as handsome and charming as you? Why, even one with my own talents (which are quite decent of course, though nothing in comparison to your own gifts) can scarcely imagine bringing such a golden figure out of the fires of creation! At this I swung back my head in a great laugh, like so: HA! And my golden mane whipped around me in the wind, and all were charmed and chortled alongside me to see my wit and good humour, and we all joined together in an uprarious shout of laughter, such that the whole world could hear it - in fact I have no doubts that you must have heard it yourself, even out here in this backwater location, so loud was the sound, although perhaps you took it for a minor earthquake."
                        hide tornPage1 onlayer screens
                        hide tornPage1bg onlayer screens
                        f "Perhaps I could put in a good word for you with Him later. Pond scum?"
                    if godfather == "White":
                        pov "I'm searching for a way to escape my Godfather, Old Scratch."
                        pov "He will be here to take me away at midnight, and I have no wish to leave."
                        f "A sticky situation indeed!"
                        f "I know the Black One well myself, in fact."
                        show tornPage2 onlayer screens zorder 101
                        show tornPage2bg onlayer screens zorder 99
                        f "Why just the other day I said to Him, I said Devil! How dare you twist the lives of these innocent souls here, tricking them into a terrible life of debauchery and ill-humour, just to suit your own devious and ill-concieved personal goals, when you could instead behave yourself and simply put things to rights like a well-mannered member of society such as myself? At my words, He shrank back with a most timiditous cowardice, and I saw Him gulp in nervous anxiety most profound, such was His fear of my great anger (which can be quite considerable when my dander is up, although of course I take care to remain in good humour for the purpose of conversing with polite gentlefolk such as yourself). In an instant, He swore never to do evil again, and scurried away over hill and dale without a backwards glance."
                        hide tornPage2 onlayer screens
                        hide tornPage2bg onlayer screens
                        f "Perhaps I could put in a good word for you with Him later. Pond scum?"
                    if godfather == "Black":
                        "I'm searching for a way to escape my Godmother, the Reaper."
                        pov "She said she will soon send 3 messengers, and then take me away. But I have no wish to leave just yet."
                        f "A sticky situation indeed!"
                        f "Why, that reminds me of the situation when my own dear old mother was about to die."
                        show tornPage1 onlayer screens zorder 101
                        show tornPage1bg onlayer screens zorder 99
                        f "I've chatted with Death many times, of course, and so on this occasion I marched right on up to Her and said \"Unhand my mother, you ruffian! I cannot allow you to continue this wave of terror you have inflicted across the forest left and right, taking away women and old maids and children at will, rich and poor alike, before their time has come to pass! Release her at once, or I'll have to get extremely unpleasant with you (And you do NOT wish to see me when I'm being unpleasant, I assure you, such a thing has driven many hard men to tears!) At this stern talking-to from me, She released my mother at once with a sincere apology, and I need hardly say that She has not darkened our door again."
                        hide tornPage1 onlayer screens
                        hide tornPage1bg onlayer screens
                        f "Perhaps I could put in a good word for you with Her later. Pond scum?"
                "If you remained vague about your true plans, turn to page 71.":
                    pov "Just... travelling, I suppose."
                    f "Fantastic! Nothing better than a spot of travelling. I've done quite a bit in my day, let me tell you."
                    f "Why just the other day I travelled to the living city of Brilochiorp, built on a turtle's back, where your dreams cast shadows and your thoughts chase after you in the mid-afternoon sun. I was there to discuss matters with the queen of the dream thieves, you see, a rascally beggar who had been running about the city fliching this dream and that right out of the heads of the poor citizens, so that they dreamed nothing and had no ideas and the city's art and culture stagnated to nothing! Well, we can't have this sort of thing going on, Brilebrogue, I said to myself, and so I paid the blighter a visit and gave her a stern talking-to, and no mistake. She renounced his ways in an instant and placed all the dreams back exactly where he found them, promising to reform her ways and be a better woman. Another successful adventure, all told."
                    f "But I'm sure your little festival will be quite quaint, too. Pond scum?"
                "If you said nothing, turn to page 74.":
                    f "No bother, then, keep your secrets to yourself."
                    f "I myself am excellent at keeping secrets. Why, just the other day the Brass Magician of the City of Pale Stones said to me, he said Brildebrogue! Can I trust you with a most powerful and deadly secret, such that it would destroy the heavens if it were to be released? Of course I gave him my assurances immediately, and thus he told me that the devil's seven daughters were locked below the city in chains, and could only be released with the most secret and magical word, \"Grolabicon\"! Of course if this were ever to be discovered and the daughters released, they would wreak such terrible havoc on the world as to bring the Firmament crashing down from Her place up above, and it would be the eigth and final apocalypse come at last, which is why I gave him my word that I would keep the secret safe as houses, and I have never told anyone of the matter to this day."
                    f "Pond scum?"
            show hand onlayer transient:
                yalign 0.67#0.743
                xalign 0.5
            menu:
                "He offered a decanter of pondwater to you."
                "If you accepted (as any kind and generous guest would), turn to page 75.": # (The choice of a kind and generous guest)
                    #Change: Bad luck
                    "You knew better than to say no. After all, it\'s bad luck to refuse a gift from a toad."
                    "The pondwater was surprisingly delicious. It tasted of lavender honey, cold coffee, and long evenings by a shaded pool in the heat of summer."
                    "As you sipped it you felt a cool emerald chill pass through your whole body."

                "If you refused (the action of a witless and ungrateful churl), turn to page 76.":
                    "\"No thank you,\" you said, like a fool. (Don't you know that it's bad luck to refuse a gift from a toad?)"
                    f "More for me, then!"
                    "And the toad greedily gulped down the pondwater, without comment on your obvious poor manners and lack of breeding."
            "The old squash rattled about hither and thither through the forest, giving you bruises all over, but before you knew it you had arrived at the village square."
            "The toad rose out of his seat, leapt out through the curtains, and with a flourish offered his hand to help you down the carriage steps (which were made of old shoe-leather)."
            f "There you are!"
            f "Thank you gracefully for the wonderful company, and I wish you the best of luck with the festival!"
            jump chapter6
        "If you refused the lift, turn to page 55.":
            if godfather == "Red":
                pov "Begone, worm. Pester me again and I'll drive you into the grave, just as I did my own mother."
            else:
                pov "No thank you, Sir. My mother warned me not to talk to strangers."
            eg "You would spurn me? ME?"
            eg "I'll have you know that I am {b}Bridlebrogue Chippingham{/b}, and I've never failed at anything in my life!"
            "The curtains parted and inside you saw a small, ugly cane toad, squatting in muck. The graceful arm that beckoned you from behind the curtain was nothing but a wooden prop in his webbed hand. He tossed it to the ground with disgust."
            show tornPage3 onlayer screens zorder 101
            show tornPage3bg onlayer screens zorder 99
            if godfather == "Red":
                f "Why, if your mother was alive I would give her a good piece of my mind about the way she raised you. If she were in her right mind she would have reminded you to mind your betters, and had you the presence of mind to mindfully bring to mind an open mind, you wouldn't dismiss my offer with such peace of mind! I tell you, when I was a tadpole we treated our elders with respect, a good deal more respect than this, and we knew a thing or two about a thing or two, let me tell you, but we never let that go to our heads and despite my vast experience and knowledge even at that young and naive age, I still knew how to give the basic respect that a toad about town deserved, let alone the respect due to a toad with such a fine and noble name as the Burpengary Chippinghams!"
            else:
                f "Why, I have half a mind to give your mother a good piece of my mind. If she were in her right mind she would have reminded you to mind your betters, and had you the presence of mind to mindfully bring to mind an open mind, you wouldn't dismiss my offer with such peace of mind! I tell you, when I was a tadpole we treated our elders with respect, a good deal more respect than this, and we knew a thing or two about a thing or two, let me tell you, but we never let that go to our heads and despite my vast experience and knowledge even at that young and naive age, I still knew how to give the basic respect that a toad about town deserved, let alone the respect due to a toad with such a fine and noble name as the Burpengary Chippinghams!"
            hide tornPage3 onlayer screens
            hide tornPage3bg onlayer screens
            "With a furious clap of his hand, he ordered the horses to ride on. The horses shrugged off their clothes and revealed themselves to be a crow-shrike, a rat, a bat and an old black cockatoo. You realised that the brilliant carriage they pulled was nothing more than an old rotten squash."
            "They pulled it bouncing down the road, crashing and rolling and pulling apart pinecones and causing terrible devastation as they went, until they were down the road and out of sight."
            pov "Well! It's a good thing I know not to talk to strangers."
            "(A wise habit. The Lord knows this world is full of cheats and liars.)"
            jump chapter6

    #---- Act 1, Chapter 6: The Village.
    label chapter6:
        if mushroomArc == 0 and thiefArc == 0 and toadArc == 0:
            if godfather == "Red":
                "And so it was that you stayed on the path the whole way, ignoring your wanton nature and never once being tempted by the offers of strangers."
            else:
                "And so it was that you stayed on the path the whole way, following your mother's advice and never once being tempted by the offers of strangers."
            "(Some protagonist you turned out to be.)"
            jump witch1
        else:
            "And so you finally arrived at the village."
        "The rich dark blanket of night was softly rolling over the town, and cooking fires lit up all across the hills, one by one."
        jump villageExplore1

    label witch1:
        #TK: add choices here
        "As you walked up to the village, you spied a hunter standing guard."
        h "Good evening."
        show hand onlayer transient:
             yalign 0.68#0.743
             xalign 0.5
        menu:
            h "Be careful tonight. They say there's witches abroad."
            "If you said there's no such thing as witches, turn to page 38.":
                        pov "Witches? Nonsense! There's no such thing!"
                        "No sooner had those foolish words escaped your mouth than a witch lept out of the bushes and onto your back. Before you could say or do anything, she dug her heels into your sides and rode you up into the sky and over the mountains."
                        $witchArc +=1
                        "In a wink you found yourself at the blue mountains, exhausted from hard riding."
                        "A witches sabbath was afoot. A great fire raged on the peak before you."
                        "The witches cackled and jibbered and danced around you with glee, poking you cruelly in your sides and making cutting remarks like, \"Now who's not real, eh?\" and \"We don't believe in YOU! How do you like that?\" which wounded your feelings grievously."
                        w "Oh gosh, oh no, are you all right?"
                        "A figure pulled you away from the jeering crowd and tended to your wounds."
                        w "I'm so sorry about that. The old girls tend to get a bit carried away. They don't get out much, you know, it's a bit of a treat for them."
                        w "Are you feeling ok? Let me get you up. I'm so sorry about this, I know this is probably the last thing you want to be doing on a friday night, really can't apologise enough, it's just the full moon, you know? Always gets them a bit riled up, and it does them good to get some fresh air and dance around once in a while, you know, fulfill their oath to the devil, but, yeah, no excuses for kidnapping you obviously, that kind of behaviour is really not on."
                        w "Here, let me give you a lift home."
                        "She helped you get up on her broom and spirited you away into the sky."
                        "Below you, you heard the witches you chanting praise to Belphegor, lord of Hogs."
                        w "So."
                        w "You come through here often?"
                        #TK: Choice
                        pov "Not often, no."
                        w "Oh, it's lovely out here, you should definitely try coming back when you have a chance. Beautiful views."
                        "A great rumbling broke out all around you. You twisted around to look back. Behind you, you saw the mountain split open and ten thousand hogs burst up from beneath the earth. The witches screeched in demonic glee."
                        w "Oh dear. I'm going to miss everything."
                        w "Alright, here you are. I'd better be getting back."
                        w "Have a good night!"
                        "She set you down at the edge of town and flew off into the sky."
                        "The rich dark blanket of night was softly rolling over the village, and cooking fires lit up all across the hills, one by one."
                        jump villageExplore1
            "If you trembled in terrible fear, turn to page 39.":
                "You looked around in fright. The bushes rustled. But you saw no witches."
                pov "Thank you for the warning, kind hunter. I'll be careful."
                "You walked into town."
                "The rich dark blanket of night was softly rolling over the village, and cooking fires lit up all across the hills, one by one."
                jump villageExplore1

    label villageExplore1:
        show hand onlayer transient:
            yalign 0.728#0.743
            xalign 0.5
        menu:
            "The town was overflowing with people bustling about and preparing for the festival, pulling up chairs and laying great tables around the enormous bonfire in the centre of town."
            "If you looked at the food, turn to page 36." if not foodLook:
                $foodLook = True
                "Over the bonfire was a great suckling pig being prepared on a spit, slathered in rosemary and garlic butter and herbs of all types, and stuffed with breadcrumbs and fresh figs and crisp walnuts and apples and all the fruits of the earth."
                if pig:
                    "Your pig looked upon it sadly, and shook its head at the foolish greed of the human race."
                "The mangos were in season, and the trees were so weighed down with them that they would fall off and roll down the town gutters, so that the whole town was rich with the sweet scent of fruit mixed with the smell of woodsmoke and spices and crackling fat from the cooking fires."
                "Those mangos that didn't roll away fast enough were plucked up immediately and eaten by gleeful clouds of fruit bats that chittered and cackled in a great whirling chaos overhead."
                "Great glass bowls of red sangria were placed at each table, filled with fresh oranges and giant yellow lemon slices, ground cinnamon and brandy and crisp sweet apples and ginger ale."
                "For desert there were giant lemon meringue pies made from lemons as big as your fist, covered in fresh-whipped meringue from the Baker's parlour."
                jump villageExplore1
            "If you sat down with the rest of the guests without delay, turn to page 37.":
                "You took your place at the table."
    "The Hunter was there, and the old Gloom-monger, and the young Goose-girl."
    "The stars and the moon slowly arrived to take their places. The birds and moths and the Firmament and the soft mist of night all came and were seated."
    "But one guest was missing: No one had seen the Wild Witch of the Woods all night."
    "As the festival began a terrible concern and commotion went up amongst the guests, for we all know what terrible luck it is to spurn a witch."
    may "Did her invitation go missing?"
    h "Impossible. I delivered it myself."
    if witchArc >=1:
        pov "Um, excuse me."
        pov "I saw the witch just tonight, actually. She was at a ritual in the Blue Mountains."
        may "What!? Why would she spurn our invitation?"
    else:
        "But still, the witch did not arrive, and soon everyone was a frenzy of worry."
    gm "We've given offence to her somehow. She'll turn all our hair to straw and infest all our picnics with ants. None shall escape."
    go "All our spoons will rust, and our forks will get stuck in the drawers! I already have enough on my hands dealing with the geese!"
    "The panic increased when the Sparrow-Herder rushed in and waved for attention."
    sh "The Master Thief has struck again!"
    sh "The entire suckling pig is missing. Quick - check your valuables!"
    "The whole town turned out their pockets and discovered that all their spare change had been taken and replaced with live rats, which shrieked and leapt away and ran into the forest."
    town "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!"
    gm "Told you so."
    #More investigating around the village, adventure game style.
    jump village

# Act 2: Chapter I - Chat and investigation
#You can investigate the village and choose between 2 main pathways
label village:
    show hand onlayer transient:
        yalign 0.7#0.743
        xalign 0.5
    menu:
        "You stood in the middle of the village as chaos and woe erupted around you."
        "If you investigated the banquet, turn to page 64.":
            jump banquet
        "If you investigated the edge of town, turn to page 70.":
            jump town

label banquet:
    "You walked down the tables of the village banquet. Some folks were gripping each other tight and crying out at the misfortune that had befallen their town. Others simply sat in glum silence."
    "The cane toad from the road was gulping down every morsel of food he could find, cradling a wineglass that was almost as big as he was and darting his tongue out to snatch prawns and hot potatoes from nearby unattended plates."
    label banquetMenu:
        show hand onlayer transient:
            yalign 0.625#0.743
            xalign 0.5
        menu:
            "You looked over the tables."
            "If you talked to the woeful villagers, turn to page 84." if not banquetChat:
                "They paid no attention to you, but continued shaking their heads and wailing with wretched misery."
                $banquetChat = True
                jump banquetMenu
            "If you talked to the Sparrow-Herder, turn to page 85."  if sparrowherderChat <= 4:
                if sparrowherderRand ==1:
                    if sparrowherderChat == 0:
                        sh "G'day."
                        sh "The ruin to the south has many poisonous beasts. Be sure to carry Antidotes if you head that way."
                    elif sparrowherderChat == 1:
                        sh "They say these beasts were once envious hogs that spoke ill of our dear Lord."
                        sh "Thus He cursed them, and now they can speak nothing but poisonous words. As soon as you hear their evil gossip, you'll fall down dead as a doornail."
                        sh "That's what I heard, anyway."
                    elif sparrowherderChat == 2:
                        sh "The ruin? They say it's left over from the fifth age."
                        sh "It was an age of wise beetles that loved to make puzzles and games."
                        sh "The greatest puzzle-makers would go on to become consorts for their Queen."
                    elif sparrowherderChat == 3:
                        sh "Their labyrinthine stone puzzle-boxes lie across the land even now, untouched. None who live can solve them."
                        sh "The Hogmasters laugh at all who try, and their poison words cut them asunder."
                    elif sparrowherderChat >= 4:
                        sh "How do I know all this? The sparrows told me."
                elif sparrowherderRand == 2:
                    if sparrowherderChat == 0:
                        sh "G'day."
                    elif sparrowherderChat == 1:
                        sh "You seen those rings of mushrooms in the woods?"
                        sh "Be wary, friend. Those are the Hag Tracks. They show where the witches danced last night."
                    elif sparrowherderChat == 2:
                        sh "As they dance, the Lady Death pushes her fingers slowly through the grass to grab at their ankles. If they tarry too long, they'll be grabbed by their feet and whisked away straight down to the last kingdom."
                        sh "Long have they danced away from death, and eagerly does she clutch for them. If she doesn't catch them, they fly away with the dawn, and the fingers are left behind."
                    elif sparrowherderChat == 3:
                        sh "The lady can be nice enough, sometimes. When we had the famine years ago, she pushed her fingers through the grass so we could eat."
                        sh "But never go into the circle. She might hear your footsteps, and mistake you for a witch. In a flash, you'll feel her fingers wrap around your ankles and drag you down into the earth. Once she has you, she'll never let you go."
                    elif sparrowherderChat >= 4:
                        sh "How do I know all this? The sparrows told me."
                $sparrowherderChat +=1
                jump banquetMenu
            "If you talked to the Mayor, turn to page 82." if mayorChat <= 6:
                if mayorChat == 0:
                    may "If you're going out to hunt the witch, be wary! They say Moon-Head walks these roads tonight."
                elif mayorChat == 1:
                    may "They say his front face is a full moon, and his back face is a new moon."
                elif mayorChat == 2:
                    may "If he looks at you with his bright face, you can tell nothing but the truth. If he looks at you with his dark face, you can tell nothing but lies."
                elif mayorChat == 3:
                    may "His robes are rich blue silk with clouds and fog rippling across them, and they flow around him in hypnotising waves as he dances."
                elif mayorChat == 4:
                    may "He leaps through the trees calling for his disciples, the lost and insane, and they all spring together through the woods with glee, singing moon-mad songs."
                    may "It's quite the sight to see."
                elif mayorChat == 5:
                    may "He winked at my mother once, and I never saw her again."
                elif mayorChat >= 6:
                    may "Sometimes I still hear her laughter on moonless nights."
                $mayorChat += 1
                jump banquetMenu
            #If you're going out to hunt the witch, be wary. There's a wolf out there.
            #My sister heard it howling, once. The wolf appeared in her head, and spoke to her.
            #You will have three days, it said.
            #Three days passed, and I never saw her again.
            #Do you hear that?
            "If you talked to the Second Pig, turn to page 266." if pig2Rand == 1 and pigChat <= 7:
                if pig:
                    if pigChat == 0:
                        p2 "Oh. It's you."
                        "Your pig turned rose up on its hind legs."
                        p1 "Montgomery."
                        p2 "Gregory."
                    if pigChat == 1:
                        p2 "I'm sorry, but you'd better not stay here. I don't think it's safe for us to be so close."
                        p1 "Hm. I see you are still gripped by this insane delusion."
                        p2 "It's no delusion, brother. I know you've heard {color=#f00}it{/color} too. No matter how you hard you try to hide it."
                    if pigChat == 2:
                        p1 "Cast off this madness, Montgomery. Come back to us. We all miss you."
                        p2 "Look me in the eyes and tell me you haven't heard the scrabbling in the walls."
                        p1 "Nothing but rats."
                        p2 "Tell me you haven't heard the howling in the pipes."
                        p1 "The wind. Just the wind."
                        p2 "You cannot tell me you don't see the house twist with it. Swollen. You can barely breathe in there for the stink of it."
                        p1 "Only a dream."
                    if pigChat == 3:
                        p2 "Perhaps it is a dream."
                        p2 "But I hear that dream coming for me. From the space between the trees."
                        p2 "It will not be long now."
                    if pigChat == 4:
                        p1 "I will pray for you, Montgomery. But I will not follow you down the path of madness."
                        p2 "Very well, brother. Let us each have our delusions."
                    if pigChat == 5:
                        p2 "I will always love you."
                        p1 "And I you, brother. And I you."
                    if pigChat == 6:
                        p1 "Let us keep moving. He is lost."
                    if pigChat == 7:
                        p1 "There is nothing for us here."
                else:
                    if pigChat == 0:
                        p2 "Oh. Hello."
                    if pigChat == 1:
                        p2 "I'm sorry, but you'd better not stay here. It's not safe around me."
                    if pigChat == 2:
                        p2 "You see, I'm expecting {color=#f00}someone{/color}."
                    if pigChat == 3:
                        p2 "I can hear {color=#f00}them{/color} coming now. In the pipes."
                    if pigChat == 4:
                        p2 "The others say it's all in my head. But I know better."
                    if pigChat == 5:
                        p2 "You'd better get moving. You don't want to be here when {color=#f00}they{/color} come."
                    if pigChat == 6:
                        p2 "Or perhaps I'm wrong."
                    if pigChat == 7:
                        p2 "Perhaps you've already met {color=#f00}them{/color}. You just haven't realised yet."
                $pigChat +=1
                jump banquetMenu
            "If you talked to the Toad, turn to page 87." if not toadStole2:
                if toadStole:
                    f "You!"
                    f "Hellion! Knave! You'll see justice for your crimes, or my name isn't Brildebrogue Chippingham!"
                    "You quickly hid under the tablecloth until the toad became distracted by a passing prawn platter and gave you time to slip away."
                    "Best avoid him for now."
                    $toadStole2=True
                    jump banquetMenu
                else:
                    if toadConvo2Spoke == False and toadArc == 0:
                        f "Hello again, fellow traveler!"
                        "He sprayed food as he spoke. He was sitting on a tower of pillows on his chair, so he could reach the table."
                        f "Do not be alarmed! I have already forgiven your poor manners in refusing my generous offer on the road."
                    elif toadConvo2Spoke == False and toadArc > 0:
                        f "Good evening, my dear friend!"
                        "He sprayed food as he spoke. He was sitting on a tower of pillows on his chair, so he could reach the table."
                        f "It warms my heart to see you again! Although we have known each other but a little time now, I already feel the bonds of our friendship have grown strong as the thickest iron, so warmed have I been by your gregarious companionship!"
                        f "Please, take a seat beside me! I would count myself proud to sit amoung such distinguished company as yours."
                    elif toadConvo2Spoke:
                        f "Ah, the traveller returns!"
                        f "You {i}must{/i} try some of these prawns, they're simply to die for. A credit to your humble village!"
                label toadConvo2:
                    show hand onlayer transient:
                        yalign 0.65#0.743
                        xalign 0.5
                    $toadConvo2Spoke = True
                    menu:
                        f "Try the crackling, it's marvelous."
                        "If you asked about the feast, turn to page 89." if not toadFeast:
                            f "Yes, it's adequate, perfectly adequate."
                            "He opened his mouth wide and took a bite out of a flank of roast pork."
                            f "Nothing like the feasts back at Chippingham Manor, of course, you understand, nothing like them at all, but certainly adequate nonetheless, I have to say, if I do say so myself, needless to say, as the saying goes, to say nothing of this fine vintage!"
                            "He awkwardly tilted the wineglass towards him and drank deeply, almost falling in."
                            show tornPage1 onlayer screens zorder 101
                            show tornPage1bg onlayer screens zorder 99
                            f "Why, it quite reminds me of when I was staying with the Sultana of Yolkorich, a land far to the south across the seas, completely made out of delectable food, you understand! The trees were made of licorice sticks, all the pillars were fine musk candy, the streams ran fresh with sparkling champagne, and the citizens would drive over the rocky roads on peppermint carriages drawn by mouth-watering omlette stallions. Well, one day I woke up and tucked into a hearty breakfast of raisin toast, smoked salmon and fried eggs, only to discover I had devoured the Sultana herself, along with her entire retinue! I had to make a hasty retreat from that situation post-haste."
                            hide tornPage1 onlayer screens
                            hide tornPage1bg onlayer screens
                            f "There was egg on my face, I can tell you!"
                            $toadFeast = True
                            jump toadConvo2
                        "If you asked about his plans, turn to page 90." if not toadLong:
                            f "Aha! Allow me to elucidate."
                            "He slurped noisily from his wineglass until it was empty."
                            f "I plan to track this witch character down tonight, before she causes any more chaos."
                            f "We must help the poor, accursed people of this village! Already they panic, terrified that she will descend upon them and turn them all into beasts!"
                            if witchArc >= 1:
                                pov "I think that may just be a misunderstanding."
                                "A tray of drinks came by and the toad dragged a new full-sized wineglass into his arms, struggling with the weight."
                                f "Maybe so, maybe so. But between you and me, I have a curse of my own I need her to lift."
                            else:
                                "A tray of drinks came by and the toad dragged a new full-sized wineglass into his arms, struggling with the weight."
                                f "And between you and me, I have a curse of my own I need her to lift."
                            f "{i}Transformed{/i}, you know. Keep that under your hat, very hush hush, you understand."
                            $toadLong = True
                            jump toadConvo2
                        "If you asked for more information about the witch, turn to page 93." if toadLong and not toadFind:
                            $toadFind = True
                            f "I understand she lurks in a cottage in the darkest depths of the rainforest, where all fear to tread."
                            f "All except for Brildebrogue Chippingham, of course!"
                            "He attempted to give you a bold wink, but accidentally winked with both eyes at once. He was slowly sliding under the table as he talked."
                            f "What do you say? Care to join me?"
                            f "I hear she knows much, and consorts with the Devil Himself!"
                            jump toadWitchJoin
                            label toadWitchJoin:
                                show hand onlayer transient:
                                    yalign 0.7#0.743
                                    xalign 0.5
                                menu:
                                    f "I need to lift this curse of mine, and surely she could help you out with... I don't know, whatever problem you have."
                                    "If you accepted, and set off to the witch\'s Cottage with the toad, turn to page 105.":
                                        f "Sensational! Stay close to me, and you won\'t have a thing to fear."
                                        f "It would be the brave forest beast indeed that would dare to cross swords with THESE powerful weapons."
                                        "He flexed his arms for you. A tiny bump of muscle rose up."
                                        f "Let us be off at once!"
                                        jump toad1
                                    "If you politely declined (for now, at least), turn to page 102.":
                                        f "I understand. The witch's fear quails even the most courageous heart."
                                        f "Not mine, of course! If you change your mind, I'll be here."
                                        #$toadDecline = True
                                        jump toadConvo2
                        "If you asked about the witch again, turn to page 93." if toadFind:
                            f "Ah, have you changed your mind?"
                            jump toadWitchJoin
                        "If you asked him about the thief, turn to page 78." if toadLong and not toadThief:
                            $toadThief = True
                            pov "Aren't you going to do anything about all the stolen goods?"
                            f "And risk the wrath of the Master Thief? Not on your life! I heard they eat danger, and breathe death!"
                            may "I heard they stole a horse right out from under its rider."
                            sh "I heard they stole the King of Spain right out from under his wife."
                            f "Well, I heard that every winter they shrink down to the size of a pin, and hide away in your house to steal all your odd socks and hairpins and loose change."
                            f "Why do they do it? Why, to make a nest, of course. All the better to lure their suitor, THE DEVIL!"
                            jump toadConvo2
                        "If you asked about your Godparent, turn to page 85." if not toadHelp:
                            if godfather== "Black":
                                pov "I need a way to escape my Godmother, Lady Death. Can you help me?"
                                f "Possibly, possibly."
                                f "Perhaps the witch will know something about it. You should join me in hunting her down!"
                            elif godfather == "White":
                                pov "I need a way to escape my Godfather, the Lord. Can you help me?"
                                f "Possibly, possibly."
                                f "Perhaps the witch will know something about it. You should join me in hunting her down!"
                            elif godfather == "Red":
                                pov "I need a way to escape my Godfather, the Devil. Can you help me?"
                                f "I'm sure the witch would know something about that. Rumour is that she dances with the Devil on cold, moonless nights! You should join me in hunting her down."
                            $toadHelp = True
                            jump toadConvo2
                        "If you made your excuses and left, turn to page 83.":
                            f "Return soon! You can't possibly leave without sampling some of this fine green mango salad over here, absolutely sensational!"
                            jump banquetMenu
            "If you returned to the village square, go back to page 50.":
                "You turned and walked back to the center of the village."
                jump village
            #Then somehow that turns to stealing from the mushroom / helping the mushroom against the theif

label town:
    "You walked out to the edge of town, where villagers ran to and fro, searching for the Master Thief."
    "Fruit bats chirped and swirled overhead, fat with fresh mangos."
    #TK: Add another character who randomly appears and disappears - moon-head?
    label townExplore:
        show hand onlayer transient:
            yalign 0.63#0.743
            xalign 0.5
        menu:
            "Some of the villagers were strapping down a tarp."
            "If you investigated the tarp, turn to page 79.":
                pov "What is this?"
                h "Shhh! Keep your voice down. This is all part of our plan to catch that dastardly Master Thief."
                gm "We're sure to fail. This whole plan is doomed."
                jump villagersConvo
            "If you talked to the Goose-girl, turn to page 97." if goosemongerChat <= 6:
                if goosemongerChat == 0:
                    go "Greetings, friend. Be careful of the crystal caverns to the north."
                elif goosemongerChat == 1:
                    go "It is said that the first of the Goose-girls, old crooked Belziah, attempted dark experiments there."
                elif goosemongerChat == 2:
                    go "She created abominable goose-faced men that even now infest the caverns, honking endlessly and plotting to turn the world to ruin."
                elif goosemongerChat == 3:
                    go "Sometimes, I dream of those caves."
                    go "Home of the Goose-folk! I can scarcely imagine it."
                elif goosemongerChat == 4:
                    go "What would it be like to throw off my human skin and join them?"
                    go "To honk in ecstasy with my brothers?"
                    go "To live every day with the fierce, honest joy of a goose?"
                elif goosemongerChat == 5:
                    go "But they are just dreams. I would never have the courage."
                elif goosemongerChat == 6:
                    go "Do not make my mistake, friend. Think not of the crystal caverns."
                    go "Their beauty was not made for us."
                $goosemongerChat += 1
                jump townExplore
            "If you talked to the Hunter, turn to page 98." if hunterChat <=2:
                if hunterChat == 0:
                    h "A {color=#f00}wolf{/color}? Don't be silly."
                if hunterChat == 1:
                    h "There are no {color=#f00}wolves{/color} in Australia."
                if hunterChat == 2:
                    h "Howling? No. You must be imagining it."
                $hunterChat += 1
                jump townExplore
            "If you talked to the Gloom-monger, turn to page 99." if gloommongerChat <=6:
                #TK: Longer gloom-monger chat.
                if gloommongerChat == 0:
                    gm "Give it up now. You're already doomed."
                elif gloommongerChat == 1:
                    gm "We have already died countless times. And we will die countless more before this business is through."
                elif gloommongerChat == 2:
                    gm "Can't you hear them? The footsteps of the Ash Giants?"
                elif gloommongerChat == 3:
                    gm "When we lit that first fire in the dark, they started walking."
                elif gloommongerChat == 4:
                    gm "They are almost here now."
                elif gloommongerChat == 5:
                    gm "In their right hand is a terrible sound."
                elif gloommongerChat == 6:
                    gm "In their left hand is a terrible light."
                $gloommongerChat += 1
                jump townExplore
            "If you looked in the well, turn to page 346." if wellRand == 1 and wellChat <=2:
                if wellChat == 0:
                    well "Evening."
                elif wellChat == 1:
                    show hand onlayer transient:
                        yalign 0.7#0.743
                        xalign 0.5
                    menu:
                        well "Got any smokes?"
                        "If you found some cigarettes for the thing, turn to page 367.":
                            well "Cheers."
                        "If you refused, turn to page 368.":
                            well "No worries."
                        #"If your notes say that {b}You know the secret name of Belphagor, lord of hogs{/b}, turn to page 210."
                        #TK: Write secret Thing in the Well Path
                elif wellChat == 2:
                    show hand onlayer transient:
                        yalign 0.624#0.743
                        xalign 0.5
                    menu:
                        "You peered into the well's depths."
                        "If your notes say {b}you have an Emerald Brooch{/b}, turn to page 630.":
                            "You tossed the Emerald Brooch down in the well, and wished for a way out of your terrible predicament."
                            well "Thanks for the Brooch. I can't help you, though."
                        "Otherwise, if {b}your things have been stolen{/b}, turn to page 365.":
                            "You would have liked to be able to make a wish. But you had no coins on you."
                        "Otherwise, if {b}you have ventured into the Smoke World and rescued the stolen Skin-Mask from King Famine{b}, turn to page 742.":
                            well "Thank G-d you have it. Quickly! Come in!"
                            "You scrambled down into the well towards the secret passage. The breath of King Famine was hot on your neck. Behind you, you could see His soldiers tearing apart the village, just as He swore He would when you stole the mask from Him."
                            sc "Go. I'll hold them off."
                            "You turned to your faithful companion, tears in your eyes."
                            pov "Scraggs, are you sure?"
                            well "After all we've been through together... we can't just abandon you!"
                            "He just gave you his crooked grin."
                            sc "Such is life."
                            sc "Don't worry about me. Just make sure you collect that reward money."
                            "You embraced in a passionate kiss. Then Scraggs pushed you away. His Colt Navy revolvers roared out into the night as you fled deeper into the well."
                            sc "Come, you bastards! Come!"
                            "The secret entrance slammed shut behind you, cutting off the sounds of battle."
                            "The Skin-Mask was burning hot in your hands, slowly twisting as it tried to squirm out of your grip. Whispers seeped into your mind."
                            well "Don't listen to it. You're almost there now. I'll open the way."
                            pov "Alouicious... your brother told us about what happened. I just wanted to say-"
                            well "Save your breath. There's nothing to be done about it now."
                            well "In the years since I died in that freak chainsaw juggling accident... there's one thing I've learned."
                            well "You can't change the past."
                            well "All you can do is try to change the future. Once step at a time."
                            "A rumble shook the cave. In horror, you saw the fingers of King Famine slowly breaking in through the earth around you. In the cracks you could see his gaping maw. A terrible screaming broke out all around you."
                            "With a powerful crack, Alouicious stretched his ghostly form across the cave, holding it together through sheer force of will. Thick smoke billowed all around you."
                            well "Go to her."
                            pov "No. I can't lose you too."
                            well "Have you forgotten?"
                            well "I'm already dead."
                            "The smoke howled through the cave and pushed you deeper into the depths. You stumbled onwards, tears pouring down your face."
                            "The wind fell silent. The cave was quiet."
                            sm "You are alone now."
                            "You struggled through the cave, feeling the thing twisting in your hands."
                            sm "Your limbs are slowing."
                            sm "There is no need to worry."
                            sm "Soon, this part of the cycle will be over, and you can lay down your burden."
                            "Your shoulders ached. Your hands were raw and burnt."
                            sm "Listen."
                            sm "Do you hear that?"
                            sm "The footsteps of the Ash Giants."
                            sm "They will be here soon."
                            sm "None of this matters any more."
                            "You stumbled out into the great cavern. Below you, you could see the vortex of souls. In the middle of the vortex, Princess Sun lay peacefully at rest in her tomb."
                            "You fell to your knees. Your legs were lead."
                            sm "Come."
                            sm "It is time to end this."
                            show hand onlayer transient:
                                yalign 0.69
                                xalign 0.5
                            menu:
                                sm "Put me on."
                                "If you accepted your fate, turn to page 722.":
                                    "You put on the mask."
                                    "The warm heat of it slowly closed around your face."
                                    "The skin pressed into your mouth and eyes. It folded over and enveloped you."
                                    sm "Good."
                                    "The {color=#f00}howling{/color} finally stopped."
                                    "All was silent and still."
                                    call endStamp
                                    "And then there was rest in the land."
                                    jump end
                                "If you defied your fate, turn to page 723.":
                                    "You crawled forward, step by step."
                                    sm "Rest, child."
                                    "Your hand started to shake. To your horror, the mask slowly crawled towards your face as you lay on the ground."
                                    sm "Good. Rest."
                                    "The skin crept over your mouth, towards your throat."
                                    "You tried to scream. Nothing came out."
                                    "Suddenly, you felt someone grab you and pull you up."
                                    "A burly figure lifted you up and carried you towards the cliff edge."
                                    "In your blurred vision, you caught sight of a banksia seed."
                                    pov "S...scraggs?"
                                    sc "Heh. Don't think this means I like you or anything."
                                    sc "I just need my cut of the reward."
                                    "You reached the edge of the cliff. The vortex of souls screamed out in terror."
                                    "With the last of your strength, you hurled the mask over the edge."
                                    "There was a moment of silence."
                                    "Then a gigantic explosion hurled you and Scraggs off your feet."
                                    "Princess Sun rose before you, the Skin-Mask writhing in her hands."
                                    "There was a blinding light, and they both disappeared."
                                    "Silence fell on the cavern. You heard birdsong outside."
                                    "Scraggs clapped a hand on your shoulder."
                                    sc "Alright. Time to head home."
                                    "You tilted your head back and laughed with relief."
                                    "Years passed, and the story of the Skin-Mask was forgotten. You and Scraggs lived happily ever after for the rest of your days."
                                    call endStamp
                                    "And if you are not dead, you are still alive."
                                    jump end
                        "Otherwise, you may make a wish. Turn to page 367.":
                            "You toss a coin in the well, and wish for a way out of your terrible predicament."
                $wellChat += 1
                jump townExplore
            "If you returned to the village, go back to page 50.":
                "You turned and walked back to the village."
                jump village
    label villagersConvo:
        show hand onlayer transient:
            yalign 0.63#0.743
            xalign 0.5
        menu:
            #TK: look at the wording of this and "hot sweaty anarchy"
            go "Care to join us?"
            "If you asked how they planned to catch the thief, turn to page 66." if not villagersPlan:
                h "With this!"
                "The Hunter flexed their muscles and pulled back the tarp to reveal an ornate chest full of lustrous pebbles and stones."
                go "We'll take this out to my house, and nail it to the veranda. Everyone knows that the Master Thief can't resist anything that's nailed down."
                h "Exactly. And their love for shiny rocks is well-known."
                echidna "A fine plan indeed, friends! There's no way this \"Master Thief\" I've heard so much about could ever detect this scheme, no matter how cunning and gorgeous they may be."
                h "Thanks, friend. Your confidence means a lot."
                $villagersPlan = True
                jump villagersConvo
            "If you asked why they planned to catch the thief, turn to page 68." if not villagersCatch:
                h "They stole my courage!"
                gm "They stole my wisdom!"
                go "They stole my heart."
                h "We can't let them just run around doing as they please and getting the Goose-girl all hot and bothered. What if everyone decided to do that? It'd be anarchy!"
                go "Hot, sweaty anarchy."
                $villagersCatch = True
                jump villagersConvo
            "If you asked them about your Godparent, turn to page 77." if not villagersEscape:
                if godfather== "White":
                    pov "I need a way to escape my Godfather, the Lord. Do any of you know how I can do that?"
                    gm "Hpmh. I advise you to give up immediately."
                    go "Well, it is said that the Master Thief has hidden from the Lord all their life. If anyone would know, they would."
                    h "Once we track the thief down, you could question them!"
                elif godfather == "Red":
                    pov "I need a way to escape my Godfather, the Devil. Do any of you know how I can do that?"
                    gm "Hpmh. I advise you to give up immediately."
                    go "Well, I have heard that the witch has sworn her soul to the devil. She would know how to help you, if anyone would."
                    sh "If only she was here tonight! Oh, I can already feel her curse upon me."
                elif godfather == "Black":
                    pov "I need a way to escape my Godmother, Lady Death. Do any of you know how I can do that?"
                    gm "Hpmh. I advise you to give up immediately."
                    go "Well, as we all know, mushrooms are the fingers of death. That wise mushroom in the deep forest would know how to help you, if anyone would."
                    sh "I heard that dastardly Master Thief was planning to steal from her this very night! We'd better get the trap laid before they have a chance."
                $villagersEscape = True
                jump villagersConvo
            "If you asked them about the witch, turn to page 79." if villagersCatch and not villagersWitch:
                pov "Are you going to do anything about the witch's Curse?"
                go "And risk the wrath of the witch? Not on your life."
                gm "I heard that she has fingers as long and fat as carpet snakes, and once you fall into her clutches, you'll never see daylight again."
                go "I heard she has many children with the Devil, who are all evil."
                h "Well, I heard that all the trees of the woods are her children, but she regards them with vicious envy, and if any of them displease her by becoming too beautiful, she strikes them down!"
                h "This is why the most beautiful trees are always thunderstruck."
                $villagersWitch = True
                jump villagersConvo
            "If you accepted their offer, and head off to catch the Master Thief, turn to page 124." if villagersPlan or villagersCatch:
                h "Excellent! Let's be off at once."
                "You all lept on the cart and rattled away down the road, leaving the old Gloom-monger behind."
                gm "You're all doomed! Doooooooomed!"
                h "Don't worry. He says that every time we go anywhere."
                jump thief2
            "If you made your excuses and left, turn to page 51.":
                sh "No worries. Have a good one!"
                jump townExplore

# Act 2, Chapter 2A: The Master Thief
label thief2:
    "Soon, you arrived at the young goose-girls house, which was overrun by honking geese who tore at the furniture and ransacked the pantry until she was at her wit's end."
    if pig:
        "The pig quailed from the goose's wrath behind you."
    show hand onlayer transient:
        yalign 0.67#0.743
        xalign 0.5
    menu:
        "You nailed the chest down to the veranda while the goose-girl kept the geese at bay."
        "If you set bear traps around the chest, turn to page 119.":
            "You got some bear traps from the Hunter's cart and placed them all around the chest, disguising them with leaves."
            $chest = "Traps"
        "If you rigged tripwires to bundles of tin cans around the chest, turn to page 112.":
            "You pulled thin tripwires all around the chest tied to old tin cans. As soon as anyone approached it the tin cans would rattle like crazy, alerting the waiting geese."
            $chest = "Tripwires"
        "If you placed a terrible goose inside the chest itself, turn to page 116.":
            "You picked up the orneriest goose from the pack and carefully placed it inside the chest, shielding your eyes as it pecked at you in rage."
            "As soon as it was inside the chest, you slammed it shut."
            $chest = "Goose"
    "Then you ducked behind a bush to watch the chest."
    h "Now we wait."
    go "No way the thief can get past us now."
    echidna "I couldn't agree more, friends. This cunning and charismatic \"Master Thief\" character stands no chance against us."
    h "Don't get cocky."
    "You lay there in silence, watching the chest."
    "A fly landed on it."
    "One of the geese waddled up and began to lick it."
    go "Wait a second..."
    "The goose-girl crawled out and cautiously dragged a finger over the chest, then stuck it in his mouth."
    go "It's... icing!"
    "The entire chest had been replaced with a massive cake, baked to look exactly like the chest in every detail."
    if chest == "Traps":
        "You tested the traps to find that they were now all made out of carefully crafted fondant."
    elif chest == "Tripwires":
        "You pulled at the tripwires to discover that every can was now a perfect cake replica of a tin can made from sponge and fondant."
    elif chest == "Goose":
        "You cut open the cake to find a fine meringue goose inside."
    "The smell of chocolate wafted from behind you. You turned in horror."
    label thiefCake:
        show hand onlayer transient:
            yalign 0.67#0.743
            xalign 0.5
        menu:
            "The goose-girl's entire cottage had been replaced with a gigantic gingerbread house."
            "If you all wailed in piteous woe, turn to page 109.":
                go "{i}NoOOoOOOOOOOOOOoooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOOOoOOOOOOOOOoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOOOOOOoOOOOoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOooOOOOOOOOOoooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOOOOOOoooOOOOOOOoooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOoOOOooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!{/i}"
                sh "{i}NOOOooooOOOOoOOOOOOOOOOoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOOoOOOOOOOOOOOooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOOOOOooOOOOOOOoOOOOOOooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOOOOOOOOOOoOOOoOOOOOOOOOOOOoOoOOoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOOOOOOOoOOOOOoOOOOOOOOOOOOoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOOOOOOOOOoOOoOOOOOOOooOOOOoOoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOoOOOOOOOOOOOOOOoOOOOoOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!{/i}"
                h "{i}NooOOOOOOOOOOOOoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOOOOOOOOOoooOOOoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOoOOOOoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOoOOOOOOOooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOOOOOOoOOOOOOOOOoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOoooOOOOOoOOOOOOOOOOOOoOOOOOOoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOOOoOOOOOoOoOOOOOOOOoOOOOOOOOOOOOOOOOOOOOOOOOOOOO!{/i}"
                pov "{i}NOooOOOOoOOoOOOOOOOoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOooOOOOooOOOOOOOOoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOoOOOOooOOOOOOooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOOOOOOOOOOOOOOOOOOOOoOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOOOOOOooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOOOOOoOOOOOOoOOOOOOOooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                OOOOOOOoOOOOOOOoOOOOOOOOOOOOOOOoOOOOOOOOOOOOOOOOOOOO!{/i}"
                echidna2 "What a shame. Oh well! I'd best be off."
                $pitiful +=1
                jump thiefCake
            "If you asked your pig to find the culprit, turn to page 132." if pig:
                "The pig lept from your hands and began snuffling around in the grass. It soon began sniffing at the Echidna, grunting with suspicion."
                echidna2 "Looks like the jig is up!"
                "You lept for the Echidna, but it backflipped away just in time."
                "Laughing maniacally, it ripped off its mask to reveal none other than the Master Thief."
                t "That's right, it was I all along! I have stolen the eyes of heaven and the hands of G-d, and now I use those eyes and hands to wreak mischief and misery upon this cursed earth!"
                h "Stop them!"
                "The thief fled into the forest, with you and the loyal pig sprinting after."
                jump thiefChase2
            "If you took the cake as evidence, turn to page 131." if not thiefChestCake:
                "You grabbed a slice of the chest cake to present to the local magistrate."
                "The goose hissed at your foolishness, then continued devouring the chest."
                $thiefChestCake = True
                jump thiefCake
            "If you searched for the Master Thief, turn to page 130.":
                "You looked around wildly."
                echidna2 "What a shame. Oh well! I'd best be off."
                pov "Wait just a second!"
                "You lept for the Echidna, but it backflipped away just in time."
                "Laughing maniacally, it ripped off its mask to reveal none other than the Master Thief."
                t "That's right, it was I all along! I have stolen the eyes of heaven and the hands of god, and now I use those eyes and hands to wreak mischief and misery upon this cursed earth!"
                h "Stop them!"
                "The thief fled into the forest."
                jump thiefChase2
    label thiefChase2:
        show hand onlayer transient:
            yalign 0.65#0.743
            xalign 0.5
        menu:
            #TK: test this menu with the pig
            "The others chased after them."
            "If you tried to chase after the thief, turn to page 135.":
                "The thief led you on a merry chase, until you were deep into the forest with all the others behind you."
                "You slowly closed the distance, until you finally lept forward and grabbed their cloak."
            "If you tried to go around and cut them off, turn to page 136.":
                "You ran deep into the forest, planning to lay an ambush for the thief. Soon, you left the others far behind."
                "You lay in wait behind a bush until you heard their running footsteps. Then you lept out and grabbed them."
            "If you sent your pig after them while you set an ambush, turn to page 137." if pig:
                "The pig chased after them furiously, grunting pig curses at the fleeing figure."
                "You hid behind the bushes and lay in wait until you heard the thief's footsteps. Then you lept out and grabbed them as your pig squealed in triumph."
    "As you pulled at their cloak, it came away with a tearing sound, and the figure before you fell apart into dust."
    "It was nothing more than a pile of dead leaves and mud, carefully posed to look like the Master Thief using a series of pulleys and wires."
    "A slow clap echoed behind you."
    t "Well done, friend."
    if chest == "Goose":
        "The ornery goose you hid in the chest was now perched on their right shoulder, wearing a thief's mask and honking smugly."
    elif chest == "Traps":
        "They casually munched on a frosted bear trap."
    elif chest == "Tripwires":
        "They tossed you a small cake in the shape of a tin can."
    "The thief's long, thin fingers toyed with some of the shiny rocks from the chest."
    if pig:
        "Your pig oinked at them, moving to protect you."
    if stuffStolen:
        pov "You! Give me back my stuff!"
        "They laughed. As if from nowhere, your loaf of bread appeared in their hands. They tossed it up in the air, and before you could blink it had disappeared again."
        t "I'll give it all back in time, don't worry. But first, I have an offer for you."
    else:
        t "You gave me quite the chase. I have an offer you may be interested in."
    if godfather == "Red":
        t "You see, I've heard of you. They say you run wild over the hills, doing as you please and living in contempt of the law."
    elif godfather == "White":
        t "You see, I've heard of you. They say you're a good little christian, and you always do as you're told."
        t "Why not change that?"
    elif godfather == "Black":
        t "You see, I've heard of you. They say you're a strange one. You lurk out late at night and scare people."
    t "I know you live near the Mushroom, who is rich beyond the dreams of avarice."
    t "I plan to go there tonight and take her for all she's worth. Want to join?"
    if stuffStolen:
        t "I'll give you all your things back. Promise."
    label thiefConvo:
        show hand onlayer transient:
            yalign 0.62#0.743
            xalign 0.5
        menu:
            "They flashed you a charming smile."
            "If you tried to make the thief see the error of their ways, turn to page 142." if not thiefWrong:
                pov "But isn't that wrong and evil?"
                t "Of course!"
                t "I was born evil, and I've only gotten more evil every day I'm alive."
                t "But don't worry, the Mushroom cares nothing for money. It'll get much better use in our pockets."
                $thiefWrong = True
                jump thiefConvo
            "If you accepted, and joined the Master Thief on this daring Mushroom heist, turn to page 143.":
                t "Wonderful! This will be a caper for the books."
                t "You'd best be careful, though. I'm rotten to the core, and I'm sure to betray you sooner or later."
                jump thief3
            "If you accepted, while secretly planning to betray the Master Thief at a critical moment, turn to page 143.":
                t "Wonderful! This will be a caper for the books."
                t "You'd best be careful, though. I'm rotten to the core, and I'm sure to betray you sooner or later."
                jump thief3
            "If you refused, and rushed to warn the Mushroom of this impending theft, turn to page 144.":
                t "Aha, I knew you'd see things my - wait, what did you say?"
                "Before they could react, you slipped away from them and ran away into the woods, heading for the Mushroom's house."
                "Soon you stood knocking at the Mushroom's door, panting for breath and covered in scrapes from the journey."
                jump mushroom1

# Act 2, Chapter 3A: Help the Mushroom against the Thief
label mushroom1:
    #if mushroomCurse:
        #m "I warn you, this better be a good one, or I'll curse you right back into the mud."
    show hand onlayer transient:
        yalign 0.7#0.743
        xalign 0.5
    menu:
        m "You again? Have you returned with a tale for me?"
        #TK: Add a bunch of potential tales here.
        #"Tell the tale you heard from the Goose-boy.":
        #"Tell the tale you heard from the Gloom-monger.":
        #"Tell the tale you heard from the Mayor.":
        #"Tell the tale you heard from the Sparrow-Herder.":
        "If you told the tale of how you attempted to catch the Master Thief, turn to page page 134.":
            "The mushroom ushered you inside, and you both took a seat in the plush red armchairs. You pretended to sip a cup of decaying leaf matter as you told your tale."
            m "Well! Never in all the years I've known you have you ever told me a tale such as this!"
            pov "Um... we only just met tonight."
            m "You know what I mean. The other you's."
            label mushroomTales:
                show hand onlayer transient:
                    yalign 0.723#0.743
                    xalign 0.5
                menu:
                    #TK: more dialogue options here
                    m "I have to say, darling, your stories are improving. Still a bit flabby in the second act, but I was most intrigued by your subtle commentary on the innate oneness of being."
                    "If you ask the mushroom to lift the curse, turn to page 140." if not mushroomCurseChat:
                        m "Well, your tale still could have done with some improvement."
                        m "The plot was rambling, and the characterisation was flimsy at best."
                        m "But I suppose a deal's a deal. I swear I will not curse you with a mushroom's curse."
                        m "This time."
                        $mushroomCurseChat = True
                        jump mushroomTales
                    "If you ask the Mushroom about \"the other you's\", turn to page 138.":
                        m "No need to worry about it, darling. I'm just glad you decided to come clean about your plan to steal our treasure."
                        pov "No no... it's the Master Thief who's planning to steal the treasure."
                        m "Right, the \"Master Thief\" you. But of course you can just stop yourself from doing it, right?"
                        pov "Uh - I - That's not..."
                        jump mushroomThiefBattle
    label mushroomThiefBattle:
        "At just that moment, you noticed your cup had dissappeared from your hand and been replaced with an old gumboot full of pond scum."
        "You looked around and saw a shadow flit across the wall."
        "Grabbing a nearby jeweled scimitar, you leapt up from your seat and swung around to clash swords with the Master Thief!"
        t "Haha! You're learning."
        t "There's still time, you know. Join me."
        show hand onlayer transient:
            yalign 0.7#0.743
            xalign 0.5
        menu:
            t "Together we'll spit in the face of the law and destroy the concept of private ownership once and for all."
            "If you joined the thief, turn to page 126.":
                "You hesitated... and then you dropped your sword."
                t "Excellent. Now..."
                jump thiefFinale
            "If you refused, and defended the Mushroom's treasure, page 127.":
                pov "Never!"
                "You pulled yourself up and fought fiercely across the glittering hills of treasure, gold pieces sliding away with every step."
                "The Master Thief effortlessly riposted your blows with one hand, while the other hand darted around grabbing nearby gems and stuffing them into their cloak."
                jump mushroomFinale
        #"The mushroom looked shocked and saddened."


label mushroomFinale:
    m "Oh dear."
    "Another mushroom, identical to the lady, emerged from a side door."
    m2 "I know, it's awful."
    if he == "they":
        m2 "I mean, what are [he] trying to say, here? I think we can find a vague stab towards meaning in this performance, but who's the audience?"
    else:
        m2 "I mean, what is [he] trying to say, here? I think we can find a vague stab towards meaning in this performance, but who's the audience?"
    "You stumbled and teetered at the edge of a cliff as the thief's stabs pushed you backwards. Another identical mushroom popped up."
    m4 "Perhaps it's meant to be ironic."
    m2 "Perhaps it's satirical."
    m3 "Yes, but what is it satirising?"
    "You regained your footing and slashed the thief's sword out of their hands. Just as you were on the brink of victory, mushrooms swarmed up and surrounded you."
    m "I think we've seen enough. It's time to get off the stage."
    "Before you could blink, they took hold of your ankles and dragged you down into the earth."
    m3 "Shh. Shhh."
    "The Master Thief managed to wriggle out of their grasp and leap up out a nearby window."
    t "Au revoir, my friend!"
    "That was the last thing you saw before you were dragged underneath the earth."
    "You were pulled down through untold layers of earth by your ankles. You heard the mushrooms whisper around you."
    #TK: Have a house of leaves text effect for the many mushrooms
    m3 "Everything's going to be ok.{vspace=30}                                             {w=0.4}You're safe here.{vspace=30}                                             {w=0.8}Shhhh."
    "Soon, you emerged into a colossal underground kingdom lit with flickering silver light."
    "All around you pressed a blooming mass of webcaps, milkcaps, scarlet elf caps, poisonpies, decievers, pinkgills, brittlegills, veiled ladies, lawyer's wigs, stinkhorns, earthstars, beefsteaks, chicken of the woods, earthballs, sculpted puffballs, yellowfoots, lungworts, brown-eyed wolves, golden-eyed umbrellas, Satan's boletes, false chanterelles, death caps and destroying angels, and all members of the mysterious Dark Taxa, the dark matter fungi that lie unknown to mankind."
    "They all swept to and fro through a twisted city of endless tunnels. The shape of a giant, pale and broken mountain loomed over the city, barely visible through the thick fog of spores."
    pov "I was about to win! Why have you kidnapped me?"
    m "Darling, trust us, that sad production wasn't going to win anything. You were hurting yourself."
    m2 "Hurting yourself."
    m "Please don't take the criticism too personally. It was an intriguing bit of invisible theatre. We do respect the way you put everything into the role. But you really must consider the problematic aspects of the piece."
    "Dozens of identical mushrooms pressed around you, speaking in soft, overlapping voices."
    m3 "I think it might be best if you stay here until I know that you're safe.{vspace=30}                                             {w=0.4}Until I know you're safe.{vspace=30}                         {w=0.8}It's for the best, if you stay here."
    m4 "I'll watch over you.{vspace=30}                                             {w=0.4}Over you.{vspace=30}                         {w=0.8}Watch over."
    "You were taken through a great palace of yellow chanterelles and dressed in robes of fine moss. Your room was lushly furnished with soft covers woven from black mushroom silk, and all the gems and gold and treasures of the earth were available to you."
    label mushroomPrison:
        show hand onlayer transient:
            yalign 0.63#0.743
            xalign 0.5
        menu:
            m "You will be safe here."
            "If you asked where you were, turn to page 145." if not mushroomPlace:
                "The mushroom looked at you sadly."
                m2 "We've talked about this many times, darling. Don't you remember?"
                m3 "This is the kingdom of Lady Death. Mother of Mushrooms. I am her fingers, and we take all things on earth to her."
                m "Would you like me to tell you the story again?"
                $mushroomPlace = True
                jump mushroomPrison
            "If you listened to the mushroom's tale, turn to page 152." if mushroomPlace and not mushroomDeathTale:
                $mushroomDeathTale = True
                "She sat down and began to tell you her tale."
                m "Once upon a time, Death came for Our Dear Lord, as it was His appointed time."
                m2 "He did not wish to go, and so they fought across the great sea of the world. We fought for forty days and forty nights, but eventually the Heavenly Father got the upper hand."
                m3 "He broke Our Lady across the sky, and cut off Her hands, and threw me down into the deepest pit underground. I was so weak that we could not pull ourselves up."
                m "\"What will become of the world,\" we asked ourselves, \"If I just lie here?\""
                m4 "\"There will be no more deaths, and soon there'll be so many people in the world that they won't have the room to stand next to each other.\""
                m3 "And so I extended Her long, broken arms, so that our fingers poked out of the soil."
                m2 "These fingers are the Mushrooms."
                m "We provide food for the poor and the animals of the forest, and I support the plants and connect them together."
                m4 "But most importantly, we do The Work."
                m2 "We take hold of the dead and the dying, and the old wood and the old bones, and carry it all down to my kingdom, far underground."
                m3 "I work slowly. We are patient. Soon, the work will be complete, and everything will rest here inside Her kingdom, as was intended when the world began."
                "The mushroom gestured to the pale mountain, looming over the city through the fog of spores."
                m4 "My body still lies there, broken. It is what the hills and forests and continents are built on. She lies in great pain, and it is but rarely that I can walk among men as we once did."
                if godfather == "Black":
                    m "It was a strange occasion indeed on which I walked the earth to become your godmother. I hope it was worth it."
                jump mushroomPrison
            "If you demanded to return to the surface, turn to page 146." if not mushroomImprisoned:
                m "I'm sorry."
                m "You're a danger to yourself. All of yourself."
                m "I only wish I could keep all of you in here, until you're well again."
                $mushroomImprisoned = True
                jump mushroomPrison
            "If you enquired as to what the mushroom meant by \"All of yourself\", turn to page 162." if mushroomImprisoned and not mushroomMyself:
                m "We've talked about this so many times, darling. And you have forgotten so much."
                m2 "You're not well."
                m3 "You argue with yourself. Even kill yourself. All the time."
                m4 "You make food and then give it to us to rot, while you lie starving."
                m2 "You build houses and then leave them empty, while you die of cold on the streets."
                m "We respect your dedication to your art. It is a beautiful performance."
                m2 "But is it worth the cost?"
                $mushroomMyself = True
                jump mushroomPrison
            "If you tried to explain that each human being has their own separate sentience and experience of the world, turn to page 154." if mushroomMyself and not mushroomPerson:
                pov "I think you're confused. Me and the thief and all those other people... they're separate. We aren't the same person."
                m "Darling, I think you're the one who's confused. You've been taken in by the surface elements of the piece without considering the greater picture."
                m2 "When you look at mushrooms on the surface, it may look like each one is a separate being."
                m3 "But when you look underneath, you can see it. It's all one beast. Impossibly large. Under the earth."
                m "You're the same. You've just forgotten."
                m4 "You can't see the shape of the great Human Being under the dirt."
                $mushroomPerson = True
                jump mushroomPrison
            "If you asked for food, turn to page 149." if not mushroomFood:
                m3 "Of course. One moment."
                "The mushrooms took one of their number out of the room. There was a chopping sound from outside. In moments, they returned with a rich mushroom stew."
                #Mushroom missing chunks out of itself image maybe.
                m2 "Here."
                $mushroomFood = True
                jump mushroomPrison
            "If you politely requested to be allowed out of the room, turn to page 147.":
                m3 "Do you promise not to hurt any of your selves?"
                pov "Um... yes, I do."
                m2 "Very well. I will come with you."
                m "You can go anywhere in the kingdom. But if I ever feel that you're a danger to yourself, we'll have to take you back here."
                jump mushroomKingdom

    label mushroomKingdom:
        "You walked out into the lush expanse of the underground kingdom. Rich moss and lichens flowered from every surface. "
        if godfather != "Black":
            m "Don't worry. I know about your godfather. He cannot reach us here."

        label mushroomExplore:
            show hand onlayer transient:
                yalign 0.63#0.743
                xalign 0.5
            menu:
                "Every type of fungi bustled around you."
                "If you explored the moss garden, turn to page 135." if not mushroomMoss:
                    #TK mushrooms
                    "The mushroom showed you all the wonders of that undiscovered land, where life and death go hand in hand."
                    "You saw the four seasons all flowering at once. To the north, the cicadas and crickets chirped loudly in a summer haze. To the south, the ground was silver white with snow. To the west, the autumn rains fell, and to the east was the full glory of spring."
                    "The wonder of those gardens were so great that the tongue fails to describe them, and you walked and watched for days, until your eyes were so full that they couldn't stand to see another scrap of beauty."
                    m "A bit kitsch, isn't it?"
                    $mushroomMoss = True
                    jump mushroomExplore
                "If you feasted in the great palace, turn to page 138." if not mushroomFeast:
                    "As soon as you entered the palace a train of toadstools appeared, all in ceremonial garb. With silent steps, they surrounded you, bearing delicacies of mushroom risotto and crisp goose roasted in truffle butter and dark red wine and platters of mushroom bourguignon with roast potatoes, and set this wondrous feast before you. "
                    m "You HAVE to try the truffle aioli, darling, that's my absolute favourite."
                    pov "You... eat mushrooms?"
                    m2 "Of course. And one day they will eat me."
                    "Never in your whole life had you sat down to such a marvelous feast, and you gorged yourself for days on end until they had to roll you out of the palace."
                    $mushroomFeast = True
                    jump mushroomExplore
                "If you explored the root embassy, turn to page 139." if not mushroomEmbassy:
                    "The mushroom took you down to show you the great roots of the whole forest above you. Delicate fungal networks wove through every root, carrying vital letters and trade agreements and treaties to every plant in the woods."
                    "You spent days amoung them, learning their intricate customs. You realised that the forest you knew was an intricate web of delicate alliances between opposing factions that hated each other with bitter envy."
                    m3 "Exhausting, isn't it? But it must be done."
                    m2 "If we didn't do this, the whole forest would probably fall into all-out war. And then we'd never get The Work done."
                    $mushroomEmbassy = True
                    jump mushroomExplore
                "If you explored the lands in the shadow of the vast, pale mountain, turn to page 146." if not mushroomPale:
                    "The mushroom took you closer to the shape you saw from the palace. It loomed over you, larger than life. With a start, you saw that it was breathing."
                    m2 "This is the Lady. She waits here, while we do The Work."
                    pov "The Work?"
                    #m "Uh-huh." #We are the fingers of Lady Death. Our job is to push up through the surface and drag everything up there down to Her kingdom."
                    m4 "We take all things down here, one by one. It's slow work. But already, those down here outnumber the ones above. I am more than halfway done."
                    m3 "Someday, everyone and everything will be down here."
                    m "On that day, the Lady will draw her fingers down through the soil and back to her."
                    m3 "We will finally have completed the piece. Our Magnum Opus. It will be spectacular, I assure you, darling."
                    m "Don't look yet, it's not finished. Barely a first draft, really, I'd be so embarrassed if you saw it in it's current state."
                    m2 "So much left to do."
                    m3 "No need to worry. We have all the time in the world."
                    "You felt a strange peace in the shadow of the pale lady, and you stayed there with the mushroom for many days, looking out at the splendour of the world."
                    $mushroomPale = True
                    jump mushroomExplore
                #"Marry the mushroom.":
                    #"Placeholder."
                    #"You get married and have a gorgeous ceremony together."
                "If you asked to return home, turn to page 148.":
                    #TK: Persistance: Make the mention of siblings change as you play through routes
                    if godfather == "Red":
                        "Such were the wonders of that kingdom that you almost forgot everything, even the riches you left behind and your siblings and your own country."
                    else:
                        "Such were the wonders of that kingdom that you almost forgot everything, even the home you left behind and your mother and siblings and your own country."
                    "But soon, your mind came back to you, and you realised that you did not belong to this wonderful land. And so you said to the mushroom:"
                    pov "I've been very happy with you, and you've been kinder to me than words can tell. But I must go back."
                    show hand onlayer transient:
                        yalign 0.66#0.743
                        xalign 0.5
                    menu:
                        m "Do you have to go? Why not stay with me here?"
                        "If you changed your mind and decided to stay here underground, turn to page 127.":
                            "For a long time, you thought over the Mushroom's proposal. Finally, you agreed."
                            show hand onlayer transient:
                                yalign 0.72#0.743
                                xalign 0.5
                            menu:
                                "You and the mushroom stayed together for many long and happy years, roaming the ancient underground gardens of that fungal kingdom."
                                "If you remained good friends with the mushrooms, turn to page 155.":
                                    if godfather == "Red":
                                        "You and the mushrooms stayed the greatest of friends, talking all through the small hours together."
                                        "You set up a quaint home in that strange country, and soon you were even able to find your poor mother and make amends for your wicked behaviour."
                                        "After a long time, your siblings came down to join you there, one by one."
                                    else:
                                        "You and the mushrooms stayed the greatest of friends, talking all through the small hours together."
                                        "You set up a quaint home in that dark kingdom. After a long time, your mother and siblings came down to join you there, one by one."
                                "If you married the mushrooms, turn to page 156.":
                                    "After slowly growing close over many years, you and the mushrooms all became married together in a beautiful ceremony. Your mother came down to the kingdom of death for the occasion, and all the plants and lichens and moss and toadstools of the forest were in attendance."
                            if godfather == "White":
                                "Long did your Godfather the Almighty search for you, but never could he find you, hidden as you were in that undiscovered country."
                            elif godfather == "Red":
                                "Long did your Godfather the Devil search for you, but never could he find you, hidden as you were in that undiscovered country."
                            elif godfather == "Black":
                                "And so the promise came to pass, and you took your place with the woman clad all in black, just as she promised your mother all those years ago."
                            call endStamp
                            "You stayed there at the side of the Pale Lady, forever and ever, until the final horn and the coming of the end of days."
                            jump end
                        "If you held fast to your desire to return to the world above, turn to page 164.":
                            if godfather == "Red":
                                pov "Don't think that I want to leave you. It's just that I must see my siblings and my old country."
                            else:
                                pov "Don't think that I want to leave you. It's just that I must see my old mother and my old country."
                            m3 "I see. Then we won't stand in your way. Take this to remember us by."
                            "She handed you a black box tied with a tassel of red silk."
                            m4 "This is the box of the jeweled hand, and it holds something very precious. Do not open it, no matter what happens."
                            "And so you promised that you would never open the box, and the mushrooms took hold of you and bore you back up to the surface."
    "You blinked in the harsh light of the sun above, and found that your eyes had become almost blind in the darkness below. Your skin was pale and shrunken."
    "As you looked around, a strange anxiety gripped you. The ancient old strangler fig was gone. You couldn't see the blue door to the mushroom's domain."
    "As you walked down the road to your house, something seemed wrong. The prople you saw walking past had different faces to the people you knew so well before. Even your old house was a different shape."
    "You walked up to your old home and called out:"
    pov "Mum! I'm back!"
    "But just as you were about to enter, a strange man came out."
    som "Who are you?"
    pov "What? Who are you? And why do you twist in that crooked way?"
    som "We're all crooked now, child. It's the law. But answer my question!"
    #You raced through crowds of bent and crooked people.
    pov "My name is [povname]."
    som "Don't joke around like that."
    som "It's true that someone by the name of [povname] once lived here, but that is a tale three hundred years old! [He] couldn't possibly be alive now."
    "When you heard those odd words, a terrible fear gripped you, and you ran out onto the street and across the land. The forest you knew was gone. A grey rain of ash fell ceaselessly across the land from the grey clouds above. The bent and crooked people of the land huddled in grim shelters underneath places that hideously resembled the hills and lakes and villages you once knew."
    "Over and over, you heard them mutter of the Ash Giants, and you heard terrible footfalls shake the earth from some distant place, closer all the time."
    "The awful feeling came over you that what the old man said was true. Each day you spent in the underground kingdom was as a hundred years on earth."
    "You ran through the grey streets and parking lots and abandoned shopping centers and vast, decayed, echoing airports and twisting underground toll roads and long slow landfill rivers that seethed with the serpentine motion of the trash queens as you stumbled onto the cracked bitumen roads and empty apartment complexes packed with flickering TV screens of static under the grim endless maze of freeways stacked above you that blotted out the grey sky above, but try as you might you couldn't find the way back to the kingdom you left."
    if godfather == "White":
        miw "Finally."
        "You felt a heavy hand fall on your shoulder. A great light shone behind you, too bright for you to turn and face it."
        miw "Long have I waited. Now, you will come with me."
        jump mushroomBox
    elif godfather == "Red":
        mir "Finally."
        "A crooked red hand fell on your shoulder, and you turned to see the cackling face of the old serpent himself."
        mir "Now you see that no matter how long you hide, none can escape the devil's clutches! Come with me, and we will dance together in hell forever."
        jump mushroomBox
    else:
        label mushroomBox:
            show hand onlayer transient:
                yalign 0.69#0.743
                xalign 0.5
            menu:
                "You felt the weight of the mushroom's box in your pocket."
                "If you opened the box, turn to page 178.":
                    "Having lost everything dear to you, you realised that there was no reason not to open it."
                    pov "At such a time, surely I will find something inside this box to save me and lead me back to the Mushroom."
                    if godfather == "White":
                        miw "No."
                    elif godfather == "Red":
                        mir "What are you doing? No!"
                    "You untied the red silk and lifted the lid of the precious box."
                    "As soon as you did, all of your years rushed out of the box, and they came upon you at once. Your hair grew and turned white, your back twisted into a knot with age, your face wrinkled up and you fell down dead in an instant."
                    "Poor thing! Because of your disobediance, never would you live to see your mushroom again."
                    call endStamp
                    "Little children, never be disobediant to those who are wiser than you, for disobediance is the mother of all misery and father of all woe."
                    jump end
                "If you refused to open the box, even when all hope was lost, turn to page 179.":
                    if godfather == "White":
                        "You hesitated - but in the end you couldn't bring yourself to break your promise to the mushroom."
                        call endStamp
                        "And so the Lord took you, and you rested in the basement of His White House forever and ever, until the final horn and the coming of the end of days."
                        jump end
                    elif godfather == "Red":
                        "You hesitated - but in the end you couldn't bring yourself to break your promise to the mushroom."
                        call endStamp
                        "And so the Devil took you, and you were trapped as his servant in Hell forever and ever, until the final horn and the coming of the end of days."
                        jump end
                    else:
                        "And so you stayed there, forever searching for an entrance back to that kingdom you missed so much."
                        "For years you searched, with no success. Soon, the Ash Giants came upon the world, and you felt their searing light upon your skin."
                        "As the light burnt you away, you felt something take ahold of you and draw you into the earth."
                        m "It's ok. It's just me. Just us."
                        m "You've returned."
                        call endStamp
                        "The mushrooms took you down into the earth. There you stayed at the side of Lady Death, forever and ever, until the work was complete, and the glory of it shone out forevermore."
                        jump end
            #You can stay with the mushroom and explore the mushroom world, different areas
            #NOTE: Use the story of Urashima Tarō, the Fisher Lad

    #Mosses
    #Parasites and cordyceps
    #Fungi that the ants farm
    #Symbiotic trading fungi that work with the plants
    #Ambassador mushrooms
    #At some point in all of this, you can marry the mushroom
    #God and the Devil cannot reach you while you're there.
    #In this menu you have the option to return home
        #If you do the mushroom gives you a jeweled box. You leave and find out that thousands of years have passed and all your friends are dead.
        #If God or the Devil are your godfather, they show up here and take you away
        #You can open the box. If you do, all your lost years come back to you and you wither and die on the spot. The mushrooms take you back down to the underground kingdom, where you lie forever with lady death.
        #If you don't open the box, you remain immortal and stay alive forever.

# Act 2, Chapter 3B: Journey with the Thief
label thief3:
    # if you accept, you sneak into the mushroom's house through fantasy traps and tricks (Swinging sawblades, magical traps, Ali Baba and the 40 thieves stuff.
    "The thief strode ahead on their long, long legs, and you had to run to keep up. Their nimble fingers were constantly moving, grabbing leaves off the trees or small rocks from the ground to fiddle with, and they couldn't seem to keep a single part of their body still for even a second."
    #TK: Backgrounds
    "The night grew dark."
    "You walked past a river."
    "You walked past an open field."
    #TK: background for the ruins
    "You walked past the ruins of the 6th age, a grim reminder of the inevitable destruction fast approaching your world."
    "You walked past a tree."
    t "So, tell me about yourself. Got a family? A pet? Likes, dislikes, hobbies, dreams, nightmares? If you were stranded on a desert island, which limb would you gnaw off first?"
    label thiefConvo3:
        if ThiefConvo3Options >= 3:
            jump thiefWatchThis
        else:
            show hand onlayer transient:
                yalign 0.58#0.743
                xalign 0.5
            menu:
                t " "
                #TK: Make this go down when your family is dissappeared
                "If you talked about your family, turn to page 88." if not thiefFam:
                    if godfather == "Red":
                        pov "I have a family. 12 brothers and sisters. No mother anymore, though. She was driven into the grave by my wicked ways."
                        t "My condolences and/or congratulations!"
                    else:
                        pov "I have a family. 12 brothers and sisters. No mother anymore"
                        t "How prolific your mother is! It must be hard to get a word in edgewise."
                    t "I have no family, of course. One day a horned toad sat on a magpie egg and I popped out fully formed."
                    t "I stole my first breath of air, then I stole these hands and these legs and this body of mine, and I've been stealing ever since."
                    $thiefFam = True
                    $ThiefConvo3Options +=1
                    jump thiefConvo3
                "If you talked about your new pet pig, turn to page 91." if pig and not thiefPet:
                    $thiefPet = True
                    pov "Well, because of you I have this pet pig now."
                    "The pig lept into your arms and oinked at the thief with great malice."
                    t "Gregory! You would abandon me, after all the schemes we've pulled together?"
                    p1 "Oink."
                    t "Oh, I can't stay mad at you, you silver-tongued devil. Come here."
                    "The thief patted the pig's head while it grunted cheerfully."
                    $ThiefConvo3Options +=1
                    jump thiefConvo3
                "If you talked about your lack of pets, turn to page 92." if not pig and not thiefPet:
                    $thiefPet = True
                    pov "No pets. I'd love to have one someday, though."
                    t "Do what I do. Talk with the magpies, and the rats, and the possums on the roof. You'll never be lonely again."
                    "They tossed up a hunk of bread, and a kookaburra swooped down and grabbed it out of the air."
                    $ThiefConvo3Options +=1
                    jump thiefConvo3
                "If you talked about your hobbies, turn to page 94." if not thiefHobbies:
                    $thiefHobbies = True
                    pov "Well, I like reading."
                    #menu:
                        #".":
                    t "Interesting. I never learned."
                    t "Too busy, you know. Schemes and such."
                    pov "Well, I can recommend it."
                    t "Perhaps I'll try it, if I can find the time."
                        #"I play sports sometimes.":
                            #"*PLACEHOLDER*"
                        #"*PLACEHOLDER* other answer":
                            #"*PLACEHOLDER*"
                    $ThiefConvo3Options +=1
                    jump thiefConvo3
                "If you talked about your dreams, turn to page 95." if not thiefDream:
                    pov "I dreamt I had a dad, once. That was nice."
                    t "Interesting. I dreamt the same thing."
                    t "More of a nightmare, really."
                    $ThiefConvo3Options +=1
                    $thiefDream = True
                    jump thiefConvo3
                "If you talked about your nightmares, turn to page 96." if not thiefNightmare:
                    pov "I've had this dream many times. I find myself in the middle of the forst. There is a great crowd around me, but I know someone is missing."
                    pov "I look down, and I realise I have no hands. Then I look down, and realise I have no feet."
                    pov "I always know what will happen next. I will look up, into the space between the trees. I am terrified, but I can't stop myself from doing it."
                    pov "I know I will see {color=#f00}something{/color} there. Waiting for me. In the dream, I know what {color=#f00}it{/color} is. I know what will happen when I see {color=#f00}it{/color}."
                    pov "I look up."
                    pov "I wake up screaming. I never remember what I saw there. Until I have the dream again."
                    "There was a long pause."
                    t "Well!"
                    t "Once I had a nightmare I was chased by clowns."
                    $ThiefConvo3Options +=1
                    $thiefNightmare = True
                    jump thiefConvo3
                "If you talked about what limb you would gnaw off first, turn to page 100." if not thiefLimb:
                    $thiefLimb = True
                    pov "I think I would gnaw off an arm first."
                    t "What? No, I could never. You need that arm for survival!"
                    "They flexed their long, slender fingers."
                    t "This is my money-maker. If I lose it, I'm finished."
                    $ThiefConvo3Options +=1
                    jump thiefConvo3
                "If you said nothing, turn to page 101.":
                    t "Alright, suit yourself."
                    jump thiefWatchThis

    label thiefWatchThis:
        t "Watch this!"
        "They caught hold of a tree bough and spun around on it, then lept off and landed on one foot on a nearby branch, balancing precariously."
        show hand onlayer transient:
            yalign 0.65#0.743
            xalign 0.5
        menu:
            t "Eh? Eh?"
            "If you clapped politely, turn to page 103.":
                t "Thank you, thank you!"
                "They bowed, blew you a kiss, then drew roses out of the cuffs of their coat and tossed them out to an imaginary audience. Then they lept down."
                t "Anyway, enough of my talents for now. We're here!"
            "If you enquired as to the source of the thief's incredible abilities, turn to page 108":
                t "The goblins taught me."
                "They lept off the branch and landed with perfect poise, posing dramatically."
                t "Anyway, enough of my talents for now. We're here!"
            "If you ignored the thief's displays of acrobatics, turn to page 105.":
                t "What? Come on, that was great!"
                "The thief sprang from the branch, performed a triple backflip and then landed on their hands. They looked at you expectantly, panting."
                show hand onlayer transient:
                    yalign 0.67#0.743
                    xalign 0.5
                menu:
                    t "How about that!"
                    #TK: Add a path where you keep being dismissive and the thief does bigger and bigger things to impress you
                    "If you gave a dismissive shrug, turn to page 104.":
                        t "What the - you're crazy. Come on, you must be out of your mind, that was amazing. You just don't know talent when you see it."
                        "They got back to their feet and sulked for the rest of the journey."
                        "Eventually, they brightened up as you approached your goal."
                        t "Alright. Never mind all that, then. We're here!"
                    "If you clapped politely, turn to page 106.":
                        t "Hmph. Acceptable. Thank you."
                        "They twisted over onto their feet."
                        t "Anyway, enough of my talents for now. We're here!"
                    "If you gave rapturous applause, turn to page 107.":
                        t "Thank you! Thank you!"
                        t "Now this is the praise I deserve."
                        "They twisted over onto their feet."
                        t "Anyway, enough of my talents for now. We're here!"
        "The colossal buttress roots of the Mushroom's fig tree rose above you."
        t "Alright. Here's the job."
        "They drew a floor plan in the dirt."
        t "The treasure is in the central chamber, here. The front door can only be opened with a password."
        t "There's another entrance up through the canopy, guarded by banksia boys."
        t "Or we could try to get in here, through an underground river patrolled by an old crocodile."
        show hand onlayer transient:
            yalign 0.65#0.743
            xalign 0.5
        menu:
            t "So what's the plan, chief?"
            "If your notes say that you {b}know the password{/b}, turn to page 131.":
                pov "I saw the mushroom put in the password. We can walk straight in the front door."
                t "You devil, you. Lead the way!"
                "You walked up to the fig and cut the vines and swamp flowers away to reveal the small blue door, inlaid with precious sapphires and intricate engravings."
                pov "Gorge, guzzle, gulp and grab; never shall this wound scab."
                "The door sprung open at once."
                jump thiefMushroomCavern
            "If you climb up and go in from above, turn to page 142.":
                t "Great idea. We'll draw you into a life of crime yet."
                "You climbed up through the canopy. Before you knew it, a gaggle of Banksia seeds dropped down all around you. Their many mouths gabbled at you with wild abandon."
                sc "That's right, it's me!"
                sc "Scraggs McKenzie, the baddest banksia in the bush."
                boys "You tell 'em, Scraggs! {vspace=30}                                             {w=0.4} Yeah! {vspace=30}                         {w=0.8}You're the best, Scraggs!"
                label scraggsConvo:
                    show hand onlayer transient:
                        yalign 0.68#0.743
                        xalign 0.5
                    menu:
                        sc "I bet you weren't expecting to run into me and my boys."
                        "If you asked the thief if they'd ever met these people, turn to page 172." if not scraggsBoys:
                            t "Never heard of him."
                            sc "What! Everyone's heard of Scraggs McKenzie and the boys."
                            boys "You know it, Scraggs! {vspace=30}                                             {w=0.4} Yeah! {vspace=30}                         {w=0.8}No-one messes with us!"
                            $scraggsBoys = True
                            jump scraggsConvo
                        "If you asked who they are, turn to page 173" if not scraggsMusical:
                            $scraggsMusical = True
                            #TK: "Musical number starting" piano sting
                            sc "Why, they call us..."
                            "Scraggs and company launched into a long, flashy musical number explaining their backstory, the details of which I won't bore you with here."
                            boys "...we're just tryna survive, in a world of baa-aad seeeeeeeds!"
                            sc "That's right!"
                            "You and the thief clapped politely."
                            jump scraggsConvo
                        "If you asked them to let you past, turn to page 174.":
                            sc "NO-ONE gets past Scraggs McKenzie."
                            sc "Not without answering one of my riddles first."
                            show hand onlayer transient:
                                yalign 0.66#0.743
                                xalign 0.5
                            menu:
                                sc "What walks on 4 legs in the morning, 2 legs at noon, and 3 legs in the evening?"
                                "If you answered \"Time\", turn to page 175.":
                                    sc "Ha Ha Ha! Wrong!"
                                    jump scraggsWrong
                                "If you answered \"Fate\", turn to page 175.":
                                    sc "Ha Ha Ha! Wrong!"
                                    jump scraggsWrong
                                "If you answered \"A dog jumping around on its hind legs\", turn to page 175.":
                                    sc "Ha Ha Ha! Wrong!"
                                    jump scraggsWrong
                                "If you answered \"Man.\", turn to page 176.":
                                    sc "That's... that's correct. You may pass."
                                    boys "You'll get 'em next time, Scraggs. {vspace=30}                                             {w=0.4} Don't worry about it. {vspace=30}                         {w=0.8} We still love you, Scraggs!"
                                    sc "I know, boys. I know."
                                    sc "Alright, go on through. But if me or my boys see you around here again, you'll be in serious trouble."
                                    "You walked down passed the banksias, and found a little yellow door in the tree."
                                    "You pulled it open and peered down inside."
                                    jump thiefMushroomCavern
                label scraggsWrong:
                    sc "You're in serious trouble now. Me and my boys are going to make you think twice before you step in this neck of the woods again."
                    boys "That's right, Scraggs. {vspace=30}                                             {w=0.4} You've got it handled! {vspace=30}                         {w=0.8} No-one does it like you, Scraggs."
                    sc "Alright boys, that's enough. Now listen here-"
                    boys "You tell 'em, Scraggs. {vspace=30}                                             {w=0.4}  They're nothing. {vspace=30}    {w=0.4}                              These jokers have nothing on you. {vspace=30}{w=0.4}This is in the bag, Scraggs. {vspace=30}                                   {w=0.8} You got this -"
                    sc "Boys! Please! Just give me a second."
                    sc "Aw geeze, now look what you've done. Y-you made me lose it with the boys."
                    sc "I'm sorry boys, I never shoulda spoken to you in that way. You don't deserve that kind of treatment."
                    boys "It's ok Scraggs!  {vspace=30}                                             {w=0.4}  We forgive you Scraggs. {vspace=30}                         {w=0.8}  Forget about it."
                    sc "Now it's personal. No-one disrespects my boys like that."
                    t "Watch out!"
                    "The thief dived into you and pulled you to the floor just as a razor-sharp banksia leaf slashed above you."
                    "The bankisa boys swung their leaves around them like sawblades, and their dozens of eyes opened and closed in fury."
                    "The thief dragged you up and you both darted and dived through the melee until you dove through a door in the tree trunk and slammed it behind you."
                    "You fell to the floor, gasping. You had some bruises, and you saw that the Master Thief had suffered a slash across their arm."
                    t "N-nothing to worry about."
                    show hand onlayer transient:
                        yalign 0.7#0.743
                        xalign 0.5
                    menu:
                        "The thief sprung to their feet, then faltered and fell against the wall."
                        "If you tried to help the thief, turn to page 182.":
                            "You tore off one of your sleeves and bound it around the thief's arm as a bandage. They grumbled about it, but accepted your help."
                            t "You're wasting your time, I'm telling you."
                            t "One day soon I will make love to the ropemaker's daughter, and the croaking of ravens will be our music for the occasion, and the world will be a better place for it."
                            show hand onlayer transient:
                                yalign 0.68#0.743
                                xalign 0.5
                            menu:
                                t "And then all your work will be for naught."
                                "If you tried to motivate the thief by telling them you plan to betray them, turn to page 183.":
                                    pov "Well, you'd better hold on a while longer. I plan to betray you and grab all the treasure for my own, and I can't do that if you're dead."
                                    t "Fantastic!"
                                    t "Then let the best betrayer win."
                                    "They grabbed your hand and shook it."
                                    "You pulled them up, and you both crept through the tree until you found a rotted red door."
                                    jump thiefMushroomCavern
                                "If you tried to push the thief onwards, turn to page 184":
                                    pov "Come on. Don't talk like that."
                                    "The thief shrugged."
                                    t "I never learned any other way to talk."
                                    "They struggled to their feet, and you both crept through the tree until you found a rotted red door."
                                    jump thiefMushroomCavern
                        #"If you have {b}the singing bone of Grundlesnitch{/b} in your items, turn to page 137."
            "If you entered through the underground river below, turn to page 173.":
                t "Great idea. We'll draw you into a life of crime yet."
                "You lept down a well and crept up the underground river until you came across an ancient, leviathan saltwater crocodile."
                t "Watch this."
                "Before you could say anything, they stole right up to the old master. With a flick of their wrist they stole his claws, and with a twist of their fingers stole his brightest emerald scales."
                t "Not impressed yet? How about this?"
                "They began reaching down into his gullet to steal the stones from his belly. You saw the crocodile's jaws about to clamp shut, and you grabbed their midnight cloak and pulled them away just in time."
                "The old lord snapped about in a fury and turned on you."
                t "Watch out!"
                "The thief dived and pulled you to the floor just as its powerful jaws closed above your head."
                "The thief dragged you up and you both darted and dived through the melee until you dove through a door and slammed it behind you."
                "You fell to the floor, gasping. You had some bruises, and you saw that the Master Thief had suffered a slash across their arm."
                label thiefHeal:
                    show hand onlayer transient:
                        yalign 0.68#0.743
                        xalign 0.5
                    menu:
                        t "N-nothing to worry about."
                        #TK: More menu options
                        "If you admonish the thief for their wild actions, turn to page 153." if not thiefCroc:
                            $thiefCroc = True
                            pov "Are you crazy? That crocodile could have swallowed you whole!"
                            t "So much the better. A crocodile's belly is no less than I deserve."
                            t "And you'd be better off not saving me next time, for I plan to soon betray you."
                            jump thiefHeal
                        "If you helped the thief in silence, turn to page 156." if not thiefHelp:
                            $thiefHelp = True
                            "You tore off one of your sleeves and bound it around the thief's arm as a bandage. They grumbled about it, but accepted your help."
                            t "You're wasting your time, I'm telling you."
                            t "One day soon I will make love to the ropemaker's daughter, and the croaking of ravens will be our music for the occasion, and the world will be a better place for it."
                            #"They smiled, but you could see pain behind the smile."
                            #TK: Illustration showing a pained smile for the character
                            show hand onlayer transient:
                                yalign 0.68#0.743
                                xalign 0.5
                            menu:
                                t "And then all your work will be for naught!"
                                "If you told the thief you plan to betray them, turn to page 183.":
                                    pov "Well, you'd better hold on a while longer. I plan to soon betray you and grab all the treasure for my own, and I can't do that if you're dead."
                                    t "Fantastic!"
                                    t "Then let the best betrayer win."
                                    "They grabbed your hand and shook it."
                                    "You pulled them up, and you both ventured further into the tunnel. Eventually you found a little silver door in the rock."
                                    jump thiefMushroomCavern
                                "If you tried to push the thief onwards, turn to page 184":
                                    pov "Come on. Don't talk like that."
                                    "The thief shrugged."
                                    t "I never learned any other way to talk."
                                    "They struggled to their feet, and you both ventured further into the tunnel. Eventually you found a little silver door in the rock."
                                    jump thiefMushroomCavern
    label thiefMushroomCavern:
                #TK: An opportunity for betrayal
                if mushroomCavernSeen:
                    "The door opened to reveal the vast cavern of glittering treasure far below. You saw the gold and gems and red mist of incense, just as it was earlier in the night."
                else:
                    "The door opened to reveal a vast cavern of glittering treasure far below."
                    #TK: Double check my descriptions on the heat - is it consistently hot rainforest sweaty weather
                    "It was the hollow interior of an enormous strangler fig. A great cavern was formed inside it, cold as ice despite the heat outside."
                    "The floor of the cavern was piled with rubies and sapphires and glinting emeralds and solid gold pieces, larger than your fist."
                    "All across the room were lush silks and pillars of precious metals of every type, and riches that would turn the King of Kings green with envy."
                    "You inhaled the rich dark scent of incense, and saw glimmering magenta smoke roll across the room and coat it all in a dark haze, smelling of the most incredible spices and herbs and enchanting odours."
                t "Jackpot."
                "The thief tied a rope around their waist, tied the other end to the doorknob, and began to lower themselves down to the treasure below."
                t "Come on!"
                show hand onlayer transient:
                    yalign 0.68#0.743
                    xalign 0.5
                #TK: Gems
                menu:
                    "You saw a jeweled scimitar stuck into the wood nearby."
                    "If you helped the thief with their plunder, turn to page 185.":
                        "You tied a rope around your waist and lowered yourself down to help the thief."
                        "They grabbed up a shining goblet, encrusted with rubies and amethysts and chunks of moonstone carved in the shape of wild flowers."
                        "As soon as they did,you heard a great terrible rumbling and groaning all around you, and the walls shook. The Mushroom emerged from a trapdoor in the floor and looked around wildly."
                        t "Whoops. Looks like we'd better work fast!"
                        jump thiefFinale
                    "If you grabbed the scimitar, betrayed the thief and defended the mushroom's riches, turn to page 186.":
                        "You grabbed the scimitar and slashed through the rope in a single motion."
                        "The form of the thief fell down below. As it fell away, you saw it was nothing but a raggedy old cloak stuffed with straw. You felt a sharp point at your back."
                        t "You're learning, my friend. But not quite quick enough. En Guarde!"
                        "You whirled around and barely parried a slash from the thief, but the force of the blow sent you tumbling away and onto a pile of sapphires."
                        "You pulled yourself up and fought fiercely across the glittering hills of treasure, gold pieces sliding away with every step."
                        "The Master Thief effortlessly riposted your blows with one hand, while the other hand darted around grabbing nearby gems."
                        jump mushroomFinale


label thiefFinale:
    pov "Run!"
    "You grabbed the thief's and tried to pull them away as they stuffed gems and jewels into their pockets."
    m "So you've decided to steal from our Lady after all?"
    if mushroomCurse:
        m "I knew should never have given you a second chance. Curse first, ask questions later, darling, that's what I've always said."
    else:
        m "How trite. I hoped you had the originality to avoid rehashing such dull tropes, darling."
    "The floor began to fall away before you, and all the golden treasure sprouted and turned into jellyspots and rust fungus and dog lichen and yellow staghorn and blue mould which bloomed in all directions."
    if pig:
        "The pig lept into your arms, grunting in fear."
    "The floor fell away as the black tongues of the earth wriggled out of the treasure horde and lashed around you, and out from the soil emerged ten dozen mushrooms, all identical to the one in front of you. For weapons they held puffballs and shield fungi and spindle toughshanks, and they walked towards you with slow but terrible confidence."
    #TK: Echo or repetition effect
    m3 "Drop the treasure.  {vspace=30}                                             {w=0.4} Drop the treasure.   {vspace=30}                                             {w=0.8}Drop the treasure.  "

    label thiefMushroomBattle:
        show hand onlayer transient:
            yalign 0.64#0.743
            xalign 0.5
        menu:
            "The mushrooms surrounded you."
            "If you tried fighting off the mushrooms, turn to page 189." if not mushroomFight:
                $mushroomFight = True
                "You grabbed a nearby candlesnuff fungus and parried a thrust from the closest mushroom."
                m "Hmm. I think I can see glimpses of what you were going for, darling, but ultimately the performance feels superficial and dated."
                "The mushroom effortlessly disarmed you with a sweep of her toughshank."
                m2 "Dissappointing."
                m4 "Agreed. A lackluster piece. One suspects the artist's best days are behind [him]."
                "Their attacks began to push you and the thief towards the edge of the ragged hole in the floor."
                jump thiefMushroomBattle
            "If you took the opportunity to steal some spare gems, turn to page 177." if not mushroomGems:
                $mushroomGems = True
                "You ducked back and crammed some tumbling gems into your pockets with your spare hand."
                "As you did, they burst apart into puffballs which sent a waft of spores out of your pockets. The room began to spin around you."
                "You slipped on a scarlet elf cap and began to fall into the pit. Below you, you could hear the slow beating of a great heart, and you looked down and saw pale flesh twisting languidly in the darkness of the earth."
                "The Master Thief threw up a grappling hook and grabbed hold of your waist. The hook caught, and the two of you swung across the cavern to solid ground."
                "Still, you couldn't escape the swarms of fungi."
                jump thiefMushroomBattle
            "If you ran for your life, turn to page 180" if not mushroomRun:
                $mushroomRun = True
                "You tried to run. But you were completely surrounded."
                m3 "No-one escapes the Lady's embrace.  {vspace=30}                                             {w=0.4} Lady's embrace.   {vspace=30}                                             {w=0.8}No-one.  "
                jump thiefMushroomBattle
            "If you lost all hope, turn to page 187.":
                pov "There's too many of them!"
                t "Not so fast."
                "They took a whistle from their pocket and blew on it, making a harsh, shrill whine echo through the cavern."
                "At first there was silence. The mushrooms paused."
                "Then, you heard an answering whistle, deep and loud enough to deafen you."
                "A brilliant light shine through the windows of the cavern. There was the sound of thundering wheels."
                #TK: Train SFX, horn, crashing sound
                "A train crashed through the walls of the cavern."
                "It was swarming with wild and chaotic shapes of all manner of monsters, and you could see a team of things holding onto the front and laying tracks in front of the train as fast as they could as it swerved through the cavern, fungi leaping aside before it."
                m "Really? A Deus Ex Machina, at this stage?"
                t "Grab on!"
                "Behind you the mushrooms closed in, throwing puffballs that exploded in clouds of spores around you. You ran up to the side of the train as it clattered along."
                "The thief pushed you up to grab onto the side of the carriage, then you reached down and pulled them up beside you."
                "The train whistled with full force, gathering speed until it smashed through the other wall of the cavern and shot through the trees of the forest, leaving the mushrooms behind."
                t "Well! Did you ever doubt me?"
                "From all across the train came a great cheer, and you looked around to see goblins of a thousand shapes emerge to hold up the thief in celebration."
                "Some had the heads of bats, some had the paws of cats, six heads, three heads, five arms, ten tails, and they bristled with tails and wings and fur and scales."
                "One crawled like a snail, one prowled like a wombat, one looked like seven doves tied together with string. All of them had a chaos of forms the likes of which you had never seen."
                "A dozen hands clapped you on the back and drew you into the train carriage."
                goblin1 "Have a drink with us! Any friend of the thief's is a friend of ours."

                label goblinTrain:
                    show hand onlayer transient:
                        yalign 0.64#0.743
                        xalign 0.5
                    menu:
                        "The train was bustling with a chaos of forms."
                        "If you sat down, turn to page 194." if not goblinSit:
                            "You fell into a chair and looked around."
                            "This part of the train was some kind of bar or gambling hall. Looking up through a maze of trapdoors in the roof, you could see there were many floors stacked above this one. Bathhouses, gardens, workshops and observatories."
                            if pig:
                                "Your pig nestled into the chair beside you and began to chat to the nearby goblins in the language of mud."
                            $goblinSit = True
                            jump goblinTrain
                        "If you looked outside, turn to page 195." if not goblinLook:
                            "A team of goblins hung off the back of the train and picked up the tracks behind it, then climbed around to hand the tracks to the goblins at the front, who laid them in front of the train as it squeezed through the trees of the forest."
                            $goblinLook = True
                            jump goblinTrain
                        "If you accepted a goblin beverage, turn to page 196." if not goblinDrink:
                            "The goblins poured you dozens of goblin brews, bubbling ales and steaming warm ciders, goblin wines that oozed with red fog and goblin brandies that froze and melted and froze again as you drank them."
                            "Foolishly, you drank deeply of the brews. You guzzled them down until you could drink no more, until your vision was a haze and the brew ran down your mouth and drenched your clothes, and still you thirsted for them."
                            "From that day on, no other drink would ever be able to quench your thirst, and you would always shiver and feel cold without the wild drunken feeling of warmth the goblin drinks gave you."
                            goblin2 "On the house! Just for tonight."
                            $goblinDrink = True
                            jump goblinTrain
                        "If you went to find the Master Thief, turn to page 197.":
                            "You walked through the cramped corridors of the train and found yourself in a giant feast hall where they were celebrating the Master Thief at the head of the table."
                            goblin3 "Show us the loot!"
                            goblin1 "Yeah, what'd you get?"
                            "The thief nervously reached into their pockets and turned them out."
                            "All the precious gold and gemstones had turned into nothing but mud, sticks, rocks and lichen."
                            "A tumble of mould and webcaps and orange peel fungus dropped onto the table."
                            "The goblins stared in silence."
                            "Then erupted into wild cheers."
                            goblin1 "These are some of the shiniest rocks I ever saw!"
                            goblin2 "Now, look at that. That right there is a nice stick if ever I seen one, and I seen quite some sticks in my time. That one is goin' in the nest for sure."
                            goblin3 "'Ow'd you get such good mould? This is the best mould haul I've seen since the great fungus caper of '48!"
                            "The crowd quieted down as a grizzled old goblin called for a toast."
                            goblin4 "Ahem! Hem Hem Hem!"
                            goblin4 "I declare your apprentiship complete!"
                            goblin4 "And so, with all the power invested in me, I hereby dub thee..."
                            goblin4 "{b}The Junior Thief!{/b}"
                            "She held up the thief's hand and all the goblins cheered and danced and sang and rolled around in celebration."
                            "The thief smiled awkwardly. But for some reason, they didn't seem to share in the good mood. The smile quickly slid off their face, and they made an excuse to leave the party."
                            label goblinTrain2:
                                show hand onlayer transient:
                                    yalign 0.64#0.743
                                    xalign 0.5
                                menu:
                                    "The celebration raged on through the train carriage."
                                    "If you celebrated with the goblins, turn to page 198." if not goblinCelebrate:
                                        $goblinCelebrate = True
                                        "The goblins laughed and cheered and served goblin fruits and carved goblin hams made of rich mould and mud and played goblin games all across the table."
                                        if pig:
                                            "Your pig was quickly drawn into a wager, with it's greatest hopes and dreams as the stakes. Fortunately it won, and was granted a a small kingdom in the blue mountains as it's prize. It would go on to raise a mighty pig empire there, and rule over it for the rest of it's days."
                                        else:
                                            "You could see goblins betting on the games with their hopes, dreams and fears as the stakes."
                                        jump goblinTrain2
                                    "If you partook of the goblin food, turn to page 199." if not goblinFood:
                                        $goblinFood = True
                                        "Foolishly, you tasted the goblin fruits."
                                        "They were sweeter than honey, stronger than wine, clearer than water and darker than tar."
                                        "You gorged yourself until you could eat no more, until you knew not whether it was night or day, and still your mouth watered for them."
                                        "From that day forward all other foods would be ash in your mouth, and you would wither and go grey with the need of them."
                                        jump goblinTrain2
                                    "If you went to find the thief, turn to page 167.":
                                        "You found them sitting on the rear balcony with their legs over the edge, watching the trees and hills roll by in the smokey night."
                                        t "Hi."
                                        "You sat there with them in silence for a while, looking out."
                                        t "Oh, before I forget."
                                        if stuffStolen:
                                            "They handed back the suckling pig and all of the loose change stolen from the village, along with your stolen posessions and some extra money for payment."
                                        else:
                                            "They handed back the suckling pig and all of the loose change stolen from the village, along with some extra money for payment."
                                        label thiefConvo2:
                                            show hand onlayer transient:
                                                yalign 0.66#0.743
                                                xalign 0.5
                                            menu:
                                                t "Sorry about that."
                                                "If you asked about the train, turn to page 168." if not thiefPlace:
                                                    $thiefPlace = True
                                                    pov "What is this place?"
                                                    t "The goblin train."
                                                    t "It travels wherever there are thoughts and dreams for the goblins to steal. Provides safe passage to desperate souls. Serves the will of the goblin queens. That kind of thing."
                                                    jump thiefConvo2
                                                "If you asked them about the ceremony, turn to page 169." if not thiefJunior:
                                                    $thiefJunior = True
                                                    pov "So... Junior Thief? I thought you were the Master Thief."
                                                    goblin1 "{i}Master{/i}? Oh Lord, that's a good one! Our young thief's been telling you some real porkies if you've picked that up!"
                                                    goblin1 "They need to complete the seven year advanced traineeship to even become a Journeyman Thief. Then they MIGHT be able to apply for their masters, IF the queen thinks they're good enough!"
                                                    "The goblin wiped tears of laughter from their eyes and headed back into the train, pulling a sack of coal behind them."
                                                    t "Um. Sorry about the deception."
                                                    t "My skill is nothing compared to the goblins. They can steal the thoughts from your head, quick as a wink."
                                                    t "Just thought it sounded more impressive than Apprentice Thief."
                                                    jump thiefConvo2
                                                "If you ask them about their apprenticeship, turn to page 163." if thiefJunior and not thiefApprentice:
                                                    $thiefApprentice = True
                                                    t "Yep. I've proved myself now."
                                                    t "I've been training here for a full year. This was my final test."
                                                    t "I have to thank you. I couldn't have done it without you."
                                                    jump thiefConvo2
                                                "If you asked them why they aren't celebrating, turn to page 170.":
                                                    show hand onlayer transient:
                                                        yalign 0.67#0.743
                                                        xalign 0.5
                                                    menu:
                                                        t "It's a long story."
                                                        "To hear the long version, turn to page 171.":
                                                            pov "I don't have anywhere to be."
                                                            t "Oh, well. No harm in telling you, I suppose."
                                                            jump thiefStory
                                                        "To hear the short version, turn to page 181.":
                                                            pov "Well, you'd better make it quick."
                                                            $thiefShort = True
                                                            if godfather == "Red" or godfather == "White":
                                                                pov "Time is moving on, and I need to find a way to escape my Godfather before midnight."
                                                            elif godfather == "Black":
                                                                pov "Time is moving on, and I need to find a way to escape my Godmother before midnight."
                                                            t "Right. I'll keep it short."
                                                            jump thiefStory
                                                        "To hear the incredibly short version, turn to page 188.":
                                                            pov "Well, I don't have a lot of time..."
                                                            t "Alright, my parents are bad and they gave me to the goblins to train as a thief. The goblins made a deal that if they couldn't recognise me when my apprenticeship ended in a year, I would go free."
                                                            jump thiefStoryEnd
label thiefStory:
    #TK: Needs more interactivity.
    if thiefShort:
        t "Long ago, the Lord came to visit my parents. I heard my mother gesture to me, and talk to The Lord of me thus:"
        thiefmum "Inside all good people there dwells a golden soul, given by you, oh Lord. But as soon as you look, anyone can see this one has nothing but a hollow nest of spiders and rats inside. What trade can I teach such a one as this?"
        #TK: Some kind of text effect for g-d's speech
        t "The Lord thought on this, and said {b}\"Bring all your children before me.\"{/b} To the first child He said:"
        miw "{b}You shall become a powerful King.{/b}"
        t "Then to the second, and third, and so on down the line:"
        miw "{b}You shall become a Duke.{/b}"
        miw "{b}You, a rich Merchant.{/b}"
        miw "{b}You, a Tanner. You, a Shoemaker. You, a Butcher. You, a Beggar.{/b}"
        t "Then He finally reached me at the end of the line."
        miw "{b}And you shall be a Thief.{/b}"
        t "My parents took me to the goblins to learn the art of Thievery as the Lord instructed."
        t "One of the Goblin Queens sat and talked with me for a long time. Then they went to my parents and said:"
        goblinQueen "Your child will be taught well. We will keep them as an apprentice for one year."
        goblinQueen "Come back then, and if you can still recognize them, I won't take any money for my services and you can take them away."
        goblinQueen "But if you cannot recognise them, you must give me three hundred talers, and they must be allowed to go free and do as they will."
        jump thiefStoryEnd
    else:
        t "My mother gave birth to 8 children - some beautiful, and some ugly."
        t "After much time passed, the Lord came by to visit. My parents were delighted, and they gathered the children around them."
        t "The beautiful children were washed and bathed, and placed in newly washed shirts. However, the ugly children were placed out of sight."
        t "One was hidden under the straw, one under a wine barrel, one under the leather we used to cut our shoes, one under the cloth from which she made our clothes. And finally, I was placed in the coal chute."
        t "And so the Lord visited the house, and ended up staying there for many years."
        t "I saw Him often from the crack in the door to the coal chute. I cried to see His glory, and my tears carved trails of pale gold down my cheeks."
        t "One day I heard my mother talk of me to the Lord, saying \"What are we to do with this one?\""
        thiefmum "Inside all good people there dwells a golden soul, given by you, oh Lord. But as soon as you look, anyone can see this one has nothing but a hollow nest of spiders and rats inside. What trade can I teach such a one as this?"
        t "The Lord thought on this, and said {b}\"Bring all your children before me.\"{/b} To the first child He said:"
        miw "{b}You shall become a powerful King.{/b}"
        t "Then to the second, and third, and so on down the line:"
        miw "{b}You shall become a Duke.{/b}"
        miw "{b}You, a rich Merchant.{/b}"
        miw "{b}You, a Tanner. You, a Shoemaker. You, a Butcher. You, a Beggar.{/b}"
        t "Then He finally reached me at the end of the line."
        miw "{b}And you shall be a Thief.{/b}"
        t "My parents took me to the goblins to learn the art of Thievery as the Lord instructed."
        t "One of the Goblin Queens sat and talked with me for a long time. Then they went to my parents and said:"
        goblinQueen "Your child will be taught well. We will keep them as an apprentice for one year."
        goblinQueen "Come back then, and if you can still recognize them, I won't take any money for my services and you can take them away."
        goblinQueen "But if you cannot recognise them, you must give me three hundred talers, and they must be allowed to go free and do as they will."
        jump thiefStoryEnd
    label thiefStoryEnd:
        t "My parents agreed, and went home. And now, that year has passed."
        t "Tonight, my parents will be here soon to take me away, and they always carry the Lord in their hearts."
        t "As soon as they arrive, He will instantly see me for the wretch I am. Then I will be whisked away from here again, and live there in the coal chute forever after."
        "They sighed."
        show hand onlayer transient:
            yalign 0.7#0.743
            xalign 0.5
        menu:
            t "There's still time. I can sneak away, and get myself arrested. Then I'll be safe in a jail cell for a bit."
            "If you gave them an inspirational speech, turn to page 191.":
                "You took their hand and squeezed it."
                pov "Come on. Haven't you escaped the wrath of The Lord and The Law all your life? Haven't you stolen fire and cheated death and escaped the hangman's noose at every turn?"
                pov "You've got this. No-one is better at hiding from G-d than you."
                "The thief held your hand tight."
                t "Thank you."
            "If you promised to stay with them no matter what, turn to page 192.":
                "You took their hand and squeezed it."
                pov "Don't do that. I'll stay with you."
                pov "If your parents want to take you, they'll have to take both of us."
                "The thief held your hand tight."
                t "Thank you."
        "In a few short hours, the thief's mother and father came."
        if godfather == "White" or godfather == "Red":
            "Midnight was approaching fast. You felt a cold chill come over you. Soon, your godfather would come and take you away."
        "The goblins lined up you and the thief with 12 goblins on a tree branch, all of you transformed to become king parrots and sparrows and magpies and birds of every type."
        if godfather == "White":
            "Just at that moment, the clock struck midnight."
            "The clouds parted and an unnatural sun shone through them,  bright as a searchlight in the dark of night."
            "You felt the hot rays of the Lord's gaze upon you, sweeping the line of people. Your skin blistered with sunburn as it struck you."
            miw "{b}Where is my godchild?{/b}"
            thiefmum "Yes. And where is my child?"
            "You felt the thief shake beside you."
            goblin4 "If you want 'em, you'll have to pick them out of the lineup!"
            "The Lord's gaze moved down the branch, hovering over the thief in their form as a blackbird."
            "Their breath grew short, and they looked straight ahead, trying not to seem as though anything was wrong."
            if pig:
                "The pig looked up from the ground with anticipation and fear."
            "After a long time, His gaze moved on down the line, hovering over each in turn. Finally, He spoke."
            miw "These are the ones we seek."
            "Rays of light beamed down on two cinnamon cockatiels at the very end of the line."
            "With a great shout, they burst into smoke, and revealed themselves to be goblins."
            "The whole line erupted into goblin smoke, and the two of you were revealed. In a flash, the goblins turned both the parents into hideous grubs which squirmed away and were buried in the dirt. The Lord cursed in disgust and vanished back behind the clouds, and the whole train leapt up in great celebration."
            "The thief stared about in amazement."
            t "But... "
            t "I felt the eyes of God upon me. How could He not see all the rot inside me?"
            pov "There is none. There never was."
        else:
            goblinQueen "Choose your child out of the line, and their life will be yours once more."
            "The thief's mother stood and stared for a long time, moving down the line slowly."
            "As she over you, the clouds parted and you felt the hot, bright rays of the Lord's gaze pierce through you, lighting up every scrap of darkness and guilt in your soul. The thief shook beside you."
            "Their breath grew short, and they looked straight ahead, trying not to seem as though anything was wrong."
            if pig:
                "The pig looked up from the ground with anticipation and fear."
            "After a long time, she moved on down the line. She stepped away and conferred with her husband. Finally, she spoke."
            thiefmum "This one is our child."
            "She pointed to a cinnamon cockatiel on the very left of the line."
            "With a great shout, it burst into smoke, and revealed itself to be a goblin."
            "The whole line erupted into goblin smoke, and the two of you were revealed. In a flash, the goblins turned both the parents into hideous grubs which squirmed away and were buried in the dirt. The blazing light vanished back behind the clouds, and the whole train leapt up in great celebration."
            "The thief stared about in amazement."
            t "But... "
            t "I felt the eyes of God upon me. How could He not see the rot inside me?"
            pov "There's none there. There never was."
            if godfather == "Red":
                "Just then in a puff of smoke, the Devil appeared! Your Godfather had come for you at last."
                mir "Well done, my crooked little friends! Always good to see The Man Upstairs outsmarted yet again."
                label devilNever:
                    show hand onlayer transient:
                        yalign 0.7#0.743
                        xalign 0.5
                    menu:
                        mir "Come along now. The Hour of Ghosts is almost up, and I need you to clean out all the boilers of hell!"
                        "If you refused, turn to page 200." if not devilRefused:
                            pov "Never!"
                            t "Psst. I think I know a way out of this. Let's go with Him."
                            $devilRefused = True
                            jump devilNever
                        "If you went with the devil, turn to page 201.":
                            t "Follow my lead."
                            t "May I come along too, oh Devil? Long have I wished to see the fires of Hell."
                            mir "Bah! We have so many thieves already. Why would I need another?"
                            t "But I am the sovereign of thieves, and all crooks owe me alliegance."
                            "And they proved it by stealing the Devil's golden tooth right out of his mouth. The Devil snatched it back with a snarl."
                            mir "Very well! A fine prize you shall make for my servants."
                            "And the three of you set along the path to hell, with the Devil rubbing His hands gleefully. As you walked, you passed a cherry tree full of red fruits."
                            t "Devil, please, if I may make one last request... may you please climb up that tree and hand us some cherries?"
                            "Believing the two of you to be broken, the Devil agreed. But as soon as he was on the tree, the thief whipped out a vial of salt. In a wink they drew a circle around the tree in chalk, and the old serpent was stuck to a branch as if He was glued to it."
                            mir "NOOOOOOOOOOOO!"
                            mir "Foolish mortal - you will pay dearly for this!"
                            t "Throw down my friend's contract, and I'll release you!"
                            "The Evil One refused for a long time, baring his teeth, wailing, and spreading an indescribable stench."
                            "But soon, the Hour of Ghosts was about to end, and the Goatfoot risked losing his reign forever, which wore Him down (As you can imagine)."
                            mir "Fine. Take it, then."
                            "He unscrewed his left horn, took out a yellowed parchment and threw it down. You recognised it as your Mother's handwriting, and in an instant you tore it into a thousand pieces. You felt a great weight lift from you."
                            show hand onlayer transient:
                                yalign 0.7#0.743
                                xalign 0.5
                            menu:
                                mir "Now let me go!"
                                "If you released the Devil to wreak havoc upon the world once more, turn to page 211.":
                                    "You nodded to the thief, and they use a pouch of mysterious coal dust to draw a circle around the tree."
                                    "The Devil was gone like the wind in an instant, cackling and spreading a terrible stench and causing misery and woe behind him. And He plagues the earth still."
                                    t "You're free now."
                                "If you leave the Devil trapped in the cherry-tree forever, turn to page 224.":
                                    "But you left Lucifer standing on that cherry-tree, stomping His feet and pulling out His hair and turning the air black with curses. And He stays there to this day."
                                    t "You're free now."
        "The sounds of goblin celebration erupted all around you."
        "You wrapped the Master Thief in a great bear hug, and lifted them up on your shoulders."
        if godfather == "Red" or godfather == "White":
            "You were both free at last."
        if pig:
            "The pig lept up joyfully into your arms, and you passed it up to the thief to lift aloft in triumph."
        "You lept on the goblin train, and the thief and the goblins danced and celebrated all through the night."
        jump thiefEnd
        label thiefEnd:
            if goblinFood or goblinDrink:
                show hand onlayer transient:
                    yalign 0.7#0.743
                    xalign 0.5
                menu:
                    "Alas, having tasted the goblin fruits, you could never return home to your family again."
                    "If you married the thief, turn to page 242.":
                        "After many adventures, the Goblin Queen married you on the train. There was a great goblin celebration for 40 days and 40 nights."
                        if pig:
                            "Your pig watched over the wedding ceremony with tears in his eyes, and stayed with you as your constant companion and friend."
                        "You lived there in happiness for all of your days, venturing from place to place with wild abandon"
                        if godfather == "Black":
                            jump thiefDeath
                        else:
                            call endStamp
                            "You live there still, rattling across the whole world on the Goblin Train, and you will have no rest until the Day of Judgement."
                            jump end
                    "If you remained good friends with the thief, turn to page 246.":
                        "You lived on the train in happiness with your friend the thief for all of your days, venturing from place to place with wild abandon."
                        if goblinCelebrate and pig:
                            "Your pig wished you a fond farewell, and went to live in his kingdom in the blue mountains."
                        elif pig:
                            "Your pig stayed with you as your constant companion and friend."
                        if godfather == "Black":
                            jump thiefDeath
                        else:
                            call endStamp
                            "You live there still, rattling across the whole world on the Goblin Train, and you will have no rest until the Day of Judgement."
                            jump end
            else:
                show hand onlayer transient:
                    yalign 0.715#0.743
                    xalign 0.5
                menu:
                    "In the morning, you were faced with a choice. Because you had not yet tasted the goblin fruits, you could still return to your family and the world of humans."
                    "If you bade the thief farewell and returned to your family, turn to page 243.":
                        "You bade a tearful farewell to the thief, and returned back to your world amoung the humans, where you lived for many years in joyous happiness."
                        if godfather == "Black":
                            jump thiefDeath
                        else:
                            "There you stayed for the rest of your days, growing slowly older. On cold nights, you swear you could still hear the whistle of the Goblin Train, and the laughter of the thief in the wind."
                            call endStamp
                            "And then came an elephant with a very long snout, and it blew the story out."
                            jump end
                    "If you stayed on the goblin train and remained good friends with the thief forever after, turn to page 244.":
                        "You lived on the train in happiness with your friend the thief for all of your days, venturing from place to place with wild abandon."
                        if goblinCelebrate and pig:
                            "Your pig wished you a fond farewell, and went to live in his kingdom in the blue mountains."
                        elif pig:
                            "Your pig stayed there as your constant companion and friend."
                        if godfather == "Black":
                            jump thiefDeath
                        else:
                            call endStamp
                            "You live there still, rattling across the whole world on the Goblin Train, and you will have no rest until the Day of Judgement."
                            jump end
                    "If you stayed on the goblin train and married the thief, turn to page 248.":
                        "After many adventures, the Goblin Queen married you on the train. There was a great goblin celebration for 40 days and 40 nights."
                        if pig:
                            "Your pig watched over the wedding ceremony with tears in his eyes."
                            if goblinCelebrate:
                                "After the wedding he wished you a fond farewell, and went to live in his kingdom in the blue mountains."
                            else:
                                "After the wedding, he stayed with you there as your constant companion and friend."
                        if godfather == "Black":
                            jump thiefDeath
                        else:
                            call endStamp
                            "And if you have not died, you live there still. On windless nights, your siblings whisper that they can hear your laughter, and the rattling wheels of the goblin train."
                            jump end
    label thiefDeath:
        if godfather == "Black":
            "But youth does not last forever."
            "One day, you felt yourself wracked with a terrible fever."
            "Then, you felt gout take hold of you and make all your limbs twitch, and you were bedeviled with one illness after another, and you fell into deep sleep for long days."
            if pig:
                "Neither the goblins nor the thief nor your loyal pig could help you, though they travelled through the land stealing the most priceless medicines and remedies for you."
            else:
                "Neither the goblins nor the thief could help you, though they travelled through the land stealing the most priceless medicines and remedies for you."
            t "We still have places left to try. Next we'll raid the treasure-palace of the lord of the plague doctors -"
            pov "Don't worry. I won't die until Death sends Her messengers."
            "But as you spoke, there was a knock on the door, and the goblins hesistantly opened it to reveal the wise mushroom from the forest."
            if mushroomCurse:
                m "I suppose my curse won't be needed after all."
            m "It is time. Come with me."

            label deathThiefQuestions:
                show hand onlayer transient:
                    yalign 0.63#0.743
                    xalign 0.5
                menu:
                    m "The mother of mushrooms is waiting for you."
                    "If you tried to object, turn to page 245." if not deathMessengers:
                        pov "But - is She going to break her promise? She said She'd send three messengers."
                        m "Didn't the fever rage at you? Didn't the Gout take hold of you and shake you to pieces?"
                        m "She even sent her sister, Sleep, to remind you of Her."
                        m "She has sent all her messengers. Now you must come down to Her kingdom."
                        $deathMessengers = True
                        jump deathThiefQuestions
                    "If you turned to say goodbye, turn to page 255." if not deathGoodbye:
                        $deathGoodbye = True
                        pov "Can I say goodbye first?"
                        m "Of course."
                        if pig:
                            "You turned to the goblins, the thief, and the pig."
                        else:
                            "You turned to the goblins and the thief."
                        show hand onlayer transient:
                            yalign 0.7#0.743
                            xalign 0.5
                        menu:
                            "They all cried bitter tears, and their tears drifted away as coal smoke."
                            "If you told them you loved them, turn to page 276.":
                                pov "Goodbye, my dear. I love you, so much."
                                t "I love you too."
                                if pig:
                                    "The thief, the pig and all the goblins embraced you in a warm, furry hug, and their tears fell upon you."
                                else:
                                    "The thief and all the goblins embraced you in a warm, furry hug, and their tears fell upon you."
                                t "I'm sorry I couldn't do more. You should have chosen someone else. Maybe if you'd-"
                                pov "Shh. I chose you. You have nothing to be sorry about."
                                "And you gripped them tight."
                                jump deathThiefQuestions
                            "If you told them goodbye, turn to page 278.":
                                pov "Goodbye, all of you. I will remember you always."
                                t "Goodbye."
                                if pig:
                                    "The thief, the pig and all the goblins embraced you in a warm, furry hug, and their tears fell upon you."
                                else:
                                    "The thief and all the goblins embraced you in a warm, furry hug, and their tears fell upon you."
                                t "I'm sorry I couldn't do more for you. You should have chosen someone else. Maybe if you'd-"
                                pov "Shh. I chose you. You have nothing to be sorry about."
                                "And you gripped them tight."
                                jump deathThiefQuestions
                    "If you accepted your fate, turn to page 265.":
                        pov "Alright. I'm ready"
                        m "No-one's ever ready. But there's no time left."
                        "She gently took you down to the kingdom of Death."
                        call endStamp
                        "And what happened after that, none who live can say."
                        #"And what happened to the Toad, you ask?"
                        #"He was never heard from again."
                        jump end

# Act 2, Chapter 2B: Journey with the Toad
label toad1:
    "He gulped down the rest of his plate and stumbled unsteadily away from the table."
    "You both stepped into the toad's squash carriage, and it went rattling away down the path into the great, dark forest."
    #TK: Transition: Fade to black and then to the next scene.
    # "Before long you came to a great rushing river."
    # r "Halt! None may cross me and live!"
    # "You looked down into it and saw that it was proud and frothing with rage."
    # f "Never fear. My boys will have us over this at once!"
    # "He whistled for the magpie, the rat, the bat and the old black cockatoo."
    # "The Magpie" "Yeah... nah."
    # "The Rat" "This is a bit above our pay grade."
    # "The Bat" "Not to mention, you haven't actually paid us yet."
    # "The Old Black Cockatoo" "Yeah, where's our money?"
    # "The toad coughed nervously."
    # f "I-I assure you fellows, the check is in the mail..."
    # "But when it became clear the toad had no money on him, the whole crew fled in disgust."
    # "They tumbled over the toad and stole the squash carriage away with them."
    # f"Never fear! I don't need those louts to deal with a puddle like this!"
    # "And with that, he hurled himself into the water and was swept away immediately."
    # menu:
    #     "Tell the river about your quest.":
    #         y "Excuse me, River, would you mind letting me cross? And spitting out my friend?"
    #         y "We have urgent business with the Wild Witch of the Woods."
    #         "\"The Witch?\" quailed the river. \"Why didn't you say so?\""
    #         r "I have no desire to mess with her business. I heard she eats mountains for breakfast, and drinks lakes for lunch!"
    #         "And with that, it surged aside to let you pass and spat the Toad out on the far side."
    #         y "Thank you."
    #         "You walked across the dry river bed."
    #     "Plead with the river.":
    #         "PLACEHOLDER"
    #     "Bargain with the old river.":
    #         "PLACEHOLDER"
    # "\"Another successful adventure,\" croaked the toad as he crawled up out of the mud of the river and tried to straighten his battered hat."
    # "He coughed up some riverwater, shuddered weakly, then stood up and said to himself in a stern voice:"
    # r "I am Bridlebrogue Chippingham, and I\'ve never failed at anything in my life."
    # "With this, he regained his former swagger, and the two of you continued on down the path."
    #
    # "Before long, you came upon a cassowary: the wildest and most dangerous creature in the forest. A terror on the earth. The bird that killed the dinosaurs."
    # f "Worry not. I will use my charm and cunning to outwit this foul creature."
    # "He approached it in the manner of a merchant, saying \"Hello, dear fellow! May I interest you in some fine amber jewels?\""
    # "Within moments the toad was trounced to within an inch of his life."
    # "His pockets were turned out, his gold was scattered to the trees, his shoes were split open, his hair was messeed up, his ears were pulled, and he was sent flying over the trees."
    # "His clothes were torn, his hat was caved in, and his breeches were stained with mud."
    # menu:
    #     "Challenge the Cassowary to single combat.":
    #         "\"Fight me, Cassowary!\" you said, like a fool."
    #         "It reared up before you with it's terrible claws, and your life would surely have been snuffed out then and there."
    #         "But just at that moment, a giant Powerful Owl swooped down, grabbed the Cassowary in it's claws, and flew away into the night."
    #         "Why did this happen? Who can say."
    #         "You ran down the path to find the Toad."
    #     "Give the Cassowary a respectful nod and walk around it.":
    #         "You gave the Cassowary a wide berth and ran to help the Toad."
    # "\"Never fear!\" he wheezed, untangling himself from a tree. \"I have subdued the brutes. I just... need a moment.\""
    # "He sat down on a stone for a long time, breathing heavily and trying not to cry."
    # menu:
    #     "Maybe I should go first next time.":
    #         f "N-nonsense! I would hear of it."
    #         "He unsteadily got up, uncrumpling his once-fine hat. You heard him whisper to himself."
    #         f "I... am Brildebrogue Chippingham. And I have never failed at anything in my life."
    #         "With this, he put on the broken hat, and the two of you continued down the road."
    hide treesbg
    show nightbg at artPos
    "As you went down the road, the forest began to get darker and darker."
    "The trees closed in like a wall around you, and the moon and stars fled in fear."
    f "Nothing to fear, my friend! My boys will get us through this dark road, quick smart!"
    "He waved the crow-shrike, the rat, the bat and the old black cockatoo onwards. But instead of going faster, they slowed down and came to a stop."
    f "What? Why are you stopping?"
    crowshrike "Well... now seems as good a time as any."
    rat "We've been meaning to have a bit of a chat with you, mate."
    bat "About the payment situation."
    "The toad coughed nervously."
    f "I-I assure you fellows, the check is in the mail..."
    cockatoo "Not good enough. Get him, boys!"
    "And with that they fell on the toad and took him for all he was worth and dumped him on the side of the road."
    "Then they turned to you and respectfully escorted you from the carriage."
    show hand onlayer transient:
        yalign 0.7#0.743
        xalign 0.5
    menu:
        crowshrike "Sorry about all that. You seem nice enough. Good luck with it."
        "If you asked for a lift, turn to page 231.":
            rat "Yeah, nah."
            cockatoo "I can't let the boys risk their necks with the Wild Witch of the Woods."
            "They all shivered."
            crowshrike "If you live through it, come get a drink with us sometime."
        "If you ask where they're headed, turn to page 232.":
            bat "Back to the feast, I reckon."
            bat "There's some mangos in the gutter with my name on them."
    "They jumped in the old rotten squash and rode it away back to the village, leaving you both on the side of the road."
    f "...Uh..."
    f "A-another successful adventure! Good thing I was able to fight off those ruffians!"
    "He coughed up some mud from the ditch, shuddering weakly."
    "Then he stood up and said to himself sternly:"
    f "I am Bridlebrogue Chippingham, and I've never failed at anything in my life."
    "With this, he regained his former swagger and strode forward."
    "You walked through the trees together."
    hide nightbg
    show nightgodbg at artPos
    "The Firmament looked down at you from Her place up above."
    hide nightgodbg
    show nightbg at artPos
    show hand onlayer transient:
        yalign 0.7#0.743
        xalign 0.5
    menu:
        "You followed the toad through a dense swamp of crooked mangroves."
        "If you asked him about the witch's cottage, turn to page 233.":
            pov "How do you know where the witch's cottage is?"
            f "Oh... just my natural good sense of direction, I suppose! Ha ha!"
            f "When you become an adventurer like me, you just know these things."
        "If you asked him about the forest, turn to page 234.":
            pov "Have you been through this part of the forest before?"
            f "Oh... no, of course not. No, I'm far too busy being off at more important places, with more important people. All across the world. Barely have a moment to myself, you know."
            f "I wouldn't have the slightest idea what it's like to live in a swamp like this. Ha. Ha."
    f "Come on, we can't let ourselves be cowed by a little darkness! Why, I remember when I was journeying through the pits of Arborkios, where darkness is forged on a black anvil of star-stuff, and the blackest night shelters for rest each night after being torn apart by the light of day each morning! Well, I marched right on through that black pit, and I said -"
    f "Ack!"
    "You heard him trip over in front of you and go tumbling down and down through the muck of the rainforest until he fell into a deep pit and landed at the bottom with a crash."
    "You picked your way carefully down to him."
    f "Never fear! I have found... a shortcut!"
    f "I just... need a moment. M-might have... sprained my ankle there, I think. And maybe my arm."
    "He wheezed and lay there in the mud for a long time, breathing heavily and trying not to cry."
    "You heard him whisper to himself weakly."
    f "I am B-brildebrogue Chippingham. And I..."
    show hand onlayer transient:
        yalign 0.7#0.743
        xalign 0.5
    menu:
        #TK: Have more options here for the diffent godfathers
        "He trailed off."
        "If you helped the toad up, turn to page 235.":
            "You reached down and found the toad's hand."
            "Even in the darkness, you saw him blush bright red."
            f "Well I - t-this is all most..."
            f "Hand-holding, before marriage? What will people say?"
            "You picked him up out of the muck and held him in your hand."
            f "Good, good. I-I'll lead you onward."
    "You walked on. Soon, you began to see a glimmer of silver light in the darkness."
    hide nightbg
    show treesbg at artPos
    "The forest was covered in great puddles of water from the rains. The puddles shone with light."
    "All around you, the woods were dark and empty. But when you looked into the water, you saw the reflection of a shining cottage."
    jump puddle

    label puddle:
        show hand onlayer transient:
            yalign 0.68#0.743
            xalign 0.5
        menu:
            "The toad gasped in terror at the sight."
            "If you looked into the puddle carefully, turn to page 236." if not puddleLook:
                "You crawled to the edge and looked down into the puddle."
                "The surface of the water was flat and still."
                "The cottage in the reflection shone with bright light, as if the setting sun was behind it."
                "There was no trace of a cottage in the world above the water."
                $puddleLook = True
                jump puddle
            "If you dropped a stick in the puddle, turn to page 206." if not puddleStick:
                "You picked up a stick from the ground, and tossed it into the puddle."
                "It fell in without a single ripple in the water."
                "You saw it drop through into the reflection, and land close to the cottage."
                "You looked up. There was no trace of it in the world outside the reflection."
                $puddleStick = True
                jump puddle
            "If you jumped into the puddle, turn to page 207.":
                "You held the toad tight, then leaped into the puddle."
                "The world flipped over."
                "You felt the water pass over you, and a cool chill tingled all through your body."
                "When you opened your eyes, you were standing right way up again."
                "The puddle you had jumped into was now a floor, like a silver mirror."
                "All around the puddle was a dense and terrible darkness. You didn't want to think about what might happen if you fell off into it."
                "Past that, you could see a network of puddles, streams, lakes and estuaries. All shining silver like the puddle you were now standing on. A network of silver paths and blotches."
                "At the center of the winding paths was the cottage, shining with light."
    "The toad was very quiet now. His fine suit was ruined with mud. He jumped out of your hand and sat down."
    f "You'd... better go on. I'd just slow you down."
    show hand onlayer transient:
        yalign 0.7#0.743
        xalign 0.5
    menu:
        "He twisted his once-beautiful hat in shaking hands and looked down at the ground."
        "If you encouraged the toad, turn to page 214.":
            pov "Thanks for pretending to fall down back there."
            f "What?"
            pov "Well, I know you must have done it deliberately. Just so I would have something to do."
            pov "After all, you were leading us here so easily!"
            pov "Thanks for making me feel included."
            f "Oh... yeah."
            "He brightened up."
            f "Yes, I had to make sure you were included! We're both on this adventure together, after all. We're a team."
            "You saw him start to smile shakily."
            f "I did do an ok job getting us here, didn't I?"
            pov "Of course!"
            "You gently slapped him across the back."
            pov "You're Brildebrogue Chippingham, and you've never failed at anything in your life."
            "With this, the toad wiped the tears from his eyes, and beamed."
        "If you crushed the toad's feelings, turn to page 220.":
            pov "You have. It would be better if you'd never come."
            "The toad winced and looked away, trying not to cry."
            f "You're right. I'm sorry."
            f "I just..."
            f "I wanted to go on an adventure."
            f "I'll stay here, then. Don't want to get in your way."
            f "But if you aren't out in ten minutes, I... I'll come in to rescue you. Alright?"
            "You agreed."
            $toadSad = True
    "Soon, you had crossed the river paths to the cottage in the center."
    "The cottage was in the center of two great fig trees which sent their buttress roots all around and through the walls and roof."
    "Up over the walls grew a riot of herbs and flowers of every type, rambling over everything and growing in a lush green-grass garden on the roof. "
    "You saw the glimmer of two red eyes watching you from a small crook in the roof. Then there was a gasp from inside, and they disappeared."
    if not toadSad:
        "The closer you got to the cottage, the more the toad shook with terror."
        pov "You'd better stay behind. Guard the rear."
        f "G-good idea."
        f "But be wary, my friend. Few have ever left that cottage alive"
        f "Witches have red eyes. They see very far, but they have a keen sense of smell, like animals, and can sense when humans are near them."
        f "If you aren't out in ten minutes, I'll come in there to rescue you."
        jump witch2

# Act 2, Chapter 3: The Witch's Cottage
label witch2:
    "You walked up the front steps, and put your hand on the doorknob."
    "The door opened up with a shuddering creak."
    "Inside the cottage was a wild clutter of books and herbs and plants of all description, growing up the walls and roof."
    "The cottage was tiny, but the walls were covered with bookshelves stuffed with old manuscripts and notebooks and thick textbooks on all kinds of plants and animals."
    #TK: Herbs and plants
    "The wooden bookshelves were sprouting with herbs and plants of every type."
    "In the corner was a small kitchen with a cauldron, and up above was a small attic crawl-space."
    "Out of the attic poked a small head with a giant black hat. It looked at you with shock."
    w "Oh!"
    "It quickly withdrew into the rafters and you heard a great crash."
    "After a moment, out popped the witch, carrying a thick binder of notes and the remains of a broken pot plant."
    w "Um... hello!"
    "She set about trying to fix the pot plant back together with tape from her belt."
    "Coiling, midnight blue smoke slowly rose out from under her hat, fogging up the whole upper half of the cottage."
    w "I'm sorry, you startled me!"
    w "I don't get much visitors here."
    w "Or... any visitors, I guess."
    w "Please, h-have a seat! Can I get you some tea?"
    w "I have so much tea and I never get a chance to drink most of it because..."
    "Her expression became vague and confused."
    w "Because, uh... why do I..."
    w "Oh, the caffeine, that's right. The caffeine makes me too wired and I can't get to sleep at night, so I have to stick to all the herbal stuff."
    w "But you don't have to take the black tea if you don't want to, I have all kinds, it's fine. Or you don't have to have any kind of tea at all, that's totally fine too, I don't want to be out here stuffing tea down your mouth."
    w "I-It's just been so long since I had company for tea, so I haven't had a chance to get it out."
    w "Not that I like company at all, obviously."
    w "I spurn it!"
    w "I need no-one, and I want no-one."
    if witchArc == 0:
        w "We haven't met before, have we?"
    else:
        w "Hold on... we've met before, haven't we?"
    "She took out her binder of notes and began to leaf through it."
    label witchConvo1:
        show hand onlayer transient:
            yalign 0.625#0.743
            xalign 0.5
        menu:
            w "I-I don't think I have any notes on you?"
            "If you accepted a tea, turn to page 265." if not witchTea:
                w "Great!"
                "The witch lept up and started rifling through a towering triangular cupboard with dozens of tiny compartments hanging open."
                w "Ok, um..."
                #TK: Give you a chance to do false hydra stuff
                "She slowed down and looked into one of the drawers blankly."
                w "What was I..."
                pov "The tea?"
                w "Oh! Of course!"
                w "Ok, so I have some fancy sour cherry tea, English breakfast, Australian breakfast if you're feeling patriotic, green tea, lemon and ginger, and a pack of this stuff which, I don't know what it is to be honest, it's all in Japanese and I haven't tried it yet."
                #TK: More unique responses.
                show hand onlayer transient:
                    yalign 0.615#0.743
                    xalign 0.5
                menu:
                    w "What do you think?"
                    "If you asked for fancy sour cherry tea, turn to page 235.":
                        w "Nice! Coming right up."
                    #"If you asked for Oolong tea, turn to page 235.":
                        #w "Nice! Coming right up."
                    "If you asked for English breakfast, turn to page 235.":
                        w "Nice! Coming right up."
                    "If you asked for Australian breakfast, turn to page 235.":
                        w "Nice! Coming right up."
                    #"If you asked for Earl Grey, turn to page page 235.":
                    #    w "Nice! Coming right up."
                    #"If you asked for Dandy chai, turn to page 235.":
                        #w "Nice! Coming right up."
                    #"If you asked for Coconut chai, turn to page page 235.":
                    #    w "Nice! Coming right up."
                    "If you asked for Green tea, turn to page 235.":
                        w "Nice! Coming right up."
                    #"If you asked for Masala tea, turn to page page 235.":
                    #    w "Nice! Coming right up."
                    "If you asked for Lemon and ginger, turn to page 235.":
                        w "Nice! Coming right up."
                    "If you asked for the unknown tea, turn to page 235.":
                        w "Nice! Coming right up."
                "She turned on the stove and set a tiny kettle down on it. Then she looked around the clutter until she found two mugs tipped over on the floor, cleaned them out in the sink, and put the tea-bags in them."
                w "Ready to go, just need the water to boil."
                w "Sit, sit!"
                "You nestled down into one of the comfy old chairs by the stove, and she took the other."
                $witchTea = True
                jump witchConvo1
            "If you told her you'd never met, turn to page 271." if witchArc == 0 and not witchMeeting:
                w "Oh, good."
                w "It gets so awkward when someone just comes up and starts talking to me out of the blue, and I'm just like \"Mmhmm, yep,\" just nodding and trying to read through my notes when they aren't looking to see who they are, and they always think it's so rude but I'm like, hey, who just walked up and started talking to me without giving me time to read my notes first? THAT's what's really rude here."
                $witchMeeting = True
                jump witchConvo1
            "If you told her you met earlier tonight, turn to page 271." if witchArc >= 1 and not witchMeeting:
                w "Oh... tonight?"
                "An expression of panic came over her face. She leafed back and forth through her notes."
                w "I'm so sorry, this is so embarrasing, I'm... I'm afraid I don't quite remember."
                w "I mustn't have written it down. It's nothing to do with you, I'm just... if I don't write it down it goes straight out of my head. I'm sorry."
                $witchMeeting = True
                jump witchConvo1

            "If you asked about your Godparent, turn to page 262." if not witchGodfather:
                if godfather == "White":
                    pov "I'm hoping you can help me with a problem. My Godfather is the Lord, and He has sworn to take me away at midnight tonight."
                    w "That's wild."
                    w "I mean, I'm a witch, yeah, but I'm not exactly all powerful over here, I'm not sure what you want me to do about that?"
                    w "But yeah nah, maybe I could help you out. Let me take a look through my books, I'll see what I can come up with."
                    "And she began rifling through the stack of books lying randomly around the floor."
                if godfather == "Red":
                    pov "I'm hoping you can help me with a problem. My Godfather is the Devil, and He has sworn to take me away at midnight tonight."
                    w "Oh no!"
                    w "Well, I..."
                    w "To be honest I do know a bit about your red friend, I have had some uh, {i}dealings{/i} with Him, I guess you could say. It wasn't my choice though, I don't want you to think I'm one of those wild women of the woods who dance around naked and worship the devil and all that kind of thing, know what I mean? I admire them but I tried it once or twice and it gets really chilly, not recommended."
                    w "But yeah, nah, maybe I could help you out. Let me take a look through my books, I'll see what I can come up with."
                    "And she began rifling through the stack of books lying randomly around the floor."
                if godfather == "Black":
                    pov "I'm hoping you can help me with a problem. My Godfather is Death, and She has sworn to take me away."
                    w "That's wild."
                    w "I mean, I'm a witch, yeah, but I'm not exactly all powerful over here, I'm not sure what you want me to do about that?"
                    w "But yeah nah, maybe I could help you out with that problem. Let me take a look through my books, I'll see what I can come up with."
                    "And she began rifling through the stack of books lying randomly around the floor."
                $witchGodfather = True
                if not witchFestival:
                    jump witchConvo1
            "If you asked her about the festival, turn to page 282." if not witchFestival:
                pov "I came to ask why you didn't come to the festival tonight. Everyone's a bit worried."
                w "The what?"
                if witchTea:
                    "She looked at you with unfocused eyes, then sat bolt upright in her chair."
                else:
                    "She looked at you with unfocused eyes, then jerked bolt upright."
                w "That was TONIGHT?"
                if witchTea:
                    "She collapsed in the chair in despair, and you saw tears of frustration in her eyes."
                else:
                    "She fell back in despair, and you saw tears of frustration in her eyes."
                w "Not again. I really wanted to go this year. I don't know what happened, I swear I..."
                "She rustled through her notes."
                w "Where is it... Where is it..."
                w "Aha!"
                "She darted under the table and came out with a sticky note saying {b}{i}\"FESTIVAL!!!!!!\"{/b}{/i} underlined three times."
                w "It must have fallen out. Oh my God, I'm so sorry. It's just-"
                "She waved helplessly at the blue smoke leaking out of her hat and pooling under the cottage roof."
                w "It all leaks out. I can't keep it in."
                $witchFestival = True
                if not witchGodfather:
                    jump witchConvo1
            "If you complimented her home, turn to page 263." if not witchPlace:
                $witchPlace = True
                pov "The place is really lovely."
                w "What place?"
                "She looked around blearily."
                w "Oh! Yeah. Yeah, I guess."
                w "It's kind of a hole, to be honest."
                w "It's really gotten away from me, like, I kind of like the wild look, and I really love all the herbs and things growing along the outside, it adds a lot to the {i}mystique{/i} I guess, but realistically it looks that way because I literally can't get it under control, I try pretty hard but it always seems to just slip away from me, it's like... trying to hold on to fog or something, you know what I mean, right?"
                w "But yeah, it's nice."
                jump witchConvo1
    "At that moment, the door smashed open and the toad burst in."
    "He was shrieking a wild war cry, waving a sword cane, and clearly terrified out of his mind."
    "The witch yelped and ducked back as he jabbed at her."
    f "Let my friend go, you wicked Curse-gobbler!"
    "The witch grabbed a crooked dagger, still gleaming with {color=#f00}wolf{/color}sbane from her potion work earlier, and parried his thrust."
    w "Do I know you?!"
    "They began to fight back and forth, crashing around the tiny cottage, and as they did the bookshelves rocked and the chairs went clattering away and the potions began to fall from the walls, breaking open in great bursts of magical smoke and light."
    "Green and blue and black and ultraviolet liquid and smoke burst out all around you."
    w "My house!"
    "The chairs were enveloped by smoke and turned into a pair of chickens, then mulberry bushes, then a pile of prunes that went clattering across the kitchen."
    "The table warped, went soggy, and splashed across the floor as a cold, swirling purple liquid."
    "The kitchen and the walls started to twist and turn and sprout with life, and all the books and furniture turned into bats and cats and chittering cicadas that ran and scratched and flew all through the house."
    "The fire in the kitchen flared up wildly and began to spew flowers in all directions."
    #TK: Flowers
    show hand onlayer transient:
        yalign 0.72#0.743
        xalign 0.5
    menu:
        "Brilliant orchids and bromeliads and corpse flowers burst out all around the witch and the toad as they fought their way back and forth through the haze."
        "If you helped the witch, turn to page 281.":
            jump witchFinale
        "If you helped the toad, turn to page 203.":
            jump toadFinale

# Act 3 Finale: The Witch.

label witchFinale:
    "You dived at the witch and pushed her out of the way of the stabbing sword cane."
    "You both went tumbling across the floor and into the fire. When you fell into the fireplace, you fell straight through the flames and down to Hell."
    #Some kind of transition here with SFX
    "Hell was dark and sooty, and the Devil was not home."
    w "Not again!"
    pov "...What do you mean, not again?"
    "The witch sighed as you both picked yourself up from the floor, battered and bruised."
    show hand onlayer transient:
        yalign 0.72#0.743
        xalign 0.5
    menu:
        w "The truth is, I have worked for the devil all this time, and wrought his wicked works upon the world - though it pleased me none to do so."
        "If you asked the witch to tell her tale, turn to page 215.":
            w "Well, ok. I guess we don't have anything better to do."
            "You both sat down on a lump of brimstone together, and she began to tell you her tale."
            #"THE GIRL WHO KNEW EVERYTHING."
            #TK: Probably too many mentions of sapphires and emeralds in this game
            w "Once, I was the princess of a vast kingdom very far from here, where we ruled over sapphire seas and emerald skies."
            w "From a young age I had a terrible hunger for knowledge, and soon I had devoured every book in the kingdom."
            w "Librarians everywhere grew to fear me, and they called me The Girl Who Knew Everything."
            w "Soon the Devil Himself learned of my wisdom and pride, and grew jealous."
            w "\"I'll teach her a thing or two,\" he said, and whipped himself to my kingdom on the spot."
            mir "Oh Princess! I have need of your wisdom!"
            mir "If you are able to answer 3 riddles of mine, I will grant you a boon. But if you cannot answer, you must come serve me in hell."
            w "\"I accept!\" I said, because there wasn't a single riddle in the world I had not eaten whole."
            mir "Poke your fingers in my eyes and I will open wide my jaws. Linen cloth, quills, or paper, my greedy lust devours them all. What am I?"
            #TK: Look at a way to have the input screen appear when the answer is above it.
            python:
                answer1 = renpy.input("{i}Answer thee my riddles three:{/i}", length=8)

            if answer1 == "Scissors" or answer1 == "scissors" or answer1 == "Scissor" or answer1 == "scissor" or answer1 == "Shears" or answer1 == "shears" or answer1 == "Shear" or answer1 == "shear" or answer1 == "Clippers" or answer1 == "clippers" or answer1 == "Clipper" or answer1 == "clipper" or answer1 == "Cutters" or answer1 == "cutters" or answer1 == "Cutter" or answer1 == "cutter":
                mir "Arrrgh... that's right."
                w "The Devil ground his teeth and stomped his feet and fled from the tower."
                w "He spent all night and all day thinking of a riddle to vex me, and on the 2nd night he came to my tower again, rubbing his long fingers together."
                jump riddle2
            else:
                jump devilWins

            label riddle2:
                mir "I have need of your wisdom again, O Princess."
                mir "You make me, but I hold you in my grasp. I terrify without limit, but disappear before dawn. What am I?"
                python:
                    answer2 = renpy.input("{i}Answer thee my riddles three:{/i}", length=9)

                if answer2 == "Nightmare" or answer2 == "nightmare" or answer2 == "Nightmares" or answer2 == "nightmares" or answer2 == "Bad Dream" or answer2 == "Bad dream" or answer2 == "bad dream" or answer2 == "bad Dream" or answer2 == "Dream" or answer2 == "dream" or answer2 == "night terror" or answer2 == "Night Terror" or answer2 == "Night terror" or "night Terror":
                    mir "Correct again!"
                    w "The Devil tore off his hat and threw it upon the ground and stomped on it, and tore at his clothes with anger, and fled from the tower again."
                    mir "This girl is too clever by half. But I have just the thing that'll show her."
                    w "That night as I slept he crawled into my bedroom through the chimney, and dropped the seed of a rose bush in my ear."
                    w "The seed quickly grew and grew inside my skull, until it cracked my head clean open."
                    w "As I awoke I saw there were roses in my ears and cracks in my crown. But worse still, my thoughts began to leak out of my head in dark heavy smoke."
                    w "My servants came to me and I could not say their names."
                    w "I looked at the clothes in the dresser, and I could not say which ones were mine."
                    w "I walked down through the tower, and where before I could have named each leaf and bush and plant, I could not for the life of me remember them now."
                    w "And all the while the dark smoke slowly leaked out of my head, no matter how I tried to stop it."
                    w "And so on the third night the Devil came again with a triumphant smile, and asked his third and final riddle."
                    jump riddle3
                else:
                    jump devilWins

            label riddle3:
                mir "What gets broken when it's not kept?"
                #TK: Have a weird text effect when you type in here
                python:
                    answer3 =  renpy.input("{i}Answer thee my riddles three:{/i}", length=10)
                w "I felt the answer, right there. I sweated and strained to remember it."
                w "But no matter how I tried to hold it, the truth slipped from my hands."
                w "\"I... do not know,\" I said."
                mir "A promise!"
                w "And the Devil cried out with glee, and he seized me at once and leapt into the fireplace and dragged me straight to hell."
                w "And so it was that I came to serve the Devil for the rest of my days."
                "You shook your head and wept to hear such a sorry tale, and all around you the tears hit the floor and turned into terrible shrieking imps that swarmed around the both of you, poking your soft legs and cackling cruelly at your misfortune."
                "Such is life in Hell."
                #TK: Possibly put in a full coversation with the Witch here
                w "Well. Sitting here crying won't help us."
                jump hell
        "If you continued forth into Hell, turn to page 216.":
            w "You're right. Sitting around here telling stories won't help us."
            jump hell

    label devilWins:
        mir "Wrong!"
        w "The Devil cried out with glee, and he seized me at once and leapt into the fireplace and dragged me straight to hell."
        w "To punish me for my hubris, he dropped the seed of a rose bush in my ear as I slept that night in hell."
        w "The seed quickly grew and grew inside my skull, until it cracked my head clean open."
        w "As I awoke I saw there were roses in my ears and cracks in my crown. My thoughts began to leak out through the cracks in dark heavy smoke."
        w "He showed me pictures of the people who love me, and I could not say their names."
        w "I walked through the hills, and where before I could have named each leaf and bush and plant, I could not for the life of me remember them now."
        w "And all the while the dark smoke slowly leaked out of my head, no matter how I tried to stop it."
        w "And so it was I was forced to swear service to him, and I came to serve the Devil for the rest of my days."
        "You shook your head and wept to hear such a sorry tale, and all around you the tears hit the floor and turned into terrible shrieking imps that swarmed around the both of you, poking your soft legs and cackling cruelly at your misfortune."
        "Such is life in Hell."
        #TK: Possibly put in a full coversation with the Witch here
        w "Well. Sitting here crying won't help us. No offence."
        jump hell

    #TK: Exploration scene where you can click around, adventure style
    label hell:
        show hand onlayer transient:
            yalign 0.69#0.743
            xalign 0.5
        menu:
            w "We'd better get moving. I want to get back and see if my cottage is still standing."
            "If you investigated the cavern wall, turn to page 205.":
                "Hell was a small cave, drafty and full of coal dust."
                "You looked through a hole in the cave wall and marvelled to see the imps cavorting in drunken song and dance beyond, each of them plotting to destroy the works of man and G-d."
                "You quickly retreated for fear of being seen."
                jump hell
            "If you investigated the center of the cavern, turn to page 206.":
                "In the center of the cavern was a small, homely cottage. You peered in the window."
                "The Devil was not home. But in a rocking chair in the corner you saw his old grandmother. She spotted you both at once."
    dg "Oh, my dears! You must be terribly lost. You'd better get out of here."
    w "We don't know how - and I'm sworn to serve the devil for the rest of my days."
    dg "Then you have a hard road ahead. My grandson will be home soon, and he will eat you up whole if he sees you."
    dg "But since I feel sorry for you, I'll see if I can help."
    "With a flick of her wrist she transformed you both into fat yellow and black carpenter bees."
    w "Oh, wow!"
    "The witch buzzed around joyously."
    w "This might seem strange but, I've always kind of wanted to be a bee."
    pov "We still have some questions."
    dg "Here. Hide in my skirts, and I will see what answers I can coax from the Devil."
    "She quickly tucked you both into her skirts."
    "Soon, the Devil came home, and no sooner did he enter the house than he noticed the air was not pure."
    mir "Crinkle, crush, wailing and fleeing. I smell the flesh of a human being."
    "And he picked up the whole house and began to turn it over looking for the flesh he smelled."
    if godfather == "Red":
        "You shook to see your Godfather in the flesh at last."
    dg "Hush, you young fool. You're always smelling human beings."
    dg "You're making a mess of the nice clean floors I just swept. Now come have some of the soup I made you."
    "Grumbling, he put the house back down on its foundations and sat down to eat and drink. Soon he was curled up fast asleep and snoring on his grandmother\'s lap."

    label devilGrandmaquestions:
        #TK: Add questions about how to defeat the false hydra
        show hand onlayer transient:
            yalign 0.621#0.743
            xalign 0.5
        menu:
            dg "Quick now, you two. What questions do you have?"
            "If you asked how to free the witch, turn to page 240." if not witchFree:
                $dgAsked += 1
                $witchFree = True
                call devilAnswers from _call_devilAnswers
                dg "I dreamed that there was a young princess who knew everything. But she was tricked, and forced to pledge her soul to you. Do you think she can ever escape?"
                mir "Ha! If only she knew!"
                mir "Underneath this house is a fat old worm that holds her promise to me. If she kills it, she will be free. But that will never happen!"
                jump devilSleeps
            "If you asked how to free yourself, turn to page 247." if not escapeGodfather and godfather == "Red":
                $dgAsked += 1
                $escapeGodfather = True
                call devilAnswers from _call_devilAnswers_1
                dg "I dreamed that a desperate mother once pledged her child to you, as the Godfather - and that you are bound to grab [him] up at midnight tonight. Can [he] evade you, do you think?"
                mir "Not on your life! None can escape the Devil!"
                "He chuckled to himself gleefully."
                show hand onlayer transient:
                    yalign 0.76#0.743
                    xalign 0.5
                if he == "they":
                    mir "Unless of course, [he] look me in the face and recite my second secret name, Belthuselah. But that will never happen!.{vspace=190}{i}In your notes, write down that you {b}know the Devil's second and most secret name.{/b}{/i}"
                else:
                    mir "Unless of course, [he] looks me in the face and recites my second secret name, Belthuselah. But that will never happen!{vspace=190}{i}In your notes, write down that you {b}know the Devil's second and most secret name.{/b}{/i}"
                jump devilSleeps
            "If you asked how to free yourself, turn to page 247." if not escapeGodfather and godfather == "White":
                $dgAsked += 1
                call devilAnswers from _call_devilAnswers_2
                $escapeGodfather = True
                dg "I dreamed that a desperate young mother once pledged her child to God, as the Godfather - and that their child was bound to be taken by Him on [his] 18th birthday. Can [he] ever escape, do you think?"
                mir "Ha! That's easy."
                if he == "they":
                    mir "The Lord is blind to the desperate. All [he] have to do is take on the disguise of an old leper, and God will walk right by."
                else:
                    mir "The Lord is blind to the desperate. All [he] has to do is take on the disguise of an old leper, and God will walk right by."
                mir "But [he]'ll never do that!"
                jump devilSleeps
            "If you asked how to free yourself, turn to page 247." if not escapeGodfather and godfather == "Black":
                $dgAsked += 1
                $escapeGodfather = True
                call devilAnswers from _call_devilAnswers_3
                dg "I dreamed that a desperate young mother once pledged her child to Death, as the Godmother - and that the child was bound to be taken by Her. Can [he] ever escape, do you think?"
                mir "Never."
                "The Devil grew somber."
                mir "There is no trick or cheat. When the child recieves Death's three messengers, [he] will have to go. And that will be that."
                jump devilSleeps
            #"How can we escape hell?" if not escapeHell:
            #    $dgAsked += 1
                #$escapeHell = True
            #    call devilAnswers
            #    dg "I dreamed that a pair of lost souls fell into a fireplace and straight down to hell. Do you think they'll ever go free?"
            #    d "Ha! If only those fools knew!"
            #    d "All you have to do to leave is tug on your heels, shout my third secret name (Eziviorn), and fall backwards into the fire."
            #    d "But they'll never do that."
            #    jump devilSleeps

            "If you asked how to cure the witch's forgetfulness, turn to page 267." if not cureWitch:
                $dgAsked += 1
                $cureWitch = True
                call devilAnswers from _call_devilAnswers_4
                dg "I dreamed of a girl who had all her thoughts drift out of her head as heavy smoke. Do you think she could ever be cured?"
                mir "Ha! The fool! She can never be cured, and she will never know peace."
                mir "The only way she could help herself is to plant a garden in her hat, so that the flowers and herbs soak up the smoke and grow with her memories. Thus she will hold the barest part of her old knowledge."
                mir "But she'll never figure that out!"
                jump devilSleeps
            #"How can I gain eternal life?":
                #dg "I will ask the Devil. What else?"
            "If you asked how to become rich, turn to page 279." if not villageRich:
                $dgAsked += 1
                $villageRich = True
                call devilAnswers from _call_devilAnswers_5
                dg "I dreamed of a poor and penniless village. Do you think they could ever claw their way out of poverty?"
                mir "Never, the pack of wretches! The gutter has a long and hungry groove, and it will not be satiated until they are pulled down into the mud like their forefathers before them!"
                "He cackled in triumph."
                mir "Of course, there is one thing. Beneath the village well is an old mouse. If they bring it grapes, the well will flow with the most delicious wine forever after, and they will all live in luxury for the rest of their days."
                mir "But they'll all go to their graves never knowing a thing about that."
                jump devilSleeps

            #"How can I see that the Master Thief is brought to justice?":
            #    dg "I will ask the Devil. What else?"
            #"Where is the Toad now?":
            #    dg "I will ask the Devil. What else?"
            "If you asked why you felt strange and hollow sometimes, turn to page 283." if not hollowFeeling:
                $dgAsked += 1
                $hollowFeeling = True
                call devilAnswers from _call_devilAnswers_6
                dg "I dreamed of a child who looked out at the woods late at night and felt hollow. Why do you think that could be?"
                "At this the Devil fell silent for a long time."
                mir "{color=#f00}Something{/color} lies under that child's house."
                mir "What it is, I do not know."
                mir "And if I knew, I wouldn't speak of it."
                mir "Do not concern yourself with this dream. Soon, you will forget it."
                mir "As will I."
                jump devilSleeps
            #"What is the Snake my mother warned me about?":
                #dg "I will ask the Devil. What else?"
    label devilAnswers:
        if dgAsked == 1:
            "In a flash, she seized one of the 3 golden hairs on his head and yanked it out. The Devil came awake with a howl of pain."
            mir "Ouch! What are you doing?"
            dg "I'm sorry, my grandson. I had a bad dream, and gripped hold of your hair."
            "The Devil was curious despite himself."
            mir "What did you dream?"
        elif dgAsked == 2:
            "Then she tore out a second hair."
            mir "Hey! What are you doing?"
            dg "I didn't mean it. I did it in a dream."
            mir "What did you dream this time?"
        elif dgAsked == 3:
            "Then she grabbed hold of the third golden hair and yanked it out by the roots."
            mir "My last hair!"
            "The Devil lept up and stomped around the house, shouting vile curses, but she soon calmed him."
            dg "I'm sorry, my grandson. But what can you do against dreams?"
            mir "Hmph."
            mir "What was the dream this time?"
        return
    label devilSleeps:
        if dgAsked == 1:
            "The grandmother began picking the lice from His head, and soon he fell asleep again and snored so loudly that the windows rattled."
            dg "Ask your second question, child."
            jump devilGrandmaquestions
        elif dgAsked == 2:
            "The grandmother spoke softly to him and began lousing him again. Soon he settled down and was fast asleep once more."
            dg "Ask your final question, child."
            jump devilGrandmaquestions
        elif dgAsked == 3:
            "The Grandmother sang a sweet lullaby to calm him."
            jump witchEnd
    label witchEnd:
        "Soon the old dragon fell soundly asleep, and His grandmother took him off to bed and closed the door."
        "She shook you out of her skirts and turned you back to your human forms."
        dg "Well! I'm sure you heard the answers to your questions. Here are the Devil's three golden hairs."
        dg "Throw them into the fire, and you will be carried straight up the chimney and out of hell."
        w "Thank you so much. How can we ever repay you?"
        dg "No need. Just forgive my grandson his trifling ways. He is young and foolish, just as I once was."
        #Answers to all your questions.
        #"NOTE: You get answers to all your questions and then see scenes where you use all the answers."
        if witchFree == True:
            "You left the cottage and crawled down into the foundations beneath it. When you found the old worm squatting beneath it, the witch speared it with her crooked finger, killing it instantly."
            "With that, she felt a great weight fall from her shoulders. You turned and saw that the Devil's mark was no longer on her."
            "Then you went to the cottage fireplace, threw in the three golden hairs from the Devil, and lept inside."
            "In an instant, you flew right up the chimney and out into the witch's cottage."
        else:
            "And so you went to the cottage fireplace, threw in the three golden hairs from the Devil, and lept inside."
            "In an instant, you flew right up the chimney and out into the witch's cottage."
        if godfather == "Red":
            "Alas, as you tumbled onto the floor of the cottage, you heard the clock strike midnight, and you saw a pair of terrible red boots ahead of you."
            mir "Time's up, child!"
            mir "Now you are mine, just as your mother promised all those years ago."
            mir "I'll keep you in a cave to darn my socks, and brew my grandmother's tea, and bake bread for all the hungry souls of hell - and there's nothing you can do about it!"
            menu:
                "Check your notes. If you {b}know the Devil's second and most secret name{/b}, turn to page 294.":
                    pov "Belthuselah."
                    mir "NOOOOOOOOOOOO! How? How did you discover my second and most secret name? Impossible!"
                    "In an instant, his spell over you broke. The Devil withered and shrank and spluttered with rage, until he grew as small as an ant, whereupon you kicked Him right into the fireplace and back to hell."
                    "With the Devil taken care of, you and the witch looked over the cottage."
                    "It was a mess of flowers and plants and flopping animals, sprouting wildly every witch-way across the room."
                    "You rolled up your sleeves and slowly put the room to rights, until it was even more clean, warm and homely than it had been before."
                "Otherwise, turn to page 297.":
                    "With a whoop, the Devil seized you and dragged you into the fireplace and straight to hell."
                    "Sadly, you were trapped there forever after. The witch mourns you still."
                    #"What of the toad, you ask? I ate him up whole."
                    call endStamp
                    "When misfortune is after someone, they may try to hide in all sorts of places or flee across the whole wide world, but it will still know where to find them."
                    jump end
        elif godfather == "White":
            w "Quick! Your Godfather will be here any minute."
            "You both lept into action. You disguised yourselves as beggars and lepers, and through great lumps of mud all over the half-ruined cottage so that it looked like an abandoned hovel."
            "Soon, the clock struck midnight, and you felt the light of God upon you."
            "It seared into your flesh as you huddled together on the floor, feeling His gaze searching for you as His heavy footfalls shook the house."
            "But He did not see you. And soon, you felt His light fade, and His gaze turned away, and His heavy footsteps fell away into the distance."
            "You and the witch clutched each other and laughed with terror and relief."
            "With God taken care of, you and the witch looked over the cottage."
            "It was a mess of flowers and plants and flopping animals, sprouting wildly every witch-way across the room."
            "You rolled up your sleeves and slowly put the room to rights, until it was even more clean, warm and homely than it had been before."
        elif godfather == "Black":
            "You slowly picked yourselves up and looked over the cottage."
            "It was a mess of flowers and plants and flopping animals, sprouting wildly every witch-way across the room."
            "Just then, the clock struck midnight. You looked around in terror, waiting for Lady Death or Her messengers. But none came."
            w "Looks like you still have some time left!"
            "You rolled up your sleeves and slowly put the room to rights, until it was even more clean, warm and homely than it had been before."
        if villageRich == True:
            "Once the cottage was put to rights, you went to the village and fed some grapes to the mouse at the bottom of the village well."
            "In an instant, the well began to flow with the richest and most satisfying red wine, and all throughout the village rejoiced."
            "The village soon prospered by selling the wine, and you and your family became rich beyond your wildest dreams."
        if cureWitch == True:
            "You stayed with the witch for a while after that, helping her with her forgetfulness."
            "Over time you cultivated a garden in her hat, using the knowledge you tricked out of the Devil."
            if godfather != "Black" and mushroomCurse == False:
                "You told the wise old Mushroom the story of your misadventures in hell, and she loved it so much that she blessed you with a mushroom's blessing, so that you always had a green thumb."
            "You sowed green grass and lavender and rosemary and thyme, and bottlebrushes and honeysuckle and silver spurflowers."
            "The smoke pooled under her hat and nourished these flowers at the roots, so they grew rich and wild with her memories."
            "Although she would never be the Girl Who Knew Everything again, she knew enough."
            if witchFree == False:
                "Alas, despite everything you'd done, she still remained sworn to the Devil. Her promise to him was kept in a secret place that he guarded jealously, and you were never able to find it."
                "Every witch's sabbath, she was forced to ride away to dance on the peak of Bald Mountain, and commit all kinds of wicked and terrible acts in his name."
                "Still, you spent many peaceful months staying with her, cultivating her garden, putting her cottage to rights, and helping her rewrite all her old notebooks again."
            else:
                "You spent many peaceful months staying with her, cultivating her garden, putting her cottage to rights, and helping her rewrite all her old notebooks again."
        else:
            "You stayed with the witch for a while after that, trying to help her with her forgetfulness."
            "Sadly, you knew not how. She would never be the Girl Who Knew Everything again. You tried everything you could, but for the rest of her days, her thoughts were cursed to leak from her head in heavy smoke."
            if witchFree == False:
                "Alas, despite everything you'd done, she still remained sworn to the Devil. Her promise to him was kept in a secret place that he guarded jealously, and you were never able to find it."
                "Every witch's sabbath, she was forced to ride away to dance on the peak of Bald Mountain, and commit all kinds of wicked and terrible acts in his name."
            "Still, you spent many peaceful months staying with her, cultivating her garden, putting her cottage to rights, and helping her rewrite all her old notebooks again."
        show hand onlayer transient:
            yalign 0.72#0.743
            xalign 0.5
        menu:
            "Finally, you'd done as much as you could to help. She had recovered enough to take care of herself again."
            "If you stayed with the Witch, turn to page 291.":
                "But you found you didn\'t want to leave after all."
                "You stayed there in the cottage, and tended to the herbs and wildflowers, and helped her gather ingredients for her potions."
                "And she created salves and poultices for you and your family, keeping her in good health into her old age."
                if godfather == "Black":
                    "You lived there in quiet happiness for many years."
                    "But youth does not last forever."
                    "One day, you felt yourself wracked with a terrible fever."
                    "Then, you felt gout take hold of you and make all your limbs twitch, and you were wracked with one illness after another, and you fell into deep sleep for long days."
                    "Not even the witch could help you, though she toiled at your bedside for many long hours."
                    w "I'm sorry. I-I wish I could do more... I should be able to heal this."
                    pov "Don't worry. I won't die until Death sends Her messengers."
                    "But as you spoke, there was a knock on the door, and the Witch hesistantly opened it to reveal the wise mushroom from the forest."
                    if mushroomCurse:
                        m "I suppose my curse won't be needed after all."
                    m "It is time. Come with me."
                    jump deathQuestions
                    label deathQuestions:
                        show hand onlayer transient:
                            yalign 0.67
                            xalign 0.5
                        menu:
                            m "The Pale Lady is waiting for you."
                            "If you tried to object, turn to page 245." if not deathMessengers:
                                pov "But - is She going to break Her promise? She said She'd send three messengers."
                                m "Didn't the fever rage at you? Didn't the gout take hold of you and shake you to pieces?"
                                m "She even sent Her sister, Sleep, to remind you of Her."
                                m "She has sent all Her messengers. Now you must come down to Her kingdom."
                                $deathMessengers = True
                                jump deathQuestions
                            "If you turned to say goodbye to the witch, turn to page 255." if not deathGoodbye:
                                $deathGoodbye = True
                                m "Of course."
                                show hand onlayer transient:
                                    yalign 0.72
                                    xalign 0.5
                                menu:
                                    "You turned to the Witch. She was crying, and where her tears fell they blossomed into twisting purple plants with long thorns."
                                    "If you told her you loved her, turn to page 276.":
                                        w "I love you too."
                                        "You embraced, and her tears fell upon you and twisted your cheeks into sprouting flowers."
                                        w "I-I'm sorry. I should have done more. Maybe if I'd checked in one of those older journals again, the one by fieldstien, I know I had a read of it before but I could have given it another try and looked for -"
                                        pov "You did everything you could. You have nothing to be sorry about."
                                        "And you gripped her tight."
                                        jump deathQuestions
                                    "If you told her you loved her platonically, turn to page 278.":
                                        pov "Goodbye, my dear friend. I love you, so much."
                                        w "G-goodbye. I love you too."
                                        "You embraced, and her tears fell upon you and twisted your cheeks into sprouting flowers."
                                        w "I-I'm sorry. I should have done more. Maybe if I'd checked in one of those older journals again, the one by fieldstien, I know I had a read of it before but I could have given it another try and looked for -"
                                        pov "You did everything you could. You have nothing to be sorry about."
                                        "And you gripped her tight."
                                        jump deathQuestions
                            "If you accepted your fate, turn to page 278.":
                                pov "I'm ready."
                                m "No-one's ever ready. But there's no time left."
                                "She gently took you down to the kingdom of Death."
                                call endStamp
                                "And what happened after that, none who live can say."
                                #"And what happened to the toad, you ask?"
                                #"He was never heard from again."
                                jump end
                else:
                    call endStamp
                    "And so you lived there together in quiet happiness. If you have not died, you live there still."
                    #"And what happened to the toad, you ask?"
                    #"He was never heard from again."
                    jump end
            "If you returned home, turn to page 261.":
                "When it was time to leave, you wished the Witch a tearful farewell, and returned to your cottage with your family."
                "You lived there in quiet happiness for many years."
                "But youth does not last forever."
                "One day, you felt yourself wracked with a terrible fever."
                "Then, you felt gout take hold of you and make all your limbs twitch, and you were wracked with one illness after another, and you fell into deep sleep for long days."
                "Not even the witch could help you, though she toiled at your bedside for many long hours."
                w "I'm sorry. I-I wish I could do more... I should be able to heal this."
                pov "Don't worry. I won't die until Death sends Her messengers."
                "But as you spoke, there was a knock on the door, and the Witch hesistantly opened it to reveal the wise mushroom from the forest."
                if mushroomCurse:
                    m "I suppose my curse won't be needed after all."
                m "It is time. Come with me."

                if godfather == "Black":
                    jump deathQuestions
                else:
                    call endStamp
                    "And so you lived there for many long, happy years, visiting the Witch each summer. If you have not died, you live there still."
                    #"And what happened to the toad, you ask?"
                    #"He was never heard from again."
                    jump end
# Act 3 Finale: The Toad.

label toadFinale:
    "You lept to defend the toad, diving and pushing him away from the slashes of the crooked dagger."
    "As you pulled him away, a black vial of liquid smashed over the two of you and you were both instantly turned into worms."
    "The cottage wall gave way and you were both washed out of the house in a multicoloured wave of potions."
    "The world flipped upside down as you fell through the silver puddle outside, and you found yourself caught up in a a torrent of writhing fish and magpies and bats and crocodiles being washed down the rainforest river, all transforming into new animals every second."
    "You popped into a cat, then a fish, then back into a worm again."
    f "Watch out!"
    "A greedy magpie dove for you as you squirmed helplessly."
    "The toad transformed into a gecko and grabbed you, dropping his tail."
    "The magpie grabbed the tail and flew off, before turning into a wallaby and falling back in the river."
    f "Hold on! I know where to go!"
    "You felt yourself transform into a squirming tadpole. The toad changed into a sea bass and held you in his mouth, swimming for a point on the shore."
    "Just as his fins began to give out, you turned into a cat, and grabbed him and pulled you both up out of the water."
    "He directed you to a small, muddy hole on the river bank. As soon as you entered, the mud fell down behind you and blocked your exit."
    "The hole was wet, and cramped, and crawling with small worms and roaches, but it was safe."
    "You shivered in the cold. The toad flopped down beside you, becoming a witchetty grub."
    #You explore the toad's home and get to know him better
    label toadExplore1:
        show hand onlayer transient:
            yalign 0.65#0.743
            xalign 0.5
        menu:
            f "Well. This is another fine mess I've made."
            "If you explored the nearby area, turn to page 208." if not toadCave:
                $toadCave = True
                "You uncovered a rug and a fireplace in the muck, and lit the fire."
                "The toad uncovered a pantry with a single, mouldy piece of bread and toasted it over the fire for the both of you."
                f "This all the food I have, sorry."
                jump toadExplore1
            "If you explored deeper in, turn to page 209." if not toadBasement:
                $toadBasement = True
                "You travelled down a hole in the back of the cave which lead down into the mud."
                "Down the hole was a small room with a bed and a cupboard."
                "The toad opened the cupboard and took out two threadbare costumes: a witch and a unicorn. You pulled them around you for warmth."
                f "I... used to like to dress up in this stuff. I'd put on little plays and things for myself."
                f "Pretty dumb, I know. Kid's stuff. Haven't done it in years."
                "But the costumes seemed well cared for."
                jump toadExplore1
            #TK: Toad admits that there was no curse.
            "If you asked the toad about this place, turn to page 216." if not toadWhere:
                $toadWhere = True
                pov "Where are we?"
                f "This is my home. My real home."
                f "That's right. The grand fortune? The prestigious inheritance? The manor on the hill? All lies."
                f "I've lived in this hole near the witch's cottage since I was a tadpole."
                f "Yes, I know it might be hard to believe with my noble bearing. But it's all true."
                jump toadExplore1
            "If you looked for a way out, turn to page 218.":
                pov "How are we going to get out of here?"
                f "Don\'t worry. I'm sure {b}{i}he{/i}{/b} will rescue us soon."
                pov "{i}He?{/i}"
                "Suddenly the ceiling burst open and a shining light came upon you, blinding in its glory."
                "Out from the light strode the most beautiful frog you'd ever seen."
                "His skin was glimmering green like the wings of summer beetles, his muscles rippled with strength, his eyes threw out glances of fire, and he was dressed in a gorgeous midnight-blue suit."
                "On each finger gleamed a golden ring inlaid with precious jadestone and chrysoprase and emeralds, and his finely-coiffed hair waved in the breeze with such beauty that none had ever seen the like, not even in a dream."
                mysFrog "Are you quite alright?"
                pov "Who are you?"
                "The toad sighed."
                f "This..."
                #TK: Change to ???
                f "...is Brildebrogue Chippingham."
                bc "The very same!"
                "The frog beamed and helped you to your feet as you transformed into a garden rake."
                bc "Say, that voice is awfully familiar..."
                bc "Is that you, Blort?"
                #TK: Change to blort Bronkum
                f "Yeah. Yeah, that's my real name."
                f "I am Blort Bronkum, and I have never succeeded at anything in my life."
    "The real Brildebrogue Chippingham pulled you out of the hole and into a golden carriage waiting nearby, which whisked you away to a stately riverside manor."
    "With a click of his fingers, Brildebrogue summoned a cavalcade of richly dressed frog manservants, who offered you all the finest delicacies from across the world, such that the king of kings would cry to taste them."
    "With another click, a dozen beautiful frog maids escorted you to golden baths where all the muck and grime was washed away as you were serenaded by the finest frog soprano choir in all the land."
    "Brildebrogue himself regaled you with witty anecdotes of his thrilling adventures, which had everyone rolling around on the floor laughing, except for the toad, who sat in the corner and scowled."
    bc "Please make yourselves at home, my friends!"
    bc "I'm afraid I must leave immediately. Business with the jeweled serpent-kings of the City of Brass, you understand."
    f "Of course. Actually, I recall I was chatting with the jeweled serpent-kings myself just the other day, and -"
    #TK: Interruption effect, like the words jump or shake or something!
    bc "Help yourselves to all the delights of Chippingham Manor! Here are the keys to the whole place. You may go wherever you wish, and open every door!"
    bc "...except one."
    bc "This little golden key will unlock the smallest closet in the tallest tower. Do not open that closet."
    bc "But I'm sure that won't be a problem! I know I can trust you, my dear friends."
    "And with a wave of his hand, he lept into a gleaming gold carriage and sped away across the horizon in an instant."
    #You explore Chippingham Manor
    #TK: Add changes based on whether you entered these rooms.
    f "Hpmh. Show-off."
    label chippinghamManor:
        show hand onlayer transient:
            yalign 0.55#0.743
            xalign 0.5
        #TK: look at setting this particular choice box to 680
        menu:
            blank ""
            "If you explored the first tower, turn to page 256." if not firstTower:
                "Inside the first tower, the two of you discovered a trio of stately frog wizards, who flushed the remaining potions from your systems and restored you to your original forms in a wink."
                $firstTower = True
                jump chippinghamManor
            "If you explored the second tower, turn to page 257." if not secondTower:
                "Inside the second tower, you discovered the finest frog chefs of all the land, who quickly sliced off their own legs and served them to you as the most delicious dish either of you had ever tasted."
                $secondTower = True
                jump chippinghamManor
            "If you explored the third tower, turn to page 258." if not thirdTower:
                "Inside the third tower, you discovered a great harem of finely-dressed courtesans of all genders, who poured rich wines and made witty conversation with you until you were both completely sloshed and dizzy from the refined repartee."
                $thirdTower = True
                jump chippinghamManor
            "If you explored the fourth tower, turn to page 259." if not fourthTower:
                $fourthTower = True
                "Inside the fourth tower was a great fountain of emeralds and sapphires and precious gems, which splashed out over a scale model replica of the forest. You could see immediately that a single gemstone from this fountain was so valuable that it would bankrupt the richest sultan."
                "The toad gazed up in wonder."
                f "I spent my whole life looking up at this place. Hard to believe we're actually here."
                jump chippinghamManor
            "If you explored the fifth tower, turn to page 260." if not fifthTower:
                $fifthTower = True
                "Inside the fifth tower you found a gigantic closet of the finest clothes, rich silks and suits and uniforms of office, all extremely masculine in cut and befitting of a king."
                jump chippinghamManor
            "If you explored the sixth tower, turn to page 262." if not sixthTower:
                $sixthTower = True
                "Inside the sixth tower you found the Library of Alexandria. A small plaque explained that Brildebrogue had miraculously saved the books from the fires and stored them safely here for all this time."
                jump chippinghamManor
            "If you explored the seventh and tallest tower, turn to page page 264." if firstTower:
                #TK: Ominious music.
                "Inside the seventh and tallest tower you found only a tiny wooden closet."
                show hand onlayer transient:
                    yalign 0.68#0.743
                    xalign 0.5
                menu:
                    "A golden keyhole shone out from the closet door."
                    "If you opened the closet, turn to page 275.":
                        "You inserted the key, and slowly opened the door with a long creak."
                        "As soon as the door opened, a stream of blood flowed over you, and you saw seven dead frog brides hanging all along the walls, some only skeletons."
                        jump brildebrogueCloset
                    "If you went back, turn to page 190.":
                        jump chippinghamManor
            #TK: Add route if you want to be good and follow the rules.
            "If you patiently awaited the return of Brildebrogue Chippingham, turn to page 161.":
                f "Well, if you're not going to open this damn closet, I am."
                "He rushed to the seventh and tallest tower, and unlocked the closet with the golden key."
                "He slowly turned the key, and opened the closet door with a long creak."
                "As soon as the door opened, a stream of blood flowed over the two of you, and you saw seven dead frog brides hanging all along the closet walls, some only skeletons."
                jump brildebrogueCloset

    label brildebrogueCloset:
        f "Oh my G-"
        show hand onlayer transient:
            yalign 0.79#0.743
            xalign 0.5
        "You slipped in the blood and felt it on your hair and tasted it in your mouth. The toad quickly slammed the door, but the key popped out and into the blood.{vspace=170}{i}In your notes, write down that you {b}have blood on your hands.{/b}{/i}"
        f "No no no no no. Oh god."
        "The clock chimed a quarter to twelve."
        "You tried to wipe the blood off the key, but it wouldn't come off."
        f "Quickly! We have to wash this off."
        "You both rushed downstairs and tore off your clothes and burned them and put on new, spotless clothes without a hint of blood. But no matter how long you scrubbed at the key, you couldn't get the blood off. When you rubbed it off one side, it appeard on the other."
        bc "Good evening!"
        f "Ack!"
        f "I-I mean hello! Brildebrogue! Back so soon?"
        bc "Yes, the business was wrapped up fairly swiftly after I recovered the megastone from the lost glacier city of Url'Iarch."
        f "Aha, o-of course, yes. Why, that reminds me of the time when I recovered the lost demondecahedron from the -"
        show hand onlayer transient:
            yalign 0.68#0.743
            xalign 0.5
        menu:
            bc "Would you be so kind to hand me back my keys, old sport? I have much business to attend to."
            "If you handed back all the keys, turn to page 123.":
                f "H-here you go... o-old sport..."
                bc "..."
                bc "Interesting."
                bc "How came this blood upon this key?"
                f "I-I am sure I do not know."
                bc "You do not know?"
                bc "But I know well enough."
                bc "If you have such an interest in my closet, you can take your place amoung the ladies there."
                "He took out his simitar and locked the door to his manor behind him."
                f "RUN!"
                jump brildebrogueFinale
            "If you pretended you lost the bloody golden key, turn to page 125.":
                f "L-looks like we must have misplaced it, sorry... o-old sport..."
                bc "..."
                bc "Interesting."
                bc "Where is it?"
                f "I-I am sure I do not know."
                bc "You do not know?"
                bc "But I know well enough."
                "In one motion he twisted the toad's arm behind his back. The toad gasped and dropped the bloody key on the floor."
                bc "If you have such an interest in my closet, you can take your place amoung the ladies there."
                "He took out his simitar and locked the door to his manor behind him."
                f "RUN!"
                jump brildebrogueFinale
    label brildebrogueFinale:
        #Number of escape attempts before you escape
        define escapesAllowed = 4
        if escapeB == 0:
            "You ran into the twisting castle corridors together, but Brildebrogue Chippingham was fast behind you, smiling a charming smile."
        if escapeB == 1:
            "You both raced up and down endless staircases, hearing Brildebrogue's pleasant, resonant voice behind you."
            bc "Just stand aside, Blort. I've no interest in you."
            bc "Honour amoung toads, and all that."
        if escapeB == 2:
            "Warm, resonant laughter echoed behind you as you stumbled across the manor's battlements."
        if escapeB == 3:
            "You pulled the exhausted toad up ladders and down wells. Brildebrogue wasn't even tired. He strolled after you at a leisurely pace."
        if escapeB == 4:
            "As you ran up the manor staircases, you saw an old clock on the wall. It was almost midnight. The moon loomed large above you."
        if escapeB == 5:
            "You smelt Brildebrogue's intoxicating cologne all around you as you dragged the toad over the crooked manor roof. His sweet breath was hot on your neck."
        if escapeB == 6:
            "You were exhausted. You struggled on, putting one stumbling foor after another. You felt Brildebrogue's elegant, manicured hand reaching over your shoulder."
        show hand onlayer transient:
            yalign 0.58#0.743
            xalign 0.5
        menu:
            blank ""
            "If you ran to the first tower, turn to page 284." if not firstTower2:
                $firstTower2 = True
                $escapeB +=1
                #if firstTower == True:
                "You begged for help from the stately trio of frog wizards inside the first tower, but with one look at Brildebrogue, they quickly turned themselves into newts and slithered away into dark holes in the rock, as fast as they could go."
                bc "Are you happy to have regained your true form, Blort? Happy to look into the mirror every morning and see that wretched face?"
                "The toad looked around at the mirrors all around him, and tears came to his eyes."
                "In a single motion, Brildebrogue swept the toad back and sliced the tower in two. You dragged the toad up and fled as it crumbled around you."
                jump brildebrogueFinale
            "If you ran to the second tower, turn to page 285." if not secondTower2:
                $secondTower2 = True
                $escapeB +=1
                #if secondTower == True:
                "You raced to the cavalcade of fine frog chefs inside the second tower. With a click of his fingers, Brildebebrogue commanded them, and they slid out of the room and began preparing the pots and pans and knives to make a delicious meal from your carcasses when the fighting was done."
                bc "Still hungry? Maybe you should lay off for a while. Go for a jog."
                "He thrust an elbow into the toad's paunch, winding him. Then with his other hand he tore down the tower. You fled as it crumbled around you."
                jump brildebrogueFinale
            "If you ran to the third tower, turn to page 286." if not thirdTower2:
                $thirdTower2 = True
                $escapeB +=1
                #if thirdTower == True:
                "You pushed your way through the pack of finely-dressed courtesans inside the third tower. Brildebrogue walked calmly after you as they stroked his thick arms and complimented his physique."
                if escapeB == 0:
                    bc "I know about the long nights you've spent alone, Blort."
                else:
                    bc "I know about the long nights you've spent alone."
                bc "Just hand [him] over, and I can buy you all the friends you want."
                "With a flick of his wrist, Bildebrogue turned the courtesans into a pack of wild squawking galahs which tore down the tower with their great curved beaks. You fled as it crumbled around you."
                jump brildebrogueFinale
            "If you ran to the fourth tower, turn to page 287." if not fourthTower2:
                $fourthTower2 = True
                $escapeB +=1
                #if fourthTower == True:
                "You ran through the glimmering fountain of emeralds and sapphires and precious gemstones in the fourth tower. The toad and Brildebrogue battled back and forth behind you."
                bc "I'm sure I can give you a few of these as a small loan."
                bc "Maybe you can finally make something of yourself."
                "The toad gritted his teeth as glittering gems fell all around him, and he parried Brildebrogue's thrust with an unsteady hand."
                "Brildebrogue shrugged, puffed up his cheeks, and blew down the tower in a single breath. You fled as it crumbled around you."
                jump brildebrogueFinale
            "If you ran to the fifth tower, turn to page 288." if not fifthTower2:
                $fifthTower2 = True
                $escapeB +=1
                #if fifthTower == True:
                "You fled through the racks of fine clothes in the fifth tower as Brildebrogue sliced them apart behind you."
                bc "Trying to steal from my wardrobe?"
                bc "I heard the servants laughing about your little dress-up obsession, Blort. I just never realised it went this far!"
                "With one clap of his hands he brought down water rushing in from the seas. You fled through through the waves as they brought the tower down around you."
                jump brildebrogueFinale
            "If you ran to the sixth tower, turn to page 290." if not sixthTower2:
                $sixthTower2 = True
                $escapeB +=1
                #if sixthTower == True:
                "You and the toad scrabbled through the aisles of books in the sixth tower - but as you turned a corner, Brildebrogue was in front of you, carelessly thumbing through a thick volume."
                bc "\"On Rays of Light.\" Democritus. One of my favourites."
                bc "But then, you never learned to read, did you?"
                f "I... I mean, of course I can..."
                "But his face fell."
                bc "Give [him] over, and I'll teach you."
                bc "Don't worry, it's easy. Even a child could do it."
                "The toad said nothing."
                "Brildebrogue tossed the book down. With a click of his fingers he brought down lightning from the skies, and the whole tower went up in flames. You both fled through the fire as it burned around you."
                jump brildebrogueFinale
            "If you ran to the seventh and tallest tower, turn to page 292." if escapeB >= escapesAllowed:
                "You burst through the door to the tallest tower. In front of you was the small room with the bloody closet, now yawning open wide."
                "There was nowhere left to run. You heard slow footsteps behind you."
                bc "You've heard all my offers, Blort. You know I could give you the life you always wanted."
                "The toad stood between you and Brildebrogue with sword cane drawn, hands shaking."
                bc "You've seen what I've built. I built it with these two hands."
                bc "You have a choice. You can hand [him] over, and become a great man. Or you can stay a wretch, and die, and leave nothing but a stain in the gutter. No-one will remember your sad little stories."
                f "..."
                f "Then I will die as a wretch. But I will die with my friend beside me."
                "The toad brought up his sword cane to clash with the scimitar. And at just that moment, you heard the clock strike twelve."
                if godfather == "Red" or godfather == "White":
                    pov "Godfather! Help me!"
                    jump frogEnding
                else:
                    "Godmother! Help me!"
                    jump frogEnding

    label frogEnding:
        if godfather == "White":
            #God rescues you, brildebrogue is smote
            miw "Be not afraid."
            "A harsh light fell upon the room, and you looked up to see a whirl of wings and feathers and eyes and fire standing before you."
            "Brildebrogue dropped to his knees."
            bc "Lord, please...I have always been your faithful disciple."
            miw "That may be so."
            miw "But none may touch my grandchild and live."
            bc "N-now see here. I am Brildebrogue Chippingham, and I have never failed at anything in my-"
            "But the light fell upon him, and without even a scream, he was burnt up in an instant and gone forever."
            miw "Come with me now, my grandchild. It is time for you to take your rightful place in heaven."
            f "Hold on just a second. How do we know you're really the Lord?"
            miw "Do not doubt my power. I am the wind in the sky and the old stones in the earth."
            f "Show us. Seeing is believing."
            "The Lord performed His feat and turned into a mighty wind. But just as He did so, the toad opened the window, and the Lord blew right out of the tower and across the sea. With this, the toad slammed the window shut."
            f "Well. That takes care of that."

        if godfather == "Red":
            #The devil drags brildebrogue down to hell
            mir "Your time is up!"
            "The Devil Himself exploded out of the floor in a flash of brimstone and soot."
            "As soon as he saw your Godfather, Brildebrogue went white as ash."
            bc "Wait- my contract isn't up yet. You told me I still had six years left."
            mir "That may be so."
            mir "But I never keep a bargain, and no-one messes with my grandchild and lives!"
            bc "N-now see here. I am Brildebrogue Chippingham, and I have never failed at anything in my-"
            "But with one cloven hoof the devil kicked him straight out the window, whereupon he fell screaming down the tower and into his grave and straight to Hell."
            mir "That takes care of that. Now come with me, my grandchild. All the wonders of Hell await!"
            f "Hold on just a second. How do we know you're really the Devil?"
            mir "Ha! You dare doubt my power? I can grow tall as a fir tree and small as a mouse."
            f "Prove it."
            "The Devil performed His feat. But just as He turned into a mouse, the toad grabbed Him and stuffed Him in a sack and threw Him out the window, whereupon He fell screaming down the tower and into His grave and straight to Hell."
            f "Well. That takes care of that."
        if godfather == "Black":
            #Death comes for brildebrogue after all these years
            "As the clock struck midnight, the ground around Brildebrogue Chippingham began to sprout with pale mushrooms (the fingers of Lady Death)."
            bc "No... please! It's not yet my time!"
            bc "N-now see here. I am Brildebrogue Chippingham, and I have never failed at anything in my-"
            "But in an instant the mushrooms grew all around and through him, and he fell to the floor."
            "And so he died, and he has remained dead up to this very day."
            f "Well. That takes care of that."

        "You and the toad left the ruins of Chippingham manor behind to rot."
        "You took the gems from the wreckage and renovated the toad's old mud-hole, turning it into a warm, comfy little cottage with a great fire and enough food for a lifetime, along with a large closet of fine clothes."
        show hand onlayer transient:
            yalign 0.66#0.743
            xalign 0.5
        menu:
            "After a while, you both had rested and mended from your terrible ordeals."
            "If you married the toad, turn to page 298.":
                "But you found you didn't want to leave. You stayed together in your cosy home in the swamp. The toad worked long hours sewing many fine costumes, and the two of you put on plays together which delighted the people of the village."
                "After many years of companionship, you finally got married and lived happily together."
                "I should know - I was at your wedding! I gorged myself on the fresh meat and raised my glass for the toast, and the beer ran down my chin but did not go into my mouth."
                if godfather == "Black":
                    jump toadDeath
                call endStamp
                "You were very happy, had many children, and you still would live if you had not died."
                #"And what happened to the witch, you ask?"
                #"I ate her up whole."
                #"Every piece."
                jump end
            "If you stayed good friends with the toad, turn to page 299.":
                "But you found you didn't want to leave. You stayed together in your cosy home in the swamp."
                "The two of you had many happy years together. The toad worked long hours sewing many fine costumes, and the two of you put on plays together which delighted the people of the village."
                if godfather == "Black":
                    jump toadDeath
                else:
                    call endStamp
                    "You were very happy there for the rest of your days, and you still would live if you had not died."
                #"And what happened to the witch, you ask?"
                #"I ate her up whole."
                #"Every piece."
                jump end
            "If you left the toad to return to your family, turn to page 300.":
                "When it was time to leave, you wished the toad a tearful farewell, and returned to your cottage with your family."
                "You lived there for many long, happy years, visiting the toad now and again as a good friend."
                if godfather == "Black":
                    jump toadDeath
                else:
                    call endStamp
                    "You were very happy there for the rest of your days, and you still would live if you had not died."
                #"And what happened to the witch, you ask?"
                #"I ate her up whole."
                #"Every piece."
                jump end
    label toadDeath:
        "But youth does not last forever."
        "One day, you felt yourself wracked with a terrible fever."
        "Then, you felt gout take hold of you and make all your limbs twitch, and you were wracked with one illness after another, and you fell into deep sleep for long days."
        "Not even the toad could help you, though he toiled at your bedside for many long hours."
        f "I-I'm so sorry, my old friend... I wish I knew more about this kind of thing."
        pov "Don't worry. I won't die until Death sends Her messengers."
        "But as you spoke, there was a knock on the door, and the toad hesistantly opened it to reveal the wise mushroom from the forest."
        if mushroomCurse:
            m "I suppose my curse won't be needed after all."
        m "It is time. Come with me."
        m "Death is waiting for you."
        label deathToadQuestions:
            show hand onlayer transient:
                yalign 0.66#0.743
                xalign 0.5
            menu:
                "If you tried to object, turn to page 245." if not deathMessengers:
                    pov "But - is She going to break her promise? She said She'd send three messengers."
                    m "She has sent all her messengers. "
                    m "Didn't the fever rage at you? Didn't the gout take hold of you and shake you to pieces?"
                    m "She even sent her sister, Sleep, to remind you of Her."
                    m "Now you must come down to Her kingdom."
                    $deathMessengers = True
                    jump deathToadQuestions
                "If you turned to say goodbye, turn to page 255." if not deathGoodbye:
                    $deathGoodbye = True
                    pov "Can I say goodbye first?"
                    m "Of course."
                    "You turned to the toad. He was crying, and where his tears fell they turned into gleaming black geckos that skittered away into the corners of the room."
                    show hand onlayer transient:
                        yalign 0.7#0.743
                        xalign 0.5
                    menu:
                        "If you told him you loved him, turn to page 276.":
                            pov "Goodbye, my dear. I love you, so much."
                            f "I love you too."
                            "You embraced, and his tears fell upon you, and you felt the cool gecko's feet across your cheeks."
                            f "I'm sorry I couldn't be more. You should have chosen someone else. Maybe if you'd-"
                            pov "Shh. I chose you. You have nothing to be sorry about."
                            "And you gripped him tight."
                            jump deathToadQuestions
                        "If you simply told him goodbye, turn to page 278.":
                            pov "Goodbye, my dear friend. I love you, so much."
                            f "Goodbye."
                            "You embraced, and his tears fell upon you, and you felt the cool gecko's feet across your cheeks."
                            f "I'm sorry I couldn't be more for you. You should have chosen someone else. Maybe if you'd-"
                            pov "Shh. I chose you. You have nothing to be sorry about."
                            "And you gripped him tight."
                            jump deathToadQuestions
                "If you accepted your fate, turn to page 265.":
                    pov "Alright. I'm ready"
                    m "No-one's ever ready. But there's no time left."
                    "She gently took you down to the kingdom of Death."
                    call endStamp
                    "And you lie there still."
                    #"And what happened to the Witch, you ask?"
                    #"I ate her up whole."
                    #"Every piece."
                    jump end

    # f "Well, you have the real thing now. You won't need me anymore."
    # label frogConvoFinale:
    #     menu:
    #         #So who are you really?
    #         #Why did you lie?
    #         "What was the curse?":
    #             f "There was never a curse."
    #             f "I just didn't want to be me anymore."
    #             jump frogConvoFinale

    #Stuff for the devil, god, death

label endStamp:
    show text "{b}THE END.{/b}":
        xalign 0.5
        ypos 650
    show stamp:
        xalign 0.5
        ypos 680
    return

label end:
    #hide treesbg
    play sound pageFlip
    scene bg page
    ""
    play sound pageFlip
    scene bg credits
    #define gui.dialogue_ypos = 100#480
    #define gui.textbox_height = 100#410
    #Space between each line of the credits
    $tx = 5
    #indent space for each number
    $ti=20
    $ ui.text("The images in this volume were collated from various illustrations in the public domain. Wherever possible, I have tried to provide the place and date of publication of each literary source. The complete list of contributers follows.{vspace=30}{space=[ti]}1. {b}The Thief:{/b} 'In Powder and Crinoline' (1912), Kay Nielsen.{vspace=[tx]}{space=[ti]}2. {b}The Witch:{/b} 'Portrait of Lady Elizabeth Keppel' (1761), Joshua Reynolds.{vspace=[tx]}{space=[ti]}3. {b}The Toad:{/b} 'Little Miss Muffet, and other stories' (1902), Published by Mcloughlin Bros. Artist unknown.{vspace=[tx]}{space=[ti]}4. {b}The Mushroom:{/b} 'Fantaisie d'Automne: Les Champignons for La Vie Parisienne' (1916), George Barbier.{vspace=[tx]}{space=[ti]}5. {b}G-d:{/b} 'Der Weeg zu Christo' (1682), Jakob Böhme.{vspace=[tx]}{space=[ti]}6. {b}The Devil:{/b} 'The Papal Pyramid' (1600), private collection. Artist unknown.{vspace=[tx]}{space=[ti]}7. {b}Death, The Thief's Mother:{/b} 'De gli habiti antichi et moderni di diversi parti del mondo, libri due ...' (1590). Woodcutting by Christoph Krieger, published by Cesare Vecellio.{vspace=[tx]}", xpos=50, ypos=150, xmaximum=520)
    $ renpy.pause ()
    $ ui.text("{space=[ti]}8. {b}Mum, You:{/b} 'Regula Emblematica Sancti Benedicti' (1780), Saint Benedict et. al.{vspace=[tx]}{space=[ti]}9. {b}Mysterious Old Woman:{/b} 'The Clothing of the Renaissance World: Europe - Asia - Africa - The Americas' (1590), Cesare Vecellio.{vspace=[tx]}{space=[ti]}10. {b}Enigmatic Gentleman:{/b} 'Silhouette Portrait of a Gentleman Standing in an Army Encampment' (1844), Auguste Edouart.{vspace=[tx]}{space=[ti]}11. {b}The Hunter:{/b} 'Lady Hunter with Rifle' (1912). Artist unknown.{vspace=[tx]}{space=[ti]}12. {b}The Sparrow-Herder:{/b} 'Grimm's Fairy Tales' (1909), Arthur Rackham. Sparrow from 'Birds of Asia' (1871), John Gould.{vspace=[tx]}{space=[ti]}13. {b}The Mayor:{/b} 'The pipe of freedom' (1869), Thomas Smith.{vspace=[tx]}{space=[ti]}14. {b}The Goose Girl, The Gloom-Monger:{/b} 'Grimm's Fairy Tales' (1909), Arthur Rackham.{vspace=[tx]}{space=[ti]}15. {b}The Thing in the Well, Passing Echidna, the Skin-Mask, and Goblin No. 2:{/b} 'Devises heroïques' (1551), Claude Paradin. 'A Year Book of Folklore' (1959), Christine Chaundler.{vspace=[tx]}{space=[ti]}16. {b}The Entire Town:{/b} 'Liber Floridus' (between 1090 and 1120), Lambert, Canon of Saint-Omer.{vspace=[tx]}", xpos=50, ypos=150, xmaximum=520)
    $ renpy.pause ()
    show tornPage2 onlayer screens zorder 101
    show tornPage2bg onlayer screens zorder 99
    $ ui.text("{space=[ti]}17. {b}Scraggs McKenzie, Banksia Bounty-Hunter:{/b} 'Wood engraving of Australian bushranger Dan Morgan' (1864), Samuel Calvert. 'The Banksia' (1790), John White.{vspace=[tx]}{space=[ti]}18. {b}The Devil's Sooty Grandmother:{/b} ‘Habit de Furie’ (1725), François Joullain.{vspace=[tx]}{space=[ti]}19. {b}Brildebrogue Chippingham:{/b} 'Aunt Friendly's Picture Book' (1800's), Joseph Kronheim.{vspace=[tx]}{space=[ti]}20. {b}The Bat:{/b} 'A History of the Earth and Animated Nature' (1820), Oliver Goldsmith.{vspace=[tx]}{space=[ti]}21. {b}The Rat:{/b} 'The Wiviparous Quadrupeds of North America' (1845), John Woodhouse.{vspace=[tx]}{space=[ti]}22. {b}The Black Cockatoo and The Crow-Shrike:{/b} 'Birds of Australia' (1840), John Gould. Illustrated by Elizabeth Gould.{vspace=[tx]}{space=[ti]}23. {b}The Strange Old Man:{/b} 'Arthur Rakham's Book of Pictures' (1913), Arthur Rackham.{vspace=[tx]}{space=[ti]}24. {b}Goblin No. 1, No. 3, and No. 4:{/b} 'Triptych of the Temptation of St Anthony' (1501), Hieronymus Bosch. 'The Garden of Earthly Delights' (between 1490 and 1500), Hieronymus Bosch.{vspace=[tx]}{space=[ti]}25. {b}The First and Second Pigs:{/b} 'Dictionnaire Universel D'Histoire Naturelle' (1845), Charles Dessalines D'orbigny.{vspace=[tx]}{space=[ti]}26. {b}The Third Pig:{/b} 'Dead Pig' (1796), Jean Bernard.{vspace=[tx]}{space=[ti]}27. {b}The {color=#f00}Wolf:{/color}{/b} 'Early Natural History Print' (Date Unknown), Karen Watson.{vspace=[tx]}", xpos=50, ypos=150, xmaximum=520)
    $ renpy.pause ()
    hide tornPage2 onlayer screens zorder 101
    hide tornPage2bg onlayer screens zorder 99
    show text "{b}FRIPPERIES:{/b}":
        xalign 0.5
        #xpos 50
        ypos 160
    $ ui.text("{space=[ti]}1. {b}Front Cover:{/b} 'The Forest Lovers' (1898), M. Hewlett.{vspace=[tx]}{space=[ti]}2. {b}Page:{/b} 'White watercolor paper texture' (2020), Olga Thelavart.{vspace=[tx]}{space=[ti]}3. {b}Hand:{/b} 'Devises heroïques' (1551), Claude Paradin.{vspace=[tx]}{space=[ti]}4. {b}This Book Belongs Too:{/b} 'Design for ornamental cartouche' (Date Unknown), Quentin Pierre Chedel.{vspace=[tx]}{space=[ti]}5. {b}Contents Page and Various Illustrations:{/b} 'Fairy tales from Hans Christian Andersen' (1899), Hans Christian Andersen.{vspace=[tx]}{space=[ti]}6. {b}Devil:{/b} 'Taylors Physicke has purged the Divel...' (1641), Voluntas Ambulatoria.{vspace=[tx]}{space=[ti]}7. {b}Torn Pages:{/b} 'Torn Up Paper Curved Pieces Texture' (2020), David Maier.{vspace=[tx]}{space=[ti]}8. {b}Eye:{/b} 'Vintage Eye Art' (2021), StarGladeVintage, Pixabay.{vspace=[tx]}", xpos=50, ypos=190, xmaximum=520)
    #TK: Appendix N
    #{b}Inspirational Reading:{/b} 'The Wonderful Wizard of Oz' (1900), L. Frank Baum.{vspace=[tx]}
    $ renpy.pause ()

    show text "{b}FONTS:{/b}":
        xalign 0.5
        #xpos 50
        ypos 160
    $ ui.text("{space=[ti]}1. {b}Oz's Wizard.{/b} Mario Arturo, 2012.{vspace=[tx]}{space=[ti]}2. {b}Journal.{/b} Fontourist, 2008.{vspace=[tx]}{space=[ti]}3. {b}Mom's Typewriter.{/b} Christoph Mueller, 1997.{vspace=[tx]}{space=[ti]}4. {b}Book Antiqua.{/b} Monotype Type Drawing Office, 1995.{vspace=[tx]}", xpos=50, ypos=190, xmaximum=520)
    $ renpy.pause ()
    show text "{b}SOUND:{/b}":
        xalign 0.5
        #xpos 50
        ypos 160
    $ ui.text("{space=[ti]}1. {b}Pencil:{/b} 'Pencil', Joseph Sardin, BigSoundBank.com.{vspace=[tx]}{space=[ti]}2. {b}Page Turn:{/b} 'Page Flip Sound Effect 1', SoundJay.com.{vspace=[tx]}{space=[ti]}3. {b}Fire:{/b} 'Fire Sound Effect 01', SoundJay.com.{vspace=[tx]}{space=[ti]}4. {b}Rain:{/b} 'Thunderstorm and Rain Loop', Mixkit.co.{vspace=[tx]}{space=[ti]}5. {b}Wildlife Ambience:{/b} 'Forest Twilight - for John', kangaroovindaloo, Freesound.org.{vspace=[tx]}", xpos=50, ypos=190, xmaximum=520)
    $ renpy.pause ()
    hide text
    $ ui.text("Written on the lands of the Turrbal and Jagera peoples. I pay my respects to their Elders, past and present. Sovereignty was never ceded.", xpos=50, ypos=190, xmaximum=520)
    $ renpy.pause ()

    play sound pageFlip
    return























    #--------------Testing Arena
    #== Testing different intros each time you restart the game

    # $ persistent.timesPlayed += 1
    #
    # if persistent.timesPlayed == 1:
    #     "This maybe happened, or maybe did not. The time is long past, and much is forgot."
    #
    # elif persistent.timesPlayed == 2:
    #     "Long ago, when wishing worked, there was a small village out in the middle of a vast rainforest."
    #
    # "Test"
    # "You have played the game [persistent.timesPlayed] time/s"
    #

    #== Testing random choices

    #$ randfruit = renpy.random.choice(['apple', 'orange', 'plum'])

    #== Testing menus, variables and persistent variables
    # menu:
    #  "What should I do?"
    #
    #  "Drink coffee.":
    #      "I drink the coffee, and it's good to the last drop."
    #
    #  "Drink tea.":
    #      $ drank_tea = True
    #
    #      "I drink the tea, trying not to make a political statement as I do."
    #  "Drink multi-dimensional hyper-tea.":
    #      $ persistent.tea = True
    #
    #
    # if drank_tea == True:
    #     "You drank the tea."
    #
    # else:
    #
    #     "You did not drink the tea."
    #
    # if persistent.tea == True:
    #     "(Persistent): You drink the tea. You have drunk the tea. You will have drunken the tea. You will always have drunk this tea."

    # This ends the game.
    #$ renpy.full_restart()
    #jump splashscreen
