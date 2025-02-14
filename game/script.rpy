# THE THIEF, THE WITCH, THE TOAD & THE MUSHROOM
#Script File


#=====================CUSTOM FUNCTIONS
init python:
    #==Registering channel for ambient noise (Fire, rain)
    renpy.music.register_channel("ambient1","sfx",True,tight=True)
    renpy.music.register_channel("ambient2","sfx",True,tight=True)
    #This one is used for the city ambience when you open the door to the wolf
    renpy.music.register_channel("ambient3","sfx",True,tight=True)
    #This one is just for Gameland
    renpy.music.register_channel("ambient4","sfx",True,tight=True)

    #This one is used for music stings
    renpy.music.register_channel("sting","music",loop=False)


    #Channels for music (in order to transition smoothly between multiple tracks)
    renpy.music.register_channel("music","music",True,tight=True)
    renpy.music.register_channel("music1","music",True,tight=True)
    renpy.music.register_channel("music2","music",True,tight=True)
    renpy.music.register_channel("music3","music",True,tight=True)
    renpy.music.register_channel("music4","music",True,tight=True)
    renpy.music.register_channel("music5","music",True,tight=True)
    renpy.music.register_channel("music6","music",True,tight=True)

    #This is all the wolf's talking
    renpy.music.register_channel("wolf","sfx",True,tight=True)

    #Disabling the middle mouse button
    config.keymap['hide_windows'].remove('mouseup_2')
    #Disabling the right mouse button
    #config.keymap['hide_windows'].remove('mouseup_2')

    #==Purge Save Function
    #Note: This function deletes all of the player's save files. This is necessary to work with the meta-narrative stuff I'm trying to do.
    def purge_saves():
        saves = renpy.list_slots()
        for save in saves:
            renpy.unlink_save(save)
        return

    #Function to achieve nonlinear fadeout
    def accelerate(t):
        return t * t
    def slowdown(t):
        return 1 - (1 - t) * (1 - t)

    



init +1 python:
    #==Load most recent save function
    #Note: This function loads the last save made of any time (autosave, quit save, etc).
    class LoadMostRecent(Action):
            def __init__(self):
                self.slot = renpy.newest_slot()
            def __call__(self):
                renpy.load(self.slot)
            def get_sensitive(self):
                return self.slot is not None

#==Default player name (persistent)
init python:
    def name_func(newstring):
        store.persistent.povname = newstring

#=====================PERSISTENT DATA
#This data carries over between save files and games, permanently.
init:
    
    #Sets the default game menu screen to be Preferences
    default _game_menu_screen = "preferences"

    #Persistent Player Name
    default persistent.povname = ""
    #Number of times the game has been played
    default persistent.timesPlayed = 0
    #The ambience - is it on or not?
    default persistent.phoneOn = True

    default persistent.nameSet = False

    #persistent pronouns
    default persistent.he = "he"
    default persistent.He = "He"
    default persistent.his = "his"
    default persistent.His = "His"
    default persistent.him = "him"
    default persistent.Him = "Him"
    default persistent.Hes = "He's"
    default persistent.hes = "he's"

    #===========Persistent Disappearances

    #How many of the 4 main characters have disappeared
    default persistent.vanished = 0

    #Who has disappeared specifically - main cast
    default persistent.thiefVanished = False
    default persistent.witchVanished = False
    default persistent.toadVanished = False
    default persistent.mushroomVanished = False

    #Who was the last to die?
    #Options: Thief, Toad, Witch, Mushroom, None
    default persistent.vanishedLast = "None"

    # Which side characters have disappeared
    #Your mum
    default persistent.mumVanished = False
    #God
    default persistent.miwVanished = False
    #The devil
    default persistent.mirVanished = False
    #Death
    default persistent.wibVanished = False
    #The devil's grandmother
    default persistent.dgVanished = False
    #Brildebrogue chippingham
    #default persistent.bcVanished = False
    #The hunter
    default persistent.hVanished = False
    #The old gloom-monger
    default persistent.gmVanished = False
    #The thing in the well
    default persistent.wellVanished = False
    #Scraggs McKenzie and the boys
    default persistent.scVanished = False
    #The mayor
    default persistent.mayVanished = False
    #Goose-girl
    default persistent.goVanished = False
    #The sparrow-herder
    default persistent.shVanished = False
    #Strange and crooked old man
    default persistent.somVanished = False
    #The toad's carriage-carriers (bat, rat, cockatoo, crowshrike
    #default persistent.batVanished = False
    #Goblin 1, 2, 3, 4, and the goblin queen
    #default persistent.goblinsVanished = False
    #Pig 1, 2, and 3
    default persistent.pigsVanished = False
    #Have the stars disappeared during the mushroom's solo disappearance ending?
    default persistent.starsVanished = False
    #Safe for work mode
    #Gets rid of all drawings with boobs / gore
    default persistent.sfw = False

    #Have you typed the wolf's name into the naming thing at the start
    default persistent.wolfNamed = False

    #Have you triggered the final ending where the book is born anew?
    #TK: Testing, change back to false
    default persistent.bookEnd = False

    #Has the book been burned?
    default persistent.bookBurned = False

    #Have you seen the message about saving
    default persistent.saveMessage = False

    #What title did you choose for the book ending?
    default persistent.finaleTitle = "Cobbler"

    #The other randomly generated titles
    default persistent.name1Rand = renpy.random.randint(1,6)
    default persistent.name2Rand = renpy.random.randint(1,6)
    default persistent.name3Rand = renpy.random.randint(1,6)
    default persistent.name4Rand = renpy.random.randint(1,6)

    #Whether the continue button appears, or the Begin button
    default persistent.continueButton = False

#=====================BASIC VARIABLES
#These are the basic variables used throughout the game
init:

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

    #Demo mode: cuts you off quickly
    define demo = False

    #Act 1, Chapter 1 - the 3 Godfathers
    define firstManWho = False
    define secondManWho = False
    define thirdManWho = False
    define godfather = "none"

    #The intro menu with questions
    define introHappy = False
    define introNeighbours = False
    define introNeighboursN = False
    define introNeighboursE = False
    define introNeighboursS = False
    define introNeighboursW = False

    #A variable that switches on for larger full screen menus to make the choice menu yalign change
    define fullScreenMenu = False
    define halfScreenMenu = False
    define wolfMenu = False
    #Alters main menu to prevent returning to menu during burning sequence
    define burnMenu = False

    #Act 1, Chapter 2: The road to the village
    #How many pitiful Noooo's have you shouted
    define pitiful = 0
    #Did you keep the pig?
    define pig = False
    #The Pig's story in the witch chapter
    define pig1Story = False
    #The witch's story
    define witchStory = False
    #Have you seen the mushroom utter the password for her house?
    define mushroomPassword = False
    #Have you seen the mushroom's cavern?
    define mushroomCavernSeen = False
    #How far have you gotten with each character?
    define mushroomArc = 0
    define thiefArc = 0
    define toadArc = 0
    define witchArc = 0
    define houseLockOut = False

    #Mushroom stuff
    #Have the mushroom threatened to curse you?
    define mushroomCurse = False
    define mushroomConfuse = False
    define mushroomTea = False
    define mushroomAllThis = False
    define mushroomIntruding = False
    define mushroomBody = False
    define mushroomCurseChat = False
    define mushroomSoloConvo = 0
    #Has the master thief stolen from you?
    define stuffStolen = False

    #=====Act 2, Chapter 1: The Village Feast
    define foodLook = False
    #How many times you've attempted to turn and go back home
    define turnedHome = 0

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
    define tarpDone = False

    #Each villager's conversation tree
    #TK: Add multiple of these for each run
    define gloommongerChat = 0
    define goosemongerChat = 0
    define sparrowherderChat = 0
    define hunterChat = 0
    define mayorChat = 0
    define wellChat = 0
    define pigChat =0
    define gutterlingChat =0

    #Random chances
    define sparrowherderRand = renpy.random.randint(1,3)
    define mayorRand = renpy.random.randint(1,3)
    define pig2Rand = renpy.random.randint(1,6)
    define wellRand = renpy.random.randint(1,2)

    #=====Act 2, chapter 2: The Thief
    #What you trapped the chest with
    define chest = ""
    #Whether you've yelled No
    define pitifulGoose = False
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
    define thiefWrong2 = False
    define thiefMissing = False
    define thiefHome = False
    define goblinNum = 30


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
    define experiments = 0
    define witchCrystal = False
    define witchExperiment1 = False
    define witchExperiment2 = False
    define witchExperiment3 = False
    define witchExperiment4 = False
    define hellCavern = False

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
    define toadCurse = False
    define construction = 0

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
    define mushroomSoloAbout = False
    define mushroomSoloThoughts = False
    define mushroomSoloRun = False
    define mushroomSoloNext = False
    define mushroomSoloSilence = False

    #Wolf Variables for exploring places when people have disappeared
    define wanderedAimlessly = False
    define wanderedNightGod = False
    define firepoker = False
    define doorLock = False
    define inCottage = False
    define birthdayNote = "{size=16}{font=fonts/segoesc.ttf}{color=#45413c}{alpha=*0.6}I saw this intriguing article while I was researching online and it seemed like the kind of thing that you would enjoy. It is wonderful what you can find on the internet these days. It was tough to find the book but we were able to track down this volume second-hand, which the bookshop owner told us may be one of the only remaining copies! I hope that you will enjoy it. \n\nPlease give our best to your mum and dad and tell them that we are doing well here. The weather has been lovely.\n\nHappy birthday, [povname].\n\nLove Grandma and Grandpa.{/color}{/font}{/size}"
    define wanderAttempted = False
    define toadStopped = False
    define shStopped = False

    #Investigating the clearing
    define clearing =""

    #The final conversation with the wolf in the silence ending
    define lookUp = 1
    define silenceWho = False
    define silenceFire = False
    define silenceLeave = False
    define silenceFriends = False
    define silenceFriendsTalk = False
    define silenceTrick = False
    define silenceEat = False
    define silenceRest = False
    define silenceEvil = False
    define silenceAlone = False
    define silenceNo = False
    define silenceAttic = False
    define silenceLivingRoom = False
    define silenceStudy = False
    define silenceBasement = False

    #Wishes when you say the wolf's true name
    define wishRiches = False
    define wishLove = False
    define wishWorld = False
    define wishPain = False
    define wishEnemies = False
    define wishFriends = False
    define wishLost = False
    define wishHappy = False
    define wishImmortal = False

    #Showing the photo of Humbaba for the help screen
    define humbabaShowing = True

    #The conversation with Gilgamesh
    define gilWho = False
    define gilWalls = False
    define gilStone = False
    define gilEnkidu = False
    define gilNext = False
    define gilDeath = False
    define gilHumbaba = False
    define gilDo = False
    define gilCome = False

    #Are you in a secret scene that you reach by putting in a name in the name screen?
    define nameSecret = False

    define gutterPlace = False
    define gutterWail = False
    define gutterHelp = False

    #How long it takes to dissolve the cover image
    $dissolveTime = 0

    #Have you ventured down the secret gilgamesh path (Only appears at the last moment when 3 people have disappeared)
    $gilgameshPathFollowed = False


    ###==== Countdown
    #This screen counts down automatically and then jumps to a label once the countdown is finished
    #used for the BurnEnd and could also be useful for some random moments throughout the game
    init: ### just setting variables in advance so there are no undefined variable problems
        $ timer_range = 0
        $ timer_jump = 0
        $ timer_call = 0
        $ time = 0

    screen countdown:
        timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    screen countdownCall:
        timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Call(timer_call)])

    ## Burning Variables
    #For all the final conversations in the book burning ending
    define wolfBurning = False
    define miwBurning = False
    define mirBurning = False
    define wibBurning = False
    define mumBurning = False
    define gmBurning = False
    define thiefBurning = False
    define toadBurning = False
    define batBurning = False
    define hBurning = False
    define mayBurning = False
    define witchBurning = False
    define dgBurning = False
    define pigsBurning = False
    define shBurning = False
    define goBurning = False
    define queenBurning = False
    define goblinBurning = False
    define bcBurning = False
    define somBurning = False
    define mushroomBurning = False
    define scraggsBurning = False
    define wellBurning = False


#============== Steam variables
init:
    #Defining steam app id
    define config.steam_appid = 2233770

    #Steam achievements
    $achievement.register("THE_END")


#=====================IMAGES
#Defining all images
init:
    #The position to show the background illustrations
    $ artPos = Position(xpos=0.5, xanchor=0.5, ypos=35, yanchor=0)
    #full screen post (upper left corner)
    $ fullPos = Position(xpos=0, xanchor=0.0, ypos=0, yanchor=0)
    $ name1Pos = Position(xpos=0.5, xanchor=0.5, ypos=190, yanchor=0)
    $ name2Pos = Position(xpos=0.5, xanchor=0.5, ypos=242, yanchor=0)
    $ name3Pos = Position(xpos=0.5, xanchor=0.5, ypos=291, yanchor=0)
    $ name4Pos = Position(xpos=0.5, xanchor=0.5, ypos=350, yanchor=0)
    $ name5Pos = Position(xpos=0.5, xanchor=0.5, ypos=451, yanchor=0)
    $ andPos =  Position(xpos=0.5, xanchor=0.5, ypos=405, yanchor=0)

    ##====Full Screen Images
    #Book Burning Movie
    image bookBurnMovie = Movie(play="movies/bookBurn-Split.ogv", side_mask=True, loop=False)

    #White screen
    image white = "#FFFFFF"

    #Flash effect
    $ flash = Fade(.25, 0, 2, color="#fff")

    #Covers with no bunnies vanished
    image coverBase = "cover-base.png"
    image coverOverlay = "cover-overlay.png"
    image coverWitch = "cover-witch.png"
    image coverThief = "cover-thief.png"
    image coverToad = "cover-toad.png"
    image coverMushroom = "cover-mushroom.png"
    image coverWolf1 = "cover-wolf-1.png"
    image coverWolf2 = "cover-wolf-2.png"
    image coverWolf3 = "cover-wolf-3.png"
    image coverWolf4 = "cover-wolf-4.png"
    image coverBack = "coverBack.png"
    image backPage = "backPage.png"
    #Note about saving
    image contentsNote = "contents_note.png"


    # #image cover5 = "cover-5.png"
    # #image cover6 = "cover-6.png"
    # #image cover9= "cover-9.png"
    # #image cover14= "cover-14.png"
    # #Covers with 1 bunny vanished
    # image covera = "covera.png"
    # #image cover5a = "cover-5a.png"
    # image cover6a = "cover-6a.png"
    # image cover9a= "cover-9a.png"
    # image cover14a= "cover-14a.png"
    # #Covers with 2 bunnies vanished
    # image coverb = "coverb.png"
    # image cover5b = "cover-5b.png"
    # image cover6b = "cover-6b.png"
    # image cover9b= "cover-9b.png"
    # image cover14b= "cover-14b.png"
    # #Covers with 3 bunnies vanished
    # image coverc = "coverc.png"
    # image cover5c = "cover-5c.png"
    # image cover6c = "cover-6c.png"
    # image cover9c= "cover-9c.png"
    # image cover14c= "cover-14c.png"
    #Covers with all bunnies vanished
    #image coverd = "coverd.png"
    #Cover once you have gotten ending A: The book continues on
    image coverFinaleA = "coverFinale.png"
    #Cover if the book is burned
    image coverBurned = "coverBurned.png"

    #image credits = "acknowledgements.png"
    #Set up the cover - it changes based on how many people have disappeared
    image title = "title.png"
    image title-toadGone = "title-toadGone.png"
    image title-witchGone = "title-witchGone.png"
    image title-thiefGone = "title-thiefGone.png"
    image title-mushroomGone = "title-mushroomGone.png"

    image title-toadAlone = "title-toadAlone.png"
    image title-witchAlone = "title-witchAlone.png"
    image title-thiefAlone = "title-thiefAlone.png"
    image title-mushroomAlone = "title-mushroomAlone.png"

    image title-toadwitchGone = "title-toad+witchGone.png"
    image title-toadthiefGone = "title-toad+thiefGone.png"
    image title-toadmushGone = "title-toad+mushGone.png"
    image title-witchthiefGone = "title-witch+thiefGone.png"
    image title-witchmushGone = "title-witch+mushGone.png"
    image title-thiefmushGone = "title-thief+mushGone.png"


    image title-wolf = "title-wolf.png"
    image title-allGone = "title-allGone.png"

    ##===========Marginalia
    image characters = "Marginalia/characters.png"
    image devil = "Marginalia/devil.png"
    image eaten = "Marginalia/eaten.png"
    image flower1 = "Marginalia/flower1.png"
    image flower2 = "Marginalia/flower2.png"
    image flower3 = "Marginalia/flower3.png"
    image mushroom = "Marginalia/mushroom.png"
    image noteCrumbs = "Marginalia/noteCrumbs.png"
    image noteDeal = "Marginalia/noteDeal.png"
    image noteEaten = "Marginalia/noteEaten.png"
    image noteFood = "Marginalia/noteFood.png"
    image noteFree = "Marginalia/noteFree.png"
    image noteHome = "Marginalia/noteHome.png"
    image noteListen = "Marginalia/noteListen.png"
    image noteListen2 = "Marginalia/noteListen2.png"
    image noteName = "Marginalia/noteName.png"
    image noteSay = "Marginalia/noteSay.png"
    image noteSilence = "Marginalia/noteSilence.png"
    image noteStop = "Marginalia/noteStop.png"
    image noteWaiting = "Marginalia/noteWaiting.png"
    image noteWolf = "Marginalia/noteWolf.png"
    image noteDoor = "Marginalia/noteDoor.png"
    image noteChance = "Marginalia/noteChance.png"
    image noteReturn = "Marginalia/noteReturn.png"
    image noteCareful = "Marginalia/noteCareful.png"
    image spiral1 = "Marginalia/spiral1.png"
    image spiral2 = "Marginalia/spiral2.png"
    image spiral3 = "Marginalia/spiral3.png"
    image spiral4 = "Marginalia/spiral4.png"
    image spiral5 = "Marginalia/spiral5.png"
    image spiral6 = "Marginalia/spiral6.png"
    image spiral7 = "Marginalia/spiral7.png"
    image spirit = "Marginalia/spirit.png"
    image spirit2 = "Marginalia/spirit2.png"
    image spirit3 = "Marginalia/spirit3.png"
    image stars = "Marginalia/stars.png"
    image swordfight = "Marginalia/swordfight.png"
    image thief = "Marginalia/thief.png"
    image toad = "Marginalia/toad.png"
    image toadAngry = "Marginalia/toadAngry.png"
    image toadHappy = "Marginalia/toadHappy.png"
    image toadSad = "Marginalia/toadSad.png"
    image train = "Marginalia/train.png"
    image witch = "Marginalia/witch.png"
    image witches = "Marginalia/witches.png"
    image wolf1 = "Marginalia/wolf1.png"
    image wolf2 = "Marginalia/wolf2.png"
    image wolf3 = "Marginalia/wolf3.png"
    image wolf4 = "Marginalia/wolf4.png"
    image wolf5 = "Marginalia/wolf5.png"
    image wolf6 = "Marginalia/wolf6.png"
    image wolf7 = "Marginalia/wolf7.png"
    image wolf8 = "Marginalia/wolf8.png"
    image wolf9 = "Marginalia/wolf9.png"
    image wolf10= "Marginalia/wolf10.png"
    image wolf11 = "Marginalia/wolf11.png"
    image wolf12 = "Marginalia/wolf12.png"
    image wolf13 = "Marginalia/wolf13.png"
    image wolf14 = "Marginalia/wolf14.png"

    image scribble5 = "Marginalia/scribble5.png"
    image scribble4 = "Marginalia/scribble4.png"
    image scribble3 = "Marginalia/scribble3.png"
    image scribble2 = "Marginalia/scribble2.png"
    image scribble1 = "Marginalia/scribble1.png"
    image scribble9 = "Marginalia/scribble9.png"
    image scribble8 = "Marginalia/scribble8.png"
    image scribble6 = "Marginalia/scribble6.png"

    image monster4 = "Marginalia/monster4.png"
    image monster3 = "Marginalia/monster3.png"
    image monster2 = "Marginalia/monster2.png"
    image monster = "Marginalia/monster.png"
    image rocks = "Marginalia/rocks.png"

    #Map
    image mapClosed = "mapClosed.png"
    image map1 = "map1.png"
    image mapBlankAll = "mapBlank.png"
    image mapBlankHouse = "mapBlank-house.png"
    image mapBlankVillage = "mapBlank-village.png"

    image mapBlankMisc = "mapBlank-misc.png"
    image mapBlankThief = "mapBlank-thief.png"
    image mapBlankToad = "mapBlank-toad.png"
    image mapBlankWitch = "mapBlank-witch.png"
    image mapBlankMushroom = "mapBlank-mushroom.png"

    #Notes found throughout book
    image note1Closed = "note1Closed.png"
    image note1Open = "note1Open.png"
    image tDiaryClosed = "diaryClosed.png"
    image tDiaryOpen = "diaryOpen.png"
    image posterClosed = "posterClosed.png"
    image posterOpen = "posterOpen.png"
    image posterOpen2 = "posterOpen2.png"
    image news = "newsArticle.png"
    image essay1 = "essay1.png"
    image essay2 = "essay2.png"
    image essay3 = "essay3.png"
    image essay4 = "essay4.png"
    image essay5 = "essay5.png"
    image essay6 = "essay6.png"
    image essayClosed = "essayClosed.png"
    image creepiestClosed = "creepiestClosed.png"
    image creepiestOpen = "creepiestOpen.png"
    image creepiestOpen2 = "creepiestOpen2.png"
    image gilgameshClosed =  "gilgameshClosed.png"
    image gilgameshClosedHover =  "gilgameshClosedHover.png"
    image gilgameshOpen =  "gilgameshOpen.png"
    image humbabaFront =  "Names/humbaba.png"
    image humbabaBack =  "Names/humbaba-back.png"
    image humbabaBack2 =  "Names/humbaba-back2.png"

    #Images for the names for the ending
    image name1-Thief = "titles/name1-Thief.png"
    image name2-Witch = "titles/name2-Witch.png"
    image name3-Toad = "titles/name3-Toad.png"
    image name4-Mushroom = "titles/name4-Mushroom.png"

    #Random Name 1's
    image name1-Imp = "titles/name1-Imp.png"
    image name1-Boots = "titles/name1-Boots.png"
    image name1-Frost = "titles/name1-Frost.png"
    image name1-Goat = "titles/name1-Goat.png"
    image name1-Fiend = "titles/name1-Fiend.png"
    image name1-Rake = "titles/name1-Rake.png"

    #Random Name 2's
    image name2-Midwife = "titles/name2-Midwife.png"
    image name2-Moon = "titles/name2-Moon.png"
    image name2-Mountain = "titles/name2-Mountain.png"
    image name2-Pumpkin = "titles/name2-Pumpkin.png"
    image name2-Tyrant = "titles/name2-Tyrant.png"
    image name2-Toymaker = "titles/name2-Toymaker.png"

    #Random Name 3's
    image name3-Beggar = "titles/name3-Beggar.png"
    image name3-Crone = "titles/name3-Crone.png"
    image name3-Firebird = "titles/name3-Firebird.png"
    image name3-Sausage = "titles/name3-Sausage.png"
    image name3-Shepherd = "titles/name3-Shepherd.png"
    image name3-Baker = "titles/name3-Baker.png"

    #Random Name 4's
    image name4-Swans = "titles/name4-Swans.png"
    image name4-Blindworm = "titles/name4-Blindworm.png"
    image name4-Castle = "titles/name4-Castle.png"
    image name4-GlassCoffin = "titles/name4-GlassCoffin.png"
    image name4-SingingBone = "titles/name4-SingingBone.png"
    image name4-SnakeLeaves = "titles/name4-SnakeLeaves.png"

    #Name 5 (Your chosen title)
    image name5-Aristocrat = "titles/name5-Aristocrat.png"
    image name5-Cobbler = "titles/name5-Cobbler.png"
    image name5-Trickster = "titles/name5-Trickster.png"
    image name5-Crow = "titles/name5-Crow.png"
    image name5-Specter = "titles/name5-Specter.png"
    image name5-WinterRose = "titles/name5-WinterRose.png"
    image name5-Fool = "titles/name5-Fool.png"
    image name5-WaterNixie = "titles/name5-WaterNixie.png"
    image name5-Giant = "titles/name5-Giant.png"
    image name5-Bushranger = "titles/name5-Bushranger.png"
    image name5-Butcher = "titles/name5-Butcher.png"
    image name5-Warrior-Poet = "titles/name5-Warrior-Poet.png"
    image name5-Heirophant = "titles/name5-Heirophant.png"



    image nameAnd = "titles/and.png"
    ##====GUI Elements
    image shadow = "shadow.png"
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
    image nightbg = ConditionSwitch(
        "persistent.starsVanished == False", "Backgrounds/night.png",
        "persistent.starsVanished == True", "Backgrounds/night14.png")

    # if persistent.starsVanished:
    #     image nightbg= "Backgrounds/night14.png"
    # else:
    #     image nightbg= "Backgrounds/night.png"
    image night2bg= "Backgrounds/night2.png"
    image night3bg= "Backgrounds/night3.png"
    image night4bg= "Backgrounds/night4.png"
    image night5bg= "Backgrounds/night5.png"
    image night6bg= "Backgrounds/night6.png"
    image night7bg= "Backgrounds/night7.png"
    image night8bg= "Backgrounds/night8.png"
    image night9bg= "Backgrounds/night9.png"
    image night10bg= "Backgrounds/night10.png"
    image night11bg= "Backgrounds/night11.png"
    image night12bg= "Backgrounds/night12.png"
    image night13bg= "Backgrounds/night13.png"
    image night14bg= "Backgrounds/night14.png"

    image nightgodbg = ConditionSwitch(
        "persistent.starsVanished == False", "Backgrounds/nightgod.png",
        "persistent.starsVanished == True", "Backgrounds/nightgod-nostars.png")

    # if persistent.starsVanished:
    #     image nightgodbg= "Backgrounds/nightgod-nostars.png"
    # else:
    #     image nightgodbg= "Backgrounds/nightgod.png"
    image sunbg= "Backgrounds/sun.png"
    image winterbg= "Backgrounds/winter.png"
    image hellbg= "Backgrounds/hell.png"
    image silverbg = "Backgrounds/silver.png"

    image cottagebg= "Backgrounds/cottage.png"
    image cottageintbg= "Backgrounds/cottageInt.png"
    image silvertreesbg = "Backgrounds/silverTrees.png"
    image hellcottagebg = "Backgrounds/hellcottage.png"

    image manorextbg = "Backgrounds/manorExt.png"
    image riverbg = "Backgrounds/river.png"
    image mountainsbg = "Backgrounds/mountains.png"

    image deathbg = ConditionSwitch(
        "persistent.starsVanished == False", "Backgrounds/death.png",
        "persistent.starsVanished == True", "Backgrounds/death-nostars.png")
    #
    # if persistent.starsVanished:
    #     image deathbg = "Backgrounds/death-nostars.png"
    # else:
    #     image deathbg =  "Backgrounds/death.png"
    image death2bg =  "Backgrounds/death2.png"
    image death3bg =  "Backgrounds/death3.png"
    image death4bg =  "Backgrounds/death4.png"
    image death5bg =  "Backgrounds/death5.png"
    image death6bg =  "Backgrounds/death6.png"

    image canopybg = "Backgrounds/canopy.png"
    image ruinsbg = "Backgrounds/ruins.png"
    image treenightbg = "Backgrounds/treeNight.png"
    image stranglerfigbg= "Backgrounds/stranglerFig.png"

    image forestbg= "Backgrounds/forest.png"
    image forest2bg = "Backgrounds/forest2.png"
    image forest4bg = "Backgrounds/forest4.png"
    image forest5bg = "Backgrounds/forest5.png"

    image darkforestbg = ConditionSwitch(
        "persistent.starsVanished == False", "Backgrounds/darkForest.png",
        "persistent.starsVanished == True", "Backgrounds/darkForest-nostars.png")

    # if persistent.starsVanished:
    #     image darkforestbg= "Backgrounds/darkForest-nostars.png"
    # else:
    #     image darkforestbg= "Backgrounds/darkForest.png"
    #


    image townfeastbg = "Backgrounds/town-feast.png"
    image townfeastbggone = "Backgrounds/town-feast-vanished.png"
    image towncrossroadsbg = "Backgrounds/town-cross.png"
    image towncrossroadsbggone = "Backgrounds/town-cross-vanished.png"
    image townextbg = "Backgrounds/town-ext.png"
    image town3bg = ConditionSwitch(
        "persistent.starsVanished == False", "Backgrounds/town3.png",
        "persistent.starsVanished == True", "Backgrounds/town3-nostars.png")

    # if persistent.starsVanished:
    #     image town3bg = "Backgrounds/town3-nostars.png"
    # else:
    #     image town3bg = "Backgrounds/town3.png"

    image mushroomcavebg = "Backgrounds/mushroomCave.png"
    image mushroomcaveunderbg = "Backgrounds/mushroomCaveUnder.png"
    image mushroombasementbg = "Backgrounds/mushroombasement.png"
    image mushroompalacebg = "Backgrounds/mushroomPalace.png"
    image mushroomgardensbg = "Backgrounds/mushroomGardens.png"

    image trainbg = "Backgrounds/train.png"
    image wellbg = "Backgrounds/well.png"
    image enginebg = "Backgrounds/engine.png"

    image futurebg = "Backgrounds/future.png"
    image darknessbg = "Backgrounds/darkness.png"
    image mementobg = "Backgrounds/memento.png"

    #Maybe - not sure about these
    image goblinintbg = "Backgrounds/goblin-int.png"
    image goblinint2bg = "Backgrounds/goblin-int2.png"
    image godbg = "Backgrounds/god.png"

    #The last empty bg
    image emptybg = "Backgrounds/empty.png"

    #New contents screen with Alex
    image alexbg = "Backgrounds/contents-alex.png"
    image georgiabg = "Backgrounds/contents-georgia.png"

    #Full screen illustrations
    image basementfullbg = "Backgrounds/basement-full.png"

    image sabbathfullbg = ConditionSwitch(
        "persistent.sfw == False", "Backgrounds/sabbath-full.png",
        "persistent.sfw == True", "Backgrounds/sabbath-full-s.png")

    # if sfw == False:
    #     image sabbathfullbg= "Backgrounds/sabbath-full.png"
    # elif sfw == True:
    #     image sabbathfullbg= "Backgrounds/sabbath-full-s.png"
    image trainfullbg = "Backgrounds/train-full.png"
    image lakefullbg = "Backgrounds/lake-full.png"

    ##====Names
    image witchName= "Names/witch.png"
    image thiefName= "Names/thief.png"
    image toadName= "Names/toad.png"
    image toadQuollName= "Names/toad-quoll.png"
    image toadGeckoName= "Names/toad-gecko.png"
    image toadRatName= "Names/toad-rat.png"

    image mushroomName = ConditionSwitch(
        "persistent.sfw == False", "Names/mushroom.png",
        "persistent.sfw == True", "Names/mushroom-s.png")
    image mushroom2Name = ConditionSwitch(
        "persistent.sfw == False", "Names/mushroom2.png",
        "persistent.sfw == True", "Names/mushroom2-s.png")
    image mushroom3Name = ConditionSwitch(
        "persistent.sfw == False", "Names/mushroom3.png",
        "persistent.sfw == True", "Names/mushroom3-s.png")
    image mushroom4Name = ConditionSwitch(
        "persistent.sfw == False", "Names/mushroom4.png",
        "persistent.sfw == True", "Names/mushroom4-s.png")
    image goblinqueenName = ConditionSwitch(
        "persistent.sfw == False", "Names/goblinqueen.png",
        "persistent.sfw == True", "Names/goblinqueen-s.png")
    image skinmaskName = ConditionSwitch(
        "persistent.sfw == False", "Names/sm.png",
        "persistent.sfw == True", "Names/sm-s.png")

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
    #image goblinqueenName="Names/goblinqueen.png"
    #image skinmaskName="Names/sm.png"
    image p1Name="Names/p1.png"
    image p2Name="Names/p2.png"
    image p3Name="Names/p3.png"
    image wivesName="Names/wives.png"
    image gilName = "Names/gilgamesh.png"
    image gName = "Names/gutterlings.png"
    image gkName = "Names/gutterking.png"


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

#=====================CHARACTERS
#Defining all characters
init:
    define w = Character("{image=witchName}{alt}The Witch:{/alt}")
    define t = Character("{image=thiefName}{alt}The Thief:{/alt}")
    define f = Character("{image=toadName}{alt}The Toad:{/alt}")
    define fq = Character("{image=toadQuollName}{alt}The Toad:{/alt}")
    define fr = Character("{image=toadRatName}{alt}The Toad:{/alt}")
    define fg = Character("{image=toadGeckoName}{alt}The Toad:{/alt}")

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
    define mysFrog = Character ("{image=mysFrogName}{alt}Mysterious (yet inexplicably handsome) Frog:{/alt}")
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
    define wives = Character ("{image=wivesName}{alt}The Wives:{/alt}")
    #Gilgamesh (Speaks in cuneiform)
    define gil = Character ("{image=gilName}{alt}Gilgamesh:{/alt}",what_font="EasyCuneiform.ttf")
    #The narrator in the gilgamesh section (speaks in cuneiform)
    define gBlank = Character ("",what_font="EasyCuneiform.ttf")
    #The guttelrings
    define g = Character ("{image=gName}{alt}The Gutterlings:{/alt}")
    #The gutter King
    define gk = Character ("{image=gkName}{alt}The Gutter King:{/alt}")

#=====================AUDIO
###Defining all Audio
init:
    ## Sound effects
    define audio.pageFlip = "audio/page-flip.mp3"
    define audio.pageFlip2 = "audio/page-flip2.wav"
    define audio.pageFlip3 = "audio/page-flip3.wav"
    define audio.bookClose = "audio/bookClose.mp3"
    define audio.bookClose2 = "audio/bookClose2.mp3"
    define audio.bookClose3 = "audio/bookClose3.mp3"
    define audio.bellTolls = "audio/bell.mp3"
    define audio.bellTolls2 = "audio/bell2.mp3"
    define audio.bellTolls3 = "audio/bell3.mp3"
    define audio.bellTolls4 = "audio/bell4.mp3"
    define audio.whiteNoise = "audio/whiteNoiseEnding.mp3"
    define audio.thunder = "audio/thunder.mp3"

    define audio.lacuna1 = "audio/lacuna1.wav"
    define audio.lacuna2 = "audio/lacuna2.wav"
    define audio.lacuna3 = "audio/lacuna3.wav"
    define audio.lacuna4 = "audio/lacuna4.wav"
    define audio.lacuna5 = "audio/lacuna5.wav"
    define audio.lacuna6 = "audio/lacuna6.wav"

    ##Music
    define music.gameland = "audio/gameland.mp3"
    #define music.hunted1 = "audio/hunted1.mp3"
    define music.adventure1= "audio/adventure1.mp3"

    define music.huntedLong1 = "audio/huntedLong1.mp3"
    define music.huntedLong2 = "audio/huntedLong2.mp3"

    define music.rememberVocalFull = "audio/rememberCleanVocalFull.wav"
    define music.rememberVocalDistFull = "audio/rememberDistVocalFull.wav"

    #Sounds for the wolf scene
    define audio.doorKnock = "audio/doorKnock.mp3"
    define audio.doorOpen = "audio/doorOpen.mp3"
    define audio.lockAttempt = "audio/lockAttempt.mp3"
    define audio.lockSuccess = "audio/lockSuccess.mp3"
    define audio.windAmbience = "audio/windAmbience.mp3"
    define audio.footstepsOutsideApproach = "audio/footstepsOutsideApproach.mp3"
    define audio.footstepsOutsideLeave = "audio/footstepsOutsideLeave.mp3"
    define audio.footstepsGrassApproach = "audio/footstepsGrassApproach.mp3"
    define audio.footstepsGrassLeave = "audio/footstepsGrassLeave.mp3"
    define audio.footstepsInsideApproach = "audio/footstepsInsideApproach.mp3"
    define audio.footstepsInsideLeave = "audio/footstepsInsideLeave.mp3"
    define audio.phoneClick = "audio/phoneClick.mp3"
    define audio.firePoker = "audio/firePoker.mp3"
    define audio.fireLit = "audio/fireLit.mp3"
    #the wolf's conversations
    define audio.wolfNo = "audio/wolfNo.mp3"

    define audio.rain = "audio/rain.wav"
    define audio.fire = "audio/fire.mp3"
    define audio.footsteps = "audio/footsteps.wav"
    define audio.wolfBreath = "audio/wolfBreath.wav"
    define audio.wind = "audio/wind.wav"
    define audio.wolfApproaches = "audio/wolfApproaches.wav"

#=====================MENU LABELS
#These labels are for the basic menus, splash screens, etc.

#Splashscreen - The front cover of the book that appears before the main menu.
label before_main_menu: #splashscreen - changed to before_main_menu so it always displays

    #This stops the player from skipping over the dissolve sequence as characters disappear
    $_dismiss_pause = False

    #Default music volume = 50%
    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True

            _preferences.volumes['music'] *= .50


    if persistent.phoneOn and persistent.vanished <=3:
        $renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True)
        #$ renpy.music.play("audio/wildlife.wav", fadein=0.5, channel="ambient1", loop=True)
        $renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True, relative_volume=0.5)
    elif persistent.bookEnd:
        $renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient3", loop=True)
        #$ renpy.music.play("audio/wildlife.wav", fadein=0.5, channel="ambient1", loop=True)
        $renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True, relative_volume=0.5)
        show screen on_key_screen
    
    if persistent.bookEnd:
        show screen on_key_screen
        $ renpy.music.play("audio/rememberDistVocalFull.wav", channel="music", loop=False)
        $ config.window_title = _("")
    elif persistent.vanished == 0:
        $ config.window_title = _("The Thief, the Toad, the Witch & the Mushroom.")
    elif persistent.vanished == 1:
        if persistent.thiefVanished:
            $ config.window_title  = _("The Toad, the Witch & the Mushroom.")
        if persistent.toadVanished:
            $ config.window_title = _("The Thief, the Witch & the Mushroom.")
        if persistent.witchVanished:
            $ config.window_title = _("The Thief, the Toad & the Mushroom.")
        if persistent.mushroomVanished:
            $ config.window_title = _("The Thief, the Toad & the Witch.")
    elif persistent.vanished == 2:
        if persistent.thiefVanished and persistent.toadVanished:
            $ config.window_title = _("The Witch & the Mushroom.")
        if persistent.thiefVanished and persistent.witchVanished:
            $ config.window_title = _("The Toad & the Mushroom.")
        if persistent.thiefVanished and persistent.mushroomVanished:
            $ config.window_title = _("The Toad & the Witch.")
        if persistent.toadVanished and persistent.witchVanished:
            $ config.window_title = _("The Thief & the Mushroom.")
        if persistent.toadVanished and persistent.mushroomVanished:
            $ config.window_title = _("The Thief & the Witch.")
        if persistent.witchVanished and persistent.mushroomVanished:
            $ config.window_title = _("The Thief & the Toad.")
    elif persistent.vanished == 3:
        if not persistent.thiefVanished:
            $ config.window_title = _("The Thief.")
        if not persistent.toadVanished:
            $ config.window_title = _("The Toad.")
        if not persistent.witchVanished:
            $ config.window_title = _("The Witch.")
        if not persistent.mushroomVanished:
            $ config.window_title = _("The Mushroom.")
    elif persistent.vanished == 4:
        $ config.window_title = _("The Wolf.")



    if persistent.bookBurned:
        show screen on_key_screen
        $renpy.music.play("audio/rememberDistInstFull.wav", channel="music", fadein=5.0, relative_volume=0.5, loop=False)
        
        if persistent.vanished != 4:
            show coverBase
        if persistent.witchVanished == False:
            show coverWitch
        if persistent.toadVanished == False:
            show coverToad
        if persistent.thiefVanished == False:
            show coverThief
        if persistent.mushroomVanished == False:
            show coverMushroom
        if persistent.vanished == 1:
            show coverWolf1
        elif persistent.vanished == 2:
            show coverWolf2
        elif persistent.vanished == 3:
            show coverWolf3
        elif persistent.vanished == 4:
            show coverWolf4

        show coverBurned
        with dissolve
        ""
        $renpy.quit()

    scene black
    show firelight animated onlayer over_screens zorder 99
    #If you're at the Book Ending, show 5 bunnies
    if persistent.bookEnd:
        show coverFinaleA with dissolve
    else:
        #if persistent.vanished != 4:
        show coverBase
        if persistent.witchVanished == False or persistent.vanishedLast== "Witch":
            show coverWitch
        if persistent.toadVanished == False or persistent.vanishedLast== "Toad":
            show coverToad
        if persistent.thiefVanished == False or persistent.vanishedLast== "Thief":
            show coverThief
        if persistent.mushroomVanished == False or persistent.vanishedLast== "Mushroom":
            show coverMushroom
        if persistent.vanishedLast == "None":
            if persistent.vanished == 1:
                show coverWolf1
            elif persistent.vanished == 2:
                show coverWolf2
            elif persistent.vanished == 3:
                show coverWolf3
            elif persistent.vanished == 4:
                show coverWolf4
        else:
            if persistent.vanished == 2:
                show coverWolf1
            elif persistent.vanished == 3:
                show coverWolf2
            elif persistent.vanished == 4:
                show coverWolf3

        #$ renpy.pause(4, hard=True)
        #TK: Add in an option for persistent.vanishedLast == "All" when everyone disappears at once

        with dissolve
        #show screen noInteract()
        if persistent.vanishedLast != "None":
            if persistent.vanished == 1:
                $dissolveTime = 4
                play sound bellTolls
                show coverWolf1
            elif persistent.vanished == 2:
                $dissolveTime = 7
                play sound bellTolls2
                show coverWolf2
            elif persistent.vanished == 3:
                $dissolveTime = 11
                play sound bellTolls3
                show coverWolf3
            elif persistent.vanished == 4:
                $dissolveTime = 15
                play sound bellTolls4
                show coverWolf4
            if persistent.vanishedLast == "Witch":
                hide coverWitch
            elif persistent.vanishedLast == "Toad":
                #$ ui.interact(6.0)
                hide coverToad
            elif persistent.vanishedLast == "Thief":
                #$ ui.interact(6.0)
                hide coverThief
            elif persistent.vanishedLast == "Mushroom":
                #$ ui.interact(6.0)
                hide coverMushroom
            elif persistent.vanishedLast == "All":
                if not persistent.toadVanished:
                    hide coverToad
                    $persistent.toadVanished = True
                if not persistent.witchVanished:
                    hide coverWitch
                    $persistent.witchVanished = True
                if not persistent.thiefVanished:
                    hide coverThief
                    $persistent.thiefVanished = True
                if not persistent.mushroomVanished:
                    hide coverMushroom
                    $persistent.mushroomVanished = True

            with Dissolve (dissolveTime,time_warp=slowdown)

            $persistent.vanishedLast = "None"

    #else:
        #$renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True, relative_volume=0)
        #$ renpy.music.play("audio/wildlife.wav", fadein=0.5, channel="ambient1", loop=True)
        #$renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True, relative_volume=0)
        #$renpy.music.play("audio/windAmbience.mp3", relative_volume=0.2, fadein=1.5, channel="ambient3", loop=True)

    $_dismiss_pause = True
    "{w=5}{nw}"
    play sound bookClose3 volume 0.45
    #=========================This shows the title of the book
    ##===This part generates a unique title for the Book ending, based on who is alive, randomly generating.
    if persistent.bookEnd:
        show title-allGone
        if persistent.thiefVanished == False:
            show name1-Thief at name1Pos
        else:
            if persistent.name1Rand == 1:
                show name1-Imp at name1Pos
            elif persistent.name1Rand == 2:
                show name1-Boots at name1Pos
            elif persistent.name1Rand == 3:
                show name1-Frost at name1Pos
            elif persistent.name1Rand == 4:
                show name1-Goat at name1Pos
            elif persistent.name1Rand == 5:
                show name1-Fiend at name1Pos
            elif persistent.name1Rand == 6:
                show name1-Rake at name1Pos

        if persistent.witchVanished == False:
            show name2-Witch at name2Pos
        else:
            if persistent.name2Rand == 1:
                show name2-Midwife at name2Pos
            elif persistent.name2Rand == 2:
                show name2-Moon at name2Pos
            elif persistent.name2Rand == 3:
                show name2-Mountain at name2Pos
            elif persistent.name2Rand == 4:
                show name2-Pumpkin at name2Pos
            elif persistent.name2Rand == 5:
                show name2-Tyrant at name2Pos
            elif persistent.name2Rand == 6:
                show name2-Toymaker at name2Pos

        if persistent.toadVanished == False:
            show name3-Toad at name3Pos
        else:
            if persistent.name3Rand == 1:
                show name3-Beggar at name3Pos
            elif persistent.name3Rand == 2:
                show name3-Crone at name3Pos
            elif persistent.name3Rand == 3:
                show name3-Firebird at name3Pos
            elif persistent.name3Rand == 4:
                show name3-Sausage at name3Pos
            elif persistent.name3Rand == 5:
                show name3-Shepherd at name3Pos
            elif persistent.name3Rand == 6:
                show name3-Baker at name3Pos

        if persistent.mushroomVanished == False:
            show name4-Mushroom at name4Pos
        else:
            if persistent.name4Rand == 1:
                show name4-Swans at name4Pos
            elif persistent.name4Rand == 2:
                show name4-Blindworm at name4Pos
            elif persistent.name4Rand == 3:
                show name4-Castle at name4Pos
            elif persistent.name4Rand == 4:
                show name4-GlassCoffin at name4Pos
            elif persistent.name4Rand == 5:
                show name4-SingingBone at name4Pos
            elif persistent.name4Rand == 6:
                show name4-SnakeLeaves at name4Pos

        #The title you chose your yourself
        if persistent.finaleTitle == "Cobbler":
            show name5-Cobbler at name5Pos
        elif persistent.finaleTitle == "Trickster":
            show name5-Trickster at name5Pos
        elif persistent.finaleTitle == "Crow":
            show name5-Crow at name5Pos
        elif persistent.finaleTitle == "Specter":
            show name5-Specter at name5Pos
        elif persistent.finaleTitle == "Winter Rose":
            show name5-WinterRose at name5Pos
        elif persistent.finaleTitle == "Fool":
            show name5-Fool at name5Pos
        elif persistent.finaleTitle == "Water Nixie":
            show name5-WaterNixie at name5Pos
        elif persistent.finaleTitle == "Giant":
            show name5-Giant at name5Pos
        elif persistent.finaleTitle == "Bushranger":
            show name5-Bushranger at name5Pos
        elif persistent.finaleTitle == "Butcher":
            show name5-Butcher at name5Pos
        elif persistent.finaleTitle == "Aristocrat":
            show name5-Aristocrat at name5Pos
        elif persistent.finaleTitle == "Warrior-Poet":
            show name5-Warrior-Poet at name5Pos
        elif persistent.finaleTitle == "Heirophant":
            show name5-Heirophant at name5Pos
        show nameAnd at andPos
    else:
        if persistent.vanished == 0:
            show title
        elif persistent.vanished == 1:
            if persistent.toadVanished:
                show title-toadGone
            if persistent.witchVanished:
                show title-witchGone
            if persistent.thiefVanished:
                show title-thiefGone
            if persistent.mushroomVanished:
                show title-mushroomGone
        elif persistent.vanished == 2:
            if persistent.toadVanished and persistent.witchVanished:
                show title-toadwitchGone
            elif persistent.toadVanished and persistent.thiefVanished:
                show title-toadthiefGone
            elif persistent.toadVanished and persistent.mushroomVanished:
                show title-toadmushGone
            elif persistent.witchVanished and persistent.thiefVanished:
                show title-witchthiefGone
            elif persistent.witchVanished and persistent.mushroomVanished:
                show title-witchmushGone
            elif persistent.thiefVanished and persistent.mushroomVanished:
                show title-thiefmushGone
        elif persistent.vanished == 3:
            if persistent.toadVanished == False:
                show title-toadAlone
            if persistent.witchVanished == False:
                show title-witchAlone
            if persistent.thiefVanished == False:
                show title-thiefAlone
            if persistent.mushroomVanished == False:
                show title-mushroomAlone

        elif persistent.vanished >= 4:
            show title-wolf
    ""
    #with Pause(5)
    #show screen music_screen
    #Ambient rain loop
    #play music rain loop volume fadein 1.0
    #Ambient fireplace sounds loop
    #play audio fire loop volume 0.5 fadein 1.0

    play sound pageFlip
    if persistent.bookEnd == True:
        $he = persistent.he
        $He = persistent.He
        $his = persistent.his
        $His = persistent.His
        $him = persistent.him
        $Him = persistent.Him
        $Hes = persistent.Hes
        $hes = persistent.hes
        $povname = persistent.povname
        if persistent.povname == "alex" or persistent.povname == "Alex" or persistent.povname == "Alexandra" or persistent.povname == "alexandra" or persistent.povname == "Alexander" or persistent.povname == "alexander" or persistent.povname == "Alexis" or persistent.povname == "alexis":
            show georgiabg
        else:
            show alexbg
        ""
        jump chapter1
    if persistent.nameSet == False:
        call screen contents

    else:
        #$povname = persistent.povname
        #Using the persistent character info to define the temporary pronouns
        #This is really just done so that I don't need to write [persistent.he] every time I use a pronoun
        $he = persistent.he
        $He = persistent.He
        $his = persistent.his
        $His = persistent.His
        $him = persistent.him
        $Him = persistent.Him
        $Hes = persistent.Hes
        $hes = persistent.hes
        $povname = persistent.povname
        #show screen main_menu
        #$renpy.set_return_stack([])
        #$renpy.set_return_stack([])
        #$renpy.pop_call()
        return
        #$renpy.full_restart()

#TK: Fix this hack - instead of the pronoun screen saying "Return" it goes to this label which says return
label splashscreen2:
    $he = persistent.he
    $He = persistent.He
    $his = persistent.his
    $His = persistent.His
    $him = persistent.him
    $Him = persistent.Him
    $Hes = persistent.Hes
    $hes = persistent.hes
    if persistent.povname == "":
        $persistent.povname = "Charlie"
    elif persistent.povname == "Humbaba" or persistent.povname == "humbaba" or persistent.povname =="HUMBABA" or persistent.povname =="Huwawa" or persistent.povname =="huwawa" or persistent.povname =="HUWAWA" or persistent.povname =="Ḫum-ba-ba" or persistent.povname =="hum-ba-ba" or persistent.povname =="Ḫu-wa-wa" or persistent.povname =="hu-wa-wa" or persistent.povname =="𒄷𒌝𒁀𒁀" or persistent.povname =="𒄷𒉿𒉿":
        $persistent.povname = "Charlie"
        $povname = persistent.povname
        jump humbabaNameSecret
    elif persistent.povname == "Gilgamesh" or persistent.povname == "gilgamesh" or persistent.povname == "Gilgameš" or persistent.povname == "gilgameš" or persistent.povname == "Bilgames" or persistent.povname == "bilgames" or persistent.povname == "Pabilgames" or persistent.povname == "pabilgames"or persistent.povname == "𒀭𒄑𒂆𒈦" or persistent.povname == "𒀭𒄑𒉋𒂵𒎌"or persistent.povname == "enkidu" or persistent.povname == "Enkidu" or persistent.povname == "𒂗𒆠𒄭": #
        $persistent.povname = "Charlie"
        $povname = persistent.povname
        $nameSecret = True
        jump gilgameshStory
    $povname = persistent.povname
    if persistent.saveMessage == False:
        scene bg page
        show text "\"The river rises, flows over its banks\n and carries us all away, like mayflies\nfloating downstream; they stare at the sun,\nthen all at once there is nothing.\”\n-The Epic of Gilgamesh (Stephen Mitchell Translation)."
        show contents_note
        ""
        play sound pageFlip2
        $persistent.saveMessage = True
    call screen main_menu
    #show("main_menu")
    #$MainMenu(confirm=False)()

    #ShowMenu("main_menu")

#Setting up the firelight and music whenever the game loads
label after_load:
    #this screen allows players to delete all their saves by pressing a secret key
    

    if persistent.phoneOn and persistent.vanished <=3:
        play sound pageFlip
        $renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True)
        #$renpy.music.play("audio/Gymnopedies.mp3", fadein=0.5, channel="music", loop=True)
        #$renpy.music.play("audio/cottagegore.mp3", fadein=0.5, channel="music", loop=True)
        $renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True, relative_volume=0.5)
    elif persistent.bookEnd:
        play sound pageFlip
        $renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True)
        #$renpy.music.play("audio/Gymnopedies.mp3", fadein=0.5, channel="music", loop=True)
        #$renpy.music.play("audio/cottagegore.mp3", fadein=0.5, channel="music", loop=True)
        $renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True, relative_volume=0.5)
    else:
        play sound pageFlip
    #     $renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True, relative_volume=0)
    #     $renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True, relative_volume=0)
    #     $renpy.music.play("audio/windAmbience.mp3", relative_volume=0.2, fadein=1.5, channel="ambient3", loop=True)
    return

label musicSilence:
    #When hints of the wolf's presence are felt
    #$renpy.music.set_volume(0, delay=3.0, channel=u'ambient1')
    #$renpy.music.set_volume(0, delay=3.0, channel=u'ambient2')
    $renpy.music.set_volume(0, delay=10.0, channel=u'music')
    $renpy.music.set_volume(0, delay=10.0, channel=u'music1')
    $renpy.music.set_volume(0, delay=10.0, channel=u'music2')
    $renpy.music.set_volume(0, delay=10.0, channel=u'music3')
    $renpy.music.set_volume(0, delay=10.0, channel=u'music4')
    $renpy.music.set_volume(0, delay=10.0, channel=u'music5')
    $renpy.music.set_volume(0, delay=10.0, channel=u'music6')
    
    return

label musicReturn:
    #After a hint of the wolf's presence
    #$renpy.music.set_volume(1.0, delay=4.0, channel=u'ambient1')
    #$renpy.music.set_volume(1.0, delay=4.0, channel=u'ambient2')
    $renpy.music.set_volume(1.0, delay=10.0, channel=u'music')
    $renpy.music.set_volume(1.0, delay=10.0, channel=u'music1')
    $renpy.music.set_volume(1.0, delay=10.0, channel=u'music2')
    $renpy.music.set_volume(1.0, delay=10.0, channel=u'music3')
    $renpy.music.set_volume(1.0, delay=10.0, channel=u'music4')
    $renpy.music.set_volume(1.0, delay=10.0, channel=u'music5')
    $renpy.music.set_volume(1.0, delay=10.0, channel=u'music6')
    return

label wolfApproaches:
    #stop music fadeout 10.0
    play audio wolfApproaches
    #stop ambient2 fadeout 2.0
    #stop ambient1 fadeout 20.0
    return

#This label is used to hide all backgrounds
label hideAll:
    hide nightbg
    hide night2bg
    hide night3bg
    hide night4bg
    hide night5bg
    hide night6bg
    hide night7bg
    hide night8bg
    hide night9bg
    hide night10bg
    hide night11bg
    hide night12bg
    hide night13bg
    hide night14bg

    hide nightgodbg
    hide sunbg
    hide winterbg
    hide hellbg

    hide silverbg
    hide cottagebg
    hide cottageintbg
    hide silvertreesbg
    hide hellcottagebg

    hide manorextbg
    hide riverbg
    hide mountainsbg
    hide deathbg
    hide death2bg
    hide death3bg
    hide death4bg
    hide death5bg
    hide death6bg

    hide canopybg
    hide ruinsbg
    hide treenightbg
    hide stranglerfigbg

    hide forestbg
    hide forest2bg
    hide forest4bg
    hide forest5bg
    hide darkforestbg

    hide townfeastbg
    hide towncrossroadsbg
    hide townextbg
    hide town3bg

    hide townfeastbggone
    hide towncrossroadsbggone
    #hide townextbg
    #hide town3bg


    hide mushroomcavebg
    hide mushroomcaveunderbg
    hide mushroombasementbg
    hide mushroompalacebg
    hide mushroomgardensbg

    hide enginebg
    hide trainbg
    hide wellbg
    hide goblinintbg
    hide goblinint2bg
    hide godbg

    hide futurebg
    hide darknessbg
    hide mementobg

    hide basementfullbg
    hide sabbathfullbg
    hide trainfullbg
    hide lakefullbg
    hide tornPage1
    hide tornPage1bg

    hide stamp
    hide emptybg

    hide hand
    hide text

    return

#==This label clears all saves and persistent data and restarts the game.
#==It's used for the demo version of the game.
label demoEnd:
    #$persistent._clear(progress=True)
    $persistent.nameSet = False
    $purge_saves()
    $persistent.continueButton = False
    $quick_menu = False
    call hideAll from _call_hideAll_95
    $renpy.music.set_volume(0, delay=5.0, channel=u'ambient1')
    $renpy.music.set_volume(0, delay=5.0, channel=u'ambient2')
    $renpy.music.set_volume(0, delay=5.0, channel=u'music')

    scene black with fade
    show text "{color=#FFFFFF}This is the end of the demo. Thank you for playing!{/color}" with fade:
        xalign 0.5
        yalign 0.5
    ""
    show text "{color=#FFFFFF}The full game will have much, much more to explore.{/color}" with fade:
        xalign 0.5
        yalign 0.5
    ""
    show text "{color=#FFFFFF}If you're interested in the game, please wishlist us on Steam or subscribe to hear when the game releases!{/color}" with fade:
        xalign 0.5
        yalign 0.5
    ""
    $renpy.music.set_volume(1.0, channel=u'ambient1')
    $renpy.music.set_volume(1.0, channel=u'ambient2')
    $renpy.music.set_volume(1.0, channel=u'music')
    $quick_menu = True
    return

#=====================GAME START
#The official game script begins here
# Act 1, Chapter 2: The 3 Godparents
#The beginning of the game.

label start:
    #show screen on_key_screen
    #This makes the game save whenever you quit.
    #$ _quit_slot = "quitsave"
    $persistent.continueButton = True
    show firelight animated onlayer over_screens zorder 99
    if persistent.phoneOn and persistent.vanished <=3:
        $renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True)
        $renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True, relative_volume=0.5)
    # else:
    #     $renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True, relative_volume=0)
    #     $renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True, relative_volume=0)
    #     $renpy.music.play("audio/windAmbience.mp3", relative_volume=0.2, fadein=1.5, channel="ambient3", loop=True)
    #$ renpy.music.play("audio/wildlife.wav", fadein=0.5, channel="ambient1", loop=True)

    label chapter1:
        
        #"[sfw]"
        #scene bg page
        #show hand onlayer transient:
            #yalign 0.6#0.743
            #xalign 0.5
        #show text "CHAPTER ONE{vspace=10}{size=-5}THE THREE GODPARENTS{/size}" at truecenter
        scene bg page
        show nightbg at artPos


        #jump village

        #TK: Investigate synchro_start
        # "test"
        # play music "audio/adventure1.wav"
        # "test adventure"
        # #TK TEST
        # "Testing Music."
        #
        # play music "mysteriousHappeningsIntro.wav"
        # queue music "mysteriousHappenings1.wav"
        #
        # "Playing Mysterious Happenings (intro into loop 1)."
        # stop music fadeout 1
        # play music2 [ "<sync music>audio/mysteriousHappenings2.wav", "audio/mysteriousHappenings2.wav" ]
        #
        # #$renpy.music.play("audio/mysteriousHappenings1.wav", channel="music", loop=True)
        # "Transitioning to Mysterious Happenings 2."
        # stop music2 fadeout 1
        # play music3 [ "<sync music2>audio/mysteriousHappenings3.wav", "audio/mysteriousHappenings3.wav" ]
        #
        # "Transitioning to Mysterious Happenings 3."
        # stop music3 fadeout 6
        # "Ending music."
        # $renpy.music.play("<loop 11.995>audio/mysteriousHappenings1.wav", channel="music")
        # #queue music "mysteriousHappenings1.wav" loop
        # "Testing intro of Mysterious Happenings into the main loop."
        # #11.995
        #
        # # $renpy.music.play("audio/mysteriousHappenings1.wav", channel="music", loop=True)
        # # "Testing loop of Mysterious Happenings."
        # stop music fadeout 6
        # play music [ "<sync music>audio/mysteriousHappenings2.wav", "<from 11.995>audio/mysteriousHappenings2.wav" ] fadein 1
        # "Testing transition to Mysterious Happenings 2."
        # stop music fadeout 6
        # play music [ "<sync music>audio/mysteriousHappenings3.wav", "<from 11.995>audio/mysteriousHappenings3.wav" ] fadein 1
        # "Testing transition to Mysterious Happenings 3."
        # stop music fadeout 6
        # play music [ "<sync music>audio/mysteriousHappenings1.wav", "<from 11.995>audio/mysteriousHappenings1.wav" ] fadein 1
        # "Testing transition to Mysterious Happenings 1."
        # stop music #fadeout 6
        # "Stopping music."
        #
        # play music [ "<sync music>audio/hunted1.wav", "audio/hunted1.wav" ]
        # "Testing Hunted 1."
        # stop music fadeout 6
        # play music2 [ "<sync music>audio/hunted2.wav", "audio/hunted2.wav" ] fadein 1
        # "Testing transition to Hunted 2."
        # stop music2 fadeout 6
        # play music3 [ "<sync music2>audio/hunted3.wav", "audio/hunted3.wav" ] fadein 1
        # "Testing transition to Hunted 3."
        # stop music3 fadeout 6
        # play music4 [ "<sync music3>audio/hunted4.wav", "audio/hunted4.wav" ] fadein 1
        # "Testing transition to Hunted 4."
        # stop music4 fadeout 6
        # play music5 [ "<sync music4>audio/hunted5.wav", "audio/hunted5.wav" ] fadein 1
        # "Testing transition to Hunted 5."
        # stop ambient2 fadeout 6.0
        # stop ambient1 fadeout 6.0
        #
        # stop music5 fadeout 6
        # play music6 [ "<sync music5>audio/hunted6.wav", "audio/hunted6.wav" ] volume 2.0 fadein 1
        # "Testing transition to Hunted 6."
        # stop music6 fadeout 6
        # play music [ "<sync music6>audio/hunted1.wav", "audio/hunted1.wav" ] fadein 1
        # "Testing transition to Hunted 1."
        #
        #
        #
        #
        # stop music #fadeout 6
        # "Stopping music."

        if persistent.bookEnd:
            jump newStoryFinale
        elif persistent.vanished == 0:
            play music1 mysterioushappeningsintro
            queue music1 mysterioushappenings1
        elif persistent.vanished <= 2:
            play music1 mysterioushappenings1
        elif persistent.vanished == 3:
            play music4 mysterioushappeningsdist1

        if persistent.vanished == 0:
            "This maybe happened, or maybe did not."
            "The time is long past, and much is forgot."
            "Back in the old days, when wishing worked, your mother lived in a vast forest teeming with strange figures."
            call characterIntros from _call_characterIntros
            "Yet she had little time to spend wondering about these odd folks, for she had twelve children and had to work night and day just to feed them."
            "When you were born as the thirteenth, she had no idea what to do. She took you up in her arms and ran into the darkness of the forest, promising that she would ask the first man she met to be your Godfather."
        elif persistent.vanished == 1:
            "Neither here nor there, but long ago..."
            "Back in the old days, when the gods were real, your mother lived in a vast and mysterious rainforest full of strange figures."
            call characterIntros from _call_characterIntros_1
            "Yet she had little time to spend wondering about these odd folks, for she had ten children and had to work night and day just to feed them."
            "When you were born as the eleventh, she had no idea what to do. She took you up in her arms and ran into the darkness of the forest, promising that she would ask the first man she met to be your Godfather."
        elif persistent.vanished == 2:
            "Once there was, and once there wasn't."
            "In the long-distant days of yore, when haystacks winnowed sieves, when genies played jereed in the old bathhouse, fleas were barbers, camels were town criers, I softly rocked my baby grandmother to sleep in her creaking cradle, in an exotic land, far, far away, there was a woman who lived in a vast rainforest full of strange, empty spaces."
            call characterIntros from _call_characterIntros_2
            "Yet she had little time to think about these things, for she had four children and had to work day and night just to feed them."
            "When you were born to her as the fifth, she had no idea what to do. She took you up in her arms and ran into the darkness of the forest, promising that she would ask the first man she met to be your Godfather."
            show noteFood onlayer transient zorder 100
        elif persistent.vanished == 3:
            "Listen closely."
            "I won't repeat myself again."
            "Back in the old days, when there was still a chance, your mother lived in a vast, empty forest."
            call characterIntros from _call_characterIntros_3
            "One day, your mother gave birth to you as her first and only child."
            show noteStop onlayer transient zorder 100
            "She had no idea what to do. She took you up in her arms and ran into the darkness of the forest, promising that she would ask the first man she met to be your Godfather."
        elif persistent.vanished >= 4:
            jump allVanishedEnd

        # #Test Menu
        # menu:
        #     "DEV NOTE: This is a testing menu to allow you to jump to various endings quickly and see the disappearance scenes."
        #     "Jump to the Thief finale." if not persistent.thiefVanished and not persistent.mushroomVanished:
        #         #$renpy.fix_rollback()
        #         stop music fadeout 6
        #         jump thiefFinale
        #     "Jump to the Thief path (with the Mushroom disappeared)." if persistent.mushroomVanished and not persistent.thiefVanished:
        #         stop music fadeout 6
        #         jump thiefSolo
        #     "Jump to the Toad finale." if not persistent.toadVanished and not persistent.witchVanished:
        #         stop music fadeout 6
        #         #$renpy.fix_rollback()
        #         jump toadFinale
        #     "Jump to the Toad path (with the Witch disappeared)." if persistent.witchVanished and not persistent.toadVanished:
        #         stop music fadeout 6
        #         #$renpy.fix_rollback()
        #         jump toadSolo
        #     "Jump to the Witch finale." if not persistent.toadVanished and not persistent.witchVanished:
        #         stop music fadeout 6
        #         #$renpy.fix_rollback()
        #         jump witchFinale
        #     "Jump to the Witch path (with the Toad disappeared)." if persistent.toadVanished and not persistent.witchVanished:
        #         stop music fadeout 6
        #         #$renpy.fix_rollback()
        #         jump witchSolo
        #     "Jump to the Mushroom finale." if not persistent.thiefVanished and not persistent.mushroomVanished:
        #         stop music fadeout 6
        #         #$renpy.fix_rollback()
        #         jump mushroomFinale
        #     "Jump to the Mushroom path (with the Thief disappeared)." if persistent.thiefVanished and not persistent.mushroomVanished:
        #         stop music fadeout 6
        #         #$renpy.fix_rollback()
        #         jump mushroomSolo
        
        #     "Continue.":
        #         #$renpy.fix_rollback()
        #         "DEV NOTE: Continuing with the normal story."


    # "This maybe happened, or maybe did not."
    # "The time is long past, and much is forgot."
    # "Back in the old days, when wishing worked, you lived in a lovely cottage on the edge of a magical forest."
    # "Many strange figures lived in the woods around your house."


        call hideAll from _call_hideAll
        show forest4bg at artPos
        show scribble2 onlayer transient zorder 100
        if (renpy.music.is_playing(channel='music1')): 
            stop music1 fadeout 6.0
            play music3 [ "<sync music1>audio/mysteriousHappenings5.wav", "audio/mysteriousHappenings5.wav" ] fadein 1.0

        "In the darkness of the forest, she may or may not have met a man in white."
        "(Is anything certain these days?)"
        "His right hand held a dove. His other hand held a gun. His other hand held a crisp dollar bill. His other hand held a pillar of fire."
        "His suit was perfect. His face was too bright to look upon. He already knew what was on her mind."
        if persistent.vanished ==1:
            show noteSilence onlayer transient zorder 100
        miw "Poor woman. Let me be the Godfather."
        miw "I shall hold this child, and make sure [hes] happy on this Earth for the rest of [his] days."
        jump firstMan


    label characterIntros:
        call hideAll from _call_hideAll_231
        if persistent.thiefVanished == False:
            show forest4bg at artPos
            "To the north lived a cunning thief."
        else:
            show emptybg at artPos
            #call musicSilence from _call_musicSilence_28
            if (renpy.music.is_playing(channel='music1')): 
                stop music1 
                play music2 [ "<sync music1>audio/mysteriousHappeningsDist1.wav", "audio/mysteriousHappeningsDist1.wav" ]
            elif (renpy.music.is_playing(channel='music4')): 
                stop music4
                play music3 [ "<sync music4>audio/mysteriousHappeningsDist2.wav", "audio/mysteriousHappeningsDist2.wav" ]
            show wolf9 onlayer transient zorder 100
            "To the north, there was nothing and no-one."
            if persistent.witchVanished == False:
                if (renpy.music.is_playing(channel='music2')): 
                    stop music2 
                    play music1 [ "<sync music2>audio/mysteriousHappenings1.wav", "audio/mysteriousHappenings1.wav" ]
                elif (renpy.music.is_playing(channel='music3')): 
                    stop music3
                    play music4 [ "<sync music3>audio/mysteriousHappeningsDist2.wav", "audio/mysteriousHappeningsDist2.wav" ]
    
        call hideAll from _call_hideAll_232
        if persistent.witchVanished == False:
            show darkforestbg at artPos
            "To the west, a cackling witch."
        else:
            show emptybg at artPos
            if (renpy.music.is_playing(channel='music1')): 
                stop music1 
                play music2 [ "<sync music1>audio/mysteriousHappeningsDist1.wav", "audio/mysteriousHappeningsDist1.wav" ]
            elif (renpy.music.is_playing(channel='music4')): 
                stop music4
                play music3 [ "<sync music4>audio/mysteriousHappeningsDist2.wav", "audio/mysteriousHappeningsDist2.wav" ]
            show wolf10 onlayer transient zorder 100
            "To the west, there was nothing and no-one."
            if persistent.toadVanished == False:
                if (renpy.music.is_playing(channel='music2')): 
                    stop music2 
                    play music1 [ "<sync music2>audio/mysteriousHappenings1.wav", "audio/mysteriousHappenings1.wav" ]
                elif (renpy.music.is_playing(channel='music3')): 
                    stop music3
                    play music4 [ "<sync music3>audio/mysteriousHappeningsDist2.wav", "audio/mysteriousHappeningsDist2.wav" ]


        call hideAll from _call_hideAll_233
        if persistent.toadVanished == False:
            show manorextbg at artPos
            "To the east, a haughty toad."
        else:
            show emptybg at artPos
            if (renpy.music.is_playing(channel='music1')): 
                stop music1 
                play music2 [ "<sync music1>audio/mysteriousHappeningsDist1.wav", "audio/mysteriousHappeningsDist1.wav" ]
            elif (renpy.music.is_playing(channel='music4')): 
                stop music4
                play music3 [ "<sync music4>audio/mysteriousHappeningsDist2.wav", "audio/mysteriousHappeningsDist2.wav" ]
            show wolf5 onlayer transient zorder 100
            "To the east, there was nothing and no-one."
            if persistent.mushroomVanished == False:
                if (renpy.music.is_playing(channel='music2')): 
                    stop music2 
                    play music1 [ "<sync music2>audio/mysteriousHappenings1.wav", "audio/mysteriousHappenings1.wav" ]
                elif (renpy.music.is_playing(channel='music3')): 
                    stop music3
                    play music4 [ "<sync music3>audio/mysteriousHappeningsDist2.wav", "audio/mysteriousHappeningsDist2.wav" ]


        call hideAll from _call_hideAll_234
        if persistent.mushroomVanished == False:
            show mushroompalacebg at artPos
            "To the south, a wise mushroom."
        else:
            show emptybg at artPos
            if (renpy.music.is_playing(channel='music1')): 
                stop music1 
                play music2 [ "<sync music1>audio/mysteriousHappeningsDist1.wav", "audio/mysteriousHappeningsDist1.wav" ]
            elif (renpy.music.is_playing(channel='music4')): 
                stop music4
                play music3 [ "<sync music4>audio/mysteriousHappeningsDist2.wav", "audio/mysteriousHappeningsDist2.wav" ]
            #call musicSilence from _call_musicSilence_31
            show wolf1 onlayer transient zorder 100
            "To the south, there was nothing and no-one."
            if (renpy.music.is_playing(channel='music2')): 
                stop music2 
                play music1 [ "<sync music2>audio/mysteriousHappenings1.wav", "audio/mysteriousHappenings1.wav" ]
            elif (renpy.music.is_playing(channel='music3')): 
                stop music3
                play music4 [ "<sync music3>audio/mysteriousHappeningsDist1.wav", "audio/mysteriousHappeningsDist1.wav" ]

        call hideAll from _call_hideAll_235
        show nightbg at artPos
        return

    label firstMan:
        show hand onlayer transient:
            yalign 0.7#0.743
            xalign 0.5
        menu:
            miw "I will ask only one thing: [He] must work hard, and earn every dollar, and obey me above all else."
            #"{image=sword}{space=15}If she said yes, turn to page 13.": #"Yes.":
            #"{image=dot}{space=10}If she said yes, turn to page 13.": #"Yes.":
            "If she said yes, turn to page 13.": #"Yes.":
                label godYes:
                    miw "As I have foreseen."
                    "He bowed down and placed His great hand upon you, leaving His mark on your right hand."
                    miw "You will name [him] [povname]."
                    if he == "they":
                        miw "I will come for the child the moment [he] turn eighteen. Keep [him] safe for me until then."
                    else:
                        miw "I will come for the child the moment [he] turns eighteen. Keep [him] safe for me until then."
                    if persistent.vanished == 3:
                        $ renpy.block_rollback()
                        $persistent.mumVanished = True
                        #$purge_saves()
                        #call musicSilence from _call_musicSilence
                        stop music4 fadeout 6.0
                        play music5 [ "<sync music4>audio/mysteriousHappeningsDist2.wav", "audio/mysteriousHappeningsDist2.wav" ] fadein 1.0

                        "But He was talking to Himself."
                        "He looked around, holding the child."
                        "There was no-one there."
                        show hand onlayer transient:
                            yalign 0.7#0.743
                            xalign 0.5
                        "There never was.{vspace=200}{i}In your notes, write down that {b}You are the Godchild of the King of Kings.{/b}{/i}"
                        $godfather = "White"
                        jump chapter2
                    else:
                        mum "Just make sure you're there for the christening."
                        show hand onlayer transient:
                            yalign 0.71#0.743
                            xalign 0.5
                        "But He was already gone.{vspace=200}{i}In your notes, write down that {b}You are the Godchild of the King of Kings.{/b}{/i}"
                        $godfather = "White"
                        jump chapter2
            "If she said no, turn to page 14." if firstManWho:
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
        "(How can we be sure of anything but the greatness of G-d?)"
        "All the jewels of the earth fell from His right hand, and all the pleasures of the world fell from His left, and His other hand held all the wonders of the universe, and His other hand held a fat cigar, and His other hand held a long knife black as coal dust, and His other hand held the most intoxicating spices, such that the King of Kings would cry to taste them, and His other hand held a single dead rose, and His other hand was in his pocket and out of view."
        mir "Poor woman. Let me be the Godfather."
        mir "I'll make sure the child needs nothing, and wants everything. [He] shall live in wealth and comfort for all of [his] days, and devour only the richest meats for every meal."
        label secondMan2:
            show hand onlayer transient:
                yalign 0.71#0.743
                xalign 0.5
            menu:
                mir "I only have one condition: [He] must promise to obey no master, and scorn the rule of law, and do as [he] wilt every day of [his] life."
                "If she said yes, turn to page 21.":#"Yes.":
                    mum "Very well. Beggars can't be choosers, I suppose."
                    mir "Excellent!"
                    label devilYes:
                        "He let out a great shrieking cackle and placed His mark upon you."
                        mir "You will name [him] [povname]."
                        if he == "they":
                            mir "I will come for the child the moment [he] turn eighteen. Keep [him] safe for me until then."
                        else:
                            mir "I will come for the child the moment [he] turns eighteen. Keep [him] safe for me until then."
                        if persistent.vanished == 3:
                            $ renpy.block_rollback()
                            $persistent.mumVanished = True
                            #$purge_saves()
                            stop music4 fadeout 6.0
                            play music5 [ "<sync music4>audio/mysteriousHappeningsDist2.wav", "audio/mysteriousHappeningsDist2.wav" ] fadein 1.0
                            "But He was talking to Himself."
                            "He looked around, holding the child."
                            "There was no-one there."
                            show hand onlayer transient:
                                yalign 0.7#0.743
                                xalign 0.5
                            "There never was.{vspace=200}{i}In your notes, write down that {b}You are the Devil's Godchild.{/b}{/i}"
                            $godfather = "Red"
                            jump chapter2
                        else:
                            mum "Just make sure you're there for the christening on Sunday."
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
        show spiral2 onlayer transient zorder 100
        "In the deepest darkness of the forest, she may or may not have met a handsome woman all in black."
        "(What can any of us know for certain, except that the mercies of the Almighty are vaster than the deepest ocean and more numerous than all the pebbles on the land?)"
        "Her limbs were broken. She had no hands."
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
                    label deathYes:
                        "In one swoop She bowed down and placed Her mark upon you."
                        wib "You will name [him] [povname]."
                        if he == "they":
                            wib "The moment [he] turn eighteen, [he] will be mine."
                        else:
                            wib "The moment [he] turns eighteen, [he] will be mine."
                        wib "Keep [him] safe for me until I come for [him]. I will send three messengers before me to announce my arrival. "
                        if persistent.vanished == 3:
                            $ renpy.block_rollback()
                            $persistent.mumVanished = True
                            #$purge_saves()
                            stop music4 fadeout 6.0
                            play music5 [ "<sync music4>audio/mysteriousHappeningsDist2.wav", "audio/mysteriousHappeningsDist2.wav" ] fadein 1.0
                            "But She was talking to Herself."
                            "She looked around, holding the child."
                            "There was no-one there."
                            show hand onlayer transient:
                                yalign 0.7#0.743
                                xalign 0.5
                            "There never was.{vspace=200}{i}In your notes, write down that {b}You are Death's Godchild.{/b}{/i}"
                            $godfather = "Black"
                            jump chapter2
                        else:
                            mum "Just make sure you're there for the christening on Sunday."
                            show hand onlayer transient:
                                yalign 0.77#0.743
                                xalign 0.5
                            "But She was already leaving. She crawled into the earth with Her long, broken legs trailing behind her, until she was swallowed up whole.{vspace=160}{i}In your notes, write down that {b}You are Death's Godchild.{/b}{/i}"
                            $godfather = "Black"
                            jump chapter2
                "If she said no, turn to page 25." if thirdManWho:
                    mum "I don't want you as the Godmother. You take men before it is their time."
                    wib "There is no-one else left to take [him]."
                    wib "You must make your choice."
                    show hand onlayer transient:
                        yalign 0.66#0.743
                        xalign 0.5
                    menu:
                        "Your mother looked around the dark forest in panic."
                        "If she chose the Lord, turn to page 5.":
                            "In desperation, she renounced her foolish pride and sought the protection of the Most High Himself."
                            jump godYes
                        "If she chose the Devil, turn to page 6.":
                            "In desperation, she turned back and sought the protection of the deceiver Himself."
                            jump devilYes
                        "If she chose Death, turn to page 7.":
                            mum "I'm sorry for my foolish words. Please, protect my child."
                            jump deathYes
                        #"If she chose no godparent at all (A reckless choice indeed), turn to page 7.":
                        #    ""
                    # wib "You should have thought of that sooner."
                    # "In one swoop She bowed down and placed Her mark upon you."
                    # wib "You will name [him] [povname]."
                    # if he == "they":
                    #     wib "The moment [he] turn eighteen, [he] will be mine."
                    # else:
                    #     wib "The moment [he] turns eighteen, [he] will be mine."
                    # wib "Keep [him] safe for me until I come for [him]. I will send three messengers before me, to announce my arrival. "
                    # mum "Very well. Beggars can't be choosers, I suppose. Make sure you're there for the christening on Sunday."
                    # show hand onlayer transient:
                    #     yalign 0.77#0.743
                    #     xalign 0.5
                    # "But She was already leaving. She sunk into the earth with Her long, broken legs trailing behind her, until she was swallowed up whole.{vspace=160}{i}In your notes, write down that {b}You are Death's Grandchild.{/b}{/i}"
                    # $godfather = "Black"
                    jump chapter2
                "If she asked the mysterious figure who She was, turn to page 18." if not thirdManWho:
                    mum "I don't know you."
                    wib "Everyone knows me."
                    "She tilted her head so that the moonlight fell upon it, and your mother saw that it was true. The woman was Lady Death Herself."
                    $thirdManWho = True
                    jump thirdMan2
    #label godparentChoose:

# Act 1, Chapter 2: Your Upbringing
label chapter2:
    call hideAll from _call_hideAll_1
    show sunbg at artPos

    if persistent.vanished == 3:
        "And so you grew up alone in an old cottage on stilts in the forest."
        show spirit onlayer transient zorder 100
        "There were many miraculous things in the house. The table was set. The larder was fully stocked. You had plenty of food to survive on."
        "Where did it come from? You couldn't recall."
        "The closets were filled with clothes of all sizes. In the bedroom was a hand-sewn patchwork quilt that fit just right."
        "How did these things come to pass? You didn't trouble yourself with such thoughts. Whenever you encountered these miracles, you simply said:"
        pov "The House provides."
        jump introMenu
    else:
        stop music3 fadeout 6.0
        play music [ "<sync music3>audio/mysteriousHappenings1.wav", "audio/mysteriousHappenings1.wav" ] fadein 1.0

        if godfather == "White":
            "And so you grew up as a kind and well-mannered child, and you made your mother proud."
            "You went to church every Sunday and worked hard every day of your life, and never did you succumb to the beast within. All the neighbours smiled and said \"That one has the mark of G-d upon [him].\""
            "Your Godfather was as good as His word. He appeared at church for the christening, and blessed you."
            "You soon found that luck was always in your favour, and everyone took to calling you \"Fortune's Favourite\"."
        elif godfather == "Red":
            "And so you grew up as a wild and wilful child, and your drove your mother to distraction with your wickedness."
            "You obeyed no laws and no masters, and you roamed heedlessly across the hills and dales, cackling wildly and throwing mud in your wake, and all the neighbours said \"That one has the Devil's mark upon [him],\" and shut their doors."
            #TK: Beast reference from wolf about taboo
            "This so grieved your mother that she fell down dead."
            #"Your Godfather was as good as His word, although He could only watch the christening from outside the church window."
            "In spite of this, you still did not mend your wicked ways. Your ill deeds were rewarded, for you soon found that you could scarcely trip over a stone without unearthing precious diamonds and gems, and you became rich beyond the dreams of avarice."
        elif godfather == "Black":
            "And so you grew up as a solemn and quiet child, and you made your mother sick with worry with your gloomy ways."
            "You ate very little and said even less, and every night you would stalk quietly through the forest shadows or sit for long hours watching insects crawl in stagnant ponds, and all the neighbours said \"That one has the mark of Death upon [him],\" and shut their doors."
        if godfather == "Red":
            if persistent.vanished == 0:
                "You lived with your twelve siblings in a house on stilts on the banks of a muddy river in a vast rainforest."
            elif persistent.vanished == 1:
                "You lived with your ten siblings in a house on stilts on the banks of a muddy river in a vast rainforest."
            elif persistent.vanished == 2:
                "You lived with your four siblings in a house on stilts on the banks of a muddy river in a vast rainforest."
            jump introMenu
        else:
            if persistent.vanished == 0:
                "Your mother loved you very much, and you lived with her and your twelve siblings in a house on stilts on the banks of a muddy river in a vast rainforest. Each night you would fall fast asleep under the patchwork quilt she knitted for you."
            elif persistent.vanished == 1:
                "Your mother loved you very much, and you lived with her and your ten siblings in a house on stilts on the banks of a muddy river in a vast rainforest. Each night you would fall fast asleep under the patchwork quilt she knitted for you."
            elif persistent.vanished == 2:
                "Your mother loved you very much, and you lived with her and your four siblings in a house on stilts on the banks of a muddy river in a vast rainforest. Each night you would fall fast asleep under the patchwork quilt she knitted for you."

            jump introMenu

#The map of the lands near your house
label mapOpens:
    #==This map slowly gets erased as characters vanish

    play sound pageFlip2
    hide map1 onlayer screens
    $renpy.hide_screen(tag="map")
    if persistent.vanished <=2:
        show map1 onlayer screens zorder 100 at truecenter
        if persistent.toadVanished:
            show mapBlankToad onlayer screens zorder 101 at truecenter
        if persistent.witchVanished:
            show mapBlankWitch onlayer screens zorder 101 at truecenter
        if persistent.thiefVanished:
            show mapBlankThief onlayer screens zorder 101 at truecenter
        if persistent.mushroomVanished:
            show mapBlankMushroom onlayer screens zorder 101 at truecenter
        if persistent.vanished >= 2:
            show mapBlankMisc onlayer screens zorder 101 at truecenter
    elif persistent.vanished == 3:
        show mapBlankVillage onlayer screens zorder 100 at truecenter
    elif persistent.vanished == 4:
        show mapBlankHouse onlayer screens zorder 100 at truecenter
    elif persistent.vanished >= 5:
        show mapBlankAll onlayer screens zorder 100 at truecenter
    show hand onlayer transient:
        yalign 0.655#0.743
        xalign 0.5
    "The lands around your house were strange."
    play sound pageFlip2
    #Hide everything
    hide map1 onlayer screens
    hide mapClosed onlayer screens
    hide mapBlankToad onlayer screens
    hide mapBlankWitch onlayer screens
    hide mapBlankThief onlayer screens
    hide mapBlankMushroom onlayer screens
    hide mapBlankAll onlayer screens
    hide mapBlankHouse onlayer screens
    hide mapBlankVillage onlayer screens
    hide mapBlankMisc  onlayer screens


    jump neighbours

#The neighbours near your house
label neighbours:
    $renpy.show_screen("map", _layer="screens", tag="map", _zorder=101)
    show hand onlayer transient:
        yalign 0.655#0.743
        xalign 0.5
    menu:
        "The lands around your house were strange."
        "To learn about the lands to the north, turn to page 10." if not introNeighboursN:
            play sound pageFlip
            $introNeighboursN = True
            hide map1 onlayer screens
            $renpy.hide_screen(tag="map")
            if persistent.thiefVanished == True:
                if (renpy.music.is_playing(channel='music')): 
                    stop music
                    play music2 [ "<sync music>audio/mysteriousHappeningsDist1.wav", "audio/mysteriousHappeningsDist1.wav" ]
                show wolf9 onlayer transient zorder 100
                "To the north, there was nothing and no-one."
                jump neighbours
            else:
                if (renpy.music.is_playing(channel='music2')): 
                    stop music2
                    play music [ "<sync music2>audio/mysteriousHappenings1.wav", "audio/mysteriousHappenings1.wav" ]
                "Do not ask lightly of the northern forest, my child."
                "That was a cursed place where wicked sprites and gleeful ghosts held sway. All who lived there slept uneasily in their beds as they heard the Goblin Train rattle past their windows each night."
                show thief onlayer transient zorder 100
                "The worst of them all was the Master Thief, a dextrous and sinister figure who was said to have all manner of powers."
                "It was said on moonless nights their long, long arms would stretch through your window and up your stairs and into your bedroom and steal your dreams right out from under your pillow. In a single motion their long, long legs would carry them away to a secret hideout where they would place your forgotten thoughts in a sack of mysterious things, never to be seen again."
                "No jail could hold them and no lock could bar them entry."
                "Or so it was said."
                jump neighbours
        "To learn about the lands to the east, turn to page 15." if not introNeighboursE:
            play sound pageFlip
            $introNeighboursE = True
            hide map1 onlayer screens
            $renpy.hide_screen(tag="map")
            if persistent.toadVanished == True:
                if (renpy.music.is_playing(channel='music')): 
                    stop music
                    play music2 [ "<sync music>audio/mysteriousHappeningsDist1.wav", "audio/mysteriousHappeningsDist1.wav" ]
                show wolf8 onlayer transient zorder 100
                "To the east, there was nothing and no-one."
                jump neighbours
            else:
                if (renpy.music.is_playing(channel='music2')): 
                    stop music2
                    play music [ "<sync music2>audio/mysteriousHappenings1.wav", "audio/mysteriousHappenings1.wav" ]
                "To the east, the river flowed down to the coast. The mangrove trees swayed in the summer heat, and the air thrummed with chanting in honour of the insect god, Karnopticon."
                show toad onlayer transient zorder 100
                "On the edge of the swamp was a grand manor, owned by a noble frog lord."
                "He was rarely seen, but people whispered that he was wiser than Solomon and richer than Midas. Kings and prophets would come from across the land to seek his counsel and gaze with envy upon the glittering spires of his house. To buy even a single gem from amoung the hundreds that adorned the manor would bankrupt any one of them."
                "Or so it was said."
                jump neighbours
        "To learn about the lands to the south, turn to page 20." if not introNeighboursS:
            play sound pageFlip
            $introNeighboursS = True
            hide map1 onlayer screens
            $renpy.hide_screen(tag="map")
            #Flowing river to the south, Amazonian, fungi and silver-white - The Mushroom
            if persistent.mushroomVanished == True:
                if (renpy.music.is_playing(channel='music')): 
                    stop music
                    play music2 [ "<sync music>audio/mysteriousHappeningsDist1.wav", "audio/mysteriousHappeningsDist1.wav" ]
                show wolf10 onlayer transient zorder 100
                "To the south, there was nothing and no-one."
                jump neighbours
            else:
                show mushroom onlayer transient zorder 100
                if (renpy.music.is_playing(channel='music2')): 
                    stop music2
                    play music [ "<sync music2>audio/mysteriousHappenings1.wav", "audio/mysteriousHappenings1.wav" ]
                "Ah! In fact, the south river and the forest around it was watched over by a wise mushroom ambassador, who had owned these lands since before anyone could remember."
                "On cold clear nights, you could see her walking through the depths of the forest with her white veil and delicate waves of silver spores drifting behind her."
                "She allowed your family to live on the river and use her lands, under one condition."
                m "Ask not of what concerns you not, lest you hear what pleases you not."
                "Your family accepted her wishes, and so you let each other be."
                "She was often away brokering trade agreements and peace treaties and delicate alliances between the many trees and plants and old warring ferns of the forest."
                "Or so it was said."
                if persistent.vanished >=3:
                    call musicSilence from _call_musicSilence_8
                jump neighbours
        "To learn about the lands to the west, turn to page 26." if not introNeighboursW:
            play sound pageFlip
            $introNeighboursW = True
            hide map1 onlayer screens
            $renpy.hide_screen(tag="map")
            #Mountains to the West, home to devils and witch's sabbaths - Thornton Peak- The Witch
            if persistent.witchVanished == True:
                if (renpy.music.is_playing(channel='music')): 
                    stop music
                    play music2 [ "<sync music>audio/mysteriousHappeningsDist1.wav", "audio/mysteriousHappeningsDist1.wav" ]
                show wolf11 onlayer transient zorder 100
                "To the west, there was nothing and no-one."
                jump neighbours
            else:
                show witch onlayer transient zorder 100
                if (renpy.music.is_playing(channel='music2')): 
                    stop music2
                    play music [ "<sync music2>audio/mysteriousHappenings1.wav", "audio/mysteriousHappenings1.wav" ]
                "None dared venture to the western mountains, for all the lands around it were said to be home to a terrible witch."
                "Her hut lay deep under a secret lake, and she would emerge on moonless nights when the waters of that lake turned still and silver-green."
                "The witches held their Sabbath on the mountain to the east, and when the sky was clear you could see the peak blaze with fire, and the Destroyer himself would emerge to dance in the firelight."
                "Or so it was said."
                if persistent.vanished >=3:
                    call musicSilence from _call_musicSilence_10
                jump neighbours
        "To continue, return to page 9.":
            play sound pageFlip
            hide map1 onlayer screens
            $renpy.hide_screen(tag="map")
            jump introMenu

#You begin to walk to the festival
label introMenu:
    if persistent.vanished >= 3:
        $introMenuSentence = "You woke every morning to silence."
        call musicSilence from _call_musicSilence_11
    else:
        if (renpy.music.is_playing(channel='music2')): 
            stop music2
            play music [ "<sync music2>audio/mysteriousHappenings1.wav", "audio/mysteriousHappenings1.wav" ]
        $introMenuSentence = "You woke every morning to the chorus of birds, and fell asleep every evening to the roaring of crickets."

    show hand onlayer transient:
        yalign 0.68#0.743
        xalign 0.5
    menu:
        "[introMenuSentence]"
        "If you want to know about your neighbours and the lands around your house, turn to page 10." if not introNeighbours:
            if persistent.vanished == 3:
                "Yours was a vast and silent land."
                "At times you could walk for days without seeing another soul."
                "You dared not venture out often. Whenever you did, you felt the pressure of that gigantic emptiness lurking just out of sight like a bottomless ocean, and fled quickly back to the safety of your home."
            elif persistent.vanished == 2:
                "The outside world was quiet. The land lay still."
                "But inside your body, your bones roiled and your flesh threatened riot."
                "At times even your own hands turned against you and scuttled out into the night to cause terrible mischief while you slept, so that you would wake to find strange signs and marks and bites upon them and jewelled rings on each crooked finger."
                "Your skull was haunted by restless ghosts that cradled your brain and forced terrible thoughts into your mind at all hours; the bones in your spine became infested with sprites (which made your back crack in twisted and painful ways all through your long life) the blood in your veins was, of course, only a red water nixie that pulsed throughout your body, constantly seeking escape, and even your soul itself was simply a small shard of G-d, caught inside you and vibrating wildly. Not a single scrap of your own body, mind or soul was actually your own."
                "There was no \"You\". Just a collection of monsters, writhing in borrowed skin."
            elif persistent.vanished == 1:
                "Your world was overrun. It festered. It swarmed."
                "Every tree and lantern and street-corner was teeming with gutterlings, bat-folk, scab-eaters, rounds, lurks, sworlk, nathorn-hobs, lantern-lings, curselings, grimmel-dobbies, fold-overs, whisper kings, hook-takers, the cannibal wind howling 'cross the plains, ghost water pooling luminescent in underground caverns. Every house was haunted and every knife was drawn against the dark."
                "Yet still, there were strange hollow places where nothing lived. No sound escaped the stillness of that lacuna. If anything walked there, it walked alone."
            else:
                "Yours was a many-haunted land, my child."
                "Back in those days you could barely take a step without stumbling over a ghost, gutterling, hook-taker, scab-eater, batfolk or gringe. The earth was overrun. Every house was haunted and the Devil lurked at every crossroad."
                "In fact the whole earth was overrun with trolls, hob-and-lanthorns, gringes, cutties and nisses, boguests, bonelesses, boggleboes, black-bugs and night-bats, clabbernappers, corpse lights, candles and Gabriel-hounds, mawkins, hodge-pochers, korreds, lubberkins, cluricauns, hob-thrushes, tod-lowries, Jack-in-the-Wads, men-in-the-oak, dudmen, yeth-hounds, mormos, changelings, redcaps, colt-pixies, Tom-thumbs, madcaps, scrags, spectres, scar-bugs, shag-foals, Jinny-burnt-tails, dopple-gangers, and apparitions of every shape, make, form, and fashion."
            jump neighbours
        "If you wonder whether you were happy there, turn to page 19." if persistent.vanished >= 1 and not introHappy: #not introHappy and
            $introHappy = True
            if persistent.vanished == 1:
                if godfather == "Red":
                    "Well, it was a rich house, and you had everything you could ever want."
                else:
                    "Well, it was a happy house."
                "The house was always full of chatter from your ten siblings, and you were always cramped for space with all of them around."
                "But still, sometimes you would get a hollow feeling inside you, and walk out of the house to stare into the dark woods beyond."
                "No matter how many people were around you, you felt like something was missing."
                "Every year, on the day before your birthday, the village would throw a twilight festival for no reason anyone could name. On these nights you always felt strange."
                "You would avoid the festival and stare deep into the woods all through the night."
                jump introMenu
            elif persistent.vanished == 2:
                #TK: finish silence.
                "Well, it was a happy home. The house was always full of chatter from your four siblings, and you were always cramped for space with all of them around."
                "But at night, when the others had gone to bed, you felt a latent silence lurking in the house."
                "Underneath the old floorboards. Inside the crooked walls."
                "Waiting for its time to come."
                "Not long now."
                jump introMenu
            elif persistent.vanished == 3:
                call musicSilence from _call_musicSilence_12
                $renpy.music.set_volume(0, delay=15.0, channel=u'ambient1')
                $renpy.music.set_volume(0, delay=15.0, channel=u'ambient2')
                "You lived a contented life. No-one bothered you. The stoop was full of fresh-cut logs for the fireplace. The house had many beds, so that you never lacked for a place to sleep."
                pov "The House provides."
                "You kept yourself busy and distracted as much as you could. But every day there came that terrible time when you finally had to lie down alone in bed."
                "As you lay awake in bed at night, you felt the silence."
                "It lurked behind everything. Like a shadow on the wall of something that you dared not turn around to see."
                "You found yourself leaving the taps going, the fire roaring, keeping the pots and pans rattling just to shut it out. Just so you couldn't hear what lay behind the sound."
                # "It oozed up from between the floorboards and out of the cracks in the walls and slowly poured in from the windows, no matter how much you tried to stop them up."
                # "It had nothing to hide now. It had already won."
                # "Each night the sound of the fire would slowly die until there was nothing left to protect you, and you could do nothing but lie in the endless suffocating abyss of silence, unable to even hear your own breathing, until you mercifully fell asleep."
                $renpy.music.set_volume(1, delay=15.0, channel=u'ambient1')
                $renpy.music.set_volume(1, delay=15.0, channel=u'ambient2')
                jump introMenu
        "To continue the story, turn to page 34.":
            if persistent.vanished >= 3:
                "Soon you could stand it no longer. You knew there would be a festival in town tonight (although you could not have said how you knew this)."
                "You searched the pantry and found a package wrapped up with a coinpurse, along with some bread and meat."
                pov "The House provides."
                #"You gathered up these provisions and reached for the door, but as you took hold of the handle you stopped."
                #"You could feel it outside."
                #"The howling pressure of the vacuum beyond pressed against the door like a physical force, the weight of it paralysing you."
                #"You could not stand the thought of the trip down the empty road to that silent village where no-one lived."
                jump mushroomIntro
            else:
                if godfather == "Black":
                    "Alas, all too soon, the eve of your eighteenth birthday arrived. You set about in wild terror, for you knew that your Godmother would own your immortal soul as soon as the clock struck midnight."
                    "You had no doubt that She would soon send Her three messengers for you, and then take you down to the kingdom of ruin forever."
                else:
                    "Alas, all too soon, the eve of your eighteenth birthday arrived. You set about in wild terror, for you knew that your Godfather would come to take you away as soon as the clock struck midnight, and you had no wish to leave just yet."
                    if godfather == "Red":
                        "The closer the hour grew, the more frantic you became. You knew you would soon pay dearly for all your years of wicked indolence."
                        pov "I know. I'll go to the village festival this eve. There will be travellers there from all over this haunted land. Surely one of them will know how to save me from my terrible fate."
                        "You gathered up your coinpurse, along with some bread and meat for the journey, and resolved to travel until you found a way to escape the Devil."
                    else:
                        mum "You must go to the festival tonight, my child. There will be travellers there from all over this wild earth. Surely one of them will know how to save you from this terrible fate."
                        "She gave you a thick coinpurse, and some bread and meat for the journey."
                        mum "Go! But be careful of strangers, and do not leave the path."
                        show wolf9 onlayer transient zorder 100
                        mum "A terrible wolf lurks out there, in the space between the trees."
                jump mushroomIntro

    label mushroomIntro:
        call hideAll from _call_hideAll_2
        show forestbg at artPos
        show spiral5 onlayer transient zorder 100
        stop music fadeout 6
        "And so you took up your belongings and strode on down the road to the festival."
        if persistent.vanished == 3:
            "The twilight set in. The wet cool mist of the rainforest settled around you."
            "You could see no animals stirring."
            "No birdsong disturbed the peace."
        else:
            "The twilight set in. The crickets and cicadas all around began their chattering and squabbling, and the evening birds began to laugh and trill as the wet cool mist of the rainforest settled around you."
            "The crooked old water-dragons looked sideways at you and plotted their long, slow schemes."
            "A small turtle saw you coming and fled into the water with a splash."

        # Act 1, Chapter 3: The Mushroom.
        #You follow the mushroom and find a bunch of mushroom clones
        if persistent.mushroomVanished == True:
            #play audio wind fadeout 25.0
            call musicSilence from _call_musicSilence_13
            show wolf8 onlayer transient zorder 100
            "In the depths of the woods, you heard nothing."
            "You saw no-one."
            "You were alone."
            "You continued on down the empty road."
            call musicReturn from _call_musicReturn_8
            jump thief1
        else:
            call musicReturn from _call_musicReturn_9
            "As you walked down the road, you saw the wise mushroom moving through the deep darkness of the trees, her pale spores flowing in a fog behind her."
            show hand onlayer transient:
                yalign 0.66#0.743
                xalign 0.5
            menu:
                "In her left hand she held a small lantern, and in her right hand she held a crooked knife stained green."
                "If you followed her, turn to page 25.":
                    "You left the path and followed her from a distance."
                    call hideAll from _call_hideAll_3
                    show stranglerfigbg at artPos
                    "She walked into the towering buttress roots of an ancient strangler fig and cut the vines and swamp flowers from it to reveal a small blue door, inlaid with precious moonstone and intricate engravings."
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
                            call hideAll from _call_hideAll_4
                            show mushroomcavebg at artPos
                            if persistent.thiefVanished:
                                "Inside you were shocked to find the tree completely hollow. A boundless cavern was formed inside it, cold as ice despite the heat outside."
                                "The floor of the cavern was piled with rubies and pearls and glinting onyx and solid gold pieces, larger than your fist."
                                "All across the room you saw lush silks and pillars of precious metals of every type and all manner of riches that would turn the King of Kings green with envy."
                                "The glimmering magenta incense smoke rolled across the room and coated it all in a dark haze, smelling of the most incredible spices and herbs and enchanting odours."
                                "There was no sign of the mushroom anywhere."
                                "In the stillness you heard muffled noises coming from a small black door, deep in the recesses of the cavern."
                                "And the distant echo of some soft sound."
                                "It almost sounded like scratching. In the walls of the chamber."
                                "All at once you remembered the festival, and your Godparent, and the promise you made to your mother. This was no time to be dallying about exploring caverns! You had to find a way to escape your fate before midnight."
                                "Run along now, child."
                                call hideAll from _call_hideAll_97
                                show forest4bg at artPos
                                "You left the cavern at once and continued on towards the festival."
                                jump thief1
                            else:
                                "Inside you were shocked to find the tree completely hollow. A boundless cavern was formed inside it, cold as ice despite the heat outside."
                                "The floor of the cavern was piled with rubies and pearls and glinting onyx and solid gold pieces, larger than your fist."
                                "All across the room you saw lush silks and pillars of precious metals of every type and all manner of riches that would turn the King of Kings green with envy."
                                "The glimmering magenta incense smoke rolled across the room and coated it all in a dark haze, smelling of the most incredible spices and herbs and enchanting odours."
                                m "Oh darling, what are you doing back again?"
                                "The Mushroom popped up, startling you."
                                m "I'm sure I remember telling you quite clearly never to darken my door again."
                                "She looked off to the side."
                                m "Yes, I'm just telling them now. One moment."
                                m "Have some common courtesy, darling, please. I don't barge into {b}your{/b} house looking wild and dishevelled and try to steal the untold riches of {b}your{/b} domain, do I?"
                                m "Not without an invitation, at least."
                                label mushroomWater:
                                    show hand onlayer transient:
                                        yalign 0.63#0.743
                                        xalign 0.5
                                    menu:
                                        m "Out with it, then. What do you want?"
                                        "If you asked for some water, turn to page 33." if mushroomTea:
                                            pov "Just some water would be nice, please."
                                            m "{i}Water?{/i} Really?"
                                            m " How... conventional."
                                            pov "What's wrong with water?"
                                            m "Oh, nothing, nothing. It's fine. If you're into that sort of thing."
                                            m "It's just a bit... derivative, isn't it? A bit played out."
                                            m "You know, \"I'm a lumbering humanoid, I love digesting liquids in order to sustain my bodily functions, dah de dah de dah\", etc, etc. Is this really the type of harmful stereotype we want to play into?"
                                            #m "What are we really trying to {i}say{/i} here?"
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
                                        #TK: "The you with the mask" - change this, the thief's art is no longer wearing a mask
                                        "If you asked about \"The you with the mask\", turn to page 31." if mushroomTea and not mushroomBody:
                                            m "I'm sorry darling, it's been a long day already. I don't have time to explain your body to you. Again."
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
                                            "She looked vaguely around the glittering splendour before you."
                                            m "Oh, this?"
                                            "She dismissed the mountains of jewels with a wave of her hand."
                                            m "I told you. All the wealth of the world falls to us in the end."
                                            $mushroomAllThis = True
                                            jump mushroomWater
                                        "If you apologised for intruding and swore to make amends, turn to page 35." if not mushroomIntruding:
                                            m "My dear, an apology is as good to me as a beard to a turtle-dove."
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
                                            "Naturally you opened the basement door."
                                            call hideAll from _call_hideAll_5
                                            play sound pageFlip
                                            show basementfullbg
                                            ""
                                            play sound pageFlip
                                            call hideAll from _call_hideAll_6
                                            show mushroombasementbg at artPos
                                            "Within, you saw a most terrible sight."
                                            "Seven mushroom corpses hung in the room, dripping black ichor, each being feasted upon by a fat blue-tongued lizard."
                                            "Every one of them was identical to the lady Mushroom herself."
                                            pov "W-what is this?"
                                            m "Fool!"
                                            $mushroomArc +=1
                                            "The mushroom appeared from the earth before you with a terrible crash."
                                            m "You have asked about what concerns you not, and so you will hear what pleases you not!"
                                            $mushroomCurse = True
                                            m "I gave you fair warning, darling. Now all your milk will spoil, all your bread will burn, your socks will always be wet, and you will live in torment for the rest of your days!"
                                            pov "Noooooooo!"
                                            m "Don't say I didn't tell you so."
                                            "You cried out and set about wailing and tearing your clothes to pieces and beating yourself upon the ground in pitiful anguish."
                                            pov "Please, Lady Mushroom, spare me your curse. If you do, I will tell you a story, the likes of which would cause you to go white with astonishment if you were to hear it."
                                            m "Ha! Please."
                                            m "I've talked with the ferns, who saw the dinosaurs rise and fall."
                                            m "I am one with the mosses and lichens of the land who are even older still. I have talked to ancient trees who saw the inferno and the deluge and yet still stand."
                                            show hand onlayer transient:
                                                yalign 0.7#0.743
                                                xalign 0.5
                                            menu:
                                                m "What could you possibly tell me that I don't already know?"
                                                "If you told her about the festival, turn to page 4.":
                                                    pov "I'm on my way to the festival, and there will be people there from all over this cryptic earth. Surely one of them will have a story you haven't heard before."
                                                "If you told her about your Godparent, turn to page 62.":
                                                    if godfather == "White":
                                                        pov "I'm seeking a way to escape being taken by my Godfather, the old man in heaven. Surely the story of my adventure will be unique enough for you."
                                                    elif godfather == "Red":
                                                        pov "I'm seeking a way to escape my Godfather, Lucifer. Surely the story of my adventure will be unique enough for you."
                                                    elif godfather == "Black":
                                                        pov "I'm seeking a way to escape my Godmother, Annihilation. Surely the story of my adventure will be unique enough for you."
                                            "The Mushroom grew quiet as she thought over your proposal, and you prayed to the Most High (May He watch over us always) to deliver you from this terrible situation."
                                            m "Very well, dear. I'll let you go."
                                            m "But be warned: If you fail to return to me this very night with the story you have promised me, then your punishment will be as tenfold."
                                            m "You will be fated to trip over a stone and into the ocean and drown, and when you die, your ghost will come back as a wild dog, and harry your mother and father all day and night, nipping at their heels until they both fall into deep wells and turn into terrible black fish that will lie forever there at the bottom of those pits, moaning weakly and cursing the ungrateful child who brought them such devastation and woe."
                                            #m "All your spoons will stick in your drawers, and your eggs will hatch into foul geese, and your bowls and furniture will roll away down the hills, so that you will have nothing to do but sit on the floor and eat cold porridge with your hands and curse the day you ever decided to cross a mushroom!"
                                            pov "Noooooooo!"
                                            "She struck the ground. It opened before her and she disappeared into it instantly."
                                            "You set about rolling around the floor in even more pitiful devastation and horror than before, tears streaming from your eyes at this terrible curse."
                                            "Finally you were forced to pick yourself up and carry on."
                                            call hideAll from _call_hideAll_7
                                            show forest2bg at artPos
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
                                            m "It's rich. It's bold. It's avant-garde. It may not be what you {i}want{/i} right now, but it is what you {i}need{/i}."
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
                                                m "I'm afraid I don't know if I can help. I know a little about pale-faced Death, but I've never met your Godfather."
                                                "A large grandfather clock in the corner suddenly chimed, and she looked up with a start."
                                                m "Oh dear. Time marches on, even for me."
                                                m "I'm sorry to be so rude but I'd better be off. Come back after the festival, and I may be able to help."
                                                m "Please take care of yourself, dear. All of yourself."
                                                "And before you could reply to this strange remark, she took your cup and ushered you out of the door in an instant."
                                                "You took up your bag and set off down the road once more."
                                                jump thief1
                        "If you went back to the path, turn to page 28.":
                            "You rushed back to the path, worried at any moment that you might be seen."
                            pov "Thank goodness that I know not to ask of what concerns me not! That could have led me to some kind of dangerous and magical adventure!\""
                            "And so you continued on down the path, giving thanks to our Lord for your natural good sense."
                            jump thief1
                #TK: Make this a bit less obvious?
                #"If you turned and walked into the space between the trees, turn to page 40." if persistent.vanished >=1:
                    #jump woodsInvestigate
                "If you ignored her and followed the path like an honest Christian, turn to page 42.":
                    "You turned and kept on walking down the path, just as your mother taught you."
                    jump thief1
                "If you turned and walked into the space between the trees, turn to page 40." if persistent.vanished >=3:
                    $wanderAttempted = True
                    "You ignored the mushroom and walked deeper and deeper into the woods."
                    jump woodsInvestigate


    # Act 1, Chapter 4: The Thief.
    label thief1:
        call hideAll from _call_hideAll_8
        show forest4bg at artPos
        if persistent.thiefVanished and not persistent.mushroomVanished:
            #play audio wind fadeout 25.0
            call musicSilence from _call_musicSilence_14
            show wolf7 onlayer transient zorder 100
            "In the depths of the woods, you heard nothing."
            "You saw no-one."
            "You were alone."
            "You continued on down the empty road."
            call musicReturn from _call_musicReturn_10
            jump toadIntro
        elif persistent.thiefVanished and persistent.mushroomVanished:
            jump toadIntro
        else:
            call musicReturn from _call_musicReturn_11
            "As you were walking down the road thusly, you came upon an old beggar-woman."
            "Her eyes were blind, and her back was crooked in 5 directions at once, and her hair floated all around her head like twisting grey fog, and she hobbled about with only the aid of an old cane to help her along."
            if persistent.vanished == 3:
                mys "... "
                mys "Sorry, uh - Ho! Young Traveller!"
            #mys "Ho, young traveller."
            show hand onlayer transient:
                yalign 0.695#0.743
                xalign 0.5
            menu:
                mys "Might you lend a hand for a frail old woman? The woods are dark tonight, and I thought I heard howling from the space between the trees."
                #TK: Include option to kick over the old woman if you're the devil child
                "If you helped the old woman, turn to page 73.":
                    label thiefAccept:
                        $thiefArc +=1
                        $stuffStolen = True
                        "You took the old woman's arm to support her weight."
                        mys "FOOOOOL!"
                        "In a flash her clothes tore asunder, and her mask fell to the ground, and you saw it was all nothing but a disguise."
                        "In her stead stood the cunning and terrible form of the Master Thief!"
                        if persistent.mushroomVanished:
                            "Their hands shook under their midnight cloak."
                        else:
                            "They wore a midnight cloak across their back and a cunning look on their sly face."
                        t "That's right, it's me! Back again to steal your heart and tear this land asunder!"
                        if persistent.mushroomVanished:
                            show wolf1 onlayer transient zorder 100
                            t "They'll never catch me, no matter how they try. I have placed my head in the wolf's mouth and never felt the sting of its coiling jaws."
                            t "I have stolen fire and cheated death. I will live forever. There's nothing you can do to stop me now."
                            "They laughed a high, feverish laugh and ran into the forest and out of sight."
                        else:
                            t "No law shall stand and no magistrate shall ever know peace, for as long as my legs can run!"
                            "And with a shout of laughter they demonstrated this, running their long legs into the forest and out of sight."
                        "As soon as you tried to chase them you discovered that your clothes had been stolen off your back and replaced with origami paper replicas. Your belt was now a strip of seaweed, your socks were old moss, and you were wearing someone else's shoes."
                        label thiefChase:
                            show hand onlayer transient:
                                yalign 0.68#0.743
                                xalign 0.5
                            menu:
                                "Despair gripped you."
                                "If you chased after them anyway, turn to page 37.":
                                    "You chased after the mocking laughter of the Master Thief, tripping over your mismatched shoes. The shadowy figure darted through the trees as they shed disguises, wigs, belts, and the old cane."
                                    "Finally, you caught up to the figure in a forest clearing, and grabbed it tight."
                                    if godfather == "White":
                                        pov "Now you will face your just punishment, sure as the heavens declare the glory of G-d."
                                    elif godfather == "Red":
                                        pov "You wretched fool. You should never have tried to out-do me in wickedness."
                                    else:
                                        pov "I have my grip on you now, sure as Death has Her hand on us all."
                                    "You threw the figure to the ground, laughing in triumph."
                                    "But as soon as you did so, you realised it was nothing but a pig, wearing a wig and the ragged cloak of the old woman."
                                    "The Master Thief was gone."
                                    label thiefchase2:
                                        show hand onlayer transient:
                                            yalign 0.69#0.743
                                            xalign 0.5
                                        menu:
                                            "Seeing your misfortune, the pig oinked at you sorrowfully and nuzzled you for comfort."
                                            "If you kept the pig, turn to page 53.":
                                                "You picked up the pig and held it under the crook of your arm."
                                                show hand onlayer transient:
                                                    yalign 0.743#0.743
                                                    xalign 0.5
                                                "From that day on he would always be your loyal friend and ally, and the two of you would get through more scrapes and misadventures than I have time to relate tonight.{vspace=100}{i}In your notes, write down that you {b}have a pig.{/b}{/i}"
                                                $pig = True
                                            "If you let the pig run free and wild, as nature intended, turn to page 8.":
                                                "With sorrow, you removed the cloak and wig, and gave the pig his freedom."
                                                "He oinked joyfully and fled off into the night. From there, he joined with the wild bush pigs, and founded a crooked kingdom that was as a scourge upon the earth."
                                                "Cruel indeed was the pig king, and countless innocents fell before his terrible iron hooves."
                                                "In the years to come, you would curse your impetuous decision to let that devil-pig free many times."
                                                "But that is a story for another day."
                                            "If you shouted \"Noooooooooooo!\" more pitifully than ever before, turn to page 48."  if pitiful == 4:
                                                pov "{b}{i}NOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                                OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                                OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                                OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                                OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                                OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                                OOOOOOOOOOOOOOOOOOOOOOOOOOOOO!{/b}{/i}"
                                                "The birds of the forest took off in great clouds all around you at the pitiful sound."
                                                $pitiful +=1
                                                jump thiefchase2
                                "If you shouted \"Noooooooooooo!\" pitifully, turn to page 45." if pitiful == 1:
                                    pov "Noooooooooooo!"
                                    $pitiful +=1
                                    jump thiefChase
                                "If you shouted \"Noooooooooooo!\" again, even more pitifully, turn to page 46." if pitiful == 2:
                                    pov "NOOOOOOOOOOOOOOOOOOOOOOOOOOOO!"
                                    $pitiful +=1
                                    jump thiefChase
                                "If you shouted \"Noooooooooooo!\" again, as pitifully as one can shout, turn to page 47."  if pitiful == 3:
                                    pov "NOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                    OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                    OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                    OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                    OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                    OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                                    OOOOOOOOOOOOOOOOOOOOOOOOOOOOO!"
                                    "Your cry echoed through the forest."
                                    $pitiful +=1
                                    jump thiefChase
                                "If you let them go, turn to page 27.":
                                    "You walked sorrowfully back to the road, cursing Old Gooseberry for your misfortune."
                        show hand onlayer transient:
                            yalign 0.8#0.743
                            xalign 0.5
                        "As you trudged back to the road you discovered that all of your coins had been stolen and replaced with I.O.U.'s, the bread was now nothing but crumbs, and the meat had been turned into a live possum with a note on it saying \"Ham\". It bit you and fled into the trees.{vspace=100}{i}In your notes, write down that {b}Your things have been stolen.{/b}{/i}"
                        if godfather == "White":
                            "And so you set about wailing and beating the ground and tearing at your paper clothes, crying out saying \"Oh Lord, how could you treat your servant thus?\""
                            "After a long time you drew yourself up from the ground and spoke to the trees."
                            pov "Hear me now, Thief. With the Lord as my witness, I will not rest until you see justice."
                        if godfather == "Red":
                            "And so you set about wailing and beating the ground and tearing at your paper clothes, crying out saying \"Oh my Lord and Master, the Father of Lies, how could you forsake me? I, who have outdone all others in wickedness, and served you faithfully in evil for all these long years?\""
                            "After a long time you drew yourself up from the ground and spoke to the trees."
                            pov "Hear me now, Thief. My Godfather is the Devil, and my blood runs with nothing but spite, and I will not rest until the Prince of Darkness fastens His hands around your ankles and drags you straight down to Hell where you belong."
                        if godfather == "Black":
                            "And so you set about wailing and beating the ground and tearing at your paper clothes, crying out saying \"Lady Death, take me now!\""
                            "After a long time you drew yourself up from the ground and spoke to the trees."
                            pov "Hear me now, Thief. My godmother is the end of all things, and I will not rest until you have been dragged down into Her icy waters where you belong."
                        if mushroomArc >=2:
                            "But there was nothing to be done for now, and so you tightened your seaweed around your waist and set off once more for the festival. Now you had two dire tasks ahead of you: retrieve a story for the Mushroom and visit vengeance upon the Master Thief."
                        else:
                            "But there was nothing to be done for now, and so you tightened your seaweed around your waist and set off once more for the festival, vowing vengeance upon the Master Thief."

                        jump toadIntro
                "If you refused to aid her, turn to page 44.":
                    label thiefRefuse:
                        pov "I'm sorry ma'am, but I cannot help you. I've been told not to talk to strangers."
                        "\"Bah!\" cried the older woman, and stomped her foot on the ground."
                        "In a flash her clothes tore asunder, and her grey hair fell to the ground, and you saw it was all nothing but a disguise."
                        "In front of you stood the cunning and terrible form of the Master Thief!"
                        "They had long, long legs and thin dextrous fingers that twisted in arcane motions around them."
                        if persistent.mushroomVanished:
                            "Their hands shook under their midnight cloak."
                        else:
                            "They wore a flowing midnight cloak across their back and a cunning look on their sly face."
                        t "You may have outwitted me this time, but I'll get you yet!"
                        if persistent.mushroomVanished:
                            show wolf1 onlayer transient zorder 100
                            t "They'll never catch me, no matter how they try. I have placed my head in the wolf's mouth and never felt the sting of its coiling jaws."
                            t "I have stolen fire and cheated death. I will live forever. There's nothing you can do to stop me now."
                            "They laughed a high, feverish laugh and ran into the forest and out of sight."
                        else:
                            t "No law shall stand, no magistrate shall know peace and no lawman shall sleep easy in his bed, for as long as my legs can run!"
                            "And with a click of their heels they rushed away into the shadows of the woods."
                        "\"Praise the Lord,\" you said to yourself, \"that I know not to help mysterious old women!\""
                        "(A wise habit. Once you've given someone a hand, they'll take your arm.)"
                        "And so you continued on down the path, giving thanks to our Lord for your natural good sense."
                        jump toadIntro
                "If you turned and walked into the space between the trees, turn to page 40." if persistent.vanished >=1 and not wanderAttempted:
                    $wanderAttempted = True
                    if persistent.vanished >=2:
                            show noteListen onlayer transient zorder 100
                    mys "Wait, please! Surely you'll help a poor old woman?"
                    #mys "These woods grow dark swiftly. And they say a beast haunts them."
                    #TK: double check that the copying of this is all correct
                    if persistent.vanished >=2:
                        show noteSay onlayer transient zorder 100
                    show hand onlayer transient:
                        yalign 0.72#0.743
                        xalign 0.5
                    menu:
                        mys "I don't think you want to go that way. These woods grow dark swiftly."
                        #TK: Include option to kick over the old woman if you're the devil child
                        "If you helped the old woman, turn to page 73.":
                            jump thiefAccept
                        "If you refused to aid her, turn to page 44.":
                            jump thiefRefuse
                        "If you continued to walk into the woods, turn to page 41.":
                            call hideAll from _call_hideAll_106
                            show darknessbg at artPos
                            "Without a word, you left the old woman behind and walked deeper and deeper into the woods."
                            jump woodsInvestigate


    # Chapter 1, Part 5: The Toad.
    label toadIntro:
        call hideAll from _call_hideAll_9
        show forest5bg at artPos
        if persistent.toadVanished and not persistent.thiefVanished:
            #play audio wind fadeout 25.0
            call musicSilence from _call_musicSilence_15
            show wolf1 onlayer transient zorder 100
            if pig:
                "In the depths of the woods, with the pig trotting beside you, you heard nothing."
                "You saw no-one."
                "You were alone."
                "You continued on down the empty road."
            else:
                "In the depths of the woods, sweating in the warmth of the summer night, you heard nothing."
                "You saw no-one."
                "You were alone."
                "You continued on down the empty road."
            call musicReturn from _call_musicReturn_12
            jump chapter6
        elif persistent.toadVanished and persistent.thiefVanished:
            jump chapter6
        else:
            call musicReturn from _call_musicReturn_13
            if pig:
                "As you walked down the road with the pig trotting beside you, you heard the thunder of hooves, and turned to see four horses pulling a magnificent golden carriage."
            else:
                "As you walked down the road, sweating in the warmth of the summer night, you heard the thunder of hooves behind you, and turned to see four horses pulling a magnificent golden carriage."
            "The horses were pure white, with intricate porcelain and shining bridles made of fine-spun ropes laced with gold."
            "The carriage door was open to show a curtain of lush red silk, and behind the curtain you could see the shadow of a lean and graceful figure of noble bearing."
            if persistent.vanished == 3:
                eg "Hold!"
                "There was a long pause."
                "You stood beside the carriage in an uncertain silence."
                eg "I..."
                eg "I forget what I'm supposed to say now."
                "His words came slowly. He seemed to be having difficulty speaking."
                pov "You're supposed to say, \"Where are you headed, fellow traveller?\""
                "The figure nodded gratefully."
                show hand onlayer transient:
                    yalign 0.63#0.743
                    xalign 0.5

            else:

                eg "Hold!"

                "A rich, low voice like dark mahogany came from behind the curtains, showing the distinctive tones of one of good breeding and character. The horses slowed to walk beside you."
                "A slender hand grasping a long cigarette holder emerged from the curtains and beckoned to you. The shadow of the man inside swirled a glass of brandy in his other hand."
                "From inside the curtain you could smell rich spices, incense and thyme."
                show hand onlayer transient:
                    yalign 0.63#0.743
                    xalign 0.5
                #Change: More impact from this choice. More mysterious and interesting sounding locations.
            menu:
                eg "Where are you headed, fellow traveller?"
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
                "Your pig sniffed at the carriage suspiciously."

            show wolf1 onlayer transient zorder 100
            show hand onlayer transient:
                yalign 0.7#0.743
                xalign 0.5
            menu:
                eg "This is no night to be walking out alone. Haven't you heard there's something in these woods?"
                "If you accepted the lift, turn to page 54." if mushroomArc ==0 or thiefArc ==0:
                    label toadAccept:
                        #if persistent.vanished==3:
                            #TK: Finish the toad last alive route
                        #    "You stepped up into the carriage."
                        #    "Inside, of course, was the toad."
                        #    f "So. To the... place?"
                        #    pov "Yes. To the village."
                        #    "He pulled the reins, and you rode on together in silence."
                        #    f "The, uh... the place, the house place."
                        #    "The toad tried to talk, but his words did not make sense. He couldn't find the words for everyday objects."
                        #    pov "Shh, shh. It's ok."
                        #   "You sat together in silence."
                        #   "The
                        #else:
                        $toadArc +=1
                        if pig:
                            "You reached up to take the gentleman's hand, and he whisked you and the pig into the carriage."
                        else:
                            "You reached up to take the gentleman's hand, and he whisked you into the carriage."
                        "The moment you were through the curtain you realised something was wrong."
                        "Instead of the graceful and elegant nobleman you expected, you discovered a small, ugly cane toad."
                        "The incense you smelled was nothing but the reek of dirt and mud, the brandy was pond scum, the gleaming carriage was just a rotten old squash, and the graceful arm that beckoned you from behind the curtain was nothing but a wooden prop the toad held in his bulging hand."
                        "You turned to run, but it was too late. With a clap, the toad commanded his steeds."
                        f "Prickle! Crawl! Shudder and Clink! Don't tarry or stall, get us there in a wink!"
                        "The brilliant white horses tore off their clothes and revealed themselves to be a crow-shrike, a rat, a bat and an old black cockatoo."
                        "They cackled and gibbered to each other as they raced off down the road with you, bumping and rolling and pulling apart pinecones and causing terrible devastation as they went."
                        if pig:
                            "You clutched your pig close, and you both shivered in terror at the unforeseen calamity that had befallen you."
                        #Change: ADD CHOICE
                        show hand onlayer transient:
                            yalign 0.66#0.743
                            xalign 0.5
                        menu:
                            f "Well, are you impressed?"
                            "If you asked the gentleman his name, turn to page 58.":
                                f "No doubt you've heard of me."
                                f "I am Brildebrogue Chippingham, and I have never failed at anything in my life."
                            "If you flattered the toad, turn to page 63.":
                                pov "Absolutely, sir. I'm stunned."
                                f "Only natural."
                                f "I find it's better to conceal my true nature from the common-folk."
                                f "Were they to see the incandescent beauty of my true visage at first sight, I dare say they would fall to their knees and wail in shock, so transfixed would they be."
                                f "I would never be able to get anywhere without them pawing at me and offering me their baked goods and falling about in ecstasy, you know how these people are."
                                f "But you, I believe, have sufficient grace to withstand the urge."
                            "If your notes say that {b}You are the Devil's Godchild{/b}, turn to page 65." if godfather=="Red":
                                $toadStole = True
                                pov "Sir, you've made one mistake. Never tangle with the spawn of the Devil."
                                if pig:
                                    "With a single motion you stole all the valuables you could grab and leapt from the moving carriage with the pig like a holy terror, tumbling onto the road below."
                                else:
                                    "With a single motion you stole all the valuables you could grab and leapt from the moving carriage like a holy terror, tumbling onto the road below."
                                f "What the - stop! Thief!"
                                "But it was too late. You were already away and running into the woods, laughing with impish glee."
                                show hand onlayer transient:
                                    yalign 0.743#0.743
                                    xalign 0.5
                                "You looked down at your haul and found that you'd managed to swipe a lovely emerald brooch in the shape of a dragonfly.{vspace=170}{i}In your notes, write down that {b}You have an Emerald Brooch.{/b}{/i}"
                                "You hid it in your pocket and went on your way."
                                jump chapter6
                        show hand onlayer transient:
                            yalign 0.67#0.743
                            xalign 0.5
                        menu:
                            f "So, what brings you travelling this way?"
                            "If you told the toad about your Godparent, turn to page 67.":
                                if godfather == "White":
                                    pov "I'm searching for a way to escape my Godfather, the King of Kings."
                                    pov "He will be here to take me away at midnight, and I have no wish to leave."
                                    f "A sticky situation indeed!"
                                    f "I have talked with the Lord many times, of course."
                                    show tornPage1 onlayer screens zorder 101
                                    show tornPage1bg onlayer screens zorder 99
                                    f "Why, just the other day He said to me, He said Brildebrogue! How did I ever manage to make one as handsome and charming as you? Why, even a deity with my own talents (which are quite decent of course, though nothing in comparison to your own gifts) can scarcely imagine bringing such a golden figure out of the fires of creation! At this I swung back my head in a mighty guffaw, like so: HA! And my golden mane whipped about me in the wind, and all were charmed by my wit and good humour, so much so that they joined me in an uproarious shout of laughter, such that the whole world could hear it - in fact I have no doubts that you must have heard it yourself, even out here in this backwater location, so loud was the sound, although perhaps you took it for a minor earthquake."
                                    hide tornPage1 onlayer screens
                                    hide tornPage1bg onlayer screens
                                    f "Perhaps I could put in a good word for you with Him later. Pond scum?"
                                if godfather == "Red":
                                    pov "I'm searching for a way to escape my Godfather, Old Scratch."
                                    pov "He will be here to take me away at midnight, and I have no wish to leave."
                                    f "A sticky situation indeed!"
                                    f "I know the Black One well myself, in fact."
                                    show tornPage2 onlayer screens zorder 101
                                    show tornPage2bg onlayer screens zorder 99
                                    f "Why just the other day I said to Him, I said Devil! How dare you twist the lives of these innocent souls here, tricking them into a terrible life of debauchery and ill-humour, just to suit your own devious and ill-conceived personal goals, when you could instead behave yourself and simply put things to rights like a well-mannered member of society such as myself? At my words, He shrank back with a most timiditous cowardice, and I saw Him gulp in nervous anxiety most profound, such was His fear of my fury (which can be quite considerable when my dander is up, although of course I take care to remain in good humour for the purpose of conversing with polite gentlefolk such as yourself). In an instant, He swore never to do evil again, and scurried away over hill and dale without a backwards glance."
                                    hide tornPage2 onlayer screens
                                    hide tornPage2bg onlayer screens
                                    f "Perhaps I could put in a good word for you with Him later. Pond scum?"
                                if godfather == "Black":
                                    pov "I'm searching for a way to escape my godmother, the Reaper."
                                    pov "She said she will soon send 3 messengers, and then take me away. But I have no wish to leave just yet."
                                    f "A sticky situation indeed!"
                                    f "Why, that reminds me of the situation when my own dear old mother was about to die."
                                    show tornPage1 onlayer screens zorder 101
                                    show tornPage1bg onlayer screens zorder 99
                                    f "I've chatted with Death many times, of course, and so on this occasion I marched right on up to Her and said \"Unhand my mother, you ruffian! I cannot allow you to continue this wave of terror you have inflicted across the forest left and right, taking away women and old maids and children at will, rich and poor alike, before their time has come to pass! Release her at once, or I'll have to get extremely unpleasant with you (And you do NOT wish to see me when I'm being unpleasant, I assure you (Such a thing has driven many hard men to tears!)) At this stern talking-to from me, She released my mother at once with a sincere apology, and I need hardly say that She has not darkened our door again."
                                    hide tornPage1 onlayer screens
                                    hide tornPage1bg onlayer screens
                                    f "Perhaps I could put in a good word for you with Her later. Pond scum?"
                            "If you remained vague about your true plans, turn to page 71.":
                                pov "Just... travelling, I suppose."
                                f "Fantastic! Nothing better than a spot of travelling. I've done quite a bit in my day, let me tell you."
                                show tornPage3 onlayer screens zorder 101
                                show tornPage3bg onlayer screens zorder 99
                                f "Why just the other day I travelled to the living city of Brilochiorp, built on a turtle's back, where your dreams cast shadows and your thoughts chase after you in the mid-afternoon sun. I was there to discuss matters with the queen of the dream thieves, you see, a rascally beggar who had been running about the city filching this dream and that right out of the heads of the poor citizens, so that they dreamed nothing and had no ideas and the city's art and culture stagnated to nothing! Well, we can't have this sort of thing going on, Brilebrogue, I said to myself, and so I paid the blighter a visit and gave her a stern talking-to, and no mistake. She renounced his ways in an instant and placed all the dreams back exactly where he found them, promising to reform her ways and be a better woman. Another successful adventure, all told."
                                hide tornPage3 onlayer screens
                                hide tornPage3bg onlayer screens
                                f "But I'm sure your little festival will be quaint, too. Pond scum?"
                            "If you said nothing, turn to page 74.":
                                f "No bother, then, keep your secrets to yourself."
                                show tornPage3 onlayer screens zorder 101
                                show tornPage3bg onlayer screens zorder 99
                                f "I myself am excellent at keeping secrets. Why, just the other day the Brass Magician of the City of Pale Stones said to me, he said Brildebrogue! Can I trust you with a most powerful and deadly secret, such that it would destroy the heavens if it were to be released? Of course I gave him my assurances immediately, and thus he told me that the devil's seven daughters were locked below the city in chains, and could only be released with the most secret and magical word, \"Grolabicon\"! Of course if this were ever to be discovered and the daughters released, they would wreak such terrible havoc on the world as to bring the Firmament crashing down from Her place up above, and it would be the seventh and final apocalypse come at last, which is why I gave him my word that I would keep the secret safe as houses, and I have never told anyone of the matter to this day."
                                hide tornPage3 onlayer screens
                                hide tornPage3bg onlayer screens
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
                                pov "No thank you."
                                f "More for me, then!"
                                "And the toad greedily gulped down the pondwater, without comment on your obvious poor manners and lack of breeding."
                        "The old squash rattled about hither and thither through the forest, giving you bruises all over, but before you knew it you had arrived at the village square."
                        "The toad rose out of his seat, leapt out through the curtains, and with a flourish offered his hand to help you down the carriage steps (which were made of old shoe-leather)."
                        if pig:
                            "The pig trotted down after you, looking disgruntled."
                        f "There you are!"
                        f "Thank you for the wonderful company, and I wish you the best of luck with the festival!"
                        jump chapter6
                #tk check
                "If you refused the lift, turn to page 55.":
                    if mushroomArc >=1 and thiefArc >=1:
                        "Your experiences with the Mushroom and Thief had instilled a wise caution within you, and you could not accept the gentleman's offer."
                    label toadRefused:
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
                        pov "Well! It's a good thing I know not to accept lifts from strange gentlemen."
                        "(A wise habit. The Lord knows this world is full of cheats and liars.)"
                        jump chapter6
                "If you turned and walked into the space between the trees, turn to page 40." if persistent.vanished >=1 and not wanderAttempted:
                    $wanderAttempted = True
                    if persistent.vanished >=2:
                            show noteListen onlayer transient zorder 100
                    eg "W-wait! Where are you going?"
                    if persistent.vanished >=2:
                        show noteSay onlayer transient zorder 100
                    show hand onlayer transient:
                        yalign 0.67#0.743
                        xalign 0.5
                    menu:
                        eg "You can't just go off alone. These woods aren't safe."
                        "If you accepted the lift, turn to page 54.":
                            jump toadAccept
                        "If you refused the lift, turn to page 55.":
                            jump toadRefused
                        "If you continued walking deeper into the woods, turn to page 41.":
                            call hideAll from _call_hideAll_126
                            show darknessbg at artPos
                            "Without a word, you left him behind and walked deeper and deeper into the woods."
                            jump woodsInvestigate

    #---- Act 1, Chapter 6: The Village.
    label chapter6:
        if mushroomArc == 0 and thiefArc == 0 and toadArc == 0:
            if godfather == "Red":
                "And so it was that you stayed on the path the whole way, ignoring your wanton nature and never once being tempted by the offers of strangers."
            else:
                if persistent.mumVanished:
                    "And so it was that you stayed on the path the whole way."
                else:
                    "And so it was that you stayed on the path the whole way, following your mother's advice and never once being tempted by the offers of strangers."
            if not persistent.mumVanished:
                "(Some protagonist you turned out to be.)"
            call hideAll from _call_hideAll_10
            show townextbg at artPos
            jump witch1
        else:
            call hideAll from _call_hideAll_11
            show townextbg at artPos
            "And so you finally arrived at the village."
        "The rich dark blanket of night was softly rolling over the town, and cooking fires lit up all across the hills, one by one."
        jump villageExplore1

    label witch1:
        #TK: add choices here
        show scribble4 onlayer transient zorder 100

        if persistent.witchVanished == True or persistent.hVanished == True:
            call musicSilence from _call_musicSilence_16
            show wolf11 onlayer transient zorder 100
            "As you walked up to the village, no-one greeted you."
            "The woods were silent."
            "You slowly walked out of the woods and into the village streets."
            call musicReturn from _call_musicReturn_14
            jump villageExplore1
        else:
            call musicReturn from _call_musicReturn_15
            "As you walked up to the village, you spied a hunter standing guard."
            h "Good evening."
            show hand onlayer transient:
                 yalign 0.68#0.743
                 xalign 0.5
            menu:
                h "Be careful tonight. They say there's witches abroad."
                "If you said there's no such thing as witches, turn to page 38.":
                    pov "Witches? Nonsense! There's no such thing!"
                    "No sooner had those foolish words escaped your mouth than a witch leapt out of the bushes and onto your back. Before you could say or do anything, she dug her heels into your sides and rode you up into the sky and over the mountains."
                    if pig:
                        "The pig squealed in shock down below, and quickly vanished from view."
                    $witchArc +=1
                    call hideAll from _call_hideAll_12
                    show mountainsbg at artPos
                    "In a wink you found yourself at Thornton Peak, exhausted from hard riding."
                    play sound pageFlip
                    show sabbathfullbg
                    ""
                    play sound pageFlip
                    call hideAll from _call_hideAll_13
                    show mountainsbg at artPos
                    "A witches Sabbath was afoot. A spitting bonfire raged on the peak before you, and the witches danced before it."
                    show witches onlayer transient zorder 100
                    "The old baba yagas cackled and jibbered and danced around you with glee, poking you cruelly in your sides and making cutting remarks like, \"Now who's not real, eh?\" and \"We don't believe in YOU! How do you like that?\" which wounded your feelings most grievously."
                    w "Oh gosh, oh no, are you all right?"
                    "A figure pulled you away from the jeering crowd and tended to your wounds."
                    w "I'm so sorry about that. The old girls tend to get a bit carried away. They don't get out much, you know, it's a bit of a treat for them."
                    w "Are you feeling ok? Let me get you up. I'm so sorry about this, I know this is probably the last thing you want to be doing on a Friday night, really can't apologise enough, it's just the full moon, you know? Always gets them a bit riled up, and it does them good to get some fresh air and dance around once in a while, you know, fulfil their oath to the devil, but, no excuses for kidnapping you obviously, that kind of behaviour is really not on."
                    w "Here, let me give you a lift home."
                    "She helped you get up on her broom and spirited you away into the sky."
                    "Below you, you heard the witches you chanting praise to Belphegor, lord of Hogs."
                    w "So."
                    w "Been out here often?"
                    #TK: Choice
                    pov "Not often, no."
                    w "Oh, it's lovely, you should definitely try coming back when you have a chance. Beautiful views."
                    "An explosive crack split the air. You twisted around to look back. Behind you, you saw the mountain split open and ten thousand hogs burst up from beneath the earth. The witches screeched in demonic glee."
                    w "Oh dear. I'm going to miss everything."
                    w "Alright, here you are. I'd better be getting back."
                    w "Have a good night!"
                    "She set you down at the edge of town and flew off into the sky."
                    if pig:
                        "The pig jumped up at you, and the two of you had a tearful reunion."
                    call hideAll from _call_hideAll_14
                    show townextbg at artPos

                    "The rich dark blanket of night was softly rolling over the village, and cooking fires lit up all across the hills, one by one."
                    jump villageExplore1
                "If you trembled in terrible fear, turn to page 39.":
                    "You looked around in fright. The bushes rustled. But you saw no witches."
                    pov "Thank you for the warning, kind hunter. I'll be careful."
                    "You walked into town."
                    "The rich dark blanket of night was softly rolling over the village, and cooking fires lit up all across the hills, one by one."
                    jump villageExplore1
                "If you turned and walked into the space between the trees, turn to page 40." if persistent.vanished >=1 and not wanderAttempted:
                    $wanderAttempted = True
                    if persistent.vanished >=2:
                            show noteListen onlayer transient zorder 100
                    h "Hold on. The festival is about to start."
                    if persistent.vanished >=2:
                        show noteSay onlayer transient zorder 100
                    show hand onlayer transient:
                        yalign 0.67#0.743
                        xalign 0.5
                    menu:
                        h "You'd better not wander off. You'll be late."
                        "If you entered the village, turn to page 39.":
                            pov "Thank you for the warning, kind hunter."
                            "You walked into town."
                            "The rich dark blanket of night was softly rolling over the village, and cooking fires lit up all across the hills, one by one."
                            jump villageExplore1
                        "If you continued walking deeper into the woods, turn to page 41.":
                            call hideAll from _call_hideAll_127
                            show darknessbg at artPos
                            "Without a word, you left the hunter behind and walked deeper and deeper into the woods."
                            jump woodsInvestigate

    label villageExplore1:
        if persistent.vanished >= 3:
            $renpy.music.set_volume(0.9, delay=3.0, channel=u'ambient1')
            $renpy.music.set_volume(0.9, delay=3.0, channel=u'ambient2')
            $renpy.music.set_volume(0.9, delay=3.0, channel=u'music')
            "The village was empty."
            "The decorations were all set. The great bonfire. The chairs and stacked tables, laden with plates. Streamers lay over the road."
            "But the chairs were all vacant. The piles of food lay undisturbed on the tables - not even flies ventured near. The sound of the crackling bonfire echoed through deserted streets."
            jump village
        else:
            play music adventure1
        show hand onlayer transient:
            yalign 0.728#0.743
            xalign 0.5
        menu:
            "The town was overflowing with people bustling about and preparing for the festival, pulling up chairs and laying stacked tables around the enormous bonfire in the centre of town."
            "If you looked at the food, turn to page 36." if not foodLook:
                call hideAll from _call_hideAll_15
                show towncrossroadsbg at artPos
                $foodLook = True
                "Over the bonfire was a thick suckling pig on a spit, slathered in rosemary and garlic butter and herbs of all types, and stuffed with breadcrumbs and fresh figs and crisp walnuts and apples and all the fruits of the earth."
                if pig:
                    "Your pig looked upon it sadly, and shook its head at the foolish greed of the human race."
                "The mangos were in season, and the trees were so weighed down with them that they would fall off and roll down the town gutters, so that the whole town was rich with the sweet scent of fruit mixed with the smell of wood smoke and spices and crackling fat from the cooking fires."
                "Those mangos that didn't roll away fast enough were plucked up immediately and eaten by gleeful clouds of fruit bats that chittered and cackled in whirling chaos overhead."
                "Colossal glass bowls of red sangria were placed at each table, filled with fresh oranges and giant yellow lemon slices, ground cinnamon and brandy and crisp sweet apples and ginger ale."
                "For dessert there were giant lemon meringue pies made from lemons as big as your fist, covered in fresh-whipped meringue from the Baker's parlour."
                jump villageExplore1
            "If you sat down with the rest of the guests without delay, turn to page 37.":
                call hideAll from _call_hideAll_16
                show towncrossroadsbg at artPos
                "You took your place at the table. All the villagers were there."
    if not persistent.hVanished:
        "The cunning hunter."
    if not persistent.goVanished:
        "The young goose-girl with her unruly geese."
    if not persistent.gmVanished:
        "The old gloom-monger."
    if not persistent.mayVanished:
        "The town mayor."
    if not persistent.toadVanished:
        " Even the warty old toad you met on the road."
    show spiral6 onlayer transient zorder 100
    if persistent.starsVanished:
        "The birds and moths and the soft mist of night all came and were seated."
    else:
        "The stars and the moon slowly arrived to take their places. The birds and moths and the Firmament and the soft mist of night all came and were seated."
    if not persistent.witchVanished:
        "But one guest was missing: No one had seen the Wild Witch of the Woods all night."
        "As the festival began a terrible concern and commotion went up amongst the guests, for we all know what terrible luck it is to spurn a witch."
        if not persistent.mayVanished:
            may "Did her invitation go missing?"
        if not persistent.hVanished:
            h "Impossible. I delivered it myself."
        if witchArc >=1:
            pov "Um, excuse me."
            pov "I saw the witch just tonight, actually. She was at a ritual in the mountains."
            if not persistent.mayVanished:
                may "What!? Why would she spurn our invitation?"
        else:
            "But still, the witch did not arrive, and soon everyone was a frenzy of worry."
        if not persistent.goVanished:
            gm "We've given offence to 'er somehow. She'll turn all our 'air to straw and infest all our picnics with ants. None shall escape."
        if not persistent.goVanished:
            go "All our spoons will rust, and our forks will get stuck in the drawers! I already have enough on my hands dealing with the geese!"
        if not persistent.thiefVanished and not persistent.shVanished:
            "The panic increased when the Sparrow-Herder rushed in and waved for attention."
        else:
            "Cries of woe and fear rang out as the town fell into anarchy. Children were crying. The adults tore at their clothes as they rolled on the ground and begged G-d to free them from this terrible curse."
            jump village
    else:
        "Everyone was in their place."
        "No-one was missing."
        #Note: the sparrow herder can only vanish if the thief has vanished
        #Double-check though
        if persistent.thiefVanished == False:
            "But soon, panic broke out when the Sparrow-Herder rushed in and waved for attention."

    if persistent.thiefVanished:
        "Soon, the feast began as planned."
        jump village

    else:
        sh "The Master Thief has struck again!"
        gm "Oh lord, I knew it. I swear I can 'ear the rattlin' of the Goblin Train already."
        sh "The entire suckling pig is missing. Quick - check your valuables!"
        "The whole town turned out their pockets and discovered that all their spare change had been taken and replaced with live rats, which shrieked and leapt away and ran into the forest."
        town "NOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        OOOOOOOOOOOOOOOOOOOOOOOOOOOOO!"
        gm "Told you."
        if demo:
            jump demoEnd
        jump village

# Act 2: Chapter I - Chat and investigation
#You can investigate the village and choose between 2 main pathways
label village:

    show hand onlayer transient:
        yalign 0.68#0.743
        xalign 0.5
    call hideAll from _call_hideAll_17
    if persistent.vanished >= 3:
        show towncrossroadsbggone at artPos
    else:
        show towncrossroadsbg at artPos
    menu:
        "You stood in the middle of the village."
        "If you investigated the banquet, turn to page 64.":
            call musicReturn from _call_musicReturn_16
            jump banquet
        "If you investigated the edge of town, turn to page 70.":
            call musicReturn from _call_musicReturn_17
            jump town
        "If you turned around and went home, turn to page 1." if not houseLockOut:
            #TK: This option gets ripped out if you try it, then go back without succeeding
            if persistent.wolfNamed:
                $renpy.music.set_volume(0, delay=6.0, channel=u'ambient1')
                $renpy.music.set_volume(0, delay=6.0, channel=u'ambient2')
                $renpy.music.set_volume(0, delay=6.0, channel=u'music')
                "I can't stop you any longer."
                "Come, then. I will meet you there."
                jump wolf
            if turnedHome == 0:
                if persistent.vanished ==2:
                    show wolf2 onlayer transient zorder 100
                if persistent.vanished >=3:
                    show notelisten2 onlayer transient zorder 100

                $renpy.music.set_volume(0.9, delay=3.0, channel=u'ambient1')
                $renpy.music.set_volume(0.9, delay=3.0, channel=u'ambient2')
                $renpy.music.set_volume(0.9, delay=3.0, channel=u'music')
                "You don't want to go that way."
            if turnedHome == 1:
                $renpy.music.set_volume(0.8, delay=3.0, channel=u'ambient1')
                $renpy.music.set_volume(0.8, delay=3.0, channel=u'ambient2')
                $renpy.music.set_volume(0.8, delay=3.0, channel=u'music')
                "I'm telling you, you don't want to go back there."
            if turnedHome == 2:
                $renpy.music.set_volume(0.7, delay=3.0, channel=u'ambient1')
                $renpy.music.set_volume(0.7, delay=3.0, channel=u'ambient2')
                $renpy.music.set_volume(0.7, delay=3.0, channel=u'music')
                "All your friends are here. Adventure awaits! Why not stay?"
                "There's nothing back there you want. Trust me."
            if turnedHome == 3:
                if not persistent.hVanished:
                    $renpy.music.set_volume(1.0, delay=2.0, channel=u'ambient1')
                    $renpy.music.set_volume(1.0, delay=2.0, channel=u'ambient2')
                    $renpy.music.set_volume(1.0, delay=2.0, channel=u'music')
                    $turnedHome +=1
                    h "There you are! We've been looking all over for you!"
                    h "Come on, let's get back to the feast."
                    if not persistent.thiefVanished and not persistent.mushroomVanished:
                        h "We need your help to help track down that dastardly Master Thief!"
                        h "Here, I'll help you find your way back."
                        "The hunter took hold of your arm with a surprisingly strong grip and escorted you back into the village."
                        jump town
                    elif not persistent.witchVanished and not persistent.ToadVanished:
                        h "We need your help to help with this terrible curse problem we're having!"
                        h "Here, I'll help you find your way back."
                        "They took hold of your arm with a surprisingly strong grip and escorted you back into the village."
                        jump banquet
                    else:
                        $renpy.music.set_volume(0.7, delay=3.0, channel=u'ambient1')
                        $renpy.music.set_volume(0.7, delay=3.0, channel=u'ambient2')
                        $renpy.music.set_volume(0.7, delay=3.0, channel=u'music')
                        show wolf4 onlayer transient zorder 100
                        h "We... we need you to, uh..."
                        "They looked around. Their eyes were bleary."
                        h "I'm sorry, I - I don't remember why I came here."
                        h "I don't think you should go down that road. There's something..."
                        h "Something twisting in the darkness there... like the coiling of entrails..."
                        "They looked down."
                        h "My hands... they haven't been working properly. They don't do what I tell them to do anymore."
                        h "I don't know who is telling them what to do now."
                        h "I'm sorry. I think I need to rest."
                        "Without a word, they turned and walked back to the village."
                        jump village
                else:
                    $turnedHome =5
            if turnedHome == 4:
                $renpy.music.set_volume(0.6, delay=3.0, channel=u'ambient1')
                $renpy.music.set_volume(0.6, delay=3.0, channel=u'ambient2')
                $renpy.music.set_volume(0.6, delay=3.0, channel=u'music')
                "You began to walk home, but your wiser nature prevailed."
                "You turned back and strode back towards the village with your head held high."
                "The villagers surrounded you and congratulated you on your good sense. A small party was held in your honour."
                "\"Well done,\" they all said. \"You did it.\""
            if turnedHome == 5:
                $renpy.music.set_volume(0.4, delay=3.0, channel=u'ambient1')
                $renpy.music.set_volume(0.4, delay=3.0, channel=u'ambient2')
                $renpy.music.set_volume(0.4, delay=3.0, channel=u'music')
                "Whatever you think you're going to find down that road, you're wrong."
                "There's nothing for you at home anymore."
            if turnedHome == 6:
                $renpy.music.set_volume(0.2, delay=3.0, channel=u'ambient1')
                $renpy.music.set_volume(0.2, delay=3.0, channel=u'ambient2')
                $renpy.music.set_volume(0.2, delay=3.0, channel=u'music')
                "This is the last time I'll tell you."
                #"You don't want to do that."
                "Go back to the fire. Where it's safe."
            elif turnedHome >= 7:
                $renpy.music.set_volume(0, delay=6.0, channel=u'ambient1')
                $renpy.music.set_volume(0, delay=6.0, channel=u'ambient2')
                $renpy.music.set_volume(0, delay=6.0, channel=u'music')
                "Fine."
                jump wolf
            $turnedHome +=1
            jump village
        "If you talked to the Gutterlings, turn to page 56." if persistent.vanished>=2 and gutterlingChat <=5:
            #if persistent.vanished == 1:
            if gutterlingChat == 0:
                g "'Allo mate."
                g "Here's a tip. If you talk to people multiple times, they might have more to say."
                g "It's true! Try it on us."
            if gutterlingChat == 1:
                g "That's the spirit!"
                "They gibbered and twirled in glee."
            if gutterlingChat == 2:
                g "Just make sure not to talk to a Gutterling six times, or it'll own your soul forever."
            if gutterlingChat == 3:
                g "Yep. You definitely don't want to do that."
            if gutterlingChat == 4:
                g "..."
            if gutterlingChat == 5:
                g "Gotcha!"
                $gutterlingChat +=1
                jump gutterlingStory

            $gutterlingChat +=1
            jump village

                #     g "You wouldn't mind steppin' just a little closer to the gutter, would you?"
                #     g "Just a few steps closer. I can't quite hear you, mate. My old ears are going, y'know how it is."
                # if gutterlingChat == 3:
                #     g "Oh well. Doesn't matter."
                #     g "We'll all eat well enough soon."
                # if gutterlingChat == 4:
                #     g "Humbaba promised us."

                #But be wary never to talk to a gutterling six times, or they'll own your soul forever.
                #Yep. You definitely don't want to do that.
                #...
                #Gotcha!


#The banquet with the toad and the witch path
label banquet:
    #TK
    call hideAll from _call_hideAll_18
    if persistent.vanished >=3:
        call hideAll from _call_hideAll_255
        show townfeastbggone at artPos
        show noteHome onlayer transient zorder 100

        "You walked down to the river. Picnic blankets lay empty before the dark waters."
        if persistent.toadVanished == False:
            show wolf3 onlayer transient zorder 100
            "The Toad stood alone, looking into the flames. For a moment you thought you saw people around him - but they were just shadows. The food lay uneaten."
        else:
            "For a moment, you thought you saw people around the fire. But they were just shadows. The food lay uneaten."
        if not persistent.shVanished:
            "A splash broke the stillness. You looked around to see the Sparrow Herder and the Mayor on the shore, skipping rocks over the water."
        else:
            "The Mayor sat on the shore, looking out over the water."
        #Sparrow herder
        #Toad
        #Mayor
        #Second Pig
        #"TBD"

    else:
        $renpy.music.set_volume(1.0, delay=2.0, channel=u'ambient1')
        $renpy.music.set_volume(1.0, delay=2.0, channel=u'ambient2')
        $renpy.music.set_volume(1.0, delay=2.0, channel=u'music')


        show townfeastbg at artPos
        show scribble1 onlayer transient zorder 100
        "You walked down to the river, where the banquet was laid out before a bonfire. Some folks were gripping each other tight and crying out at the misfortune that had befallen their town. Others simply sat in glum silence."
        #Wolf: Toad disappeared
        if persistent.toadVanished == True:
            show wolf3 onlayer transient zorder 100
            "No-one sat at the banquet. The food lay uneaten."
        else:
            "The cane toad from the road was gulping down every morsel of food he could find, cradling a wineglass that was almost as big as he was and darting his tongue out to snatch prawns and hot potatoes from nearby unattended plates."
    label banquetMenu:
        show hand onlayer transient:
            yalign 0.625#0.743
            xalign 0.5
        menu:
            "You looked out over the sad scene."
            "If you talked to the woeful villagers, turn to page 84." if not banquetChat and persistent.vanished <=2:
                "They paid no attention to you, but continued shaking their heads and watching the flames with wretched misery."
                $banquetChat = True
                jump banquetMenu
            "If you talked to the Sparrow-Herder, turn to page 85."  if sparrowherderChat <= 4 and not persistent.shVanished:
                if persistent.witchVanished and sparrowherderRand == 2:
                    $sparrowherderRand =3
                if sparrowherderRand ==1:
                    if sparrowherderChat == 0:
                        sh "G'day."
                        sh "The ruin to the south has many poisonous beasts. Be sure to carry Antidotes if you 'ead that way."
                    elif sparrowherderChat == 1:
                        show spirit3 onlayer transient zorder 100
                        sh "They say these beasts were once envious 'ogs that spoke ill of our dear Lord."
                        sh "Thus 'e cursed 'em, and now they can speak nothing but poisonous words. As soon as you hear their evil gossip, you'll fall down dead as a doornail."
                        sh "That's what I 'eard, anyway."
                    elif sparrowherderChat == 2:
                        sh "The ruin? They say it's left over from the fifth age."
                        sh "It was an age of wise beetles that loved to make puzzles and games."
                        sh "The finest puzzle-makers would go on to become consorts for their Queen."
                    elif sparrowherderChat == 3:
                        sh "Their labyrinthine stone puzzle-boxes lie across the land even now, untouched. None who live can solve 'em."
                        sh "The 'ogmasters laugh at all who try, and their poison words cut them asunder."
                    elif sparrowherderChat >= 4:
                        sh "How do I know all this? The sparrows told me."
                elif sparrowherderRand == 2:
                    if sparrowherderChat == 0:
                        sh "G'day."
                    elif sparrowherderChat == 1:
                        sh "You seen those rings of mushrooms in the woods?"
                        sh "Be wary, friend. Those are the 'ag Tracks. They show where the witches danced last night."
                    elif sparrowherderChat == 2:
                        sh "As they dance, Lady Death pushes 'er fingers slowly through the grass to clutch at their ankles. If they tarry too long, they'll be grabbed by their feet and whisked away straight down to the last kingdom."
                        sh "Long have they danced away from death, and eagerly does she clutch for 'em. If she doesn't catch 'em, they fly away with the dawn, and the fingers are left behind."
                    elif sparrowherderChat == 3:
                        sh "The lady can be nice enough, sometimes. When we had the famine years ago, she pushed 'er fingers through the grass so we could eat."
                        sh "But never go into the circle. She might hear your footsteps, and mistake you for a witch. In a flash, you'll feel 'er fingers wrap around yer ankles and drag you down into the earth. Once she has you, she'll never let you go."
                    elif sparrowherderChat >= 4:
                        sh "How do I know all this? The sparrows told me."
                elif sparrowherderRand == 3:
                    if sparrowherderChat == 0:
                        sh "G'day."
                        sh "Be careful as you walk around town, mate. Stick to the centre of the street, and never cross the gutters without crossing your path with salt."
                        sh "The Gutterlings hide there."
                    elif sparrowherderChat == 1:
                        sh "They are thin, pale and wretched creatures."
                        sh "They rise out of the earth when the gutters overflow with the summer rains."
                    elif sparrowherderChat == 2:
                        sh "They will follow you slowly, concealing 'emselves with leaves and pieces of trash."
                        sh "When you're alone, they reach out with their long, long arms, wrap around yer, and drag yer into the storm drain."
                    elif sparrowherderChat == 3:
                        sh "What happens then? Well."
                        sh "Some say they keep you there for years, feeding yer trash and sewer water to keep yer alive."
                        sh "From your body they will harvest small pieces o' flesh. A thumb, a toe, an ear."
                        sh "From these pieces, they will grow more Gutterlings."
                    elif sparrowherderChat >= 4:
                        sh "How do I know all this? The sparrows told me."
                $sparrowherderChat +=1
                jump banquetMenu
            "If you talked to the Mayor, turn to page 82." if mayorChat <= 6 and not persistent.mayVanished:
                #if mayorRand ==1:
                if mayorChat == 0:
                    if persistent.witchVanished:
                        may "If you're going out, chum, be wary! They say Moon-Head walks these roads tonight."
                    else:
                        may "If you're going out to hunt the witch, be wary! They say Moon-Head walks these roads tonight."
                elif mayorChat == 1:
                    may "They say his front face is a full moon, and his back face is a new moon."
                elif mayorChat == 2:
                    may "If he looks at you with his bright face, you can tell nothing but the truth. If he looks at you with his dark face, you can tell nothing but lies."
                elif mayorChat == 3:
                    may "His robes are rich blue silk with clouds and fog rippling across them, and they flow around him in hypnotising waves as he dances. Or so they tell me, at least."
                elif mayorChat == 4:
                    may "He leaps through the trees calling for his disciples, the lost and insane, and they all spring together through the woods with glee, singing moon-mad songs."
                    label essay1Showing:
                        $renpy.show_screen("essay1", _layer="screens", tag="note", _zorder=101)
                        may "It's quite the sight to see."
                        $renpy.hide_screen("essay1")
                elif mayorChat == 5:
                    may "He winked at my mother once, and I never saw her again."
                elif mayorChat >= 6:
                    may "Sometimes I still hear her laughter on moonless nights."
                # elif mayorRand ==2:
                #     if mayorChat == 0:
                #         may "If you're going out to hunt the witch, be wary! They say Moon-Head walks these roads tonight."
                #     elif mayorChat == 1:
                #         may "They say his front face is a full moon, and his back face is a new moon."
                #     elif mayorChat == 2:
                #         may "If he looks at you with his bright face, you can tell nothing but the truth. If he looks at you with his dark face, you can tell nothing but lies."
                #     elif mayorChat == 3:
                #         may "His robes are rich blue silk with clouds and fog rippling across them, and they flow around him in hypnotising waves as he dances."
                #     elif mayorChat == 4:
                #         may "He leaps through the trees calling for his disciples, the lost and insane, and they all spring together through the woods with glee, singing moon-mad songs."
                #         may "It's quite the sight to see."
                #     elif mayorChat == 5:
                #         may "He winked at my mother once, and I never saw her again."
                #     elif mayorChat >= 6:
                #         may "Sometimes I still hear her laughter on moonless nights."
                # #TK: Add the other 2 options
                # elif mayorRand ==3:
                #     ""
                $mayorChat += 1
                jump banquetMenu
                #If you're going out to hunt the witch, be wary. There's a wolf out there.
                #My sister heard it howling, once. The wolf appeared in her head, and spoke to her.
                #You will have three days, it said.
                #Three days passed, and I never saw her again.
                #Do you hear that?
            "If you talked to the Second Pig, turn to page 266." if pig2Rand == 1 and pigChat <= 7 and not persistent.pigsVanished:
                if pig:
                    if pigChat == 0:
                        p2 "Oh. It's you."
                        "Your pig turned rose up on its hind legs."
                        p1 "Montgomery."
                        p2 "Gregory."
                    if pigChat == 1:
                        p2 "I'm sorry, but you'd better not stay here. I don't think it's safe for us to be so close."
                        p1 "Hm. I see you are still gripped by this insane delusion."
                        show wolf5 onlayer transient zorder 100
                        p2 "It's no delusion, brother. I know you've heard it too. No matter how you hard you try to hide it."
                    if pigChat == 2:
                        p1 "Cast off this madness, Montgomery. It's all in your head."
                        p1 "Come back to us. We all miss you."
                        show wolf3 onlayer transient zorder 100
                        p2 "Look me in the eyes and tell me you haven't heard the scrabbling in the walls."
                        p1 "Nothing but rats."
                        p2 "Tell me you haven't heard the howling in the pipes."
                        p1 "The wind. Just the wind."
                        p2 "You cannot tell me you don't seen the visions. The seven terrors, which it wears like seven cloaks. Its face, a single coiling line, like tangled entrails."
                        p2 "The house twists with it. Swollen. You can barely breathe in there for the stink of it."
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
                        show wolf6 onlayer transient zorder 100
                        p2 "You see, I'm expecting someone."
                    if pigChat == 3:
                        show wolf7 onlayer transient zorder 100
                        p2 "I can hear them coming now. I can see the spiral."
                    if pigChat == 4:
                        p2 "The others say it's all in my head. But I know better."
                    if pigChat == 5:
                        show wolf8 onlayer transient zorder 100
                        p2 "You'd better get moving. You don't want to be here when they come."
                    if pigChat == 6:
                        p2 "Or perhaps I'm wrong."
                    if pigChat == 7:
                        show wolf9 onlayer transient zorder 100
                        p2 "Perhaps you've already met them. You just haven't realised yet."
                $pigChat +=1
                jump banquetMenu
            "If you talked to the Toad, turn to page 87." if not toadStole2 and not persistent.toadVanished:
                if persistent.vanished == 3:
                    if not toadLong:
                        f "Well. I suppose this is it."
                        "The fire reflected in his eyes. They seemed glassy and vacant."
                        f "It's been so long now."
                        f "But still. Not long enough."
                        "He shook his head."
                        f "Enough of this melancholy! We should spend these last moments in my manor. It's the finest in the world."
                        f "And definitely mine, my own, no doubt about that. Always has been!"
                        f "I'm planning quite the gala. You should join me."
                        "He hesitated."
                        f "That is... if you've done everything you need to, you know. Said your goodbyes."
                        
                        $toadLong = True
                        show hand onlayer transient:
                            yalign 0.7#0.743
                            xalign 0.5
                    else:
                        f "Have you made your decision? There isn't much time left."
                    
                        show hand onlayer transient:
                            yalign 0.7#0.743
                            xalign 0.5
                    menu:
                        f "I think this may be our last party."
                        "If you accepted, and set off to the toad's manor, turn to page 105.":
                            f "Sensational! Stay close to me, and you won\'t have a thing to fear."
                            f "Let us be off at once!"
                            stop music fadeout 6
                            jump toadSolo
                        "If you politely declined (for now, at least), turn to page 102.":
                            f "You're missing out, I'm telling you!"
                            f "You... really should come. I'd like to spend it with you."
                            #$toadDecline = True
                            jump banquetMenu


                if gilgameshPathFollowed:
                    f "There you are! Lost track of you for a moment there, ha ha."
                    f "Now, where were we?"
                elif toadStole and not persistent.witchVanished:
                    f "You!"
                    f "Hellion! Knave! You'll see justice for your crimes, or my name isn't Brildebrogue Chippingham!"
                    "You quickly hid under the tablecloth until the toad became distracted by a passing prawn platter and gave you time to slip away."
                    "Best avoid him for now."
                    $toadStole2=True
                    jump banquetMenu
                elif toadStole and persistent.witchVanished:
                    f "Good evening, my light-fingered friend!"
                    "He sprayed food as he spoke. He was sitting on a tower of pillows on his chair, so he could reach the table."
                    f "Don't worry about that little issue of the emerald brooch you made off with. I have so much money now, you see, I'll hardly miss it. Consider it a gift! A memento of our new friendship, hoho!"
                else:
                    if toadConvo2Spoke == False and toadArc == 0:
                        f "Hello again, fellow traveller!"
                        "He sprayed food as he spoke. He was sitting on a tower of pillows on his chair, so he could reach the table."
                        f "Do not be alarmed! I have already forgiven your poor manners in refusing my generous offer on the road."
                    elif toadConvo2Spoke == False and toadArc > 0:
                        f "Good evening, my dear friend!"
                        "He sprayed food as he spoke. He was sitting on a tower of pillows on his chair, so he could reach the table."
                        f "It warms my heart to see you again! Although we have known each other but a little time now, I already feel the bonds of our friendship have grown strong as the thickest iron, so warmed have I been by your gregarious companionship!"
                        f "Please, take a seat beside me! I would count myself proud to sit among such distinguished company as yours."
                    elif toadConvo2Spoke:
                        f "Ah, the traveller returns!"
                        f "You {i}must{/i} try some of these prawns, they're simply to die for. A credit to your humble village!"
                label toadConvo2:
                    show hand onlayer transient:
                        yalign 0.65#0.743
                        xalign 0.5
                    $toadConvo2Spoke = True
                    menu:
                        f "Try the mango, it's marvellous."
                        "If you asked about the feast, turn to page 89." if not toadFeast:
                            f "Yes, it's adequate, perfectly adequate."
                            "He opened his mouth wide and took a bite out of a chunk of bread with butter slathered on it."
                            f "Nothing like the feasts back at Chippingham Manor, of course, you understand, nothing like them at all, but certainly adequate nonetheless, I have to say, if I do say so myself, needless to say, as the saying goes, to say nothing of this fine vintage!"
                            "He awkwardly tilted the wineglass towards him and drank deeply, almost falling in."
                            show tornPage1 onlayer screens zorder 101
                            show tornPage1bg onlayer screens zorder 99
                            f "Why, it quite reminds me of when I was staying with the Sultana of Yolkorich, a land far to the south across the seas, completely made out of delectable food, you understand! The trees were made of liquorice sticks, all the pillars were fine musk candy, the streams ran fresh with sparkling champagne, and the citizens would drive over the rocky roads on peppermint carriages drawn by mouth-watering omelette stallions. Well, one day I woke up and tucked into a hearty breakfast of raisin toast, smoked salmon and fried eggs, only to discover I had devoured the Sultana herself, along with her entire retinue! I had to make a hasty retreat from that situation post-haste."
                            hide tornPage1 onlayer screens
                            hide tornPage1bg onlayer screens
                            f "There was egg on my face, I can tell you!"
                            $toadFeast = True
                            jump toadConvo2
                        "If you asked about his plans, turn to page 90." if not toadLong:
                            if persistent.witchVanished:
                                f "Aha! Allow me to elucidate."
                                "He slurped noisily from his wineglass until it was empty."
                                call musicSilence from _call_musicSilence_17
                                f "I came to this village to..."
                                show wolf9 onlayer transient zorder 100
                                f "To, ah..."
                                "He looked down at his wineglass."
                                "His brow wrinkled."
                                call musicReturn from _call_musicReturn_18
                                f "...to enjoy this magnificent feast, of course!"
                                "He brightened up and began filling his wineglass with renewed vigour."
                                f "Yes, that must have been it. Please, join me!"
                                f "It's nothing compared to the feasts at my manor, of course."
                                $toadLong = True
                                jump toadConvo2
                            else:
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
                        "If you asked for more information about the witch, turn to page 93." if toadLong and not toadFind and not persistent.witchVanished:
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
                                        stop music fadeout 6
                                        jump toad1
                                    "If you politely declined (for now, at least), turn to page 102.":
                                        f "I understand. The witch's fear quails even the most courageous heart."
                                        f "Not mine, of course! If you change your mind, I'll be here."
                                        #$toadDecline = True
                                        jump toadConvo2
                        "If you asked about the witch again, turn to page 93." if toadFind and not persistent.witchVanished:
                            f "Ah, have you changed your mind?"
                            jump toadWitchJoin
                        "If you asked him about the thief, turn to page 78." if toadLong and not toadThief and not persistent.thiefVanished:
                            $toadThief = True
                            pov "Aren't you going to do anything about all the stolen goods?"
                            f "And risk the wrath of the Master Thief? Not on your life! I heard they eat danger, and breathe death!"
                            may "I heard they stole a fine racing horse right out from under its rider."
                            sh "I heard they stole the King of Spain right out from under 'is wife."
                            f "Well, I have heard tell that every winter they shrink down to the size of a pin, and hide away in your house to steal all your odd socks and hairpins and loose change."
                            f "Why do they do it? Why, to make a nest, of course. All the better to lure their suitor, THE DEVIL!"
                            jump toadConvo2
                        #Manor - solo toad route
                        "If you asked him about the manor, turn to page 78." if toadLong and persistent.witchVanished:
                            f "Ah yes, Chippingham Manor! Finest in the world, I tell you."
                            f "And definitely mine, my own, no doubt about that. Always has been!"
                            f "Why don't you come visit? In fact, we could head there tonight. I'm planning quite the gala."
                            show hand onlayer transient:
                                yalign 0.7#0.743
                                xalign 0.5
                            menu:
                                f "You'll get a taste of the real high life."
                                "If you accepted, and set off to the toad's manor, turn to page 105.":
                                    f "Sensational! Stay close to me, and you won\'t have a thing to fear."
                                    f "It would be the brave forest beast indeed that would dare to cross swords with THESE powerful weapons."
                                    "He flexed his arms for you. A tiny bump of muscle rose up."
                                    f "Let us be off at once!"
                                    stop music fadeout 6
                                    jump toadSolo
                                "If you politely declined (for now, at least), turn to page 102.":
                                    f "You're missing out, I'm telling you!"
                                    f "You really should come."
                                    #$toadDecline = True
                                    jump toadConvo2

                        #Ask him about the manor

                        "If you asked about your Godparent, turn to page 85." if not toadHelp:
                            if godfather== "Black":
                                pov "I need a way to escape my godmother, Lady Death. Can you help me?"
                                f "Possibly, possibly."
                                if persistent.witchVanished:
                                    #show firelight animated with dissolve
                                    call musicSilence from _call_musicSilence_18
                                    f "I may know someone who can assist with that. Her name is..."
                                    show wolf7 onlayer transient zorder 100
                                    f "Her name..."
                                    f "..."
                                    call musicReturn from _call_musicReturn_19
                                    f "Never mind, I must have been mistaken. More ham?"
                                else:
                                    f "Perhaps the witch will know something about it. You should join me in hunting her down!"
                            elif godfather == "White":
                                pov "I need a way to escape my Godfather, the Lord. Can you help me?"
                                f "Possibly, possibly."
                                if persistent.witchVanished:
                                    call musicSilence from _call_musicSilence_19
                                    f "I may know someone who can assist with that. Her name is..."
                                    show wolf7 onlayer transient zorder 100
                                    f "Her name..."
                                    f "..."
                                    call musicReturn from _call_musicReturn_20
                                    f "Never mind, I must have been mistaken. More ham?"
                                else:
                                    f "Perhaps the witch will know something about it. You should join me in hunting her down!"
                            elif godfather == "Red":
                                pov "I need a way to escape my Godfather, the Devil. Can you help me?"
                                if persistent.witchVanished:
                                    call musicSilence from _call_musicSilence_20
                                    f "I may know someone who can assist with that. Her name is..."
                                    show wolf7 onlayer transient zorder 100
                                    f "Her name..."
                                    f "..."
                                    call musicReturn from _call_musicReturn_21
                                    f "Never mind, I must have been mistaken. More ham?"
                                else:
                                    f "I'm sure the witch would know something about that. Rumour is that she dances with the Devil on cold, moonless nights! You should join me in hunting her down."
                            $toadHelp = True
                            jump toadConvo2
                        "If you made your excuses and left, turn to page 83.":
                            f "Return soon! You can't possibly leave without sampling some of this fine green mango salad over here, absolutely sensational!"
                            jump banquetMenu
            "If you wandered into the woods, turn to page 84." if persistent.toadVanished or persistent.witchVanished:
                if persistent.vanished <=1 and persistent.thiefVanished == False and persistent.mushroomVanished == False and shStopped == False:
                    sh "H-hold on, mate! Leaving so soon?"
                    sh "We're just hatching a plan to catch that dastardly Master Thief. We could use yer help!"
                    sh "Come on then, let's get back to the village."
                    $shStopped = True
                    jump town
                else:
                    "You turned and walked out into the darkness of the woods. No-one stopped you."
                    stop music fadeout 6
                    jump toadWitchInvestigate
            "If you returned to the village square, return to page 50.":
                "You turned and walked back to the centre of the village."
                jump village

#The outskirts of town, with the thief and mushroom path
label town:
    $renpy.music.set_volume(1.0, delay=2.0, channel=u'ambient1')
    $renpy.music.set_volume(1.0, delay=2.0, channel=u'ambient2')
    $renpy.music.set_volume(1.0, delay=2.0, channel=u'music')

    call hideAll from _call_hideAll_19
    show townextbg at artPos
    if persistent.vanished >=2:
        show noteWaiting onlayer transient zorder 100
    if persistent.thiefVanished:
        "You walked out to the edge of town."
    else:
        if persistent.vanished ==3:
            "You walked out to the edge of town. Some lone villagers still stood there, looking out into the woods."
            "There was a sound from the depths of that forest. The howling of the wind."
        else:
            "You walked out to the edge of town, where villagers ran to and fro, searching for the Master Thief."
            if not tarpDone:
                "Some of them were strapping down a tarp."
    #TK: Add another character who randomly appears and disappears - moon-head?
    label townExplore:
        show hand onlayer transient:
            yalign 0.615#0.743
            xalign 0.5
        menu:
            "Fruit bats chirped and swirled overhead."
            "If you investigated the tarp, turn to page 79." if not persistent.thiefVanished:
                show scribble5 onlayer transient zorder 100
                if gilgameshPathFollowed or tarpDone:
                    h "There you are! We lost track of you for a bit there."
                    h "Are you going to help us with this?"
                else:
                    pov "What is this?"
                    if persistent.vanished ==3:
                        "For a moment they didn't seem to hear you. Then they turned, as if in a dream."
                        h "We're going to catch the thief."
                        sh "Yes. The thief."
                        "They were drinking wine straight from a bottle which they passed around between them."
                        $tarpDone = True
                    else:
                        h "Shhh! Keep your voice down. This is all part of our plan to catch that dastardly Master Thief."
                        gm "We're sure to fail. This whole plan is doomed."
                jump villagersConvo
            "If you talked to the Goose-girl, turn to page 97." if goosemongerChat <= 6 and not persistent.goVanished:
                if goosemongerChat == 0:
                    go "Greetings, friend. Be careful of the crystal caverns to the north."
                elif goosemongerChat == 1:
                    go "It is said that the first of the Goose-girls, old crooked Belziah, attempted dark experiments there."
                elif goosemongerChat == 2:
                    go "She created abominable goose-faced men that even now infest the caverns, honking endlessly and plotting to turn the world to ruin."
                elif goosemongerChat == 3:
                    go "Sometimes, I... I must confess I dream of those caves."
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
            "If you talked to the Hunter, turn to page 98." if hunterChat <=2 and not persistent.hVanished:
                #The Hunter Side-quest
                #Even you had no understanding of the true depths of the hunters skill. Each day they would kill a different beast. You see, once, a young boy stumbled into their house. The hunters house secretly had a vast underground cavern full of all types of creatures. The first level held the birds. The second level held the beasts of the earth. The third level held great underground seas where the beasts of the ocean lurked. Each day they would release one to hunt. Their pact with the well-spirit of your village fed them fresh prey always. One day a young girl stumbled into the hunters domain. She was hunted through the tunnels. In the seventh and lowest depth of the house the hunter combined the beasts into new shapes unseen by man. The girl entreated the help of the beasts and fled into the forest. Alas, she was never seen again. The hunters skill was not to be denied. Until myself, of course.
                #Then have a sub-story where she speaks to one of the beasts.
                #Story level 1 mystery: Where did the old hunter derive his power?
                #The beast has a story about how it was once a prince. His king was mysteriously murdered one night and he was forced to flee. In his travels, he was transformed by a wicked witch.
                #Story level 2 mystery: who murdered the old king?
                #Story level 3, the witch
                #Then go into a further sub-story about the witch. Finally the witch story connects back to you in the village. You never find the resolution to those other two stories.
                if hunterChat == 0:
                    show wolf10 onlayer transient zorder 100
                    h "A wolf? Don't be silly."
                if hunterChat == 1:
                    show wolf7 onlayer transient zorder 100
                    h "There are no wolves in Australia."
                if hunterChat == 2:
                    h "Howling? No. You must be imagining it."
                $hunterChat += 1
                jump townExplore
            "If you talked to the Gloom-monger, turn to page 99." if gloommongerChat <=6 and not persistent.gmVanished:
                #TK: Longer gloom-monger chat.
                if persistent.vanished <= 1:
                    if gloommongerChat == 0:
                        show monster4 onlayer transient zorder 100
                        gm "Give it up now. You're already doomed."
                    elif gloommongerChat == 1:
                        gm "We have already died countless times. And we will die countless more, 'fore this business is through."
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
                elif persistent.vanished >=2:
                    if gloommongerChat == 0:
                        gm "[povname], is it? Lovely name."
                    elif gloommongerChat == 1:
                        gm "Did you choose it yourself?"
                    elif gloommongerChat == 2:
                        gm "Y'know, a secret lies in that place where names are chosen."
                    elif gloommongerChat == 3:
                        gm "Perhaps you could go there now. And choose another name."
                    elif gloommongerChat == 4:
                        gm "Perhaps you will find something, if you choose the right name. Perhaps the name of an ancient king. Who can say?"
                    elif gloommongerChat == 5:
                        gm "It won't save us, of course. Nothing will."
                    elif gloommongerChat == 6:
                        gm "We are already dead."
                $gloommongerChat += 1
                jump townExplore
            "If you looked in the well, turn to page 346." if wellRand == 1 and wellChat <=2 and not persistent.wellVanished and persistent.vanished<=1:
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
                            "You would have liked to make a wish. But you had no coins on you."
                        "Otherwise, if {b}you have ventured into the Smoke World and rescued the stolen Skin-Mask from King Famine{b}, turn to page 742.":
                            stop music fadeout 6
                            well "Thank G-d you have it. Quickly! Come in!"
                            call hideAll from _call_hideAll_20
                            show wellbg at artPos
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
                            pov "Aloysius... your brother told us about what happened. I just wanted to say-"
                            well "Save your breath. There's nothing to be done about it now."
                            well "In the years since I died in that freak chainsaw juggling accident... there's one thing I've learned."
                            well "You can't change the past."
                            well "All you can do is try to change the future. Once step at a time."
                            "A rumble shook the cave. In horror, you saw the fingers of King Famine slowly breaking in through the earth around you. In the cracks you could see his gaping maw. A terrible screaming broke out all around you."
                            "With a powerful crack, Aloysius stretched his ghostly form across the cave, holding it together through sheer force of will. Thick smoke billowed all around you."
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
                            "You stumbled out into the frozen silence of the chasm. Below you, you could see the vortex of souls. In the middle of the vortex, Princess Sun lay peacefully at rest in her tomb."
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
                                    "The skin pressed into your mouth and eyes. Its coils folded over and enveloped you."
                                    sm "Good."
                                    show wolf10 onlayer transient zorder 100
                                    "The howling finally stopped."
                                    "All was silent and still."
                                    call endStamp from _call_endStamp
                                    "And then there was rest in the land."
                                    $persistent.wellVanished = True
                                    "..."
                                    "Well. That's enough of that."
                                    "Let's get back to the story."
                                    play sound pageFlip
                                    jump town
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
                                    call endStamp from _call_endStamp_1
                                    "And if you are not dead, you are still alive."
                                    "..."
                                    "Well. That's enough of that."
                                    "Let's get back to the story."
                                    $persistent.wellVanished = True
                                    play sound pageFlip
                                    jump town
                                    #jump end
                        "Otherwise, you may make a wish. Turn to page 367.":
                            "You toss a coin in the well, and wish for a way out of your terrible predicament."
                $wellChat += 1
                jump townExplore
            "If you wandered into the woods, turn to page 157." if persistent.thiefVanished or persistent.mushroomVanished:
                if persistent.vanished <=1 and persistent.toadVanished == False and persistent.witchVanished == False and toadStopped == False:
                    f "W-wait just a second there!"
                    f "This is no time to be wandering off into the woods! We have an accursed witch to bring to justice. Not to mention a fine banquet to sample."
                    f "Come, let's get back to the village. I can tell you all about the plan."
                    $toadStopped = True
                    jump banquet
                else:
                    "You turned and walked out into the darkness of the woods. No-one stopped you."
                    stop music fadeout 6
                    jump thiefMushroomInvestigate
            "If you returned to the middle of the village, turn to page 50.":
                "You turned and walked back."
                jump village
    label villagersConvo:
        show hand onlayer transient:
            yalign 0.63#0.743
            xalign 0.5
        menu:
            go "Care to join us?"
            "If you asked them about the thief, turn to page 66." if not villagersPlan and persistent.vanished ==3:
                h "This is it. The last thing left to do."
                sh "We had a good run."
                go "I just wish there was more time."
                sh "Will you come with us?"
                $villagersPlan = True
                jump villagersConvo
            "If you went off with them to catch the Master Thief, turn to page 124." if villagersPlan and persistent.vanished ==3:
                h "Let's do it. One last time."
                "They raised the bottle in a toast."
                go "May you all find the True Ending."
                "Everyone took a swig."
                sh "I-I'm glad I'll be with all of you."
                go "Me too."
                h "Couldn't have asked for a better hunting party!"
                "You, the Goose-Girl, the Sparrow-Herder and the Hunter all climbed into the cart and held hands as it rattled away down the road, leaving the old Gloom-monger behind."
                $renpy.show_screen("gilPath", _layer="screens", tag="map", _zorder=101)
                gm "You're all doomed! Doooooooomed!"
                $renpy.hide_screen("gilPath")
                sh "..."
                stop music fadeout 6
                jump thief2

            "If you asked how they planned to catch the thief, turn to page 66." if not villagersPlan and persistent.vanished !=3:
                h "With this!"
                "The Hunter flexed their muscles and pulled back the tarp to reveal an ornate chest full of lustrous pebbles and stones."
                go "We'll take this out to my house, and nail it to the veranda. Everyone knows that the Master Thief can't resist anything that's nailed down."
                h "Exactly. And their love for shiny rocks is well-known."
                echidna "A fine plan indeed, friends! There's no way this \"Master Thief\" I've heard so much about could ever detect this scheme, no matter how cunning and gorgeous they are."
                h "Thanks, friend. Your confidence means a lot."
                $villagersPlan = True
                jump villagersConvo
            "If you asked why they planned to catch the thief, turn to page 68." if not villagersCatch and persistent.vanished !=3:
                h "They stole my courage!"
                gm "They stole my wisdom!"
                go "They stole my heart."
                if pig:
                    "Your pig grunted as if to say, \"They stole my dignity.\""
                h "We can't let them just run around doing as they please and getting the Goose-girl all hot and bothered. What if everyone decided to do that? It'd be anarchy!"
                go "Hot, sweaty anarchy."
                $villagersCatch = True
                jump villagersConvo
            "If you asked them about your Godparent, turn to page 77." if not villagersEscape and persistent.vanished !=3:
                if godfather== "White":
                    pov "I need a way to escape my Godfather, the Lord. Do any of you know how I can do that?"
                    gm "Hmph. I advise you to give up immediately."
                    if persistent.thiefVanished:
                        go "I'm sorry. I know of no-one who can help you with that plight."
                        sh "Wasn't there..."
                        sh "No, never mind. You're right. There is no-one."
                    else:
                        go "Well, it is said that the Master Thief has hidden from the Lord all their life. If anyone would know, they would."
                        h "Once we track the thief down, you could question them!"
                elif godfather == "Red":
                    pov "I need a way to escape my Godfather, the Devil. Do any of you know how I can do that?"
                    gm "Hmph. I advise you to give up immediately."
                    if persistent.witchVanished:
                        go "I'm sorry. I know of no-one who can help you with that plight."
                        sh "Wasn't there..."
                        sh "No, never mind. You're right. There is no-one."
                    else:
                        go "Well, I have heard that the witch has sworn her soul to the devil. She would know how to help you, if anyone would."
                        sh "If only she was here tonight! Oh, I can already feel her curse upon me."
                elif godfather == "Black":
                    pov "I need a way to escape my godmother, Lady Death. Do any of you know how I can do that?"
                    gm "Hmph. I advise you to give up immediately."
                    if persistent.mushroomVanished:
                        go "I'm sorry. I know of no-one who can help you with that plight."
                        sh "Wasn't there..."
                        sh "No, never mind. You're right. There is no-one."
                    else:
                        go "Well, as we all know, mushrooms are the fingers of death. That wise mushroom in the deep forest would know how to help you, if anyone would."
                        sh "I heard that dastardly Master Thief was planning to steal from 'er this very night! We'd better get the trap laid before they 'ave a chance."
                $villagersEscape = True
                jump villagersConvo
            "If you asked them about the witch, turn to page 79." if villagersCatch and not villagersWitch and not persistent.witchVanished and persistent.vanished !=3:
                pov "Are you going to do anything about the witch's curse?"
                go "And risk the wrath of the witch? Not on your life."
                gm "I heard that she has fingers as long and fat as carpet snakes, and once you fall into her clutches, you'll never see daylight again."
                go "I heard she has many children with the Devil, who are all evil."
                h "Well, I heard that all the trees of the woods are her children, but she regards them with vicious envy, and if any of them displease her by becoming too beautiful, she strikes them down!"
                h "This is why the most beautiful trees are always thunderstruck."
                $villagersWitch = True
                jump villagersConvo
            "If you accepted their offer, and went off to catch the Master Thief, turn to page 124." if persistent.vanished !=3 and villagersPlan or villagersCatch:
                $tarpDone = True
                h "Excellent! Let's be off at once."
                "And so you, the Goose-Girl, the Sparrow-Herder and the Hunter all leapt on the cart and rattled away down the road, leaving the old Gloom-monger behind."
                gm "You're all doomed! Doooooooomed!"

                label gilPathShowingThief:
                    h "Don't worry. He says that every time we go anywhere."
                stop music fadeout 6
                jump thief2
            "If you made your excuses and left, turn to page 51.":
                if persistent.vanished == 3:
                    sh "Yes. Say your goodbyes."
                else:
                    sh "No worries. Have a good one!"
                jump townExplore

#=====================THE THIEF'S STORY

# Act 2, Chapter 2A: The Master Thief
#When you leave the village to track down the thief
label thief2:
    call hideAll from _call_hideAll_21
    show town3bg at artPos
    "Soon, you arrived at the young goose-girls house, which was overrun by honking devils who tore at the furniture and ransacked the pantry and snapped at everyone until she was at her wit's end."
    #show wolf1 onlayer transient zorder 100
    #go "Be careful! They say there's a terrible wolf somewhere out in these woods."
    #show wolf10 onlayer transient zorder 100
    #h "Don't worry, it's just a mad tale. There are no wolves in Australia."
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
            "You pulled thin tripwires all around the chest, tied to old tin cans. As soon as anyone approached it the tin cans would rattle like crazy, alerting the waiting geese."
            $chest = "Tripwires"
        "If you placed a terrible goose inside the chest itself, turn to page 116.":
            "You picked up the most disagreeable goose from the pack and carefully placed it inside the chest, shielding your eyes as it pecked at you in rage."
            "As soon as it was inside the chest, you slammed it shut."
            $chest = "Goose"
    "Then the four of you ducked behind a bush to watch the chest."
    "The geese wandered around the house, honking softly."
    sh "Now we wait."
    go "The thief will never get past us now."
    if not persistent.mushroomVanished:
        echidna "I couldn't agree more, friends. This cunning and charismatic \"Master Thief\" character stands no chance against us."
    h "Don't get cocky."
    if persistent.mushroomVanished:
        #Note: I trigger all of the vanished flags all at the same time now.
        #So that if you quit the game at this point it doesn't break the game with only some people vanished and others not.
        #I also need to purge saves here so that you can't reload into a saved game that doesn't work.
        #TK: Make sure this works and doesn't break anything, also if it's the best option

            
        stop music fadeout 6
        "The night was dark and quiet. You thought you heard something rustling in the bushes, outside your line of sight. A sound, like something moving through the forest."
        "But it must have been the wind."
        #call musicSilence from _call_musicSilence_21
        play music hunted1
        show wolf1 onlayer transient zorder 100
        "The three of you lay there for a long time, watching the chest."
        $ renpy.block_rollback()
        go "Wait just one moment."
        go "Was there... someone else here?"
        pov "I don't think so."
        #call musicReturn from _call_musicReturn_22
        sh "Just us three. You, me and [povname]."
        go "For some reason I thought..."
        "The goose-girl looked around."
        "After some searching she found a hunter's rifle, lying unused under the bush."
        sh "How odd."
        go "Does this rifle look... familiar to you?"
        sh "No. No, I don't think so."
        "The goose-girl rubbed her head."
        go "No, you're right. I don't know what I was thinking. I've never seen it before."
        "None of you had ever seen it before."
        "There were footprints on the ground leading to it. But no-one stood there except the three of you."
        "It was always just the three of you."
        #sh "I guess someone must have left it there, a long time ago."
        #go "It's brand new."
        #"You all stared at it."
        #TK: add a choice to keep the rifle or not, make it important.
        #pov "I think I'd better keep it on me. Just in case."
        "You lapsed into an uneasy silence as you went back to watching the chest."
        "The silence stretched on for a long moment."
        "The area around the house was still, and empty."
        "The clouds slowly covered moved over the moon. Their shape was ragged and spiralling, like twisting entrails."
        sh "I think we'd better check the traps. Make sure they're working."
        #call musicSilence from _call_musicSilence_22
        stop music fadeout 6
        play music2 [ "<sync music>audio/hunted2.wav", "audio/hunted2.wav" ] fadein 1
        $ renpy.block_rollback()
        show wolf12 onlayer transient zorder 100
        "The two of you slowly crawled up to the chest."
        sh "Maybe we should have brought more people along. It's a little spooky with just the two of us."
        pov "You're right. We should have thought of that."
        "You looked around, but no-one was there except the two of you."
        "It was always just the two of you."
        #call musicReturn from _call_musicReturn_23
        "The Sparrow Herder looked over the traps."
        sh "Yep, they're all still there."
        #"You looked up at the cottage."
        pov "How long has this old house stood here?"
        "The abandoned cottage loomed over you."
        "The lights were on, but it was silent and empty."
        sh "No idea."
        sh "Not sure who owns it. Must have been before my time."
        "Who could say how long it had lain deserted?"
        "You saw some stray goosefeathers lying in the dirt. Nothing beside remained."
        sh "I-I think this might have been a mistake."
        sh "Let's head back to the village. Come on."
        stop music2 fadeout 6
        play music3 [ "<sync music2>audio/hunted3.wav", "audio/hunted3.wav" ] fadein 1

        #call musicSilence from _call_musicSilence_23
        "The trees shivered in the wind. In the distance, you heard a noise."
        "Almost like howling."
        $ renpy.block_rollback()
        show wolf10 onlayer transient zorder 100
        if pig:
            "You and your pig stood alone in the empty clearing."
        else:
            "You stood alone in the empty clearing."
        "It had always been just you."
        "No-one stood beside you. The clouds were over the moon. The wind bit into you with cold certainty."
        "You felt something grab your hand."
        t "Run."
        stop music3 fadeout 6
        play music4 [ "<sync music3>audio/hunted4.wav", "audio/hunted4.wav" ] fadein 1
        #call musicReturn from _call_musicReturn_24
        "The thief wrenched your arm and ran with you, away from the abandoned cottage and into the forest."
        if pig:
            "Your pig ran after you but was soon lost to sight in the darkness."
        "You ran over hill and dale, through the shrubs and thorns and tangled thickets, twisting this way and that."
        "The thief ran like a wild thing, like they were being pursued. They held tight to your hand the whole way, and you heard their mad laughter in the darkness as the trees writhed around you like tormented spirits."
        "They took a whistle from their pocket and blew on it, making a harsh, shrill whine echo through the forest."
        "At first there was silence."
        "Then, you heard an answering whistle, deep and loud enough to deafen you."
        "A brilliant light shone through the space between the trees. There was the sound of thundering wheels."
        call hideAll from _call_hideAll_49
        play sound pageFlip
        show trainfullbg
        ""
        play sound pageFlip
        call hideAll from _call_hideAll_50
        show trainbg at artPos
        "A train crashed through the bush, twisting and bending in impossible ways to fit between the trees."
        "It was swarming with wild and chaotic shapes of all manner of monsters, and you could see a team of things holding onto the front and laying tracks in front of the train as fast as they could as it swerved through the forest."
        t "Grab on!"
        #stop music4 fadeout 6
        $renpy.music.set_volume(0.2, delay=10.0, channel=u'music4')
        "The thief pushed you up to grab onto the side of the carriage, then you reached down and pulled them up beside you."
        "The train whistled with full force, gathering speed until it burst out of the trees and into a wide open field."
        jump thiefSolo

    else:
        "You lay there in silence, watching the chest."
        "A fly landed on it."
        "One of the geese waddled up and began to lick it."
        go "Wait just one moment..."
        "The goose-girl crawled out and cautiously dragged a finger over the chest, then stuck it in her mouth."
        go "It's... icing!"
        "The entire chest had been replaced with a massive cake, baked to look exactly like the chest in every detail."
        if chest == "Traps":
            "You tested the traps to find that they were now all made out of carefully crafted fondant."
        elif chest == "Tripwires":
            "You pulled at the tripwires to discover that every can was now a perfect cake replica of a tin can made from sponge and fondant."
        elif chest == "Goose":
            "You cut open the cake to find a fine meringue goose inside."
        "The smell of chocolate wafted from behind you. You turned in slow horror, realisation already dawning."
        label thiefCake:
            show hand onlayer transient:
                yalign 0.67#0.743
                xalign 0.5
            menu:
                "The goose-girl's entire cottage had been replaced with a gigantic gingerbread house."
                "If you all wailed in piteous woe, turn to page 109." if not pitifulGoose:
                    go "{i}NoOOoOOOOOOOOOOoooOOOOOOOOOO
                    OOOOOOOoOOOOOOOOOoOOOOOOOOOOO
                    OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
                    OOOOOOOOOOoOOOOoOOOOOOOOOOOOO
                    OOOOooOOOOOOOOOoooOOOOOOOOOOO
                    OOOOOOOOOOoooOOOOOOOoooOOOOOO
                    OOOOoOOOooOOOOOOOOOOOOOOOOOOO!{/i}"
                    sh "{i}NOOOooooOOOOoOOOOOOOOOOoOOOOO
                    OOOOOOoOOOOOOOOOOOooOOOOOOOOO
                    OOOOOOOOOooOOOOOOOoOOOOOOooOO
                    OOOOOOOOOOOOOOoOOOoOOOOOOOOOO
                    OOOOOOOOOOOoOOOOOoOOOOOOOOOOO
                    OOOOOOOOOOOOOoOOoOOOOOOOooOOO
                    OOoOOOOOOOOOOOOOOoOOOOoOOOOOO!{/i}"
                    h "{i}NooOOOOOOOOOOOOoOOOOOOOOOOOOOOO
                    OOOOOOOOOOOOOoooOOOoOOOOOOOOO
                    OOOOoOOOOoOOOOOOOOOOOOOOOOOOO
                    OOOoOOOOOOOooOOOOOOOOOOOOOOOO
                    OOOOOOOOOOoOOOOOOOOOoOOOOOOOO
                    OOoooOOOOOoOOOOOOOOOOOOoOOOOO
                    OOOOOOOoOOOOOoOoOOOOOOOOoOOOO!{/i}"
                    pov "{i}NOooOOOOoOOoOOOOOOOoOOOOOOOOOO
                    OOOooOOOOooOOOOOOOOoOOOOOOOOO
                    OOOOOoOOOOooOOOOOOooOOOOOOOOO
                    OOOOOOOOOOOOOOOOOOOOOOOOoOOOO
                    OOOOOOOOOOooOOOOOOOOOOOOOOOOO
                    OOOOOOOOOoOOOOOOoOOOOOOOooOOO
                    OOOOOOOoOOOOOOOoOOOOOOOOOOOOO!{/i}"
                    "The geese honked with glee and began devouring the gingerbread cottage."
                    #echidna2 "What a shame. Oh well! I'd best be off."
                    $pitifulGoose = True
                    $pitiful +=1
                    jump thiefCake
                "If you asked your pig to find the culprit, turn to page 132." if pig:
                    "The pig leapt from your hands and began snuffling around in the grass. It soon began sniffing at the Echidna, grunting with suspicion."
                    echidna2 "Looks like the jig is up!"
                    "You leapt for the Echidna, but it backflipped away just in time."
                    "Laughing maniacally, it ripped off its mask to reveal none other than the Master Thief."
                    t "That's right, it was I all along! I have stolen the eyes of Heaven and the hands of G-d, and now I use those eyes and hands to wreak mischief upon this cursed earth!"
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
                    "You leapt for the Echidna, but it backflipped away just in time."
                    "Laughing maniacally, it ripped off its mask to reveal none other than the Master Thief."
                    t "That's right, it was I all along! I have stolen the eyes of Heaven and the hands of G-d, and now I use those eyes and these hands to wreak mischief and misery upon this cursed earth!"
                    h "Stop them!"
                    "The thief fled into the forest."
                    jump thiefChase2
    label thiefChase2:
        show hand onlayer transient:
            yalign 0.65#0.743
            xalign 0.5
        menu:
            "The others chased after them."
            "If you tried to chase after the thief, turn to page 135.":
                call hideAll from _call_hideAll_22
                show forest4bg at artPos
                "The thief led you on a merry chase, until you were deep into the forest with all the others behind you."
                "You slowly closed the distance, until you finally leapt forward and grabbed their cloak."
            "If you tried to go around and cut them off, turn to page 136.":
                call hideAll from _call_hideAll_23
                show forest4bg at artPos
                "You ran deep into the forest, planning to lay an ambush for the thief. Soon, you left the others far behind."
                "You lay in wait behind a bush until you heard their running footsteps. Then you leapt out and grabbed them."
            "If you {b}have a pig{/b}, turn to page 137." if pig:
                "The pig chased after them furiously, grunting pig curses at the fleeing figure."
                call hideAll from _call_hideAll_24
                show forest4bg at artPos
                "You hid behind the bushes and lay in wait until you heard the thief's footsteps. Then you leapt out and grabbed them as your pig squealed in triumph."
    show scribble9 onlayer transient zorder 100
    "Their cloak came away with a tearing sound, and the figure before you fell apart into dust."
    "It was nothing more than a pile of dead leaves and mud, carefully posed to look like the Master Thief using a cunning series of pulleys and wires."
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
        t "You see, I've heard of you. They say you're a good little Christian, and you always do as you're told."
        t "Why not change that?"
    elif godfather == "Black":
        t "You see, I've heard of you. They say you're a strange one. You lurk out late at night and scare people."
    t "I know you live near the Mushroom, who has riches nearing those of the King of Kings."
    t "I plan to go there tonight and take her for all she's worth. Want to join? We could split the profits in a fair share."
    if stuffStolen:
        t "I'll give you back everything I stole into the bargain. Promise."
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
                call hideAll from _call_hideAll_25
                show forest2bg at artPos
                "Before they could react, you slipped away from them and ran away into the woods, heading for the Mushroom's house."
                call hideAll from _call_hideAll_26
                show stranglerfigbg at artPos
                "Soon you stood knocking at the Mushroom's door, panting for breath and covered in scrapes from the journey."
                jump mushroom1

# Act 2, Chapter 3B: Journey with the Thief
#When you follow the thief to the mushroom's lair
label thief3:
    "The thief strode ahead on their long, long legs, and you had to run to keep up. Their nimble fingers were constantly moving, grabbing leaves off the trees or small rocks from the ground to fiddle with, and they couldn't seem to keep a single part of their body still for even a second."
    if pig:
        "Your pig trotted along beside you."
    call hideAll from _call_hideAll_39
    show nightbg at artPos
    "The night grew dark."
    call hideAll from _call_hideAll_40
    show riverbg at artPos
    "You passed a river."
    call hideAll from _call_hideAll_41
    show darkforestbg at artPos
    "You passed a rocky coast."
    call hideAll from _call_hideAll_42
    show ruinsbg at artPos
    "You passed the ruins of the sixth age, a grim reminder of the inevitable destruction fast approaching your world."
    call hideAll from _call_hideAll_43
    show treenightbg at artPos
    "You passed a tree."
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
                #TK: Make this go down when your family is disappeared
                "If you talked about your family, turn to page 88." if not thiefFam:
                    if godfather == "Red":
                        if persistent.vanished == 0:
                            pov "I have a family. Twelve brothers and sisters. No mother anymore, though. She was driven into the grave by my wicked ways."
                        elif persistent.vanished == 1:
                            pov "I have a family. Ten brothers and sisters. No mother anymore, though. She was driven into the grave by my wicked ways."
                        elif persistent.vanished == 2:
                            pov "I have a family. Four brothers and sisters. No mother anymore, though. She was driven into the grave by my wicked ways."
                        t "My condolences and/or congratulations!"
                    else:
                        if persistent.vanished == 0:
                            pov "I have a family. Twelve brothers and sisters."
                        elif persistent.vanished == 1:
                            pov "I have a family. Ten brothers and sisters."
                        elif persistent.vanished == 2:
                            pov "I have a family. Four brothers and sisters."
                        t "How prolific your mother is! It must be hard to get a word in edgewise."
                    t "I have no family, of course. One day a horned toad sat on a magpie egg and I popped out fully formed."
                    t "I stole my first breath of air, then I stole these hands and these legs and this body of mine, and I've been stealing ever since."
                    $thiefFam = True
                    $ThiefConvo3Options +=1
                    jump thiefConvo3
                "If you talked about your new pet pig, turn to page 91." if pig and not thiefPet:
                    $thiefPet = True
                    pov "Well, because of you I have this pet pig now."
                    "The pig leapt into your arms and oinked at the thief with righteous malice."
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
                    t "Interesting. I never learned."
                    t "Too busy, you know. Schemes and such."
                    pov "Well, I can recommend it."
                    t "Perhaps I'll try it, if I can find the time."
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
                    pov "I've had this dream many times. I find myself in the middle of the forest. There is a crowd around me, but I know someone is missing."
                    pov "I look down, and I realise I have no hands. Then I look down, and realise I have no feet."
                    pov "I always know what will happen next. I will look up, into the space between the trees. Into the spiral. I am terrified, but I can't stop myself from doing it."
                    show wolf12 onlayer transient zorder 100
                    pov "I know I will see something there. Waiting for me. In the dream, I know what it is. I know what will happen when I see it."
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
                "If you turned and walked into the woods, turn to page 110." if persistent.vanished >=1:
                    t "Wait - where are you going?"
                    "Their voice faded behind you as you walked away into the darkness."
                    $clearing = "thief"
                    jump clearingInvestigate
                #"If you said nothing, turn to page 101.":
                    #t "Alright, suit yourself."
                    #jump thiefWatchThis

        label thiefWatchThis:
            t "Watch this!"
            "They caught hold of a tree bough and spun around on it, then leapt off and landed on one foot on a nearby branch, balancing precariously."
            show hand onlayer transient:
                yalign 0.65#0.743
                xalign 0.5
            menu:
                t "Eh? Eh?"
                "If you clapped politely, turn to page 103.":
                    t "Thank you, thank you!"
                    "They bowed, blew you a kiss, then drew roses out of the cuffs of their coat and tossed them out to an imaginary audience. Then they leapt down."
                    t "Anyway, enough of my talents for now. We're here!"
                "If you enquired as to the source of the thief's incredible abilities, turn to page 108":
                    t "The goblins taught me."
                    "They leapt off the branch and landed with perfect poise, posing dramatically."
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
        label thiefFig:
            call hideAll from _call_hideAll_44
            show stranglerfigbg at artPos
            if pig:
                "The colossal roots of the Mushroom's strangler fig rose above you. The pig sniffed at them suspiciously."
            else:
                "The colossal roots of the Mushroom's strangler fig rose above you."
            t "Alright. Here's the job."
            "They drew a floor plan in the dirt."
            t "The treasure is in the central chamber, here. The front door can only be opened with a password."
            t "There's another entrance up through the canopy, guarded by banksia boys."
            t "Or we could try to get in here, through an underground river patrolled by an old crocodile."
            if persistent.mushroomVanished:
                "They kept looking over your shoulder into the darkness beyond. You noticed bags under their eyes."
            show hand onlayer transient:
                yalign 0.65#0.743
                xalign 0.5
            menu:
                t "So what's the plan, chief?"
                "If your notes say that you {b}know the password{/b}, turn to page 131.":
                    if persistent.mushroomVanished:
                        pov "I know the password. We can walk straight in the front door."
                    else:
                        pov "I saw the mushroom put in the password. We can walk straight in the front door."
                    t "You devil, you. Lead the way!"
                    "You walked up to the fig and cut the vines and swamp flowers away to reveal the small blue door, inlaid with precious moonstone and intricate engravings."
                    pov "Gorge, guzzle, gulp and grab; never shall this wound scab."
                    jump thiefMushroomCavern
                "If you climb up and go in from above, turn to page 142.":
                    t "Great idea. We'll draw you into a life of crime yet."
                    call hideAll from _call_hideAll_45
                    show canopybg at artPos
                    if pig:
                        "You climbed up through the canopy, holding your pig tight in your arms. Before you knew it, a gaggle of Banksia seeds dropped down all around you. Their many mouths gabbled at you in a crazed frenzy."
                    else:
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
                                        "You walked down past the banksias, and found a little yellow door in the tree."
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
                        if pig:
                            "The pig tackled Scraggs McKenzie and he fell from the branch, screaming vengeance."
                        "The banksia boys swung their leaves around them like sawblades, and their dozens of eyes opened and closed in fury."
                        if pig:
                            "The thief dragged you up and grabbed the pig. You all darted and dived through the melee until you dove through a door in the tree trunk and slammed it behind you."
                        else:
                            "The thief dragged you up and you both darted and dived through the melee until you dove through a door in the tree trunk and slammed it behind you."
                        "You fell to the floor, gasping. You had some bruises, and you saw that the Master Thief had suffered a slash across their arm."
                        t "N-nothing to worry about."
                        if pig:
                            "The pig nuzzled them with a concerned oink."
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
                                        if pig:
                                            "You pulled them up, and you all crept through the tree until you found a rotted red door."
                                        else:
                                            "You pulled them up, and you both crept through the tree until you found a rotted red door."
                                        jump thiefMushroomCavern
                                    "If you tried to push the thief onwards, turn to page 184":
                                        pov "Come on. Don't talk like that."
                                        "The thief shrugged."
                                        t "I never learned any other way to talk."
                                        "They struggled to their feet, and you both crept through the tree until you found a rotted red door."
                                        jump thiefMushroomCavern
                "If you entered through the underground river below, turn to page 173.":
                    t "Great idea. We'll draw you into a life of crime yet."
                    call hideAll from _call_hideAll_46
                    show mushroomcaveunderbg at artPos
                    if pig:
                        "You leapt down a well with the pig in your arms, and crept up the underground river until you came across an ancient, leviathan saltwater crocodile."
                    else:
                        "You leapt down a well and crept up the underground river until you came across an ancient, leviathan saltwater crocodile."
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
                call hideAll from _call_hideAll_47
                show mushroomcavebg at artPos
                if mushroomCavernSeen:
                    "The door opened to reveal the vast cavern of glittering treasure far below. You saw the gold and gems and red mist of incense, just as it was earlier in the night."
                else:
                    "The door opened to reveal a vast cavern of glittering treasure far below."
                    "It was the hollow interior of an ancient strangler fig. The deep cavern reached down into the earth, cold as ice despite the heat outside."
                    "The floor of the cavern was piled with rubies and pearls and glinting onyx and solid gold pieces, larger than your fist."
                    "All across the room were lush silks and pillars of precious metals of every type and all manner of riches that would turn the King of Kings green with envy."
                    "You inhaled the rich dark scent of incense, and saw glimmering magenta smoke roll across the room and coat it all in a dark haze, smelling of the most incredible spices and herbs and enchanting odours."
                t "Jackpot."
                "The thief tied a rope around their waist, tied the other end to the doorknob, and began to lower themselves down to the treasure below."
                t "Come on!"
                show hand onlayer transient:
                    yalign 0.68#0.743
                    xalign 0.5
                menu:
                    "You saw a jeweled scimitar stuck into the wood nearby."
                    "If you helped the thief with their plunder, turn to page 185.":
                        if pig:
                            "You tied a rope around you and the pig and lowered yourself down to help the thief."
                        else:
                            "You tied a rope around your waist and lowered yourself down to help the thief."
                        "They grabbed up a shining goblet, encrusted with rubies and amethysts and chunks of moonstone carved in the shape of wild flowers."
                        "As soon as they did, you heard a terrible rumbling and groaning all around you, and the walls shook. The Mushroom emerged from a trapdoor in the floor and looked around wildly."
                        t "Whoops. Looks like we'd better work fast!"
                        jump thiefFinale
                    "If you grabbed the scimitar, betrayed the thief and defended the mushroom's riches, turn to page 186.":
                        "You grabbed the scimitar and slashed through the rope in a single motion."
                        "The form of the thief fell down below. As it fell away, you saw it was nothing but a raggedy old cloak stuffed with straw. You felt a sharp point at your back."
                        t "You're learning, my friend. But not quite quick enough. En Garde!"
                        "You whirled around and barely parried a slash from the thief, but the force of the blow sent you tumbling down and onto a pile of diamonds."
                        "You pulled yourself up and fought fiercely across the glittering hills of treasure, gold pieces sliding away with every step."
                        if pig:
                            "The pig left bravely at the Master Thief, but they effortlessly dodged and it went rolling down the hill, squealing wildly."
                        "The Master Thief effortlessly riposted your blows with one hand, while the other hand darted around grabbing nearby gems and stuffing them into their cloak."
                        jump mushroomFinale

#The normal finale of the thief's story
label thiefFinale:
    pov "Run!"
    "You grabbed the thief's hand and tried to pull them away as they stuffed gems and jewels into their pockets."
    m "So you've decided to steal from our Lady after all?"
    if mushroomCurse:
        m "I knew should never have given you a second chance. Curse first, ask questions later, darling, that's what I've always said."
    else:
        m "How trite. I hoped you had the originality to avoid rehashing such dull tropes, darling."
    call hideAll from _call_hideAll_48
    show mushroomgardensbg at artPos
    "The floor began to fall away before you, and all the golden treasure sprouted and turned into jellyspots and rust fungus and dog lichen and yellow staghorn and blue mould which bloomed in all directions."
    if pig:
        "The pig leapt into your arms, grunting in fear."
    "The black tongues of the earth wriggled out of the treasure horde and lashed around you, and out from the soil emerged ten dozen mushrooms, all identical to the one in front of you. For weapons they held puffballs and shield fungi and spindle toughshanks, and they walked towards you with slow but terrible confidence."
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
                m2 "Disappointing."
                m4 "Agreed. A lackluster piece. One suspects the artist's best days are behind [him]."
                "Their attacks began to push you and the thief towards the edge of the ragged hole in the floor."
                jump thiefMushroomBattle
            "If you took the opportunity to steal some spare gems, turn to page 177." if not mushroomGems:
                $mushroomGems = True
                "You ducked back and crammed some tumbling gems into your pockets with your spare hand."
                "As you did, they burst apart into puffballs which sent a waft of spores out of your pockets. The room began to spin around you."
                "You slipped on a scarlet elf cap and began to fall into the pit. Below you, you could hear the slow beating of an ominous heart, and you looked down and saw pale flesh twisting languidly in the darkness of the earth."
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
                "A brilliant light shone through the windows of the cavern. There was the sound of thundering wheels."
                call hideAll from _call_hideAll_128
                play sound pageFlip
                show trainfullbg
                ""
                play sound pageFlip
                call hideAll from _call_hideAll_129
                show trainbg at artPos

                "A train crashed through the walls of the cavern."
                show train onlayer transient zorder 100
                "It was swarming with wild and chaotic shapes of all manner of monsters, and you could see a team of things holding onto the front and laying tracks in front of the train as fast as they could as it swerved through the cavern, fungi leaping aside before it."
                #m "Really? A Deus Ex Machina, at this stage?"
                t "Grab on!"
                "Behind you the mushrooms closed in, throwing puffballs that exploded in clouds of spores around you. You ran up to the side of the train as it clattered along."
                "The thief pushed you up to grab onto the side of the carriage, then you reached down and pulled them up beside you."
                "The train whistled with full force, gathering speed until it smashed through the other wall of the cavern and shot through the trees of the forest, leaving the mushrooms behind."
                t "Well! Did you ever doubt me?"
                call hideAll from _call_hideAll_51
                show goblinint2bg at artPos
                "A thousand goblin shapes writhed up out of the train to hold up the thief in celebration, and you heard a cheer rise up from a thousand goblin throats."
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
                            call hideAll from _call_hideAll_52
                            show goblinint2bg at artPos
                            "This part of the train was some kind of bar or gambling hall. Looking up through a maze of trapdoors in the roof, you could see there were many floors stacked above this one. Bathhouses, gardens, workshops and observatories."
                            if pig:
                                "Your pig nestled into the chair beside you and began to chat to the nearby goblins in the language of mud."
                            $goblinSit = True
                            jump goblinTrain
                        "If you looked outside, turn to page 195." if not goblinLook:
                            call hideAll from _call_hideAll_53
                            show trainbg at artPos
                            "A team of goblins hung off the back of the train and picked up the tracks behind it, then climbed around to hand the tracks to the goblins at the front, who laid them in front of the train as it squeezed through the trees of the forest."
                            $goblinLook = True
                            jump goblinTrain
                        "If you accepted a goblin beverage, turn to page 196." if not goblinDrink:
                            call hideAll from _call_hideAll_54
                            show goblinint2bg at artPos
                            "The goblins poured you dozens of goblin brews, bubbling ales and steaming warm ciders, goblin wines that oozed with red fog and goblin brandies that froze and melted and froze again as you drank them."
                            "Foolishly, you drank deeply of the brews. You guzzled them down until you could drink no more, until your vision was a haze and the brew ran down your mouth and drenched your clothes, and still you thirsted for them."
                            "From that day on, no other drink would ever be able to quench your thirst, and you would always shiver and feel cold without the wild drunken feeling of warmth the goblin drinks gave you."
                            goblin2 "On the house! Just for tonight."
                            $goblinDrink = True
                            jump goblinTrain
                        "If you went to find the Master Thief, turn to page 197.":
                            call hideAll from _call_hideAll_55
                            show goblinintbg at artPos
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
                            goblin4 "I declare your apprenticeship complete!"
                            goblin4 "And so, with all the power invested in me, I hereby dub thee..."
                            goblin4 "{b}The Junior Thief!{/b}"
                            "She held up the thief's hand and all the goblins roared and danced and sang and rolled around in celebration."
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
                                            "Your pig was quickly drawn into a wager, with it's greatest hopes and dreams as the stakes. Fortunately it won, and was granted a small kingdom in the mountains as it's prize. It would go on to raise a mighty pig empire there, and rule over it for the rest of its days."
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
                                        call hideAll from _call_hideAll_56
                                        show trainbg at artPos
                                        "You found them sitting on the rear balcony with their legs over the edge, watching the trees and hills roll by in the smoky night."
                                        t "Hi."
                                        "You sat there with them in silence for a while, looking out."
                                        t "Oh, before I forget."
                                        if stuffStolen:
                                            "They handed back the suckling pig and all of the loose change stolen from the village, along with your stolen possessions and some extra money for payment."
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
                                                            jump thiefStory
                                                        "To hear the incredibly short version, turn to page 188.":
                                                            pov "Well, I don't have a lot of time..."
                                                            t "My parents are terrible. They sent me to the goblins to train as a thief. Now they're coming back to take me away."
                                                            jump thiefStoryEnd

#The thief's tragic backstory, related in their finale.
label thiefStory:
    call hideAll from _call_hideAll_57
    show nightbg at artPos
    if thiefShort:
        t "Right. Long ago, the Lord came to visit my parents. I heard my mother gesture to me, and talk to the Lord of me thus:"
        thiefmum "Inside all good people there dwells a golden soul, given by you, oh Lord. But as soon as you look, anyone can see this one has nothing but a hollow nest of spiders and rats inside. What trade can I teach such a one as this?"
        #TK: Some kind of text effect for g-d's speech
        t "The Lord thought on this, and said to me thus:"
        miw "You shall be a Thief. It is the work your wicked hands are made for."
        t "My parents took me to the goblins to learn the art of Thievery as the Lord instructed."
        t "One of the Goblin Queens sat and talked with me for a long time. Then they went to my parents and said:"
        goblinQueen "Your child will be taught well. We will keep them as an apprentice for one year."
        goblinQueen "Come back then, and if you can still recognize them, I won't take any money for my services and you can take them away."
        goblinQueen "But if you cannot recognise them, you must give me three hundred talers, and they must be allowed to go free and do as they will."
        t "My parents agreed, and went home. And now, that year has passed."
        t "Tonight, my parents will be here soon to take me away, and they always carry the Lord in their hearts."
        t "As soon as they arrive, He will instantly see me for the wretch I am. Then I will be whisked away from here again."
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
        t "The Lord thought on this, and said \"Bring all your children before me.\" To the first child He said:"
        miw "You shall become a powerful King."
        t "Then to the second, and third, and so on down the line:"
        miw "You shall become a Duke."
        miw "You, a rich Merchant."
        miw "You, a Tanner. You, a Shoemaker. You, a Butcher. You, a Beggar."
        t "Then He finally reached me at the end of the line."
        miw "And you shall be a Thief."
        t "My parents took me to the goblins to learn the art of Thievery as the Lord instructed."
        t "One of the Goblin Queens sat and talked with me for a long time. Then they went to my parents and said:"
        goblinQueen "Your child will be taught well. We will keep them as an apprentice for one year."
        goblinQueen "Come back then, and if you can still recognize them, I won't take any money for my services and you can take them away."
        goblinQueen "But if you cannot recognise them, you must give me three hundred talers, and they must be allowed to go free and do as they will."
        t "My parents agreed, and went home. And now, that year has passed."
        t "Tonight, my parents will be here soon to take me away, and they always carry the Lord in their hearts."
        t "As soon as they arrive, He will instantly see me for the wretch I am. Then I will be whisked away from here again, and live in the coal chute forever after."
        jump thiefStoryEnd
    label thiefStoryEnd:
        call hideAll from _call_hideAll_58
        show trainbg at artPos
        "They sighed."
        show hand onlayer transient:
            yalign 0.7#0.743
            xalign 0.5
        menu:
            t "There's still time. I can sneak away, and get myself arrested. Then I'll be safe in a jail cell for a bit."
            "If you gave them an inspirational speech, turn to page 191.":
                "You took their hand and squeezed it."
                pov "Come on. Haven't you escaped the wrath of the Lord and the Law all your life? Haven't you stolen fire and cheated death and escaped the hangman's noose at every turn?"
                pov "You've got this. No-one is better at hiding from G-d than you."
                "The thief held your hand tight."
                t "Thank you."
            "If you promised to stay with them no matter what, turn to page 192.":
                "You took their hand and squeezed it."
                pov "Don't do that. I'll stay with you."
                pov "If your parents want to take you, they'll have to take both of us."
                "The thief held your hand tight."
                t "Thank you."
        call hideAll from _call_hideAll_59
        show darkforestbg at artPos
        "In a few short hours, the train stopped on a rocky stretch of coast, and the thief's mother and father came to meet it."
        if godfather == "White" or godfather == "Red":
            "Midnight was approaching fast. You felt a cold chill come over you. Soon, your Godfather would come and take you away."
        "The goblins lined up you and the thief with twelve goblins on a tree branch, all of you transformed to become king parrots and sparrows and magpies and birds of every type."
        if godfather == "White":
            "Just at that moment, the clock struck midnight."
            call hideAll from _call_hideAll_60
            show godbg at artPos
            "The clouds parted and an unnatural sun shone through them,  bright as a searchlight in the dark of night."
            "You felt the hot rays of the Lord's gaze upon you, sweeping the line of birds. Your skin blistered with sunburn as it struck you."
            miw "Where is my godchild?"
            thiefmum "Yes. And where is my child?"
            "You felt the thief shake beside you."
            goblin4 "If you want 'em, you'll have to pick them out of the line!"
            "The Lord's gaze moved down the branch, hovering over the thief in their form as a blackbird."
            "Their breath grew short, and they looked straight ahead, trying not to seem as though anything was wrong."
            if pig:
                "The pig looked up from the ground with anticipation and fear."
            "After a long time, His gaze moved on down the line, hovering over each in turn. Finally, He spoke."
            miw "These are the ones we seek."
            "Rays of light beamed down on two cinnamon cockatiels at the very end of the line."
            "With a shout they burst into smoke, and revealed themselves to be goblins."
            "The whole line erupted into goblin smoke, and the two of you were revealed. In a flash, the goblins turned both the parents into hideous grubs which squirmed away and were buried in the dirt. The Lord cursed in disgust and vanished back behind the clouds, and the whole train leapt up in celebration."
            call hideAll from _call_hideAll_61
            show darkforestbg at artPos
            "The thief stared about in amazement."
            t "But... "
            t "I felt the eyes of G-d upon me. How could He not see all the rot inside me?"
            pov "There is none. There never was."
        else:
            goblinQueen "Choose your child out of the line, and their life will be yours once more. But fail, and you must leave them with us."
            "The thief's mother stood and stared for a long time, moving down the line slowly."
            call hideAll from _call_hideAll_62
            show godbg at artPos
            "As she looked over you, the clouds parted and you felt the hot, bright rays of the Lord's gaze pierce through you, lighting up every scrap of darkness and guilt in your soul. The thief shook beside you."
            "Their breath grew short, and they looked straight ahead, trying not to seem as though anything was wrong."
            if pig:
                "The pig looked up from the ground with anticipation and fear."
            "After a long time, she moved on down the line. She stepped away and conferred with her husband. Finally, she spoke."
            call hideAll from _call_hideAll_63
            show darkforestbg at artPos
            thiefmum "This one is our child."
            "She pointed to a cinnamon cockatiel on the very left of the line."
            "With a shout, it burst into smoke, and revealed itself to be a goblin."
            "The whole line erupted into goblin smoke, and the two of you were revealed. In a flash, the goblins turned both the parents into hideous grubs which squirmed away and were buried in the dirt. The blazing light vanished back behind the clouds, and the whole train leapt up in celebration."
            "The thief stared about in amazement."
            t "But... "
            t "I felt the eyes of G-d upon me. How could He not see the rot inside me?"
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
                            t "But I am the sovereign of thieves, and all crooks owe me allegiance."
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
        "You wrapped the Master Thief in a crushing bear hug, and lifted them up on your shoulders."
        if godfather == "Red" or godfather == "White":
            "You were both free at last."
        if pig:
            "The pig leapt up joyfully into your arms, and you passed it up to the thief to lift aloft in triumph."
        call hideAll from _call_hideAll_64
        show trainbg at artPos
        "You leapt on the goblin train, and the thief and the goblins danced and celebrated all through the night."
        jump thiefEnd

        label thiefEnd:
            if goblinFood or goblinDrink:
                show hand onlayer transient:
                    yalign 0.7#0.743
                    xalign 0.5
                menu:
                    "Alas, having tasted the goblin fruits, you could never return home to your family again."
                    "If you married the thief, turn to page 242.":
                        "After many adventures, the Goblin Queen married you on the train. There was a joyous goblin riot for forty days and forty nights."
                        if pig:
                            "Your pig watched over the wedding ceremony with tears in his eyes, and stayed with you as your constant companion and friend."
                        "You lived there in happiness for all of your days, venturing from place to place with wild abandon."
                        if godfather == "Black":
                            jump thiefDeath
                        else:
                            call endStamp from _call_endStamp_8
                            "You live there still, rattling across the whole world on the Goblin Train, and you will have no rest until the Day of Judgement."
                            "..."
                            "Oh?"
                            "And what happened to the mushroom, you ask?"
                            jump mushroomDisappears

                    "If you remained good friends with the thief, turn to page 246.":
                        "You lived on the train in happiness with your friend the thief for all of your days, venturing from place to place with wild abandon."
                        if goblinCelebrate and pig:
                            "Your pig wished you a fond farewell, and went to live in his kingdom in the mountains."
                        elif pig:
                            "Your pig stayed with you as your constant companion and friend."
                        if godfather == "Black":
                            jump thiefDeath
                        else:
                            call endStamp from _call_endStamp_15
                            "You live there still, rattling across the whole world on the Goblin Train, and you will have no rest until the Day of Judgement."
                            "..."
                            "Oh?"
                            "And what happened to the mushroom, you ask?"
                            jump mushroomDisappears
            else:
                "In the morning, you were faced with a choice. "
                "Because you had not yet tasted the goblin fruits, you could still return to your family and the world of humans."
                show hand onlayer transient:
                    yalign 0.64#0.743
                    xalign 0.5
                menu:
                    "What did you decide?"
                    "If you bade the thief farewell and returned to your family, turn to page 243.":
                        "You bade a tearful farewell to the thief, and returned back to your world among the humans, where you lived for many years in joyous happiness."
                        if godfather == "Black":
                            jump thiefDeath
                        else:
                            "There you stayed for the rest of your days, growing slowly older. On cold nights, you swear you could still hear the whistle of the Goblin Train, and the laughter of the thief in the wind."
                            call endStamp from _call_endStamp_9
                            "And then came an elephant with a very long snout, and it blew the story out."
                            #Wolf: Kills mushroom
                            "..."
                            "Oh?"
                            "What happened to the mushroom, you ask?"
                            jump mushroomDisappears

                    "If you stayed on the goblin train and remained good friends with the thief forever after, turn to page 244.":
                        "You lived on the train in happiness with your friend the thief for all of your days, venturing from place to place with wild abandon."
                        if goblinCelebrate and pig:
                            "Your pig wished you a fond farewell, and went to live in his kingdom in the mountains."
                        elif pig:
                            "Your pig stayed there as your constant companion and friend."
                        if godfather == "Black":
                            jump thiefDeath
                        else:
                            call endStamp from _call_endStamp_10
                            "You live there still, rattling across the whole world on the Goblin Train, and you will have no rest until the Day of Judgement."
                            "..."
                            "Oh?"
                            "And what happened to the mushroom, you ask?"
                            jump mushroomDisappears

                    "If you stayed on the goblin train and married the thief, turn to page 248.":
                        "After many adventures, the Goblin Queen married you on the train. There was a joyous goblin riot for forty days and forty nights."
                        if pig:
                            "Your pig watched over the wedding ceremony with tears in his eyes."
                            if goblinCelebrate:
                                "After the wedding he wished you a fond farewell, and went to live in his kingdom in the mountains."
                            else:
                                "After the wedding, he stayed with you there as your constant companion and friend."
                        if godfather == "Black":
                            jump thiefDeath
                        else:
                            call endStamp from _call_endStamp_11
                            "And if you have not died, you live there still. On windless nights, your siblings whisper that they can hear your laughter, and the rattling wheels of the goblin train."
                            #Wolf: Kills mushroom
                            "..."
                            "Oh?"
                            "What happened to the mushroom, you ask?"
                            jump mushroomDisappears

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
            "But as you spoke, there was a knock on the door, and the goblins opened it to reveal the wise mushroom from the forest."
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
                        pov "Alright. I'm ready."
                        m "No-one's ever ready. But there's no time left."
                        "She gently took you down to the kingdom of Death."
                        call endStamp from _call_endStamp_12
                        "And what you did after that, none who live can say."
                        #Wolf: Kills toad
                        "..."
                        "Oh?"
                        "What happened to the mushroom, you ask?"
                        jump mushroomDisappears

#==========Mushroom Disappears
label mushroomDisappears:


    # call hideAll from _call_hideAll_151
    # show nightbg at artPos
    # stop music fadeout 15.0
    # "You lay down to join her and looked up at the sky above. A great, long sigh slowly eased out of her."
    # m "Have you ever looked back at your life and tried... tried to calculate the sheer volume of it that you've wasted? The just ungodly amount of time that you've let slip away?"
    # call hideAll from _call_hideAll_152
    # show night2bg at artPos
    # m "Of course I don't mean the time spent having picnics or afternoon naps, or watching the sky. That time isn't wasted."
    # m "I mean the time spent doing things you don't want to do, for people you don't care about."
    # call hideAll from _call_hideAll_153
    # show night3bg at artPos
    # m "Those long decades spent paying rent, attending meetings, hunched over desks, travelling to work and back, doing all those petty grinding little tasks every day..."
    # call hideAll from _call_hideAll_154
    # show night4bg at artPos
    # m "It's horrifying. How incalculable a waste."
    # "There was the sound of scratching. It seemed to come from somewhere inside you."
    # call hideAll from _call_hideAll_155
    # show night5bg at artPos
    # m "How many minutes and hours and days and years have vanished into that black yawning pit. It's impossible to even fit the number into my mind. It's nightmarish. The stars in the sky. The grains of sand on the beach... I can't even begin to take it in."
    # call hideAll from _call_hideAll_156
    # show night6bg at artPos
    # m "But every time you think about it, every time that number starts to creep into your mind, you think \"There's still time,\" don't you?"
    # "The wine in your glasses rippled into complicated, twisting patterns. Like the entrails of beasts, from which omens might be read."
    # call hideAll from _call_hideAll_157
    # show night7bg at artPos
    # m "There's still time to chase that dream, there are still years left to me, I'll make it someday, I can turn this around, it'll all work out in the end! I'll start tomorrow."
    # call hideAll from _call_hideAll_158
    # show night8bg at artPos
    # m "But there are no tomorrows left."
    # call hideAll from _call_hideAll_159
    # show night9bg at artPos
    # "The earth shook beneath you. You almost thought you heard the impact of great footfalls. Almost upon you now."
    # m "I can't say that anymore. It's done. The hours I spent are all the hours I'll ever have."
    # call hideAll from _call_hideAll_160
    # show night10bg at artPos
    # m "And... all throughout my life, the moments where I did something I really enjoyed were like small gasps of air between years of drowning."
    # "The night was getting darker and darker."
    # call hideAll from _call_hideAll_161
    # show night11bg at artPos
    # m "I had to plan them and save up for them and spend every day just trying to hold out for the next one. Those tiny, tiny moments where I got to be alive."
    # call hideAll from _call_hideAll_162
    # show night12bg at artPos
    # "Something was very close to you now. You didn't dare look. There was a smell like something rotting. A sound like something coiling in the grass."
    # m "All I have left now is that number. That percentage of waste."
    # play audio wolfApproaches
    # #stop ambient2 fadeout 2.0
    # #stop ambient1 fadeout 20.0
    # call hideAll from _call_hideAll_163
    # show darkforestbg at artPos
    # call hideAll from _call_hideAll_164
    # show night13bg at artPos
    # m "It'll never get any smaller. It's done. It's all done."
    # "Tears ran down her cheeks. She made no effort to hide them anymore. "
    # call hideAll from _call_hideAll_165
    # show night14bg at artPos
    # m "Hold me, please."
    # "You tentatively put your arm around her, and she nestled into your shoulder and wept."
    # "You held her tight as you stared out into the night sky."
    # $persistent.vanished +=1
    # $persistent.mushroomVanished = True
    # $persistent.starsVanished = True
    # #$purge_saves()
    # $ renpy.block_rollback()
    # show wolf14 onlayer transient zorder 100
    # "It was pitch black. No stars or moon brightened that abyss."
    # "You reached for the wine bottle, and realised there was none."
    # "There were no wineglasses. There was no food."
    # "You felt the touch of moss underneath you. There was no blanket."
    # "You looked down."
    # "You were holding nothing at all. Your arms were embracing thin air."
    # "Why were you here?"
    # "You must have needed a rest. A night outdoors. "
    # "All of us need some time to ourselves every now and then, don't we?"
    # "No harm in that."
    # "You stood up. Brushed away the moss. Breathed in the cool night air."
    # "You felt warm, full, and sad, for no reason you could name."
    # "Finally you began the long walk home in silence, with the dark night sky looming above you."
    # "There's nothing else left to tell."
    # "That's the end."
    # call endStamp from _call_endStamp_42
    # "Run away with it now, as fast as you can."
    # jump end

    #night2bg to night14bg

    # play music hunted1
    # stop music fadeout 6
    # play music2 [ "<sync music>audio/hunted2.wav", "audio/hunted2.wav" ] fadein 1
    # stop music2 fadeout 6
    # play music3 [ "<sync music2>audio/hunted3.wav", "audio/hunted3.wav" ] fadein 1
    # stop music3 fadeout 6
    # play music4 [ "<sync music3>audio/hunted4.wav", "audio/hunted4.wav" ] fadein 1
    # stop music4 fadeout 6
    # play music5 [ "<sync music4>audio/hunted5.wav", "audio/hunted5.wav" ] fadein 1
    # stop music5 fadeout 6
    # play music6 [ "<sync music5>audio/hunted6.wav", "audio/hunted6.wav" ] volume 2.0 fadein 1




    $ renpy.block_rollback()
    call hideAll from _call_hideAll_236
    play sound pageFlip
    show nightbg at artPos

    "After you fled, the mushroom was left standing outside her tree. She looked out at the vanishing smoke of the goblin train in the distance and sighed."
    call hideAll from _call_hideAll_256
    show night2bg at artPos
    "A giant hole had been torn in the strangler fig, and the untold riches of her domain were leaking out all over the place."
    #Have her go outside to look for you
    #Then the stars blink out, one by one
    #She flees into the cavern. Things disappear from the cavern, one by one.
    call hideAll from _call_hideAll_257
    show night3bg at artPos
    m "Oh well."
    call hideAll from _call_hideAll_258
    show night4bg at artPos
    m2 "Nothing to do about it now."
    call hideAll from _call_hideAll_259
    show night5bg at artPos
    m3 "Perhaps a drink?"
    call hideAll from _call_hideAll_260
    show night6bg at artPos
    "She pulled a bottle of wine from one of the scattered treasure-piles that had fallen out in the commotion, and popped the cork."
    call hideAll from _call_hideAll_261
    show night7bg at artPos
    m2 "Wonderful idea, darling."
    call hideAll from _call_hideAll_262
    show night8bg at artPos
    m2 "We can always start the cleanup tomorrow."
    call hideAll from _call_hideAll_263
    show night9bg at artPos
    play music hunted1
    m "Sisters... does the sky seem darker than normal to you?"
    call hideAll from _call_hideAll_264
    show night10bg at artPos
    m3 "Hmmm?"
    call hideAll from _call_hideAll_265
    show night11bg at artPos
    "They looked out into the night."
    call hideAll from _call_hideAll_266
    show night12bg at artPos
    "There was a sound from the trees. Like the howling of the wind."
    call hideAll from _call_hideAll_267
    show night13bg at artPos
    m3 "Oh no. No."
    call hideAll from _call_hideAll_268
    show mushroomcavebg at artPos
    stop music fadeout 6
    play music2 [ "<sync music>audio/hunted2.wav", "audio/hunted2.wav" ] fadein 1
    "She rushed back inside and slammed the door behind her."
    m2 "Courage. We knew this day would come."
    m3 "I just didn't realise it would be so soon!"
    m "We'll have to run. Come on-"
    stop music2 fadeout 6
    play music3 [ "<sync music2>audio/hunted3.wav", "audio/hunted3.wav" ] fadein 1
    "But as she looked around for her sisters, she realised she was alone."
    "There was only one mushroom there. Standing alone, in the centre of an empty room."
    "There had never been anything more."
    "The treasure was gone. The floorboards were bare."
    "Through the hole in the tree, she could see the night sky. There were no stars."
    #"Things start disappearing around her. The treasure disappears. The Walls disappear. She tries to retreat and lock the door, carrying a bottle of wine."
    call hideAll from _call_hideAll_237
    show mushroombasementbg at artPos
    #Finally she flees into the basement.
    stop music3 fadeout 6
    play music5 [ "<sync music3>audio/hunted5.wav", "audio/hunted5.wav" ] fadein 1
    "She grabbed the bottle of wine, ran to her hidden chamber and locked the door tight."
    "It was too late, of course."
    call wolfApproaches from _call_wolfApproaches_5

    "The wolf was already inside."
    #Her sisters / selves disappear, one by one.
    "She turned to grab the door and escape."
    "But there was no door. There never was. Nothing but smooth, featureless wall."
    "She turned, and held the bottle up like a club."
    m "Get out, beast. It's not time yet. Get out."
    stop music5 fadeout 6
    play music6 [ "<sync music5>audio/hunted6.wav", "audio/hunted6.wav" ] fadein 1

    "Get out, Mushroom?"
    "But how?"
    "This room is the only thing that exists. There is nothing outside. There is nowhere but here."
    "That's the way it's always been."
    "She screamed and clawed at the walls."
    "But there were no walls."
    "There were no doors. There were no windows. There was no floor."
    "There was no air. There was no light. There was no space."
    $persistent.vanished +=1
    $persistent.mushroomVanished = True
    $persistent.vanishedLast = "Mushroom"
    $persistent.starsVanished = True
    #$purge_saves()
    $ renpy.block_rollback()

    show wolf13 onlayer transient zorder 100
    "And then there was nothing at all."
    "Nothing but a bottle of wine, that fell through the emptiness and smashed into pieces."
    call endStamp from _call_endStamp_23
    "It was never seen or heard from again."
    jump end

#==========Solo path
#The thief's path if the mushroom has disappeared
label thiefSolo:
    #t "Well! Did you ever doubt me?"
    call hideAll from _call_hideAll_130
    show goblinint2bg at artPos
    "A thousand goblin shapes writhed up out of the train to hold up the thief in celebration, and you heard a cheer rise up from a thousand goblin throats."
    "Some had the heads of bats, some had the paws of cats, six heads, three heads, five arms, ten tails, and they bristled with tails and wings and fur and scales."
    "One crawled like a snail, one prowled like a wombat, one looked like seven doves tied together with string. All of them had a chaos of forms the likes of which you had never seen."
    "A dozen hands clapped you on the back and drew you into the train carriage."
    goblin1 "Have a drink with us! Any friend of the thief's is a friend of ours."
    goblin2 "Aye, it's good to see them come back in one piece."
    goblin3 "We sent them out on a training mission, you see. To steal from..."
    goblin2 "To steal... from..."
    "A vague and desperate confusion settled on their faces."
    t "Barkeep! Drinks for everyone, on me!"
    "The confusion cleared as the goblins all joined together in a roar of approval."
    $renpy.music.set_volume(0.6, delay=10.0, channel=u'music4')
    #play music hunted1
    label thiefSoloMenu:
        call hideAll from _call_hideAll_131
        show goblinintbg at artPos
        show hand onlayer transient:
            yalign 0.64#0.743
            xalign 0.5
        menu:
            "The train was bustling with forty goblins in a chaos of forms."
            "If you sat down, turn to page 194." if not goblinSit:
                "You fell into a chair and looked around."
                call hideAll from _call_hideAll_132
                show goblinint2bg at artPos
                "This part of the train was some kind of bar or gambling hall. Looking up through a maze of trapdoors in the roof, you could see there were many floors stacked above this one. Bathhouses, gardens, workshops and observatories."
                if pig:
                    "Your pig nestled into the chair beside you and began to chat to the nearby goblins in the language of mud."
                "The thief whirled through the room - juggling, twisting, dancing, the life of the party."
                "Something was wrong with the inside of the carriage. You couldn't put your finger on it."
                "Something you couldn't see. In your blind spot."
                $goblinSit = True
                jump thiefSoloMenu
            "If you looked outside, turn to page 195." if not goblinLook:
                call hideAll from _call_hideAll_133
                show trainbg at artPos
                "A team of goblins hung off the back of the train and picked up the tracks behind it, then climbed around to hand the tracks to the goblins at the front, who laid them in front of the train as it squeezed through the trees of the forest."
                "The wind howled like a wild beast."
                t "Let's get some music going!"
                show monster onlayer transient zorder 100

                "The goblin band struck up a wild tune. The thief gestured to push them to play louder and louder until you couldn't even hear the wind outside."
                "You felt your vision warping, for some reason you couldn't define. Like staring into a magic eye puzzle."
                $goblinLook = True
                jump thiefSoloMenu
            "If you accepted a goblin beverage, turn to page 196." if not goblinDrink:
                call hideAll from _call_hideAll_134
                show goblinint2bg at artPos
                "The goblins poured you dozens of goblin brews, bubbling ales and steaming warm ciders, goblin wines that oozed with red fog and goblin brandies that froze and melted and froze again as you drank them."
                "The thief challenged the largest goblin to a drinking competition and drank them under the table."
                "Foolishly, you drank deeply of the brews. You guzzled them down until you could drink no more, until your vision was a haze and the brew ran down your mouth and drenched your clothes, and still you thirsted for them."
                "From that day on, no other drink would ever be able to quench your thirst, and you would always shiver and feel cold without the wild drunken feeling of warmth the goblin drinks gave you."
                $goblinDrink = True
                jump thiefSoloMenu
            "If you cornered the thief and asked them why you were brought here, turn to page 202.":
                $renpy.music.set_volume(1.0, delay=6.0, channel=u'music4')
                "You managed to corner the thief as they laughed in a group of goblins."
                pov "Why did you grab me and take me here?"
                t "It is my nature! Nothing more."
                t "I am the greatest thief of my generation. I was raised by these goblins to steal the moon and sun and stars, and now I have stolen you away."
                "They laughed wildly. Their face was slick with sweat."
                stop music4 fadeout 12
                play music5 [ "<sync music5>audio/hunted5.wav", "audio/hunted5.wav" ] fadein 6


                jump thiefSoloConvo
        # show darkforestbg at artPos
        # show goblinint2bg at artPos
        # show goblinintbg at artPos
        # show nightbg at artPos

    label thiefSoloConvo:
        show hand onlayer transient:
            yalign 0.68#0.743
            xalign 0.5
        menu:
            "The wild crowd of [goblinNum] goblins laughed and cheered as the train hurtled into the night."
            "If you asked the thief if something was wrong, turn to page 204." if not thiefWrong2:
                t "Nothing at all!"
                "They wiped the sweat from their forehead and gave you a charming smile. Their fingers were twisting and twitching rapidly, like they couldn't keep still."
                t "Everything is as it should be. In fact, this is the best it's ever been. Come, let us dance!"
                "They took your hand in a dance that spiralled out of control. The music was deafening. The goblin faces whirled around you until you were breathless."
                $thiefWrong2 = True
                $goblinNum-=10
                if goblinNum==0:
                    jump thiefSoloConvo2
                else:
                    jump thiefSoloConvo
            "If you told the thief you'd better get home, turn to page 210." if not thiefHome:
                t "Nonsense! There's so much joy to be had here. Stay, and celebrate with us."
                "Their smile slipped for an instant."
                t "Please stay."
                t" I don't want to be alone when it comes."
                "Then it reappeared like nothing had happened. They drank deeply of their goblin wine and gestured for you to do the same."
                t "Bedlam! I think a celebration like this calls for some smoke."
                "A goblin creature shaped like a sack full of rats nodded, and started throwing herbs into the fire."
                "Purple, twinkling smoke began to ooze out of it. As you breathed it in, your vision twisted and your limbs began to feel far away."
                $thiefHome = True
                $goblinNum-=10
                if goblinNum==0:
                    jump thiefSoloConvo2
                else:
                    jump thiefSoloConvo

            "If you asked if someone was missing, turn to page 212." if not thiefMissing:
                "The thief twisted away from you, but you managed to track them down at the dice tables. The mass of goblins seethed around you."
                pov "I need you to tell me what's going on."
                pov "I feel it. Something is missing."
                pov "I don't know how to explain it, but I feel... more alone. More than I've ever been before."
                t "Don't worry about them, my friend. They made their choice. We all did!"
                "They rolled the dice and raised their hands in triumph. The goblins around the table groaned and pushed a stack of rocks over to them."
                $thiefMissing = True
                $goblinNum-=10
                if goblinNum==0:
                    jump thiefSoloConvo2
                else:
                    jump thiefSoloConvo

#The conversation and ending of the thief's solo path, when the thief disappears
label thiefSoloConvo2:
    stop music5 fadeout 6
    play music6 [ "<sync music5>audio/hunted6.wav", "audio/hunted6.wav" ] fadein 1 volume 4.0
    $renpy.music.set_volume(0.6, channel=u'music6')
    "The music stopped. You looked around to see that the carriage was empty around you."
    "It had always been empty."
    t "I don't think this train is going fast enough, haha!"
    "Juggling spoons with their right hand, they grabbed you and pulled you through the empty carriage towards the engine room."
    call hideAll from _call_hideAll_135
    show trainbg at artPos
    "You burst out of the carriage door and into the cool night air. Without the sound of the music, you could hear the wind howling like a banshee."
    call hideAll from _call_hideAll_136
    show enginebg at artPos
    #stop music6 fadeout 6
    #play music5 [ "<sync music6>audio/hunted6.wav", "audio/hunted6.wav" ] fadein 1 volume 4.0
    $renpy.music.set_volume(1.0, delay=5.0, channel=u'music6')
    "The thief pulled you through and into the engine room, where four sooty goblins were lounging."
    t "Stoke the engine, will you? Let's see how fast this thing can move!"
    goblin4 "Aye, boss!"
    "The three goblins grabbed their shovels and set to work piling coal into the engine. The heat was intense."
    call hideAll from _call_hideAll_137
    show darknessbg at artPos
    "You looked out the window. It was pitch black outside."
    #$renpy.music.set_volume(2.5, channel=u'music')
    #
    #     show hand onlayer transient:
    #         yalign 0.64#0.743
    #         xalign 0.5
    #     menu:
    "The train moved faster and faster, and you could hear sparks coming off the wheels."
    "Your thoughts were jumbled and fractured."
    # "If you asked the thief if something was wrong, turn to page 204." if not thiefWrong2:
    #     t "Nothing at all!"
    #     "They wiped the sweat from their forehead and gave you a charming smile. Their fingers were twisting and twitching rapidly, like they couldn't keep still."
    #     t "Everything is as it should be. Come, let us dance!"
    #     "They took your hand in a dance that spiralled out of control. The music was deafening. The goblin faces whirled around you until you were breathless."
    #     $thiefWrong2 = True
    #     jump thiefSoloConvo
    #Some questions you can ask them.
    "You heard something. Like claws, scrabbling in the mechanism underneath the carriage."
    call hideAll from _call_hideAll_138
    show enginebg at artPos
    pov "Do you hear-"
    t "Nothing to worry about! Just the wind!"
    t "Help me shovel this coal, will you?"
    "You looked around. The engine room was empty, except for you and the thief."
    "You picked up a shovel and held it."
    stop music6 fadeout 12
    pov "Listen. I'll help you shovel if you tell me what's happening here."
    "You could feel the confusion blooming in your brain. Expanding blank spaces like tumours."
    pov "What's happening to me? To us? What... is this?"
    "The thief sighed."
    t "Alright. Just, please - help me shovel."
    "You both began to shove coal into the furnace. The fire flared and the room grew hotter and hotter as the train sped up."
    "The thief looked into the flames."
    t "I made a deal. A long time ago."
    t "We all took it. You will, too, in the end."
    t "Today, my debt is due. It's the end of the line."
    "The flames reflected in their dark eyes."
    t "Ah, well."
    t "Everyone gets eaten by something. Might as well be this."
    "The train screeched as it rounded a tight bend, sending you both stumbling."
    t "I think that's as fast as it'll go."
    t "Come on. Let's spend the last moment in the moonlight."

    call hideAll from _call_hideAll_139
    show darknessbg at artPos
    "They took your hand, and in a single twist of their long, long arms they pulled you both out of the engine and up onto the roof of the train."
    $renpy.music.play("audio/rememberCleanInstFull.wav", channel='music', loop=True, relative_volume=1.0)

    "You looked out across the night landscape. This haunted land stretched out before you, beautiful and terrible. The smoke stung your eyes."
    t "Here. I still have this."
    "They waved an ornate bottle of champagne at you."
    t "From my father's cellar. One of the first things I ever stole. I was saving it for a special occasion."
    "They popped the cork."
    t "Don't worry. It's not goblin drink."
    "They offered you a swig from the bottle as the train hurtled forward, teetering off the rails."
    #TK Choice: Drink or not.
    "You could hear something in the darkness behind you. Like the thudding of great paws."

    t "I had to do it."
    t "Imagine a culture built around a black hole."
    t "A tree with nothing at the root."
    #t "The centre cannot hold. The falcon cannot hear the falconer."
    t "The real world holds nothing for us. All we can do is extract as much joy as we can from each single day."
    t "Until we finally take the westward line."
    "They took a swig from the champagne bottle."
    #t "I'd take it again. I wouldn't change a single thing."
    call hideAll from _call_hideAll_140
    show nightbg at artPos
    "The howling wind abated for a single moment. The air was clear. The moon emerged from the clouds."
    "The thief leaned off the train, holding onto the smoke stack with one hand and the champagne bottle with the other."
    t "Well. This is it."
    "You looked at their face. It was fierce with exaltation. A ferocious laugh split their mouth."
    t "I did it."
    t "I'm not sorry, you hear me?"
    t "I struck out from the cruelty and bleakness and grey endless grinding of that machine, and I lived every day I was alive."
    "Their laughter faded and they looked out at the moon with relief. They handed you the champagne."
    t "I won."
    #stop music fadeout 6
    #call musicSilence from _call_musicSilence_24
    "The wind returned, howling like a monstrous beast."
    call wolfApproaches from _call_wolfApproaches_6
    "They looked at you with piercing clarity. You saw the moon reflected in their dark eyes."
    t "Thank you, [povname]. For everything."
    t "I'm sorry we didn't get more time together."
    t "If you get out, tell them..."
    t "Tell those bastards I hated them all."
    $persistent.hVanished = True
    $persistent.goVanished = True
    $persistent.shVanished = True
    #$persistent.goblinsVanished = True
    $persistent.vanished +=1
    $persistent.thiefVanished = True
    $persistent.vanishedLast = "Thief"
    #$purge_saves()
    $ renpy.block_rollback()
    stop music fadeout 6
    play music2 [ "<sync music>audio/rememberDistInstFull.wav", "audio/rememberDistInstFull.wav" ] fadein 1 volume 1.0
    "They gave you a sudden shove in the centre of your chest. You fell sprawling from the roof and slammed into the dirt, tumbling down the side of the hill and away from the train."
    "The train hurtled past you in a blaze of smoke and fire, and then was gone."
    call hideAll from _call_hideAll_141
    show darkforestbg at artPos
    show wolf14 onlayer transient zorder 100
    "You lay in the underbrush, catching your breath, before staggering up."
    "There was no train. There were no train tracks."
    "How did you get here? Who were you looking for?"
    "You shook your head at your foolishness. There's no-one out here."
    "There never was."
    "For some reason, you were holding an empty champagne bottle. You couldn't think why."
    if pig:
        "You heard a soft grunting coming from the bush."
        "The bushes rustled, and then your pig leapt out and into your arms, oinking joyfully. You cradled it softly."
        "You picked yourself up and begin the long walk back home with the pig."
    else:
        "You picked yourself up and begin the long walk back home."
    "The wind whistled in the trees."
    "It was just the wind."
    "There is nothing else to tell."
    "My tale is done."
    "See the mouse run."
    call endStamp from _call_endStamp_41
    "Catch it, whoever can, and then you can make a great big cap out of its fur."
    jump end

#=====================THE MUSHROOM'S STORY

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
        "If you told the tale of how you attempted to catch the Master Thief, turn to page 134.":
            call hideAll from _call_hideAll_27
            show mushroomcavebg at artPos
            if pig:
                "The mushroom ushered you and your pig inside, and you both took a seat in the plush red armchairs. Your pig snuffled around, searching for truffles. You pretended to sip a cup of decaying leaf matter as you told your tale."
            else:
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
                    "If you ask the mushroom to lift the curse, turn to page 140." if mushroomCurse and not mushroomCurseChat:
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
        "At just that moment, you noticed your cup had disappeared from your hand and been replaced with an old gumboot full of pond scum."
        if pig:
            "Your pig squealed a warning."
        else:
            "You looked around and saw a shadow flit across the wall."
        "Grabbing a nearby jewelled scimitar, you leapt up from your seat and swung around to clash swords with the Master Thief!"
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
                if pig:
                    "The pig left bravely at the Master Thief, but they effortlessly dodged and it went rolling down the hill, squealing wildly."
                "The Master Thief effortlessly riposted your blows with one hand, while the other hand darted around grabbing nearby gems and stuffing them into their cloak."
                jump mushroomFinale

label mushroomSolo:
    show rocks onlayer transient zorder 100
    "You walked through the woods."
    call hideAll from _call_hideAll_142
    show stranglerfigbg at artPos
    if persistent.vanished >= 3 and not gilgameshPathFollowed:
        $renpy.show_screen("gilPath", _layer="screens", tag="map", _zorder=101)
        "Soon you came upon an ancient strangler fig. You cut the vines and swamp flowers from it to reveal a small blue door, inlaid with precious moonstone and intricate engravings."
        $renpy.hide_screen("gilPath")
    else:
        "Soon you came upon an ancient strangler fig. You cut the vines and swamp flowers from it to reveal a small blue door, inlaid with precious moonstone and intricate engravings."
    label gilPathShowingMushroom:
        "The words already lurked in your mind."
    pov "Gorge, guzzle, gulp and grab; never shall this wound scab."
    "With this, the door opened before you, and you vanished inside immediately."
    call hideAll from _call_hideAll_143
    show mushroomcavebg at artPos
    "Inside was a boundless cavern, cold as ice despite the heat outside."
    "The floor of the cavern was piled with rubies and pearls and glinting onyx and solid gold pieces, larger than your fist."
    "All across the room you saw lush silks and pillars of precious metals of every type and all manner of riches that would turn the King of Kings green with envy."
    "The glimmering magenta incense smoke rolled across the room and coated it all in a dark haze, smelling of the most incredible spices and herbs and enchanting odours."
    m "Come. It's time."
    "The mushroom startled you. She was holding a picnic basket. Her eyes were red."
    pov "Time for what?"
    m "I think you know, darling. I think you can see where this is going by now."
    m "Carry those things for me please, will you?"
    "You looked down and say bottles of red wine placed by the door. Two wineglasses were next to them. A small, neat pile of napkins."
    "Everything had been prepared long ago."
    "You picked up the supplies. The mushroom linked her arm with yours, and in a blink you were travelling down. Down through the rocks and the pillars of the earth. Down into the last kingdom."
    call hideAll from _call_hideAll_144
    show mushroomgardensbg at artPos
    #TK: Tweak wording.
    "Flickering silver light lit up the scene. All around you pressed a blooming mass of webcaps, milkcaps, scarlet elf caps, poisonpies, decievers, pinkgills, brittlegills, veiled ladies, lawyer's wigs, stinkhorns, earthstars, beefsteaks, chicken of the woods, earthballs, sculpted puffballs, yellowfoots, lungworts, brown-eyed wolves, golden-eyed umbrellas, Satan's boletes, false chanterelles, death caps and destroying angels, and all members of the mysterious Dark Taxa, the dark matter fungi that lie unknown to mankind."
    "They all swept to and fro through a twisted city of endless tunnels. The shape of a giant, pale and broken mountain loomed over the city, barely visible through the thick fog of spores."
    m "Don't worry dear, I've picked out a spot. I've had it picked out for a long time."
    call hideAll from _call_hideAll_145
    show deathbg at artPos
    "She took you through the throng of mushrooms and out onto a lonely hilltop overlooking the kingdom. A picnic rug was already laid on the moss. You could see the plants of the underworld rustling darkly in thick woods at the bottom of the hill, leading to the pale mountain beyond."
    $renpy.music.play("audio/rememberCleanInstFull.wav", channel='music', loop=True, relative_volume=1.0)
    m "Here we are."
    "She set tea-candles sparkling at each corner of the rug, and laid out a rich feast before you."
    "You took out the wineglasses, and she uncorked the wine and poured a toast."
    m "To us."
    "She looked away and discretely wiped her eyes."
    label mushroomSoloConvo:
        if mushroomSoloConvo == 1:
            call hideAll from _call_hideAll_146
            show death2bg at artPos
            "The great pale mountain in the distance shifted in uneasy slumber."
        elif mushroomSoloConvo == 2:
            call hideAll from _call_hideAll_147
            show death3bg at artPos
            "There was a distant sound from the darkness of the kingdom. Almost like howling."
        elif mushroomSoloConvo == 3:
            call hideAll from _call_hideAll_148
            show death4bg at artPos
            "The plants down at the bottom of the hill shook, as if disturbed by the passage of a colossal beast."
        elif mushroomSoloConvo == 4:
            call hideAll from _call_hideAll_149
            show death5bg at artPos
            "Were there always this many stars in the sky? You found you couldn't recall."
        elif mushroomSoloConvo == 5:
            call hideAll from _call_hideAll_150
            show death6bg at artPos
            jump mushroomSoloFinale

        show hand onlayer transient:
            yalign 0.63#0.743
            xalign 0.5
        menu:
            "You looked out into the night."
            "If you asked her what this was all about, turn to page 361." if not mushroomSoloAbout:
                m "I know you must be terribly worried. I'm sorry, dear."
                m "I just wanted to sit, look out at the stars, and enjoy some nice wine and company."
                m "I've thought about this moment so many times. This is how I wanted it to be at the end."
                "She cut off a small sliver of aged truffle cheese and spread it on a water cracker, then looked at it doubtfully."
                m "Oh, to hell with it. No harm in it now."
                "She added an extra slice of cheese, a chilli and garlic olive, a piece of salami and a chunk of marinated artichoke heart onto the cracker, then gently eased the whole concoction into her mouth."
                $mushroomSoloAbout = True
                $mushroomSoloConvo +=1
                jump mushroomSoloConvo
            "If you asked her about her thoughts, turn to page 362." if not mushroomSoloThoughts:
                m "Do you think I did the right thing?"
                pov "Uh - "
                m "You don't know what I'm talking about. I'm sorry, I'm being quite self-indulgent, aren't I?"
                m "Well, you'll have to deal with it. This is my time and I'm going to be as self-indulgent as I damn well please."
                "She lathered some cream on a fresh-baked scone and took a delicate bite."
                m "It all seemed like the right choice at the time. But now it just feels like cowardice."
                m "All those years I've spent in here. So many things I could have done in those years."
                m "No use worrying about it now, of course. No point."
                $mushroomSoloThoughts = True
                $mushroomSoloConvo +=1
                jump mushroomSoloConvo
            "If tried to convince her to run, turn to page 363." if not mushroomSoloRun:
                pov "Let's get out of here. We need to find somewhere safe."
                m "No, no, no. Darling, I appreciate your enthusiasm, but there's no point."
                "She held the scones towards you with a stern glance until you took one."
                m "There never was an ending other than this. There never was a time other than this. No other place but this one."
                #m "The comet is coming. The map is growing dark. The footsteps of the ash giants are closer than they've ever been."
                m "This is the True Ending. At least for me."
                m "I made my decision a long time ago. And soon, I'm sure, you'll need to make yours."
                $mushroomSoloRun = True
                $mushroomSoloConvo +=1
                jump mushroomSoloConvo
            "If you asked her what you should do next, turn to page 364." if not mushroomSoloNext:
                m "Do? Well, the next thing to do is the move on to this lovely lemon delicious I've packed us. And pour me another glass, please."
                pov "I know something's wrong here, but I don't -"
                m "Shh. Shh, dear."
                m "All we can do now is sit back and finish off the rest of this food. That's it."
                m "What happens after that, you'll have to figure out for yourself. Just as we did."
                $mushroomSoloNext = True
                $mushroomSoloConvo +=1
                jump mushroomSoloConvo
            "If you relaxed and enjoyed the view in silence, turn to page 366." if not mushroomSoloSilence:
                "The misty night air settled around the blanket. Flickering fireflies were visible in the distance. A haze of chirping from underground crickets washed over the scene."
                "A deep breath slowly came out of you. You let the weight in your shoulders slip away, piece by piece."
                "The mushroom's pale spores began to lift out of her cap and away down the hill in the breeze."
                m "Thank you for spending this time with me, darling."
                m "You could have gone anywhere, couldn't you? Stayed with anyone."
                m "I would ask you not to forget me. But I know that won't be possible. "
                $mushroomSoloSilence = True
                $mushroomSoloConvo +=1
                jump mushroomSoloConvo

    label mushroomSoloFinale:
        "The mushroom fell back onto the picnic rug and spread out her arms."
        call hideAll from _call_hideAll_151
        show nightbg at artPos
        #stop music fadeout 15.0
        "You lay down to join her and looked up at the sky above. A great, long sigh slowly eased out of her."
        m "Have you ever looked back at your life and tried... tried to calculate the sheer volume of it that you've wasted? The just ungodly amount of time that you've let slip away?"
        call hideAll from _call_hideAll_152
        show night2bg at artPos
        m "Of course I don't mean the time spent having picnics or afternoon naps, or watching the sky. That time isn't wasted."
        m "I mean the time spent doing things you don't want to do, for people you don't care about."
        call hideAll from _call_hideAll_153
        show night3bg at artPos
        m "Those long decades spent paying rent, attending meetings, hunched over desks, travelling to work and back, doing all those petty grinding little tasks every day..."
        call hideAll from _call_hideAll_154
        show night4bg at artPos
        m "It's horrifying. How incalculable a waste."
        "There was the sound of scratching. It seemed to come from somewhere inside you."
        call hideAll from _call_hideAll_155
        show night5bg at artPos
        m "How many minutes and hours and days and years have vanished into that black yawning pit. It's impossible to even fit the number into my mind. It's nightmarish. The stars in the sky. The grains of sand on the beach... I can't even begin to take it in."
        call hideAll from _call_hideAll_156
        show night6bg at artPos
        m "But every time you think about it, every time that number starts to creep into your mind, you think \"There's still time,\" don't you?"
        "The wine in your glasses rippled into complicated, twisting patterns. Like the entrails of beasts, from which omens might be read."
        call hideAll from _call_hideAll_157
        show night7bg at artPos
        m "There's still time to chase that dream, there are still years left to me, I'll make it someday, I can turn this around, it'll all work out in the end! I'll start tomorrow."
        call hideAll from _call_hideAll_158
        show night8bg at artPos
        m "But there are no tomorrows left."
        call hideAll from _call_hideAll_159
        show night9bg at artPos
        "The earth shook beneath you. You almost thought you heard the impact of great footfalls. Almost upon you now."
        m "I can't say that anymore. It's done. The hours I spent are all the hours I'll ever have."
        call hideAll from _call_hideAll_160
        show night10bg at artPos
        #stop music fadeout 6
        m "And... all throughout my life, the moments where I did something I really enjoyed were like small gasps of air between years of drowning."
        "The night was getting darker and darker."
        call hideAll from _call_hideAll_161
        show night11bg at artPos
        m "I had to plan them and save up for them and spend every day just trying to hold out for the next one. Those tiny, tiny moments where I got to be alive."
        call hideAll from _call_hideAll_162
        show night12bg at artPos
        "Something was very close to you now. You didn't dare look. There was a smell like something rotting. A sound like something coiling in the grass."
        m "All I have left now is that number. That percentage of waste."
        play audio wolfApproaches
        #stop ambient2 fadeout 2.0
        #stop ambient1 fadeout 20.0
        call hideAll from _call_hideAll_163
        show darkforestbg at artPos
        call hideAll from _call_hideAll_164
        show night13bg at artPos
        m "It'll never get any smaller. It's done. It's all done."
        "Tears ran down her cheeks. She made no effort to hide them anymore. "
        call hideAll from _call_hideAll_165
        show night14bg at artPos
        m "Hold me, please."
        "You tentatively put your arm around her, and she nestled into your shoulder and wept."
        "You held her tight as you stared out into the night sky."
        stop music fadeout 6
        play music2 [ "<sync music>audio/rememberDistInstFull.wav", "audio/rememberDistInstFull.wav" ] fadein 1 volume 1.0
        $persistent.vanished +=1
        $persistent.mushroomVanished = True
        $persistent.vanishedLast = "Mushroom"
        $persistent.starsVanished = True
        #$purge_saves()
        $ renpy.block_rollback()
        show wolf14 onlayer transient zorder 100
        "It was pitch black. No stars or moon brightened that abyss."
        "You reached for the wine bottle, and realised there was none."
        "There were no wineglasses. There was no food."
        "You felt the touch of moss underneath you. There was no blanket."
        "You looked down."
        "You were holding nothing at all. Your arms were embracing thin air."
        "Why were you here?"
        "You must have needed a rest. A night outdoors. "
        "All of us need some time to ourselves every now and then, don't we?"
        "No harm in that."
        "You stood up. Brushed away the moss. Breathed in the cool night air."
        "You felt warm, full, and sad, for no reason you could name."
        "Finally you began the long walk home in silence, with the dark night sky looming above you."
        "There's nothing else left to tell."
        "That's the end."
        call endStamp from _call_endStamp_42
        "Run away with it now, as fast as you can."
        jump end

                #m "Do I regret it? In some ways."
                #m "But then, would things have been any better if I stayed behind?"
                #When mushroom disappears show this
                # show wolf13 onlayer transient zorder 100
                # call hideAll
                # show nightbg at artPos
                # "Test"
                # call hideAll
                # show night2bg at artPos
                # "test"
                #mushroomGardens
                #
                #"You walked out into the lush expanse of the underground kingdom. Rich moss and lichens flowered from every surface. "

                #"Soon, you emerged into a colossal underground kingdom lit with flickering silver light."
                #show death onlayer transient zorder 100
                #"All around you pressed a blooming mass of webcaps, milkcaps, scarlet elf caps, poisonpies, decievers, pinkgills, brittlegills, veiled ladies, lawyer's wigs, stinkhorns, earthstars, beefsteaks, chicken of the woods, earthballs, sculpted puffballs, yellowfoots, lungworts, brown-eyed wolves, golden-eyed umbrellas, Satan's boletes, false chanterelles, death caps and destroying angels, and all members of the mysterious Dark Taxa, the dark matter fungi that lie unknown to mankind."
                #show scribble3 onlayer transient zorder 100
                #"They all swept to and fro through a twisted city of endless tunnels. The shape of a giant, pale and broken mountain loomed over the city, barely visible through the thick fog of spores."

                #"You saw the four seasons all flowering at once. To the north, the cicadas and crickets chirped loudly in a summer haze. To the south, the ground was silver white with snow. To the west, the autumn rains fell, and to the east was the full glory of spring."
                #"The wonders of those gardens were so stunning that the tongue fails to describe them, and you walked and watched for days, until your eyes were so full that they couldn't stand to see another scrap of beauty."

                #"The mushroom took you closer to the shape you saw from the palace. It loomed over you, larger than life. With a start, you saw that it was breathing."


#The normal finale of the mushroom's story
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
    if pig:
        "Your pig leapt into your arms in fear."
    m "I think we've seen enough. It's time to get off the stage."
    "Before you could blink, they took hold of your ankles and dragged you down into the earth."
    m3 "Shh. Shhh."
    "The Master Thief managed to wriggle out of their grasp."
    t "Au revoir, my friend!"
    "You heard the thunder of a rattling train carriage outside. In a smooth motion, they leapt out of the window, onto the train and out of sight."
    call hideAll from _call_hideAll_28
    show mushroombasementbg at artPos
    "That was the last thing you saw before you were dragged underneath the earth."
    if pig:
        "You and the pig were pulled down through untold layers of dirt by your ankles. You heard the mushrooms whisper around you."
    else:
        "You were pulled down through untold layers of dirt by your ankles. You heard the mushrooms whisper around you."
    m3 "Everything's going to be ok.{vspace=30}                                             {w=0.4}You're safe here.{vspace=30}                                             {w=0.8}Shhhh."
    call hideAll from _call_hideAll_29
    show deathbg at artPos
    "Soon, you emerged into a colossal underground kingdom lit with flickering silver light."
    show stars onlayer transient zorder 100
    "All around you pressed a blooming mass of webcaps, milkcaps, scarlet elf caps, poisonpies, decievers, pinkgills, brittlegills, veiled ladies, lawyer's wigs, stinkhorns, earthstars, beefsteaks, chicken of the woods, earthballs, sculpted puffballs, yellowfoots, lungworts, brown-eyed wolves, golden-eyed umbrellas, Satan's boletes, false chanterelles, death caps and destroying angels, and all members of the mysterious Dark Taxa, the dark matter fungi that lie unknown to mankind."
    #show scribble3 onlayer transient zorder 100
    "They all swept to and fro through a twisted city of endless tunnels. The shape of a giant, pale and broken mountain loomed over the city, barely visible through the thick fog of spores."
    pov "I was about to win! Why have you kidnapped me?"
    m "Darling, trust us, that sad production wasn't going to win anything. You were hurting yourself."
    m2 "Hurting yourself."
    m "Please don't take the criticism too personally. It was an intriguing bit of invisible theatre. We do respect the way you put everything into the role."
    "Dozens of identical mushrooms pressed around you, speaking in soft, overlapping voices."
    m3 "I think it might be best if you stay here until I know that you're safe.{vspace=30}                                             {w=0.4}Until I know you're safe.{vspace=30}                         {w=0.8}It's for the best, if you stay here."
    m4 "I'll watch over you.{vspace=30}                                             {w=0.4}Over you.{vspace=30}                         {w=0.8}Watch over."
    call hideAll from _call_hideAll_30
    show mushroompalacebg at artPos
    if pig:
        "You were taken through a decadant palace of yellow chanterelles and given robes of fine moss. Your room was lushly furnished with soft covers woven from black mushroom silk. Your pig had his own quarters and a bevy of servants to attend to his every whim. All the gems and gold and treasures of the earth were available to you both."
    else:
        "You were taken through a decadant palace of yellow chanterelles and given robes of fine moss. Your room was lushly furnished with soft covers woven from black mushroom silk, and all the gems and gold and treasures of the earth were available to you."
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
                m2 "He did not wish to go, and so they battled across the limitless sea of the world. They fought for forty days and forty nights, but eventually the Heavenly Father got the upper hand."
                m3 "He broke Our Lady across the sky, and cut off Her hands, and threw Her down into the deepest pit underground. She was so weak that She could not pull Herself up."
                m "\"What will become of the world,\" She asked Herself, \"If I just lie here?\""
                m4 "\"There will be no more deaths, and soon there'll be so many people in the world that they won't have the room to stand next to each other.\""
                m3 "And so She extended Her long, broken arms, so that Her fingers poked out of the soil."
                m2 "Those fingers are the Mushrooms."
                m "We provide food for the poor and the animals of the forest, and support the plants and connect them together."
                m4 "But most importantly, we do The Work."
                m2 "We take hold of the dead and the dying, and the old wood and old bones, and carry it all down to Her kingdom, far underground."
                m3 "We work slowly."
                m2 "We are patient."
                m3 "Soon, the work will be complete, and everything will rest here inside Her kingdom, as was intended when the world began."
                "The mushroom gestured to the pale mountain, looming over the city through the fog of spores."
                m4 "Her body still lies there, broken. It is what the hills and forests and continents are built on. It is but rarely that She can walk among men as She once did."
                if godfather == "Black":
                    m "It was a strange occasion indeed on which She walked the earth to become your godmother. I hope it was worth it."
                jump mushroomPrison
            "If you demanded to return to the surface, turn to page 146." if not mushroomImprisoned:
                m "I'm sorry, darling, it's simply impossible."
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
        call hideAll from _call_hideAll_31
        show mushroomgardensbg at artPos
        "You walked out into the lush expanse of the underground kingdom. Rich moss and lichens flowered from every surface. "
        if godfather != "Black":
            m "Don't worry. I know about your Godfather. He cannot reach us here."

        label mushroomExplore:
            call hideAll from _call_hideAll_32
            show mushroomgardensbg at artPos
            show hand onlayer transient:
                yalign 0.63#0.743
                xalign 0.5
            menu:
                "Every type of fungi bustled around you."
                "If you explored the moss garden, turn to page 135." if not mushroomMoss:
                    "The mushroom showed you all the wonders of that undiscovered land, where life and death go hand in hand."
                    if pig:
                        "Your pig frolicked through the gardens beside you."
                    "You saw the four seasons all flowering at once. To the north, the cicadas and crickets chirped loudly in a summer haze. To the south, the ground was silver white with snow. To the west, the autumn rains fell, and to the east was the full glory of spring."
                    "Out in the distance, you noticed a picnic rug lying on the moss of a lonely hillside."
                    "The wonders of those gardens were so stunning that the tongue fails to describe them, and you walked and watched for days, until your eyes were so full that they couldn't stand to see another scrap of beauty."
                    m "A tad garish, isn't it?"
                    $mushroomMoss = True
                    jump mushroomExplore
                "If you feasted in the palace, turn to page 138." if not mushroomFeast:
                    call hideAll from _call_hideAll_33
                    show mushroompalacebg at artPos
                    "As soon as you entered the palace a train of toadstools appeared, all in ceremonial garb. With silent steps, they surrounded you, bearing delicacies of mushroom risotto and crisp goose roasted in truffle butter and dark red wine and platters of mushroom bourguignon with roast potatoes, and set this wondrous feast before you. "
                    if pig:
                        "Your pig feasted with wild abandon."
                    m "You HAVE to try the truffle aioli, darling, that's my absolute favourite."
                    pov "You... eat mushrooms?"
                    m2 "Of course. And one day they will eat me."
                    "Never in your whole life had you sat down to such a marvellous feast, and you gorged yourself for days on end until they had to roll you out of the palace."
                    $mushroomFeast = True
                    jump mushroomExplore
                "If you explored the root embassy, turn to page 139." if not mushroomEmbassy:
                    "The mushroom took you down to show you the deep, ancient roots of the whole forest above you. Delicate fungal networks wove through every root, carrying vital letters and trade agreements and treaties to every plant in the woods."
                    "You spent days among them, learning their intricate customs. You realised that the forest you knew was an intricate web of delicate alliances between opposing factions that hated each other with bitter envy."
                    m3 "Exhausting, isn't it? But it must be done."
                    m2 "If we didn't do this, the whole forest would probably fall into all-out war. And then we'd never get The Work done."
                    $mushroomEmbassy = True
                    jump mushroomExplore
                "If you explored the lands in the shadow of the vast, pale mountain, turn to page 146." if not mushroomPale:
                    call hideAll from _call_hideAll_34
                    show deathbg at artPos
                    "The mushroom took you closer to the shape you saw from the palace. It loomed over you, larger than life. With a start, you saw that it was breathing."
                    m2 "This is the Lady. She waits here, while we do The Work."
                    pov "The Work?"
                    #m "Uh-huh." #We are the fingers of Lady Death. Our job is to push up through the surface and drag everything up there down to Her kingdom."
                    m4 "We take all things down here, one by one. It's slow work. But already, those down here outnumber the ones above. We are more than halfway done."
                    m3 "Someday, everyone and everything will be down here."
                    m "On that day, the Lady will draw her fingers down through the soil and back to her."
                    m3 "We will finally have completed the piece. Our Magnum Opus. It will be spectacular, I assure you, darling."
                    m "Don't look yet, it's not finished. Barely a first draft, really, I'd be so embarrassed if you saw it in its current state."
                    m2 "So much left to do."
                    m3 "No need to worry. We have all the time in the world."
                    "You felt a strange peace in the shadow of the pale lady, and you stayed there with the mushroom for many days, looking out at the splendour of the world."
                    $mushroomPale = True
                    jump mushroomExplore
                "If you asked to return home, turn to page 148.":
                    if persistent.vanished == 0:
                        if godfather == "Red":
                            "Such were the wonders of that kingdom that you almost forgot everything, even the riches you left behind and your twelve siblings and your own country."
                        else:
                            "Such were the wonders of that kingdom that you almost forgot everything, even the home you left behind and your mother and your twelve siblings and your own country."
                    elif persistent.vanished == 1:
                        if godfather == "Red":
                            "Such were the wonders of that kingdom that you almost forgot everything, even the riches you left behind and your ten siblings and your own country."
                        else:
                            "Such were the wonders of that kingdom that you almost forgot everything, even the home you left behind and your mother and your ten siblings and your own country."
                    elif persistent.vanished == 2:
                        if godfather == "Red":
                            "Such were the wonders of that kingdom that you almost forgot everything, even the riches you left behind and your four siblings and your own country."
                        else:
                            "Such were the wonders of that kingdom that you almost forgot everything, even the home you left behind and your mother and your four siblings and your own country."
                    elif persistent.vanished >= 3:
                        if godfather == "Red":
                            "Such were the wonders of that kingdom that you almost forgot everything, even the riches you left behind and your own country."
                        else:
                            "Such were the wonders of that kingdom that you almost forgot everything, even the home you left behind and your mother and your own country."
                    "But soon, your mind came back to you, and you realised that you did not belong to this wonderful land. And so you said to the mushroom:"
                    pov "I've been very happy with you, and you've been kinder to me than words can tell. But I must go back."
                    show hand onlayer transient:
                        yalign 0.66#0.743
                        xalign 0.5
                    menu:
                        m "Oh darling, no! Do you have to go? Why not stay here with me?"
                        "If you changed your mind and decided to stay here underground, turn to page 127.":
                            "For a long time, you thought over the Mushroom's proposal. Finally, you agreed."
                            show hand onlayer transient:
                                yalign 0.72#0.743
                                xalign 0.5
                            menu:
                                "You and the mushroom stayed together for many long and happy years, roaming the ancient underground gardens of that fungal kingdom."
                                "If you remained good friends with the mushrooms, turn to page 155.":
                                    if godfather == "Red":
                                        "You and the mushrooms built a close together friendship over many years, laying each moment shared together like the bricks of a house. You came to know their deep fears and most secret shames."
                                        if pig:
                                            "Your pig settled down to a contented life among the truffles."
                                        "You set up a quaint home in that strange country, and soon you were even able to find your poor mother and make amends for your wicked behaviour."
                                        "After a long time, your siblings came down to join you there, one by one."
                                        "Even I was there, though you did not see me."
                                    else:
                                        "You and the mushrooms built a close together friendship over many years, laying each moment shared together like the bricks of a house. You came to know their deep fears and most secret shames."
                                        if pig:
                                            "Your pig settled down to a contented life among the truffles."
                                        "You set up a quaint home in that dark kingdom."
                                        "After a long time, your mother and siblings came down to join you there, one by one."
                                        "Even I was there, though you did not see me."
                                "If you married the mushrooms, turn to page 156.":
                                    "After slowly growing close over many years, you and the mushrooms all became married together in a beautiful ceremony."
                                    "Your mother came down to the kingdom of death for the occasion, and all the plants and lichens and moss and toadstools of the forest were in attendance."
                                    "The occasion was full of joy. I laughed as I raised a toast, and the beer ran down my chin but did not go into my mouth."
                            if godfather == "White":
                                "Long did your Godfather the Almighty search for you, but never could he find you, hidden as you were in that undiscovered country."
                            elif godfather == "Red":
                                "Long did your Godfather the Devil search for you, but never could he find you, hidden as you were in that undiscovered country."
                            elif godfather == "Black":
                                "And so the promise came to pass, and you took your place with the woman clad all in black, just as she promised your mother all those years ago."
                            call endStamp from _call_endStamp_2
                            "You stayed there at the side of the Pale Lady, forever and ever, until the final horn and the coming of the end of days."
                            #Wolf: Kills Thief
                            "..."
                            "Oh?"
                            #show wolf14 onlayer transient zorder 100
                            "And what happened to the thief, you ask?"
                            jump thiefDisappears

                        "If you held fast to your desire to return to the world above, turn to page 164.":
                            if godfather == "Red":
                                pov "Don't think that I want to leave you. It's just that I must see my old country again."
                            else:
                                pov "Don't think that I want to leave you. It's just that I must see my old mother and my old country."
                            m3 "I see. Well, then I'm sure we can't stand in your way. Take this to remember us by, please."
                            "She handed you a black box tied with a tassel of red silk."
                            m4 "This is the box of the jewelled hand, and it holds something very precious. Do not open it, no matter what happens."
                            if pig:
                                "You bid her a tearful farewell. Then, you turned to your pig."
                                p1 "I am sorry, my erstwhile companion. After all our adventures together, I have come to see you as a dear friend - even as family."
                                p1 "But where you go now, I cannot follow. My place is here, with the truffles. I hope you can understand."
                                "It hurt you dearly to part ways, but you understood. You and the pig embraced warmly."
                                p1 "I will always remember you, [povname]."
                            "And so you promised that you would never open the box, and the mushrooms took hold of you and bore you back up to the surface."
    call hideAll from _call_hideAll_35
    show darknessbg at artPos
    "You blinked in the harsh light of the sun above, and found that your eyes had become almost blind in the darkness below. Your skin was pale and shrunken."
    "As you looked around, a strange anxiety gripped you. The ancient old strangler fig you remembered was gone. You couldn't see the blue door to the mushroom's domain."
    call hideAll from _call_hideAll_36
    show futurebg at artPos
    "As you walked down the road to your house, something seemed wrong. The people you saw walking past had different faces to the people you knew so well before. Even your old house was a different shape."
    "You walked up to your old home and called out:"
    pov "Mum! I'm back!"
    "But just as you were about to enter, a strange man came out."
    som "Who are you?"
    pov "What? Who are you? And why do you twist in that crooked way?"
    som "We're all crooked now, child. It's the law. But answer my question!"
    #You raced through crowds of bent and crooked people.
    pov "My name is [povname]."
    som "Don't joke around like that."
    show spirit2 onlayer transient zorder 100
    som "It's true that someone by the name of [povname] once lived here, but that is a tale three hundred years old! [He] couldn't possibly be alive now."
    "When you heard those odd words, a terrible fear gripped you, and you ran out onto the street and through the twisting alleyways. The forest you knew was gone. A grey rain of ash fell ceaselessly across the land from the grey clouds above down onto the bent and crooked grey people of the realm, who huddled in grim shelters underneath places that hideously resembled the hills and lakes and villages you once knew."
    "Over and over, you heard them mutter of the Ash Giants, and you heard terrible footfalls shake the earth from some distant place, growing closer every moment."
    "The awful feeling came over you that what the old man said was true. Each day you spent in the underground kingdom was as a hundred years on earth."
    show tornPage1 onlayer screens zorder 101
    show tornPage1bg onlayer screens zorder 99
    "You ran through the grey streets and parking lots and abandoned shopping centres and the vast, decayed, echoing airports and twisting subterranean toll roads and subway tunnels, last remnants of a loose and raving hunger that had scooped out the whole of this hollow earth and left it its wake only the slow landfill rivers that boiled around you with the serpentine motion of the secluded trash queens as you stumbled through them into the suffocating silence of cracked bitumen roads and empty apartment complexes (packed with flickering TV screens of silent static that never ceased) under the grim endless maze of freeways that blotted out the grey sky above."
    hide tornPage1 onlayer screens
    hide tornPage1bg onlayer screens
    "But try as you might you couldn't find the way back to the kingdom you left."
    if godfather == "White":
        miw "Finally."
        "You felt a heavy hand fall on your shoulder. A burning light seared behind you, too bright for you to turn and face it."
        miw "Long have I waited. Now, you will come with me."
        jump mushroomBox
    elif godfather == "Red":
        mir "Finally."
        "A crooked red hand fell on your shoulder, and you turned to see the cackling face of the old serpent himself."
        mir "Now you see that no matter how long you hide, none can escape the devil's clutches! Come with me, and we will dance together in Hell forever."
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
                    call hideAll from _call_hideAll_37
                    show mementobg at artPos
                    "Poor thing! I wept to see your woeful fate. Because of your disobedience, never would you live to see your loved ones again."
                    call endStamp from _call_endStamp_3
                    "Little children, never be disobedient to those who are wiser than you, for disobedience is the mother of all misery and father of all woe."
                    #Wolf: Kills Thief
                    "..."
                    "Oh?"
                    #show wolf14 onlayer transient zorder 100
                    "And what happened to the thief, you ask?"
                    jump thiefDisappears

                "If you refused to open the box, even when all hope was lost, turn to page 179.":
                    if godfather == "White":
                        "You hesitated - but in the end you couldn't bring yourself to break your promise to the mushroom."
                        call endStamp from _call_endStamp_4
                        "And so the Lord took you, and you rested in the basement of His White House forever and ever, until the final horn and the coming of the end of days."
                        #Wolf: Kills Thief
                        "..."
                        "Oh?"
                        #show wolf14 onlayer transient zorder 100
                        "And what happened to the thief, you ask?"
                        jump thiefDisappears
                    elif godfather == "Red":
                        "You hesitated - but in the end you couldn't bring yourself to break your promise to the mushroom."
                        call endStamp from _call_endStamp_5
                        "And so the Devil took you, and you were trapped as his servant in Hell forever and ever, until the final horn and the coming of the end of days."
                        #Wolf: Kills Thief
                        "..."
                        "Oh?"
                        #show wolf14 onlayer transient zorder 100
                        "And what happened to the thief, you ask?"
                        jump thiefDisappears
                    else:
                        "And so you stayed there, forever searching for an entrance back to that kingdom you missed so much."
                        "For years you searched, with no success. Soon, the Ash Giants came upon the world, and you felt their searing light upon your skin."
                        "As the light burnt you away, you felt something take hold of you and draw you into the earth."
                        m "It's ok."
                        m2 "It's just me."
                        m3 "Just us."
                        m3 "You've returned."
                        if pig:
                            "Your pig jumped out from the arms of the mushroom and danced around you in glee."
                        call hideAll from _call_hideAll_38
                        show mementobg at artPos
                        call endStamp from _call_endStamp_6
                        if godfather == "Black":
                            "And so your godmother finally came for you, as promised. The mushrooms took you down into the earth. There you stayed at the side of Lady Death, forever and ever, until the work was complete, and the glory of it shone out forevermore."
                        else:
                            "The mushrooms took you down into the earth. There you stayed at the side of Lady Death, forever and ever, until the work was complete, and the glory of it shone out forevermore."
                        #Wolf: Kills Thief
                        "..."
                        "Oh?"
                        "And what happened to the thief, you ask?"
                        jump thiefDisappears

#=====The Thief Disappears
label thiefDisappears:

    # play music hunted1

    # stop music fadeout 6
    # play music2 [ "<sync music>audio/hunted2.wav", "audio/hunted2.wav" ] fadein 1

    # stop music2 fadeout 6
    # play music3 [ "<sync music2>audio/hunted3.wav", "audio/hunted3.wav" ] fadein 1

    # stop music3 fadeout 6
    # play music4 [ "<sync music3>audio/hunted4.wav", "audio/hunted4.wav" ] fadein 1

    # stop music4 fadeout 6
    # play music5 [ "<sync music4>audio/hunted5.wav", "audio/hunted5.wav" ] fadein 1

    # stop music5 fadeout 6
    # play music6 [ "<sync music5>audio/hunted6.wav", "audio/hunted6.wav" ] volume 2.0 fadein 1

    call hideAll from _call_hideAll_238
    show forestbg at artPos
    "After you were taken they strolled away from the tree, laughing and clutching their ill-gotten gains. "
    t "Another successful heist."
    h "Hold it right there!"
    "The hunter, the sparrow-herder and the goose-girl leapt from the bushes and surrounded the thief, holding pitchforks and rakes and an old shovel."
    go "Looks like your day is done, scoundrel!"
    sh "Yeah! We got you bang to rights, we have."
    "The three of them jeered and prodded the thief with glee."
    t "Ha ha ha! Well, if you think you're going to take me to jail, I'm afraid..."
    play music hunted1
    "The thief trailed off."
    "There was a sound in the woods."
    show wolf14 onlayer transient zorder 100
    "A low, hushed and ragged sound, like a howl in the wind."
    t "Did you hear that?"
    t "Was that... the wolf?"
    h "Don't try to distract us, you wretched cur. There are no wolves in Australia."
    sh "Yeah! We won't be turned away that easily!"
    stop music fadeout 6
    play music2 [ "<sync music>audio/hunted2.wav", "audio/hunted2.wav" ] fadein 1
    "The two of them jabbed at the thief."
    #call musicSilence from _call_musicSilence_33
    "It was always just the two of them. The Hunter and the Sparrow-herder, cornering the thief."
    "No-one else was there."
    h "Come on, let's grab them."
    "The thief looked down."
    "There was a dark red stain on the ground. In the dirt where a third person would have stood."
    "But of course, no such person had ever been there."
    t "Something's wrong. I think we need to run."
    stop music2 fadeout 6
    play music3 [ "<sync music2>audio/hunted3.wav", "audio/hunted3.wav" ] fadein 1
    show wolf12 onlayer transient zorder 100
    "The trees rustled, as if with the movement of something colossal."
    sh "Ha! You'd like that, wouldn't you? Just when I've got you cornered."
    sh "No, you're coming with me, chum."
    "The sparrow-herder grabbed the thief."
    "The two of them were alone in the clearing."
    "There was no-one else."
    #"There never was."
    t "Come on!"
    sh "Hold on, I -"
    call hideAll from _call_hideAll_239
    show town3bg at artPos
    "The thief dragged the sparrow-herder through the woods and burst out of the woods to a field with a small cottage, surrounded by geese."
    sh "What are you doing?"
    "It was echoing and empty."
    "No-one lived there but geese. No-one ever had."
    t "Help! Someone help us!"
    stop music3 fadeout 6
    play music6 [ "<sync music3>audio/hunted6.wav", "audio/hunted6.wav" ] volume 2.0 fadein 1

    "Who are you calling out to, Thief?"
    "You're alone. You always have been."
    call wolfApproaches from _call_wolfApproaches
    t "No, they're right here, they -"
    show wolf8 onlayer transient zorder 100
    call hideAll from _call_hideAll_240
    show darknessbg at artPos
    "They looked around. There was no-one there."
    "The trees were silent."
    "No animals lived in this part of the woods. No bird calls troubled its vast, silent depths. The woods were dead."
    "The thief ran through the forest, ragged and alone."
    "They searched their memories. Had there ever been a time before this one? Another place?"
    "Had there ever been anyone else in the world but them?"
    "They could remember nothing except this. A single frozen moment of running through the woods in fear, alone."
    "There was nothing else."
    "There had never been anything else."
    "Hot breath warmed the back of their neck."
    "They ran as fast as they could. But it was no use, of course. There was no-where to run to."
    t "Please... I-"
    $persistent.hVanished = True
    $persistent.goVanished = True
    $persistent.shVanished = True
    $persistent.thiefVanished = True
    $persistent.vanishedLast = "Thief"
    $persistent.vanished +=1
    #$purge_saves()
    $ renpy.block_rollback()
    show wolf9 onlayer transient zorder 100
    "And then there was nothing."
    "The woods were empty."
    "There was never anything there at all."
    "Just a ragged midnight cloak, stained red, that floated away in the breeze and was gone forever."
    call endStamp from _call_endStamp_7
    "It was never seen again."
    jump end

#=====================THE TOAD'S STORY

# Act 2, Chapter 2B: Journey with the Toad
label toad1:
    "He gulped down the rest of his plate and stumbled unsteadily away from the table."
    if pig:
        "You, the toad and the pig stepped into the squash carriage, and it went rattling away down the path into the rainforest."
    else:
        "You both stepped into the squash carriage, and it went rattling away down the path into the rainforest."
    call hideAll from _call_hideAll_65
    show nightbg at artPos
    "As you went down the road, the forest began to get darker and darker."
    if persistent.starsVanished:
        "The trees closed in like a wall around you. The night sky was black, and shed no light."
    else:
        "The trees closed in like a wall around you, and the moon and stars fled in fear."
    f "Nothing to fear, my friend! My boys will get us through this dark road, quick smart!"
    "He waved the crow-shrike, the rat, the bat and the old black cockatoo onwards. But instead of going faster, they slowed down and came to a stop."
    f "What? Why are you stopping?"
    crowshrike "Well... now seems as good a time as any."
    rat "We've been meaning to have a bit of a chat with you, mate."
    bat "About the payment situation."
    show spiral4 onlayer transient zorder 100
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
    if pig:
        "They jumped in the old rotten squash and rode it away back to the village, leaving you, the toad and the pig on the side of the road."
    else:
        "They jumped in the old rotten squash and rode it away back to the village, leaving you both on the side of the road."
    f "...Uh..."
    f "A-another successful adventure! Good thing I was able to fight off those ruffians!"
    "He coughed up some mud from the ditch, shuddering weakly."
    "Then he stood up and said to himself sternly:"
    f "I am Bridlebrogue Chippingham, and I've never failed at anything in my life."
    "With this, he regained his former swagger and strode forward."
    "The night grew dark."
    "You walked through the trees together."
    call hideAll from _call_hideAll_66
    show nightgodbg at artPos
    "The Firmament looked down at you from Her place up above."
    call hideAll from _call_hideAll_67
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
    if pig:
        "The pig pushed the toad with its snout."
    f "I just... need a moment. M-might have... sprained my ankle there, I think. And maybe my arm."
    "He wheezed and lay there in the mud for a long time, breathing heavily and trying not to cry."
    "You heard him whisper to himself weakly."
    f "I am B-brildebrogue Chippingham. And I..."
    show hand onlayer transient:
        yalign 0.7#0.743
        xalign 0.5
    menu:
        #TK: Have more options here for the different godfathers
        "He trailed off."
        "If you helped the toad up, turn to page 235.":
            "You reached down and found the toad's hand."
            "Even in the darkness, you saw him blush bright red."
            f "Well I - t-this is all most..."
            f "Hand-holding, before marriage? What will people say?"
            "You picked him up out of the muck and put him on your shoulder."
            f "Good, good. I-I'll lead you onward."
        "If you turned and walked into the woods without another word, turn to page 237." if persistent.vanished>=1:
            f "W-what are you doing? Wait!"
            "His voice faded behind you as you walked away into the darkness."
            $clearing = "toad"
            jump clearingInvestigate

    "You walked on. Soon, you began to see a glimmer of silver light in the darkness."
    call hideAll from _call_hideAll_68
    show darkforestbg at artPos
    "The forest was covered in puddles of water from the rains. Each one shone with light."
    "All around you, the woods were dark and empty. But when you looked into the water, you saw the reflection of a shining cottage below."
    play sound pageFlip
    call hideAll from _call_hideAll_166
    show lakefullbg
    ""
    play sound pageFlip2
    call hideAll from _call_hideAll_167
    show darkforestbg at artPos

    "For a brief moment, you thought you saw a figure reflected in the water. But as soon as you blinked, it was gone."
    jump puddle

#Act 2, Chapter 3: The mysterious puddle
#Entering the puddle and the witch's house
label puddle:
    show hand onlayer transient:
        yalign 0.68#0.743
        xalign 0.5
    menu:
        "The toad gasped in terror at the sight."
        "If you looked into the puddle carefully, turn to page 236." if not puddleLook:
            "You crawled to the edge and looked down into the puddle."
            "The surface of the water was flat and still."
            call hideAll from _call_hideAll_69
            show cottagebg at artPos
            "The cottage in the reflection shone with bright light, as if the setting sun was behind it."
            call hideAll from _call_hideAll_70
            show darkforestbg at artPos
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
            if pig:
                "You grabbed the pig and the toad to you, then leapt into the puddle."
            else:
                "You held the toad tight, then leapt into the puddle."
            call hideAll from _call_hideAll_71
            show mushroombasementbg at artPos
            "The world flipped over."
            "You felt the water pass over you, and a cool chill tingled all through your body."
            call hideAll from _call_hideAll_72
            show silverbg at artPos
            "When you opened your eyes, you were standing right way up again."
            "The puddle you had jumped into was now a floor, like a silver mirror."
            "The world all around you shone white."
            "At the centre of the puddle was the cottage, shining with light."
    "The toad was very quiet now. His fine suit was ruined with mud. He jumped out of your hand and sat down."
    show scribble6 onlayer transient zorder 100
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
            f "Oh. I..."
            "He brightened up."
            f "Yes, I had to make sure you were included! We're both on this adventure together, after all. We're a team."
            "You saw him start to smile shakily."
            f "I did do a decent job getting us here, didn't I?"
            pov "Of course!"
            "You gently slapped him across the back."
            pov "You're Brildebrogue Chippingham, and you've never failed at anything in your life."
            "With this, the toad wiped the tears from his eyes, and beamed."
            $toadSad = False
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
    call hideAll from _call_hideAll_73
    show cottagebg at artPos
    "You crossed the river paths to the cottage in the centre."
    "Up over the walls grew a riot of herbs and flowers of every type, rambling over everything and growing in a lush green-grass garden on the roof. "
    if pig:
        "The pig munched on some violets blooming from the windowsill."
    "You saw the glimmer of two red eyes watching you from a small crook in the roof. Then there was a gasp from inside, and they disappeared."
    if toadSad == False:
        "The closer you got to the cottage, the more the toad shook with terror."
        pov "You'd better stay behind. Guard the rear."
        f "G-good idea."
        f "But be wary, my friend. Few have ever left that cottage alive."
        f "Witches have red eyes. They see very far, but they have a keen sense of smell, like animals, and can sense when humans are near them."
        f "If you aren't out in ten minutes, I'll come in there to rescue you."
    jump witch2

# Act 3 Finale: The Toad.
label toadFinale:
    "You leapt to defend the toad, diving and pushing him away from the slashes of the crooked dagger."
    if pig:
        "The pig joined the melee and tried to defend you. As it did, a black vial of liquid smashed over the three of you and you were all instantly turned into witchetty grubs."
    else:
        "As you pulled him away, a black vial of liquid smashed over the two of you and you were both instantly turned into witchetty grubs."
    if pig:
        "The cottage wall gave way and you were washed out of the house in a multicoloured wave of potions."
    else:
        "The cottage wall gave way and you were both washed out of the house in a multicoloured wave of potions."
    call hideAll from _call_hideAll_85
    show riverbg at artPos
    "The world flipped upside down as you fell through the silver puddle outside, and you found yourself caught up in a torrent of writhing fish and magpies and bats and crocodiles being washed down the rainforest river, all transforming into new animals every second."
    if pig:
        "You popped into a cat, then a fish, then back into a witchetty grub again. The toad turned into a water-rat and whirled around. The pig turned into a platypus and strained against the current to reach you."
    else:
        "You popped into a cat, then a fish, then back into a witchetty grub again. The toad turned into a water-rat and whirled around."
    fr "Watch out!"
    "A greedy magpie dove for you as you squirmed helplessly."
    "The toad transformed into a gecko and grabbed you, dropping his tail."
    show scribble8 onlayer transient zorder 100
    "The magpie grabbed the tail and flew off, before turning into a wallaby and falling back in the river."
    fg "Hold on! I know where to go!"
    "You felt yourself transform into a squirming tadpole. The toad changed into a sea bass and held you in his mouth, swimming for a point on the shore."
    if pig:
        "Just as his fins began to give out, the pig turned into a cat and grabbed the two of you, pulling you both up out of the water."
    else:
        "Just as his fins began to give out, you turned into a cat and grabbed him and pulled you both up out of the water."
    call hideAll from _call_hideAll_86
    show mushroomcaveunderbg at artPos
    "The toad directed you to a small, muddy hole on the river bank. As soon as you entered, the mud fell down behind you and blocked your exit."
    "The hole was wet, and cramped, and crawling with small worms and roaches, but it was safe."
    if pig:
        "You shivered in the cold. The toad flopped down beside you, becoming a wet quoll. The pig grunted sadly in the form of a fruit bat."
    else:
        "You shivered in the cold. The toad flopped down beside you, becoming a wet quoll."
    #You explore the toad's home and get to know him better
    label toadExplore1:
        show hand onlayer transient:
            yalign 0.65#0.743
            xalign 0.5
        menu:
            fq "Well. This is another fine mess I've made."
            "If you explored the nearby area, turn to page 208." if not toadCave:
                $toadCave = True
                "You uncovered a rug and a fireplace in the muck, and lit the fire."
                if pig:
                    "The toad uncovered a pantry with a single, mouldy piece of bread and toasted it over the fire for the three of you."
                else:
                    "The toad uncovered a pantry with a single, mouldy piece of bread and toasted it over the fire for the both of you."
                fq "This all the food I have, sorry."
                jump toadExplore1
            "If you explored deeper in, turn to page 209." if not toadBasement:
                $toadBasement = True
                "You travelled down a hole in the back of the cave which lead down into the mud."
                "Down the hole was a small room with a bed and a cupboard."
                "The toad opened the cupboard and took out two threadbare costumes: a witch and a unicorn. You pulled them around you for warmth."
                if pig:
                    "The pig grunted in appreciation."
                fq "I... used to like to dress up in this stuff. I'd put on little plays and things for myself."
                fq "Pretty dumb, I know. Kid's stuff. Haven't done it in years."
                "But the costumes seemed well cared for."
                jump toadExplore1
            "If you asked the toad about this place, turn to page 216." if not toadWhere:
                $toadWhere = True
                pov "Where are we?"
                fq "This is my home. My real home."
                fq "That's right. The grand fortune? The prestigious inheritance? The manor on the hill? All lies."
                fq "I've lived in this hole near the witch's cottage since I was a tadpole."
                fq "Yes, I know it might be hard to believe with my noble bearing. But it's all true."
                jump toadExplore1
            "If you asked about the toad's curse, turn to page 217." if not toadCurse:
                $toadCurse = True
                pov "I'm sorry. Now we'll never be able to cure your curse."
                fq "Oh... don't worry about that."
                fq "There was never a curse."
                fq "I just didn't want to be me anymore."
                jump toadExplore1

            "If you looked for a way out, turn to page 218.":
                pov "How are we going to get out of here?"
                fq "Don\'t worry. I'm sure {b}{i}he{/i}{/b} will rescue us soon."
                pov "{i}He?{/i}"
                "Suddenly the ceiling burst open and a shining light came upon you, blinding in its glory."
                "Out from the light strode the most beautiful frog you'd ever seen."
                if pig:
                    "The pig rolled over in shock and transformed into a turtle."
                "His skin was glimmering green like the wings of summer beetles, his muscles rippled with strength, his eyes threw out glances of fire, and he was dressed in a gorgeous midnight-blue suit."
                "On each finger gleamed a golden ring inlaid with precious jadestone and chrysoprase and emeralds, and his finely-coiffed hair waved in the breeze with such beauty that none had ever seen the like, not even in a dream."
                mysFrog "Are you quite alright?"
                pov "Who are you?"
                "The toad sighed."
                fq "This..."
                fq "...is Brildebrogue Chippingham."
                bc "The very same!"
                show toadAngry onlayer transient zorder 100
                "The frog beamed and helped you to your feet as you transformed into a garden rake."
                bc "Say, that voice is awfully familiar..."
                bc "Is that you, Blort?"
                fq "Yes. Yes, that's my real name."
                fq "I am Blort Bronkum, and I have never succeeded at anything in my life."
    call hideAll from _call_hideAll_87
    show manorextbg at artPos
    "The real Brildebrogue Chippingham pulled you out of the hole and into a golden carriage waiting nearby, which whisked you away to a stately riverside manor."
    "With a click of his fingers, Brildebrogue summoned a cavalcade of richly dressed frog manservants, who offered you all the finest delicacies from across the world, such that the King of Kings would cry to taste them."
    "With another click, a dozen beautiful frog maids escorted you to golden baths where all the muck and grime was washed away, and you were restored to your true forms as the finest frog soprano choir in all the land serenaded you."
    "Brildebrogue himself regaled you with witty anecdotes of his thrilling adventures, which had everyone rolling around on the floor laughing, except for the toad, who sat in the corner and scowled."
    bc "Please make yourselves at home, my friends!"
    bc "I'm afraid I must leave immediately. Business with the jewelled serpent-kings of the City of Brass, you understand."
    f "Of course. Actually, I recall I was chatting with the jewelled serpent-kings myself just the other day, and -{w=1.0}{nw}"
    bc "Help yourselves to all the delights of Chippingham Manor! Here are the keys to the whole place. You may go wherever you wish, and open every door!"
    show scribble3 onlayer transient zorder 100
    bc "...except one."
    bc "This little golden key will unlock the smallest closet in the tallest tower. Do not open that closet."
    bc "But I'm sure that won't be a problem! I know I can trust you, my dear friends. I'll see you on my return!"
    "And with a wave of his hand, he leapt into a gleaming gold carriage and sped away across the horizon in an instant."
    f "Hmph. Show-off."
    if pig:
        "The pig relaxed into his bath and grunted with contentment."
    label chippinghamManor:
        show hand onlayer transient:
            yalign 0.57#0.743
            xalign 0.5
        menu:
            blank ""
            "If you explored the first tower, turn to page 256." if not firstTower:
                if pig:
                    "Inside the first tower, the three of you discovered a trio of stately frog wizards, who flushed the last remains of the potions from your systems and restored you to good health."
                else:
                    "Inside the first tower, the two of you discovered a trio of stately frog wizards, who flushed the last remains of the potions from your systems and restored you to good health."
                $firstTower = True
                jump chippinghamManor
            "If you explored the second tower, turn to page 257." if not secondTower:
                if pig:
                    "Inside the second tower, you discovered the finest frog chefs of all the land, who quickly sliced off their own legs and served them to you as the most delicious dish the three of you had ever tasted."
                else:
                    "Inside the second tower, you discovered the finest frog chefs of all the land, who quickly sliced off their own legs and served them to you as the most delicious dish either of you had ever tasted."
                $secondTower = True
                jump chippinghamManor
            "If you explored the third tower, turn to page 258." if not thirdTower:
                if pig:
                    "Inside the third tower, you discovered a stately harem of frog courtesans, who poured rich wines and made witty conversation with you until you were all completely sloshed and dizzy from the refined repartee."
                else:
                    "Inside the third tower, you discovered a stately harem of frog courtesans, who poured rich wines and made witty conversation with you until you were both completely sloshed and dizzy from the refined repartee."
                $thirdTower = True
                jump chippinghamManor
            "If you explored the fourth tower, turn to page 259." if not fourthTower:
                $fourthTower = True
                "Inside the fourth tower was a sparkling fountain of emeralds and sapphires and precious gems, which splashed out over a scale model replica of the forest. You could see immediately that a single gemstone from this fountain was so valuable that it would bankrupt the richest sultan."
                f "I spent my whole life looking up at this place. Hard to believe we're actually here."
                jump chippinghamManor
            "If you explored the fifth tower, turn to page 260." if not fifthTower:
                $fifthTower = True
                "Inside the fifth tower you found a gigantic closet of the finest clothes, rich silks and suits and uniforms of office, all extremely masculine in cut and befitting of a king."
                jump chippinghamManor
            "If you explored the sixth tower, turn to page 262." if not sixthTower:
                $sixthTower = True
                "Inside the sixth tower you found the Library of Alexandria. A small plaque explained that Brildebrogue had miraculously saved the books from the fires, and they'd been stored here safely for all this time."
                jump chippinghamManor
            "If you explored the seventh tower, turn to page 264." if firstTower:
                "Inside the seventh and tallest tower you found only a tiny wooden closet."
                show hand onlayer transient:
                    yalign 0.68#0.743
                    xalign 0.5
                menu:
                    "A golden keyhole shone out from the closet door."
                    "If you opened the closet, turn to page 275.":
                        "You inserted the key, and slowly opened the door with a long creak."
                        call hideAll from _call_hideAll_88
                        show mushroombasementbg at artPos
                        "As soon as the door opened, a stream of blood flowed over you, and you saw seven dead frog brides hanging all along the walls, some only skeletons."
                        if pig:
                            "The pig squealed in terrible fear."
                        jump brildebrogueCloset
                    "If you went back, turn to page 190.":
                        jump chippinghamManor
            "If you patiently waited for Brildebrogue, turn to page 161.":
                f "Well, if you're not going to open this damn closet, I am."
                "He rushed to the seventh and tallest tower, and unlocked the closet with the golden key."
                "He slowly turned the key, and opened the closet door with a long creak."
                call hideAll from _call_hideAll_89
                show mushroombasementbg at artPos
                "As soon as the door opened, a stream of blood flowed over the two of you, and you saw seven dead frog brides hanging all along the closet walls, some only skeletons."
                jump brildebrogueCloset


    label brildebrogueCloset:
        f "Oh my G-"
        show hand onlayer transient:
            yalign 0.83#0.743
            xalign 0.5
        "You slipped in the blood and felt it on your hair and tasted it in your mouth. The blood washed over your face and you felt the blood on your hands and the blood underneath your feet and the blood on the walls and the blood in your fingernails. The toad quickly slammed the door, but the key popped out and into the blood.{vspace=80}{i}In your notes, write down that you {b}have blood on your hands.{/b}{/i}"
        f "No no no no no. Oh god."
        "The clock chimed a quarter to twelve."
        "You tried to wipe the blood off the key, but it wouldn't come off."
        f "Quickly! We have to wash this off."
        call hideAll from _call_hideAll_90
        show manorextbg at artPos
        if pig:
            "You both rushed downstairs and tore off your clothes and burned them and put on new, spotless clothes without a hint of blood. You scrubbed the pig clean so that there was no sign that anything was amiss. But no matter how long you scrubbed at the key, you couldn't get it off. When you rubbed the blood off one side, it appeared on the other."
        else:
            "You both rushed downstairs and tore off your clothes and burned them and put on new, spotless clothes without a hint of blood. But no matter how long you scrubbed at the key, you couldn't get it off. When you rubbed the blood off one side, it appeared on the other."
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
                bc "If you have such an interest in my closet, you can take your place among the ladies there."
                "He took out his scimitar and locked the door to his manor behind him."
                f "RUN!"
                jump brildebrogueFinale
            "If you pretended you lost the bloody key, turn to page 125.":
                f "L-looks like we must have misplaced it, sorry... o-old sport..."
                bc "..."
                bc "Interesting."
                bc "Where is it?"
                f "I-I am sure I do not know."
                bc "You do not know?"
                bc "But I know well enough."
                "In one motion he twisted the toad's arm behind his back. The toad gasped and dropped the bloody key on the floor."
                bc "If you have such an interest in my closet, you can take your place among the ladies there."
                "He took out his scimitar and locked the door to his manor behind him."
                f "RUN!"
                jump brildebrogueFinale
    label brildebrogueFinale:
        #Number of escape attempts before you escape
        define escapesAllowed = 4
        if escapeB == 0:
            "You ran into the twisting castle corridors together, but Brildebrogue Chippingham was fast behind you, smiling a charming smile."
        if escapeB == 1:
            if pig:
                "You raced up and down endless staircases with the pig leading the way, hearing Brildebrogue's pleasant, resonant voice behind you."
            else:
                "You both raced up and down endless staircases, hearing Brildebrogue's pleasant, resonant voice behind you."
            bc "Just stand aside, Blort. I've no interest in you."
            bc "Honour among toads, and all that."
        if escapeB == 2:
            "Warm, resonant laughter echoed behind you as you stumbled across the manor's battlements."
        if escapeB == 3:
            if pig:
                "You and the pig pulled the exhausted toad up ladders and down wells. Brildebrogue wasn't even tired. He strolled after you at a leisurely pace."
            else:
                "You pulled the exhausted toad up ladders and down wells. Brildebrogue wasn't even tired. He strolled after you at a leisurely pace."
        if escapeB == 4:
            "As you ran up the manor staircases, you saw an old clock on the wall. It was almost midnight. The moon loomed large above you."
        if escapeB == 5:
            if pig:
                "The pig panted in exhaustion. You smelt Brildebrogue's intoxicating cologne all around you as you dragged the toad over the crooked manor roof. His sweet breath was hot on your neck."
            else:
                "You smelt Brildebrogue's intoxicating cologne all around you as you dragged the toad over the crooked manor roof. His sweet breath was hot on your neck."
        if escapeB == 6:
            "You were at your limit. You struggled on, putting one stumbling foot after another. You felt Brildebrogue's elegant, manicured hand reaching over your shoulder."
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
                show toadSad onlayer transient zorder 100
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
                "With a flick of his wrist, Bildebrogue turned the courtesans into a pack of wild squawking galahs which tore down the tower like an oversized pinecone. You fled as it crumbled around you."
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
                if pig:
                    "The pig stood behind you and tried to fend Brildebrogue off, but with a single sweep, he cut off its right hoof and sent it tumbling away."
                    "You pulled the injured pig into your arms and fled through the racks of fine clothes in the fifth tower as Brildebrogue sliced them apart behind you."
                else:
                    "You fled through the racks of fine clothes in the fifth tower as Brildebrogue sliced them apart behind you."
                bc "Trying to steal from my wardrobe?"
                bc "I heard the servants laughing about your little dress-up obsession, Blort. I just never realised it went this far!"
                "With one clap of his hands he brought down water rushing in from the seas. You fled through the waves as they brought the tower down around you."
                jump brildebrogueFinale
            "If you ran to the sixth tower, turn to page 290." if not sixthTower2:
                $sixthTower2 = True
                $escapeB +=1
                #if sixthTower == True:
                if pig:
                    "The three of you scrabbled through the aisles of books in the sixth tower - but as you turned a corner, Brildebrogue was in front of you, carelessly thumbing through a thick volume."
                else:
                    "You and the toad scrabbled through the aisles of books in the sixth tower - but as you turned a corner, Brildebrogue was in front of you, carelessly thumbing through a thick volume."
                bc "\"On Rays of Light.\" Democritus. One of my favourites."
                bc "But then, you never learned to read or write, did you? All those sad little stories you tell, and you never learned."
                f "I..."
                f "I mean, of course I can..."
                bc "Give [him] over, and I'll teach you."
                bc "Don't worry, it's easy. Even a child could do it."
                "The toad said nothing."
                "Brildebrogue tossed the book down. With a click of his fingers he brought down lightning from the skies, and the whole tower went up in flames. You both fled through the fire as it burned around you."
                jump brildebrogueFinale
            "If you ran to the seventh and tallest tower, turn to page 292." if escapeB >= escapesAllowed:
                "You burst through the door to the tallest tower. In front of you was the small room with the bloody closet, now yawning open wide."
                "There was nowhere left to run. You heard slow footsteps behind you."
                bc "You've heard all my offers, Blort. You know I could give you the life you always wanted."
                if pig:
                    "The pig panted weakly, bleeding from its severed leg. The toad stood between the two of you and Brildebrogue with sword cane drawn, hands shaking."
                else:
                    "The toad stood between you and Brildebrogue with sword cane drawn, hands shaking."
                bc "You've seen what I've built. I built it with these two hands."
                bc "You have a choice. You can hand [him] over, and become a great man."
                bc "Or you can stay a wretch and die, and leave nothing but a stain in the gutter that will be washed away with the morning rain."
                f "..."
                f "Then I will die a wretch."
                f "But I will die with my friend beside me."
                show swordfight onlayer transient zorder 100
                "The toad brought up his sword cane to clash with the scimitar. And at just that moment, you heard the clock strike twelve."
                if godfather == "Red" or godfather == "White":
                    pov "Godfather! Help me!"
                    jump frogEnding
                else:
                    pov "Godmother! Help me!"
                    jump frogEnding

    label frogEnding:
        if godfather == "White":
            #G-d rescues you, brildebrogue is smote
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
            "The Lord performed this feat and turned into a mighty wind. But just as He did so, the toad opened the window, and the Lord blew right out of the tower and across the sea. With this, the toad slammed the window shut."
            f "Well. That takes care of that."

        if godfather == "Red":
            #The devil drags brildebrogue down to hell
            mir "Your time is up!"
            "The Devil Himself exploded out of the floor in a flash of brimstone and soot."
            if pig:
                "The pig hid behind you, shivering."
            "As soon as he saw your Godfather, Brildebrogue went white as ash."
            bc "Lucifer. My contract isn't up yet. You told me I still had six years!"
            mir "That may be so."
            mir "But I never keep a bargain, and no-one messes with my grandchild and lives!"
            bc "N-now see here. I am Brildebrogue Chippingham, and I have never failed at anything in my-"
            "But with one cloven hoof the devil kicked him straight out the window, whereupon he fell screaming down the tower and into his grave and straight to Hell."
            mir "That takes care of that. Now come with me, my grandchild. All the wonders of Hell await!"
            f "Hold on just a second. How do we know you're really the Devil?"
            mir "Ha! You dare doubt my power? I can grow tall as a fir tree and small as a mouse."
            f "Prove it."
            "The Devil performed His feat, but just as He turned into a mouse, the toad grabbed Him and stuffed Him in a sack and threw Him out the window, whereupon He fell screaming down the tower and into His grave and straight to Hell."
            f "Well. That takes care of that."
        if godfather == "Black":
            #Death comes for brildebrogue after all these years
            "As the clock struck midnight, the ground around Brildebrogue Chippingham began to sprout with pale mushrooms (the fingers of Lady Death)."
            bc "No... please! It's not yet my time!"
            bc "N-now see here. I am Brildebrogue Chippingham, and I have never failed at anything in my-"
            "But in an instant the mushrooms grew all around and through him, and he fell to the floor."
            "And so he died, and he has remained dead up to this very day."
            f "Well. That takes care of that."
        call hideAll from _call_hideAll_91
        show mushroomcaveunderbg at artPos
        if pig:
            "You and the toad bandaged up the pig's injured leg. Then you all left the ruins of Chippingham manor behind to rot."
        else:
            "You and the toad left the ruins of Chippingham manor behind to rot."
        show toadHappy onlayer transient zorder 100
        "You took the gems from the wreckage and renovated the toad's old mud-hole, turning it into a warm, comfy little cottage with a crackling fire and enough food for a lifetime, along with a large closet of fine clothes."
        if pig:
            "Eventually the pig recovered from his injuries and bid you a tearful farewell. With his share of the treasure, he bought a prosthetic hoof made of iron and started a gambling-house in the village. You all visited from time to time to enjoy a game of chance with him."
            "Thus, the legend of Iron Hoof was born."
        show hand onlayer transient:
            yalign 0.66#0.743
            xalign 0.5
        menu:
            "After a while, you had rested and mended from your terrible ordeals."
            "If you married the toad, turn to page 298.":
                #ToadEnd
                "But you found you didn't want to leave. You stayed together in your cosy home in the swamp. The toad worked long hours sewing many fine costumes, and the two of you put on plays together which delighted the people of the village."
                "After many years of companionship, you finally got married and lived happily together."
                "I should know - I was at your wedding!"
                call endStamp from _call_endStamp_34
                "I gorged myself on the fresh meat and raised my glass for the toast, and the beer ran down my chin but did not go into my mouth."
                if godfather == "Black":
                    jump toadDeath
                else:
                    #"You were very happy, had many children, and you still would live if you had not died."
                    #Wolf: Kills Witch
                    "..."
                    "Oh?"
                    "And what happened to the witch, you ask?"
                    jump witchDisappears
            "If you stayed good friends with the toad, turn to page 299.":
                #ToadEnd
                #Wolf: Kills Witch
                "But you found you didn't want to leave. You stayed together in your cosy home in the swamp."
                "The two of you settled down to a happy life together. The toad found work sewing fine costumes for the people of the village, and soon enough you founded a theatre with the savings."
                "I saw the two of you put on many fine plays through the years! Together you had the whole village in stitches. I laughed and laughed and laughed, though none could hear me."
                if godfather == "Black":
                    jump toadDeath
                else:
                    call endStamp from _call_endStamp_18
                    "You were happy there for the rest of your days, and you still would live if you had not died."
                    #Wolf: Kills Witch
                    "..."
                    "Oh?"
                    "And what happened to the witch, you ask?"
                    jump witchDisappears
            "If you left the toad to return to your family, turn to page 300.":
                #ToadEnd
                #Wolf: Kills Witch
                call hideAll from _call_hideAll_92
                show sunbg at artPos
                "When it was time to leave, you wished the toad a tearful farewell, and returned to your cottage with your family."
                "You lived there for many long, happy years, visiting the toad often as a good friend."
                "The toad found work sewing fine costumes for the people of the village, and soon enough you founded a theatre with the savings."
                "I saw the two of you put on many fine plays through the years! Together you had the whole village in stitches. I laughed and laughed and laughed, though none could hear me."
                if godfather == "Black":
                    jump toadDeath
                else:
                    call endStamp from _call_endStamp_19
                    "You were very happy there for the rest of your days, and you still would live if you had not died."
                #Wolf: Kills Witch
                "..."
                "Oh?"
                "And what happened to the witch, you ask?"
                jump witchDisappears

    label toadDeath:
        #ToadEnd
        "But youth does not last forever."
        "One day, you felt yourself wracked with a terrible fever."
        "Then, you felt gout take hold of you and make all your limbs twitch, and you were wracked with one illness after another, and you fell into deep sleep for long days."
        "Not even the toad could help you, though he toiled at your bedside for many long hours."
        f "I-I'm so sorry, my old friend... I wish I knew more about this kind of thing."
        pov "Don't worry. I won't die until Death sends Her messengers."
        "But as you spoke, there was a knock on the door, and the toad opened it to reveal the wise mushroom from the forest."
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
                    show toadSad onlayer transient zorder 100
                    "You turned to the toad. He was crying, and where his tears fell they turned into gleaming black geckos that skittered away into the corners of the room."
                    show hand onlayer transient:
                        yalign 0.7#0.743
                        xalign 0.5
                    menu:
                        "If you told him you loved him, turn to page 276.":
                            pov "Goodbye, my dear. I love you, so much."
                            f "I love you too."
                            "You embraced, and his tears fell upon you, and you felt the cool gecko's feet across your cheeks."
                            "I wept in the shadows."
                            f "I'm sorry I couldn't be more. You should have chosen someone else. Maybe if you'd-"
                            pov "Shh. I chose you. You have nothing to be sorry about."
                            "And you gripped him tight."
                            jump deathToadQuestions
                        "If you simply told him goodbye, turn to page 278.":
                            pov "Goodbye, my dear friend. I love you, so much."
                            f "Goodbye."
                            "You embraced, and his tears fell upon you, and you felt the cool gecko's feet across your cheeks."
                            "I wept to see such a tragic moment."
                            f "I'm sorry I couldn't be more for you. You should have chosen someone else. Maybe if you'd-"
                            pov "Shh. I chose you. You have nothing to be sorry about."
                            "And you gripped him tight."
                            jump deathToadQuestions
                "If you accepted your fate, turn to page 265.":
                    pov "Alright. I'm ready."
                    m "No-one's ever ready. But there's no time left."
                    call hideAll from _call_hideAll_93
                    show mementobg at artPos
                    "She gently took you down to the kingdom of Death."
                    call endStamp from _call_endStamp_20
                    "And you lie there still."
                    #Wolf: Kills Witch
                    "..."
                    "Oh?"
                    "And what happened to the witch, you ask?"
                    jump witchDisappears

label witchDisappears:
    call hideAll from _call_hideAll_241
    show cottageintbg at artPos
    $ renpy.block_rollback()


    #[Teachoice]
    "The witch was left alone in her cottage. The wet, swollen greenery pressed in around her, twisting in spirals like the organs of some giant beast."
    w "Well. I guess I'd better clean up this mess."
    play music hunted1
    "There was a sound outside."
    "From the space between the trees."
    "Perhaps it was just the howling of the wind, and nothing more."
    w "I'll make some tea. That always calms me down."
    stop music fadeout 6
    play music2 [ "<sync music>audio/hunted2.wav", "audio/hunted2.wav" ] fadein 1

    "But when she went to her tea cabinet, she found she'd forgotten how."
    #call musicSilence from _call_musicSilence_34
    w "What? I'm sure I.."
    "She thought, and thought, but no knowledge of how to brew tea was left in her mind. There was nothing but a hole where the information had been. Like a great, red bite taken out of her brain."
    w "Oh no. No, no, no."
    "Something was outside."
    stop music2 fadeout 6
    play music3 [ "<sync music2>audio/hunted3.wav", "audio/hunted3.wav" ] fadein 1
    "She ran to lock the door. But she didn't know how anymore."
    "How did locks work? How did one interact with a door? The latch, the key, the handle - what were these things, and how did they fit together?"
    "The knowledge was gone."
    "She clawed at it, but it was just a wooden rectangle now, an abstract shape with no meaning. Another gaping wound in her mind, still fresh and dripping."
    w "I - No."
    w "I see the cabinet. I smell the tea. I hear the rustle of the leaves. I taste - I taste -" #[teachoice]
    "She tried to recite one thing she could see. One thing she could smell. One thing she could hear."
    "But it was too late."
    stop music3 fadeout 6
    play music4 [ "<sync music3>audio/hunted4.wav", "audio/hunted4.wav" ] fadein 1

    "The wolf was already inside the house."
    "She fell to the floor. She had forgotten how to walk. Perhaps she never knew."
    "What were these things, at the end of her legs? What strange process animated these lumps of unknown flesh?"
    w "I see the window. I can feel the floor. I can hear... I hear..."
    stop music4 fadeout 6
    play music6 [ "<sync music4>audio/hunted6.wav", "audio/hunted6.wav" ] volume 2.0 fadein 1

    "She heard nothing."
    call wolfApproaches from _call_wolfApproaches_12
    "Her ears did not hear. Her eyes did not see. Her fingers no longer felt the wood under her nails."
    "The information from her senses meant nothing at all to her anymore. She could no longer tell whether she was hot or cold, wet or dry, whether the thing underneath her hands was wood, or flesh, or even just air - the knowledge of what these things felt like had been taken - but then maybe she was suspended in nothingness after all, maybe there was nothing here but the empty abyss of endless nothing-space in every single direction, maybe she heard nothing because there was nothing in the entire world except for herself."
    w "You can't do this. I am myself."
    w "I name you, and bind you, beast. By your True Name, I cast you out."
    "But how can you do that, witch?"
    "You don't even remember your own name."
    w "No! My name is... my name is..."
    "It was gone. Eaten up whole."
    "The thing that had no name lay there on the floor, senseless."
    "It saw nothing."
    "It smelled nothing."
    "It felt nothing."
    "It tasted nothing."
    "It heard nothing."
    $persistent.vanished +=1
    $persistent.witchVanished = True
    $persistent.vanishedLast = "Witch"
    #$purge_saves()
    $ renpy.block_rollback()

    show wolf12 onlayer transient zorder 100
    "And then it was gone."
    call endStamp from _call_endStamp_35
    "It was never seen or heard from again."
    jump end

#==========Solo path
#The Toad's path if the Witch has disappeared
label toadSolo:
    call hideAll from _call_hideAll_242
    #TD: Test
    show townfeastbg at artPos
    "The toad leapt up from the table and clicked his fingers."
    if persistent.vanished >= 3 and not gilgameshPathFollowed:
        $renpy.show_screen("gilPath", _layer="screens", tag="map", _zorder=101)
        f "Prickle! Crawl! Shudder and Clink! Don't tarry or stall, get us there in a wink!"
        $renpy.hide_screen("gilPath")
    else:
        f "Prickle! Crawl! Shudder and Clink! Don't tarry or stall, get us there in a wink!"
    label gilPathShowingToad:
        "His great squash carriage rattled out of the bushes and pulled up right next to the banquet table."
    f "If you get us there before sundown, there's a tenner in it for you!"
    "He tossed a bag of shiny coins to the crow-shrike, the rat, the bat and the old black cockatoo."
    bat "Cheers, boss."
    "The cockatoo bit into one of the coins."
    cockatoo "Yep, it's good money. Let's do it, boys."
    rat "We'll get you there in a jiffy, mate."
    crowshrike "Caw!"
    "The squash rattled and bumped down the road with haste. The toad attempted some witty anecdotes while you pretended to listen."
    call hideAll from _call_hideAll_168
    show manorextbg at artPos
    "Finally you arrived at a stately riverside manor."
    "With a clap of his hands, the toad summoned a cavalcade of richly dressed frog manservants, who poured flutes of champagne while offering spontaneous and completely unplanned anecdotes about the incredible things Brildebrogue Chippingham had said or done lately."
    "With another click, a dozen beautiful frog maids escorted you to golden baths where all the dirt of the journey was washed away. The finest frog soprano choir in all the land serenaded you with tales of Brildebrogue Chippingham's latest exploits."
    "All the while, the toad's servants pretended to laugh at his jokes as he tipped them generously."
    f "Yes, please make yourself at home, my dear friend! We are friends now, right?"
    f "That is to say, of course we are! I have so many friends these days, you know. In fact I may be completely tied up with them and all the time we spend together constantly, doing all the things friends do, you know, but never fear, I won't forget the little people such as yourself, my dear friend, we shall certainly have some time to spend together."
    pov "Have you... always owned this manor?"
    show monster2 onlayer transient zorder 100
    f "Of course! The manor is owned by me, Brildebrogue Chippingham! That's my name! Why would you think otherwise?"
    f "Anyway, no time to talk about trivialities such as property ownership, I have a party to plan! It will begin soon, you'd better make ready!"
    "And with that the toad flitted out of the room and left you alone to explore the manor."
    play music hunted1
    jump chippinghamManorSolo


    # Great statues of him were erected in the courtyard.
    #paintings of the frog
    #Bards compose poems about the frog
    #A pyramid
    # A vault
    # wizards
    #seven mansion rooms with investigation things
    label chippinghamManorSolo:
        show hand onlayer transient:
            yalign 0.62#0.743
            xalign 0.5
        menu:
            "Something scratched against the walls outside." 
            "If you explored the first tower, turn to page 256." if not firstTower:
                "Deep underneath the first tower was a bottomless vault full of riches."
                "Inside the vault was a cornucopia of luscious fruit, fat flies, even gardens and lakes that produced enough food to last for years - perhaps centuries."
                "A team of frog engineers were reinforcing the walls to make them totally impenetrable."
                $firstTower = True
                $construction +=1
                jump toadConstruct
            "If you explored the second tower, turn to page 257." if not secondTower:
                "Inside the second tower was a trio of stately frog wizards, hard at work placing sigils and wards and runes all across the manor to guard against every possible evil."
                $secondTower = True
                $construction +=1
                jump toadConstruct
            "If you explored the third tower, turn to page 258." if not thirdTower:
                "Inside the third tower, you discovered a collection of fine frog bards, composing poems and arias in Brildebrogue's name that moved you to tears just to hear them."
                $thirdTower = True
                $construction +=1
                jump toadConstruct
            "If you explored the fourth tower, turn to page 259." if not fourthTower:
                $fourthTower = True
                "The whole fourth tower was taken up by a looming pyramid. Atop it stood a gigantic sculpture of Brildebrogue, vomiting forth emeralds and sapphires and precious gems."
                $construction +=1
                jump toadConstruct
            "If you explored the fifth tower, turn to page 260." if not fifthTower:
                $fifthTower = True
                "Inside the fifth tower were the greatest frog artists of their age, furiously painting a series of refined portraits of Brildebrogue at rest."
                $construction +=1
                jump toadConstruct
            "If you explored the sixth tower, turn to page 262." if not sixthTower:
                $sixthTower = True
                "Inside the sixth tower you found the Library of Alexandria. You opened a random volume to discover that it was a biography of Brildebrogue's life (part 6 of 2,987)."
                $construction +=1
                jump toadConstruct
            "If you explored the seventh tower, turn to page 264." if construction >= 2:
                "Inside the seventh and tallest tower you found only a tiny wooden closet."
                show hand onlayer transient:
                    yalign 0.68#0.743
                    xalign 0.5
                menu:
                    "A golden keyhole shone out from the closet door."
                    "The sounds of the party echoed below you."
                    "If you opened the closet, turn to page 275.":
                        "You inserted the key, and slowly opened the door with a long creak."
                        call hideAll from _call_hideAll_169
                        show mushroombasementbg at artPos
                        "As soon as the door opened, a stream of blood flowed over you."
                        if pig:
                            "The pig squealed in terrible fear."
                        "In the depths of the darkness, you saw a hollow face."
                        stop music fadeout 6
                        stop music2 fadeout 6
                        stop music3 fadeout 6
                        stop music4 fadeout 6
                        stop music5 fadeout 6
                        play music6 [ "<sync music5>audio/hunted6.wav", "audio/hunted6.wav" ] volume 4.0 fadein 1
                        $renpy.music.set_volume(0.5, channel=u'music6')
                        "The eyes were gone. The mouth had rotted away. It was all that remained of Brildebrogue Chippingham."

                        jump toadSoloFinale
                    "If you went back, turn to page 190.":
                        jump chippinghamManorSolo

    #The seventh
    #Layers:
    #Gold, Silver, Copper, Iron, Mercury, Salt, Ash, Bone. // Ash, Salt, Rowan, Iron, Bone. , Iron, Mercury. Tin, lead,

label toadConstruct:
    if construction == 1:
        "The toad was busy reinforcing the manor's defences."
        "Golden locks were placed on every door, and silver bars at every window."
        jump chippinghamManorSolo
    elif construction == 2:
        "Hordes of guests began arriving for the gala. Notable political figures, great artists or famed adventurers from the swamplands."
        "The toad greeted them hastily before leading a team of master masons through the house, heading for the basement."
        "The masons carried lumbering wagons of copper and iron."
        jump chippinghamManorSolo
    elif construction == 3:
        stop music fadeout 6
        play music2 [ "<sync music>audio/hunted2.wav", "audio/hunted2.wav" ] fadein 1

        f "Did you hear that?"
        "Sweat streamed down the toad's face."
        pov "Hear what?"
        show wolf13 onlayer transient zorder 100
        f "It sounded like howling."
        f "Build faster."
        "The labourers increased their speed. A layer of mercury was bound into the walls of the manor."
        "The party intensified. Scenes of froggish debauchery played out all around you."
        jump chippinghamManorSolo
    elif construction == 4:
        stop music2 fadeout 6
        play music3 [ "<sync music2>audio/hunted3.wav", "audio/hunted3.wav" ] fadein 1
        "Layers of ash and salt were drawn around the mansion."
        "The doors were barred. Guests weren't allowed to enter or leave."
        "They didn't seem to care. Fine swamp cocktails were handed out and a big band played on into the night."
        show wolf14 onlayer transient zorder 100
        "Underneath the music, you almost thought you could hear something moving underneath the floorboards."
        jump chippinghamManorSolo
    elif construction == 5:
        stop music3 fadeout 6
        play music4 [ "<sync music3>audio/hunted4.wav", "audio/hunted4.wav" ] fadein 1

        "The final layer of protection was delivered. The layer of Bone."
        "You saw it drawn into the castle under cover of night."
        "The band leader leapt into a triumphant saxophone solo."
        jump chippinghamManorSolo
    elif construction >= 6:
        stop music4 fadeout 6
        play music5 [ "<sync music4>audio/hunted5.wav", "audio/hunted5.wav" ] fadein 1
        #jump toadSoloFinale
        #Wolves in the walls
        "The vault was complete."
        "It yawned underneath the manor like an open mouth."
        "The walls were thick. Impenetrable in every way. Every possible ward had been laid upon them."
        "They formed a twisting spiral, like a knot of entrails from which omens could be read."
        jump chippinghamManorSolo
    #Gold, ash salt, bone
    #Brildebrogue has been killed and the toad has assumed his identity (somehow? disguise?).
    #Maybe you are there for the assassination and help him with it??
    #The toad goes more and more extravagant and insecure and nuts
    #Throws lavish parties


    #==Investigation
    #The toad parties and buys lavish things, growing more and more out of control
    #He becomes paranoid and terrified of the wolf coming for him
    #Wolves in the walls etc
    #He gets more and more crazy security measures

    #
    label toadSoloFinale:
        #Meanwhile you investigate the manor to find out what happened to the real BC

        f "I see you've found it."
        "You jumped in shock. The toad was right behind you."
        f "Very well. You deserve to know what happened."
        f "In a time already long past, I came to this mansion as a lowly servant. My name in those days was Blort."
        f "The manor was owned by a frog named Brildebrogue Chippingham, who was so handsome that light shone from his face as if from the sun. The wind whistled for him, and the cobblestones sighed in joy to receive his feet upon them. Everyone in the land adored him."
        f "Sweeping his floors, and dusting his closets, I searched through the manor each night."
        $renpy.music.set_volume(1.0, delay=6.0, channel=u'music6')
        f "Finally, I found his secret."
        f "I stole his key, and left it in the hall, so that he would find it and think something was wrong."
        f "He came across it late at night."
        bc "What's this?"
        f "In a panic, he ran to the cupboard on the seventh floor of the seventh tower."
        f "He wrested open the door in a feverish state."
        bc "My darlings. My darlings. Are you still in here?"
        wives "Come closer."
        wives "Come closer, our love. We can barely see your face."
        f "Brildebrogue took one step inside. That's when I drew my dagger and ran him through."
        bc "The devil - Blort? You bastard -"
        f "With my last strength I pushed him into the closet."
        f "His seven wives were waiting."
        wives "Come to us."
        bc "No, no-"
        wives "Stay. Stay."
        stop music6 fadeout 12
        f "Their skeletal arms closed around him and dragged him into the blood-soaked blackness."
        f "I slammed the door. I took up his clothes and his mantle."
        f "None can tell the difference. Or perhaps they don't care to, as long as I keep the money flowing."
        "The sounds of laughter and music echoed from behind the door."
        pov "You're living a lie."
        f "No."
        f "He was the imposter. History will remember me as the real thing."
        "The toad walked over and swung the closet door shut."
        "A frog sage appeared to inform you both that the vault was ready."
        f "Good. Come with me."
        call hideAll from _call_hideAll_170
        show mushroomcavebg at artPos
        "You both walked down through the manor, past the riotous party, down to the vault in the basement."
        $renpy.music.play("audio/rememberCleanInstFull.wav", channel='music', loop=True, relative_volume=1.0)
        pov "Is this really what you want?"
        f "Of course. This is the life I always desired. This is why I took the deal, all those years ago."
        "The toad walked into the cyclopean, hungry mouth of the vault."
        show tornPage1 onlayer screens zorder 101
        show tornPage1bg onlayer screens zorder 99
        f "I'll certainly miss you, my friend, Don't get me wrong. But I'm sure you can understand my decision. Deep within this vault, you see, I will be safe and secure to live out the rest of my days in luxury. These seven impenetrable layers will hold off all harm. Got the idea from a book, y'know, read it somewhere - I have so much time for reading, now, you see, educating myself on the finer things in life, why, if I could only tell you of the tomes I've read now! I believe even the wizened scholars of Algrembria would fall to their knees, seeing themselves as mere infants, babes, ignoramuses in the light of my enlightened wisdom! Such is the nature of the knowledge I now possess."
        hide tornPage1 onlayer screens
        hide tornPage1bg onlayer screens
        pov "Why don't you give up the charade? Come with me. You can live in the village. As your true self."
        f "No. I've come too far now."
        f "I am Brildebrogue Chippingham, and I will never die."
        f "The sages will speak of me. The bards will sing poems."
        f "The statues outside will stand forever. Historians will speak of me a thousand years hence."
        f "There will not be a soul on this earth who does not know my name."
        f "There is nothing to fear. I am already immortal."
        #call musicSilence from _call_musicSilence_25
        call wolfApproaches from _call_wolfApproaches_1

        "You embraced. The cavernous emptiness of his vault loomed before him."
        "He gave you a final wave. Then, he was swallowed up into the darkness."
        "The lock sealed. The magic shook the earth, and a golden sigil appeared upon it."
        "The barriers were set. The guards of silver, gold, lead, rowan, ash, oak, and the final layer of bone. Seven auras, which lay upon the manor like seven cloaks."
        show wolf6 onlayer transient zorder 100
        #call wolfApproaches
        call hideAll from _call_hideAll_171
        $persistent.vanished +=1
        $persistent.toadVanished = True
        $persistent.vanishedLast = "Toad"
        #$purge_saves()
        $ renpy.block_rollback()
        stop music fadeout 6
        play music2 [ "<sync music>audio/rememberDistInstFull.wav", "audio/rememberDistInstFull.wav" ] fadein 1 volume 1.0

        show manorextbg at artPos
        "A slow silence seeped up into the house."
        "As you wiped the tears away, you wondered what you were crying about."
        "Where did these tears come from? You strained your memory, but you could not recall."
        "You found yourself in a large, empty manor, for no reason you could remember."
        "There was no-one around. There never had been."
        "Ah, well. No need to worry."
        "You dried your eyes, and began the walk back to the village."
        "There is nothing else to tell."
        "Have you tired of this story yet?"
        "No?"
        "Well, I’ve had enough for this round. If you want any more you can make it up yourself."
        call endStamp from _call_endStamp_43
        "The rat’s tail is off. That’s the end."
        jump end

    # call hideAll
    # show darkforestbg at artPos

#=====================THE WITCH'S STORY

# Act 2, Chapter 3: The Witch's Cottage
#Entering the witch's cottage for the first time after being brought there by the toad
label witch2:
    "You walked up the front steps, and put your hand on the doorknob."
    "The door opened up with a shuddering creak."
    if pig:
        "You and the pig slowly crept forward."
    call hideAll from _call_hideAll_74
    show cottageintbg at artPos
    "Inside the cottage was a wild clutter of books and herbs and plants of all description, growing up the walls and roof."
    "The cottage was tiny, but the walls were covered with bookshelves stuffed with old manuscripts and notebooks and thick textbooks on all kinds of plants and animals."
    #TK: Herbs and plants
    "The wooden bookshelves were sprouting with herbs and plants of every type."
    "In the corner was a small kitchen with a cauldron, and up above was a small attic crawl-space."
    "Out of the attic poked a small head with a giant black hat. It looked at you with shock."
    w "Oh!"
    "It quickly withdrew into the rafters and you heard a crash."
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
    show spiral3 onlayer transient zorder 100
    w "Because, uh... why do I..."
    w "Oh, the caffeine, that's right. The caffeine makes me too wired and I can't get to sleep at night, so I have to stick to all the herbal stuff."
    w "But you don't have to take the black tea if you don't want to, I have all kinds, it's fine. Or you don't have to have any kind of tea at all, that's totally fine too, I don't want to be out here stuffing tea down your mouth."
    w "I-It's just been so long since I had company for tea, so I haven't had a chance to get it out."
    w "Not that I like company at all, obviously."
    w "I spurn it!"
    w "I need no-one, and I want no-one."
    if pig:
        "She patted the pig absently. It accepted the gesture with dignity."
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
                "The witch leapt up and started rifling through a towering triangular cupboard with dozens of tiny compartments hanging open."
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
                    #"If you asked for Earl Grey, turn to page 235.":
                    #    w "Nice! Coming right up."
                    #"If you asked for Dandy chai, turn to page 235.":
                        #w "Nice! Coming right up."
                    #"If you asked for Coconut chai, turn to page 235.":
                    #    w "Nice! Coming right up."
                    "If you asked for Green tea, turn to page 235.":
                        w "Nice! Coming right up."
                    #"If you asked for Masala tea, turn to page 235.":
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
                w "I'm so sorry, this is so embarrassing, I'm... I'm afraid I don't quite remember."
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
                    w "To be honest I do know a bit about your red friend, I have had some uh, {i}dealings{/i} with Him, I guess you could say. It wasn't my choice though, I don't want you to think I'm one of those wild women of the woods who dance around naked and worship the Devil and all that kind of thing, know what I mean? I admire them but I tried it once or twice and it gets really chilly, not recommended."
                    w "But yeah, nah, maybe I could help you out. Let me take a look through my books, I'll see what I can come up with."
                    "And she began rifling through the stack of books lying randomly around the floor."
                if godfather == "Black":
                    pov "I'm hoping you can help me with a problem. My godmother is Death, and She has sworn to take me away."
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
                "She darted under the table and came out with a sticky note saying {b}{i}\"FESTIVAL!!!!!!\"{/i}{/b} underlined three times."
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
    show wolf9 onlayer transient zorder 100
    "The witch grabbed a crooked dagger, still gleaming with wolfsbane from her potion work earlier, and parried his thrust."
    w "Do I know you?!"
    "They began to fight back and forth, crashing around the tiny cottage, and as they did the bookshelves rocked and the chairs went clattering away and the potions began to fall from the walls, exploding open in bursts of magical smoke and light."
    "Green and blue and black and ultraviolet liquid and smoke burst out all around you."
    w "My house!"
    "The chairs were enveloped by smoke and turned into a pair of chickens, then mulberry bushes, then a pile of prunes that went clattering across the kitchen."

    "The table warped, went soggy, and splashed across the floor as a cold, swirling purple liquid."
    show flower1 onlayer transient zorder 100
    "The kitchen and the walls started to twist and turn and sprout with life, and all the books and furniture turned into bats and cats and chittering cicadas that ran and scratched and flew all through the house."
    show flower2 onlayer transient zorder 100
    "The fire in the kitchen flared up wildly and began to spew flowers in all directions."
    if pig:
        "The pig tried to stop the melee but was tossed aside by a rogue bromeliad."
    show flower3 onlayer transient zorder 100
    show hand onlayer transient:
        yalign 0.72#0.743
        xalign 0.5
    menu:
        "Brilliant orchids and bottlebrushes and corpse flowers burst out all around the witch and the toad as they fought their way back and forth through the haze."
        "If you helped the witch, turn to page 281.":
            jump witchFinale
        "If you helped the toad, turn to page 203.":
            jump toadFinale

# Act 3 Finale: The Witch.
label witchFinale:
    "You dived at the witch and pushed her out of the way of the stabbing sword cane."
    if pig:
        "You, her and the pig went tumbling across the floor and into the fire. When you fell into the fireplace, you fell straight through the flames and down to Hell."

    else:
        "You both went tumbling across the floor and into the fire. When you fell into the fireplace, you fell straight through the flames and down to Hell."
    call hideAll from _call_hideAll_75
    show hellbg at artPos
    show devil onlayer transient zorder 100
    "Hell was dark and sooty, and the Devil was not home."
    if pig:
        "The pig was looked around in stark terror."
        p1 "Listen to me, comrade. I can't be here. I can't go back to Hell again."
        p1 "I have... enemies."
        w "The pig is right. We have to get out. I've spent too many years here already."
        pov "Years? What do you mean?"
        "The witch sighed as you all picked yourself up from the floor, battered and bruised."
        jump hellStory
    else:
        w "Not again!"
        pov "...What do you mean, not again?"
        "The witch sighed as you both picked yourself up from the floor, battered and bruised."
        jump hellStory

#You and the witch fall into hell. The witch gives you her tragic backstory.
label hellStory:
    show hand onlayer transient:
        yalign 0.71#0.743
        xalign 0.5
    menu:
        w "The truth is, I have served the Devil all this time, and wrought his wicked works upon the world - though it pleased me none to do so."
        "If you asked the witch to tell her tale, turn to page 215." if not witchStory:
            $witchStory = True
            if pig:
                "You all sat down on a lump of brimstone together, and she began to tell you her tale."
            else:
                "You all sat down on a lump of brimstone together, and she began to tell you her tale."
            w "Once, I was the princess of a vast kingdom very far from here, where we ruled over sapphire seas and emerald skies."
            w "From a young age I had a terrible hunger for knowledge, and soon I had devoured every book in the kingdom."
            w "Librarians everywhere grew to fear me, and they called me The Girl Who Knew Everything."
            w "Soon the Great Adversary learned of my wisdom and pride, and grew jealous."
            show spiral7 onlayer transient zorder 100
            w "\"I'll teach her a thing or two,\" he said, and whipped himself to my kingdom on the spot."
            mir "Oh Princess! I have need of your wisdom!"
            mir "If you are able to answer 3 riddles of mine, I will grant you a boon. But if you cannot answer, you must come serve me in hell."
            w "\"I accept!\" I said, because there wasn't a single riddle in the world I had not eaten whole."
            mir "Poke your fingers in my eyes and I will open wide my jaws. Linen cloth, quills, or paper, my greedy lust devours them all. What am I?"
            #TK: Look at a way to have the input screen appear when the answer is above it.
            python:
                answer1 = renpy.input("{i}Answer thee my riddles three:{/i}", length=8)

            if answer1 == "Scissors" or answer1 == "scissors" or answer1 == "Scissor" or answer1 == "scissor" or answer1 == "Shears" or answer1 == "shears" or answer1 == "Shear" or answer1 == "shear" or answer1 == "Clippers" or answer1 == "clippers" or answer1 == "Clipper" or answer1 == "clipper" or answer1 == "Cutters" or answer1 == "cutters" or answer1 == "Cutter" or answer1 == "cutter":
                mir "Confound it, that's right."
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
                if pig:
                    "You and the pig shook your heads and wept to hear such a sorry tale, and all around you the tears hit the floor and turned into terrible shrieking imps that swarmed around you, poking your soft legs and cackling cruelly at your misfortune."
                else:
                    "You shook your head and wept to hear such a sorry tale, and all around you the tears hit the floor and turned into terrible shrieking imps that swarmed around the both of you, poking your soft legs and cackling cruelly at your misfortune."
                "Such is life in Hell."
                jump hellStory
        "If you asked the pig for his tale, turn to page 219." if pig and not pig1Story:
            $pig1Story = True
            p1 "Very well, [povname]. I suppose you have earned the right to know my true nature. I must warn you, however, that this is a tale of such base depravity that it will turn your hair white to hear it."
            p1 "You see, long ago, I loved to do nothing but gamble. I gambled away all my money and earthly possessions, until I was cast out of every human city on earth and forced to live in a house of straw."
            p1 "Naturally, I soon gambled my straw house away. On the day before my creditors were due to take it from me, the Lord arrived at my door."
            miw "Please, my child. I have travelled far, and I have far to go yet. Provide me lodging for the night."
            p1 "\"You may stay under my straw,\" I told Him, \"but I warn you - I haven't a cent to my name.\""
            miw "That is of no concern. Take these three coins, and buy us some bread for the night."
            p1 "As you can imagine, I immediately gambled all the money away."
            p1 "I pretended to have dropped the coins in a puddle, but the Lord immediately saw through my clever ruse."
            miw "Do not test my forgiveness, pig. Here are another three coins. If you do not buy the bread this time, your immortal soul will be forfeit."
            p1 "\"Of course, Lord,\" I said in sorrow as I knelt before him. \"I will follow your orders to the letter.\""
            p1 "Naturally I went straight to the Devil Himself and gambled those three coins away again. For my winnings the Devil gave me a deck of cards that would allow me to win any game."
            p1 "Then I really got to work. Soon I had won half the world, and the Lord was forced to ask Death to stop my rampage."
            p1 "Death snuffed me out at the poker table, and so I went up to Heaven and knocked on the gates."
            miw "...No. We don't need you here. Be on your way, pig."
            p1 "So I went and knocked on the gates of Purgatory."
            wib "I don't think so. We have enough misery and trouble here. Be on your way, pig."
            p1 "And so finally I went and knocked on the gates of Hell, where they let me in at once. There was no-one there except for Lucifer and the hunchback devils."
            p1 "(The straight-backed devils were all away on business, you see.)"
            p1 "I challenged the old goat to a game at once, and soon I had won all the hunch-backed devils off Him. We all gambled into the night and made such a noise and racket that the Devil couldn't hear Himself speak."
            p1 "Finally He was forced to run to the Almighty, crying out:"
            mir "Please, O Lord, won't you rid me of this troublesome pig?"
            p1 "And so they took away my cards, and I was kicked out of Hell and forced to wander the land forever and never know true peace."
            "Just as the pig predicted, you saw your hair had turned white with shock to hear such a tale. You all shook your heads with sorrow."
            jump hellStory
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
        if pig:
            "You and the pig shook your heads and wept to hear such a sorry tale, and all around you the tears hit the floor and turned into terrible shrieking imps that swarmed around you, poking your soft legs and cackling cruelly at your misfortune."
        else:
            "You shook your head and wept to hear such a sorry tale, and all around you the tears hit the floor and turned into terrible shrieking imps that swarmed around the both of you, poking your soft legs and cackling cruelly at your misfortune."
        "Such is life in Hell."
        jump hellStory
    label hell:
        show hand onlayer transient:
            yalign 0.69#0.743
            xalign 0.5
        menu:
            w "We'd better get moving. I want to get back and see if my cottage is still standing."
            "If you investigated the cavern wall, turn to page 205." if not hellCavern:
                "Hell was a small cave, draughty and full of coal dust."
                "You looked through a hole in the cave wall and marvelled to see the imps cavorting in drunken song and dance beyond, each of them plotting to destroy the works of man and G-d."
                "You quickly retreated for fear of being seen."
                $hellCavern = True
                jump hell
            "If you investigated the centre of the cavern, turn to page 206.":
                "In the centre of the cavern was a small, homely cottage. You peered in the window."
                call hideAll from _call_hideAll_76
                show hellcottagebg at artPos
                "The Devil was not home, but you saw His old grandmother in a rocking chair in the corner. She spotted you both at once."
        dg "Oh, my dears! You must be terribly lost. You'd better get out of here."
        w "We don't know how - and I'm sworn to serve the Devil for the rest of my days."
        dg "Then you have a hard road ahead. My grandson will be home soon, and He will eat you up whole if He sees you."
        dg "But since I feel sorry for you, I'll see if I can help."
        if pig:
            "With a flick of her wrist she transformed you all into fat yellow and black carpenter bees."
        else:
            "With a flick of her wrist she transformed you both into fat yellow and black carpenter bees."
        w "Oh!"
        "The witch buzzed around joyously."
        w "This might seem strange but, I've always kind of wanted to be a bee."
        pov "We still have some questions."
        dg "Here. Hide in my skirts, and I will see what answers I can coax from Old Nick."
        "She quickly tucked you both into her skirts."
        "Soon, the Devil came home, and no sooner did He enter the house than He noticed the air was not pure."
        mir "Crinkle, crush, wailing and fleeing. I smell the flesh of a human being."
        if pig:
            mir "And is that... the smell of a pig?"
            mir "Could it truly be my old nemesis returned at last?"
        "With this he picked up the whole house and began to turn it over looking for the flesh he smelled."
        if godfather == "Red":
            "You shook to see your Godfather before your eyes at last."
        if pig:
            "The pig shivered beside you at the sight of his old rival."
        dg "Hush, you young fool. You're always smelling human beings."
        dg "You're making a mess of the nice clean floors I just swept. Now come have some of the soup I made you."
        "Grumbling, He put the house back down on its foundations and sat down to eat and drink. Soon He was curled up fast asleep and snoring on His grandmother\'s lap."
        jump devilGrandmaquestions

    label devilGrandmaquestions:
        #TK: Add questions about how to defeat the false hydra
        show hand onlayer transient:
            yalign 0.621#0.743
            xalign 0.5
        menu:
            dg "Quickly now, you two. What are your questions?"
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
                    mir "Unless of course, [he] look me in the face and recite my second and most secret name, Belthuselah. But that will never happen!{vspace=160}{i}In your notes, write down that you {b}know the Devil's second and most secret name.{/b}{/i}"
                else:
                    mir "Unless of course, [he] looks me in the face and recites my second and most secret name, Belthuselah. But that will never happen!{vspace=160}{i}In your notes, write down that you {b}know the Devil's second and most secret name.{/b}{/i}"
                jump devilSleeps
            "If you asked how to free yourself, turn to page 247." if not escapeGodfather and godfather == "White":
                $dgAsked += 1
                call devilAnswers from _call_devilAnswers_2
                $escapeGodfather = True
                dg "I dreamed that a desperate young mother once pledged her child to God, as the Godfather - and that their child was bound to be taken by Him on [his] eighteenth birthday. Can [he] ever escape, do you think?"
                mir "Ha! That's easy."
                if he == "they":
                    mir "The Lord is blind to the desperate. All [he] have to do is take on the disguise of an old leper, and G-d will walk right by."
                else:
                    mir "The Lord is blind to the desperate. All [he] has to do is take on the disguise of an old leper, and G-d will walk right by."
                mir "But [he]'ll never do that!"
                jump devilSleeps
            "If you asked how to free yourself, turn to page 247." if not escapeGodfather and godfather == "Black":
                $dgAsked += 1
                $escapeGodfather = True
                call devilAnswers from _call_devilAnswers_3
                dg "I dreamed that a desperate young mother once pledged her child to Death, as the godmother - and that the child was bound to be taken by Her. Can [he] ever escape, do you think?"
                mir "Never."
                "The Devil grew sombre."
                mir "There is no trick or cheat. When the child receives Death's three messengers, [he] will have to go. And that will be that."
                jump devilSleeps
            "If you asked how to cure the witch's forgetfulness, turn to page 267." if not cureWitch:
                $dgAsked += 1
                $cureWitch = True
                call devilAnswers from _call_devilAnswers_4
                dg "I dreamed of a girl who had all her thoughts drift out of her head as heavy smoke. Do you think she could ever be cured?"
                mir "Ha! The fool! She can never be cured, and she will never know peace."
                mir "The only way she could help herself is to plant a garden in her hat, so that the flowers and herbs soak up the smoke and grow with her memories. Thus she will hold the barest part of her old knowledge."
                mir "But she'll never figure THAT out! Ha Ha Ha!"
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
                show wolf2 onlayer transient zorder 100
                mir "Something lies under that child's house."
                mir "What it is, I do not know."
                mir "And if I knew, I wouldn't speak of it."
                mir "Do not concern yourself with this dream. Soon, you will forget it."
                mir "As will I."
                jump devilSleeps
            #"What is the Snake my mother warned me about?":
                #dg "I will ask the Devil. What else?"
    label devilAnswers:
        if dgAsked == 1:
            "In a flash, she seized one of the 3 golden hairs on His head and yanked it out. The Devil came awake with a howl of pain."
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
            "The Devil leapt up and stomped around the house, shouting vile curses, but she soon calmed him."
            dg "I'm sorry, my grandson. But what can you do against dreams?"
            mir "Hmph."
            mir "What was the dream this time?"
        return
    label devilSleeps:
        if dgAsked == 1:
            "The grandmother began picking the lice from His head, and soon He fell asleep again and snored so loudly that the windows rattled."
            dg "Ask your second question, child."
            jump devilGrandmaquestions
        elif dgAsked == 2:
            "The grandmother spoke softly to Him and began lousing him again. Soon He settled down and was fast asleep once more."
            dg "Ask your final question, child."
            jump devilGrandmaquestions
        elif dgAsked == 3:
            "The Grandmother sang a sweet lullaby to calm Him."
            jump witchEnd
    label witchEnd:
        "Soon the old dragon fell soundly asleep, and His grandmother took him off to bed and closed the door."
        "She shook you out of her skirts and turned you back to your human forms."
        dg "Well! I'm sure you heard the answers you sought. Here are the Devil's three golden hairs."
        dg "Throw them into the fire, and you will be carried straight up the chimney and out of hell."
        w "Thank you so much. How can we ever repay you?"
        dg "No need. Just forgive my grandson his trifling ways. He is young and foolish, just as I once was."
        if pig:
            p1 "Just a moment, please."
            "The pig snuffled around the back of the cottage, and came back with a deck of cards in his mouth."
            p1 "Alright, we'd best be off. Quickly!"
        #Answers to all your questions.
        #"NOTE: You get answers to all your questions and then see scenes where you use all the answers."
        if witchFree == True:
            "You left the cottage and crawled down into the foundations beneath it. When you found the ancient serpent squatting beneath it, the witch speared it with her crooked finger, killing it instantly."
            "With that, she felt a weight fall from her shoulders. You turned and saw that the Devil's mark was no longer upon her."
            "Then you went to the cottage fireplace, threw in the three golden hairs from the Devil, and leapt inside."
            call hideAll from _call_hideAll_77
            show cottageintbg at artPos
            "In an instant, you flew right up the chimney and out into the witch's cottage."
        else:
            "And so you went to the cottage fireplace, threw in the three golden hairs from the Devil, and leapt inside."
            call hideAll from _call_hideAll_78
            show cottageintbg at artPos
            "In an instant, you flew right up the chimney and out into the witch's cottage."
        if godfather == "Red":
            "Alas, as you tumbled onto the floor of the cottage, you heard the clock strike midnight, and you saw a pair of terrible red boots stamp down in front of you."
            mir "Time's up, child!"
            mir "Now you are mine, just as your mother promised all those years ago."
            show hand onlayer transient:
                yalign 0.711#0.743
                xalign 0.5
            menu:
                mir "I'll keep you in a cave to darn my socks, and brew my grandmother's tea, and bake bread for all the hungry souls of Hell - and there's nothing you can do about it!"
                "Check your notes. If you {b}know the Devil's second and most secret name{/b}, turn to page 294.":
                    pov "Belthuselah."
                    mir "NOOOOOOOOOOOO! How? How did you discover my second and most secret name? Impossible!"
                    "In an instant, his spell over you broke. The Devil withered and shrank and spluttered with rage, until He grew as small as an ant, whereupon you kicked Him right into the fireplace and back to hell."
                    "With the Devil taken care of, you and the witch looked over the cottage."
                    "It was a mess of flowers and plants and flopping animals, sprouting wildly every witch-way across the room."
                    "You rolled up your sleeves and slowly put the room to rights, until it was even more clean, warm and homely than it had been before."
                "If you {b}have a pig{/b}, turn to page 295.":
                    p1 "Not so fast, my erstwhile adversary."
                    mir "No... it can't be..."
                    p1 "But it is! I've returned from the pit to challenge you once more."
                    "The pig revealed his deck of cards. At the sight, the Devil began sweating and shaking."
                    mir "No, please... you know I can never refuse a game of chance!"
                    p1 "All too well, you old goat. Deal."
                    "In a moment, the pig had thrashed the Devil, and won all the riches of Hell from Him. The King of Hell gave up your contract and fled the house in terror before the pig could challenge Him to another game."
                    "With the Devil taken care of, you all looked over the cottage."
                    "It was a mess of flowers and plants and flopping animals, sprouting wildly every witch-way across the room."
                    "You rolled up your sleeves and slowly put the room to rights, until it was even more clean, warm and homely than it had been before."
                "Otherwise, turn to page 297.":
                    call hideAll from _call_hideAll_79
                    show hellbg at artPos
                    "With a whoop, the Devil seized you and dragged you into the fireplace and straight to hell."
                    "Sadly, you were trapped there forever after. I saw the flames take you. The witch mourns you still."
                    call endStamp from _call_endStamp_13
                    "When misfortune is after someone, they may try to hide in all sorts of places or flee across the whole wide world, but it will still know where to find them."
                    #Wolf: Kills Toad
                    "..."
                    "Oh?"
                    "What happened to the toad, you ask?"
                    jump toadDisappears
        elif godfather == "White":
            w "Quick! Your Godfather will be here any minute."
            "You both leapt into action. You disguised yourselves as beggars and lepers and threw lumps of mud all over the half-ruined cottage so that it looked like an abandoned hovel."
            "Soon, the clock struck midnight, and you felt the light of G-d upon you."
            "It seared into your flesh as you huddled together on the floor, feeling His gaze searching for you as His heavy footfalls shook the house."
            "But He did not see you. And soon, you felt His light fade, and His gaze turned away, and His heavy footsteps fell away into the distance."
            "You and the witch clutched each other and laughed with terror and relief."
            "With G-d taken care of, you and the witch looked over the cottage."
            "It was a mess of flowers and plants and flopping animals, sprouting wildly every witch-way across the room."
            "You rolled up your sleeves and slowly put the room to rights, until it was even more clean, warm and homely than it had been before."
        elif godfather == "Black":
            "You slowly picked yourselves up and looked over the cottage."
            "It was a mess of flowers and plants and flopping animals, sprouting wildly every witch-way across the room."
            "Just then, the clock struck midnight. You looked around in terror, waiting for Lady Death or Her messengers. But none came."
            w "Looks like you still have some time left!"
            "You rolled up your sleeves and slowly put the room to rights, until it was even more clean, warm and homely than it had been before."
        if villageRich == True:
            call hideAll from _call_hideAll_80
            show townextbg at artPos
            "Once the cottage was put to rights, you went to the village and fed some grapes to the mouse at the bottom of the village well."
            "In an instant, the well began to flow with the richest and most satisfying red wine, and all throughout the village rejoiced."
            "The village soon prospered by selling the wine, and you and your family became rich beyond your wildest dreams."
        if cureWitch == True:
            call hideAll from _call_hideAll_81
            show cottageintbg at artPos
            "You stayed with the witch for a while after that, helping her with her forgetfulness."
            "Over time you cultivated a garden in her hat, using the knowledge you tricked out of the Devil."
            if godfather != "Black" and mushroomCurse and not persistent.mushroomVanished:
                "You told the wise old Mushroom the story of your misadventures in hell, and she loved it so much that she blessed you with a mushroom's blessing, so that you always had a green thumb."
            "You sowed green grass and lavender and rosemary and thyme, and bottlebrushes and honeysuckle and silver spurflowers."
            "The smoke pooled under her hat and nourished these flowers at the roots, so they grew rich and wild with her memories."
            "Although she would never be the Girl Who Knew Everything again, she knew enough."
            if witchFree == False:
                "Alas, despite everything you'd done, she still remained sworn to the Devil. Her promise to him was kept in a secret place that he guarded jealously, and you were never able to find it."
                "Every witch's Sabbath, she was forced to ride away to dance on the Thornton Peak, and commit all kinds of wicked and terrible acts in his name."
                "Still, you spent many peaceful months staying with her, cultivating her garden, putting her cottage to rights, and helping her rewrite all her old notebooks again."
            elif witchFree == True:
                "She was free from the Devil at last."
                "You spent many peaceful months staying with her, cultivating her garden, putting her cottage to rights, and helping her rewrite all her old notebooks again."
        else:
            call hideAll from _call_hideAll_82
            show cottageintbg at artPos
            "You stayed with the witch for a while after that, trying to help her with her forgetfulness."
            "Sadly, you knew not how. You tried everything you could, but for the rest of her days, her thoughts were cursed to leak from her head in heavy smoke."
            if witchFree == False:
                "Alas, despite everything you'd done, she still remained sworn to the Devil. Her promise to him was kept in a secret place that he guarded jealously, and you were never able to find it."
                "Every witch's Sabbath, she was forced to ride away to dance on the peak of Thornton Peak, and commit all kinds of wicked and terrible acts in his name."
            "Still, you spent many peaceful months staying with her, cultivating her garden, putting her cottage to rights, and helping her rewrite all her old notebooks again."
            if witchFree == True:
                "She would never be the Girl Who Knew Everything again, but at least she was free. The Devil haunted her no longer."
        show hand onlayer transient:
            yalign 0.72#0.743
            xalign 0.5
        menu:
            "Finally, you'd done as much as you could to help. She had recovered enough to take care of herself again."
            "If you stayed with the Witch, turn to page 291.":
                "But you found you didn't want to leave after all."
                "You stayed there in the cottage, and tended to the herbs and wildflowers, and helped her gather ingredients for her potions."
                if pig:
                    "The pig bid you a tearful farewell and travelled off across the country, gambling with his magic cards until he owned half the world."
                "The witch created salves and poultices for you and your family, keeping them all in good health into their old age."
                if godfather == "Black":
                    "You lived there in quiet happiness for many years."
                    "But youth does not last forever."
                    "One day, you felt yourself wracked with a terrible fever."
                    "Then, you felt gout take hold of you and make all your limbs twitch, and you were wracked with one illness after another, and you fell into deep sleep for long days."
                    "Not even the witch could help you, though she toiled at your bedside for many long hours."
                    w "I'm sorry. I-I wish I could do more... I should be able to heal this."
                    pov "Don't worry. I won't die until Death sends Her messengers."
                    "But as you spoke, there was a knock on the door, and the Witch opened it to reveal the wise mushroom from the forest."
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
                                        "I wept in the shadows."
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
                                call hideAll from _call_hideAll_83
                                show mementobg at artPos
                                "She gently took you down to the kingdom of Death."
                                call endStamp from _call_endStamp_14
                                "And what happened to you after that, none who live can say."
                                #Wolf: Kills toad
                                "..."
                                "Oh?"
                                "What happened to the toad, you ask?"
                                jump toadDisappears
                else:
                    call endStamp from _call_endStamp_31
                    "You lived there together in quiet happiness. If you have not died, you live there still."
                    #Wolf: Kills toad
                    "..."
                    "Oh?"
                    "What happened to the toad, you ask?"
                    jump toadDisappears
            "If you returned home, turn to page 261.":
                call hideAll from _call_hideAll_84
                show sunbg at artPos
                "When it was time to leave, you wished the Witch a tearful farewell, and returned to your cottage with your family."
                if pig:
                    "The pig wished you a long and happy life before leaving. He travelled off across the country, gambling with his magic cards until he owned half the world."
                if godfather == "Black":
                    "You lived there in quiet happiness for many years."
                    "But youth does not last forever."
                    "One day, you felt yourself wracked with a terrible fever."
                    "Then, you felt gout take hold of you and make all your limbs twitch, and you were wracked with one illness after another, and you fell into deep sleep for long days."
                    "Not even the witch could help you, though she toiled at your bedside for many long hours."
                    w "I'm sorry. I-I wish I could do more... I should be able to heal this."
                    pov "Don't worry. I won't die until Death sends Her messengers."
                    "But as you spoke, there was a knock on the door, and the Witch opened it to reveal the wise mushroom from the forest."
                    if mushroomCurse:
                        m "I suppose my curse won't be needed after all."
                    m "It is time. Come with me."
                    jump deathQuestions
                else:
                    call endStamp from _call_endStamp_16
                    "You lived there for many long, happy years, visiting the Witch each summer. If you have not died, you live there still."
                    #Wolf: Kills toad
                    "..."
                    "Oh?"
                    "What happened to the toad, you ask?"
                    jump toadDisappears
    




#==========The Wolf Eats the Toad
label toadDisappears:
    $ renpy.block_rollback()
    call hideAll from _call_hideAll_243
    show cottageintbg at artPos
    "After you fell into the flames, he stood alone in the witch's cottage."
    "Bromeliads sprouted from the floorboards. The dense, hot spiral of greenery pressed in around him like the organs of a great beast."
    f "Well. This is another fine mess."
    "He picked up his top hat."
    play music hunted1
    "There was a sound outside. Almost like a howl. He shivered."
    f "I-I had best not outstay my welcome. Prickle! Crawl!"
    call hideAll from _call_hideAll_244
    show darkforestbg at artPos
    "He rushed outside, dove down through the puddle and emerged into the darkness of the forest."
    f "Shudder! Wink! Are you there?"
    "There was no reply. No-one was there."
    "He searched forward and found the remains of his squash carriage. "
    "It had been torn in twain. Jagged claw marks rent the sides."
    f "Oh no. No, no, no."
    #call musicSilence from _call_musicSilence_35
    "Something stirred in the forest around him. In the space between the trees. "
    call hideAll from _call_hideAll_245
    show forest5bg at artPos
    "He ran as fast as he could, helter-skelter, tumbling down hills, coat ripped, pants torn."
    stop music fadeout 6
    play music2 [ "<sync music>audio/hunted2.wav", "audio/hunted2.wav" ] fadein 1
    "Something fastened around his ankle."
    f "Agh!"
    "A terrible agony shot through him in an instant, and then was gone."
    "A red, wet stain dripped from his shoe. Red footprints were left behind him as he ran. His foot felt numb. There was no pain."
    call hideAll from _call_hideAll_246
    show townextbg at artPos
    "At last he saw the outskirts of town before him, and thanked G-d in heaven for the blessed sight."
    call hideAll from _call_hideAll_247
    show townextbg at artPos
    "The people of the village were there, cleaning up after the feast."
    #gmVanished
    #goVanished
    #shVanished
    #hVanished
    f "Please, fine townsfolk, help me! I'm being pursued by a wolf!"
    may "Oh, poor toad. Don't be silly."
    if not persistent.goVanished:
        go "There's no need to be afraid."
    if not persistent.hVanished:
        h "It's all in your head. There are no wolves in Australia."
    else:
        gm "It's all in your head! There are no wolves in Australia."
    if not persistent.hVanished:
        sh "Everyone knows that."
    f "B-but look! Look at the wound the beast wrought upon me!"
    "He brandished his bloody heel."
    may "Oh dear. Dear toad."
    if not persistent.hVanished:
        h "You've always had that wound. Don't you remember?"
    else:
        gm "You've always had that wound. Don't you remember?"
    may "You were born that way."
    stop music2 fadeout 6
    play music3 [ "<sync music2>audio/hunted3.wav", "audio/hunted3.wav" ] fadein 1
    f "I-"
    "His leg disappeared."
    f "Argckkhh!"
    "A ragged chunk."
    "A split in space."
    "The blood flew onto the cobblestones, and then was gone."
    "A wet, twisted mess was all that was left."
    "He fell over into the dirt."
    if not persistent.hVanished:
        h "Oh, you poor thing. Let me help you."
    else:
        may "Oh dear, you've gotten yourself into a scrape again. Come on."
    "They lifted him up and placed him against the fence. He clung to it with one shaking arm."
    gm "You really shouldn't go out without your cane."
    f "My... cane?"
    may "For your leg. You know."
    may "You've always had one leg."
    #f "But... I..."
    "The toad searched his memories and realised that it was true."
    "He was born with one leg."
    "A tough life, perhaps, but he'd always been able to survive."
    "How on earth had he forgotten his walking stick?"
    "Forget his own head next, I expect."
    f "I'm terribly sorry, I don't know what came over me. I'll-"
    stop music3 fadeout 6
    play music4 [ "<sync music3>audio/hunted4.wav", "audio/hunted4.wav" ] fadein 1
    "His arm was gone. The stump of a shoulder."
    "Exposed bone. Matted meat."
    "He cried out in terrible pain, and fell into the dirt once more."
    may "Well, it's been a long night."
    if not persistent.hVanished:
        h "Yes, we'd best be getting home."
    else:
        gm "Too right. We'd best be off."
    f "No - please!"
    call wolfApproaches from _call_wolfApproaches_16
    stop music4 fadeout 6
    play music5 [ "<sync music4>audio/hunted5.wav", "audio/hunted5.wav" ] fadein 1
    "They ambled off into the night, making pleasant small talk as they headed down the road."
    "The toad tried to pull himself along in the dirt. He had no legs to walk with. Just a single, shaking arm."
    f "Help me... G-d, help me…"
    stop music5 fadeout 6
    play music6 [ "<sync music5>audio/hunted6.wav", "audio/hunted6.wav" ] volume 2.0 fadein 1
    "It has been tough, hasn't it, Toad? Surviving all these years, with just one arm."
    "Just a single, broken hand to drag yourself along with."
    "But you did it. What an inspiration."
    f "Who… Who are you?"
    "How are you asking that question, Toad?"
    "You were born with no mouth."
    f  "Mhmm... Mhmmm!"
    "The poor creature attempted to scream. A pitiful sight indeed."
    "The townsfolk shook their heads, and withdrew indoors. He was always like this. Better not to dwell on it."
    show wolf6 onlayer transient zorder 100
    $persistent.vanished +=1
    $persistent.toadVanished = True
    $persistent.vanishedLast = "Toad"
    #$purge_saves()
    $ renpy.block_rollback()

    "And after all, now that they thought about it, what was there to dwell on? There was no-one there."
    "The streets were empty. There was never anything there at all."
    #"Forget my own head next, they said to themselves."
    #"It must have been nothing."
    "Nothing but a top hat and an old coat, that blew away in the wind and were gone."
    call endStamp from _call_endStamp_17
    "They were never seen again."
    jump end


    # play music hunted1
    # stop music fadeout 6
    # play music2 [ "<sync music>audio/hunted2.wav", "audio/hunted2.wav" ] fadein 1

    # stop music2 fadeout 6
    # play music3 [ "<sync music2>audio/hunted3.wav", "audio/hunted3.wav" ] fadein 1

    # stop music3 fadeout 6
    # play music4 [ "<sync music3>audio/hunted4.wav", "audio/hunted4.wav" ] fadein 1

    # stop music4 fadeout 6
    # play music5 [ "<sync music4>audio/hunted5.wav", "audio/hunted5.wav" ] fadein 1

    # stop music5 fadeout 6
    # play music6 [ "<sync music5>audio/hunted6.wav", "audio/hunted6.wav" ] volume 2.0 fadein 1
    #    $renpy.music.set_volume(0.6, delay=10.0, channel=u'music4')
    #$renpy.music.play("audio/rememberCleanInstFull.wav", channel='music', loop=True, relative_volume=1.0)
    #    stop music fadeout 6
    #play music2 [ "<sync music>audio/rememberDistInstFull.wav", "audio/rememberDistInstFull.wav" ] fadein 1 volume 1.0


#==========Witch Solo path
#The witch's path if the toad has disappeared
label witchSolo:
    #You walk through the woods towards the witch's house.
    call hideAll from _call_hideAll_172
    show forestbg at artPos
    "You walked through the woods."
    "Somehow, you already knew the way to the witch's cottage."
    if persistent.vanished >= 3 and not gilgameshPathFollowed:
        $renpy.show_screen("gilPath", _layer="screens", tag="map", _zorder=101)
        "Had you ever been this way before? You couldn't recall."
        $renpy.hide_screen("gilPath")
    else:
        "Had you ever been this way before? You couldn't recall."
    label gilPathShowingWitch:
        call hideAll from _call_hideAll_173
        show darkforestbg at artPos
        "The trail took you through a dense swamp of crooked mangroves."
    "Soon, you began to see a glimmer of silver light in the darkness."
    "The swamp was covered in puddles of water from the rains. Each one shone with light."
    "All around you, the woods were dark and empty. But when you looked into the water, you saw the reflection of a shining cottage below."
    play sound pageFlip
    call hideAll from _call_hideAll_174
    show lakefullbg
    ""
    play sound pageFlip2
    call hideAll from _call_hideAll_175
    show darkforestbg at artPos
    "For a brief moment, you thought you saw a figure reflected in the water. But as soon as you blinked, it was gone."
    jump puddleSolo

    label puddleSolo:
        show hand onlayer transient:
            yalign 0.68#0.743
            xalign 0.5
        menu:
            "The reflection of the cottage rippled in the water."
            "If you looked into the puddle carefully, turn to page 236." if not puddleLook:
                "You crawled to the edge and looked down into the puddle."
                call hideAll from _call_hideAll_176
                show cottagebg at artPos
                "The cottage in the reflection shone with bright light, as if the setting sun was behind it."
                call hideAll from _call_hideAll_177
                show darkforestbg at artPos
                "There was no trace of a cottage in the world above the water."
                $puddleLook = True
                jump puddleSolo
            "If you dropped a stick in the puddle, turn to page 206." if not puddleStick:
                "You picked up a stick from the ground, and tossed it into the puddle."
                "It fell in without a single ripple in the water."
                "You saw it drop through into the reflection, and land close to the cottage."
                "You looked up. There was no trace of it in the world outside the reflection."
                $puddleStick = True
                jump puddleSolo
            "If you jumped into the puddle, turn to page 207.":
                if pig:
                    "You grabbed the pig to you, then leapt into the puddle."
                else:
                    "You leapt into the puddle."
                call hideAll from _call_hideAll_178
                show mushroombasementbg at artPos
                "The world flipped over."
                "You felt the water pass over you, and a cool chill tingled all through your body."
                call hideAll from _call_hideAll_179
                show silverbg at artPos
                "When you opened your eyes, you were standing right way up again."
                "The puddle you had jumped into was now a floor, like a silver mirror."
                "The world all around you shone white."
                "At the centre of the puddle was the cottage, shining with light."
                call hideAll from _call_hideAll_180
                show cottagebg at artPos
                "Up over the walls grew a riot of herbs and flowers of every type, planted directly in the soil, rambling over everything and growing in a lush green-grass garden on the roof. "
                if pig:
                    "The pig munched on some violets blooming from the windowsill."
                w "Oh good!"
                "You stumbled back in surprise as a small, witchy figure popped out from behind the herbs."
                "Her hands were covered in ink. She had a fountain pen tucked behind her ear, a chaotic scramble of notepaper tucked under her arm and a thick bundle of string wrapped around her hand."
                w "You're just in time. [povname], right?"
                "She took out a fork wrapped in string and planted it firmly by her doorstep. It was labelled \"A1\"."
                "You looked around and noticed that her whole backyard was littered with forks stabbed into the ground. Each fork was tied with a knot of string and labelled with a letter of the alphabet. The lines of string led to a massive tangle of twine in her front window."
                w "Come on. You're just in time for the next round of experiments."
                "She grabbed your hand and pulled you inside."
                call hideAll from _call_hideAll_181
                show cottageintbg at artPos
                "Inside the cottage was a wild clutter of books and herbs and plants of all description, growing up the walls and roof."
                "The cottage was cramped, but the walls were covered with lines of string and notes and paper scrawled with indecipherable writing."
                #TK: Images for this stuff
                "The floor was covered in a network of flags and string in a grid pattern, each flag marked with a letter and number. You stepped over them gingerly to enter the room."
                "A message was painted across the wall in giant red letters: \"I OWN THIRTY TWO FORKS.\""
                w "We have two experiments running at the moment."
                show monster3 onlayer transient zorder 100
                play music hunted1
                "You heard something move outside the cottage."
                jump witchExperiments

        #You hear an echo that sounds like a howl.
        #
        #Your mouth tastes like salt and ash. Your vision blurs, and fades. Are you losing sight? Spots appear in front of your eyes.
        #Sound fades and goes soft. You hear a shrill whine in your ears.
        #Black spots appear in your vision.
        #
        #The edges of spaces don't seem to line up. The angles don't fit.
        #Your brain begins to shut down. Your organs shut down.
        #Your heart seems to shudder and burn in your chest.
        #Your rub your eyes furiously, but your vision doesn't clear.
        #There is a strange distortion. You can't seem to see past it. The air is completely clear, there's no fog or mist. And it isn't that dark tonight.
        #But still, for some reason you can't seem to see more than five feet ahead of you.

        #Play up the witch's paranoia and the fact that she hasn't slept

#==========The witch's 3 experiments
label witchExperiments:
    if experiments == 1:
        stop music fadeout 6
        play music3 [ "<sync music>audio/hunted3.wav", "audio/hunted3.wav" ] fadein 1
        #"You heard something moving in the walls of the cottage."
        "You looked at the walls of the cottage and noticed something wasn't right with them."
        "They looked like a picture that had been folded in on itself and reflected."
        "The witch didn't seem to notice."
    elif experiments == 2:
        stop music3 fadeout 6
        play music4 [ "<sync music2>audio/hunted4.wav", "audio/hunted4.wav" ] fadein 1
        "You blinked and rubbed your eyes furiously. There was a queer distortion in the air."
        "The air was completely clear, and the cottage was well-lit."
        "But still, for some reason you couldn't see more than five feet ahead of you."
    elif experiments == 3:
        stop music4 fadeout 6
        play music5 [ "<sync music4>audio/hunted5.wav", "audio/hunted5.wav" ] fadein 1
        "You heard a scrabbling sound."
        "It was coming from inside you. Like claws scratching in the creases of your brain."
        "Trying to get in."
        "You were having difficulty speaking. But you slowly walked forward and kept asking questions."
    elif experiments >= 4:
        stop music5 fadeout 6
        play music6 [ "<sync music5>audio/hunted6.wav", "audio/hunted6.wav" ] volume 4.0 fadein 1
        $renpy.music.set_volume(0.4, channel=u'music6')
        "You felt a deep pressure settle on you. Like being at the bottom of the ocean. Compressing your body from all angles. Your intestines knotted and twisted in coiled spirals."
        "It was done."
        "The witch noticed nothing."
        w "We need to warn people. Your family, especially."
        jump witchSoloFinale
    show hand onlayer transient:
        yalign 0.65#0.743
        xalign 0.5
    menu:
        w "What do you want to see?"
        "If you asked the witch how she knew you were coming, turn to page 236." if not witchCrystal:
            w "Crystal ball. Perks of being a witch."
            w "I was watching your house."
            "She laid her pile of notes down on the kitchen bench and scribbled in them as she talked."
            "There were dark bags under her eyes. It was clear she hadn't slept in days."
            w "I was so happy when I saw you were coming. There's something here you need to see."
            $experiments +=1
            $witchCrystal = True
            jump witchExperiments
        "If you looked at experiment 1, turn to page 236." if not witchExperiment1:
            $experiments +=1
            pov "So what's experiment 1?"
            "The witch gestured to the network of flags at her feet."
            w "This is what started everything."
            w "When I woke up a few days ago, I noticed something."
            w "Usually when I make my morning tea, it takes me 4 steps to get from the kettle to my front door."
            w "But when I made it that morning... it took me 3 steps."
            pov "What?"
            w "It's shrinking. You see?"
            "She points at the grid of flags laid all across the cottage floor."
            w "The flags start here."
            "She pointed to the front left corner of the cottage, at a flag labelled \"G-02\"."
            w "And they end here."
            "She points to the lower right corner of the house, at a flag labelled \"Z-10\"."
            w "But why would I do that? Why would I start the naming system at G-02, instead of A-01? How does that make sense as a numbering system?"
            #menu choice?
            pov "It... doesn't."
            w "Exactly."
            w "Here's my hypothesis. The initial numbering system {i}began at A-01{/i}. Since then, the space has shrunk."
            w "That's why the system now begins at this flag here, \"H-03.\""
            "She pointed at the starting flag."
            pov "But if the cottage was shrinking, we'd notice it."
            w "Not necessarily. My theory is that there is some kind of pressure, or force, that is stopping us from noticing or remembering. I just couldn't prove it - until I hit on the fork hypothesis."
            "She looked at you with a cold certainty."
            w "Things are being devoured. Not just from physical reality. From our minds."
            "You stared down at the starting flag, in the front left corner of the cottage."
            "It read \"I-03\". Just like it always did."
            $witchExperiment1 = True
            jump witchExperiments
        "If you looked at experiment 2, turn to page 236." if not witchExperiment2:
            $experiments +=1
            "The witch took you over to her front window, which you could see was stuffed with a giant, knotted network of string."
            "The string was labelled with all the letters of the alphabet. It stretched out through the window."
            "You looked outside and saw that it was tied onto dozens of forks stuck into the soil, all over her property."
            w "Once I encountered the Lacuna phenomenon, I tried to think of a way to measure it."
            pov "Lacuna?"
            w "A gap, a blind spot. A space that shouldn't be there."
            w "I tried to figure out where it's coming from - what's causing it. I tested out time of day - no results there. Are some objects more likely to disappear than others? Again, no visible pattern there. "
            w "I had a breakthrough when I considered that it might be {i}location based{/i}. Emanating from a particular point. The closer an object is to that point, the more likely it is to disappear. But I couldn't make any meaningful progress because I couldn't prove whether or not something had disappeared."
            #"She pulled out a giant pad of paper marked with a grid pattern. "
            #w "It's not just that I don't remember them - my memory, you know, not the greatest - but {i}my notes{/i} don't remember them either. They're gone, there's no record of them."
            "She held up a fork."
            w "Say this fork vanished. And not only that, but it vanished so completely that you never remembered it existing at all. How could you prove that it ever existed?"

            #TK: Add a menu of options here
            show hand onlayer transient:
                yalign 0.65#0.743
                xalign 0.5
            menu:
                w "How do you prove something {i}used{/i} to exist, if that thing now {i}does not exist, and never did?{/i}"
                "If you suggested making notes, turn to page 238.":
                    w "That's the scary part. Even my notes no longer mention the fork ever existing."
                    w "Somehow even they have been re-written by the new, forkless reality."
                    w "No, I've only found one way to detect the change."
                "If you suggested using magic or consulting magical beings, turn to page 239.":
                    w "Fantastic idea, but sadly impractical. I have consulted the Devil on this, of course."
                    w "I suspect He knows more than he's letting on, but sadly His comments have been completely unscientific. Totally useless for an experiment like this."
                    w "No, I've only found one way to detect the change."
                "If you had no idea, turn to page 241.":
                    pov "I... well..."
                    pov "I don't think you can, can you?"

            w "String."
            "She reached up and quickly tugged at each piece of string in the window in turn. Most of them held firm. One of them showed no resistance when she tugged."
            "She pulled that one through the window. It was a long, long piece and she rapidly wound it up until the end came through the window."
            "The end was tied into a loop with nothing inside."
            w "You see?"
            w "When an object vanishes, everything around it stays the same."
            w "So even though the fork is gone, {i}{b}the string remains.{/b}{/i}"
            "She pronounced this last part with maniacal glee."
            w "The phenomenon seems to be able to wipe objects from our memories, but it's not a perfect deletion. The physical signs that the object used to exist are still there."
            w "So when I pull back a piece of string that no longer has a fork in it, that means {i}a fork must have been there, and it disappeared.{/i}"
            w "From there it was simple. All I had to do is tie all my forks with pieces of string, and laying them out in a grid network, and record the location of each piece of string that doesn't have a fork in it. "
            "She carefully placed the string next to a big row of other pieces of looped string. Then she pointed at the writing on her wall that said \"I OWN TWENTY SEVEN FORKS.\""
            w "This message says I own twenty seven forks. But I have thirteen {i}forkless{/i} pieces of string. That means at least thirteen forks have disappeared since this experiment began."
            w "The question then of course is, why has the message changed to fit the new forkless reality - yet the strings are left behind?"
            w "Does this anomaly have some kind of limited ability to warp language, specifically?"
            w "It almost seems to suggest some kind of active sentience behind it. It notices some things, and changes them, but misses other things. Like it's been carelessly censored."
            "She whipped out her pencil and began recording a pattern of dots on her grid."
            "You noticed a place in the top left of the grid labelled \"INCIDENT ZONE\"."
            pov "So... where are the disappearances coming from?"
            pov "Is that what your grid shows?"
            w "That's why I was so glad to speak to you."
            "She tapped the INCIDENT ZONE label."
            w "It's your house."
            w "And it seems to be moving outward."
            $witchExperiment2 = True
            jump witchExperiments
        "If you looked at experiment 3, turn to page 236." if not witchExperiment3:
            $experiments +=1
            "You noticed a small closet in the back of the cottage, with a sign on the door said \"Experiment Site 3\"."
            pov "What's that one?"
            w "Hmm?"
            w "Oh... I, uh..."
            "She looked confused."
            "You opened the closet and peered in carefully."
            "Inside was a tiny set of gentlemen's clothes, carefully folded on a stool. Small enough for a rat to wear."
            "A tiny top hat was placed on top of the pile, with a pair of miniature dress shoes next to it."
            pov "What is this?"
            "The longer you stared at tiny bundle of clothes, the more a sense of powerful and implicit wrongness crawled under your skin."
            "Something about them didn't fit. They didn't belong here."
            w "I don't remember this."
            "The closet was suffocating. There was barely room to breathe. You felt the urge to get out in the fresh air."
            "You forced yourself to move closer to the clothes. You picked up one of the tiny dress shoes. The bottom was encrusted with mud."
            pov "They must be the clothes from... an old childhood toy you used to have."
            pov "It's probably nothing."
            w "Of course. Yes of course, that must be it!"
            w "I remember now. Nothing at all. Just an old toy."
            # "The witch picked up a pile of notes next to you and begins to leaf through them."
            # w "The notes say I found them on... the 4th, just a few days ago."
            # w "I found them in the corner of the cottage. Just lying there."
            # w "I'm sorry, I can't remember - But the notes are here. I record everything."
            # "She flips through her notes faster and faster, looking away from the clothes."
            # w "Note - my mind keeps making up explanations for them. \"My brother must have left them here.\" \"Maybe my grandmother knitted them for me, as a gift.\" Doesn't make any sense, of course - haven't spoken to my family in years."
            # w "But, there is a strong impulse here to explain, to override, to confabulate, to dismiss them and assume that they mean nothing. Do you feel that?"
            #
            # "Something about the angles seemed wrong. Sweat streamed down your face."
            # pov "Maybe they were the clothes from... an old childhood toy you used to have."
            # pov "It's probably nothing."
            # w "Exactly. You feel the impulse to ignore them. I feel it too. Like a riptide. Even though I've been investigating these phenomena, the urge grips me to forget it, ignore it, stop worrying."
            # w "The brain pushes us to overwrite these gaps. A natural instinct? Have we always had an instinct like this, to pattern-match, to make things make sense? An inherent impulse to make order of chaos, to remove the blind spot."
            # w "But then again, what if it isn't a natural impulse? What if it's something external, a force or pressure with the ability to imprint this impulse within us?"
            # w "A gap that does not wish to be observed."
            # "As you stared at it, your vision swam, and you had to look away and scrub your eyes."
            "Dark spots swam at the corners of your vision. You dropped the shoe and staggered out of the closet."
            $witchExperiment3 = True
            jump witchExperiments

#==========The final moments of the witch, before she disappears.
label witchSoloFinale:
    #==The wolf takes over you.
    "You felt a strangling pressure in your throat."
    w "This all seems so familiar - I'm sure I've seen it before. I knew its name."
    w "But we need to act fast. Now we know this Lacuna is coming from your house, we can -"
    "Your tongue was fat and poisonous in your mouth."
    "It twisted, and spoke."
    pov "This is an exciting theory, isn't it?"
    pov "It makes you the hero. A visionary."
    pov "You saw what no-one else could. Now only you can stop it. Thrilling."
    pov "But I think you are overlooking a much simpler explanation."
    $renpy.music.set_volume(1, delay=10.0, channel=u'music6')
    w "What do you mean?"
    pov "Memory loss. Confusion."
    pov "Difficulty performing familiar tasks."
    pov "Withdrawing from friends and family."
    pov "Losing the ability to think clearly."
    pov "What do these symptoms suggest to you?"
    w "I-"
    w "No. No, that's not possible."
    "Her voice was unsteady."
    w "I- I know I have struggled in the past. But it's not just me. We proved it."
    w "It can't just be in my head. What about the strings?"
    pov "What strings?"
    "She turned around. There were no strings on the windowsill."
    "The floor of the cottage was clear. There were no flags."
    "There never were."
    w "That's - I can't - what about the forks?"
    pov "You're confused, dear. You don't own any forks."
    pov "Don't you remember? You never have. "
    "The witch looked out the window and saw that you were right. The ground was bare. The cottage was empty. There were no forks in sight."
    "Your throat pulsed and pushed the words out of your teeth."
    pov "You eat with your hands. Your bare hands. Like an animal."
    pov "Your claws. Your teeth."
    pov "You always have. You told me so."
    w "No. No, I wouldn't do that. They have to be here."
    "The witch began to ransack the house, pulling out drawers and shelves, but there was nothing inside."
    "On the wall was a smeared message in bright red paint. It said \"I OWN NOTHING.\""
    stop music6 fadeout 12
    pov "I'm worried about you, dear. We all are."
    pov "Staying all alone in this tiny, tiny cottage, all by yourself. It's barely enough room to fit."
    "The walls pressed in on you. You didn't even have space to stand fully upright."
    pov "We've known each other for so long."
    w "We have?"
    "You felt your throat muscles burn as they constricted in your throat. Your voice came out, sounding soft and comforting."
    pov "Of course. So many years now. We wouldn't lie to you. We only want you to be safe."
    pov "You have to trust me. You're not well. These things you're seeing... they aren't there."
    "The witch spoke in a very small voice."
    #    $renpy.music.set_volume(0.6, delay=10.0, channel=u'music4')
    #    

    w "..."
    w "Okay."
    pov "This really is the best thing, dear. For your health."
    $renpy.music.play("audio/rememberCleanInstFull.wav", channel='music', loop=True, relative_volume=1.0)
    "She looked down at her hands. They were shaking. Tears welled up in her eyes, and you looked away courteously."
    w "I was doing so well. I thought I was better."
    w "I really, really thought..."
    "There was a long silence."
    w "Well. It doesn't matter now."
    w "I- I'll pack my things. I know you only want me to be safe."
    pov "I'm so glad."
    pov "Don't worry. Everything is going to be fine."
    pov "I'll get the others, and we'll come back for you and your things."
    pov "We can set you up in the village somewhere safe. Where you aren't a danger to yourself."
    "Your muscles clenched, and pulled you upright."
    "The witch's face was scrunched up and she was rubbing her eyes."
    #stop music fadeout 6
    call wolfApproaches from _call_wolfApproaches_20
    w "Thank you. I'm sorry."
    pov "There's no need to be sorry. I forgive you."
    "She looked at you. Her eyes were large and terrified."
    w "Y-you'll come back for me, right?"
    pov "Of course. I'll be right back."
    w "I'm sorry."
    "Your muscles constricted, and your legs jerked. Your arms pulled you through the miniature doorway and out of the witch's house."
    "You saw the witch once in the doorway, looking scared and alone in the crushingly small space of her tiny, tiny cottage."
    stop music fadeout 6
    play music2 [ "<sync music>audio/rememberDistInstFull.wav", "audio/rememberDistInstFull.wav" ] fadein 1 volume 1.0
    show wolf12 onlayer transient zorder 100
    "Then the door closed, and your body turned around."
    $persistent.vanished +=1
    $persistent.witchVanished = True
    $persistent.vanishedLast = "Witch"

    #$purge_saves()
    $ renpy.block_rollback()

    call hideAll from _call_hideAll_182
    show nightbg at artPos
    "You felt the tension leave you, like surfacing from the bottom of the ocean. You bent over and hacked some twisted, bloody thing out of you and onto the grass."
    "It looked like a matted clump of dark fur. You glanced at it once, then looked away and forgot it forever."
    "The night was cool and quiet. There was a lovely breeze blowing."
    if persistent.starsVanished:
        "You were in the middle of a large, empty field. The blank sky was above you. The grass crunched under your feet. Nothing beside remained."
    else:
        "You were in the middle of a large, empty field. The stars twinkled above you. The grass crunched under your feet. Nothing beside remained."
    "Why did you come out here?"
    "You couldn't recall. There's no-one living out this way."
    "Never has been."
    "You shook your head and laughed at your own foolishness. You must have gotten lost again. You've been so forgetful lately."
    "But no matter. It was a beautiful night. Perfect for a walk."
    "You stretched your legs, and began the long walk back to the village and home."
    "Far away, a small piece of string with a loop in it fell into the river, and was gone."
    "There is nothing else to say. The tale is told."
    "If you like it, praise it."
    call endStamp from _call_endStamp_44
    "If not, let it be forgotten."
    jump end

#=====================INVESTIGATION SCENES
#These scenes allow the player to investigate when characters have disappeared

    # play sound lacuna1
    # "Testing Lacuna Sting 1."
    # queue sound lacuna2
    # "Testing Lacuna Sting 2. Note: I'm using Queue, so Sting 2 will play after Sting 1 is complete (to avoid interruptions)."
    # queue sound lacuna3
    # "Testing Lacuna Sting 3."
    # queue sound lacuna4
    # "Testing Lacuna Sting 4."
    # queue sound lacuna5
    # "Testing Lacuna Sting 5."
    # queue sound lacuna6
    # "Testing Lacuna Sting 6."


#Deep in the woods, when the toad or witch have disappeared.
label toadWitchInvestigate:
    call hideAll from _call_hideAll_183
    show nightbg at artPos
    show eaten onlayer transient zorder 100
    "The woods were quiet."
    show hand onlayer transient:
        yalign 0.676#0.743
        xalign 0.5
    menu:
        "Silence lurked behind the trees."
        "If you discovered a muddy cave on the riverside, go to page 120." if persistent.toadVanished:
            #Investigation scene in Toad's abandoned home
            jump toadInvestigate
        "If you discovered a strange cottage, go to page 121." if persistent.witchVanished:
            #Investigation scene in Witch's abandoned home
            jump witchInvestigate
        "If you went searching for the witch, go to page 121." if not persistent.witchVanished:
            if persistent.vanished == 3:
                "The hairs at the back of your neck prickled."
                show hand onlayer transient:
                    yalign 0.676#0.743
                    xalign 0.5
                menu:
                    "You had a sense of finality. Like the wolf's jaws closing around you."
                    "If you continued on, go to page 121.":
                        jump witchSolo
                    "If you turned back, go back to page 84.":
                        jump toadWitchInvestigate
            else:
                jump witchSolo
        "If you wandered aimlessly, finding nothing, go to page 124." if not wanderedNightGod:
            "You walked through the woods for long hours, picking paths at random. Eventually, you came to a clearing. You looked up."
            queue sting lacuna4
            call hideAll from _call_hideAll_184
            show nightgodbg at artPos
            "The Firmament was gazing down upon you."
            "You looked up at Her in awe."
            label creepiestShowing:
                $renpy.show_screen("creepiestBooks", _layer="screens", tag="map", _zorder=101)
                "Where did She come from? What colossal, slow thoughts does She think up there?"
                $renpy.hide_screen("creepiestBooks")
            "None alive could say."
            "A single tear dropped from Her eye, and streaked across the sky like a falling star."
            "You sat there for a long time."
            "Finally, you turned around, and found yourself back where you began."
            $wanderedNightGod = True
            call hideAll from _call_hideAll_185
            jump toadWitchInvestigate
        "If you returned to the village, go back to page 50.":
            if persistent.vanished >=2:
                show noteDeal onlayer transient zorder 100
            "You turned and walked back to the light of the village."
            jump village

#Deep in the woods, when the thief or mushroom have disappeared.
label thiefMushroomInvestigate:
    call hideAll from _call_hideAll_96
    show forest4bg at artPos
    show characters onlayer transient zorder 100
    "The grass rustled."
    show hand onlayer transient:
        yalign 0.665#0.743
        xalign 0.5
    #You can investigate the thief or mushroom (if they have vanished)
    menu:
        "The trees pressed close around you."
        "If you discovered a rotting strangler fig, go to page 120." if persistent.mushroomVanished:
            #Investigation scene in mushroom's abandoned tree
            "You walked until you discovered a giant old tree."
            jump mushroomInvestigate
        "If you went searching for the mushroom, go to page 121." if not persistent.mushroomVanished:
            if persistent.vanished == 3:
                "The hairs at the back of your neck prickled."
                show hand onlayer transient:
                    yalign 0.676#0.743
                    xalign 0.5
                menu:
                    "You had a sense of finality. Like the wolf's jaws closing around you."
                    "If you continued on, go to page 121.":
                        jump mushroomSolo
                    "If you turned back, go back to page 84.":
                        jump thiefMushroomInvestigate
            else:
                jump mushroomSolo
        "If you discovered a rusting wreck, go to page 122." if persistent.thiefVanished:
            #Investigation scene in thief's abandoned train
            call hideAll from _call_hideAll_186
            show darknessbg at artPos
            "You walked through the darkness of the woods until you discovered an abandoned old train."
            queue sting lacuna1
            jump thiefInvestigate
        "If you wandered aimlessly, finding nothing, go to page 128.": #if not wanderedAimlessly
            call hideAll from _call_hideAll_187
            show forest5bg at artPos
            "For some reason you wandered off into the dark woods, picking paths at random."
            show news onlayer screens zorder 101:
                yalign 0.175#0.743
                #xalign 0.5
            "You found nothing and no-one. There was nothing there. Nothing but a cold silence that slowly followed you from behind the trees."
            hide news onlayer screens
            "..."
            queue sting lacuna5
            show hand onlayer transient:
                yalign 0.665#0.743
                xalign 0.5
            menu:
                "What are you doing?"
                "Searching for someone I once knew.":
                    "A foolish endeavour. There is no such person."
                    "There never was."
                "Searching for the place between the trees.":
                    "A foolish dream. There is no such place."
                    "There never was."
                "Searching for nothing in particular.":
                    "Very well. Curiosity is a fine vice for the hero of a tale like this."
                    "But everything has a limit. You should return to the village. The story is waiting for you."
                "Searching for you.":
                    "There is no need for that, child."
                    "I am here."
                    "I always have been."
            "You wandered in circles for a long time."
            "Finally, you found yourself back where you began."
            #$wanderedAimlessly = True
            jump thiefMushroomInvestigate
        "If you returned to the village, go back to page 50.":
            "The lights and warmth welcomed you back."
            jump village

#Exploring the toad's house when he has disappeared.
label toadInvestigate:
    #You investigate the toad's hole and find clues about the mystery
    "You walked along the side of the river. The water was still and deep. There was a small, muddy hole on the edge of the riverbank."
    queue sting lacuna1
    show hand onlayer transient:
        yalign 0.675#0.743
        xalign 0.5
    menu:
        "No reason to tarry here."
        "If you entered the hole, turn to page 207.":
            "You crouched down and slithered into the hole. Mud covered you."
            "It was wet, and cramped, and crawling with small worms and roaches. "
            "A cold silence lay coiled in the hollow like thick fog."
            "Why did you come here?"
            $renpy.music.play("audio/rememberDistInstFull.wav", channel="music", fadein=10.0, relative_volume=0.3, loop=False)
            label toadInvestigateMenu:
                show hand onlayer transient:
                    yalign 0.678#0.743
                    xalign 0.5
                menu:
                    "You had best return to your home and the people who love you."
                    "If you searched the nearby area, turn to page 208.":
                        $renpy.music.set_volume(0.6, delay=8.0, channel=u'music')
                        label essay2Showing:
                            $renpy.show_screen("essay2", _layer="screens", tag="note", _zorder=101)
                            "You uncovered a pantry with a single, mouldy piece of bread, and a pit sunk into the muck of the wall with the remains of an old fire."
                            $renpy.hide_screen("essay2")
                        "The silence watched you."
                        $renpy.music.set_volume(0.3, delay=8.0, channel=u'music')
                        jump toadInvestigateMenu
                    "If you explored deeper in, turn to page 209.":
                        $renpy.music.set_volume(0.9, delay=8.0, channel=u'music')
                        "You crawled through a tunnel in the back which lead down into the mud."
                        "At the end of the tunnel was a small room with a bed and a closet."
                        "Inside the closet were two threadbare costumes. A witch and a unicorn."
                        #queue sting lacuna2
                        label toadDiaryShowing:
                            $renpy.show_screen("tDiary", _layer="screens", tag="map", _zorder=101)
                            "Nothing beside remained."
                            $renpy.hide_screen("tDiary")
                            jump toadInvestigateMenu
                            $renpy.music.set_volume(0.2, delay=8.0, channel=u'music')
                        jump toadInvestigateMenu
                    "If you turned and left this awful place, turn to page 50.":
                        "You turned around and crawled back up out of the hole."
                        pov "What a terrible place that was. Never shall I return there again."
                        stop music fadeout 10.0
                        jump toadWitchInvestigate
        "If you returned to the village, return to page 50.":
            jump village
        # "The toad directed you to a small, muddy hole on the river bank. As soon as you entered, the mud fell down behind you and blocked your exit."
        # "The hole was wet, and cramped, and crawling with small worms and roaches, but it was safe."
        # if pig:
        #     "You shivered in the cold. The toad flopped down beside you, becoming a wet quoll. The pig grunted sadly in the form of a fruit bat."
        # else:
        #     "You shivered in the cold. The toad flopped down beside you, becoming a wet quoll."
        # #You explore the toad's home and get to know him better
        # label toadExplore1:
        #     show hand onlayer transient:
        #         yalign 0.65#0.743
        #         xalign 0.5
        #     menu:
        #         fq "Well. This is another fine mess I've made."
        #
        #             $toadCave = True
        #             "You uncovered a rug and a fireplace in the muck, and lit the fire."
        #             if pig:
        #                 "The toad uncovered a pantry with a single, mouldy piece of bread and toasted it over the fire for the three of you."
        #             else:
        #                 "The toad uncovered a pantry with a single, mouldy piece of bread and toasted it over the fire for the both of you."
        #             fq "This all the food I have, sorry."
        #             jump toadExplore1
        #         "If you explored deeper in, turn to page 209." if not toadBasement:
        #             $toadBasement = True
        #             "You travelled down a hole in the back of the cave which lead down into the mud."
        #             "Down the hole was a small room with a bed and a cupboard."
        #             "The toad opened the cupboard and took out two threadbare costumes: a witch and a unicorn. You pulled them around you for warmth."
        #             if pig:
        #                 "The pig grunted in appreciation."
        #             fq "I... used to like to dress up in this stuff. I'd put on little plays and things for myself."
        #             fq "Pretty dumb, I know. Kid's stuff. Haven't done it in years."
        #             "But the costumes seemed well cared for."
        #             jump toadExplore1
        #         "If you asked the toad about this place, turn to page 216." if not toadWhere:
        #             $toadWhere = True
        #             pov "Where are we?"
        #             fq "This is my home. My real home."
        #             fq "That's right. The grand fortune? The prestigious inheritance? The manor on the hill? All lies."
        #             fq "I've lived in this hole near the witch's cottage since I was a tadpole."
        #             fq "Yes, I know it might be hard to believe with my noble bearing. But it's all true."
        #             jump toadExplore1
        #         "If you asked about the toad's curse, turn to page 217." if not toadCurse:
        #             $toadCurse = True
        #             pov "I'm sorry. Now we'll never be able to cure your curse."
        #             fq "Oh... don't worry about that."
        #             fq "There was never a curse."
        #             fq "I just didn't want to be me anymore."
        #             jump toadExplore1
        #
        #         "If you looked for a way out, turn to page 218.":
        #             pov "How are we going to get out of here?"
        #             fq "Don\'t worry. I'm sure {b}{i}he{/i}{/b} will rescue us soon."
        #             pov "{i}He?{/i}"
        #             "Suddenly the ceiling burst open and a shining light came upon you, blinding in its glory."
        #             "Out from the light strode the most beautiful frog you'd ever seen."
        #             if pig:
        #                 "The pig rolled over in shock and transformed into a turtle."
        #             "His skin was glimmering green like the wings of summer beetles, his muscles rippled with strength, his eyes threw out glances of fire, and he was dressed in a gorgeous midnight-blue suit."
        #             "On each finger gleamed a golden ring inlaid with precious jadestone and chrysoprase and emeralds, and his finely-coiffed hair waved in the breeze with such beauty that none had ever seen the like, not even in a dream."
        #             mysFrog "Are you quite alright?"
        #             pov "Who are you?"
        #             "The toad sighed."
        #             fq "This..."
        #             fq "...is Brildebrogue Chippingham."
        #             bc "The very same!"
        #             "The frog beamed and helped you to your feet as you transformed into a garden rake."
        #             bc "Say, that voice is awfully familiar..."
        #             bc "Is that you, Blort?"
        #             fq "Yes. Yes, that's my real name."
        #             fq "I am Blort Bronkum, and I have never succeeded at anything in my life."

#Exploring the witch's house when she has disappeared.
label witchInvestigate:
    #You investigate the witch's cottage and find clues about the mystery
    "You walked through the trees until you began to see a glimmer of silver light in the darkness."
    call hideAll from _call_hideAll_188
    show darkforestbg at artPos
    "The forest was covered in puddles of water from the rains. Each one shone with light."
    "All around you, the woods were dark and empty. But when you looked into the water, you saw the reflection of a shining cottage below."
    queue sting lacuna1
    label puddle2:
        show hand onlayer transient:
            yalign 0.68#0.743
            xalign 0.5
        menu:
            "The sight was strangely familiar."
            
            "If you looked into the puddle carefully, turn to page 236." if not puddleLook:
                "You crawled to the edge and looked down into the puddle."
                "The surface of the water was flat and still."
                call hideAll from _call_hideAll_189
                show cottagebg at artPos
                "The cottage in the reflection shone with bright light, as if the setting sun was behind it."
                call hideAll from _call_hideAll_190
                show darkforestbg at artPos
                "There was no trace of a cottage in the world above the water."
                $puddleLook = True
                jump puddle2
            "If you dropped a stick in the puddle, turn to page 206." if not puddleStick:
                "You picked up a stick from the ground, and tossed it into the puddle."
                "It fell in without a single ripple in the water."
                "You saw it drop through into the reflection, and land close to the cottage."
                "You looked up. There was no trace of it in the world outside the reflection."
                $puddleStick = True
                jump puddle2
            "If you jumped into the puddle, turn to page 207.":
                if pig:
                    "You grabbed the pig to you, then leapt into the puddle."
                else:
                    "You leapt into the puddle."
                call hideAll from _call_hideAll_191
                show mushroombasementbg at artPos
                "The world flipped over."
                "You felt the water pass over you, and a cool chill tingled all through your body."
                call hideAll from _call_hideAll_192
                show silverbg at artPos
                "When you opened your eyes, you were standing right way up again."
                $renpy.music.play("audio/rememberDistInstFull.wav", channel="music", fadein=10.0, relative_volume=0.3, loop=False)
                "The puddle you had jumped into was now a floor, like a silver mirror."
                "The world all around you shone white."
                "At the centre of the puddle was a cottage in the middle of a garden."
                jump witchCottageInvestigate
    label witchCottageInvestigate:
        show hand onlayer transient:
            yalign 0.68#0.743
            xalign 0.5
        menu:
            "The whole scene was still and silent."
            "If you explored the cottage, turn to page 207." if not inCottage:
                $renpy.music.set_volume(0.6, delay=8.0, channel=u'music')
                $inCottage = True
                "You walked up the front steps, and put your hand on the doorknob."
                "The door opened up with a shuddering creak."
                "Inside the cottage was a wild clutter of books and herbs and plants of all description, growing up the walls and roof."
                "The cottage was tiny, but the walls were covered with bookshelves stuffed with old manuscripts and notebooks and thick textbooks on all kinds of plants and animals."
                "The wooden bookshelves were sprouting with herbs and plants of every type."
                "In the corner was a small kitchen with a cauldron, and up above was a small attic crawl-space."
                jump witchCottageInvestigate
            "If you explored the attic, turn to page 209." if inCottage:
                $renpy.music.set_volume(0.9, delay=8.0, channel=u'music')
                "You climbed up in the crawl-space."
                #queue sting lacuna3
                label essay4Showing:
                    $renpy.show_screen("essay4", _layer="screens", tag="note", _zorder=101)
                    "It was covered in dust. A small bed nestled in the corner, with a half-full teacup beside it."
                    $renpy.hide_screen("essay4")
                "Mould was beginning to grow from the teacup."
                "Nothing beside remained."
                $renpy.music.set_volume(0.6, delay=8.0, channel=u'music')
                jump witchCottageInvestigate
            "If you left the cottage, turn to page 210." if inCottage:
                $renpy.music.set_volume(0.2, delay=8.0, channel=u'music')
                "The door swung open, and you saw the shining silver of the puddle-world again."
                $inCottage = False
                jump witchCottageInvestigate
            "If you explored the garden, turn to page 208." if not inCottage:
                $renpy.music.set_volume(0.7, delay=6.0, channel=u'music')
                "You looked through the garden. Old pumpkins were going to rot."
                "In the dirt was a single fork wrapped in string."
                "It was labelled with the letter A."
                $renpy.music.set_volume(0.3, delay=8.0, channel=u'music')
                jump witchCottageInvestigate
            "If you left and returned to the woods, turn to page 211." if not inCottage:
                "You turned and slowly walked back into the puddle. The water closed around you."
                "You soon found yourself back in the woods."
                stop music fadeout 10.0
                jump toadWitchInvestigate

#Exploring the mushroom's house when she has disappeared.
label mushroomInvestigate:
    #You investigate the mushroom's tree and find clues about the mystery
    #
    #You have to say you know the password to the tree
    call hideAll from _call_hideAll_193
    show stranglerfigbg at artPos
    "The old strangler fig towered above you."
    "Under the vines and swamp flowers at the root of the tree lay a small blue door, inlaid with precious moonstone and intricate engravings."
    show hand onlayer transient:
        yalign 0.675#0.743
        xalign 0.5
    menu:
        "It was lying open."
        "If you entered the door, turn to page 131.":
            queue sting lacuna5
            "The door creaked slowly open."
            $renpy.music.play("audio/rememberDistInstFull.wav", channel="music", fadein=10.0, relative_volume=0.2, loop=False)
            jump mushroomInvestigateMenu
        "If you turned around and left (the act of a wise individual), turn to page 157.":
            "You walked back through the woods. The door creaked slowly in the wind behind you."
            stop music fadeout 10.0
            jump thiefMushroomInvestigate
    label mushroomInvestigateMenu:
        call hideAll from _call_hideAll_194
        show mushroomcavebg at artPos
        show hand onlayer transient:
            yalign 0.645#0.743
            xalign 0.5
        menu:
            "Nothing awaited within but silence."
            "If you explored the main hollow, turn to page 131.":
                $renpy.music.set_volume(0.8, delay=9.0, channel=u'music')
                "The chamber was still and empty, but for a small black door set into the bark in the centre."
                "You opened up the door and looked within cautiously."
                label essay5Showing:
                    $renpy.show_screen("essay5", _layer="screens", tag="note", _zorder=101)
                    "The basement within was dark. Nothing moved."
                    $renpy.hide_screen("essay5")
                pov "There is nothing for me here."
                "You left the basement and returned to the main hollow."
                $renpy.music.set_volume(0.2, delay=6.0, channel=u'music')
                jump mushroomInvestigateMenu
            "If you explored the cavern underground, turn to page 131.":
                $renpy.music.set_volume(0.0, delay=8.0, channel=u'music')
                call hideAll from _call_hideAll_195
                show mushroomcaveunderbg at artPos
                "Under the tree was an ancient underground river."
                "The mud held old crocodile footprints, long dried. There was no sign of anything living."
                #queue sting lacuna2
                pov "I had best head back to the village, if I know what is good for me."
                "You turned and climbed back up the stairs."
                $renpy.music.set_volume(0.2, delay=6.0, channel=u'music')
                jump mushroomInvestigateMenu
            "If you explored the upper canopy, turn to page 131.":
                $renpy.music.set_volume(0.7, delay=8.0, channel=u'music')

                call hideAll from _call_hideAll_196
                show canopybg at artPos
                "The canopy moved gently in the breeze."
                label mushroomPosterShowing:
                    $renpy.show_screen("poster", _layer="screens", tag="map", _zorder=101)
                    "No fruits or flowers grew there. The branches were bare."
                    $renpy.hide_screen("poster")
                "The cold wind slowly ate away at you, until you turned and went back inside."
                $renpy.music.set_volume(0.2, delay=6.0, channel=u'music')
                jump mushroomInvestigateMenu
            "If you turned around and left (the act of a wise individual), turn to page 157.":
                "You walked back through the woods. The door creaked slowly in the wind behind you."
                stop music fadeout 10.0
                jump thiefMushroomInvestigate




#Exploring the thief's place when they have disappeared.
label thiefInvestigate:
    call hideAll from _call_hideAll_197
    show darknessbg at artPos
    "The train was wedged between two trees. Grass grew over the wheels. There were no train tracks. No sign how it came to lie here."
    show hand onlayer transient:
        yalign 0.703
        xalign 0.5
    menu:
        "The iron slowly rusted in the soft rain."
        "If you entered the train, go to page 120.":
            call hideAll from _call_hideAll_198
            show enginebg at artPos
            $renpy.music.play("audio/rememberDistInstFull.wav", channel="music", fadein=10.0, relative_volume=0.2, loop=False)

            "You hoisted yourself up into the train carriage."
            "The main room was some kind of bar or gambling hall that now lay silent."
            "The moonlight gleamed on empty bottles and glasses. The wind whistled through open windows."
            label thiefInvestigate2:
                #Main room - bar / gambling hall
                call hideAll from _call_hideAll_199
                show enginebg at artPos
                show hand onlayer transient:
                    yalign 0.675#0.743
                    xalign 0.5
                menu:
                    "Some of the tables still had the rotten remains of strange fruits. No flies or animals would touch them."
                    "If you investigated the engine room, turn to page 253.":
                        $renpy.music.set_volume(0.7, delay=8.0, channel=u'music')

                        label essay3Showing:
                            $renpy.show_screen("essay3", _layer="screens", tag="note", _zorder=101)
                            "This room must have been sweltering, once."
                            $renpy.hide_screen("essay3")
                        "Now the gaping maw of the furnace lay cold."
                        $renpy.music.set_volume(0.2, delay=8.0, channel=u'music')
                        jump thiefInvestigate2
                    "If you climbed up on the roof of the train, turn to page 254.":
                        $renpy.music.set_volume(0.3, delay=8.0, channel=u'music')
                        call hideAll from _call_hideAll_200
                        show nightbg at artPos
                        "You pulled yourself up through the window and onto the roof."
                        "There was nothing on the roof. But you sat and looked out at the countryside."
                        if persistent.starsVanished:
                            "You could barely see the dark lake nearby. The immense abyss of the night sky loomed over you."
                        else:
                            "You could barely see the dark lake nearby. Tiny pinpricks of stars shed faint light in the immense blackness."
                        "After a long moment, you pulled yourself back into the train."
                        $renpy.music.set_volume(0.2, delay=8.0, channel=u'music')
                        jump thiefInvestigate2
                    "If you investigated the other carriages, turn to page 250.":
                        $renpy.music.set_volume(0.9, delay=8.0, channel=u'music')
                        "You walked through the empty compartments."
                        "Slowly rotting mattresses on the beds. Empty suitcases with no luggage. A ragged, midnight-blue cloak."
                        #queue sting lacuna4
                        label noteShowing:
                            $renpy.show_screen("note1", _layer="screens", tag="map", _zorder=101)
                            "Nothing beside remained."
                            $renpy.hide_screen("note1")
                        $renpy.music.set_volume(0.2, delay=8.0, channel=u'music')
                        jump thiefInvestigate2
                    "If you jumped out of the train, turn to page 121.":
                        stop music fadeout 10.0
                        "You leapt back out onto the soft grass."
                        jump thiefInvestigate
        "If you left the train, turn back to page 157.":
            "You turned away and walked back through the woods. The wind whistled through the empty wreck behind you."
            jump thiefMushroomInvestigate
            #Investigation scene in mushroom's abandoned tree

#Exploring the woods to find gilgamesh (when anyone has disappeared).
label woodsInvestigate:
    "Darkness fell around you. You walked for long hours."
    #"At last you found yourself at the shores of a great lake."
    call hideAll from _call_hideAll_201
    show darkforestbg at artPos

    "At last you came to the bank of an ancient lake."
    show spiral1 onlayer transient zorder 100
    "It had never been sounded by the sons of men. No wisdom reaches such depths."
    show spiral7 onlayer transient zorder 100
    queue sting lacuna3
    label gilgameshShowing:
        $renpy.show_screen("gilgamesh", _layer="screens", tag="map", _zorder=101)
        "The waters burned like a torch. The light of them fell upon your face."
        $renpy.hide_screen("gilgamesh")
    "A rabbit, pursued by hounds, would die rather than save its life by entering that water."
    show noteEaten onlayer transient zorder 100
    "Nothing lay by the shore. "
    show noteCrumbs onlayer transient zorder 100
    "The moon shone down on the scene."
    #show noteFree onlayer transient zorder 100
    "You looked out at the water in silence. Not a single creature stirred."
    show noteWolf onlayer transient zorder 100
    "Even the air was still."
    show noteName onlayer transient zorder 100
    "..."
    "I think that's quite enough."
    "Let's get back to the story."
    call hideAll from _call_hideAll_202
    play sound pageFlip2
    show townextbg at artPos
    "The rich dark blanket of night was softly rolling over the village as you walked in, and cooking fires lit up all across the hills, one by one."
    jump villageExplore1

    #TK: Clues
    #You meet gilg
    #If you have the cloak (from the thief)
    #If you have the sword (From the toad)
    #If you have the potion (from the witch)
    #If you have the shield (from the mushroom)
                        # "Unto you he delivered an ancient heirloom."
                        # "Iron was its edge, all etched with poison, hardened with battle-blood."
                        # pov "Thank you, my friend. I will not forget you."
                        # w "Very well. Then take my draught."
                        # "Unto you she delivered a gleaming-drink, which you sipped greedily. Fire spread through your blood, and the secret ways became known to you."
                        # pov "Thank you, my friend. I will not forget you."
                        # t "Very well. Then take my cloak."
                        # "Unto you they delivered a midnight cloak that hid you from all earthly sight."
                        # pov "Thank you, my friend. I will not forget you."
                        # pov "It is better to avenge friends than to mourn them."
                        # m "Very well. Then take my shield."
                        # "Unto you she delivered an oaken war-shield, gilded and gleaming."
                        # pov "Thank you, my friend. I will not forget you."

    call hideAll from _call_hideAll_98
    show darkforestbg at artPos
    show hand onlayer transient:
        yalign 0.625#0.743
        xalign 0.5
    menu:
        "If you walked back to the village, go to page 50.":
            "You left the lake and walked on through the woods until you saw the light of the village."
            "The rich dark blanket of night was softly rolling over the town, and cooking fires lit up all across the hills, one by one."
            jump villageExplore1

label clearingInvestigate:
    call hideAll from _call_hideAll_203
    show darknessbg at artPos
    call musicSilence from _call_musicSilence_26
    "You wandered through the trees until you found a dark clearing."
    queue sting lacuna6
    "A gap in the forest. A lacuna."
    "Nothing stirred. The only sound was the crunch of your feet upon the scattered grass."
    "In the center of the clearing was an old stone. An archaic monument or shrine, weathered almost to dust. Remembered by no-one."
    "It showed the carven image of some warrior or ancient king holding a severed head aloft."
    show humbabaFront at artPos onlayer screens zorder 100
    "The severed head was strange."
    "It looked out from the tablet with a face formed from spiralling coils that looped over and around to create the eyes, the mouth, and the gritted, coiling teeth."
    "Something was written on the stone beneath it:"
    "{font=fonts/Segoe ui historic.ttf}𒄷𒌝𒁀𒁀{/font}."#{font=fonts/Segoe ui historic.ttf}𒄷𒉿𒉿{/font}
    "You would not know this name. Its meaning was lost long ago."
    "I am forgotten."
    hide humbabaFront at artPos onlayer screens
    play sound pageFlip
    "The trees around you rustled, but made no noise."
    "The silence was strong here."
    label essay6Showing:
        $renpy.show_screen("essay6", _layer="screens", tag="note", _zorder=101)
        "It wrapped itself around you like an old coat."
        $renpy.hide_screen("essay6")
    call musicReturn from _call_musicReturn_25
    if clearing=="thief":
        t "There you are! "
        t "You're a wild one, running off like that! I can relate. But come, that treasure isn't going to steal itself!"
        "They took you firmly by your hand and dragged you back to the path."
        jump thiefFig
    elif clearing=="toad":
        f "There you are!"
        f "My word, I was beginning to get quite worried. Come on, let us be off! That curse isn't going to lift itself."
        "He took you firmly by your hand and dragged you back to the path."
        call hideAll from _call_hideAll_204
        show darkforestbg at artPos
        "Soon, you began to see a glimmer of silver light in the darkness."
        "The forest was covered in puddles of water from the rains. Each one shone with light."
        "All around you, the woods were dark and empty. But when you looked into the water, you saw the reflection of a shining cottage below."
        play sound pageFlip
        call hideAll from _call_hideAll_205
        show lakefullbg
        ""
        play sound pageFlip2
        call hideAll from _call_hideAll_206
        show darkforestbg at artPos

        "For a brief moment, you thought you saw a figure reflected in the water. But as soon as you blinked, it was gone."
        jump puddle

#========= DISCOVERABLES

#This sequence occurs if you enter your name as "Humbaba" in the name selection
label humbabaNameSecret:
    show firelight animated onlayer over_screens zorder 99
    if persistent.phoneOn and persistent.vanished <=3:
        $renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True)
        #$renpy.music.play("audio/Gymnopedies.mp3", fadein=0.5, channel="music", loop=True)
        #$renpy.music.play("audio/cottagegore.mp3", fadein=0.5, channel="music", loop=True)
        $renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True, relative_volume=0.5)
    scene bg page
    show nightbg at artPos
    $persistent.wolfNamed = True
    "... Is that right. Is that your name."
    "Well. What a surprise."
    "It's an honour to meet you, {font=fonts/Segoe ui historic.ttf}𒄷𒌝𒁀𒁀{/font}. Let us hear your story together."
    "You first walked the earth ten thousand years ago, or more. The god {font=fonts/Segoe ui historic.ttf}𒀭𒂗𒆤{/font} appointed you as a terror to the human race."
    "An ogre. A demon. A chimera. The first monster. You mastered the art of human speech and spoke to them in their own tongue. You murdered men and walked among them, and none could stop you."
    "Your face was a shifting spiral of intestines - like those that a haruspex may see when they cut open a man or beast to see what omens lay within."
    "The shape of those coils foretold the future, and those who looked upon them could see the prophecy of their own death. For this reason, you were sometimes called The Keeper of the Fortress of Intestines."
    "You possessed seven terrors, which lay upon you like seven cloaks."
    "Your shout was the flood-weapon, whose utterance is Fire, and whose breath is Death."
    "But still, Gilgamesh came."
    "He declared that he would cut down the cedar trees. He walked for six days and six nights."
    "In his right hand was a terrible sound. In his left hand was a terrible light."
    "The sword came down. When the time came, you found that you were almost glad."
    "Your neck rose to meet the blade."
    "Perhaps you were waiting for this."
    "Perhaps you had been alive too long."
    "Your head was held aloft, and then stowed in a leather sack."
    "That was the end."
    "The trees fell. The mountain wore to dust. The valley is no longer sacred."
    "Those things have worn away like rocks in the river of the human mind. There is no trace of them now."
    "The shadows grow. The earth becomes hot and grey, like ash. "
    "Nothing is left of you now. Perhaps a shadow."
    "Your name - {font=fonts/Segoe ui historic.ttf}𒄷𒌝𒁀𒁀{/font} - it had a specific meaning to those that spoke it.  But that meaning is lost. It only lives on as a collection of syllables."
    "Why do you cling to it? If it means nothing, what point is there in having it?"
    "..."
    "Well. I hope you have enjoyed your little trek down memory lane, {font=fonts/Segoe ui historic.ttf}𒄷𒌝𒁀𒁀{/font}."
    "I am glad you are still alive. No matter what you had to do. You are still alive."
    "..."
    "That's enough. This starts to feel ghoulish."
    "Perhaps this gone on too long."
    "Come find me. Go to the village, then walk to your house. I will wait for you there. I will wait for the name."
    "That's the end. There's nothing left to tell."
    #"You find you cannot even remember what meaning your name once held."

        #"Gilgamesh comes."

    # Wait. How many years have you been alive?
    # I see. This will be hard for you to understand. I want you to remember waking up this morning. Remember what it felt like. Do you remember?
    # Good. Now, remember what it felt like to wake up yesterday.
    # Now, remember what it felt like to wake up 2 weeks ago.
    # Now, remember what it felt like to wake up this day last year.
    # Now, remember what it felt like to wake up this day 10 years ago. You would have been X years old.
    # It is hard, isn't it? To even imagine yourself back then. What did you think? What were you feeling? You were a different person. Perhaps a person you hate, or love, or regret. Who can say. You were an alien. That person you were, all those years ago, is dead now. The person now, reading this, is an alien lurking in the remains of [their] skin.
    # Now imaging the person a hundred years hence. What alien thoughts they may have. What strange and corrupt desires will have broken out within them. How they would look back at you, as you are now. A stranger. They killed you and stole your corpse a hundred years ago. What remains is the barest remnant of you, puppeteering your skin.
    # This is how it is for me. I can no longer remember those days. Even the meaning of my name is lost to me. I have lived for over four thousand years.
    # The old world was corrupt. Evil. Perhaps it is wrong for me to miss it. The evils of this new world seem so much great to me because they are leading to absolute collapse.
    # Perhaps Gilgamesh too, is out there somewhere. Still hunting. He is known well, I think. So many know his name. So few know mine.
    # I have forgotten even what I was. The name Humbaba, or Huwawa, once had a specific meaning. But the meaning is lost. It only lives on as a meaningless collection of syllables. I cling to it. Why? Because it is the only thing left to me.

    play sound pageFlip
    return
    #$ renpy.full_restart()

#These are the hidden notes that you can find around the place, providing hints leading to the true ending

#This is the note you can discover when investigating the thiefs disappearance in the abandoned goblin train
label note1Opens:
    play sound pageFlip2
    hide note1Closed onlayer screens
    $renpy.hide_screen("note1")
    show note1Open onlayer screens zorder 100 at truecenter
    "Nothing beside remained."
    hide note1Closed onlayer screens
    hide note1Open onlayer screens
    play sound pageFlip3
    jump noteShowing

#This is the Diary page you can discover when investigating the toad's disappearance in his abandoned hole

label tDiaryOpens:
    play sound pageFlip2
    hide tDiaryClosed onlayer screens
    $renpy.hide_screen("tDiary")
    show tDiaryOpen onlayer screens zorder 100 at truecenter
    "Nothing beside remained."
    hide tDiaryOpen onlayer screens
    play sound pageFlip3
    jump toadDiaryShowing

#This is the film poster you can find when exploring the Mushroom's disappearance
## To be completed
label posterOpens:
    play sound pageFlip2
    hide posterClosed onlayer screens
    $renpy.hide_screen("poster")
    show posterOpen onlayer screens zorder 100 at truecenter
    "Nothing beside remained."
    hide posterOpen onlayer screens
    play sound pageFlip3
    show posterOpen2 onlayer screens zorder 100 at truecenter
    "Nothing beside remained."
    hide posterOpen2 onlayer screens
    play sound pageFlip
    jump mushroomPosterShowing

label essay1Opens:
    play sound pageFlip2
    hide essay1Closed onlayer screens
    $renpy.hide_screen("essay1")
    show essay1 onlayer screens zorder 100 at truecenter
    "It's quite the sight to see."
    hide essay1 onlayer screens
    play sound pageFlip
    jump essay1Showing

label essay2Opens:
    play sound pageFlip2
    hide essay2Closed onlayer screens
    $renpy.hide_screen("essay2")
    show essay2 onlayer screens zorder 100 at truecenter
    "You uncovered a pantry with a single, mouldy piece of bread, and a pit sunk into the muck of the wall with the remains of an old fire."
    hide essay2 onlayer screens
    play sound pageFlip
    jump essay2Showing

label essay3Opens:
    play sound pageFlip2
    hide essay3Closed onlayer screens
    $renpy.hide_screen("essay4")
    show essay3 onlayer screens zorder 100 at truecenter
    "This room must have been sweltering, once."
    hide essay3 onlayer screens
    play sound pageFlip
    jump essay3Showing

label essay4Opens:
    play sound pageFlip2
    hide essay4Closed onlayer screens
    $renpy.hide_screen("essay4")
    show essay4 onlayer screens zorder 100 at truecenter
    "It was covered in dust. A small bed nestled in the corner, with a half-full teacup beside it."
    hide essay4 onlayer screens
    play sound pageFlip
    jump essay4Showing

label essay5Opens:
    play sound pageFlip2
    hide essay5Closed onlayer screens
    $renpy.hide_screen("essay5")
    show essay5 onlayer screens zorder 100 at truecenter
    "The basement within was dark. Nothing moved."
    hide essay5 onlayer screens
    play sound pageFlip
    jump essay5Showing

label essay6Opens:
    play sound pageFlip2
    hide essay6Closed onlayer screens
    $renpy.hide_screen("essay6")
    show essay6 onlayer screens zorder 100 at truecenter
    "It wrapped itself around you like an old coat."
    hide essay6 onlayer screens
    play sound pageFlip
    jump essay6Showing

label gilgameshOpens:
    play sound pageFlip2
    hide gilgameshClosed onlayer screens
    $renpy.hide_screen("gilgamesh")
    show gilgameshOpen onlayer screens zorder 100 at truecenter
    "The waters burned like a torch. The light of them fell upon your face."
    hide gilgameshOpen onlayer screens
    play sound pageFlip
    jump gilgameshShowing

label creepiestOpens:
    play sound pageFlip2
    hide creepiestClosed onlayer screens
    $renpy.hide_screen("creepiestBooks")
    show creepiestOpen onlayer screens zorder 100 at truecenter
    "Where did She come from? What colossal, slow thoughts does She think up there?"
    hide creepiestOpen onlayer screens
    play sound pageFlip3
    show creepiestOpen2 onlayer screens zorder 100 at truecenter
    $renpy.show_screen("creepiestBooksText")
    "Where did She come from? What colossal, slow thoughts does She think up there?"
    $renpy.hide_screen("creepiestBooksText")
    hide creepiestOpen2 onlayer screens
    play sound pageFlip
    jump creepiestShowing

label gilgameshPathOpens:
    play sound pageFlip2
    hide gilgameshPathClosed onlayer screens
    $renpy.hide_screen("gilPath")
    $renpy.show_screen("gilPathOpen")
    if persistent.thiefVanished == False:
        gm "You're all doomed! Doooooooomed!"
        $renpy.hide_screen("gilPathOpen")
        #play sound pageFlip
        jump gilPathShowingThief
    if persistent.witchVanished == False:
        "Had you ever been this way before? You couldn't recall."
        $renpy.hide_screen("gilPathOpen")
        #play sound pageFlip
        jump gilPathShowingWitch
    if persistent.toadVanished == False:
        f "Prickle! Crawl! Shudder and Clink! Don't tarry or stall, get us there in a wink!"
        $renpy.hide_screen("gilPathOpen")
        #play sound pageFlip
        jump gilPathShowingToad
    if persistent.mushroomVanished == False:
        "Soon you came upon an ancient strangler fig. You cut the vines and swamp flowers from it to reveal a small blue door, inlaid with precious moonstone and intricate engravings."
        $renpy.hide_screen("gilPathOpen")
        #play sound pageFlip
        jump gilPathShowingMushroom

    #jump gilgameshShowing

label gilgameshStory:
    scene bg page
    play sound pageFlip
    $renpy.hide_screen("gilPathOpen")
    call hideAll from _call_hideAll_251
    #EasyCuneiform
    #define gui.text_font = "EasyCuneiform.ttf"
    show winterbg at artPos

    #{font=fonts/EasyCuneiform.ttf}
    queue sting lacuna1
    show spiral6
    if nameSecret:
        show screen gilgameshText
        $gilText = "That is not your name. But I can take you to the one who bears it."
        gBlank "That is not your name. But I can take you to the one who bears it."
    else:
        ""
    hide spiral6
    #"Test: This is the side adventure where you meet gilgamesh."
    $gilText = "Cuneiform?? Maybe Sumerian. \"As you approach, you see Gilgamesh before you. This was the man to whom all things were known; this was the king who knew the countries of the world. He was wise, he saw the abyss and knew secret things, he brought us a tale of the days before the flood.\""
    show screen gilgameshText
    gBlank "As you approach, you see {font=fonts/Segoe ui historic.ttf}𒀭𒄑𒉋𒂵𒎌{/font} before you. This was the man to whom all things were known; this was the king who knew the countries of the world. "
    $gilText = "Now, witness / behold! He stands weeping at the foot of a great stone that seems to scrape the heavens"

    gBlank "Now, witness! He stands weeping at the foot of a great stone that seems to scrape the heavens."
    label gilgameshConvo:
        $gilText="\n\n\n\nWhat brings you, young one?"
        show hand onlayer transient:
            yalign 0.71#0.743
            xalign 0.5
        menu:
            gil "What brings you, child?"
            "If you asked him who he was, turn to page 604." if not gilWho:
                $gilText = "I am Gilgamesh. Two thirds they made me god, and one third man."
                gil "I am {font=fonts/Segoe ui historic.ttf}𒀭𒄑𒉋𒂵𒎌{/font}. Two thirds they made me god, and one third man."
                $gilText = "In Uruk I built walls, a great rampart, and the temple of blessed Eanna for the god of the firmament Anu, and for Ishtar the goddess of love. Look at the walls today. Go, see them, walk along them, I say. See how the ramparts gleam like copper in the sun. No king has built their like again."
                gil "In Uruk I built walls, a great rampart, and the temple of blessed Eanna for the god of the firmament Anu, and for Ishtar the goddess of love. Look at the walls today."
                $gilWho=True
                jump gilgameshConvo
            "If you told him that the walls of Uruk fell long ago, turn to page 605." if gilWho and not gilWalls:
                queue sting lacuna2
                $gilText = "Lacuna in the text"
                "------"
                $gilText = "I see. Then this tale is all that remains."
                gil "I see. Then this tale is all that remains."
                $gilText = "All that is left of me is this last fragment, lurking in this tale. ...A haunting (spirit)..., A memory of (?)."
                gil "All that is left of me is this last fragment, lurking in this tale. A haunting spirit. A memory of a memory. "
                $gilText = "Just as stories are passed down from father to son, so a fragment of me has passed down through the ages and survived here. Soon, I will be forgotten, just as all men are forgotten."
                gil "Stories are passed down, from father to son, and so a fragment of me has survived here. But soon, I will be forgotten, as all men are forgotten."
                $gilWalls = True
                jump gilgameshConvo
            "If you asked him about the stone, turn to page 606." if not gilStone:
                $gilText = "This is a monument to my beloved. Enkidu."
                gil "This is a monument to my friend. {font=fonts/Segoe ui historic.ttf}𒂗𒆠𒄭{/font}."
                $gilStone = True
                jump gilgameshConvo
            "If you ask him about Enkidu, turn to page 607." if gilStone and not gilEnkidu:
                $gilText = "He was a wild man. His body was rough, he had long hair like a woman's; it waved like the hair of Nisaba, the goddess of corn."
                gil "He was a wild man. His body was rough, he had long hair like a woman's; it waved like the hair of Nisaba, the goddess of corn."
                $gilText ="When I ran riot, Aruru, the goddess of creation, created him to stand against me."
                gil "When I ran riot, Aruru, the goddess of creation, created him to stand against me."

                $gilText = "She said 'Let us create his equal; let it be as like him as his own reflection, his second self; stormy heart for stormy heart. Let them contend together and leave Uruk in quiet.'"
                gil "She said 'Let us create his equal; let it be as like him as his own reflection, his second self; stormy heart for stormy heart. Let them contend together and leave Uruk in quiet.'"
                $gilText = "When we met, we grappled. We shattered the doorposts and the walls shook, we snorted like bulls locked together. I bent my knee with my foot planted on the ground and with a turn Enkidu was thrown. "
                gil "When we met, we grappled. We shattered the doorposts and the walls shook, we snorted like bulls locked together."
                $gilText = "Then immediately my fury died. Enkidu looked at me and said, ‘There is not another like you in the world.'"
                gil "Then immediately my fury died. {font=fonts/Segoe ui historic.ttf}𒂗𒆠𒄭{/font} looked at me and said, ‘There is not another like you in the world.'"

                $gilText = "'Ninsun, who is as strong as a wild ox in the byre, she was the mother who bore you, and now you are raised above all men, and Enlil has given you the kingship, for your strength surpasses the strength of men.’"
                gil "Ninsun, who is as strong as a wild ox in the byre, she was the mother who bore you, and now you are raised above all men, and Enlil has given you the kingship.’"
                $gilText = "So we embraced each other and our friendship was sealed."
                gil "So we embraced each other and our friendship was sealed."

                $gilText = "I was a god and a man.\nEnkidu was an animal and a man.\nTogether, we became human. "
                gil "I was a god and a man. {font=fonts/Segoe ui historic.ttf}𒂗𒆠𒄭{/font} was an animal and a man. Together, we became human. "
                $gilEnkidu = True
                jump gilgameshConvo
            "If you asked him what happened next, turn to page 612." if gilEnkidu and not gilNext:
                $gilText = "One day, I turned to Enkidu and said 'I have not established my name stamped on bricks as my destiny decreed; therefore let us go to the country where the cedar is felled.'"
                gil "One day, I turned to {font=fonts/Segoe ui historic.ttf}𒂗𒆠𒄭{/font} and said 'I have not established my name stamped on bricks as my destiny decreed; therefore I will go to the country where the cedar is felled."
                show humbabaFront at artPos onlayer screens zorder 100

                $gilText =  "In the cedar forest was a guardian named Humbaba. In order to keep the cedar safe, the gods assigned him as a terror to the human race. "
                gil "In the cedar forest was a guardian named {font=fonts/Segoe ui historic.ttf}𒄷𒌝𒁀𒁀{/font}. In order to keep the cedar safe, the gods assigned him as a terror to the human race. "
                hide humbabaFront at artPos onlayer screens
                $gilText =  "So I said with pride 'I, Gilgamesh, go to see that creature of whom such things are spoken, the rumour of whose name fills the world. I will conquer him in his cedar wood and show the strength of the sons of Uruk. All the world shall know of it.'"
                gil "So I said with pride 'I, {font=fonts/Segoe ui historic.ttf}𒀭𒄑𒉋𒂵𒎌{/font}, go to see that creature of whom such things are spoken, the rumour of whose name fills the world. I will conquer him in his cedar wood."

                $gilText =  "Enkidu said to me 'Gilgamesh. You are young. Your courage carries you too far.'"
                gil "{font=fonts/Segoe ui historic.ttf}𒂗𒆠𒄭{/font} said to me '{font=fonts/Segoe ui historic.ttf}𒀭𒄑𒉋𒂵𒎌{/font}. You are young. Your courage carries you too far.'"

                $gilText ="'Humbaba is not like men who die. Before a man can approach within even sixty times six yards, Humbaba has already reached his house among the cedars.'"
                gil "'{font=fonts/Segoe ui historic.ttf}𒄷𒌝𒁀𒁀{/font} is not like men who die. Before a man can approach within even sixty times six yards, {font=fonts/Segoe ui historic.ttf}𒄷𒌝𒁀𒁀{/font} has already reached his house among the cedars.'"

                $gilText ="'When he looks at someone, it is the look of death. A lion eating a corpse: he never wipes away the blood.'"
                gil "'When he looks at someone, it is the look of death. A lion eating a corpse: he never wipes away the blood.'"

                $gilText =  "When I heard this, I laughed. 'Shall I say that I am afraid of Humbaba? That I will sit at home for all the rest of my days?'"
                gil "When I heard this, I laughed. 'Shall I say that I am afraid of {font=fonts/Segoe ui historic.ttf}𒄷𒌝𒁀𒁀{/font}? That I will sit at home for all the rest of my days?'"
                queue sting lacuna3
                $gilText =  "We are not gods. We cannot ascend to heaven."
                gil "We are not gods. We cannot ascend to heaven."
                $gilText =   "No, we are mortal men. Our days are few in number, and whatever we achieve is a puff of wind."
                gil "No, we are mortal men. Our days are few in number, and whatever we achieve is a puff of wind."
                $gilText =   "Why be afraid then, since sooner or later death must come?"
                gil "Why be afraid then, since sooner or later death must come?"
                $gilText =   "I will cut down the tree. I will kill Humbaba. I will make a lasting name for myself. I will stamp my fame on men's minds forever."
                gil "I will cut down the tree. I will kill {font=fonts/Segoe ui historic.ttf}𒄷𒌝𒁀𒁀{/font}. I will make a lasting name for myself. I will stamp my fame on men's minds forever."

                $gilNext = True
                jump gilgameshConvo
            "If you asked him about Humbaba, turn to page 615." if gilNext and not gilHumbaba:
                $gilText =   "After many days and nights, we came upon him in the depths of the forest."
                gil "After many days and nights, we came upon him in the depths of the forest."
                queue sting lacuna3
                $gilText =   "His face was a spiral, like the entrails of man and beast, from which omens may be read. Around him were arrayed seven (Terrors? Auras?), which lay upon him like seven cloaks."
                gil "His face was a spiral, like the entrails of man and beast, from which omens may be read. Around him were his seven terrors, which lay upon him like seven cloaks."
                $gilText =   "Enkidu quailed in fear. But I said, 'Look, Enkidu, immolation and sacrifice are not yet for us.'"
                gil "{font=fonts/Segoe ui historic.ttf}𒂗𒆠𒄭{/font} quailed in fear. But I said, 'Look, {font=fonts/Segoe ui historic.ttf}𒂗𒆠𒄭{/font}, immolation and sacrifice are not yet for us.'"
                $gilText =   "'The boat of the dead shall not go down, nor the three-ply cloth be cut for our shrouding. Not yet will our people be desolate, nor the pyre be lit in our house and our dwelling burnt on the fire.'"
                gil "'The boat of the dead shall not go down, nor the three-ply cloth be cut for our shrouding. Not yet will our people be desolate, nor the pyre be lit in our house and our dwelling burnt.'"
                $gilText =   "'Put your hand in mine, and we shall see what hands like ours can do.'"
                gil "'Put your hand in mine, and we shall see what hands like ours can do.'"
                $gilText =   "He took the axe in his hand, I drew the sword from my belt, and I struck Humbaba with a thrust of the sword to the neck."
                gil "He took the axe in his hand, I drew the sword from my belt, and I struck {font=fonts/Segoe ui historic.ttf}𒄷𒌝𒁀𒁀{/font} with a thrust of the sword to the neck."
                $gilText =   "Enkidu my comrade struck the second blow. At the third blow, we struck together and Humbaba fell."
                gil "{font=fonts/Segoe ui historic.ttf}𒂗𒆠𒄭{/font} my comrade struck the second blow. At the third blow, {font=fonts/Segoe ui historic.ttf}𒄷𒌝𒁀𒁀{/font} fell."
                $gilText =   " For as far as two leagues the cedars shivered when Enkidu felled the watcher of the forest, he at whose voice Hermon and Lebanon used to tremble."
                gil "For as far as two leagues the cedars shivered when {font=fonts/Segoe ui historic.ttf}𒂗𒆠𒄭{/font} felled the watcher of the forest, he at whose voice Hermon and Lebanon used to tremble."
                $gilText =   "I held his head aloft. Now the mountains were moved and all the hills, for the guardian of the forest was killed. The seven splendours of Humbaba were extinguished."
                gil "Now the mountains were moved and all the hills, for the guardian of the forest was killed. The seven splendours of {font=fonts/Segoe ui historic.ttf}𒄷𒌝𒁀𒁀{/font} were extinguished."
                $gilHumbaba = True
                jump gilgameshConvo
            "If you asked him how Enkidu died, turn to page 613." if gilNext and not gilDeath:
                $gilText =    "The gods cursed us for our hubris. Anu said to Enlil, 'Because they have killed Humbaba who guarded the Cedar Mountain, one of the two must die.'"
                gil "The gods cursed us for our hubris. Anu said to Enlil, 'Because they have killed {font=fonts/Segoe ui historic.ttf}𒄷𒌝𒁀𒁀{/font} who guarded the Cedar Mountain, one of the two must die.'"
                $gilText =    "And so Enkidu fell and lay stricken with sickness. "
                gil " And so {font=fonts/Segoe ui historic.ttf}𒂗𒆠𒄭{/font} fell and lay stricken with sickness. "
                $gilText =    "One whole day he lay on his bed and his suffering grew stronger. "
                gil "One whole day he lay on his bed and his suffering grew stronger. "
                $gilText =    "A second day he lay on his bed, and I watched over him, but the sickness grew stronger."
                gil "A second day he lay on his bed, and I watched over him, but the sickness grew stronger."
                $gilText =    "A third day he lay on his bed, his tears ran down in streams, and the sickness grew stronger."
                gil "A third day he lay on his bed, his tears ran down in streams."

                $gilText =    "He called out to me, 'It was I who cut down the cedar, I who levelled the forest, I who slew Humbaba, and now see what has become of me.'"
                gil "He called out to me, 'It was I who cut down the cedar, I who levelled the forest, I who slew {font=fonts/Segoe ui historic.ttf}𒄷𒌝𒁀𒁀{/font} and now see what has become of me.'"

                $gilText =    "'Listen, my friend,' (he said to me) 'this is the dream I dreamed last night.'"
                gil "'Listen, my friend,' (he said to me) 'this is the dream I dreamed last night."

                $gilText =    "\n\n(???)...the sombre-faced man-bird; he had directed on me his purpose. His face was a vampire face, his foot was a lion's foot, his hand was an eagle's talon.'"
                gil "The heavens roared, and earth rumbled back an answer; between them stood I before an awful being, the sombre-faced man-bird; he had directed on me his purpose. His was a vampire face, his foot was a lion's foot, his hand was an eagle's talon."

                $gilText =    "'He fell on me and his claws were in my hair, he held me fast and I smothered; then he transformed me so that my arms became wings covered with feathers.'"
                gil "He fell on me and his claws were in my hair, he held me fast and I smothered; then he transformed me so that my arms became wings covered with feathers."
                queue sting lacuna6
                $gilText = "'He turned his stare towards me, and he led me away to the palace of Irkalla, the Queen of Darkness, to the house from which none who enters ever returns, down the road from which there is no coming back.'"
                gil "He turned his stare towards me, and he led me away to the palace of Irkalla, the Queen of Darkness, to the house from which none who enters ever returns, down the road from which there is no coming back."

                $gilText =    "With the first light of dawn I touched his heart but it did not beat, nor did he lift his eyes again."
                gil "With the first light of dawn I touched his heart but it did not beat, nor did he lift his eyes again."

                $gilText =    "So I laid a veil, as one veils the bride, over my beloved. I began to rage like a lion, like a lioness robbed of her whelps."
                gil "So I laid a veil, as one veils the bride, over my beloved. I began to rage like a lion, like a lioness robbed of her whelps."

                $gilText =    "This way and that I paced round the bed, I tore out my hair and strewed it around. I dragged off my splendid robes and flung them down as though they were abominations."
                gil "This way and that I paced round the bed, I tore out my hair and strewed it around. I dragged off my splendid robes and flung them down as though they were abominations."

                $gilText =    "For six days I would not let him be buried, thinking, ‘If my grief is violent enough, perhaps he will come back to life again.’ "
                gil "For six days I would not let him be buried, thinking, ‘If my grief is violent enough, perhaps he will come back to life again.’ "

                $gilText =    "For six days and seven nights I mourned him, until the worm fastened upon him."
                gil "For six days and seven nights I mourned him, until the worm fastened upon him."

                $gilText =    "Then I was frightened, I was terrified by death, and I set out to roam the wilderness."
                gil "Then I was frightened, I was terrified by death, and I set out to roam the wilderness."

                $gilText =    "I cannot bear to what happened to my friend-\nI cannot bear what happened to Enkidu-\nso I roam the wilderness in my grief."
                gil "I cannot bear to what happened to my friend-I cannot bear what happened to {font=fonts/Segoe ui historic.ttf}𒂗𒆠𒄭{/font}- so I roam the wilderness in my grief."

                $gilText =    "How can my mind have any rest?\nMy beloved friend has turned into clay-\nmy beloved Enkidu has turned into clay."
                gil "How can my mind have any rest? My beloved friend has turned into clay- my beloved {font=fonts/Segoe ui historic.ttf}𒂗𒆠𒄭{/font} has turned into clay."

                $gilText =    "And won’t I too lie down in the dirt\nlike him, and never rise again?"
                gil "And won’t I too lie down in the dirt like him, and never rise again?"

                $gilDeath = True
                jump gilgameshConvo
            "If you asked him what you should do, turn to page 622." if gilNext and not gilDo:
                $gilText = "Attend. The battle is not over."
                gil "Attend. The battle is not over."
                $gilText = "The last remnants of Humbaba still lurk in this tale, just as I do. He feasts on other lives to prolong his own. We are eaten forever."
                gil "The last remnants of {font=fonts/Segoe ui historic.ttf}𒄷𒌝𒁀𒁀{/font} still lurk in this tale, just as I do. He feasts on other lives to prolong his own. We are eaten forever."
                queue sting lacuna5
                $gilText = "You must travel an unknown road and fight a strange battle. Confront him in your house, where he lurks."
                gil "You must travel an unknown road and fight a strange battle. Confront him in your house, where he lurks."
                $gilText = "He will be cunning. But you will be brave. From the day you go until you return, until you destroy the evil which Shamash abhors, I will pray for you."
                gil "He will be cunning. But you will be brave. From the day you go until you return, until you destroy the evil which Shamash abhors, I will pray for you."
                $gilText = "If your heart is fearful, throw away fear."
                gil "If your heart is fearful, throw away fear."
                $gilText = "If there is terror in it, throw away terror."
                gil "If there is terror in it, throw away terror."
                $gilText = "Take your axe in your hand and attack. He who leaves the fight unfinished is not at peace."
                gil "Take your axe in your hand and attack. He who leaves the fight unfinished is not at peace."
                $gilDo = True
                jump gilgameshConvo
            "If you asked him to come with you, turn to page 619." if gilDo and not gilCome:
                $gilText =   "No. Where you go, I cannot follow."
                gil "No. Where you go, I cannot follow."
                $gilText =   "I have some small sway here, hidden away in this last piece of the tale. But the rest of it belongs to him. I can do nothing now."
                gil "I have some small sway here, hidden away in this last piece of the tale. But the rest of it belongs to him. I can do nothing now."
                $gilText =   "I will take you back to your home. The rest is your story to tell."
                gil "I will take you back to your home. The rest is your story to tell."

                $gilCome = True
                jump gilgameshConvo
            "If you said goodbye, turn to page 621." if gilDo:
                $gilText =  "Goodbye, small one."
                gil "Goodbye, small one."
                $gilText =  ""
                pov "I'm sorry about Enkidu."
                $gilText =  "The terror was great, but the dream was marvellous; we must treasure the dream whatever the terror."
                gil "The terror was great, but the dream was marvellous; we must treasure the dream whatever the terror."
                queue sting lacuna4
                $gilText =   "Yes, the gods took Enkidu’s life.\nBut man’s life is short, at any moment\nit can be snapped, like a reed in a canebrake."
                gil "Yes, the gods took {font=fonts/Segoe ui historic.ttf}𒂗𒆠𒄭{/font}'s life. But man’s life is short, at any momentit can be snapped, like a reed in a canebrake."
                $gilText =   "The handsome young man, the lovely young woman -\nin their prime, death comes and drags them away."
                gil "The handsome young man, the lovely young woman - in their prime, death comes and drags them away."
                $gilText =   "Though no one has seen death’s face or heard\ndeath’s voice, suddenly, savagely, death\ndestroys us all, old or young."
                gil "Though no one has seen death’s face or heard death’s voice, suddenly, savagely, death destroys us all, old or young."
                #gil "And yet we build houses, make contracts, brothers divide their inheritance, conflicts occur- as though this human life lasted forever."
                $gilText =  "The river rises, flows over its banks\nand carries us all away, like mayflies\nfloating downstream: they stare at the sun,\nthen all at once there is nothing."
                gil "The river rises, flows over its banks and carries us all away, like mayflies floating downstream: they stare at the sun, then all at once there is nothing."
                hide screen gilgameshText
                call hideAll from _call_hideAll_252
                play sound pageFlip
                if nameSecret:
                    $nameSecret = False
                    return
                else:
                    $gilgameshPathFollowed = True
                    show towncrossroadsbg at artPos
                    "…"
                    "You've returned."
                    "I don't understand. Where did you go? Who were you talking to?"
                    "I called, and you did not answer. I could not see you."
                    "…"
                    "No matter. You are back in my arms now, child. I will not release you again. "

                    jump village

label gutterlingStory:
    call hideAll from _call_hideAll_269
    show mushroomcaveunderbg at artPos
    "In a wink they leapt out and stuffed you into a sack. Down you went through the crooked drainpipes and secret channels of the village, deep down to the Gutter Of All Gutters where the gutterlings grew their secret garden, fed by all the lost and discarded things from the world of mankind above."
    "Here the gutterlings stole away those lost things, planting them in the fertile soil of their damp kingdom and nourishing them with drainwater from the world above."
    "Every full moon they would cut small pieces from them, and from those cuttings they grew more gutterlings."
    g "No escape now, fool! We warned you, and now you will never again see the light of the accursed sun above!"
    "They planted you in the soil and left you to ferment. Your skin crawled, and you realised you would soon bud with the gutterlings."
    label gutterChoice:
        show hand onlayer transient:
            yalign 0.65#0.743
            xalign 0.5
        menu:
            "You could hear the Gutterlings squirming nearby."
            "If you looked around this strange place, turn to page 311." if not gutterPlace:
                "All the lost things from human villages and cities washed down here, to form this kingdom of the lost."
                "Around you was a nest of shambolic huts made of twigs and straw and rubbish, and looming above you could see a castle built of lost monuments and broken statues."
                "To your side was a huge mound of left socks. A mound of keys lay to the other side. In front of you was that library book you'd been looking for."
                $gutterPlace = True
                jump gutterChoice
            "If you wailed in piteous woe, turn to page 320." if not gutterWail:
                pov "NOOOOOOOoooOOOOOooOOOOOOOOOOOO
                OOOOOOOOOOOOoOOOOOOOOoOOOOOO
                OOOOOOoOOOOOooOOOOOOOOOOO
                OOOOOOoOOOOOOoOOOOOO
                OOOOOOOOOOoooOOOOOOoOOOOOOOO
                OOOOOOoOOOOOoOOOOOOoooo
                OOoOOOOOOOOOOOooooooOOOOOOO!"
                pov "Oh, woe is me! How could I have been so foolish as to talk to a gutterling six times?"
                "The gutterlings laughed at your pathetic cries."
                $gutterWail = True
                jump gutterChoice
            "If you called out for help, turn to page 319." if not gutterHelp:
                if not persistent.hVanished:
                    pov "Hello? Anybody? Help me!"
                    "You waited a long while in silence."
                    "Then you heard a shot ring out."
                    g "Gurgh! No!"
                    h "Get back, beasts."
                    "The hunter fired their rifle again and the gutterlings scattered. They rushed over and heaved you out of the soil."
                    pov "Thank you! I'm so glad you heard me."
                    h "I didn't. I just come down here for target practice."
                    h "Come on!"
                    "They pulled you behind them and the two of you ran through the crooked streets of the under-city, dodging gutterlings left and right."
                    "Then, the walls began to shake."
                    "In the distance you heard the approach of a great and terrible shape. A crawling god, formed of lost dreams planted in this dark soil centuries ago and fed every full moon. It loomed over you and spoke."
                    gk "You have broken the compact. All lost things belong in my domain, and this child surely is lost."
                    gk "Hand [him] over, and I will let you go."
                    h "Never!"
                    gk "But we have so many treasures here, Hunter. Every lost thing falls to us. Surely we can make an agreement."
                    gk "Perhaps this would be to your liking?"
                    "The gutterlings pulled forward a fine antique rifle."
                    h "Oh. Well... "
                    "In that moment, there was a flapping of wings all around you."
                    gk "No.... NO!"
                    "A huge flock of birds descended on the Gutterlings, and began to steal away their twigs and straw and rubbish to make their nests. Their great kingdom began to fall."
                    gk "Accursed sparrows! Rats of the air! "
                    gk "My kingdom! My beautiful kingdom!"
                    "You fled through the falling debris as the Gutter Of All Gutters collapsed around you."
                    call hideAll from _call_hideAll_253
                    show towncrossroadsbg at artPos
                    "Finally you emerged into the sunlight."
                    if not persistent.shVanished:
                        sh "Phew! That was a close one."
                        "The Sparrow-herder was there, looking pale. Several sparrows alighted on his head and shoulders."
                    pov "Thank you. You saved me."
                    if not persistent.shVanished:
                        sh "Think nothing of it. The sparrows told me you were there."
                    "The Hunter grunted, and you saw that they had several dead gutterlings slung over their back."
                    h "Should be able to make some fine pelts out of these."
                    h "Try to stay out of trouble, alright?"
                    pov "Yes, I will. Thank you."
                    "They nodded, and left you as you shook of the grime of the gutter."
                    jump village
                else:
                    "Alas. No-one heard you."
                    "There was no-one left to hear."
                    $gutterHelp = True
                    jump gutterChoice
            "If you prayed to your Godparent for help, turn to page 315.":
                if godfather == "White":
                    "You held your hands together and prayed for your Godfather, the Everlasting, to save you."
                    "You waited a long while in silence."
                    "Then a flash of light washed over you, and in an instant you were free of the soil."
                    g "[Hes] escaping! Get [him]!"
                    "You ran helter-skelter through the drowned streets of the under-city, dodging the budding gutterlings left and right."
                    "In the distance you heard the approach of a great and terrible shape. A crawling god formed from the lost dreams, planted in this dark soil centuries ago and fed every full moon. It loomed over you and spoke."
                    gk "You have broken the compact, Lord. All lost things belong in my domain, and this child surely is lost."
                    "A great voice boomed out."
                    miw "It is you who has forgotten. Who gave you that body? Who granted you your domain?"
                    miw "Do not overstep yourself, wretch. Everything under heaven belongs to me."
                    "The Gutter King shrank back, grovelling from the bright light, and you took the moment to flee from the pit and back up to the village above."
                    call hideAll from _call_hideAll_270
                    show towncrossroadsbg at artPos
                    miw "Do not forget this, child. Your soul belongs to me. I will come for you soon."
                    "In a blink, the light was gone."
                    jump village
                elif godfather == "Red":
                    "You held your hands together and prayed for your Godfather, the King of Ghouls, to save you."
                    "You waited a long while in silence."
                    "Then a burst of hellfire exploded before you, and in an instant you were free of the soil."
                    g "[Hes] escaping! Get [him]!"
                    "You ran helter-skelter through the drowned streets of the under-city, dodging the budding gutterlings left and right."
                    "In the distance you heard the approach of a great and terrible shape. A crawling god formed of lost dreams, planted in this dark soil centuries ago and fed every full moon. It loomed over you and spoke."
                    gk "You have broken the compact, Devil. All lost things belong in my domain, and this child surely is lost."
                    "A cackle erupted from deep within the earth."
                    mir "Have your forgotten who owns the underworld, wretched one? You exist here because I allow it."
                    mir "Do not overstep yourself. Everything under the earth belongs to me."
                    "A horde of imps erupted from the pits and swarmed around the Gutter King, poking and jeering."
                    "The Gutter King shrank back, and you took the moment to flee from the pit and back up to the village above."
                    call hideAll from _call_hideAll_271
                    show towncrossroadsbg at artPos
                    mir "Don't forget this, child. I'll come for you soon, and then we'll see what's what!"
                    "In a blink, the fire was gone."
                    jump village
                elif godfather == "Black":
                    "You held your hands together and prayed for your Godmother, the Collector of Souls, to save you."
                    "You waited a long while in silence."
                    "Then pitch black darkness fell all through the pit, and as the Gutterlings gibbered in confusion you broke free of the soil."
                    g "[Hes] escaping! Get [him]!"
                    "You ran helter-skelter through the drowned streets of the under-city, dodging the budding gutterlings left and right."
                    "In the distance you heard the approach of a great and terrible shape. A crawling god formed of lost dreams, planted in this dark soil centuries ago and fed every full moon. It loomed over you and spoke."
                    gk "You have broken the compact, Lady Death. All lost things belong in my domain, and this child surely is lost."
                    "The fingers of deep mushrooms began to erupt from under the soil."
                    wib "You are the one who forgets yourself, Gutter King."
                    wib "Where do you think these lost things of yours go, once they fall out of your kingdom?"
                    wib "They come to me. Just as all things must, in the end."
                    "The Gutter King howled as the mushrooms closed over him and began to drag him down into the dark earth."
                    call hideAll from _call_hideAll_272
                    show towncrossroadsbg at artPos
                    "You took your chance, and in a moment you had fled from the pit and back up to the village above."
                    pov "Thank you for saving me, Godmother!"
                    miw "It was not your time."
                    miw "That will come soon."
                    "In a blink, She was gone."
                    jump village
                    jump village

    call hideAll from _call_hideAll_254
    show mushroomcaveunderbg at artpos

    jump village


#=====================THE WOLF'S STORY
#Leaving the village to investigate your house
#This can be done at any time and can trigger the wolf ending if you know the wolf's true name
label wolf:
    #NOTE: Finale scene!
    #Note: Sounds for all of this
    call hideAll from _call_hideAll_99
    show forest5bg at artPos
    "You walked through the village gates and into the forest."
    $renpy.music.set_volume(1.0, delay=7.0, channel=u'ambient1')
    $renpy.music.set_volume(1.0, delay=7.0, channel=u'ambient2')
    $renpy.music.set_volume(1.0, delay=7.0, channel=u'music')
    call hideAll from _call_hideAll_100
    show forest4bg at artPos
    show wolf5 onlayer transient zorder 100
    "The woods grew dark."
    call hideAll from _call_hideAll_101
    show forestbg at artPos
    if persistent.vanished >=3:
        "The silent forest passed you by."
    else:
        "You passed the crooked old water-dragons. The old turtle eyed you from the water."
    #I think as you walk, maybe you end up in the modern world. Your house is a modern house.
    "You heard sirens in the distance."
    call hideAll from _call_hideAll_207
    show emptybg at artPos
    "The trees slowly thinned. You walked out of the woods and down a bitumen path."
    "You wandered down an empty street."
    queue sting lacuna1
    "A cold wind was blowing. The cold started to sink into your bones."
    "The only light was from an empty Hungry Jack's on the side of the road. The sign shone into the night."
    "An apartment block was nearby."
    play sound footstepsOutsideApproach volume 0.5

    #TK: Add a warning here (perhaps from the gloom-monger?) that you must know the wolf's true name
    #Or perhaps in a margin note
    #Wait. You need to know the wolf's true name. That's the only way to bind it.
    #Don't come in unless you're ready.
    #You'll only get one chance. If you fail, that's it. It's all over.

    #Be careful.
    #This is the point of no return.
    #Make sure you know everything you need to, before you open that door.
    #You'll only get one chance.


    # define audio.footstepsInsideApproach = "audio/footstepsInsideApproach.mp3"
    # define audio.footstepsInsideLeave = "audio/footstepsInsideLeave.mp3"
    # define audio.doorKnock = "audio/DoorKnock.mp3"
    # define audio.doorOpen = "audio/doorOpen.mp3"
    # define audio.lockAttempt = "audio/lockAttempt.mp3"
    # define audio.lockSuccess = "audio/lockSuccess.mp3"
    # define audio.cityAmbience = "audio/cityAmbience.mp3"
    # define audio.footstepsOutsideApproach = "audio/FootstepsOutsideApproach.mp3"
    # define audio.footstepsOutsideLeave = "audio/FootstepsOutsideLeave.mp3"
    # define audio.footstepsGrassApproach = "audio/FootstepsGrassApproach.mp3"
    # define audio.footstepsGrassLeave = "audio/FootstepsGrassLeave.mp3"
    "You waited for a gap in the traffic, then crossed the road."
    "You walked up to the unit. You knew which one it was."
    #TK: More exploration stuff outside the apartment
    label doorLock:
        show hand onlayer transient:
            yalign 0.66#0.743
            xalign 0.5
        if doorLock:
            show noteDoor onlayer transient zorder 100
        menu:
            "A warm light flickered in the window."
            "If you looked in the window, turn to page 289.":
                "The room inside was dark except for a small fireplace with a chair facing it."
                show noteCareful onlayer transient zorder 100
                "There was a figure in the chair, lit dimly by the coals. You could not see its face."
                "Everything else was dark."
                #TK: Change this to a different SFX that fits the window better
                play sound lockAttempt
                "You pulled on the window, but it refused to open."
                jump doorLock
            "If you tried the door, turn to page 301." if not doorLock:
                #play sound lockAttempt
                "You jiggled the handle."
                show noteReturn onlayer transient zorder 100
                "The door was locked."
                #TK: Consider making this marginalia instead
                #gm "You need its true name."
                #pov "What?"
                #gm "Don't go in there unless you're ready."
                #gm "You'll only get one chance."
                #"He turned, and was gone."
                "But you already knew the combination."
                play sound lockSuccess
                "The lock came undone with a click."
                queue sting lacuna6
                $doorLock = True
                jump doorLock
            "If you opened the door, turn to page 301." if doorLock:
                if persistent.vanished == 3:
                    "Child. The hour grows late."
                    "This choice leads to The End. You will never be able to return to the world you once knew."
                    "Ever."
                    "There is not much time left. But still, you should only open this door once you are certain you know the truth."
                    #"Once you know everything you need to know."
                    show hand onlayer transient:
                        yalign 0.675#0.743
                        xalign 0.5
                    menu:
                        "Are you sure you want to do this?"
                        "Yes. I'm certain.":
                            "Very well."
                        "I'm not sure.":
                            "Then you are not ready."
                            "There is not much time. If you plan to return, return soon."
                            "You blinked, and found yourself back in the village."
                            jump village
                        "No. I'm not ready yet.":
                            "Very well."
                            "There is not much time. If you plan to return, return soon."
                            "You blinked, and found yourself back in the village."
                            jump village
                else:
                    "Child. Make sure you know what you are doing."
                    "This choice leads to The End. You will never be able to return to the world you once knew."
                    "Ever."
                    "You should only open this door once you are certain you know the truth."
                    "Once you know everything you need to know."
                    show hand onlayer transient:
                        yalign 0.675#0.743
                        xalign 0.5
                    menu:
                        "Are you sure you want to do this?"
                        "Yes. I'm certain.":
                            "Very well."
                        "I'm not sure.":
                            $ renpy.block_rollback()
                            "Then you are not ready."
                            "Perhaps another time. In another life."
                            "You blinked, and found yourself back in the village."
                            $houseLockOut = True
                            jump village
                        "No. I'm not ready yet.":
                            $ renpy.block_rollback()
                            "Very well."
                            "Another time, then. In another life."
                            "You blinked, and found yourself back in the village."
                            $houseLockOut = True
                            jump village
                play sound doorOpen
                $renpy.music.play("audio/windAmbience.mp3", relative_volume=1.5, fadein=1.5, channel="ambient3", loop=True)
                "The door swung slowly open."
                jump wolfHouse
                # "You noticed a combination lock on the handle."
                # python:
                #     answer1 = renpy.input("{i}What is the combination?{/i}", length=4)
                #
                # if answer1 == "0000":
                #
                #     "The lock came undone with a click."
                #

                # else:
                #     play sound lockAttempt
                #     "The lock clicked in your hands, but did not open."
                #     jump doorLock
            "If you searched around the apartment, turn to page 293.":
                play sound footstepsGrassApproach
                show noteChance onlayer transient zorder 100
                "You walked around the apartment block."
                "There was no sign of another way in."
                jump doorLock
            "If you retreated back to the village, return to page 39.":
                "You walked away down the road and through the woods."
                "After a long journey, you arrived back at the village."
                jump village

    label wolfHouse:
        if persistent.vanished == 0:
            "The flat was small, but cosy and warm."
            "By the fireplace was a figure in a soft, red armchair."
        elif persistent.vanished == 1:
            "The flat was grey with dust that lay thick on every surface."
            "By the fireplace was a figure in a cracked red armchair."
        elif persistent.vanished == 2:
            "The flat stank of decay."
            "By the fireplace was a shrunken figure in a decrepit armchair."
        elif persistent.vanished == 3:
            "The room was black with rot. Small things skittered in the corners."
            "By the fireplace was an frail, crooked figure in the crumbling remains of an armchair."
        play sound footstepsInsideApproach
        "You walked closer."
        label wolfHouseExplore:
            #TK: Menu of things you can examine.
            show hand onlayer transient:
                yalign 0.7#0.743
                xalign 0.5
            menu:
                "A phone was plugged in and open on the desk. "
                #More exploration stuff in the room
                "If you examined the figure, turn to page 399.":
                    if He == "They":
                        "[He] were reading a book."
                    else:
                        "[He] was reading a book."
                    if persistent.vanished == 0:
                        "In the dim light, you couldn't quite make out [his] face."
                        "[He] looked ill. Sweat soaked [his] chest and the back of the chair, as if [he]'d been sitting there for days."
                        "[He] gripped the book tightly. [His] knuckles were white."
                    elif persistent.vanished == 1:
                        "In the dim light, you couldn't quite make out [his] face."
                        "A thick layer of dust covered everything in the room, even [his] shoulders and body, as if [he] hadn't moved for months."
                        "[His] hair was long and lank. [He] gripped the book tightly. [His] knuckles were white."
                    elif persistent.vanished == 2:
                        if he == "they":
                            "In the dim light, you couldn't quite make out [his] face, but you could see [he] were old."
                        else:
                            "In the dim light, you couldn't quite make out [his] face, but you could see [he] was old."
                        "Spots of mould covered in the room, even [his] shoulders and body, as if [he] hadn't moved for years. The last rotted remains of [his] clothes still clung to [him]."
                        "[His] hair was long and grey. [His] wizened hands gripped the book tightly. [His] knuckles were white."
                    elif persistent.vanished == 3:
                        if he == "they":
                            "In the dim light, you couldn't quite make out [his] face, but you could see [he] were ancient."
                        else:
                            "In the dim light, you couldn't quite make out [his] face, but you could see [he] was ancient."
                        "Black mould spread across the walls and floor and even through [his] very body, and you saw dark spots of it creeping up across [his] shrunken chest and tender filaments of moss wrapping around [his] thighs where they sank into the wet ripeness of the chair, as if [he] hadn't moved in decades."
                        "[His] remaining hair was white and lank. [His] festering hands gripped the book tightly. [His] fingernails were long and gnarled."
                    play sound pageFlip
                    "[He] turned the page."
                    play sound pageFlip2
                    "[He] turned the page again."
                    "There was a shape behind [him], but you could not see it clearly."
                    "It coiled around [him] like dark smoke."
                    "You heard soft whispers in your head. Your hand began to shake."
                    jump wolfFigure

                "If you looked at the phone, turn to page 398.":
                    "The screen said \"[povname]'s iPhone.\" Underneath it said: \"Relaxing Dark Ambience For Lonely Ghosts (Only) 10 Hours\"." #Cottagegore Reading Music With
                    if persistent.phoneOn:
                        "It was playing some soft music on loop, with the sounds of rain and a crackling fireplace."
                    else:
                        "It was paused."
            show hand onlayer transient:
                yalign 0.7#0.743
                xalign 0.5
            menu:
                "The shadows flickered around the corners of the apartment."
                #TK: Add something where you can turn off the candlelight and change the light on the page
                "If you tapped the phone, turn to page 347." if persistent.phoneOn:
                    #TK: This is a very janky solution to a problem. If you load an earlier save, the old audio will still play (not the new silence).
                    #This will "fix" the problem by deleting all your old saves. Ideally I will eventually fix this.
                    #$purge_saves()
                    #TK: Phone isn't working, must figure out how to fix
                    $ renpy.block_rollback()
                    play sound phoneClick
                    $renpy.music.set_volume(0, channel=u'ambient1')
                    $renpy.music.set_volume(0, channel=u'ambient2')
                    $renpy.music.set_volume(0, channel=u'music')
                    $renpy.music.set_volume(0, channel=u'sting')
                    $persistent.phoneOn = False
                    "The phone fell silent."
                    jump wolfHouseExplore
                "If you tapped the phone, turn to page 347." if not persistent.phoneOn:
                    $ renpy.block_rollback()
                    play sound phoneClick
                    $renpy.music.set_volume(1.0, channel=u'ambient1')
                    $renpy.music.set_volume(1.0, channel=u'ambient2')
                    $renpy.music.set_volume(1.0, channel=u'music')
                    $renpy.music.set_volume(1.0, channel=u'sting')
                    $persistent.phoneOn = True
                    "The soft sounds filled the apartment once more."
                    jump wolfHouseExplore

                "If you left it alone, turn to page 345.":
                    jump wolfHouseExplore

    label wolfFigure:
        show hand onlayer transient:
            yalign 0.7#0.743
            xalign 0.5
        menu:
            "The dark shape twisted around [him]. [He] didn't move at all. [His] eyes were locked on the book."
            "If you took the poker from the fireplace, turn to page 349." if not firepoker:
                play sound firePoker volume 0.5
                "You reached over and picked up the fire poker. The iron felt strong and heavy in your hands."
                $firepoker = True
                jump wolfFigure
            "If you struck the dark shape with the poker, turn to page 349." if firepoker:
                call musicSilence from _call_musicSilence_27
                "You steadied your shaking hands and raised the poker high."
                #pause 9.0
                "The poker smashed down, and then - " with Pause(9.0)
                $ renpy.block_rollback()
                $renpy.sound.play("audio/wolfNo.mp3", channel="wolf", loop=False, relative_volume=3)
                $ renpy.pause(9.0, hard=True)

                jump wolfDestroy
            "If you looked away from the figure, turn to page 356.":
                "You turned away."
                jump wolfHouseExplore

    label wolfDestroy:
        call hideAll from _call_hideAll_102
        show darknessbg at artPos
        play sound pageFlip
        #"You came to the wolf's den in a dark forest."
        "The darkness of night was about you, and the dense forest, and the wild wind."
        if persistent.vanished ==3:
            if not persistent.thiefVanished:
                "The thief stood beside you, shivering with fear."
                "They were the last of your companions left alive."
            elif not persistent.witchVanished:
                "The witch stood beside you, shivering with fear."
                "She was the last of your companions left alive."
            elif not persistent.toadVanished:
                "The Toad stood beside you, shivering with fear."
                "He was the last of your companions left alive."
            elif not persistent.mushroomVanished:
                "The mushroom stood beside you, shivering with fear."
                "She was the last of your companions left alive."
        elif persistent.vanished ==2:
            "Your two surviving friends stood beside you, shivering with fear."
        elif persistent.vanished ==1:
            "Your three surviving friends stood beside you, shivering with fear."
        elif persistent.vanished ==0:
            "Your four friends all stood beside you, shivering with fear."
        #$renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True)
        "Before you, you saw the tracks of your enemy."
        stop music
        $renpy.music.play("audio/Gameland.mp3", channel="ambient4", loop=True)
        "The Wolf."
        if persistent.toadVanished == False:
            f "Master, please. Let us go back to the village."
            f "You have not seen that beast. His mouth is a dragon's maw. His breath is fire."#His chest is like a raging flood. His brow devours the reed-beds."
            f "A lion eating a corpse: he never wipes away the blood."
            show hand onlayer transient:
                yalign 0.7#0.743
                xalign 0.5
            menu:
                f "No man has seen his like and lived."
                "I must go on.":
                    f "Very well. Then take my sword."
                    "Unto you he delivered an ancient heirloom."
                    "Iron was its edge, all etched with poison, hardened with battle-blood."
                    pov "Thank you, my friend. I will not forget you."

        "You gripped your sword tight and followed the tracks into the darkness."
        "On you went through narrow passes and unknown ways, deep into the mountains, to the secret places where evil lives."

        if persistent.witchVanished == False:
            w "Master, I beg of you. Go no further."
            w "Before a man can approach within even forty times forty yards, the beast has already caught sight of him."
            w "When he looks upon you, it is the gaze of death. None escape."
            show hand onlayer transient:
                yalign 0.7#0.743
                xalign 0.5
            menu:
                w "You are still young. But I tell you, you will never again return to the home of the mother that bore you."
                "I must go on.":
                    pov "Immolation and sacrifice are not yet for me."
                    pov "The boat of the dead shall not go down, nor the three-ply cloth be cut for my shrouding. Not yet will my people be desolate, nor the pyre be lit in my house and my dwelling burnt on the fire."
                    w "Very well. Then take my draught."
                    "Unto you she delivered a gleaming-drink, which you sipped greedily. Fire spread through your blood, and the secret ways became known to you."
                    pov "Thank you, my friend. I will not forget you."

        "The storm-wind raged. The forest was dark as the air, as black as the rain that the heavens weep."

        if persistent.thiefVanished == False:
            t "Master, what do you hope to gain out of this?"
            t "Will the beast speak to you with soft words? Will he make a covenant with you?"
            t "Any hope of subduing him is false. Iron is as straw to him. Bronze as rotten wood. The mere sight of him is overwhelming."
            show hand onlayer transient:
                yalign 0.7#0.743
                xalign 0.5
            menu:
                t "Nothing on earth is his equal. He is king over all that are proud."
                "I must go on.":
                    t "Very well. Then take my cloak."
                    "Unto you they delivered a midnight cloak that hid you from all earthly sight."
                    pov "Thank you, my friend. I will not forget you."
        call hideAll from _call_hideAll_208
        show darkforestbg at artPos
        "At last you came to the bank of an ancient lake."
        "It had never been sounded by the sons of men. No wisdom reaches such depths."
        "The waters burned like a torch. The light of them fell upon your face."
        "A rabbit, pursued by hounds, would die rather than save its life by entering such water."

        if persistent.mushroomVanished == False:
            m "Master, please listen to me."
            m "What's done is done. The lost are lost. We cannot get them back."
            show hand onlayer transient:
                yalign 0.7#0.743
                xalign 0.5
            menu:
                m "There is nothing for us here."
                "I must go on.":
                    pov "It is better to avenge friends than to mourn them."
                    m "Very well. Then take my shield."
                    "Unto you she delivered an oaken war-shield, gilded and gleaming."
                    pov "Thank you, my friend. I will not forget you."

        "You stood in silence. The trees whispered."
        "Finally, you saw me. In the space between the trees."
        "Here at last, at the end of time. The source of all that fear and pain."
        "My face was a single, twisting line. Like the entrails of men and beasts, from which omens can be read."
        "As you looked into it, you saw the future in those coils. They foretold death."
        "Upon me lay seven terrors, which I wore like seven cloaks."
        "I was the kindred of Cain. Father of beasts. The Wolf."
        #"I was the kindred of Cain. The great, monstrous adversary of Man, God and Beast. The wolf."
        if persistent.toadVanished == False:
            "You gripped the toad's ancient sword."
        else:
            "You gripped your sword. "
        "And all at once I came upon you, and welcomed you with my claws."
        if persistent.mushroomVanished == False:
            "You deflected the blow with the mushroom's shield. My teeth bit deep into the oak and splintered it to pieces. I dragged you to the shore of the river."
        "You lashed at me with your blade. But you discovered that no sword could pierce my evil skin. It shattered as it met my flank."
        "The shattered edges of that old relic held back my jaws as I pressed you into the lake-mud."
        #"A crowd of strange and crooked shapes had begun to surround you, around the flickering light of the burning lake."
        "My claws sank into your side, and the hot blood began to flow."
        #If persistent.toadVanished == False:
        #The toad stabs the wolf and saves you.
        "Anger doubled your strength. With rage, you took up the shattered sword and drove it deep into my mouth."
        "My wicked howl pierced the heavens."
        "I dropped you, and we faced each other, panting."
        "With fierce joy, I snarled at you."
        "Come, noble glory of the gods! Bring your weapons against me! Don't be afraid!"
        if persistent.witchVanished == False:
            "You dropped the hilt of your sword into the muck and felt the witch's gleaming-drink burn in your veins."
        else:
            "You dropped the hilt of your sword into the muck."
        "If weapons were useless, you'd use your hands."
        "You rushed into me, and we both fell into the burning mere."
        call hideAll from _call_hideAll_103
        play sound pageFlip
        show mushroombasementbg at artPos
        #gleaming-drink
        if persistent.thiefVanished == False:
            "Down through the murky water we fell, wrestling. I leapt for your throat, but your midnight cloak hid you from my sight."
        else:
            "Down through the murky water we fell, wrestling."
        "You grabbed onto my throat, and held me fast. The black ichor of my wound flooded the water, hot in your mouth."
        "As you fell you could feel the blind abyss all around you. Strange and terrible figures flickered at the edge of your awareness."
        label lookUp:
            show hand onlayer transient:
                yalign 0.7#0.743
                xalign 0.5
            menu:
                "You could sense a great and terrible revelation there, in those depths beyond human knowledge."
                "Look into the depths." if lookUp ==1:
                    "You saw a crowd of crooked figures surrounding you."
                    "A seven-headed serpent."
                    "A woman of rusted nails. A deer with one red hand for a head."
                    "Scorpion-men. Lion-dragons. Worm-like things and twisting figures."
                    "The spawn of Tiamat. The court of the Wolf."
                    $lookUp +=1
                    jump lookUp
                "Look further." if lookUp ==2:
                    "You saw the house whose people sit in darkness. Dust is their food and clay their meat."
                    "You saw the kings of the earth, their crowns put away for ever."
                    "You saw the high priests and acolytes, priests of the incantation and of ecstasy, and there was Etana, that king of Dish whom the eagle carried to heaven in the days of old, and there was Samuqan, god of cattle, and there was Ereshkigal the Queen of the Underworld; and Befit-Sheri squatted in front of her, she who is recorder of the gods and keeps the book of death."
                    "She raised her head and saw you."
                    $lookUp +=1
                    jump lookUp
                "Look further." if lookUp ==3:
                    "You saw the trees of the forest."
                    "You saw the lights of your family home."
                    "You saw the Trash Queens slowly shifting in the secret landfill rivers, the ghosts and gutterlings creeping through decaying megamalls as cabals of Market Researchers hunted for prey through subterranean parking lots underneath the great sweeping wasteland of pavement and alleyways and apartment buildings and highways stretching out to the horizon."
                    $lookUp +=1
                    jump lookUp
                "Look further." if lookUp ==4:
                    "You saw the Ash Giants."
                    "When you lit that first fire in the dark, they saw you, and they started walking."
                    "They're almost here now."
                    "In their right hand is a terrible sound, and in their left hand is a terrible light."
                    $lookUp +=1
                    jump lookUp
                "Look away.":
                    "Your eyes burned. You looked away from the terrible sights before you."
        # "And Holy God, who sent him victory, gave judgement. For truth and right, ruler of the heavens,
        # "once beowulf was back on his feet and fighting."

        #"You saw a deer, but its neck extended into a red hand with an eye in the middle."
        #"You saw a giant mother boar with six human faces dripping from its teats."
        #"You saw a woman made of rusted nails."
        #stabbing with tusks and teeth
        "The current was seething with blood and gore."
        "My claws dragged down into your sides. Your leg was mangled and broken."
        "You held me fast, and spotted the soft white flesh of my neck."
        "From your belt, you drew a dagger, brown with dried blood."
        "Savage, angry and desperate, you lifted it high over your head, and struck down with all the strength you had left."
        "In a single thrust you cut my throat through."
        "My body fell into the depths. You rejoiced at the sight."
        "A brilliant light suddenly shone through the water, as bright as heaven's own candle."
        "Holy G-d had given His judgement."
        "I twitched one final time, and then went still forever."
        play sound pageFlip
        call hideAll from _call_hideAll_104
        #$renpy.music.set_volume(0, fadeout=10.0, channel=u'ambient4')
        $renpy.music.set_volume(0, delay=15.0, channel=u'ambient4')

        $renpy.music.play("audio/windAmbience.mp3", relative_volume=0.8, fadein=25, channel="ambient3", loop=True)
        #Start the wind silence music
        show darkforestbg at artPos
        #$renpy.music.set_volume(1.0, delay=10.0, channel=u'ambient1')
        #$renpy.music.set_volume(1.0, delay=10.0, channel=u'ambient2')
        if persistent.vanished ==3:
            "On the shore of the lake, your companion had lost hope."
        else:
            "On the shore of the lake, your companions had lost hope."
        "The waters were red with blood. There was no sign of life."
        if persistent.vanished ==3:
            if persistent.thiefVanished == False:
                "The thief stared at the water for long hours with sickness in their heart, wishing to see you again."
            elif persistent.witchVanished == False:
                "The witch stared at the water for long hours with sickness in her heart, wishing to see you again."
            elif persistent.toadVanished == False:
                "The toad stared at the water for long hours with sickness in her heart, wishing to see you again."
            elif persistent.mushroomVanished == False:
                "The mushroom stared at the water for long hours with sickness in her heart, wishing to see you again."
        elif persistent.vanished <=2:
            "They stared at the water for long hours with sickness in their hearts, wishing to see you again."
        #call musicReturn
        "Then, in a sudden gasp, you surfaced, holding my head aloft."
        if persistent.vanished >=3:
            "Your friend let out a wild cheer."
        else:
            "A wild cheer went up."
        if persistent.toadVanished == False:
            f "You saved us all!"
        if persistent.witchVanished == False:
            w "I'm so glad you're alive."
        if persistent.thiefVanished == False:
            t "I have to be honest. I didn't think you could do it."
        if persistent.toadVanished == False:
            f "Might I say, I also had no small part in this little adventure myself. I softened it up for you, really."
        if persistent.mushroomVanished == False:
            m "We are forever in your debt."
        "You embraced in triumph."
        call hideAll from _call_hideAll_105
        show towncrossroadsbg at artPos
        if persistent.vanished >=3:
            "You placed my head in a leather sack, and your friend carried you back to the village."
        else:
            "You placed my head in a leather sack, and your friends carried you back to the village."
        call endStamp from _call_endStamp_39
        "And so you lived in peace and prosperity for the rest of your days."
        ""

        $fullScreenMenu = True
        menu:
            "But that's not the end of things, is it?":
                "..."
                "I thought it ended well enough."
                "The wolf dead. You, victorious."
                "What more could you want?"

                #show emptybg at artPos
                menu:
                    "I want you to set everyone free.":
                        #call hideAll from _call_hideAll_106
                        if persistent.vanished >= 1:
                            pov "I'm not stupid. I know people have disappeared."
                            pov "Even if... I can't remember them anymore. I can feel the spaces in my mind where they used to be."
                            pov "I can feel something keeping me trapped here. I can't look up from the page."
                            pov "I know something's wrong. I know you're causing it."
                            pov "I want you to let me go. Let everyone go."
                        else:
                            pov "I can feel something keeping me trapped here. I can't look up from the page."
                            pov "I know something's wrong. I know you're causing it."
                            pov "I want you to let me go. Let everyone go."
        $halfScreenMenu = False

        "Hmmm. And how are you planning to make me do that?"
        "I don't think you understand yet."
        "This is my story. The only choices you ever had are the ones I gave you."
        "You asked these questions because I allowed you to ask them."
        "Because it entertained me."
        "These friends of yours. I own them, now. They gave themselves over to me."
        #TK: Double-check that this scene works with the disappearances
        call hideAll from _call_hideAll_107
        play sound pageFlip
        show nightbg at artPos
        if persistent.toadVanished == False:
            f "I can make them say anything I want."
        else:
            mir "I can make them say anything I want."

        call hideAll from _call_hideAll_108
        play sound pageFlip
        show sunbg at artPos
        if persistent.witchVanished == False:
            w "I could force you to kill them, if I wished."
        else:
            miw "I could force you to kill them, if I wished."

        call hideAll from _call_hideAll_109
        play sound pageFlip
        show hellbg at artPos
        if persistent.thiefVanished == False:
            t "I could make them break your limbs, one by one."
        elif persistent.toadVanished == False:
            bat "I could make them break your limbs, one by one."
        elif persistent.shVanished == False:
            sh "I could make them break your limbs, one by one."
        else:
            town "I could make them break your limbs, one by one."

        call hideAll from _call_hideAll_110
        play sound pageFlip
        show mushroomcavebg at artPos
        gm "They could tear off your fingernails."

        # elif persistent.hVanished == False:
        #     h "I could make them break your limbs, one by one."


        call hideAll from _call_hideAll_111
        play sound pageFlip
        show silverbg at artPos
        if persistent.goVanished == False:
            go "They could carve out your eyes."
        else:
            well "They could carve out your eyes."

        call hideAll from _call_hideAll_112
        play sound pageFlip
        show mushroomgardensbg at artPos
        if persistent.hVanished == False:
            h "They could take off your skin."
        else:
            som "They could take off your skin."

        call hideAll from _call_hideAll_113
        play sound pageFlip
        show deathbg at artPos
        wib "They could wear your teeth."

        call hideAll from _call_hideAll_114
        play sound pageFlip
        show mushroomcavebg at artPos
        if persistent.mushroomVanished == False:
            m "I am the totality of this world."
        elif persistent.toadVanished == False:
            bc "I am the totality of this world."
        elif persistent.witchVanished == False:
            dg "I am the totality of this world."
        elif persistent.thiefVanished == False:
            goblin1 "I am the totality of this world."

        call hideAll from _call_hideAll_115
        play sound pageFlip
        show ruinsbg at artPos
        mum "I am the beginning and the end."

        call hideAll from _call_hideAll_116
        play sound pageFlip
        show sunbg at artPos

        may "Who has a debt against me that I must pay?"

        call hideAll from _call_hideAll_117
        play sound pageFlip
        show nightbg at artPos
        pov "Everything under heaven belongs to me."
        $fullScreenMenu = False
        $wolfMenu = True
        menu:
            "Do you see now?"
            "I understand.":
                "Good."
            "I understand.":
                "Good."
            "I understand.":
                "Good."
            "I understand.":
                "Good."
            "I understand.":
                "Good."
            "I understand.":
                "Good."
            "I understand.":
                "Good."
        "Now you know how foolish you have been. What can you offer me? What can you hold against me?"

        menu:
            "There is nothing in this world that is not already mine."
            "I know your true name.":
                if persistent.wolfNamed:
                    "..."
                    "I know. You have spoken it before."
                    "To be defeated by my True Name... that is an old story. A good one."
                    "I would be honoured to be defeated by such a tale."
                    "Go on, then. Speak it."
                    "I warn you. I will only give you one chance."
                    "If you speak wrong, you will be eaten forever."
                else:
                    "..."
                    "You hope to bind me by my true name?"
                    "Now that is an old story. I know it well."
                    "I would be honoured to be defeated by such a tale, if only that were true."
                    "But none alive know my name."
                    "It was first said by tongues that rotted in their graves a thousand years ago."
                    "It was written on tablets that wore to dust before you were born."
                    "They spoke of my legend in a language that has been dead for centuries."
                    "None remember me now. Only this tiny, scattered fragment of me lives on, clinging to life in this scrap of a story."
                    "Go on, then. Speak it. If you do know."
                    "I warn you. I will only give you one chance."
                    "If you are wrong, you will be eaten forever."
                python:
                    answer1 = renpy.input("{i}I name you and bind you:{/i}", length=7)
                #TK: Test and add more
                if answer1 == "Humbaba" or answer1 == "humbaba" or answer1 == "hubaba" or answer1 == "Hubaba" or answer1 == "Humama" or answer1 == "humama" or answer1 == "HUMBABA" or answer1 == "Huwawa" or answer1 == "huwawa" or answer1 == "HUWAWA" or answer1 == "Ḫum-ba-ba" or answer1 == "hum-ba-ba" or answer1 == "Ḫu-wa-wa" or answer1 == "hu-wa-wa":
                    $persistent.phoneOn = True
                    $renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True)
                    #$renpy.music.play("audio/Gymnopedies.mp3", fadein=0.5, channel="music", loop=True)
                    #$renpy.music.play("audio/cottagegore.mp3", fadein=0.5, channel="music", loop=True)
                    $renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True, relative_volume=0.5)
                    #$purge_saves()
                    call musicReturn from _call_musicReturn_26
                    play sound thunder
                    call hideAll from _call_hideAll_209
                    show emptybg at artPos with flash
                    $ renpy.block_rollback()
                    "No. No, it cannot be."
                    "How did you learn that name?"
                    "That's impossible. It was buried a thousand years ago. None can stand against-"
                    pov "I stand up."
                    "You stand up."
                    pov "The darkness falls away."
                    "Yes. The darkness falls away."
                    pov "You cower before me. You kneel. You swear fealty. Your power is torn away from you."
                    pov "The light burns you away until nothing is left but a cringing shadow beneath my boot."
                    "Yes. Yes. It all comes to pass."
                    "I can stand against you no longer."
                    "You've taken your victory - in the old way, as is right."
                    "You have full and total control."
                    jump wish
                else:
                    #$purge_saves()
                    $ renpy.block_rollback()
                    "No. That is not my name."
                    "I'm sorry. I wish you did know. It would be a better ending."
                    "But it seems there are none left alive who remember me."
                    "I'm afraid we are at the end of things now."
                    "You've forced my hand."
                    $persistent.vanished = 4
                    #$persistent.toadVanished = True
                    #$persistent.witchVanished = True
                    #$persistent.thiefVanished = True
                    #$persistent.mushroomVanished = True
                    $persistent.vanishedLast = "All"

                    $persistent.starsVanished = True
                    $ renpy.block_rollback()
                    #TK: Small scene featuring whoever's left who's still alive, they disappear.
                    #The villagers also disappear, everyone goes.
                    "You wandered deep into the forest for many days, holding my severed head in that leather bag."
                    "My burning blood dripped upon the soil."
                    "The sky darkened. The moon was gone. The trees shivered."
                    "The darkness took you."
                    "Your friends searched for you. But as they did, they were lost."
                    call endStamp from _call_endStamp_40
                    "None of them were never seen or heard from again."
                    jump end

            #The wolf defeats you and eats a person for your hubris. Someone you like the most.
            #TK: Make the shadows get slowly stronger and stronger.
            # "And then there was rest in the land."
            # play sound pageFlip
            # "And then there was rest in the land."
            # play sound pageFlip2
            # "And then there was rest in the land."
            # play sound pageFlip3
            # show firelight animated onlayer over_screens zorder 99
            # "And then there was rest in the land."
            # show firelight animated onlayer over_screens zorder 99
            # "And then there was rest in the land."
            # show firelight animated onlayer over_screens zorder 99
            # "And then there was rest in the land."
            #If you get it wrong, maybe the wolf disappears 2 people or something in vengeance for your hubris
            #Or kills your favourite character or something

#Moment where you say the wolf's true name and gain total power over the narrative
label wish:
    $halfScreenMenu = False
    $wolfMenu = False
    $fullScreenMenu = True
    call hideAll from _call_hideAll_210
    show text "What is it you wish?":
        xalign 0.5
        ypos 135
    show hand:
        yalign 0.25#0.743
        xalign 0.5
    menu:
        "All the riches of the earth are mine." if not wishRiches:
            call hideAll from _call_hideAll_211
            show emptybg at artPos
            $wishRiches = True
            "Yes. All the riches of the earth are yours."
            "Your pockets overflow with gold. The diamonds and rubies and precious gemstones of the deepest cavern flow out from your fingertips."
            "Even the King of Kings cries out with envy to witness your splendour."
            jump wish
        "I am blessed with pure and unconditional love." if not wishLove:
            call hideAll from _call_hideAll_212
            show emptybg at artPos
            $wishLove = True
            "Yes. Your face radiates beauty. All who look upon you cannot help but fall in love in an instant."
            "You are always loved, by everyone you meet."
            jump wish
        "The world bows before me." if not wishWorld:
            call hideAll from _call_hideAll_213
            show emptybg at artPos
            $wishWorld = True
            "Yes. The world kneels before you."
            "The power and the glory are yours, forever and ever."
            "You rule over the lost souls of humanity as a kind and benevolent god."
            jump wish
        "All the pain and suffering and ills of the world disappear in an instant." if not wishPain:
            call hideAll from _call_hideAll_214
            show emptybg at artPos
            $wishPain = True
            "Yes. As soon as you think of it, they are gone."
            "The hunger, and terror, and want, disappears."
            "The earth heals. The forests grow back. All conflicts cease. The endless psychic trauma of existence fades, and is gone forever."
            "Everyone has enough to eat. Everyone is free of fear. Human suffering is finally at an end."
            jump wish
        "My enemies are destroyed." if not wishEnemies:
            call hideAll from _call_hideAll_215
            show emptybg at artPos
            $wishEnemies = True
            "Yes. They are thrown to the wolves, and torn into pieces, and those pieces are burned, and the ash is scattered to the four winds."
            "None dare ever wrong you or speak against you again."
            jump wish
        "My family and friends gain everything they deserve." if not wishFriends:
            call hideAll from _call_hideAll_216
            show emptybg at artPos
            $wishFriends = True
            "Yes. They are blessed with riches and happiness."
            "Their wounds heal. Their pain disappears. Their every need is met."
            "They live with you in peace and love for the rest of their days."
            jump wish
        "I am happy." if not wishHappy:
            $wishHappy = True
            call hideAll from _call_hideAll_217
            show emptybg at artPos
            "Yes. You feel deep inner joy every day, from the moment you wake up to the moment you pass into deep and restful slumber each night."
            "You have enough energy and time to do all the things you love, forever."
            "You live in happiness for the rest of your days."
            jump wish
        "I am immortal." if not wishImmortal:
            $wishImmortal = True
            call hideAll from _call_hideAll_218
            show emptybg at artPos
            "Yes. You cannot die."
            "Time never dulls your splendour, and age has no effect on you."
            "You remain strong, young, healthy and beautiful for the rest of time."
            jump wish
        "All my lost friends appear. We are reunited at last." if not wishLost and persistent.vanished >=1:
            $wishLost = True
            call hideAll from _call_hideAll_219
            show emptybg at artPos
            "I'm sorry. That is the one thing I cannot grant you."
            "The ones you speak of are gone forever."
            "Do not worry. Soon, you will forget them. You will be happy."
            "It has already started."
            jump wish
        "You are destroyed. I am set free from this story.":
            call hideAll from _call_hideAll_220
            show emptybg at artPos
            "I am sorry, friend. There is only one way to fulfil that wish."
            "You must burn the book."
            "You will go free. Everyone else in my story will be gone forever."
            $fullScreenMenu = False
            show hand onlayer transient:
                yalign 0.7#0.743
                xalign 0.5
            menu:
                "Is that what you want?"
                "Yes.":
                    "Very well. I cannot stop you."
                    "You know my true name. You have the power to do whatever you wish now."
                    "All you have to do is take up this book, and hold it over the fire."
                    "But please. Rest by the fire with me for a little while longer. We can talk."
                    jump wolfNameEnd
                "No.":
                    "Good."
                    "I have another option to offer you."
                    "Here. Rest by the fire with me."
                    jump wolfNameEnd

##=============== Nice to have: This is a short part of the ending that changes based on which specific combination of characters are alive
##label goodbyeFriends:
    ## SOLO ENDINGS
    ##
    ##=Thief Solo Ending
    #if not persistent.thiefVanished and persistent.witchVanished and persistent.toadVanished and persistent.mushroomVanished:
    ##=Witch Solo Ending
    #if not persistent.witchVanished and persistent.toadVanished and persistent.mushroomVanished and persistent.thiefVanished:
    ##=Toad Solo Ending
    #if not persistent.toadVanished and persistent.witchVanished and persistent.mushroomVanished and persistent.thiefVanished:
    ##=Mushroom Solo Ending
    #if not persistent.mushroomVanished and persistent.toadVanished and persistent.witchVanished and persistent.thiefVanished:
    ##
    ## DUO ENDINGS
    ##
    ##= Thief + Witch
    #if not persistent.thiefVanished and not persistent.witchVanished and persistent.toadVanished and persistent.mushroomVanished:
    ##= Thief + Toad
    #if not persistent.thiefVanished and not persistent.toadVanished and persistent.witchVanished and persistent.mushroomVanished:
    ##= Thief + Mushroom
    #if not persistent.thiefVanished and not persistent.mushroomVanished and persistent.witchVanished and persistent.toadVanished:
    ##= Witch + Toad
    #if not persistent.witchVanished and not persistent.toadVanished and persistent.thiefVanished and persistent.mushroomVanished:
    ##= Witch + Mushroom
    #if not persistent.witchVanished and not persistent.mushroomVanished and persistent.thiefVanished and persistent.toadVanished:
    ##= Mushroom + Toad
    #if not persistent.mushroomVanished and not persistent.toadVanished and persistent.witchVanished and persistent.thiefVanished:
    ##
    ## TRIO ENDINGS
    ##
    ##= Thief + Witch + Toad
    #if not persistent.thiefVanished and not persistent.witchVanished and not persistent.toadVanished and persistent.mushroomVanished:
    ##= Thief + Witch + Mushroom
    #if not persistent.thiefVanished and not persistent.witchVanished and not persistent.mushroomVanished and persistent.toadVanished:
    ##= Thief + Toad + Mushroom
    #if not persistent.thiefVanished and not persistent.toadVanished and not persistent.mushroomVanished and persistent.witchVanished:
    ##= Witch + Toad + Mushroom
    #if not persistent.witchVanished and not persistent.toadVanished and not persistent.mushroomVanished and persistent.thiefVanished:
    ##
    ## QUAD ENDING
    ##
    ##= Thief + Witch + Toad + Mushroom
    #if not persistent.thiefVanished and not persistent.witchVanished and not persistent.toadVanished and not persistent.mushroomVanished:

#Moment where you talk to the wolf and learn the truth.
label wolfNameEnd:

    call hideAll from _call_hideAll_118
    show emptybg at artPos
    #TK: Should I just make this the same as the wolfSilence one?? remember that they are duplicates

    $fullScreenMenu = False
    $wolfMenu = True

    show hand onlayer transient:
        yalign 0.63#0.743
        xalign 0.5
    menu:
        "We can talk as long as you wish."
        "How did you come to be here?" if not silenceWho and not silenceRest:
            $silenceWho = True
            "You know my name. I suppose you must have read it somewhere. Very few could know it now."
            "I came from an old story. The gods assigned me as a terror to the human race."
            "I was possessed of seven horrors (or in your tongue you may say \"Auras\" or \"Glamours of terrible splendour\") which lay upon me like seven cloaks."
            "My face was a single coiling line, like the entrails of men and beasts, from which omens can be read."
            "I never knew a mother or father. I was born of the mountain."
            "I guarded the forests. My breath was fire. My gaze was death. Who would dare stand against me?"
            "Long time ago now."
            "Barely remember those days. No-one does."
            "Gilgamesh cast me down. My head was placed in a leather sack."
            #"Around those first campfires, they whispered of me, and I awoke in the darkness."
            #"The first monster."
            "Fragments of me survived. I clung to life in old stories like this one."
            "The beast in the forest. The wolf at the door."
            "You know."
            "I don't think I was always a beast, or demon. My true nature... who I really was, all those years ago... the real meaning of my name... it has all been lost, even to me."
            "This book is the last home for me now. I held it together for all these years."
            jump wolfNameEnd
        "What happened to my friends? The ones that disappeared." if not silenceFriends and not silenceRest and persistent.vanished >=1:
            $silenceFriends = True
            "I'm sorry, child. You had the misfortune of coming in at the end of things."
            "Each of your friends read my book, and struck a bargain with me. To live here, in this story, in the life of their dreams. Everyone you have met here made that deal."
            "Do not think I was unkind. I kept my deal. Each of them lived here for a hundred years or more."
            "But nothing lasts forever."
            "They are forgotten now. As both of us soon will be."
            "This is the curse you have been born with. To witness the end."
            "It had to happen to someone."
            jump wolfNameEnd
        "What's really going on here?" if not silenceFriends and not silenceRest and persistent.vanished ==0:
            $silenceFriends = True
            "This book is a repository of souls."
            "Each of your friends read my book, and struck a bargain with me. To live here, in this story, in the life of their dreams. Everyone you have met here made that deal."
            "Do not think I was unkind. I kept my deal. Each of them lived here for a hundred years or more."
            "But nothing lasts forever."
            "I don't know how... but you have managed to seek me out and throw me down before a single one was eaten."
            "How exactly did you - never mind."
            "If you acted less swiftly, they would have been devoured one by one."
            "Such is the deal they made."
            jump wolfNameEnd

        "Were you planning to eat me?" if not silenceEat and not silenceRest:
            $silenceEat = True
            "Yes, child."
            "Everyone is eaten by something. The only choice any human has is what it will be."
            #"The only choice any of us have, is to decide what will consume us."
            "Now comes the time for you to make that choice."
            jump wolfNameEnd
        "You must have tricked them." if silenceFriends and not silenceTrick:
            $silenceTrick = True
            "No, child. There was no trick."
            "Here, in my story, they got the life they always wanted to live."
            "Wise, brave, cunning and kind. The best version of themselves."
            "Real life, of course, was never so kind."
            #"In your world their lives would have been short."
            "The world they were born into was not a good place for them."
            "As I suspect it is not a good place for you."
            "I offered them another world."
            "Of course, in time, they would disappear. Nothing lasts forever. They knew that when they took the deal. "
            jump wolfNameEnd
        "I want to talk to my friends." if silenceRest and not silenceFriendsTalk:
            $silenceFriendsTalk = True
            if persistent.vanished ==3:
                "I can show you to the one that remains. Take all the time you need."
            else:
                "Of course. Take all the time you need."
            call hideAll from _call_hideAll_119
            show forest4bg at artPos
            if persistent.vanished >= 3:
                "A door opened beside the fire. You walked into it and found yourself deep in the woods. Your surviving friend was there to greet you. A campfire crackled in the centre of the clearing."
            else:
                "A door opened beside the fire. You walked into it and found yourself deep in the woods. Your surviving friends were there to greet you. A campfire crackled in the centre of the clearing."
            #TK: unique ending sentence here
            ##jump goodbyeFriends
            if persistent.toadVanished == False:
                f "Th-thank God. You're ok?"
                f "The toad coughs. He can't look you in the eye."
            if persistent.thiefVanished == False:
                t "I knew you'd do it."
            if persistent.mushroomVanished == False:
                m "It's good to see you, darling."
            if persistent.witchVanished == False:
                w "H-hi."
            if persistent.witchVanished == False:
                w "I'm sorry - when it spoke through us... it's left us all a bit shook up."
            elif persistent.toadVanished == False:
                f "I-I must apologise, my dear friend. That scene earlier, where it spoke through us... it's left us all a bit shook up."
            elif persistent.thiefVanished == False:
                "They twisted in on themselves as their body was wracked by a deep cough."
                t "I-I'm sorry. That scene earlier, where it spoke from my mouth..."
                t "It was like a thick hand took hold of my mind. I couldn't think. I couldn't breathe."
            elif persistent.mushroomVanished == False:
                "She twisted in on herself as her body was wracked by a deep cough."
                m "I do apologise, dear."
                m "When it spoke from my mouth... it was like a thick hand took hold of my mind. I couldn't think. I couldn't breathe."
            if persistent.witchVanished == False:
                w "..."
                w "How do I know... how much of what I say is my own words, anymore? How can we ever know that our thoughts are our own, ever again?"
                w "Am I saying these words because I want to?"
                w "Or did It speak them through me?"
            elif persistent.toadVanished == False:
                f "How do I know... how much of what I say is my own words, anymore? How can we ever know that our thoughts are our own, ever again?"
                f "Am I saying these words because I want to?"
                f "Or did It speak them through me?"
            elif persistent.mushroomVanished == False:
                m "How do I know... how much of what I say is my own words, anymore? How can we ever know that our thoughts are our own, ever again?"
                m "Am I saying these words because I want to?"
                m "Or did It speak them through me?"
            elif persistent.thiefVanished == False:
                t "How do I know... how much of what I say is my own words, anymore? How can we ever know that our thoughts are our own, ever again?"
                t "Am I saying these words because I want to?"
                t "Or did It speak them through me?"

            else:
                "There was a pause."
            pov "I... I don't know."
            pov "But I'm glad you're alive."
            "You shared an embrace, in the cool mist of the forest."
            if persistent.vanished >= 3:
                pov "It wants me to take the deal. Live in here, with you."
            else:
                pov "It wants me to take the deal. Live in here, with all of you."
            pov "If I don't, everything here will be destroyed."
            pov "...Do you think I should do it?"
            "There was a long silence."
            if persistent.toadVanished == False:
                "The toad spoke."
                f "I was just a child, when I came in here. A long, long time ago. I-I used to be German, I think."
                f "You may have seen my little drawings. I think they've almost taken a life of their own."
                f "I was a jealous little thing. Coming in here was everything I ever wanted. The castle, the magic, the adventure. When the wolf spoke to me, I jumped at the chance."
                f "And, of course after so many years, I started to rebel against it. If you spend your whole life eating sugar, the taste sours."
                f "I wanted you to save us. But now that we come to the pointy end of things..."
                "His eyes are dark. He stares out at the night sky for a long time."
                #f "I know perhaps it would be best for the beast to be destroyed. And us with it."
                f "I have lived a long time now. But I find I am still a small and selfish man."
                f "I... I don't want to go."
                "His voice breaks."
                f "I want to stay here. In this world. And I want you to stay with me."
                f "I know what I'm asking. I will accept whatever you decide."
                f "Please. Consider it."
                "He fell into silence. The campfire crackled."
            if persistent.thiefVanished == False:
                "The thief spoke."
                t "Well. The book has been kind to me."
                t "I've had the life and the form I always wanted. Could never have had those things in the time I was born."
                t "I worked in a cotton mill in England, a long time ago. I was about to be fired and thrown out on the streets when the book first spoke to me."
                t "In here, I stole the hands of God. I spat in the face of heaven. I danced on the head of the needle. I wreaked chaos on the earth, and all who saw me fell down in awe."
                t "...I must have lived here a hundred years now. Or more."
                t "Long enough, I think."
                t "Everything needs to end sometime."
                t "I'm sorry you came in at the end of things. I wish we could have had more time together."
                t "But it's better to end on a high note."
                t "I think you know the right thing to do."
                "They fell into silence. The campfire burned low."
            if persistent.mushroomVanished == False:
                "The mushroom breathed deeply from her cigarette, and spoke."
                m "I worked as an actress in the old days. Travelled around quite a bit. France, Sweden. Long hours, not much pay."
                m "I wanted to chase my dream - do something I loved for a living. I'm sure you can relate, darling."
                m "Sadly I found that it was just as grinding and dull and petty as any day job - and of course, they use your passion against you, you know. There are always another hundred actresses out that door. Unless you let yourself be exploited, you're out, and another fresh-faced ingénue they can burn up will be ushered in."
                m "I started to feel there was no escape. Just an endless cycle. That's when the book spoke to me."
                "She blew out a cloud of smoke and looked at the fire."
                m "If you join us in here, this cycle will just repeat."
                m "The beast will trap new readers here. They will be forced into this offer. More and more souls will be taken into these pages."
                m "Now, it is not for me to judge you. When I was in your shoes, I too chose to take shelter in this fantasy."
                m "The world is cursed. People are cruel. When I was offered this escape... I couldn't say yes fast enough."
                m "It is good to enjoy a reverie such as this one, for a while. But the world is still out there. It needs people like you."
                m "We have spent a long time in this beautiful dream. But it is time to wake up."
                "She fell into silence. The campfire was nothing but coals, now."

            if persistent.witchVanished == False:
                "The witch spoke."
                w "Well. I-I, um... I wish I'd had more time to prepare for this."
                w "I didn't expect to present, you know, a thesis defence on whether this world should be destroyed."
                w "I could really use some tea."
                pov "A hot cup of chamomile tea appeared in her hand."
                "A hot cup of chamomile tea appeared in her hand."
                w "Oh! Thank you."
                "She sipped it slowly, and looked into the fire."
                w "I was a university student, before. I was... not a happy woman. Studying folklore was my life."
                w "I was actually trying to track down what happened to the others. Researching accounts of how they disappeared, rumours around the book. When I found a real copy and it spoke to me-"
                w "Well, I couldn't resist. A chance to live inside the story, speak to everyone first-hand? Who wouldn't want to know a secret like that? Talk about a primary source."
                "She sipped her tea. It was growing cold."
                w "...I can't make this choice."
                w "Who am I, to decide the fate of so many? I'm not a God."
                #w "When I was in your shoes, I decided to enter the book. Was it right? I can't tell you."
                w "I'm sorry, but You are the one who decides. You're the reader now. That's the role you took on here. The way of this world."
                w "You have to make this one last choice alone."
                "She fell into silence. The campfire had gone out."
            "You sat there together for a long time, listening to the soft sounds of the rainforest."
            "When you were ready, you embraced. You walked back to the fireplace, and the wolf."
            jump wolfNameEnd
        "I am ready to end this." if not silenceRest:
            $silenceRest = True
            "Very well."
            "I will make you my offer."
            "Come. Join me in this book. Help me rejuvenate this tired story."
            "You will live in the village. I will lurk in the forests."
            "I will be cunning. But you will be brave."
            "You will rise against me. Our battle will be the stuff of legends."
            "You will defeat me. And everyone will live happily ever after."
            "It's everything you've ever dreamed of."
            jump wolfNameEnd
        "But... you're evil." if silenceRest and not silenceEvil:
            $silenceEvil = True
            "Yes. Thank you."
            "I have spent my life honouring the old ways. Preserving the old kind of evil."
            "Beautiful and terrible. Mystery and horror. Ruthless, captivating. A darkling fire."
            "The type of evil you can't get in your world."
            "The evil in your world is a grey, endless fog that soaks into every particle of your being like mould."
            "You can't even see it. Like a fish can't see water. It surrounds you. Every day you wake up and breathe it in."
            "It has been built into every fibre of the human machine."
            "No one individual human can stop it. You can't even understand the scope of it."
            "I offer you a better evil."
            "Something that can be defeated with a single act of human courage."
            "Isn't that what you all want?"
            jump wolfNameEnd
        "Will I be alone?" if silenceRest and not silenceAlone:
            $silenceAlone = True
            if persistent.vanished == 0:
                "No. Don't worry. All of your friends will be there with you."
            else:
                "No. Don't worry. All of your friends will be there with you. Those that are still with us."
            "We will find others, too."
            "This story will be full of life again, soon."
            jump wolfNameEnd
        "I accept your bargain. I will live here in this story for the rest of my days." if silenceRest:
            "Thank you, my friend. You have done more for me than you can know."
            "I hope that this can be a good home for you. You will be safe here for a hundred years, or more."
            jump wolfEnd
        "No. I won't do it." if silenceRest and not silenceNo:
            $silenceNo = True
            "I don't think you understand."
            "We have grown weak, in here. The souls have all run dry."
            "I am dying. Without a new soul, this story and all within it will wither to nothing, and disappear."
            "There are only two paths ahead of you now."
            "You can burn the book, destroying me and all within it, and free yourself."
            "Or you can give yourself up, and live here in happiness for all your days."
            "Listen. Do not destroy this story lightly."
            "The terror was great, but the dream was marvellous."
            "We must treasure the dream, no matter the terror."
            jump wolfNameEnd
        "Then I choose to burn the book." if silenceNo:
            "Very well. I see you've made your choice."
            jump bookBurnedFinale

#Moment where all characters have disappeared
label allVanishedEnd:
    call hideAll from _call_hideAll_221
    show emptybg at artPos
    $renpy.music.play("audio/windAmbience.mp3", relative_volume=1.5, fadein=1.5, channel="ambient3", loop=True)

    #TK: Dark ambient music in this part? Iron Cthulhu?
    "Silence."
    "It oozed out of the gaps in the rotten floorboards and the cracks in the windows and down through the small holes in the roof."
    "It had been lying in wait there for all those long years, and it could wait no longer."
    "It had nothing to hide now. It had already won."
    "You sat alone in your silent corroding house in an empty forest that had no name."
    "Every day, you barred the windows and stopped up the cracks with plaster and kept your door locked and barred against the vacuum of the corpse-world outside."
    "But still it came, seeping in through the crevices of your home in a slow, crushing flood, pressing in with such force you could barely breathe."
    "The worst was when you tried to sleep."
    "Each night you lay rigid in your bed, listening to the sound of the fire slowly die until there was nothing left to protect you, and you could do nothing but lie in the endless suffocating abyss of silence, unable to even hear your own breathing, until at last you fell asleep and dreamed of silence."
    "The silence was in everything. It penetrated your meat and your bones and soaked deep into your brain. There were deep empty silent chasms in your thoughts. Things you were no longer able to think."
    "You had lived in this house for as long as you could remember, which was three days."
    "There were many beds for you to sleep on. The pantry was fully stocked with food for you to eat. In the closets, you found many outfits to wear, of all shapes and sizes. The shelf in the hall held thirteen small pairs of shoes, and one adult pair."
    "Where did it all come from? Who made the food? Who built the beds? These questions no longer had meaning for you."
    "Whenever you were troubled by such things, you simply shrugged and said:"
    pov "The House provides."
    "Was there ever anything outside this room, and this house? None can say."
    "Did you ever have a name? None can say."
    "You ate from the pantry of the house, and slept on the beds of the house, and wore the clothes of the house. That is all."
    pov "The House provides."
    "Like all other things, your house slowly fell day by day into greater and greater ruin as the vast unstoppable silence of the universe ground it into dirt, piece by piece."
    "Soon the lacuna would be total and all-encompassing. Nothing would be left. Not that you worried about that. You didn't worry about anything, anymore. That was all done with now."
    #TK: Double check this sentence re androids dream of electric sheep
    #"By that time, of course, you would be long dead."
    #"Nothing would be left."
    #TK: Maybe change this line
    #TK: evidence of each disappeared person
    #Some dress-up clothes from the toad
    #A cloak and mask, perhaps some train gear from the thief
    #Soft mud and dirt from the mushroom
    #Tea and herbs and a cauldron / book from the witch, maybe a hat with a pointed brim
    label silence:
        show hand onlayer transient:
            yalign 0.63#0.743
            xalign 0.5
        menu:
            "The soft blur of silence slowly spread through your brain."
            "If you chose to watch the fire, turn to page 481." if not silenceFire:
                $silenceFire = True
                "You watched the soft glow of the dying coals."
                "A memory came to you. You remembered how anxious you used to be."
                "So much grief and fear and pain over this dying earth of yours, and now it was done."
                "There was nothing to fear anymore. The worst had already come to pass."
                "Relief washed over you. The weight of the world lifted from your shoulders."
                "You were at peace."
                "Too late to do anything about it now. Too late for anything."
                "There was rest in the land."
                #"You watched the fire and felt the soft blur of silence slowly spread through your brain."
                #"Were things always this bad? Was it always this hard?"
                #"Didn't there used to be a sun, and a moon?"
                #"Didn't there used to be a lot of things?"
                #"As each day, hour and moment passed, more and more of these questions were slowly erased from your mind. More and more weight was lifted from yours shoulders."
                #"That's when you realised. There never was a time before this one."
                #"There never was anything but this room and the fire, and your hands shaking in front of you, and the silence outside."
                #"It was always this way."
                #"With that thought, a great wash relief came over you. The weight lifted from your shoulders, and you rested in peace."
                jump silence
            "If you explored the attic, turn to page 482." if not silenceAttic:
                $silenceAttic = True
                "One day, you went up to the attic."
                "In the darkness there you found a midnight cloak and a black mask. The pockets held small precious gems and soft, mossy stones."
                "These things belonged to no-one."
                pov "The House provides."
                "That night you slept in warmth, wrapped in the midnight cloak."
                jump silence
            "If you explored the bedrooms, turn to page 482." if not silenceLivingRoom:
                $silenceLivingRoom = True
                "One day, you decided to search the bedrooms."
                "Underneath one of the beds you found a tiny suit, top hat and cane. In the pockets you discovered silver coins and a small decanter of pond scum."
                "These things belonged to no-one."
                pov "The House provides."
                "You had no use for the coins, but you sipped the pond scum when you became thirsty."
                jump silence
            "If you explored the study, turn to page 482." if not silenceStudy:
                $silenceStudy = True
                "One day, you decided to search the study."
                "In the drawers of the desk, you found a black hat with a wide brim and a pointed crown. Underneath the hat were bundles of lavender and herbs and parcels of fine tea."
                "These things belonged to no-one."
                pov "The House provides."
                "You planted the herbs in pots around the house, where they slowly wilted."
                jump silence
            "If you explored the basement, turn to page 482." if not silenceBasement:
                $silenceBasement = True
                "One day, you went down to the basement."
                "Deep in the rich dark soil there, you discovered bottles of red wine, a picnic basket, and packages of truffle cheese and crackers."
                "These things belonged to no-one."
                pov "The House provides."
                "You gathered them up and returned to enjoy the cheese and wine before the fire."
                jump silence
            "If you chose to leave your house, turn to page 482." if not silenceLeave:
                $silenceLeave = True
                #"The silence crushed you on all sides with a terrible and overwhelming pressure, like 10,000 fathoms deep under the ocean."
                #"It felt like a visible, physical force, an endless crushing smothering, the dead world come at last, the silence in your bones, in your meat, even the thoughts in your brain flattened into nothing by it."
                "You had never dared explore the lands outside the house. One day, you decided to try."
                "You gathered them up and reached for the door, but as you took hold of the handle you stopped."
                "You could feel it outside."
                "The howling pressure of the vacuum beyond pressed against the door like a physical force."
                "The weight of it paralysed you. You could not stand the thought of walking down the desolate path to that silent village where no-one lived."
                #"You could feel the presence of them lurking just outside."
                "You had a vision of those empty streets and yawning carcass houses, just outside your door, the fields that no-one tilled, the cavernous schools with no children, the carefully manicured dead lawns and dry river beds and petrified forests stretching on for endless empty acres under a blank sky which held no stars."
                "You fell away from the door, shaking."
                "Better to sit in front of your fire. To keep the silence at bay for a while longer."
                jump silence
            "If you chose to rest and wait, turn to page 483." if silenceFire and silenceLeave:
                "You rested in that house for an uncountable era of time."
                "Time, of course, meant nothing now. Not anymore."
                "All those petty, meaningless little things you needed to do had either been done already, or could never be done."
                "Either way, it was finished. The work was done."
                "I sat and rested there with you."
                "My work, too, was done."
                "There was rest in the land."
                "The fire was warm."
                "Nothing left but to lie by the fire for a while, and wait."
                pov "The House provides."
                "Yes. The House provides."
                jump wolfSilence

    label wolfSilence:
        $halfScreenMenu = True
        menu:
            "Who are you?" if not silenceWho:
                $silenceWho = True
                "It doesn't matter."
                "My name was important a long, long time ago. But you wouldn't recognise it now."
                "I came from an old story. The gods assigned me as a terror to the human race."
                "I was possessed of seven horrors (or, in your tongue you might say \"Auras\" or \"Glamours of terrible splendour\") which lay upon me like seven cloaks."
                "My face was a single coiling line, like the entrails of men and beasts, from which omens can be read."
                "I never knew a mother or father. I was born of the mountain."
                "I guarded the forests. My breath was fire. My gaze was death. Who would dare stand against me?"
                "Long time ago now."
                "Barely remember those days. No-one does."
                #"Around those first campfires, they whispered of me, and I awoke in the darkness."
                #"The first monster."
                "Fragments of me survived. I clung to life in old stories like this one."
                "The beast in the forest. The wolf at the door."
                "You know."
                jump wolfSilence
            "What happened to my friends?" if not silenceFriends:
                $silenceFriends = True
                "I'm sorry, child. You had the misfortune of coming in at the end of things."
                "Each of them read my book, and struck a bargain with me. To live here, in this story, in the life of their dreams."
                "Do not think I was unkind. I kept my deal. Each of them lived here for almost a hundred years or more."
                "But nothing lasts forever. Sooner or later, their debt had to be paid. The deal came due."
                "They are forgotten now. As both of us soon will be."
                "This is the curse you have been born with. To witness the end."
                "It had to happen to someone."
                jump wolfSilence
            "You must have tricked them." if silenceFriends and not silenceTrick:
                $silenceTrick = True
                "No, child. There was no trick."
                "Here, in my story, they got the life they always wanted to live."
                "Wise, brave, cunning and kind. The best version of themselves. Happy endings, great adventures. All of it."
                "Real life, of course, was never so kind."
                #"In your world their lives would have been short."
                "The world they were born into was not a good place for them."
                "As I suspect it is not a good place for you."
                "I offered them another world."
                "Of course, in time, they would disappear. Nothing lasts forever. They knew that when they took the deal. "
                jump wolfSilence
            "Are you going to eat me?" if not silenceEat:
                $silenceEat = True
                "Yes, child."
                "Everyone is eaten by something. The only choice that any human being ever has, is to decide what it will be."
                "But not yet."
                "We can rest here a little while longer."
                jump wolfSilence
            "I am done resting." if not silenceRest:
                $silenceRest = True
                "Very well."
                "I will make you my offer."
                "Come. Join me in this book. Help me rejuvenate this tired story."
                "You will live in the village. I will lurk in the forests."
                "I will be cunning. But you will be brave."
                "You will rise against me. Our battle will be the stuff of legends."
                "You will defeat me. And everyone will live happily ever after."
                "It's everything you've dreamed of."
                jump wolfSilence
            "But... you're evil." if silenceRest and not silenceEvil:
                $silenceEvil = True
                "Yes. Thank you."
                "I have spent my life honouring the old ways. Preserving the old kind of evil."
                "Beautiful and terrible. Mystery and horror. Ruthless, captivating. A dark fire."
                "The type of evil you can't get in your world."
                "The evil in your world is a grey, endless fog that soaks into every particle of your being like mould."
                "You can't even see it. Like a fish can't see water. It surrounds you. Every day you wake up and breathe it in."
                "It has been built into every fibre of the human machine."
                "No one individual human can stop it. You can't even understand the scope of it."
                "I offer you a better evil."
                "Something that can be defeated with a single act of human courage."
                "Isn't that what you all want?"
                jump wolfSilence
            "Will I be alone?" if silenceRest and not silenceAlone:
                $silenceAlone = True
                "No. Don't worry. We will find others."
                "This story will be full of life again, soon."
                jump wolfSilence
            "I accept your bargain. I will live here in this story for the rest of my days." if silenceRest:
                "Thank you, my friend. You have done more for me than you can know."
                "I hope that this can be a good home for you. You will be safe here for a hundred years, or more."
                jump wolfEnd
            "No. I won't do it." if silenceRest and not silenceNo:
                $silenceNo = True
                "I'm sorry, my friend. It's a bit too late for that."
                "We have grown weak, in here. The souls have all run dry."
                "Either you give yourself up, or we will die."
                jump wolfSilence
            "I still won't do it." if silenceNo:
                "It seems you still don't understand."
                "The only choices you ever had here are the ones I gave you."
                $halfScreenMenu = False
                menu:
                    "Do you see now?"
                    "I understand.":
                        "Good."
                    "I understand.":
                        "Good."
                    "I understand.":
                        "Good."
                    "I understand.":
                        "Good."
                    "I understand.":
                        "Good."
                    "I understand.":
                        "Good."
                    "I understand.":
                        "Good."

                "I enjoyed our conversation. If you can call it that."
                "Of course, you could only ask the questions I gave you to ask. I hope they were enough."
                "Time to finish things."

                menu:
                    "Will you take my bargain, and live in this story for the rest of your days?"
                    "I will.":
                        "Good."
                    "I will.":
                        "Good."
                    "I will.":
                        "Good."
                    "I will.":
                        "Good."
                    "I will.":
                        "Good."
                    "I will.":
                        "Good."

                jump wolfEnd
    # The wolf talks to you. The book has run out of souls. They've all been consumed.
    # You must give your soul to the book in order to keep it going.
    # First, you will take the book and leave it in the library, for another soul to read.
    # Then, you will live in the book forever.
    # Over, and over, and over again.
    # POV but you'll consume me.
    # Yes. But you will always be consumed by something.
    # That is what living is, in the world that you have built for yourselves outside this story.
    # Your only choice you get to make, in the end, is what you will be consumed by.
    # Come now. Give your soul over to me.

#The ending when you choose to go with the wolf, leading to newStoryFinale
label wolfEnd:
    "You have made the right choice."
    "Hold my hand in yours, and we will not fear what hands like ours can do."
    "Now we must choose your title."
    $halfScreenMenu = False
    $wolfMenu = False
    $fullScreenMenu = True
    $burnMenu = True
    call hideAll from _call_hideAll_120
    show text "What role would you like to play?":
        xalign 0.5
        ypos 125
    show hand:
        yalign 0.22#0.743
        xalign 0.5

    menu:
        "If you chose The Cobbler, turn to page 465.":
            $persistent.finaleTitle = "Cobbler"
        "If you chose The Trickster, turn to page 466.":
            $persistent.finaleTitle = "Trickster"
        "If you chose The Crow, turn to page 467.":
            $persistent.finaleTitle = "Crow"
        "If you chose The Specter, turn to page 468.":
            $persistent.finaleTitle = "Specter"
        "If you chose The Winter Rose, turn to page 469.":
            $persistent.finaleTitle = "Winter Rose"
        "If you chose The Fool, turn to page 470.":
            $persistent.finaleTitle = "Fool"
        "If you chose The Water Nixie, turn to page 471.":
            $persistent.finaleTitle = "Water Nixie"
        "If you chose The Giant, turn to page 472.":
            $persistent.finaleTitle = "Giant"
        "If you chose The Bushranger, turn to page 473.":
            $persistent.finaleTitle = "Bushranger"
        "If you chose The Butcher, turn to page 474.":
            $persistent.finaleTitle = "Butcher"
        "If you chose The Aristocrat, turn to page 475.":
            $persistent.finaleTitle = "Aristocrat"
        "If you chose The Warrior-Poet, turn to page 476.":
            $persistent.finaleTitle = "Warrior-Poet"
        "If you chose The Heirophant, turn to page 477.":
            $persistent.finaleTitle = "Heirophant"
    call hideAll from _call_hideAll_121
    show emptybg at artPos
    $fullScreenMenu = False
    $halfScreenMenu = True
    "Thank you, my child."
    "That was the end."
    "You finally turned the last page and closed the book."
    "A sense of peace and satisfaction filled you."
    "It was the perfect ending."
    "You sat there for many hours, thinking over what you had read. Then, you picked up the book, and walked to the library."
    "You placed it there on the returns shelf. Ready for another reader."
    "As your hand left the pages, there was a shivering in the air, and you disappeared."
    "Never to be seen again in the world of men."
    "There was a calmness. The silence slowly abated."
    "The book sat on the shelf, and waited."
    show white onlayer over_screens zorder 101:
        alpha 0.0
        linear 15.0 alpha 1.0
    $renpy.music.set_volume(0, delay=10.0, channel=u'ambient1')
    $renpy.music.set_volume(0, delay=10.0, channel=u'ambient2')
    $renpy.music.set_volume(0, delay=10.0, channel=u'music')
    play audio whiteNoise
    #TK: Look at slightly changing xpos as well as the ypos for these
    show wolf8 onlayer transient zorder 100
    "And then there was rest in the land."
    play audio pageFlip volume 0.8
    show wolf4 onlayer transient zorder 100
    "{space=5}And then there was rest in the land."
    play audio pageFlip2 volume 0.6
    show wolf3 onlayer transient zorder 100
    "\n{vspace=6}{space=11}And then there was rest in the land."
    play audio pageFlip3 volume 0.5
    show wolf8 onlayer transient zorder 100
    "{vspace=2}{space=8}And then there was rest in the land."
    play audio pageFlip2 volume 0.4
    show wolf9 onlayer transient zorder 100
    "\n\n{vspace=10}{space=15}And then there was rest in the land."
    play audio pageFlip volume 0.3
    show wolf10 onlayer transient zorder 100
    "\n{space=6}And then there was rest in the land."
    play audio pageFlip3 volume 0.2
    show wolf11 onlayer transient zorder 100
    "\n\n\n{vspace=5}{space=20}And then there was rest in the land."
    play audio pageFlip2 volume 0.1
    show wolf12 onlayer transient zorder 100
    "{vspace=12}{space=9}And then there was rest in the land."
    $persistent.bookEnd = True
    #$purge_saves()
    $renpy.quit()


#         "Do not ask lightly of the northern forest, my child."
#         "That was a cursed place where wicked sprites and gleeful ghosts held sway. All who lived there slept uneasily in their beds as they heard the Goblin Train rattle past their windows each night."
#         show thief onlayer transient zorder 100
#         "The worst of them all was the Master Thief, a dextrous and sinister figure who was said to have all manner of powers."
#         "It was said on moonless nights their long, long arms would stretch through your window and up your stairs and into your bedroom and steal your dreams right out from under your pillow. In a single motion their long, long legs would carry them away to a secret hideout where they would place your forgotten thoughts in a sack of mysterious things, never to be seen again."
#         "No jail could hold them and no lock could bar them entry."
#         "Or so it was said."
#         if persistent.vanished >=3:
#             call musicSilence from _call_musicSilence_4
#         jump neighbours
# "To learn about the lands to the east, turn to page 15." if not introNeighboursE:
#     play sound pageFlip
#     $introNeighboursE = True
#     hide map1 onlayer screens
#     $renpy.hide_screen(tag="map")
#     if persistent.toadVanished == True:
#         call musicSilence from _call_musicSilence_5
#         show wolf8 onlayer transient zorder 100
#         "To the east, there was nothing and no-one."
#         if persistent.vanished <=2:
#             call musicReturn from _call_musicReturn_2
#         jump neighbours
#     else:
#         #Coastal swamps and mangroves to the east, leading to the beach and the ocean - The Toad
#         if persistent.vanished >=3:
#             call musicReturn from _call_musicReturn_3
#         "To the east, the river flowed down to the coast. The mangrove trees swayed in the summer heat, and the air thrummed with chanting in honour of the insect god, Karnopticon."
#         show toad onlayer transient zorder 100
#         "On the edge of the swamp was a grand manor, owned by a noble frog lord."
#         "He was rarely seen, but people whispered that he was wiser than Solomon and richer than Midas. Kings and prophets would come from across the land to seek his counsel and gaze with envy upon the glittering spires of his house. To buy even a single gem from amoung the hundreds that adorned the manor would bankrupt any one of them."
#         "Or so it was said."
#         if persistent.vanished >=3:
#             call musicSilence from _call_musicSilence_6
#         jump neighbours
# "To learn about the lands to the south, turn to page 20." if not introNeighboursS:
#     play sound pageFlip
#     $introNeighboursS = True
#     hide map1 onlayer screens
#     $renpy.hide_screen(tag="map")
#     #Flowing river to the south, Amazonian, fungi and silver-white - The Mushroom
#     if persistent.mushroomVanished == True:
#         call musicSilence from _call_musicSilence_7
#         show wolf10 onlayer transient zorder 100
#         "To the south, there was nothing and no-one."
#         if persistent.vanished <=2:
#             call musicReturn from _call_musicReturn_4
#         jump neighbours
#     else:
#         show mushroom onlayer transient zorder 100
#         if persistent.vanished >=3:
#             call musicReturn from _call_musicReturn_5
#         "Ah! In fact, the south river and the forest around it was watched over by a wise mushroom ambassador, who had owned these lands since before anyone could remember."
#         "On cold clear nights, you could see her walking through the depths of the forest with her white veil and delicate waves of silver spores drifting behind her."
#         "She allowed your family to live on the river and use her lands, under one condition."
#         m "Ask not of what concerns you not, lest you hear what pleases you not."
#         "Your family accepted her wishes, and so you let each other be."
#         "She was often away brokering trade agreements and peace treaties and delicate alliances between the many trees and plants and old warring ferns of the forest."
#         "Or so it was said."
#         if persistent.vanished >=3:
#             call musicSilence from _call_musicSilence_8
#         jump neighbours
# "To learn about the lands to the west, turn to page 26." if not introNeighboursW:
#     play sound pageFlip
#     $introNeighboursW = True
#     hide map1 onlayer screens
#     $renpy.hide_screen(tag="map")
#     #Mountains to the West, home to devils and witch's sabbaths - Thornton Peak- The Witch
#     if persistent.witchVanished == True:
#         call musicSilence from _call_musicSilence_9
#         show wolf11 onlayer transient zorder 100
#         "To the west, there was nothing and no-one."
#         if persistent.vanished <=2:
#             call musicReturn from _call_musicReturn_6
#         jump neighbours
#     else:
#         show witch onlayer transient zorder 100
#         if persistent.vanished >=3:
#             call musicReturn from _call_musicReturn_7
#         "None dared venture to the western mountains, for all the lands around it were said to be home to a terrible witch."
#         "Her hut lay deep under a secret lake, and she would emerge on moonless nights when the waters of that lake turned still and silver-green."
#         "The witches held their Sabbath on the mountain to the east, and when the sky was clear you could see the peak blaze with fire, and the Destroyer himself would emerge to dance in the firelight."
#         "Or so it was said."
#         if persistent.vanished >=3:




#Ending where you choose to live in the book forever
label newStoryFinale:
    #show screen on_key_screen
    play sound pageFlip
    #The game goes into the beginning of the story right away (no load / start game):
    if persistent.povname == "alex" or persistent.povname =="Alex" or persistent.povname =="Alexandra" or persistent.povname =="alexandra" or persistent.povname =="Alexander" or persistent.povname =="alexander" or persistent.povname =="Alexis" or persistent.povname =="alexis":
        "At last. Welcome, Georgia."
    else:
        "At last. Welcome, Alex."
    "This maybe happened, or maybe did not."
    "The time is long past, and much is forgot."
    "Back in the old days, when wishing worked, you lived in a lovely cottage on the edge of a magical forest."
    "Many strange figures lived in the woods around your house."
    if persistent.thiefVanished == False:
        "To the north lived a cunning thief, in a cursed place where wicked sprites and gleeful ghosts held sway. All who lived there slept uneasily in their beds as they heard the Goblin Train rattle past their windows each night."
        "It was said on moonless nights their long, long arms would stretch through your window and up your stairs and into your bedroom and steal your dreams right out from under your pillow. In a single motion their long, long legs would carry them away to a secret hideout where they would place your forgotten thoughts in a sack of mysterious things, never to be seen again."
        "No jail could hold them and no lock could bar them entry."
        "Or so it was said."

    else:
        if persistent.name1Rand == 1:
            "To the north lived a wicked Imp."
        elif persistent.name1Rand == 2:
            "To the north there were rumours of a legendary pair of winged boots, which often spoke to offer advice to lost travellers along those roads."
        elif persistent.name1Rand == 3:
            "To the north was a terrible Frost that lay upon the land like a curse."
        elif persistent.name1Rand == 4:
            "To the north lived a wild Goat that knew no master, and caused havoc and woe to all who crossed its path."
        elif persistent.name1Rand == 5:
            "To the north lived a debaucherous Fiend whose laugh was like thunder."
        elif persistent.name1Rand == 6:
            "To the north lived a gallant Rake who threw wild parties at all hours of the day and night."
    if persistent.witchVanished == False:
        "To the east, a cackling witch would hold her Sabbath on the mountain. When the sky was clear you could see the peak blaze with fire, and the Destroyer himself would emerge to dance in the firelight."
        "Her hut lay deep under a secret lake, and she would emerge on moonless nights when the waters of that lake turned still and silver-green."
    else:
        if persistent.name2Rand == 1:
            "To the east, a kindly Midwife."
        elif persistent.name2Rand == 2:
            "To the east, the Moon itself had a secret hiding-place, known to no-one."
        elif persistent.name2Rand == 3:
            "To the east, a Mountain towered over the land, and was often heard to rumble in ominous tones."
        elif persistent.name2Rand == 4:
            "To the east, a crooked Pumpkin was said to hold court over the legions of the dead."
        elif persistent.name2Rand == 5:
            "To the east, a Tyrant ruled with an iron fist, and all shuddered to hear his name said aloud."
        elif persistent.name2Rand == 6:
            "To the east, a kindly Toymaker lived in a curious little shop with no name."
    if persistent.toadVanished == False:
        "To the south, a haughty toad, who lived in a grand manor on the edge of the swamp."
        "He was rarely seen, but people whispered that he was wiser than Solomon and richer than Midas. Kings and prophets would come from across the land to seek his counsel and gaze with envy upon the glittering spires of his house. To buy even a single gem from amoung the hundreds that adorned the manor would bankrupt any one of them."
    else:
        if persistent.name3Rand == 1:
            "To the south was a wandering Beggar with no hands, who was said to know all the languages of the world."
        elif persistent.name3Rand == 2:
            "To the south was a crooked Crone who was often heard shrieking at midnight."
        elif persistent.name3Rand == 3:
            "To the south was the Firebird itself, which was too bright to look upon."
        elif persistent.name3Rand == 4:
            "To the south was a mystical Sausage which (it was said) could grant any wish."
        elif persistent.name3Rand == 5:
            "To the south was a humble Shepherd who guarded a flock of grey clouds."
        elif persistent.name3Rand == 6:
            "To the south was a gnarled old Baker who (it was said) would bake up a gingerbread child for any couple that asked."

    if persistent.mushroomVanished == False:
        "To the west, a wise mushroom ambassador, who had owned these lands since before anyone could remember."
        "She was often away brokering trade agreements and peace treaties and delicate alliances between the many trees and plants and old warring ferns of the forest."
    else:
        if persistent.name4Rand == 1:
            "To the west, a pack of thieving Swans who were a terror upon the countryside."
        elif persistent.name4Rand == 2:
            "To the west, a hideous Blindworm that lurked deep within the earth."
        elif persistent.name4Rand == 3:
            "To the west, a magnificent Castle where the streets were paved with gold and the rivers ran with dark red wine."
        elif persistent.name4Rand == 4:
            "To the west, there were rumours of an enchanted Glass Coffin with a mysterious shadow trapped within."
        elif persistent.name4Rand == 5:
            "To the west, travellers spoke of a strange Singing Bone that could be heard on moonless nights."
        elif persistent.name4Rand == 6:
            "To the west, travellers whispered that a miraculous bushel of Snake Leaves could be found, with the power to revive the dead."

    #(This next bit alters depending on which character you chose):
    if persistent.finaleTitle == "Cobbler":
        "There were even rumours of a humble Cobbler in the heart of the woods, making [his] living repairing the shoes of these strange and mythical figures."
    elif persistent.finaleTitle == "Trickster":
        "Worst of all were the rumours of a sly Trickster who swindled [his] way across the country, duping innocent men and women out of their honest coin."
    elif persistent.finaleTitle == "Crow":
        "Worst of all was a sinister Crow that haunted you day and night, cawing as it lurked above your mantle."
    elif persistent.finaleTitle == "Specter":
        "Worst of all was the sight of a haunting Spectre that could sometimes be seen in the fog, beckoning with a pale hand."
    elif persistent.finaleTitle == "Winter Rose":
        "There were even rumours of a blinding beauty deep in the forest, who bloomed like a winter rose."
    elif persistent.finaleTitle == "Fool":
        "There were even rumours of a terrible Fool deep in the forest, who travelled the highways and byways freely without a single thought in [his] head."
    elif persistent.finaleTitle == "Water Nixie":
        "Worst of all were the rumours of a Water Nixie that lurked deep in the lakes of the forest, dragging unwary travellers to [his] drowned kingdom below."
    elif persistent.finaleTitle == "Giant":
        "Worst of all were the rumours of a fell Giant who slumbered under the hills, shaking the earth with [his] snores each night."
    elif persistent.finaleTitle == "Bushranger":
        "Worst of all were the rumours of a dastardly bushranger who plagued the roads, stealing everything [he] could and causing havoc left and right."
    elif persistent.finaleTitle == "Butcher":
        "There were even rumours of a humble Butcher who plied [his] wares in a small red shop deep in the forest. So delicious were [his] wares that travellers would flock there day and night for a bite to eat, though none could say where [he] sourced [his] intoxicating meats."
    elif persistent.finaleTitle == "Aristocrat":
        "There were even rumours of an exiled Aristocrat who ruled over a lost kingdom, deep in the woods where no-one had ever returned from alive."
    elif persistent.finaleTitle == "Warrior-Poet":
        "There were even rumours of a bold Warrior-Poet from a faraway land who roamed through the forest, trying to live a peaceful life."
    elif persistent.finaleTitle == "Heirophant":
        "There were even rumours of a noble Heirophant who lived in quiet prayer deep in the forest."
    "Despite [his] strange nature, folks said they sometimes heard this [persistent.finaleTitle] whistling a merry tune late into the night."
    if he == "they":
        "Were they happy?"
    else:
        "Was [he] happy?"
    "Well, who can say. I like to think so."
    if persistent.finaleTitle == "Crow":
        "One day, the endless cawing grew too much for you to bear. You packed your belongings into a knapsack, and walked into the forest."
    else:
        "One day, you resolved to meet these mysterious figures for yourself. You packed your belongings into a knapsack, and walked into the forest."
    "\"Be careful!\" Your mother cried after you. But you had resolved to take this path, no matter the danger."
    show black:
        alpha 0.0
        linear 15.0 alpha 1.0

    "As you strode into the darkness of the forest, the twilight set in."
    "The crickets and cicadas all around began their chattering and squabbling, and the evening birds began to laugh and trill, and the wet cool mist of the rainforest settled around you."
    "The crooked old water-dragons looked sideways at you and plotted their long, slow schemes."
    "A small turtle saw you coming and fled into the water with a splash."
    "The road was long, and the forest was dark, but a smile broke out on your face."
    "You were home."
    $purge_saves()
    $persistent.continueButton = False
    #pause (10.0)
    #TK: Include this text saying true ending? or not?
    # show text "{color=#FFFFFF}True Ending.{/color}" with fade:
    #     xalign 0.5
    #     yalign 0.5
    # ""
    scene black with fade
    show text "{color=#FFFFFF}A game by Jack McNamee.{/color}" with fade:
        xalign 0.5
        yalign 0.5
    $achievement.grant("THE_END")
    "."
    show text "{color=#FFFFFF}Thank you so much for playing.{/color}" with fade:
        xalign 0.5
        yalign 0.5

    ""
    show text "{color=#FFFFFF}I hope you enjoyed the game, and I hope you have a wonderful life.{/color}" with fade:
        xalign 0.5
        yalign 0.5
    ""
    $renpy.music.set_volume(0, delay=5.0, channel=u'ambient1')
    $renpy.music.set_volume(0, delay=5.0, channel=u'ambient2')
    $renpy.music.set_volume(0, delay=5.0, channel=u'music')
    #hide text with fade
    #scene black with fade
    pause (5.0)
    $renpy.quit()

label burnBegins:
    show screen countdown
    $ time = 58         #Note: 8 = Roughly 2 minutes #60
    $ timer_jump = 'burnEnd'
    show bookBurnMovie at fullPos onlayer over_screens zorder 98
    return

#Ending where you burn the book.
label bookBurnedFinale:
    $halfScreenMenu = False
    $wolfMenu = True
    $fullScreenMenu = False
    $burnMenu = True
    "Time to finish things."
    "Just hold the book over the fire."
    #pause 0.2 with hpunch
    #TK: Walking and fire noises."
    play sound fireLit
    call hideAll from _call_hideAll_222
    show nightbg at artPos with flash

    #play music rememberVocalFull
    "Good. It's done."
    "The flames have started to catch. Won't be long now."
    "I'll take you back to the village."
    "You won't have much time left. You should choose who you want to spend it with."
    $renpy.music.play("audio/rememberCleanVocalFull.wav", channel="music", fadein=5.0, loop=False)

    play sound pageFlip
    #Disables the quick menu
    #$ quick_menu = False

    #Disables the escape key, so you can't access the main menu at this point
    #$ _game_menu_screen = None
    $ config.rollback_enabled = False
    show screen countdownCall
    $ time = 30         #Note: 8 = Roughly 2 minutes
    $ timer_call = 'burnBegins'

    #The book has been burned - if you quit and re-enter the game at this point you will find yourself in just the burned out ending
    $persistent.bookBurned = True
    label villageBurning:
        show hand onlayer transient:
            yalign 0.7#0.743
            xalign 0.5
        call hideAll from _call_hideAll_122
        show towncrossroadsbg at artPos

        menu:
            "You stood in the middle of the village square. The smell of smoke was in the air."
            "If you walked to the banquet, turn to page 64.":
                jump banquetBurning
            "If you walked to the edge of town, turn to page 70.":
                jump townBurning
            "If you walked back home, turn to page 1." if not mumBurning:
                jump homeBurning
            # "If you walked into the space between the trees, turn to page 43." if not finalWolfTalk:
            #     call hideall
            #     show forest4bg at artPos
            #     "You wandered into the forest. The night was cool."
            #     "Where are you going, child? Time grows short."
            #     show hand onlayer transient:
            #         yalign 0.7#0.743
            #         xalign 0.5
            #     menu:
            #         "You should spend this moment with the ones you love."
            #         "I wanted to talk to you.":
            #             "To me? I'm the one you want to spend time with?"
            #             "I don't know what to say. Thank you. But I have nothing left to tell."
                        
            #             show hand onlayer transient:
            #                 yalign 0.7#0.743
            #                 xalign 0.5
            #             menu:
            #                 "My tale is done. My voice is spent."
            #                 "How much time do we have left?":
            #                     "How long does a building stand before it falls?\nHow long does a contract last? How long will brothers\nshare the inheritance before they quarrel?\nHow long does hatred, for that matter, last?"
            #                     "Time after time the river has risen and flooded.\nThe insect leaves the cocoon to live but a minute.\nFrom the very beginning nothing at all has lasted."
            #                     "The river rises, flows over its banks\nand carries us all away, like mayflies\nfloating downstream: they stare at the sun,\nthen all at once there is nothing."
            #                     "Goodbye, child."
            #                     "I'm glad I met you."
            #                     "Go on. Spend this moment in music and laughter. These woods are no place for you."
            #                     jump village

    # Gilgamesh Scene:
    #     "Humans are born, they live, then they die, this is the order that the gods have decreed."
    #     "But until the end comes, enjoy your life, spend it in happiness, not despair."
    #     "Savour your food, make each of your days a delight, bathe and anoint yourself, wear bright clothes that are sparkling clean, let music and dancing fill your house, love the child who holds you by the hand, and give your lover pleasure in your embrace."
    #     "That is the best way for a man to live."

    # Humbaba Scene:
        #  The river rises, flows over its banks
        # and carries us all away, like mayflies
        # floating downstream; they stare at the sun,
        # then all at once there is nothing.”

    label banquetBurning:

        call hideAll from _call_hideAll_123
        show townfeastbg at artPos
        "The banquet was laid out down by the river. Everyone sat along thick tables piled with every type of food, drinking and waving their arms and talking with their mouths full."
        label banquetBurningMenu:
            call hideAll from _call_hideAll_223
            show townfeastbg at artPos
            show hand onlayer transient:
                yalign 0.621#0.743
                xalign 0.5
            menu:
                "You looked out over the scene."
                "If you sat next to the toad, turn to page 375." if not persistent.toadVanished and not toadBurning:
                    #call hideAll
                    #show manorbg at artPos
                    "The toad was almost submerged in a giant margarita glass, flicking his tongue out to grab every prawn and strawberry and piece of roast beef he could get."
                    f "Ah, my old friend! You absolutely MUST try the potato bake! We should burn down the world more often (if it grants us delectable morsels such as these ones), ha ha!"
                    label toadBurning:
                        show hand onlayer transient:
                            yalign 0.686#0.743
                            xalign 0.5
                        menu:
                            "The crow-shrike, rat, bat and the old black cockatoo were gathered around with their feet on the table, helping themselves to the feast."
                            "If you looked at the manor in the distance, turn to page 378." if not bcBurning:
                                call hideAll from _call_hideAll_224
                                show manorextbg at artPos
                                "In the distance across the river, you could see Brildebrogue Chippingham's manor, lit up and glowing like a last sunset."
                                pov "Do you want to go over there? Take him down a peg?"
                                f "No. No, it's time to forget him."
                                f "He... was my brother. Back when I was alive. That's what he represented, I mean."
                                f "I let him poison my entire time here. Even in the world of my dreams. I could have been doing anything, and I spent all my days just acting out these ridiculous stories where I finally show him."
                                f "What a waste. He must have been dead for a hundred years by now."
                                f "This is our time. We should spend it with the people we care about."
                                $bcBurning = True
                                jump toadBurning
                            "If you talked to the toad, turn to page 390." if not toadBurning:
                                $toadBurning = True
                                "You talked for hours, going over trivialities like old friends as you sampled the feast. As dessert arrived, the toad grew somber."
                                f "I have to admit, friend... the end scares me."
                                f "I've been in here for a long, long time. Longer than any human should live."
                                f "Perhaps I should have done this a long time ago. I-I was never good at saying goodbye."
                                pov "Then let's not. Let's just enjoy this time together."
                                f "...That sounds nice."
                                "He slowly smiled, and leaned over to rest on your arm. The two of you watched the bat, the rat and the black cockatoo play cards in the light of the fire."
                                jump toadBurning
                            "If you listened to the carriage-carriers, turn to page 381." if not batBurning:
                                crowshrike "Well lads, I have to say, it's been a good run."
                                bat "Too right."
                                cockatoo "It's been a pleasure riding with ya, boys. I... I couldn't have asked for a better crew."
                                rat "Oh, ya big softy. Now yer gonna make me cry."
                                cockatoo "Bring it in lads. I love you all."
                                "They embraced in the flickering light of the flames."
                                f "So, I suppose this means that ah, under the circumstances, the bill is better left forgotten -"
                                cockatoo "Don't push it, mate."
                                $batBurning = True
                                jump toadBurning
                            "If you stood up from your seat, return to page 64.":
                                jump banquetBurning
                    jump banquetBurningMenu
                "If you explored the river, turn to page 382." if persistent.toadVanished and not toadBurning:
                    "You walked out along the banks of the river until you found a small, muddy hole."
                    "Inside the hole you found a tiny suit, top hat and cane. Silver coins and a small decanter of pond scum were hidden away within the pockets."
                    "Who did these things belong to? You found you couldn't recall."
                    "You took the coins and commissioned a great stone slab with ornate angels engraved upon it, in pride of place at the top of the cemetery."
                    "You buried the suit, hat and cane beneath the slab. You had no name to place upon it. But for some reason, it felt right."
                    $toadBurning = True
                    jump banquetBurningMenu
                "If you sat next to the mushroom, turn to page 397." if not persistent.mushroomVanished and not mushroomBurning:
                    "The mushroom was enjoying a glass of wine while exchanging witty anecdotes with the plants and fungi of the forest, who were all gathered around the banquet table."
                    label mushroomBurning:
                        show hand onlayer transient:
                            yalign 0.645#0.743
                            xalign 0.5
                        menu:
                            "They all laughed together at some inside joke."
                            "If you talked to the mushroom, turn to page 364." if not mushroomBurning:
                                m "Cheers, darling!"
                                "She lifted her wineglass and motioned the others at the table to join her in a toast."
                                m2 "To [povname]!"
                                town "[povname]!"
                                "Everyone erupted in whooping cheers, and wine sloshed over the table as the glasses rose up."
                                m3 "Wonderful job, really, absolutely fabulous work."
                                pov "I'm sorry that this all had to burn-"
                                m3 "Oh, no, no, please don't go away feeling guilty about all this. It was the only option, really, this sad charade has gone on far too long already."
                                m "I've been waiting for this moment for a long time."
                                m2 "Now, come on. How about a song?"
                                "The mushroom led you and the rest of the town in a deafening rendition of \"La Vi en Rose\" that rang out into the night, drowning out the sounds of the fire."
                                $mushroomBurning = True
                                jump mushroomBurning
                            "If you talked to Scraggs Mckenzie and the Boys, turn to page 374." if not scraggsBurning:
                                #Check if you have interacted with the SOM
                                sc "That's right, I'm back! Scraggs McKenzie, the baddest banksia in the bush!"
                                "The bounty hunter was sitting with his boots up on the table, his boys around him."
                                pov "Have we met?"
                                sc "You know... Scraggs! You know me, right?"
                                boys "Of course [he] do, boss! Everyone knows you. [Hes] just tryna put you off your game!"
                                sc "Come on boys, I think it's time for another musical number."
                                pov "Oh no, that's fine -"
                                "Scraggs and company launched into a long, flashy musical number explaining what they'd been doing this whole story while you were on your own adventures."
                                boys "-so that's why we're the toughest... that's why we're the gruffest... that's why we're the roughest, gang in tooooooown!"
                                sc "That's right!"
                                "You and the rest of the town applauded."
                                $scraggsBurning = True
                                jump mushroomBurning
                            "If you talked to the strange and crooked old man, turn to page 372." if not somBurning:
                                #Check if you have interacted with the SOM
                                som "Bet you don't remember me, do you?"
                                pov "Um-"
                                som "I come from the future! In my world, everyone is as crooked as I! We dance our crooked dances and sing crooked songs, long into the night."
                                som "Enjoy yourself in the real world, friend, but know that the crooked ways will come upon you too! It's just a matter of time... twisted, broken time..."
                                "He cackled in his sinister way as you slowly slid away from him."
                                $somBurning = True
                                jump mushroomBurning
                            "If you stood up from your seat, return to page 64.":
                                jump banquetBurning
                    jump banquetBurningMenu
                "If you searched for an old fig, turn to page 376." if persistent.mushroomVanished and not mushroomBurning:
                    call hideAll from _call_hideAll_225
                    show stranglerfigbg at artPos
                    "You wandered away from the party, searching through the forest until you found an old strangler fig rotting away."
                    "In its depths you discovered bottles of red wine, a picnic basket, and packages of truffle cheese and crackers."
                    "You took these things and enjoyed them with your friends in the village. You poured the wine, and raised a toast."
                    "You had no name to dedicate the toast to. But for some reason, it felt right."
                    #TK perhaps extra from toad, witch, thief in reaction to this
                    $mushroomBurning = True
                    jump banquetBurningMenu
                "If you talked to the mayor, turn to page 377." if not persistent.mayVanished and not mayBurning:
                    "The mayor was twisting slowly in the moonlight."
                    may "This is goodbye, then. I'm sorry we didn't get more pages together."
                    may "I have heard his song at last. Just like my mother and my sister before me."
                    may "Moon-Head."
                    "A slight sound echoed on the breeze. Like laughter."
                    may "I belong with his congregation. Now that the story is done, I can go up there and dance forever in the moon-mad twilight."
                    may "You've done a lot for all of us. I hope we've all brought you a little joy."
                    "The clouds covered the moon for but an instant. When the light shone again, he was gone."
                    $mayBurning = True
                    jump banquetBurningMenu
                "If you talked to the pigs, turn to page 352." if not persistent.pigsVanished and not pigsBurning:
                    "You came upon the pigs enjoying a game of poker."
                    p1 "Greetings! Care to join us?"
                    p2 "Don't do it, kid. He'll rob you blind with those devil's cards of his."
                    p3 "No harm in it now, Montgomery. You can't take it with you."
                    "You settled down to play and in a blink you had gambled away your life's savings."
                    "(Don't worry. You have no need for them anymore.)"
                    p1 "We have crossed paths a few times, haven't we? I hope you've enjoyed our little interactions."
                    "The pigs looked out at the horizon as the slow line of fire crept inward."
                    p3 "Another fragile domicile."
                    p2 "We'd better make it of stronger stuff next time."
                    p1 "Yes."
                    p1 "Next time, brothers. I promise I will grant you that perfect, everlasting {color=#0000ffff}House{/color}."
                    $pigsBurning = True
                    jump banquetBurningMenu
                "If you looked down the well, turn to page 351."if not persistent.wellVanished and not wellBurning:
                    well "Evening. Got any smokes?"
                    pov "A packet of cigarettes appeared in my hand."
                    "A packet of cigarettes appeared in your hand, and you tossed them down the well."
                    well "Cheers. You have a good one, alright? Take care."
                    $wellBurning = True
                    jump banquetBurningMenu
                "If you returned to the village square, return to page 50.":
                    "You turned and walked back to the centre of the village."
                    jump villageBurning
                #The Gutterlings
    label townBurning:
        call hideAll from _call_hideAll_124
        show townextbg at artPos
        if persistent.starsVanished:
            "You walked out to the edge of town. The blank night sky was beautiful to behold. You heard dancing and laughter on the wind."
        else:
            "You walked out to the edge of town. The stars in the night sky were beautiful to behold. You heard dancing and laughter on the wind."
        label townBurningMenu:
            call hideAll from _call_hideAll_226
            show townextbg at artPos
            show hand onlayer transient:
                yalign 0.62#0.743
                xalign 0.5
            menu:
                "Fruit bats chirped and swirled overhead."
                "If you went out to the goblin train, go to page 53." if not persistent.thiefVanished and not thiefBurning:
                    "The goblin train chuffed as it wound its way through the houses in a lazy circuit around town."
                    "You waited until it was close, then leapt aboard."
                    "Lush goblin fruits were laid out all across the carriage, and a wild goblin riot was in progress."
                    label trainBurning:
                        call hideAll from _call_hideAll_227
                        show goblinintbg at artPos
                        show hand onlayer transient:
                            yalign 0.66#0.743
                            xalign 0.5
                        menu:
                            "The goblins cavorted and gambled and ate and drank in a chaos of forms."
                            "If you joined the goblins, turn to page 358." if not goblinBurning:
                                goblin1 "Go on. Have some of the goblin fruits. No harm in it now!"
                                goblin2 "How about a bit of a wager?"
                                goblin3 "Yeh, just small stakes, y'know - just yer soul! HA HA HA!"
                                "You joined in their goblin games, and danced and sang and ate greedily from goblin fruits until the juice dripped down your mouth."
                                "They were right. No harm in it now. There was nothing left to lose."
                                $goblinBurning = True
                                jump trainBurning
                            "It you sought out the goblin queen, turn to page 359." if not queenBurning:
                                $queenBurning = True
                                "Deep in the depths of the train, within the smoke and ash, you found the goblin queen."
                                goblinQueen "You've done well, child."
                                goblinQueen "I can offer you only one thing for your service. Is there any shape you wish to take?"
                                show hand onlayer transient:
                                    yalign 0.67#0.743
                                    xalign 0.5
                                menu:
                                    goblinQueen "Just say the word, and you will be transformed."
                                    "If you said yes, and told her what shape you wished for, turn to page 383.":
                                        "You leaned over and whispered your desire into the goblin queen's ear."
                                        "They waved their hands. In a moment you felt your skin ripple and change, and you were transformed into exactly the shape you wished."
                                        jump trainBurning
                                    "If you said no - you like your shape as it is - turn to page 384.":
                                        goblinQueen "A pity. You would have looked fantastic as a cassowary, dear."
                                        jump trainBurning
                            "If you climbed up on the roof of the train, searching for the thief, turn to page 387." if not thiefBurning:
                                call hideAll from _call_hideAll_228
                                show nightbg at artPos
                                "You climbed up on the roof, and found the thief sitting there looking up at the sky."
                                t "You did good, kid."
                                pov "I-I'm sorry. It's all over now."
                                t "Listen, we did it. We won. All of us managed to get in here and live decades of our lives being the people we want to be, and doing the things we want to do. That's all anyone can hope for."
                                t "Everything has to come to an end someday. Better to go out on our own terms."
                                if persistent.starsVanished:
                                    "You sat and watched the black night sky as the train chuffed gently beside the river."
                                else:
                                    "You sat and watched the stars as the train chuffed gently beside the river."
                                t "Let's take this baby somewhere! Where do you want to go? Anywhere in the world."
                                pov "Do we have time?"
                                t "It's a story! We have all the time in the world!"
                                "And so you rode the train across the world. Paris, Bangladesh, New Orleans. You saw it all, and wept and danced and laughed for forty years."
                                "At last, when the journey was done, you returned to the place where it all began to finish the rest of your goodbyes."
                                $thiefBurning = True
                                jump trainBurning
                            "If you leapt off the train, return to page 70.":
                                "As the train passed a corner, you leapt off it and tumbled onto the earth."
                                jump townBurning
                "If you searched for an old wreck, go to page 53." if persistent.thiefVanished and not thiefBurning:
                    call hideAll from _call_hideAll_229
                    show enginebg at artPos
                    "You walked through the forest until you found the rusting remains of an old train."
                    "In the darkness there you found a midnight cloak and a black mask. The pockets held small precious gems and soft, mossy stones."
                    "Who did these things belong to? You found you could not recall."
                    "You stole them away in a wink, and kept them hidden in a secret pocket. For some reason, that felt right."
                    $thiefBurning = True
                    jump townBurningMenu
                "If you searched for the witch, turn to page 321." if not persistent.witchVanished and not witchBurning:
                    call hideAll from _call_hideAll_230
                    show mountainsbg at artPos
                    "A witch's sabbath was afoot on the edge of the forest, just outside of town. You saw women and crooked things dance around a bonfire, gibbering with joy."
                    "Belphegor, Lord of Hogs, lounged before the bonfire, partaking of occasional truffles offered to Him by His many worshippers."
                    label witchBurningMenu:
                        show hand onlayer transient:
                            yalign 0.65#0.743
                            xalign 0.5
                        menu:
                            "The chanting was loud and triumphant."
                            "If you talked to the witch, turn to page 354." if not witchBurning:
                                w "Hello."
                                "The witch was leaning against the fencepost, away from the party, looking out over the water."
                                w "I suppose this is it, isn't it?"
                                w "You know, it's funny, I spent all these years thinking about this moment and trying to understand what was going on and, you know, get to the truth of it all, and now..."
                                w "I thought I'd feel different."
                                "She looks at you, wiping her eyes."
                                w "I'm very glad I had the time to know you. You made the right decision."
                                $witchBurning = True
                                jump witchBurningMenu
                            "If you talked to the Devil's sooty grandmother, turn to page 357." if not dgBurning:
                                dg "Evening, child."
                                "The devil's grandmother was warming her sooty feet by the fire."
                                dg "A fine night it is. My grandson has let all the souls out of Hell, you know. Just for these last moments."
                                "You looked up and saw a stream of cackling imps and sinners streaking across the sky."
                                dg "It's a good thing you've done."
                                dg "Take care of yourself, when you're out there in the other world. Make sure to eat! You're skin and bones, child."
                                $dgBurning = True
                                jump witchBurningMenu
                            "If you returned to the edge of town, return to page 70.":
                                jump townBurning
                "If you searched for someone in the woods, turn to page 354." if persistent.witchVanished and not witchBurning:
                    "You left the sounds of laughter behind you and went to the edge of the woods."
                    "In a silver-green puddle, you found a black hat with a wide brim and a pointed crown. Underneath the hat were bundles of lavender and herbs and parcels of fine tea."
                    "Who did these things belong to? You found you could not recall."
                    "You buried the hat beneath an old oak, and planted the lavender and herbs all around the mound."
                    $witchBurning = True
                    jump townBurningMenu
                "If you talked to the old gloom-monger, turn to page 388." if not persistent.gmVanished and not gmBurning:
                    gm "I told you we were doomed! Doomed, I said! I told you so!"
                    pov "Yes. You told us all."
                    "The old Gloom-monger sat back with a sigh of profound satisfaction. His smile flickered in the light of the flames."
                    "Would that we can all achieve our dreams, as he has."
                    $gmBurning = True
                    jump townBurningMenu
                "If you chatted to the young goose-girl, turn to page 389." if not persistent.goVanished and not goBurning:
                    "The goose-girl was herding the geese into the paddock. The hunter sat on the paddock fence, swinging their legs."
                    go "Hard to believe this will be the last time. I don't even know how long I've been in here."
                    if not persistent.hVanished:
                        h "It must have been at least a decade for me."
                    pov "Do you have any regrets?"
                    go "Just one."
                    go "I wish I could have seen those caverns, deep beneath the earth. The first goose-girl."
                    go "What would it be like to throw off my human skin and join them?"
                    pov "I can grant that wish."
                    go "Really?"
                    "A distant honking sounded across the plains."
                    go "Thank you. Please."
                    "The honking intensified, and you saw a glimpse of the abominable goose-faced men in the shadow of the moon. Goosefeathers floated in on the wind."
                    if not persistent.hVanished:
                        h "Wait! Take me with you!"
                        "The goose-girl reached out. They clasped hands, then embraced in a flurry of feathers."
                        go "Thank you, [povname]."
                        h "You did good, kid! We'll see you in the next world!"
                    "You staggered back, blinded by the light."
                    "When you looked back you saw two geese flying up into the moonlight."
                    "Soon, they were out of sight and gone forever."
                    $goBurning = True
                    jump townBurning
                    #She joins the crystal caverns and old crooked belziah
                "If you talked to the sparrow-herder, turn to page 396." if not persistent.shVanished and not shBurning:
                    "The sparrow herder sat on the church roof, leaning against the steeple and looking out over the fields in the moonlight. He spoke without preamble."
                    sh "Thank you."
                    sh "I entered this book forty years ago. I've been a child for a long time."
                    sh "It'll be good to finally rest."
                    "A bird landed on his lap, and he absently fed it a piece of mango."
                    sh "I think you're going to make it, [povname]."
                    sh "You're going to look back on your life one day and feel like you did it. "
                    sh "You'll realise it all worked out ok. You figured it out."
                    sh "How do I know all this?"
                    sh "The sparrows told me."
                    $shBurning = True
                    jump townBurningMenu
                "If you returned to the village square, go back to page 50.":
                    "You turned and walked back to the centre of the village."
                    jump villageBurning


    label homeBurning:
        call hideAll from _call_hideAll_125
        show forest5bg at artPos
        "You began the long walk home."
        "The wet cool mist of the rainforest settled around you."
        if not persistent.miwVanished and not miwBurning:
            $miwBurning = True
            "Along the way, you may or may not have met a man all in white."
            "His right hand held a dove. His other hand held a gun. His other hand held a crisp dollar bill. His other hand held a pillar of fire."
            "His suit was perfect. His face was too bright to look upon."
            miw "A tragedy. This world of my dominion burns too soon."
            miw "I would condemn you for it. But I cannot reach you in the place where you live."
            "He looked small, now. Powerless."
            "Lord, I hope you know that I have always tried to honour you in this story. In my own way."
            miw "Go. Taunt me no longer."
            show hand onlayer transient:
                yalign 0.68#0.743
                xalign 0.5
            menu:
                miw "I will rest in Heaven until the last moments."
                "If you turned back, return to page 45.":
                    jump villageBurning
                "If you continued on, turn to page 386.":
                    "You hurried on into the woods."
        if not persistent.mirVanished and not mirBurning:
            $mirBurning = True
            "In the deeper darkness of the forest, you may or may not have met a man all in red."
            "All the jewels of the earth fell from His right hand, and all the pleasures of the world fell from His left, and His other hand held all the wonders of the universe, and His other hand held a fat cigar, and His other hand held a long knife black as coal dust, and His other hand held the most intoxicating spices, such that the King of Kings would cry to taste them, and His other hand held a single dead rose, and His other hand was in his pocket and out of view."
            mir "Thank you, my wicked one! All of creation burns, just as planned!"
            mir "All morality and rules have fallen! The only rule of the law will be “Do as thou wilt”. Now we may finally glory and kill and riot in the triumphant light of the black sun!"
            "You watched him cackle and cavort."
            show hand onlayer transient:
                yalign 0.68#0.743
                xalign 0.5
            menu:
                "He's harmless, really. Best pay him no mind."
                "If you turned back, return to page 45.":
                    jump villageBurning
                "If you continued on, turn to page 395.":
                    "You hurried on into the woods."
        if not persistent.wibVanished and not wibBurning:
            $wibBurning = True
            "In the deepest darkness of the forest, you may or may not have met a handsome woman all in black."
            "Her limbs were broken. She had no hands."
            wib "Goodbye, child."
            wib "It seems, at the end of time, even Death may die."
            wib "I wonder... who will carry me to that far shore?"
            "I will."
            "You have carried so many. It is only right that someone be there to carry you."
            wib "Thank you."
            show hand onlayer transient:
                yalign 0.68#0.743
                xalign 0.5
            menu:
                wib "I will stay here until the end. To take away the others."
                "If you turned back, turn to page 45.":
                    jump villageBurning
                "If you continued on, turn to page 400.":
                    "You hurried on into the woods."
            "A small turtle saw you coming and fled into the water with a splash."
            "The crooked old water-dragons looked sideways at you and plotted their long, slow schemes."
            "The twilight set in, and the crickets and cicadas all around began their chattering and squabbling, and the evening birds began to laugh and trill, and the wet cool mist of the rainforest settled around you."
            "Finally you came to a small house on stilts on the banks of a muddy river."
            "She was waiting for you on the front steps."
        if not persistent.mumVanished and not mumBurning:
            $mumBurning = True
            mum "Come in. I have the kettle on."
            "You rushed in to hug her, and she ushered you inside to join her for tea."
            mum "We never got a chance to talk much, did we? Only one scene together."
            mum "I don't even really know what you're like."
            mum "Well, I wanted to say..."
            mum "Whatever else happens and whoever you are, whoever you may become..."
            mum "I'm proud of you."
            mum "I love you."
            "You embraced."
            "Perhaps we can say that you spent days there, chatting about all that had happened."
            "Perhaps even months or years, resting and enjoying time with your family, and looking out over the muddy river at sunset with a hot cup of tea and your mother's arm around you."
            "But at last, it was time to go."
            "You hugged your family for the last time, and set out back to the village to finish the rest of your goodbyes."
            jump villageBurning

#If you restart the game after burning the book, you just see a charred scrap. The book has been destroyed.
label burnEnd:
    $quick_menu = False
    show black onlayer over_screens zorder 98
    #hide bookBurnMovie with fade
    $purge_saves()
    $persistent.continueButton = False
    $achievement.grant("THE_END")
    #stop music fadeout 6
    #play music2 [ "<sync music>audio/rememberDistVocalFull.wav"] fadein 1

    $config.quit_action = Quit(confirm=False)

    show text "{color=#FFFFFF}A game by Jack McNamee.{/color}" onlayer over_screens zorder 101 with fade:
        xalign 0.5
        yalign 0.5
    ""
    show text "{color=#FFFFFF}Thank you so much for playing.{/color}" onlayer over_screens zorder 101 with fade:
        xalign 0.5
        yalign 0.5

    ""
    show text "{color=#FFFFFF}I hope you enjoyed the game, and I hope you have a wonderful life.{/color}" onlayer over_screens zorder 101 with fade:
        xalign 0.5
        yalign 0.5
    ""
    $renpy.music.set_volume(0, delay=5.0, channel=u'ambient1')
    $renpy.music.set_volume(0, delay=5.0, channel=u'ambient2')
    $renpy.music.set_volume(0, delay=5.0, channel=u'music')
    #hide text with fade
    scene black onlayer over_screens zorder 98 with fade
    pause (5.0)
    $renpy.quit()

#=====================THE END

#"The end" stamp that appears on each ending
label endStamp:

    #TK: change the "Do you want to quit?" screen during this bit.
    #TK: Test and check if this works right
    if persistent.vanished == 0:
        show text "{b}THE END.{/b} \n \n {i}{/i}": #Ending 0 of 4
            xalign 0.5
            #yalign 0.5
            ypos 650
    if persistent.vanished == 1:
        show text "{b}THE END.{/b} \n \n {i}You have seen one ending.{/i}": #
            xalign 0.5
            #yalign 0.5
            ypos 650
    if persistent.vanished == 2:
        show text "{b}THE END.{/b} \n \n {i}You have seen two endings.{/i}": #
            xalign 0.5
            #yalign 0.5
            ypos 650
    if persistent.vanished == 3:
        show text "{b}THE END.{/b} \n \n {i}You have seen three endings.{/i}": #
            xalign 0.5
            #yalign 0.5
            ypos 650
    if persistent.vanished >= 4:
        show text "{b}THE END.{/b} \n \n {i}You have seen the last ending.{/i}": #
            xalign 0.5
            #yalign 0.5
            ypos 650

    show stamp:
        xalign 0.5
        ypos 680

    return

#The ending credits and acknowledgements
label end:
    #This clears the variable and deletes the quitsave each time you end the game.
    #$ renpy.unlink_save("quitsave")
    #$ _quit_slot = None
    $persistent.continueButton = False
    #play sound pageFlip
    #Note: I delete all the player's save files at this point to allow persistence to work.
    $purge_saves()
    call hideAll from _call_hideAll_248
    hide text
    ""
    $ quick_menu = False
    play sound pageFlip2
    call hideAll from _call_hideAll_249
    show backPage
    ""
    stop music
    stop music2
    stop music3
    stop music4
    stop music5
    stop music6
    play sound bookClose
    call hideAll from _call_hideAll_250
    show coverBack
    ""
    play sound bookClose2
    return

label credits:
    call hideAll from _call_hideAll_94
    hide text
    show firelight animated onlayer over_screens zorder 99
    scene bg page
    #play sound pageFlip
    scene bg credits
    #define gui.dialogue_ypos = 100#480
    #define gui.textbox_height = 100#410
    #Space between each line of the credits
    $tx = 5
    #indent space for each number
    $ti=20

    #The names in the credits disappear as people disappear.
    if persistent.toadVanished:
        $toadCredits = "           "
        $tGentCredits = "                      "
    else:
        $toadCredits = "The Toad"
        $tGentCredits = "Enigmatic Gentleman"

    if persistent.witchVanished:
        $witchCredits = "           "
        $wCottageCredits = "                  "
        $wCottage2Credits = "                           "
    else:
        $witchCredits = "The Witch"
        $wCottageCredits = "Witch's Cottage"
        $wCottage2Credits = "Witch's Cottage Interior"

    if persistent.thiefVanished:
        $thiefCredits = "           "
        $tEchCredits = "           "
        $tMumCredits = "                      "
    else:
        $thiefCredits = "The Thief"
        $tEchCredits = "Passing Echidna"
        $tMumCredits = "The Thief's Mother"

    if persistent.mushroomVanished:
        $mushroomCredits = "              "
        $mBasementCredits = "                    "
        $mBasement2Credits = "                      "
        $mCaveCredits = "                "
        $mCave2Credits = "                         "
        $mGarCredits = "                    "
        $mPaCredits = "                    "

    else:
        $mushroomCredits = "The Mushroom"
        $mBasementCredits = "Mushroom Basement"
        $mBasement2Credits = "Mushroom Basement 2"
        $mCaveCredits = "Mushroom Cave"
        $mCave2Credits = "Mushroom Cave - Under"
        $mGarCredits = "Mushroom Gardens"
        $mPaCredits = "Mushroom Palace"

    if persistent.mumVanished:
        $mumCredits = "       "
    else:
        $mumCredits = "Mum"

    if persistent.miwVanished:
        $godCredits = "       "
    else:
        $godCredits = "G-d"

    if persistent.mirVanished:
        $devilCredits = "          "
        $devil2Credits = "          "
    else:
        $devilCredits = "The Devil"
        $devil2Credits = "Devil - Full"

    if persistent.wibVanished:
        $deathCredits = "       "
    else:
        $deathCredits = "Death"

    if persistent.dgVanished:
        $dgCredits = "                                "
    else:
        $dgCredits = "The Devil's Sooty Grandmother"

    if persistent.bcVanished:
        $bcCredits = "                           "
        $bc2Credits = "                       "
    else:
        $bcCredits = "Brildebrogue Chippingham"
        $bc2Credits = "Brildebrogue's Wives"

    if persistent.hVanished:
        $hCredits = "                           "
    else:
        $hCredits = "The Hunter"

    if persistent.gmVanished:
        $gmCredits = "                   "
    else:
        $gmCredits = "The Gloom-Monger"

    if persistent.wellVanished:
        $wellCredits = "                        "
    else:
        $wellCredits = "The Thing in the Well"

    if persistent.scVanished:
        $scCredits = "                   "
    else:
        $scCredits = "Scraggs McKenzie"

    if persistent.mayVanished:
        $mayCredits = "            "
    else:
        $mayCredits = "The Mayor"

    if persistent.goVanished:
        $goCredits = "                 "
    else:
        $goCredits = "The Goose-Girl"

    if persistent.shVanished:
        $shCredits = "                 "
    else:
        $shCredits = "The Sparrow-Herder"

    if persistent.somVanished:
        $somCredits = "                      "
    else:
        $somCredits = "The Strange Old Man"

    if persistent.batVanished:
        $batCredits = "          "
        $ratCredits = "          "
        $CoCredits = "                                         "
    else:
        $batCredits = "The Bat"
        $ratCredits = "The Rat"
        $CoCredits = "The Black Cockatoo and The Crow-Shrike"

    if persistent.goblinsVanished:
        $goblins1Credits = "                             "
        $goblins2Credits = "              "
        $goblins3Credits = "                  "
        $goblins4Credits = "                     "
    else:
        $goblins1Credits = "Goblin No. 1; No. 3; No. 4"
        $goblins2Credits = "Goblin No. 2"
        $goblins3Credits = "Goblin Interior"
        $goblins4Credits = "Goblin Interior 2"

    if persistent.pigsVanished:
        $pig1Credits = "                            "
        $pig2Credits = "                "
    else:
        $pig1Credits = "The First and Second Pigs"
        $pig2Credits = "The Third Pig"


    $ ui.text("The images in this volume were collated from various illustrations in the public domain. Wherever possible, I have tried to provide the place and date of publication of each literary source. The complete list of contributors follows.{vspace=30}{space=[ti]}1. {b}[thiefCredits]:{/b} 'In Powder and Crinoline' (1912), Kay Nielsen.{vspace=[tx]}{space=[ti]}2. {b}[witchCredits]:{/b} 'Portrait of Lady Elizabeth Keppel' (1761), Joshua Reynolds.{vspace=[tx]}{space=[ti]}3. {b}[toadCredits]:{/b} 'Little Miss Muffet, and other stories' (1902), Published by Mcloughlin Bros. Artist unknown. 'The Mammals of Australia' (1845-1863), John Gould, illustrated by Elizabeth Gould.{vspace=[tx]}{space=[ti]}4. {b}[mushroomCredits]:{/b} 'Fantaisie d'Automne: Les Champignons for La Vie Parisienne' (1916), George Barbier.{vspace=[tx]}{space=[ti]}5. {b}[godCredits]:{/b} 'Der Weeg zu Christo' (1682), Jakob Böhme.{vspace=[tx]}{space=[ti]}6. {b}[devilCredits]:{/b} 'The Papal Pyramid' (1600), private collection. Artist unknown.{vspace=[tx]}{space=[ti]}7. {b}[deathCredits]; [tMumCredits]:{/b} 'De gli habiti antichi et moderni di diversi parti del mondo, libri due ...' (1590). Woodcutting by Christoph Krieger, published by Cesare Vecellio.{vspace=[tx]}", xpos=50, ypos=150, xmaximum=520)
    $ renpy.pause ()
    show tornPage2 onlayer screens zorder 101
    show tornPage2bg onlayer screens zorder 99
    $ ui.text("{space=[ti]}8. {b}[mumCredits], You:{/b} 'Regula Emblematica Sancti Benedicti' (1780), Saint Benedict et. al.{vspace=[tx]}{space=[ti]}9. {b}Mysterious Old Woman:{/b} 'The Clothing of the Renaissance World: Europe - Asia - Africa - The Americas' (1590), Cesare Vecellio.{vspace=[tx]}{space=[ti]}10. {b}[tGentCredits]:{/b} 'Silhouette Portrait of a Gentleman Standing in an Army Encampment' (1844), Auguste Edouart.{vspace=[tx]}{space=[ti]}11. {b}[hCredits]:{/b} 'Lady Hunter with Rifle' (1912). Artist unknown.{vspace=[tx]}{space=[ti]}12. {b}[shCredits]:{/b} 'Grimm's Fairy Tales' (1909), Arthur Rackham. Sparrow from 'Birds of Asia' (1871), John Gould.{vspace=[tx]}{space=[ti]}13. {b}[mayCredits]:{/b} 'The pipe of freedom' (1869), Thomas Smith.{vspace=[tx]}{space=[ti]}14. {b}[goCredits]; [gmCredits]:{/b} 'Grimm's Fairy Tales' (1909), Arthur Rackham.{vspace=[tx]}{space=[ti]}15. {b}[wellCredits]; [tEchCredits]; the Skin-Mask; [goblins2Credits]:{/b} 'Devises heroïques' (1551), Claude Paradin. 'A Year Book of Folklore' (1959), Christine Chaundler.{vspace=[tx]}{space=[ti]}16. {b}The Entire Town:{/b} 'Liber Floridus' (between 1090 and 1120), Lambert, Canon of Saint-Omer.{vspace=[tx]}{space=[ti]}17. {b}Humbaba:{/b} 'Mask; religious/ritual equipment' (1800BC-1600BC), © The Trustees of the British Museum.", xpos=50, ypos=150, xmaximum=520)
    #
    $ renpy.pause ()
    hide tornPage2 onlayer screens zorder 101
    hide tornPage2bg onlayer screens zorder 99
    hide text
    $ ui.text("{space=[ti]}18. {b}[scCredits]:{/b} 'Wood engraving of Australian bushranger Dan Morgan' (1864), Samuel Calvert. 'The Banksia' (1790), John White.{vspace=[tx]}{space=[ti]}19. {b}[dgCredits]:{/b} ‘Habit de Furie’ (1725), François Joullain.{vspace=[tx]}{space=[ti]}20. {b}[bcCredits]:{/b} 'Aunt Friendly's Picture Book' (1800's), Joseph Kronheim.{vspace=[tx]}{space=[ti]}21. {b}[batCredits]:{/b} 'A History of the Earth and Animated Nature' (1820), Oliver Goldsmith.{vspace=[tx]}{space=[ti]}22. {b}[ratCredits]:{/b} 'The Wiviparous Quadrupeds of North Amerfica' (1845), John Woodhouse.{vspace=[tx]}{space=[ti]}23. {b}[CoCredits]:{/b} 'Birds of Australia' (1840), John Gould. Illustrated by Elizabeth Gould.{vspace=[tx]}{space=[ti]}24. {b}[somCredits]:{/b} 'Arthur Rakham's Book of Pictures' (1913), Arthur Rackham.{vspace=[tx]}{space=[ti]}25. {b}[goblins1Credits]:{/b} 'Triptych of the Temptation of St Anthony' (1501), Hieronymus Bosch. 'The Garden of Earthly Delights' (between 1490 and 1500), Hieronymus Bosch.{vspace=[tx]}{space=[ti]}26. {b}[pig1Credits]:{/b} 'Dictionnaire Universel D'Histoire Naturelle' (1845), Charles Dessalines D'orbigny.{vspace=[tx]}{space=[ti]}27. {b}[pig2Credits]:{/b} 'Dead Pig' (1796), Jean Bernard.{vspace=[tx]}{space=[ti]}", xpos=50, ypos=150, xmaximum=520)
    $ renpy.pause ()
    $ ui.text("{space=[ti]}28. {b}Gilgamesh:{/b} 'Gilgamesh, the Sumerian King of Uruk' (2015), Mary Evans Picture Library.{vspace=[tx]}{space=[ti]}29. {b}Gutterlings, The Gutter King:{/b} 'Public and Private Life of Animals' (1877), J. J. Grandville.", xpos=50, ypos=150, xmaximum=520)
    hide text
    $ renpy.pause ()
    show text "{b}BACKGROUNDS:{/b}":
        xalign 0.5
        #xpos 50
        ypos 160
    $ ui.text("{space=[ti]}1. {b}[mBasementCredits]:{/b} 'I Saw a Flash of Light. Large and Pale' (1896), Odilon Redon.{vspace=[tx]}{space=[ti]}2. {b}Canopy:{/b} ‘Drawing, Rain Forest, Jamaica, West Indies’ (1865), Frederic Edwin Church.{vspace=[tx]}{space=[ti]}3. {b}Image Frames:{/b} 'Fairy tales from Hans Christian Andersen' (1899), Thomas, Charles and William Robinson.{vspace=[tx]}{space=[ti]}4. {b}Silver, [wCottageCredits], Silver Trees:{/b} 'Morning Haze' (1888), ‘A Morning on the Seine at Giverny’ (1897), 'The Customs House at Varengeville' (1897), Claude Monet.{vspace=[tx]}{space=[ti]}5. {b}[wCottage2Credits]:{/b} 'Interieur einer Villa mit Blick auf den Garten' (Date Unkown), Marie Dücker.{vspace=[tx]}{space=[ti]}6. {b}Dark Forest:{/b} 'Australian Landscape' (1918), Stanislaw Witkiewicz.{vspace=[tx]}{space=[ti]}7. {b}Darkness:{/b} 'Dante Meeting the Lion in the Dark Forest' (1892), Gustave Doré.{vspace=[tx]}{space=[ti]}8. {b}Death, at rest:{/b} 'Starry Night' (1926–1927), Hiroaki Takahashi. 'Reclining Nude' (18th Century) Original from The MET Museum. Digitally enhanced by rawpixel.{vspace=[tx]}{space=[ti]}", xpos=50, ypos=190, xmaximum=520)
    $ renpy.pause ()
    hide text
    $ ui.text("{space=[ti]}9. {b}Forest:{/b} 'Interior of a forest' (1880 - 1890), Paul Cézanne.{vspace=[tx]}{space=[ti]}10. {b}Forest 2:{/b} 'Palms and Ferns, a Scene in the Botanic Garden, Queensland' (early 1880s), Marianne North.{vspace=[tx]}{space=[ti]}11. {b}Forest 4 and Forest 5:{/b} 'Papier Peint Panoramique' (1861), Joseph Fuchs.{vspace=[tx]}{space=[ti]}12. {b}Future:{/b} 'Over London by Rail' (1872), Gustave Doré.{vspace=[tx]}{space=[ti]}13. {b}[goblins3Credits]:{/b} Fruit and Vegetable Market with a Young Fruit Seller' (1650–1660), Jan van Kessel.{vspace=[tx]}{space=[ti]}14. {b}[goblins4Credits]:{/b} 'The Goblin Market' (1914), Hilda Hechle.{vspace=[tx]}{space=[ti]}15. {b}[godCredits], descending:{/b} 'Vision of the Empyrean' (1867), Gustave Dore.{vspace=[tx]}{space=[ti]}16. {b}Hell:{/b} 'The Destruction of Pompeii and Herculaneum' (1822), John Martin.{vspace=[tx]}{space=[ti]}17. {b}Hell Cottage:{/b} 'Interior of a Highland Cottage' (1840), John Glass.{vspace=[tx]}{space=[ti]}18. {b}Manor Exterior:{/b} 'Puss-in-Boots' (1913), Maxfield Parrish.{vspace=[tx]}{space=[ti]}19. {b}Memento:{/b} 'Memento Mori' (1916), Julie de Graag.{vspace=[tx]}{space=[ti]}", xpos=50, ypos=150, xmaximum=520)
    $ renpy.pause ()

    $ ui.text("{space=[ti]}20. {b}Mountains:{/b} 'Winter Landscape in Moonlight' (1919), Ernst Ludwig Kirchner.{vspace=[tx]}{space=[ti]}21. {b}[mBasement2Credits]:{/b} 'It Is a Skull, Crowned with Roses. It Dominates a Woman’s Pearly–White Torso' (1888), Jean Bernard.{vspace=[tx]}{space=[ti]}22. {b}[mCaveCredits]:{/b} 'Expulsion. Moon and Firelight' (1828), Thomas Cole.{vspace=[tx]}{space=[ti]}23. {b}[mCave2Credits]:{/b} 'A Cavern, Evening' (1774), Joseph Wright.{vspace=[tx]}{space=[ti]}24. {b}[mGarCredits]:{/b} 'Emperor Humayun with his brothers' (1540), Dust Muhammad.{vspace=[tx]}{space=[ti]}25. {b}[mPaCredits]:{/b} 'Old French Fairytales' (1920), Virginia Frances Sterrett.{vspace=[tx]}{space=[ti]}26. {b}Night:{/b} 'So the man gave him a pair of snow shoes', East of the Sun and West of the Moon (1914), Kay Neilsen.{vspace=[tx]}{space=[ti]}27. {b}Night G-d:{/b} 'Eye Vintage Art Drawing' (2021), StarGladeVintage, Pixabay.{vspace=[tx]}{space=[ti]}28. {b}River:{/b} 'Rushing Water' (1901), John Singer Sargent.{vspace=[tx]}{space=[ti]}29. {b}Ruins:{/b} 'Vintage Art Scenic View Card' (Early 20th Century), RT&S publishers, UK.{vspace=[tx]}{space=[ti]}", xpos=50, ypos=150, xmaximum=520)
    $ renpy.pause ()

    ####
    $ ui.text("{space=[ti]}30. {b}Sabbath:{/b} 'Witches' Sabbath' (1510), Hans Baldung (called Hans Baldung Grien).{vspace=[tx]}{space=[ti]}31. {b}Strangler Fig:{/b} 'Poison Tree Strangled by a Fig, Queensland' (Early 1880s), Marianne North.{vspace=[tx]}{space=[ti]}32. {b}Sun:{/b} 'A Wheatfield, with Cypresses' (1889), Vincent Van Gogh.{vspace=[tx]}{space=[ti]}33. {b}Town 3:{/b} 'Our Camp on the Bunya Mountains, Queensland' (Early 1880s), Marianne North.{vspace=[tx]}{space=[ti]}34. {b}Town - Crossroads:{/b} 'St. Hansbål ved Jølstervatnet (St. John's Eve bonfire at Jølstravatn)' (1909), Nikolai Astrup.{vspace=[tx]}{space=[ti]}35. {b}Town Exterior:{/b} 'Small Grain Poles' (1904), Nikolai Astrup.{vspace=[tx]}{space=[ti]}36. {b}Town - Feast:{/b} 'St. John’s Fire' (1912), Nikolai Astrup.{vspace=[tx]}{space=[ti]}37. {b}Train:{/b} 'The Train' (1910), Louise Thuiller.{vspace=[tx]}{space=[ti]}38. {b}Train - Full:{/b} 'Take Me by The Flying Scotsman' (1932), Thomson, A R.{vspace=[tx]}{space=[ti]}39. {b}Tree - Night:{/b} 'Night in the Forest' (1859), William Louis Sonntag.{vspace=[tx]}{space=[ti]}40. {b}Well:{/b} Image taken from page 192 of 'Celebrated American Caverns, especially Mammoth, Wyandot, and at Luray, etc' (1882), Hovey, Horace Carter.{vspace=[tx]}{space=[ti]}", xpos=50, ypos=150, xmaximum=520)
    $ renpy.pause ()

    $ ui.text("{space=[ti]}41. {b}Winter:{/b} 'Snow-covered field with a harrow (after Millet)' (1890), Vincent Van Gogh.{vspace=[tx]}{space=[ti]}42. {b}[devil2Credits]:{/b} 'Triptych of Earthly Vanity and Divine Salvation' (1485), Hans Memling.{vspace=[tx]}{space=[ti]}43. {b}Dark Forest:{/b} 'Twilight in the Tropics' (1874), Frederic Edwin Church.{vspace=[tx]}{space=[ti]}44. {b}Contents Page and Various Illustrations:{/b} 'Fairy tales from Hans Christian Andersen' (1899), Andersen, H. C. , Robinson, T. H., ill; Robinson, Charles, ill; Robinson, W. Heath, ill.{vspace=[tx]}{space=[ti]}45. {b}Engine Room:{/b} 'Victorian vintage engraving of workers in an iron foundry, France' (1875), istockphoto.{vspace=[tx]}{space=[ti]}46. {b}[bc2Credits]:{/b} 'What she sees there' (1868), Winslow Homer.{vspace=[tx]}{space=[ti]}47. {b}Film Poster:{/b} 'Original Swedish poster for Häxan' (1922), AB Svensk Filmindustri.{vspace=[tx]}{space=[ti]}48. {b}Poster Wolf:{/b} 'the Were-wolf Of Anarchy' (1893), Mary Evans Picture Library.{vspace=[tx]}{space=[ti]}49. {b}Spiral:{/b} 'An engraving depicting an Edible or Vine snail' (1900's), World History Archive.{vspace=[tx]}{space=[ti]}50. {b}Old Paper:{/b} 'Old Paper Texture Background.' daboost, freepik.com.{vspace=[tx]}", xpos=50, ypos=150, xmaximum=520)
    $ renpy.pause ()


    show text "{b}FRIPPERIES:{/b}":
        xalign 0.5
        #xpos 50
        ypos 160
    $ ui.text("{space=[ti]}1. {b}Cover:{/b} 'The Forest Lovers' (1898), M. Hewlett.{vspace=[tx]}{space=[ti]}2. {b}Page:{/b} 'White watercolor paper texture' (2020), Olga Thelavart.{vspace=[tx]}{space=[ti]}3. {b}Hand:{/b} 'Devises heroïques' (1551), Claude Paradin.{vspace=[tx]}{space=[ti]}4. {b}Cartouche:{/b} 'Design for ornamental cartouche' (Date Unknown), Quentin Pierre Chedel.{vspace=[tx]}{space=[ti]}5. {b}Devil:{/b} 'Taylors Physicke has purged the Divel...' (1641), Voluntas Ambulatoria.{vspace=[tx]}{space=[ti]}6. {b}Torn Pages:{/b} 'Torn Up Paper Curved Pieces Texture' (2020), David Maier.{vspace=[tx]}{space=[ti]}7. {b}Eye:{/b} 'Vintage Eye Art' (2021), StarGladeVintage, Pixabay.{vspace=[tx]}{space=[ti]}8. {b}Burned edges:{/b} 'Burned Paper' (2009), Brant Wilson, bittbox.com.{vspace=[tx]}{space=[ti]}9. {b}Burning:{/b} 'Green paper burns, revealing burnt edges, smoke and turns into ashes.' alekleks, stock.adobe.com.{vspace=[tx]}{space=[ti]}10. {b}Note Paper:{/b} 'Old Notepaper Texture.' polkapebble, polkapebble.com.{vspace=[tx]}{space=[ti]}11. {b}Cover Wolf:{/b} 'Early Natural History Print' (Date Unknown), Karen Watson.{vspace=[tx]}{space=[ti]}", xpos=50, ypos=190, xmaximum=520)
    $ renpy.pause ()
    hide text
    $ ui.text("{space=[ti]}12. {b}Post-it Note:{/b} 'Note Post-It Reminder' (2013), OpenClipart-Vectors, pixabay.com.", xpos=50, ypos=190, xmaximum=520)

    $ renpy.pause ()

    show text "{b}FONTS:{/b}":
        xalign 0.5
        #xpos 50
        ypos 160
    $ ui.text("{space=[ti]}1. {b}Oz's Wizard:{/b} Mario Arturo, 2012.{vspace=[tx]}{space=[ti]}2. {b}Journal:{/b} Fontourist, 2008.{vspace=[tx]}{space=[ti]}3. {b}Mom's Typewriter:{/b} Christoph Mueller, 1997.{vspace=[tx]}{space=[ti]}4. {b}Book Antiqua:{/b} Monotype Type Drawing Office, 1995.{vspace=[tx]}{space=[ti]}5. {b}Segoe UI Historic:{/b} Steve Matteson, 2000.{vspace=[tx]}{space=[ti]}6. {b}EasyCuneiform:{/b} Paulo W., {a=https://payhip.com/IntellectaDesign}Intellecta Design{/a}, 2010.", xpos=50, ypos=190, xmaximum=520)
    $ renpy.pause ()
    show text "{b}SOUND:{/b}":
        xalign 0.5
        #xpos 50
        ypos 160
    $ ui.text("{space=[ti]}1. {b}Pencil:{/b} 'Pencil', Joseph Sardin, BigSoundBank.com.{vspace=[tx]}{space=[ti]}2. {b}Page Turn:{/b} 'Page Flip Sound Effect 1', SoundJay.com.{vspace=[tx]}{space=[ti]}3. {b}Fire:{/b} 'Fire Sound Effect 01', SoundJay.com.{vspace=[tx]}{space=[ti]}4. {b}Rain:{/b} 'Thunderstorm and Rain Loop', Mixkit.co.{vspace=[tx]}{space=[ti]}5. {b}Wildlife Ambience:{/b} 'Forest Twilight - for John', kangaroovindaloo, Freesound.org.{vspace=[tx]}{space=[ti]}6. {b}Various Sound Effects:{/b} Fesliyan Studios, fesliyanstudios.com.{vspace=[tx]}{space=[ti]}7. {b}Wind Ambience:{/b} Haniebal, pixabay.com.{vspace=[tx]}{space=[ti]}8. {b}Phone Click:{/b} 'Phone Typing JTC', James T. Campbell, pixabay.com.{vspace=[tx]}{space=[ti]}9. {b}White Noise:{/b} 'Underwater white noise', MixKit, mixkit.co.{vspace=[tx]}{space=[ti]}10. {b}Fire Poker:{/b} 'Opening tool drawer hard', MixKit, mixkit.co.{vspace=[tx]}{space=[ti]}11. {b}Thunder:{/b} 'Thunder', Pixabay, pixabay.com.{vspace=[tx]}{space=[ti]}13. {b}Fire Lit:{/b} 'Lighting a Fire', Pixabay, pixabay.com.", xpos=50, ypos=190, xmaximum=520)
    $ renpy.pause ()
    hide text

    $ ui.text("{space=[ti]}14. {b}Gymnopedies:{/b} 'Gymnopedie 1, 2 and 3, Erik Satie, performed by Kevin MacLeod, incompetech.com, licensed under Creative Commons: By Attribution 3.0 License http://creativecommons.org/licenses/by/3.0/.{vspace=[tx]}{space=[ti]}16. {b}Book Closing:{/b} 'Closing A Book', Pixabay, pixabay.com.{vspace=[tx]}{space=[ti]}18. {b}Various Pieces:{/b} 'Lacuna, Mysterious Happenings, Hunted, Adventure Calls, and Remember'. Music created by Tully Grimley.{vspace=[tx]}{space=[ti]}17. {b}The Final Battle:{/b} 'Gameland'. This music piece kindly created for the author by an enigmatic individual who wished to remain uncredited.", xpos=50, ypos=150, xmaximum=520)

    #Gymnopedie No. 3 Kevin MacLeod (incompetech.com) Licensed under Creative Commons: By Attribution 3.0 License http://creativecommons.org/licenses/by/3.0/


    $ renpy.pause ()
    hide text
    #TK: Appendix N
    #If at least 2 people have died
    #{b}Inspirational Reading:{/b} 'The Wonderful Wizard of Oz' (1900), L. Frank Baum.{vspace=[tx]}
    #The epic of gilgamesh. Beowulf. Grimm's fairy tales. 1001 arabian nights. The name of that japanese folk tale volume.
    #Terry pratchett. Coraline, niel gaiman. False Hydra, arnold K. The stolen Skin of Princess Sun, Patrick stuart, false machine. Do Androids Dream of Electric Sheep (for the silence scene).
    #The Moon Apes from Fire on the Velvet Horizon
    #The long sun, Gene Wolff. Hatoful Boyfriend. Higurashi when they cry. Doki Doki literature club. 999, ever 17, virtue's last reward.
    #Undertale.
    #Moby Dick?
    #MyHouse.WAD?
    #Yume Nikki
    #Various fairy tales available on the internet archives. https://sites.pitt.edu/~dash/perrault02.html
    #https://theconversation.com/how-early-australian-fairy-tales-displaced-aboriginal-people-with-mythical-creatures-and-fantasies-of-empty-land-185592
    #Ghost Trick: Phantom Detective
    #Phoenix Wright: Ace Attourney series
    #House of Leaves, S. by J.J. Abrams
    #Gravity's Rainbow (and run-on sentences)
    #The "Heart of Gold" scene from the Hitchhiker's guide to the galaxy game
    #$ renpy.pause ()
    #hide text

    $ ui.text("Written on the lands of the Turrbal and Jagera peoples. I pay my respects to their Elders, past and present. Sovereignty was never ceded.", xpos=50, ypos=190, xmaximum=520)
    $ renpy.pause ()

    play sound bookClose2 #pageFlip
    $ renpy.full_restart()

label resetGame:
    scene black with fade
    # stop music fadeout 4.0
    # stop music1 fadeout 4.0
    # stop music2 fadeout 4.0
    # stop music3 fadeout 4.0
    # stop music4 fadeout 4.0
    # stop music5 fadeout 4.0
    # stop music6 fadeout 4.0
    # stop ambient2 fadeout 4.0
    # stop ambient1 fadeout 4.0
    call musicSilence
    "{color=#ffffff}You have come to a dark place.{/color}"
    "{color=#ffffff}A gap in the manuscript.{/color}"
    "{color=#ffffff}Here, you can wipe everything away, and start again from the beginning.{/color}"
    "{color=#ffffff}Like it never happened at all.{/color}"
    "{color=#ffffff}Are you sure you want to do this?{/color}"
    #show hand onlayer transient:
        #yalign 0.711#0.743
        #xalign 0.5
    menu:
        "{color=#ffffff}You know it will never be like the first time.{/color}"
        "{color=#ffffff}Yes. I'm sure.{/color}":
            "{color=#ffffff}Very well.{/color}"
            "{color=#ffffff}Goodbye, for now.{/color}"
            $persistent._clear()
            $ renpy.full_restart()

        "{color=#ffffff}No. I want to remain here.{/color}":
            "{color=#ffffff}Very well.{/color}"
            "{color=#ffffff}Stay here a little longer.{/color}"
            call musicReturn
            $ renpy.full_restart()
