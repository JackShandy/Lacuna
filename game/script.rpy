# THE THIEF, THE WITCH, THE TOAD & THE MUSHROOM
#Script File

#=====================CUSTOM FUNCTIONS
#==Registering channel for ambient noise (Fire, rain)
init python:
    renpy.music.register_channel("ambient1","sfx",True,tight=True)
    renpy.music.register_channel("ambient2","sfx",True,tight=True)
    #This one is used for the city ambience when you open the door to the wolf
    renpy.music.register_channel("ambient3","sfx",True,tight=True)
    #This is all the wolf's talking
    renpy.music.register_channel("wolf","sfx",True,tight=True)

#==Purge Save Function
#Note: This function deletes all of the player's save files. This is necessary to work with the meta-narrative stuff I'm trying to do.
init python:
    def purge_saves():
        saves = renpy.list_slots()
        for save in saves:
            renpy.unlink_save(save)
        return

#==Default player name (persistent)
init python:
    def name_func(newstring):
        store.persistent.povname = newstring

#=====================PERSISTENT DATA
#This data carries over between save files and games, permanently.
init:

    #Persistent Player Name
    default persistent.povname = "Charlie"
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
    default persistent.toadVanished = False
    default persistent.witchVanished = False
    default persistent.thiefVanished = False
    default persistent.mushroomVanished = False

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
    default persistent.bcVanished = False
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
    default persistent.batVanished = False
    #Goblin 1, 2, 3, 4, and the goblin queen
    default persistent.goblinsVanished = False
    #Pig 1, 2, and 3
    default persistent.pigsVanished = False

    #If you get the final bad ending, who was the last to die?
    #Options: Thief, Toad, Witch, Mushroom
    #TK: Currently not set or used. Delete?
    default persistent.vanishedLast = "Thief"

    #Have you triggered the final ending where the book is born anew?
    #TK: Testing, change back to false
    default persistent.bookEnd = False

    #Has the book been burned?
    default persistent.bookBurned = False

    #What title did you choose for the book ending?
    default persistent.finaleTitle = "Cobbler"

    #The other randomly generated titles
    default persistent.name1Rand = renpy.random.randint(1,6)
    default persistent.name2Rand = renpy.random.randint(1,6)
    default persistent.name3Rand = renpy.random.randint(1,6)
    default persistent.name4Rand = renpy.random.randint(1,6)

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

    #Safe for work mode
    #Gets rid of all drawings with boobs / gore
    define sfw = True

    #Demo mode: cuts you off quickly
    define demo = True

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

    #Act 1, Chapter 2: The road to the village
    #How many pitiful Noooo's have you shouted
    define pitiful = 1
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

    #The final conversation with the wolf in the silence ending
    define lookUp = False
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

    ###==== Countdown
    #This screen counts down automatically and then jumps to a label once the countdown is finished
    #used for the BurnEnd and could also be useful for some random moments throughout the game
    init: ### just setting variables in advance so there are no undefined variable problems
        $ timer_range = 0
        $ timer_jump = 0
        $ time = 0

    screen countdown:
        timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])

    ## Burning Variables
    #For all the final conversations in the book burning ending
    define wolfBurning = False
    define miwBurning = False
    define mirBurning = False
    define wibBurning = False
    define mumBurning = False
    define gmBurning = False
    define thiefBurning = False

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

    #Covers with no bunnies vanished
    image cover = "cover.png"
    image cover5 = "cover-5.png"
    image cover6 = "cover-6.png"
    image cover9= "cover-9.png"
    image cover14= "cover-14.png"
    #Covers with 1 bunny vanished
    image covera = "covera.png"
    image cover5a = "cover-5a.png"
    image cover6a = "cover-6a.png"
    image cover9a= "cover-9a.png"
    image cover14a= "cover-14a.png"
    #Covers with 2 bunnies vanished
    image coverb = "coverb.png"
    image cover5b = "cover-5b.png"
    image cover6b = "cover-6b.png"
    image cover9b= "cover-9b.png"
    image cover14b= "cover-14b.png"
    #Covers with 3 bunnies vanished
    image coverc = "coverc.png"
    image cover5c = "cover-5c.png"
    image cover6c = "cover-6c.png"
    image cover9c= "cover-9c.png"
    image cover14c= "cover-14c.png"
    #Covers with all bunnies vanished
    image coverd = "coverd.png"
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
    image nightbg= "Backgrounds/night.png"
    image nightgodbg= "Backgrounds/nightgod.png"
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
    image deathbg =  "Backgrounds/death.png"
    image canopybg = "Backgrounds/canopy.png"
    image ruinsbg = "Backgrounds/ruins.png"
    image treenightbg = "Backgrounds/treeNight.png"
    image stranglerfigbg= "Backgrounds/stranglerFig.png"

    image forestbg= "Backgrounds/forest.png"
    image forest2bg = "Backgrounds/forest2.png"
    image forest4bg = "Backgrounds/forest4.png"
    image forest5bg = "Backgrounds/forest5.png"
    image darkforestbg= "Backgrounds/darkForest.png"

    image townfeastbg = "Backgrounds/town-feast.png"
    image towncrossroadsbg = "Backgrounds/town-cross.png"
    image townextbg = "Backgrounds/town-ext.png"
    image town3bg = "Backgrounds/town3.png"

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
    if sfw == False:
        image sabbathfullbg= "Backgrounds/sabbath-full.png"
    elif sfw == True:
        image sabbathfullbg= "Backgrounds/sabbath-full-s.png"
    image trainfullbg = "Backgrounds/train-full.png"
    image lakefullbg = "Backgrounds/lake-full.png"

    ##====Names
    image witchName= "Names/witch.png"
    image thiefName= "Names/thief.png"
    image toadName= "Names/toad.png"
    image toadQuollName= "Names/toad-quoll.png"
    image toadGeckoName= "Names/toad-gecko.png"
    image toadRatName= "Names/toad-rat.png"

    #TK: Clean up and make SFW mode work properly
    if sfw == False:
        image mushroomName= "Names/mushroom.png"
        image mushroom2Name= "Names/mushroom2.png"
        image mushroom3Name= "Names/mushroom3.png"
        image mushroom4Name= "Names/mushroom4.png"
        image goblinqueenName="Names/goblinqueen.png"
        image skinmaskName="Names/sm.png"
    elif sfw == True:
        image mushroomName= "Names/mushroom-s.png"
        image mushroom2Name= "Names/mushroom2-s.png"
        image mushroom3Name= "Names/mushroom3-s.png"
        image mushroom4Name= "Names/mushroom4-s.png"
        image goblinqueenName="Names/goblinqueen-s.png"
        image skinmaskName="Names/sm-s.png"

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
    image wivesName="Names/wives.png"
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


#=====================AUDIO
###Defining all Audio
init:
    ## Sound effects
    define audio.pageFlip = "audio/page-flip.mp3"
    define audio.pageFlip2 = "audio/page-flip2.wav"
    define audio.pageFlip3 = "audio/page-flip3.wav"
    define audio.whiteNoise = "audio/whiteNoiseEnding.mp3"

    ##Music
    define music.gameland = "audio/gameland.mp3"

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
    if persistent.bookBurned:
        show coverBurned with dissolve
        ""
        $renpy.quit()

    scene black
    show firelight animated onlayer over_screens zorder 99
    #If you're at the Book Ending, show 5 bunnies
    if persistent.bookEnd:
        show coverFinaleA with dissolve
    else:
        #Shows a random cover each time. 13.32% chance of a variant cover.
        $randomCover = renpy.random.randint(1, 30)
        #If no-one has vanished, all covers have all bunnies visible
        if persistent.vanished == 0:
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
        #If 1 character has vanished, 1 bunny disappears
        elif persistent.vanished == 1:
            if randomCover <=18:
                show covera with dissolve
            elif randomCover >=19 and randomCover <= 21:
                show cover14a with dissolve
            elif randomCover >=22 and randomCover <= 24:
                show cover5a with dissolve
            elif randomCover >=25 and randomCover <= 27:
                show cover6a with dissolve
            elif randomCover >=28 and randomCover <= 30:
                show cover9a with dissolve
        #If 2 characters have vanished, 2 bunnies disappear
        elif persistent.vanished == 2:
            if randomCover <=14:
                show coverb with dissolve
            elif randomCover >=15 and randomCover <= 18:
                show cover14b with dissolve
            elif randomCover >=19 and randomCover <= 22:
                show cover5b with dissolve
            elif randomCover >=23 and randomCover <= 26:
                show cover6b with dissolve
            elif randomCover >=27 and randomCover <= 30:
                show cover9b with dissolve
        #If 3 characters have vanished, 3 bunnies disappear
        elif persistent.vanished == 3:
            if randomCover <=10:
                show coverc with dissolve
            elif randomCover >=11 and randomCover <= 15:
                show cover14c with dissolve
            elif randomCover >=16 and randomCover <= 20:
                show cover5c with dissolve
            elif randomCover >=21 and randomCover <= 25:
                show cover6c with dissolve
            elif randomCover >=26 and randomCover <= 30:
                show cover9c with dissolve
        #If 4 characters have vanished, all bunnies and the wolf disappear
        elif persistent.vanished >= 4:
            show coverd with dissolve

    if persistent.phoneOn and persistent.vanished <=3:
        $renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True)
        #$ renpy.music.play("audio/wildlife.wav", fadein=0.5, channel="ambient1", loop=True)
        $renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True, relative_volume=0.5)
    elif persistent.bookEnd:
        $renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True)
        #$ renpy.music.play("audio/wildlife.wav", fadein=0.5, channel="ambient1", loop=True)
        $renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True, relative_volume=0.5)
    #else:
        #$renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True, relative_volume=0)
        #$ renpy.music.play("audio/wildlife.wav", fadein=0.5, channel="ambient1", loop=True)
        #$renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True, relative_volume=0)
        #$renpy.music.play("audio/windAmbience.mp3", relative_volume=0.2, fadein=1.5, channel="ambient3", loop=True)


    #with Pause(5)
    ""
    play sound pageFlip
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
            show title-wolf
        elif persistent.vanished >= 4:
            show title-allGone
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
    $povname = persistent.povname

    return

#Setting up the firelight and music whenever the game loads
label after_load:
    if persistent.phoneOn and persistent.vanished <=3:
        play sound pageFlip
        $renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True)
        $renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True, relative_volume=0.5)
    elif persistent.bookEnd:
        play sound pageFlip
        $renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True)
        $renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True, relative_volume=0.5)
    else:
        play sound pageFlip
    #     $renpy.music.play("audio/rain.wav", fadein=0.5, channel="ambient1", loop=True, relative_volume=0)
    #     $renpy.music.play("audio/fire.mp3", fadein=0.5, channel="ambient2", loop=True, relative_volume=0)
    #     $renpy.music.play("audio/windAmbience.mp3", relative_volume=0.2, fadein=1.5, channel="ambient3", loop=True)
    return

#This label is used to hide all backgrounds
label hideAll:
    hide nightbg
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
    $quick_menu = False
    call hideAll
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
        if persistent.bookEnd:
            show nightbg at artPos
            jump newStoryFinale
        show nightbg at artPos
        #TEST please delete
        #jump bookBurnedFinale

        if persistent.vanished == 0:
            "This maybe happened, or maybe did not."
            "The time is long past, and much is forgot."
            "Back in the old days, when wishing worked, your mother had twelve children and had to work night and day just to feed them."
            "When you were born as the thirteenth, she had no idea what to do. She took you up in her arms and ran into the darkness of the forest, promising that she would ask the first man she met to be your godfather."
        elif persistent.vanished == 1:
            "Neither here nor there, but long ago..."
            "Back in the old days, when the gods were real, your mother had ten children and had to work night and day just to feed them."
            "When you were born as the eleventh, she had no idea what to do. She took you up in her arms and ran into the darkness of the forest, promising that she would ask the first man she met to be your godfather."
        elif persistent.vanished == 2:
            "Once there was, and once there wasn't."
            "In the long-distant days of yore, when haystacks winnowed sieves, when genies played jereed in the old bathhouse, fleas were barbers, camels were town criers, I softly rocked my baby grandmother to sleep in her creaking cradle, in an exotic land, far, far away, there was a woman with 4 children who had to work day and night just to feed them."
            "When you were born to her as the fifth, she had no idea what to do. She took you up in her arms and ran into the darkness of the forest, promising that she would ask the first man she met to be your godfather."
            show noteFood onlayer transient zorder 100
        elif persistent.vanished == 3:
            "I've told you what's coming."
            "Back in the old days, when there was still a chance, your mother gave birth to you as her first and only child."
            show noteStop onlayer transient zorder 100
            "She had no idea what to do. She took you up in her arms and ran into the darkness of the forest, promising that she would ask the first man she met to be your godfather."
        elif persistent.vanished >= 4:
            jump allVanishedEnd

        call hideAll from _call_hideAll
        show forest4bg at artPos
        show scribble2 onlayer transient zorder 100
        "In the darkness of the forest, she may or may not have met a man in white."
        "(Is anything certain these days?)"
        "His right hand held a dove. His other hand held a gun. His other hand held a crisp dollar bill. His other hand held a pillar of fire."
        "His suit was perfect. His face was too bright to look upon. He already knew what was on her mind."
        if persistent.vanished ==1:
            show noteSilence onlayer transient zorder 100
        miw "Poor woman. Let me be the godfather."
        miw "I shall hold this child, and make sure [hes] happy on this Earth for the rest of [his] days."

    label firstMan:
            show hand onlayer transient:
                yalign 0.7#0.743
                xalign 0.5
            menu:
                miw "I will only ask one thing: [He] must work hard, and earn every dollar, and obey me above all else."
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
                            "But He was talking to Himself."
                            "He looked around, holding the child."
                            "There was no-one there."
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
                                "But He was talking to Himself."
                                "He looked around, holding the child."
                                "There was no-one there."
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
        "(What can any of us be certain of, except that the mercies of the Almighty are vaster than the deepest ocean and more numerous than all the pebbles on the land?)"
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
                        wib "Keep [him] safe for me until I come for [him]. I will send three messengers before me, to announce my arrival. "
                        if persistent.vanished == 3:
                            "But She was talking to Herself."
                            "She looked around, holding the child."
                            "There was no-one there."
                            "There never was.{vspace=200}{i}In your notes, write down that {b}You are Death's Godchild.{/b}{/i}"
                            $godfather = "Black"
                            jump chapter2
                        else:
                            mum "Just make sure you're there for the christening on Sunday."
                            show hand onlayer transient:
                                yalign 0.77#0.743
                                xalign 0.5
                            "But She was already leaving. She sunk into the earth with Her long, broken legs trailing behind her, until she was swallowed up whole.{vspace=160}{i}In your notes, write down that {b}You are Death's Godchild.{/b}{/i}"
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
                        "If she chose The Lord, turn to page 5.":
                            "In desperation, she renounced her foolish pride and sought the protection of the Most High Himself."
                            jump godYes
                        "If she chose The Devil, turn to page 6.":
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
                    "She tilted her head so that the moonlight fell upon it, and your mother saw that it was true. It was Lady Death herself."
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
        "The closets were filled with clothes of all sizes. In the bedroom was a hand-sewn quilt that fit just right."
        "There were fourteen pairs of shoes in the hall. Each day you would try a different pair."
        "How did these things come to pass? You didn't trouble yourself with such thoughts. Whenever you encountered these miracles, you simply said:"
        pov "The House provides."
        jump introMenu
    else:
        if godfather == "White":
            "And so you grew up as a kind and well-mannered child, and you made your mother proud."
            "You went to church every Sunday, and worked hard every day of your life, and never did you succumb to the beast within you. All the neighbours smiled and said \"That one has the mark of G-d upon [him].\""
            "Your Godfather was as good as His word. He appeared at church for the christening, and blessed you."
            "You soon found luck was always in your favour, and everyone took to calling you \"Fortune's Favourite\"."
        elif godfather == "Red":
            "And so you grew up as a wild and wilful child, and your drove your mother to distraction with your wickedness."
            "You obeyed no laws and no masters, and you roamed heedlessly across the hills and dales, cackling wildly and throwing mud in your wake, and all the neighbours said \"That one has the Devil's mark upon [him],\" and shut their doors."
            #TK: Beast reference from wolf about taboo
            "This so grieved your mother that she fell down dead."
            #"Your Godfather was as good as His word, although He could only watch the christening from outside the church window."
            "In spite of this, you still did not mend your wicked ways. Your ill deeds were rewarded, for you soon found that you could scarcely trip over a stone without unearthing precious diamonds and gems, and you became rich beyond the dreams of avarice."
        elif godfather == "Black":
            "And so you grew up as a solemn and quiet child, and you made your mother sick with worry with your gloomy ways."
            "You ate very little, and said even less, and every night you would stalk quietly through the forest shadows or sit for long hours watching insects crawl in stagnant ponds, and all the neighbours said \"That one has the mark of Death on [him],\" and shut their doors."
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
                "Your mother loved you very much, and you lived with her and your twelve siblings in a house on stilts on the banks of a muddy river in a vast rainforest. Each night you would fall fast asleep under a quilt she knitted for you."
            elif persistent.vanished == 1:
                "Your mother loved you very much, and you lived with her and your ten siblings in a house on stilts on the banks of a muddy river in a vast rainforest. Each night you would fall fast asleep under a quilt she knitted for you."
            elif persistent.vanished == 2:
                "Your mother loved you very much, and you lived with her and your four siblings in a house on stilts on the banks of a muddy river in a vast rainforest. Each night you would fall fast asleep under a quilt she knitted for you."

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
        #TK: >= 2?? Looks like a mistake
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
            #Haunted land to the North, further in land, the darkest depths of the rainforest where no living human has trod - The Thief
            if persistent.thiefVanished == True:
                $renpy.music.set_volume(0, delay=3.0, channel=u'ambient1')
                $renpy.music.set_volume(0, delay=3.0, channel=u'ambient2')
                $renpy.music.set_volume(0, delay=3.0, channel=u'music')
                show wolf9 onlayer transient zorder 100
                "To the north, there was nothing and no-one."
                $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient1')
                $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient2')
                $renpy.music.set_volume(1.0, delay=3.0, channel=u'music')
                jump neighbours
            else:
                "Do not ask lightly of the northern forest, my child."
                "That was a cursed place where wicked sprites and gleeful ghosts held sway. All who lived there slept uneasily in their beds as they heard the Goblin Train rattle past their windows each night."
                show thief onlayer transient zorder 100
                "The worst of them all was the Master Thief, a dextrous and sinister figure who was said to have all manner of powers."
                "It was said that on moonless nights their long, long, long arms would stretch through your window and up your stairs and into your bedroom and steal your dreams right out from under your pillow. In a single motion their long, long, long legs would carry them away to a secret hideout where they would place your forgotten thoughts in a sack of mysterious things, never to be seen again."
                "No jail could hold them and no lock could bar them entry. Or so it was said."
                jump neighbours
        "To learn about the lands to the east, turn to page 15." if not introNeighboursE:
            play sound pageFlip
            $introNeighboursE = True
            hide map1 onlayer screens
            $renpy.hide_screen(tag="map")
            if persistent.toadVanished == True:
                $renpy.music.set_volume(0, delay=3.0, channel=u'ambient1')
                $renpy.music.set_volume(0, delay=3.0, channel=u'ambient2')
                $renpy.music.set_volume(0, delay=3.0, channel=u'music')
                show wolf8 onlayer transient zorder 100
                "To the east, there was nothing and no-one."
                $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient1')
                $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient2')
                $renpy.music.set_volume(1.0, delay=3.0, channel=u'music')
                jump neighbours
            else:
                #Coastal swamps and mangroves to the east, leading to the beach and the ocean - The Toad
                "To the east, the river flowed down to the coast. The mangrove trees swayed in the summer heat, and the air thrummed with chanting in honour of the insect god, Karnopticon."
                show toad onlayer transient zorder 100
                "On the edge of the swamp was a grand manor, owned by a noble frog lord."
                "He was rarely seen, but people whispered that he was wiser than Solomon and richer than Midas."
                jump neighbours
        "To learn about the lands to the south, turn to page 20." if not introNeighboursS:
            play sound pageFlip
            $introNeighboursS = True
            hide map1 onlayer screens
            $renpy.hide_screen(tag="map")
            #Flowing river to the south, Amazonian, fungi and silver-white - The Mushroom
            if persistent.mushroomVanished == True:
                $renpy.music.set_volume(0, delay=3.0, channel=u'ambient1')
                $renpy.music.set_volume(0, delay=3.0, channel=u'ambient2')
                $renpy.music.set_volume(0, delay=3.0, channel=u'music')
                show wolf10 onlayer transient zorder 100
                "To the south, there was nothing and no-one."
                $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient1')
                $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient2')
                $renpy.music.set_volume(1.0, delay=3.0, channel=u'music')
                jump neighbours
            else:
                show mushroom onlayer transient zorder 100
                "Ah! In fact, the south river and the forest around it was watched over by a wise mushroom ambassador, who had owned these lands since before anyone could remember."
                "She was often away brokering trade agreements and peace treaties and delicate alliances between the many trees and plants and old warring ferns of the forest."
                "But every now and then, on cold clear nights, you could see her walking through the depths of the forest with her white veil and delicate waves of silver spores drifting behind her."
                "She allowed your family to live on the river and use her lands, under one condition."
                m "Ask not of what concerns you not, lest you hear what pleases you not."
                "Your family accepted her wishes, and so you let each other be."
                jump neighbours
        "To learn about the lands to the west, turn to page 26." if not introNeighboursW:
            play sound pageFlip
            $introNeighboursW = True
            hide map1 onlayer screens
            $renpy.hide_screen(tag="map")
            #Mountains to the West, home to devils and witch's sabbaths - Thornton Peak- The Witch
            if persistent.witchVanished == True:
                $renpy.music.set_volume(0, delay=3.0, channel=u'ambient1')
                $renpy.music.set_volume(0, delay=3.0, channel=u'ambient2')
                $renpy.music.set_volume(0, delay=3.0, channel=u'music')
                show wolf11 onlayer transient zorder 100
                "To the west, there was nothing and no-one."
                $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient1')
                $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient2')
                $renpy.music.set_volume(1.0, delay=3.0, channel=u'music')
                jump neighbours
            else:
                show witch onlayer transient zorder 100
                "None dared venture to the western mountains, for all the lands around it were said to be home to a terrible witch."
                "People said her hut lay deep under a secret lake, and she would emerge on moonless nights when the waters of that lake turned strange and silver-green."
                "They said the witches held their Sabbath on the mountain to the east, and when the sky was clear you could see the peak blaze with fire, and the Destroyer himself would emerge to dance in the firelight."
                jump neighbours
        "To continue, return to page 9.":
            play sound pageFlip
            hide map1 onlayer screens
            $renpy.hide_screen(tag="map")
            jump introMenu

#You begin to walk to the festival
label introMenu:
    if persistent.vanished == 3:
        $introMenuSentence = "You woke every morning to silence."
    else:
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
                "You dared not venture out often. Whenever you did, you felt the pressure of that gigantic emptiness crushing in all around you like a bottomless ocean, and fled quickly back to the safety of your home."
            else:
                "Yours was a many-haunted land, my child."
                "Back in those days you could barely take a step without stumbling over a fiend, ghost, bloody bones, flay-boggart, bugaboo or sprite. Every house was haunted and the Devil lurked at every crossroad."
                "In fact the whole earth was overrun with trolls, hob-and-lanthorns, gringes, cutties and nisses, boguests, bonelesses, boggleboes, black-bugs and night-bats, clabbernappers, corpse lights, candles and Gabriel-hounds, mawkins, hodge-pochers, korreds, lubberkins, cluricauns, hob-thrushes, tod-lowries, Jack-in-the-Wads, men-in-the-oak, dudmen, yeth-hounds, mormos, changelings, redcaps, colt-pixies, Tom-thumbs, madcaps, scrags, specters, scar-bugs, shag-foals, Jinny-burnt-tails, dopple-gangers, and apparitions of every shape, make, form, and fashion."
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
                "Every year, on the day before your birthday, the village would throw a great festival for no reason anyone could name. On these nights you always felt sad and strange."
                "You would avoid the festival and stare deep into the woods all through the night."
            elif persistent.vanished == 2:
                #TK: finish silence.
                "Well, it was a happy home. The house was always full of chatter from your four siblings, and you were always cramped for space with all of them around."
                "But at night, when the others had gone to bed, you felt a great silence lurking in the house."
                "Underneath the old floorboards. Inside the crooked walls."
                "Waiting for it's time to come."
            elif persistent.vanished == 3:
                $renpy.music.set_volume(0, delay=4.0, channel=u'ambient1')
                $renpy.music.set_volume(0, delay=4.0, channel=u'ambient2')
                $renpy.music.set_volume(0, delay=4.0, channel=u'music')
                "You lived a contented life. No-one bothered you. The stoop was full of fresh-cut logs for the fireplace. The house had many beds, so that you never lacked for a place to sleep."
                pov "The House provides."
                "You kept yourself busy and distracted as much as you could. But every day there came that terrible time when you finally had to lie down alone in bed."
                "As you lay awake in bed at night, you felt the silence."
                "It oozed up from between the floorboards and out of the cracks in the walls and slowly poured in from the windows, no matter how much you tried to stop them up."
                "It had nothing to hide now. It had already won."
                "Each night the sound of the fire would slowly die until there was nothing left to protect you, and you could do nothing but lie in the endless suffocating abyss of silence until you mercifully fell asleep."
            jump introMenu
        "To continue the story, turn to page 34.":
            if persistent.vanished == 3:
                "Soon you could stand it no longer. You searched the pantry and found a package wrapped up with a coinpurse, along with some bread and meat."
                pov "The House provides."
                #"You gathered up these provisions and reached for the door, but as you took hold of the handle you stopped."
                #"You could feel it outside."
                #"The howling pressure of the vacuum beyond pressed against the door like a physical force, the weight of it paralysing you."
                #"You could not stand the thought of the trip down the empty road to that silent village where no-one lived."
            if godfather == "Black":
                "Alas, all too soon, the eve of your 18th birthday arrived. You set about in wild terror, for you knew that your Godmother would own your immortal soul as soon as the clock struck midnight."
                "You had no doubt that She would soon send Her three messengers for you, and then take you down to the kingdom of ruin forever."
            else:
                "Alas, all too soon, the eve of your 18th birthday arrived. You set about in wild terror, for you knew that your Godfather would come to take you away as soon as the clock struck midnight, and you had no wish to leave just yet."
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

    call hideAll from _call_hideAll_2
    show forestbg at artPos
    show spiral5 onlayer transient zorder 100

    "And so you took up your belongings and strode on down the road to the festival."
    "The twilight set in, and the crickets and cicadas all around began their chattering and squabbling, and the evening birds began to laugh and trill, and the wet cool mist of the rainforest settled around you."
    "The crooked old water-dragons looked sideways at you and plotted their long, slow schemes."
    "A small turtle saw you coming and fled into the water with a plop."

    # Act 1, Chapter 3: The Mushroom.
    #You follow the mushroom and find a bunch of mushroom clones
    if persistent.mushroomVanished == True:
        #play audio wind fadeout 25.0
        $renpy.music.set_volume(0, delay=3.0, channel=u'ambient1')
        $renpy.music.set_volume(0, delay=3.0, channel=u'ambient2')
        $renpy.music.set_volume(0, delay=3.0, channel=u'music')
        show wolf8 onlayer transient zorder 100
        "As you walked down the road thusly, sweating in the warmth of the summer night, you heard nothing."
        "You saw no-one."
        "You were alone."
        "You continued on down the empty road."
        $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient1')
        $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient2')
        $renpy.music.set_volume(1.0, delay=3.0, channel=u'music')
        jump thief1
    else:

        "As you walked down the road, you saw the wise mushroom moving through the deep darkness of the trees, her pale spores flowing in a train behind her."
        show hand onlayer transient:
            yalign 0.7#0.743
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
                        "Inside you were shocked to find the tree completely hollow. A great cavern was formed inside it, cold as ice despite the heat outside."
                        "The floor of the cavern was piled with rubies and pearls and glinting onyx and solid gold pieces, larger than your fist."
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
                                #TK: "The you with the mask" - change this, the thief's art is no longer wearing a mask
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
                                    "She looked vaguely around the glittering splendour before you."
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
                                                pov "I'm seeking a way to escape being taken by my Godfather, the old man in heaven. Surely the story of my adventure will be unique enough for you."
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
                                        m "I'm afraid I don't know if I can help. I know a little about pale-faced Death, but I've never met your godfather."
                                        "A large grandfather clock in the corner suddenly chimed, and she looked up with a start."
                                        m "Oh dear. Time marches on, even for me."
                                        m "I'm sorry to be so rude but I'd better be off. Come back after the festival, and I may be able to help."
                                        m "Please take care of yourself, dear. All of yourself."
                                        "And before you could reply to this strange remark, she took your cup and ushered you out of the door in an instant."
                                        "You took up your bag and set off down the road once more."
                                        jump thief1
                    "If you went back to the path, turn to page 28.":
                        "You rushed back to the path, worried at any moment that you might be seen."
                        "\"Thank goodness,\" you thought to yourself, \"that I know not to ask of what concerns me not! That could led me to some kind of dangerous and magical adventure.\""
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
        if persistent.thiefVanished == True:
            #play audio wind fadeout 25.0
            $renpy.music.set_volume(0, delay=3.0, channel=u'ambient1')
            $renpy.music.set_volume(0, delay=3.0, channel=u'ambient2')
            $renpy.music.set_volume(0, delay=3.0, channel=u'music')
            show wolf7 onlayer transient zorder 100
            "As you walked down the road thusly, sweating in the warmth of the summer night, you heard nothing."
            "You saw no-one."
            "You were alone."
            "You continued on down the empty road."
            $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient1')
            $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient2')
            $renpy.music.set_volume(1.0, delay=3.0, channel=u'music')
            jump toadIntro
        else:
            "As you were walking down the road thusly, you came upon an old beggar-woman."
            "Her eyes were blind, and her back was crooked in 5 directions at once, and her hair floated all around her head like twisting grey fog, and she hobbled about with only the aid of an old cane to help her along."
            mys "Ho, young traveller."
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
                            t "They'll never catch me, no matter how they try. I have placed my head in the wolf's mouth and never felt the sting of its jaws."
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
                                                show hand onlayer transient:
                                                    yalign 0.743#0.743
                                                    xalign 0.5
                                                "From that day on he would always be your loyal friend and ally, and the two of you would get through more scrapes and misadventures than I have time to relate tonight.{vspace=100}{i}In your notes, write down that you {b}have a pig.{/b}{/i}"
                                                $pig = True
                                            "If you let the pig run free and wild, as nature intended, turn to page 8.":
                                                "With sorrow, you removed the cloak and wig, and gave the pig his freedom."
                                                "He oinked joyfully and fled off into the night. From there, he joined with the wild bush pigs, and founded a great kingdom that was as a scourge upon the earth."
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
                                    $pitiful +=1
                                    jump thiefChase
                                "If you let them go, turn to page 27.":
                                    "You walked sorrowfully back to the road, cursing Old Gooseberry for your misfortune."
                        show hand onlayer transient:
                            yalign 0.8#0.743
                            xalign 0.5
                        "As you trudged back to the road you discovered that all of your coins had been stolen and replaced with I.O.U.'s, the bread was now nothing but crumbs, and the meat had been turned into a live possum with a label on it saying \"Ham\". It bit you and fled into the trees.{vspace=100}{i}In your notes, write down that {b}Your things have been stolen.{/b}{/i}"
                        if godfather == "White":
                            "And so you set about wailing and beating the ground and tearing at your paper clothes, crying out saying \"Oh Lord, how could you treat your servant thus?\""
                            "After a long time you drew yourself up from the ground and spoke to the trees."
                            pov "Hear me now, Thief. With the Lord as my witness, I will not rest until you see justice."
                        if godfather == "Red":
                            "And so you set about wailing and beating the ground and tearing at your paper clothes, crying out saying \"Oh my Lord and Master, the Father of Lies, how could you forsake me? I, who have outdone all others in wickedness, and served you faithfully in evil for all these long years?\""
                            "After a long time you drew yourself up from the ground and spoke to the trees."
                            pov "Hear me now, Thief. My godfather is the Devil, and my blood runs with nothing but spite, and I will not rest until the Prince of Darkness fastens His hands around your ankles and drags you straight down to Hell where you belong."
                        if godfather == "Black":
                            "And so you set about wailing and beating the ground and tearing at your paper clothes, crying out saying \"Lady Death, take me now!\""
                            "After a long time you drew yourself up from the ground and spoke to the trees."
                            pov "Hear me now, Thief. My godmother is the end of all things, and I will not rest until you have been dragged down into Her icy waters where you belong."
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
                            t "They'll never catch me, no matter how they try. I have placed my head in the wolf's mouth and never felt the sting of its jaws."
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
                            call hideAll
                            show darknessbg at artPos
                            "Without a word, you left the old woman behind and walked deeper and deeper into the woods."
                            jump woodsInvestigate


    # Chapter 1, Part 5: The Toad.
    label toadIntro:
        call hideAll from _call_hideAll_9
        show forest5bg at artPos
        if persistent.toadVanished == True:
            #play audio wind fadeout 25.0
            $renpy.music.set_volume(0, delay=3.0, channel=u'ambient1')
            $renpy.music.set_volume(0, delay=3.0, channel=u'ambient2')
            $renpy.music.set_volume(0, delay=3.0, channel=u'music')
            show wolf1 onlayer transient zorder 100
            if pig:
                "As you walked down the road with the pig trotting beside you, you heard nothing."
                "You saw no-one."
                "You were alone."
                "You continued on down the empty road."
            else:
                "As you walked down the road, sweating in the warmth of the summer night, you heard nothing."
                "You saw no-one."
                "You were alone."
                "You continued on down the empty road."
            $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient1')
            $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient2')
            $renpy.music.set_volume(1.0, delay=3.0, channel=u'music')

            jump chapter6
        else:
            if pig:
                "As you walked down the road with the pig trotting beside you, you heard a great clattering of hooves, and turned to see four horses pulling a magnificent golden carriage."
            else:
                "As you walked down the road, sweating in the warmth of the summer night, you heard a great clattering of hooves behind you, and turned to see four horses pulling a magnificent golden carriage."
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
            else:

                eg "Hold!"

                "A rich, low voice like dark mahogany came from behind the curtains, showing the distinctive tones of one of good breeding and character. The horses slowed to walk beside you."
                "A slender hand holding a long cigarette holder emerged from the curtains and beckoned to you. The shadow of the man inside swirled a glass of brandy in his other hand."
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
                "If you accepted the lift, turn to page 54.":
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
                        "The incense you smelled was nothing but the reek of dirt and mud, the brandy was pond scum, the gleaming carriage was just a rotten old squash, and the graceful arm that beckoned you from behind the curtain was nothing but a wooden prop the toad held in his webbed hand."
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
                                    pov "I'm searching for a way to escape my godfather, the King of Kings."
                                    pov "He will be here to take me away at midnight, and I have no wish to leave."
                                    f "A sticky situation indeed!"
                                    f "I have talked with the Lord many times, of course."
                                    show tornPage1 onlayer screens zorder 101
                                    show tornPage1bg onlayer screens zorder 99
                                    f "Why, just the other day He said to me, He said Brildebrogue! How did I ever manage to make one as handsome and charming as you? Why, even a deity with my own talents (which are quite decent of course, though nothing in comparison to your own gifts) can scarcely imagine bringing such a golden figure out of the fires of creation! At this I swung back my head in a great laugh, like so: HA! And my golden mane whipped about me in the wind, and all were charmed by my wit and good humour, so much so that they joined me in an uproarious shout of laughter, such that the whole world could hear it - in fact I have no doubts that you must have heard it yourself, even out here in this backwater location, so loud was the sound, although perhaps you took it for a minor earthquake."
                                    hide tornPage1 onlayer screens
                                    hide tornPage1bg onlayer screens
                                    f "Perhaps I could put in a good word for you with Him later. Pond scum?"
                                if godfather == "Red":
                                    pov "I'm searching for a way to escape my godfather, Old Scratch."
                                    pov "He will be here to take me away at midnight, and I have no wish to leave."
                                    f "A sticky situation indeed!"
                                    f "I know the Black One well myself, in fact."
                                    show tornPage2 onlayer screens zorder 101
                                    show tornPage2bg onlayer screens zorder 99
                                    f "Why just the other day I said to Him, I said Devil! How dare you twist the lives of these innocent souls here, tricking them into a terrible life of debauchery and ill-humour, just to suit your own devious and ill-conceived personal goals, when you could instead behave yourself and simply put things to rights like a well-mannered member of society such as myself? At my words, He shrank back with a most timiditous cowardice, and I saw Him gulp in nervous anxiety most profound, such was His fear of my great anger (which can be quite considerable when my dander is up, although of course I take care to remain in good humour for the purpose of conversing with polite gentlefolk such as yourself). In an instant, He swore never to do evil again, and scurried away over hill and dale without a backwards glance."
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
                                    f "I've chatted with Death many times, of course, and so on this occasion I marched right on up to Her and said \"Unhand my mother, you ruffian! I cannot allow you to continue this wave of terror you have inflicted across the forest left and right, taking away women and old maids and children at will, rich and poor alike, before their time has come to pass! Release her at once, or I'll have to get extremely unpleasant with you (And you do NOT wish to see me when I'm being unpleasant, I assure you, such a thing has driven many hard men to tears!) At this stern talking-to from me, She released my mother at once with a sincere apology, and I need hardly say that She has not darkened our door again."
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
                                f "But I'm sure your little festival will be quite quaint, too. Pond scum?"
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
                            call hideAll
                            show darknessbg at artPos
                            "Without a word, you left him behind and walked deeper and deeper into the woods."
                            jump woodsInvestigate

    #---- Act 1, Chapter 6: The Village.
    label chapter6:
        if mushroomArc == 0 and thiefArc == 0 and toadArc == 0:
            if godfather == "Red":
                "And so it was that you stayed on the path the whole way, ignoring your wanton nature and never once being tempted by the offers of strangers."
            else:
                "And so it was that you stayed on the path the whole way, following your mother's advice and never once being tempted by the offers of strangers."
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

        if persistent.witchVanished == True:
            $renpy.music.set_volume(0, delay=3.0, channel=u'ambient1')
            $renpy.music.set_volume(0, delay=3.0, channel=u'ambient2')
            $renpy.music.set_volume(0, delay=3.0, channel=u'music')
            show wolf11 onlayer transient zorder 100
            "As you walked up to the village, you saw nothing."
            "There was no-one standing guard on the village outskirts."
            "The woods were silent."
            "No-one greeted you."
            "You slowly walked out of the woods and into the village streets."
            $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient1')
            $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient2')
            $renpy.music.set_volume(1.0, delay=3.0, channel=u'music')
            jump villageExplore1
        else:

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
                    "A witches Sabbath was afoot. A great fire raged on the peak before you, and the witches danced before it."
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
                    "A great rumbling broke out all around you. You twisted around to look back. Behind you, you saw the mountain split open and ten thousand hogs burst up from beneath the earth. The witches screeched in demonic glee."
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
                            call hideAll
                            show darknessbg at artPos
                            "Without a word, you left the hunter behind and walked deeper and deeper into the woods."
                            jump woodsInvestigate

    label villageExplore1:
        show hand onlayer transient:
            yalign 0.728#0.743
            xalign 0.5
        menu:
            "The town was overflowing with people bustling about and preparing for the festival, pulling up chairs and laying great tables around the enormous bonfire in the centre of town."
            "If you looked at the food, turn to page 36." if not foodLook:
                call hideAll from _call_hideAll_15
                show towncrossroadsbg at artPos
                $foodLook = True
                "Over the bonfire was a great suckling pig on a spit, slathered in rosemary and garlic butter and herbs of all types, and stuffed with breadcrumbs and fresh figs and crisp walnuts and apples and all the fruits of the earth."
                if pig:
                    "Your pig looked upon it sadly, and shook its head at the foolish greed of the human race."
                "The mangos were in season, and the trees were so weighed down with them that they would fall off and roll down the town gutters, so that the whole town was rich with the sweet scent of fruit mixed with the smell of wood smoke and spices and crackling fat from the cooking fires."
                "Those mangos that didn't roll away fast enough were plucked up immediately and eaten by gleeful clouds of fruit bats that chittered and cackled in a great whirling chaos overhead."
                "Colossal glass bowls of red sangria were placed at each table, filled with fresh oranges and giant yellow lemon slices, ground cinnamon and brandy and crisp sweet apples and ginger ale."
                "For desert there were giant lemon meringue pies made from lemons as big as your fist, covered in fresh-whipped meringue from the Baker's parlour."
                jump villageExplore1
            "If you sat down with the rest of the guests without delay, turn to page 37.":
                call hideAll from _call_hideAll_16
                show towncrossroadsbg at artPos
                "You took your place at the table."
    "All the villagers were there."
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
            if persistent.mayVanished = False:
                may "What!? Why would she spurn our invitation?"
        else:
            "But still, the witch did not arrive, and soon everyone was a frenzy of worry."
        if persistent.goVanished == False:
            gm "We've given offence to her somehow. She'll turn all our hair to straw and infest all our picnics with ants. None shall escape."
        if persistent.goVanished == False:
            go "All our spoons will rust, and our forks will get stuck in the drawers! I already have enough on my hands dealing with the geese!"
        if persistent.thiefVanished == False and not persistent.shVanished:
            "The panic increased when the Sparrow-Herder rushed in and waved for attention."
        else:
            "There was a great hubbub and outcry, and the villagers trembled and wept in fear of the terrible curse."
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
        gm "Oh lord, I knew it. I swear I can hear the rattling of the Goblin Train already."
        sh "The entire suckling pig is missing. Quick - check your valuables!"
        "The whole town turned out their pockets and discovered that all their spare change had been taken and replaced with live rats, which shrieked and leapt away and ran into the forest."
        town "NOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        OOOOOOOOOOOOOOOOOOOOOOOOOOOOO!"
        gm "Told you so."
        if demo:
            jump demoEnd
        jump village

# Act 2: Chapter I - Chat and investigation
#You can investigate the village and choose between 2 main pathways
label village:
    #TK: Test: End of the demo
    show hand onlayer transient:
        yalign 0.68#0.743
        xalign 0.5
    call hideAll from _call_hideAll_17
    show towncrossroadsbg at artPos
    if persistent.vanished >= 3:
        show noteHome onlayer transient zorder 100
    menu:
        "You stood in the middle of the village."
        "If you investigated the banquet, turn to page 64.":
            $renpy.music.set_volume(1.0, delay=2.0, channel=u'ambient1')
            $renpy.music.set_volume(1.0, delay=2.0, channel=u'ambient2')
            $renpy.music.set_volume(1.0, delay=2.0, channel=u'music')
            jump banquet
        "If you investigated the edge of town, turn to page 70.":
            $renpy.music.set_volume(1.0, delay=2.0, channel=u'ambient1')
            $renpy.music.set_volume(1.0, delay=2.0, channel=u'ambient2')
            $renpy.music.set_volume(1.0, delay=2.0, channel=u'music')
            jump town
        "If you turned around and went home, turn to page 1.":
            #TK: This option gets ripped out if you try it, then go back without succeeding
            if turnedHome == 0:
                if persistent.vanished >=2:
                    show wolf2 onlayer transient zorder 100
                $renpy.music.set_volume(0.9, delay=3.0, channel=u'ambient1')
                $renpy.music.set_volume(0.9, delay=3.0, channel=u'ambient2')
                $renpy.music.set_volume(0.9, delay=3.0, channel=u'music')
                "You don't want to go that way"
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
                $renpy.music.set_volume(1.0, delay=2.0, channel=u'ambient1')
                $renpy.music.set_volume(1.0, delay=2.0, channel=u'ambient2')
                $renpy.music.set_volume(1.0, delay=2.0, channel=u'music')
                h "There you are! We've been looking all over for you!"
                h "Come on, let's get back to the feast."
                if not persistent.thiefVanished and not persistent.mushroomVanished:
                    h "We need your help to help track down that dastardly Master Thief!"
                    h "Here, I'll help you find your way back."
                    "The hunter took hold of your arm with a surprisingly strong grip and escorted you back into the village."
                    $turnedHome +=1
                    jump town
                elif not persistent.witchVanished and not persistent.ToadVanished:
                    h "We need your help to help with this terrible curse problem we're having!"
                    h "Here, I'll help you find your way back."
                    "They took hold of your arm with a surprisingly strong grip and escorted you back into the village."
                    $turnedHome +=1
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
                    "They looked down."
                    h "My hands... they haven't been working properly. They don't do what I tell them to do anymore."
                    h "I'm sorry. I think I need to rest."
                    "Without a word, they turned and walked back to the village."
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
                #TK: Wolf scene
                jump wolf
            $turnedHome +=1
            jump village
        # "If you talked to the Gutterling, turn to page 56." if persistent.vanished>=1 and gutterlingChat <=2:
        #     if persistent.vanished == 1:
        #         if gutterlingChat == 0:
        #             g "'Allo."
        #             g "Here's a tip. If you talk to people multiple times, they might have more to say."
        #             g "It's true! Try it on me."
        #         if gutterlingChat == 1:
        #             g "There's the spirit mate!"
        #         if gutterlingChat == 2:
        #             g "It works on more than just people too, y'know. "

#The banquet with the toad and the witch path
label banquet:
    call hideAll from _call_hideAll_18
    show townfeastbg at artPos
    show scribble1 onlayer transient zorder 100
    "You walked down to the river, where the banquet was laid out. Some folks were gripping each other tight and crying out at the misfortune that had befallen their town. Others simply sat in glum silence."
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
            "You looked over the sad scene."
            "If you talked to the woeful villagers, turn to page 84." if not banquetChat:
                "They paid no attention to you, but continued shaking their heads and wailing with wretched misery."
                $banquetChat = True
                jump banquetMenu
            "If you talked to the Sparrow-Herder, turn to page 85."  if sparrowherderChat <= 4 and not persistent.shVanished:
                if persistent.witchVanished and sparrowherderRand == 2:
                    $sparrowherderRand =3
                if sparrowherderRand ==1:
                    if sparrowherderChat == 0:
                        sh "G'day."
                        sh "The ruin to the south has many poisonous beasts. Be sure to carry Antidotes if you head that way."
                    elif sparrowherderChat == 1:
                        show spirit3 onlayer transient zorder 100
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
                elif sparrowherderRand == 3:
                    if sparrowherderChat == 0:
                        sh "G'day."
                        sh "Be careful as you walk around town, friend. Stick to the centre of the street, and never cross the gutters without crossing your path with salt."
                        sh "The Gutterlings hide there."
                    elif sparrowherderChat == 1:
                        sh "They are thin, pale and wretched creatures."
                        sh "They rise out of the earth when the gutters overflow with the summer rains."
                    elif sparrowherderChat == 2:
                        sh "They will follow you slowly, concealing themselves with leaves and pieces of trash."
                        sh "When you are alone, they reach out their long, long arms, wrap around you, and drag you into the storm drain."
                    elif sparrowherderChat == 3:
                        sh "What happens then? Well..."
                        sh "Some say they keep you there for years, feeding you trash and sewer water to keep you alive."
                        sh "From your body they will harvest small pieces of flesh. A thumb, a toe, an ear."
                        sh "From these pieces, they will grow more Gutterlings."
                    elif sparrowherderChat >= 4:
                        sh "How do I know all this? The sparrows told me."
                $sparrowherderChat +=1
                jump banquetMenu
            "If you talked to the Mayor, turn to page 82." if mayorChat <= 6 and not persistent.mayVanished:
                #if mayorRand ==1:
                if mayorChat == 0:
                    if persistent.witchVanished:
                        may "If you're going out, be wary! They say Moon-Head walks these roads tonight."
                    else:
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
                        p1 "Cast off this madness, Montgomery. Come back to us. We all miss you."
                        show wolf3 onlayer transient zorder 100
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
                        show wolf6 onlayer transient zorder 100
                        p2 "You see, I'm expecting someone."
                    if pigChat == 3:
                        show wolf7 onlayer transient zorder 100
                        p2 "I can hear them coming now. In the pipes."
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
                if toadStole and not persistent.witchVanished:
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
                        f "Try the crackling, it's marvellous."
                        "If you asked about the feast, turn to page 89." if not toadFeast:
                            f "Yes, it's adequate, perfectly adequate."
                            "He opened his mouth wide and took a bite out of a flank of roast pork."
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
                                $renpy.music.set_volume(0.5, delay=3.0, channel=u'ambient1')
                                $renpy.music.set_volume(0.5, delay=3.0, channel=u'ambient2')
                                $renpy.music.set_volume(0.5, delay=3.0, channel=u'music')
                                f "I came to this village to..."
                                show wolf9 onlayer transient zorder 100
                                f "To, ah..."
                                "He looked down at his wineglass."
                                "His brow wrinkled."
                                $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient1')
                                $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient2')
                                $renpy.music.set_volume(1.0, delay=3.0, channel=u'music')
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
                            may "I heard they stole a horse right out from under its rider."
                            sh "I heard they stole the King of Spain right out from under his wife."
                            f "Well, I heard that every winter they shrink down to the size of a pin, and hide away in your house to steal all your odd socks and hairpins and loose change."
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
                                    $renpy.music.set_volume(0.3, delay=3.0, channel=u'ambient1')
                                    $renpy.music.set_volume(0.3, delay=3.0, channel=u'ambient2')
                                    $renpy.music.set_volume(0.3, delay=3.0, channel=u'music')
                                    f "I may know someone who can assist with that. Her name is..."
                                    show wolf7 onlayer transient zorder 100
                                    f "Her name..."
                                    f "..."
                                    $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient1')
                                    $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient2')
                                    $renpy.music.set_volume(1.0, delay=3.0, channel=u'music')
                                    f "Never mind, I must have been mistaken. More ham?"
                                else:
                                    f "Perhaps the witch will know something about it. You should join me in hunting her down!"
                            elif godfather == "White":
                                pov "I need a way to escape my godfather, the Lord. Can you help me?"
                                f "Possibly, possibly."
                                if persistent.witchVanished:
                                    $renpy.music.set_volume(0.3, delay=3.0, channel=u'ambient1')
                                    $renpy.music.set_volume(0.3, delay=3.0, channel=u'ambient2')
                                    $renpy.music.set_volume(0.3, delay=3.0, channel=u'music')
                                    f "I may know someone who can assist with that. Her name is..."
                                    show wolf7 onlayer transient zorder 100
                                    f "Her name..."
                                    f "..."
                                    $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient1')
                                    $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient2')
                                    $renpy.music.set_volume(1.0, delay=3.0, channel=u'music')
                                    f "Never mind, I must have been mistaken. More ham?"
                                else:
                                    f "Perhaps the witch will know something about it. You should join me in hunting her down!"
                            elif godfather == "Red":
                                pov "I need a way to escape my godfather, the Devil. Can you help me?"
                                if persistent.witchVanished:
                                    $renpy.music.set_volume(0.3, delay=3.0, channel=u'ambient1')
                                    $renpy.music.set_volume(0.3, delay=3.0, channel=u'ambient2')
                                    $renpy.music.set_volume(0.3, delay=3.0, channel=u'music')
                                    f "I may know someone who can assist with that. Her name is..."
                                    show wolf7 onlayer transient zorder 100
                                    f "Her name..."
                                    f "..."
                                    $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient1')
                                    $renpy.music.set_volume(1.0, delay=3.0, channel=u'ambient2')
                                    $renpy.music.set_volume(1.0, delay=3.0, channel=u'music')
                                    f "Never mind, I must have been mistaken. More ham?"
                                else:
                                    f "I'm sure the witch would know something about that. Rumour is that she dances with the Devil on cold, moonless nights! You should join me in hunting her down."
                            $toadHelp = True
                            jump toadConvo2
                        "If you made your excuses and left, turn to page 83.":
                            f "Return soon! You can't possibly leave without sampling some of this fine green mango salad over here, absolutely sensational!"
                            jump banquetMenu
            "If you wandered into the woods, turn to page 84." if persistent.toadVanished or persistent.witchVanished:
                if persistent.thiefvanished == False and persistent.mushroomvanished == False and shStopped == False:
                    sh "H-hold on, friend! Leaving so soon?"
                    sh "We're just hatching a plan to catch that dastardly Master Thief. We could use your help!"
                    sh "Come on, let's get back to the village."
                    $shStopped = True
                    jump town
                else:
                    "You turned and walked out into the darkness of the woods."
                    jump toadWitchInvestigate
            "If you returned to the middle of the village, return to page 50.":
                "You turned and walked back to the centre of the village."
                jump village

#The outskirts of town, with the thief and mushroom path
label town:
    call hideAll from _call_hideAll_19
    show townextbg at artPos
    if persistent.vanished >=2:
        show noteWaiting onlayer transient zorder 100
    if persistent.thiefVanished:
        "You walked out to the edge of town."
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
            "If you investigated the tarp, turn to page 79." if not persistent.thiefVanished and not tarpDone:
                show scribble5 onlayer transient zorder 100
                pov "What is this?"
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
                    go "Sometimes, I... I confess I dream of those caves."
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
                if gloommongerChat == 0:
                    show monster4 onlayer transient zorder 100
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
            "If you looked in the well, turn to page 346." if wellRand == 1 and wellChat <=2 and not persistent.wellVanished:
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
                            "You would have liked to be able to make a wish. But you had no coins on you."
                        "Otherwise, if {b}you have ventured into the Smoke World and rescued the stolen Skin-Mask from King Famine{b}, turn to page 742.":
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
                                    show wolf10 onlayer transient zorder 100
                                    "The howling finally stopped."
                                    "All was silent and still."
                                    call endStamp from _call_endStamp
                                    "And then there was rest in the land."
                                    $persistent.wellVanished = True
                                    "..."
                                    "Well. That's enough of that."
                                    "Let's get back to the story."
                                    play sound pageflip
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
                                    play sound pageflip
                                    jump town
                                    #jump end
                        "Otherwise, you may make a wish. Turn to page 367.":
                            "You toss a coin in the well, and wish for a way out of your terrible predicament."
                $wellChat += 1
                jump townExplore
            "If you wandered into the woods, turn to page 157." if persistent.thiefVanished or persistent.mushroomVanished:
                if persistent.toadvanished == False and and persistent.witchvanished == False and toadStopped == False:
                    f "W-wait just a second there!"
                    f "This is no time to be wandering off into the woods! We have an accursed witch to bring to justice. Not to mention a fine banquet to sample."
                    f "Come, let's get back to the village. I can tell you all about the plan."
                    $toadStopped = True
                    jump banquet
                else:
                    "You turned and walked out into the darkness of the woods."
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
                if pig:
                    "Your pig grunted as if to say, \"They stole my dignity.\""
                h "We can't let them just run around doing as they please and getting the Goose-girl all hot and bothered. What if everyone decided to do that? It'd be anarchy!"
                go "Hot, sweaty anarchy."
                $villagersCatch = True
                jump villagersConvo
            "If you asked them about your Godparent, turn to page 77." if not villagersEscape:
                if godfather== "White":
                    pov "I need a way to escape my godfather, the Lord. Do any of you know how I can do that?"
                    gm "Hmph. I advise you to give up immediately."
                    if persistent.thiefVanished:
                        go "I'm sorry. I know of no-one who can help you with that plight."
                        sh "Wasn't there..."
                        sh "No, never mind. You're right. There is no-one."
                    else:
                        go "Well, it is said that the Master Thief has hidden from the Lord all their life. If anyone would know, they would."
                        h "Once we track the thief down, you could question them!"
                elif godfather == "Red":
                    pov "I need a way to escape my godfather, the Devil. Do any of you know how I can do that?"
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
                        sh "I heard that dastardly Master Thief was planning to steal from her this very night! We'd better get the trap laid before they have a chance."
                $villagersEscape = True
                jump villagersConvo
            "If you asked them about the witch, turn to page 79." if villagersCatch and not villagersWitch and not persistent.witchVanished:
                pov "Are you going to do anything about the witch's curse?"
                go "And risk the wrath of the witch? Not on your life."
                gm "I heard that she has fingers as long and fat as carpet snakes, and once you fall into her clutches, you'll never see daylight again."
                go "I heard she has many children with the Devil, who are all evil."
                h "Well, I heard that all the trees of the woods are her children, but she regards them with vicious envy, and if any of them displease her by becoming too beautiful, she strikes them down!"
                h "This is why the most beautiful trees are always thunderstruck."
                $villagersWitch = True
                jump villagersConvo
            "If you accepted their offer, and head off to catch the Master Thief, turn to page 124." if villagersPlan or villagersCatch:
                $tarpDone = True
                h "Excellent! Let's be off at once."
                "And so you, the Goose-Girl, the Sparrow-Herder and the Hunter all leapt on the cart and rattled away down the road, leaving the old Gloom-monger behind."
                gm "You're all doomed! Doooooooomed!"
                h "Don't worry. He says that every time we go anywhere."
                jump thief2
            "If you made your excuses and left, turn to page 51.":
                sh "No worries. Have a good one!"
                jump townExplore

#=====================THE THIEF'S STORY

# Act 2, Chapter 2A: The Master Thief
#When you leave the village to track down the thief
label thief2:
    call hideAll from _call_hideAll_21
    show town3bg at artPos
    "Soon, you arrived at the young goose-girls house, which was overrun by honking geese who tore at the furniture and ransacked the pantry until she was at her wit's end."
    show wolf1 onlayer transient zorder 100
    go "Be careful! They say there's a terrible wolf somewhere out in these woods."
    show wolf10 onlayer transient zorder 100
    h "Don't worry, it's just a mad tale. There are no wolves in Australia."
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
    go "No way the thief can get past us now."
    if not persistent.mushroomVanished:
        echidna "I couldn't agree more, friends. This cunning and charismatic \"Master Thief\" character stands no chance against us."
    h "Don't get cocky."
    if persistent.mushroomVanished:
        #Note: I trigger all of the vanished flags all at the same time now.
        #So that if you quit the game at this point it doesn't break the game with only some people vanished and others not.
        #I also need to purge saves here so that you can't reload into a saved game that doesn't work.
        #TK: Make sure this works and doesn't break anything, also if it's the best option
        $persistent.hVanished = True
        $persistent.goVanished = True
        $persistent.shVanished = True
        $persistent.goblinsVanished = True
        $persistent.vanished +=1
        $persistent.thiefVanished = True
        $purge_saves()
        $ renpy.block_rollback()
        "The night was dark and quiet. You thought you heard something rustling in the bushes, outside your line of sight. A sound, almost like howling."
        "But it must have been the wind."
        show wolf1 onlayer transient zorder 100
        "The three of you lay there for a long time, watching the chest."
        $ renpy.block_rollback()
        go "Wait a moment."
        go "Was there... someone else here?"
        pov "I don't think so."
        sh "Just us three. You, me and [povname]."
        go "For some reason I thought..."
        "The goose-girl looked around."
        "After some searching she found a hunter's rifle, lying unused under the bush."
        sh "How odd."
        go "I - Does this rifle look... familiar to you?"
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
        "The clouds slowly passed over the moon."
        sh "I think we'd better check the traps. Make sure they're working."
        $ renpy.block_rollback()
        show wolf12 onlayer transient zorder 100
        "The two of you slowly crawled up to the chest."
        sh "Maybe we should have brought more people along. It's a little spooky with just the two of us."
        "It was always just the two of you."
        "The Sparrow Herder looked over the traps."
        sh "Yep, they're all still there."
        "You looked around at the cottage."
        pov "How long has this old house stood here?"
        "The abandoned house loomed over you."
        "The lights were on, but it was silent and empty."
        sh "No idea."
        sh "Not sure who owns it. Must have been before my time."
        "Who could say how long it had lain deserted?"
        "You saw some stray goosefeathers lying in the dirt. Nothing beside remained."
        sh "I-I think this might have been a mistake."
        sh "Let's head back to the village. Come on."
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
        "The thief pushed you up to grab onto the side of the carriage, then you reached down and pulled them up beside you."
        "The train whistled with full force, gathering speed until it burst out of the trees and into a wide open field."
        jump thiefSolo

    else:
        "You lay there in silence, watching the chest."
        "A fly landed on it."
        "One of the geese waddled up and began to lick it."
        go "Wait a second..."
        "The goose-girl crawled out and cautiously dragged a finger over the chest, then stuck it in her mouth."
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
                    t "That's right, it was I all along! I have stolen the eyes of Heaven and the hands of G-d, and now I use those eyes and hands to wreak mischief and misery upon this cursed earth!"
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
        t "You see, I've heard of you. They say you're a good little Christian, and you always do as you're told."
        t "Why not change that?"
    elif godfather == "Black":
        t "You see, I've heard of you. They say you're a strange one. You lurk out late at night and scare people."
    t "I know you live near the Mushroom, who has riches nearing those of the King of Kings."
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
    "You walked past a river."
    call hideAll from _call_hideAll_41
    show darkforestbg at artPos
    "You walked past a rocky coast."
    call hideAll from _call_hideAll_42
    show ruinsbg at artPos
    "You walked past the ruins of the 6th age, a grim reminder of the inevitable destruction fast approaching your world."
    call hideAll from _call_hideAll_43
    show treenightbg at artPos
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
                #TK: Make this go down when your family is disappeared
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
                    "The pig leapt into your arms and oinked at the thief with great malice."
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
                    pov "I've had this dream many times. I find myself in the middle of the forest. There is a great crowd around me, but I know someone is missing."
                    pov "I look down, and I realise I have no hands. Then I look down, and realise I have no feet."
                    pov "I always know what will happen next. I will look up, into the space between the trees. I am terrified, but I can't stop myself from doing it."
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
                "If you said nothing, turn to page 101.":
                    t "Alright, suit yourself."
                    jump thiefWatchThis

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
                    "It was the hollow interior of an enormous strangler fig. A great cavern was formed inside it, cold as ice despite the heat outside."
                    "The floor of the cavern was piled with rubies and pearls and glinting onyx and solid gold pieces, larger than your fist."
                    "All across the room were lush silks and pillars of precious metals of every type, and riches that would turn the King of Kings green with envy."
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
                        "As soon as they did, you heard a great terrible rumbling and groaning all around you, and the walls shook. The Mushroom emerged from a trapdoor in the floor and looked around wildly."
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
    "You grabbed the thief's and tried to pull them away as they stuffed gems and jewels into their pockets."
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
                "A brilliant light shone through the windows of the cavern. There was the sound of thundering wheels."
                call hideAll
                play sound pageFlip
                show trainfullbg
                ""
                play sound pageFlip
                call hideAll
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
                                            "Your pig was quickly drawn into a wager, with it's greatest hopes and dreams as the stakes. Fortunately it won, and was granted a a small kingdom in the mountains as it's prize. It would go on to raise a mighty pig empire there, and rule over it for the rest of it's days."
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
                                                            t "Right. I'll keep it short."
                                                            jump thiefStory
                                                        "To hear the incredibly short version, turn to page 188.":
                                                            pov "Well, I don't have a lot of time..."
                                                            t "Alright, my parents are bad and they gave me to the goblins to train as a thief. The goblins made a deal that if they couldn't recognise me when my apprenticeship ended in a year, I would go free."
                                                            jump thiefStoryEnd

#The thief's tragic backstory, related in their finale.
label thiefStory:
    call hideAll from _call_hideAll_57
    show nightbg at artPos
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
        call hideAll from _call_hideAll_58
        show trainbg at artPos
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
        call hideAll from _call_hideAll_59

        "In a few short hours, the train stopped on a rocky stretch of coast, and the thief's mother and father came to meet it."
        if godfather == "White" or godfather == "Red":
            "Midnight was approaching fast. You felt a cold chill come over you. Soon, your godfather would come and take you away."
        "The goblins lined up you and the thief with 12 goblins on a tree branch, all of you transformed to become king parrots and sparrows and magpies and birds of every type."
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
            "With a great shout, they burst into smoke, and revealed themselves to be goblins."
            "The whole line erupted into goblin smoke, and the two of you were revealed. In a flash, the goblins turned both the parents into hideous grubs which squirmed away and were buried in the dirt. The Lord cursed in disgust and vanished back behind the clouds, and the whole train leapt up in great celebration."
            call hideAll from _call_hideAll_61
            show darkforestbg at artPos
            "The thief stared about in amazement."
            t "But... "
            t "I felt the eyes of G-d upon me. How could He not see all the rot inside me?"
            pov "There is none. There never was."
        else:
            goblinQueen "Choose your child out of the line, and their life will be yours once more."
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
            "With a great shout, it burst into smoke, and revealed itself to be a goblin."
            "The whole line erupted into goblin smoke, and the two of you were revealed. In a flash, the goblins turned both the parents into hideous grubs which squirmed away and were buried in the dirt. The blazing light vanished back behind the clouds, and the whole train leapt up in great celebration."
            "The thief stared about in amazement."
            t "But... "
            t "I felt the eyes of G-d upon me. How could He not see the rot inside me?"
            pov "There's none there. There never was."
            if godfather == "Red":
                "Just then in a puff of smoke, the Devil appeared! Your godfather had come for you at last."
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
        "You wrapped the Master Thief in a great bear hug, and lifted them up on your shoulders."
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
                        "After many adventures, the Goblin Queen married you on the train. There was a great goblin celebration for 40 days and 40 nights."
                        if pig:
                            "Your pig watched over the wedding ceremony with tears in his eyes, and stayed with you as your constant companion and friend."
                        "You lived there in happiness for all of your days, venturing from place to place with wild abandon"
                        if godfather == "Black":
                            jump thiefDeath
                        else:
                            "You live there still, rattling across the whole world on the Goblin Train, and you will have no rest until the Day of Judgement."
                            play audio wolfApproaches
                            stop ambient2 fadeout 2.0
                            stop ambient1 fadeout 20.0
                            show wolf13 onlayer transient zorder 100
                            "And what happened to the mushroom, you ask?"
                            $persistent.vanished +=1
                            $persistent.mushroomVanished = True
                            $ renpy.block_rollback()
                            "Long did she germinate in the dark hollows of the world."
                            "But she could not hide there forever."
                            "After many days, she finally emerged from the dirt, into the cold air."
                            "No-one was there."
                            "Nothing was left."
                            #"Nothing but the {color=#f00}lacuna{/color}."
                            "It was already too late."
                            #"She was already gone."
                            call endStamp from _call_endStamp_23
                            "She was never seen or heard from again."
                            jump end
                    "If you remained good friends with the thief, turn to page 246.":
                        "You lived on the train in happiness with your friend the thief for all of your days, venturing from place to place with wild abandon."
                        if goblinCelebrate and pig:
                            "Your pig wished you a fond farewell, and went to live in his kingdom in the mountains."
                        elif pig:
                            "Your pig stayed with you as your constant companion and friend."
                        if godfather == "Black":
                            jump thiefDeath
                        else:
                            call endStamp from _call_endStamp_8
                            "You live there still, rattling across the whole world on the Goblin Train, and you will have no rest until the Day of Judgement."
                            stop music fadeout 1.0
                            play audio wolfApproaches
                            stop ambient2 fadeout 2.0
                            stop ambient1 fadeout 20.0
                            show wolf13 onlayer transient zorder 100
                            "And what happened to the mushroom, you ask?"
                            $persistent.vanished +=1
                            $persistent.mushroomVanished = True
                            $ renpy.block_rollback()
                            "Long did she germinate in the dark hollows of the world."
                            "But she could not hide there forever."
                            "After many days, she finally emerged from the dirt, into the cold air."
                            "No-one was there."
                            "Nothing was left."
                            #"Nothing but the {color=#f00}lacuna{/color}."
                            "It was already too late."
                            #"She was already gone."
                            call endStamp from _call_endStamp_24
                            "She was never seen or heard from again."
                            jump end

            else:
                show hand onlayer transient:
                    yalign 0.715#0.743
                    xalign 0.5
                menu:
                    "In the morning, you were faced with a choice. Because you had not yet tasted the goblin fruits, you could still return to your family and the world of humans."
                    "If you bade the thief farewell and returned to your family, turn to page 243.":
                        "You bade a tearful farewell to the thief, and returned back to your world among the humans, where you lived for many years in joyous happiness."
                        if godfather == "Black":
                            jump thiefDeath
                        else:
                            "There you stayed for the rest of your days, growing slowly older. On cold nights, you swear you could still hear the whistle of the Goblin Train, and the laughter of the thief in the wind."
                            call endStamp from _call_endStamp_9
                            "And then came an elephant with a very long snout, and it blew the story out."
                            #Wolf: Kills mushroom
                            stop music fadeout 1.0
                            play audio wolfApproaches
                            stop ambient2 fadeout 2.0
                            stop ambient1 fadeout 20.0
                            "..."
                            "Oh?"
                            show wolf13 onlayer transient zorder 100
                            "What happened to the mushroom, you ask?"
                            $persistent.vanished +=1
                            $persistent.mushroomVanished = True
                            $ renpy.block_rollback()
                            "Long did she germinate in the dark hollows of the world."
                            "But she could not hide there forever."
                            "After many days, she finally emerged from the dirt, into the cold air."
                            "No-one was there."
                            "Nothing was left."
                            #"Nothing but the {color=#f00}lacuna{/color}."
                            "It was already too late."
                            #"She was already gone."
                            call endStamp from _call_endStamp_25
                            "She was never seen or heard from again."
                            jump end
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
                            #Wolf: Kills mushroom
                            stop music fadeout 1.0
                            play audio wolfApproaches
                            stop ambient2 fadeout 2.0
                            stop ambient1 fadeout 20.0
                            show wolf13 onlayer transient zorder 100
                            "And what happened to the mushroom, you ask?"
                            $persistent.vanished +=1
                            $persistent.mushroomVanished = True
                            $ renpy.block_rollback()
                            "Long did she germinate in the dark hollows of the world."
                            "But she could not hide there forever."
                            "After many days, she finally emerged from the dirt, into the cold air."
                            "No-one was there."
                            "Nothing was left."
                            #"Nothing but the {color=#f00}lacuna{/color}."
                            "It was already too late."
                            #"She was already gone."
                            call endStamp from _call_endStamp_26
                            "She was never seen or heard from again."
                            jump end
                    "If you stayed on the goblin train and married the thief, turn to page 248.":
                        "After many adventures, the Goblin Queen married you on the train. There was a great goblin celebration for 40 days and 40 nights."
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
                            stop music fadeout 1.0
                            play audio wolfApproaches
                            stop ambient2 fadeout 2.0
                            stop ambient1 fadeout 20.0
                            "..."
                            "Oh?"
                            show wolf13 onlayer transient zorder 100
                            "What happened to the mushroom, you ask?"
                            $persistent.vanished +=1
                            $persistent.mushroomVanished = True
                            $ renpy.block_rollback()
                            "Long did she germinate in the dark hollows of the world."
                            "But she could not hide there forever."
                            "After many days, she finally emerged from the dirt, into the cold air."
                            "No-one was there."
                            "Nothing was left."
                            #"Nothing but the {color=#f00}lacuna{/color}."
                            "It was already too late."
                            #"She was already gone."
                            call endStamp from _call_endStamp_27
                            "She was never seen or heard from again."
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
                        pov "Alright. I'm ready"
                        m "No-one's ever ready. But there's no time left."
                        "She gently took you down to the kingdom of Death."
                        call endStamp from _call_endStamp_12
                        "And what you did after that, none who live can say."
                        #Wolf: Kills toad
                        stop music fadeout 1.0
                        play audio wolfApproaches
                        stop ambient2 fadeout 2.0
                        stop ambient1 fadeout 20.0
                        "..."
                        "Oh?"
                        show wolf13 onlayer transient zorder 100
                        "What happened to the mushroom, you ask?"
                        $persistent.vanished +=1
                        $persistent.mushroomVanished = True
                        $ renpy.block_rollback()
                        "Long did she germinate in the dark hollows of the world."
                        "But she could not hide there forever."
                        "After many days, she finally emerged from the dirt, into the cold air."
                        "No-one was there."
                        "Nothing was left."
                        #"Nothing but the {color=#f00}lacuna{/color}."
                        "It was already too late."
                        #"She was already gone."
                        call endStamp from _call_endStamp_28
                        "She was never seen or heard from again."
                        jump end

#==========Solo path
#The thief's path if the mushroom has disappeared
label thiefSolo:
    #t "Well! Did you ever doubt me?"
    call hideAll
    show goblinint2bg at artPos
    "From all across the train came a great cheer, and you looked around to see goblins of a thousand shapes emerge to hold up the thief in celebration."
    "Some had the heads of bats, some had the paws of cats, six heads, three heads, five arms, ten tails, and they bristled with tails and wings and fur and scales."
    "One crawled like a snail, one prowled like a wombat, one looked like seven doves tied together with string. All of them had a chaos of forms the likes of which you had never seen."
    "A dozen hands clapped you on the back and drew you into the train carriage."
    goblin1 "Have a drink with us! Any friend of the thief's is a friend of ours."
    goblin2 "Aye, it's good to see them come back in one piece."
    goblin3 "We sent them out on a training mission, you see. To steal from..."
    goblin3 "To steal... from..."
    "A vague and desperate confusion settled on the goblins face."
    t "Barkeep! Drinks for everyone, on me!"
    "The confusion cleared as the goblins all joined together in a great cheer."

    label thiefSoloMenu:
        call hideAll
        show goblinintbg at artPos
        show hand onlayer transient:
            yalign 0.64#0.743
            xalign 0.5
        menu:
            "The train was bustling with forty goblins in a chaos of forms."
            "If you sat down, turn to page 194." if not goblinSit:
                "You fell into a chair and looked around."
                call hideAll
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
                call hideAll
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
                call hideAll
                show goblinint2bg at artPos
                "The goblins poured you dozens of goblin brews, bubbling ales and steaming warm ciders, goblin wines that oozed with red fog and goblin brandies that froze and melted and froze again as you drank them."
                "The thief challenged the largest goblin to a drinking competition and drank them under the table."
                "Foolishly, you drank deeply of the brews. You guzzled them down until you could drink no more, until your vision was a haze and the brew ran down your mouth and drenched your clothes, and still you thirsted for them."
                "From that day on, no other drink would ever be able to quench your thirst, and you would always shiver and feel cold without the wild drunken feeling of warmth the goblin drinks gave you."
                $goblinDrink = True
                jump thiefSoloMenu
            "If you cornered the thief and asked them why you were brought here, turn to page 202.":
                "You managed to corner the thief as they laughed in a group of goblins."
                pov "Why did you grab me and take me here?"
                t "It is my nature! Nothing more."
                t "I am the greatest thief of my generation. I was raised by these goblins to steal the moon and sun and stars, and now I have stolen you away."
                "They laughed wildly. Their face was slick with sweat."
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
    "The music stopped. You looked around to see that the carriage was empty around you."
    "It had always been empty."
    t "I don't think this train is going fast enough, haha!"
    "Juggling spoons with their right hand, they grabbed you and pulled you through the empty carriage towards the engine room."
    call hideAll
    show trainbg at artPos
    "You burst out of the carriage door and into the cool night air. Without the sound of the music, you could hear the wind howling like a banshee."
    call hideAll
    show enginebg at artPos

    "The thief pulled you through and into the engine room, where four sooty goblins were lounging."
    t "Stoke the engine, will you? Let's see how fast this thing can move!"
    goblin4 "Aye, boss!"
    "The three goblins grabbed their shovels and set to work piling coal into the engine. The heat was intense."
    call hideAll
    show darknessbg at artPos
    "You looked out the window. It was pitch black outside."

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
    call hideAll
    show enginebg at artPos
    pov "Do you hear-"
    t "Nothing to worry about! Just the wind!"
    t "Help me shovel this coal, will you?"
    "You looked around. The engine room was empty, except for you and the thief."
    "You picked up a shovel and held it."
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
    call hideAll
    show darknessbg at artPos
    "They took your hand, and in a single twist of their long, long arms they pulled you both out of the engine and up onto the roof of the train."
    "You looked out across the night landscape. The land was haunted and beautiful. The smoke stung your eyes."
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
    call hideAll
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
    "The wind returned, howling like a monstrous beast."
    "They looked at you with piercing clarity. You saw the moon reflected in their dark eyes."
    t "Thank you, [povname]. For everything."
    t "I'm sorry we didn't get more time together."
    t "If you get out, tell them..."
    t "Tell those bastards I hated them all."
    "They gave you a sudden shove in the centre of your chest. You fell sprawling from the roof and slammed into the dirt, tumbling down the side of the hill and away from the train."
    "The train hurtled past you in a blaze of smoke and fire, and then was gone."
    stop music fadeout 1.0
    play audio wolfApproaches
    stop ambient2 fadeout 2.0
    stop ambient1 fadeout 20.0
    call hideAll
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
    call endStamp
    "Catch it, whoever can, and then you can make a great big cap out of it's fur."
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
    #TK: To complete
    show rocks onlayer transient zorder 100
    #m "Do I regret it? In some ways."
    #m "But then, would things have been any better if I stayed behind?"
    #When mushroom disappears show this
    show wolf13 onlayer transient zorder 100

    ""

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
    "The Master Thief managed to wriggle out of their grasp and leap up out a nearby window."
    t "Au revoir, my friend!"
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
    show scribble3 onlayer transient zorder 100
    "They all swept to and fro through a twisted city of endless tunnels. The shape of a giant, pale and broken mountain loomed over the city, barely visible through the thick fog of spores."
    pov "I was about to win! Why have you kidnapped me?"
    m "Darling, trust us, that sad production wasn't going to win anything. You were hurting yourself."
    m2 "Hurting yourself."
    m "Please don't take the criticism too personally. It was an intriguing bit of invisible theatre. We do respect the way you put everything into the role. But you really must consider the problematic aspects of the piece."
    "Dozens of identical mushrooms pressed around you, speaking in soft, overlapping voices."
    m3 "I think it might be best if you stay here until I know that you're safe.{vspace=30}                                             {w=0.4}Until I know you're safe.{vspace=30}                         {w=0.8}It's for the best, if you stay here."
    m4 "I'll watch over you.{vspace=30}                                             {w=0.4}Over you.{vspace=30}                         {w=0.8}Watch over."
    call hideAll from _call_hideAll_30
    show mushroompalacebg at artPos
    if pig:
        "You were taken through a great palace of yellow chanterelles and dressed in robes of fine moss. Your room was lushly furnished with soft covers woven from black mushroom silk. Your pig had his own quarters and a bevy of servants to attend to his every whim. All the gems and gold and treasures of the earth were available to you both."
    else:
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
        call hideAll from _call_hideAll_31
        show mushroomgardensbg at artPos
        "You walked out into the lush expanse of the underground kingdom. Rich moss and lichens flowered from every surface. "
        if godfather != "Black":
            m "Don't worry. I know about your godfather. He cannot reach us here."

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
                    "The wonder of those gardens were so great that the tongue fails to describe them, and you walked and watched for days, until your eyes were so full that they couldn't stand to see another scrap of beauty."
                    m "A tad garish, isn't it?"
                    $mushroomMoss = True
                    jump mushroomExplore
                "If you feasted in the great palace, turn to page 138." if not mushroomFeast:
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
                    "The mushroom took you down to show you the great roots of the whole forest above you. Delicate fungal networks wove through every root, carrying vital letters and trade agreements and treaties to every plant in the woods."
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
                "If you asked to return home, turn to page 148.":
                    #TK: this mention of siblings should be ok because, by the time all of your siblings have been eaten, this route is inaccessible. Just make sure.
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
                                        if pig:
                                            "Your pig settled down to a contented life among the truffles."
                                        "You set up a quaint home in that strange country, and soon you were even able to find your poor mother and make amends for your wicked behaviour."
                                        "After a long time, your siblings came down to join you there, one by one."
                                        "Even I was there, though you did not see me."
                                    else:
                                        "You and the mushrooms stayed the greatest of friends, talking all through the small hours together."
                                        if pig:
                                            "Your pig settled down to a contented life among the truffles."
                                        "You set up a quaint home in that dark kingdom."
                                        "After a long time, your mother and siblings came down to join you there, one by one."
                                        "Even I was there, though you did not see me."
                                "If you married the mushrooms, turn to page 156.":
                                    "After slowly growing close over many years, you and the mushrooms all became married together in a beautiful ceremony."
                                    "Your mother came down to the kingdom of death for the occasion, and all the plants and lichens and moss and toadstools of the forest were in attendance."
                                    "The occaision was full of joy. I laughed as I raised a toast, and the beer ran down my chin but did not go into my mouth."
                            if godfather == "White":
                                "Long did your godfather the Almighty search for you, but never could he find you, hidden as you were in that undiscovered country."
                            elif godfather == "Red":
                                "Long did your godfather the Devil search for you, but never could he find you, hidden as you were in that undiscovered country."
                            elif godfather == "Black":
                                "And so the promise came to pass, and you took your place with the woman clad all in black, just as she promised your mother all those years ago."
                            call endStamp from _call_endStamp_2
                            "You stayed there at the side of the Pale Lady, forever and ever, until the final horn and the coming of the end of days."
                            #Wolf: Kills Thief
                            stop music fadeout 1.0
                            play audio wolfApproaches
                            stop ambient2 fadeout 2.0
                            stop ambient1 fadeout 20.0
                            "..."
                            "Oh?"
                            show wolf14 onlayer transient zorder 100
                            "And what happened to the thief, you ask?"
                            $persistent.vanished +=1
                            $persistent.thiefVanished = True
                            $ renpy.block_rollback()
                            "Long did they run from the law."
                            "Over hill and dale, through the valleys, under the mountains and across the sea they ran."
                            "Finally one night, they ran deep into the desert."
                            "They caught their breath and looked around. The sky was vast and empty above them."
                            "No-one was there."
                            "Nothing was left."
                            #"Nothing but the {color=#f00}lacuna{/color}."
                            "It was already too late."
                            #"They were already gone."
                            call endStamp from _call_endStamp_7
                            "They were never seen or heard from again."
                            jump end
                        "If you held fast to your desire to return to the world above, turn to page 164.":
                            if godfather == "Red":
                                pov "Don't think that I want to leave you. It's just that I must see my siblings and my old country."
                            else:
                                pov "Don't think that I want to leave you. It's just that I must see my old mother and my old country."
                            m3 "I see. Then we won't stand in your way. Take this to remember us by."
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
    "As you looked around, a strange anxiety gripped you. The ancient old strangler fig was gone. You couldn't see the blue door to the mushroom's domain."
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
    "When you heard those odd words, a terrible fear gripped you, and you ran out onto the street and through the twisting alleyways. The forest you knew was gone. A grey rain of ash fell ceaselessly across the land from the grey clouds above. The bent and crooked people of the realm huddled in grim shelters underneath places that hideously resembled the hills and lakes and villages you once knew."
    "Over and over, you heard them mutter of the Ash Giants, and you heard terrible footfalls shake the earth from some distant place, closer all the time."
    "The awful feeling came over you that what the old man said was true. Each day you spent in the underground kingdom was as a hundred years on earth."
    "You ran through the grey streets and parking lots and abandoned shopping centres and vast, decayed, echoing airports and twisting underground toll roads and long slow landfill rivers that seethed with the serpentine motion of the trash queens as you stumbled onto the cracked bitumen roads and empty apartment complexes packed with flickering TV screens of static under the grim endless maze of freeways stacked above you that blotted out the grey sky above, but try as you might you couldn't find the way back to the kingdom you left."
    if godfather == "White":
        miw "Finally."
        "You felt a heavy hand fall on your shoulder. A great light shone behind you, too bright for you to turn and face it."
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
                    stop music fadeout 1.0
                    play audio wolfApproaches
                    stop ambient2 fadeout 2.0
                    stop ambient1 fadeout 20.0
                    "..."
                    "Oh?"
                    show wolf14 onlayer transient zorder 100
                    "And what happened to the thief, you ask?"
                    $persistent.vanished +=1
                    $persistent.thiefVanished = True
                    $ renpy.block_rollback()
                    "Long did they run from the law."
                    "Over hill and dale, through the valleys, under the mountains and across the sea they ran."
                    "Finally one night, they ran deep into the desert."
                    "They caught their breath and looked around. The sky was vast and empty above them."
                    "No-one was there."
                    "Nothing was left."
                    #"Nothing but the {color=#f00}lacuna{/color}."
                    "It was already too late."
                    #"They were already gone."
                    call endStamp from _call_endStamp_15
                    "They were never seen or heard from again."
                    jump end
                "If you refused to open the box, even when all hope was lost, turn to page 179.":
                    if godfather == "White":
                        "You hesitated - but in the end you couldn't bring yourself to break your promise to the mushroom."
                        call endStamp from _call_endStamp_4
                        "And so the Lord took you, and you rested in the basement of His White House forever and ever, until the final horn and the coming of the end of days."
                        #Wolf: Kills Thief
                        stop music fadeout 1.0
                        play audio wolfApproaches
                        stop ambient2 fadeout 2.0
                        stop ambient1 fadeout 20.0
                        "..."
                        "Oh?"
                        show wolf14 onlayer transient zorder 100
                        "And what happened to the thief, you ask?"
                        $persistent.vanished +=1
                        $persistent.thiefVanished = True
                        $ renpy.block_rollback()
                        "Long did they run from the law."
                        "Over hill and dale, through the valleys, under the mountains and across the sea they ran."
                        "Finally one night, they ran deep into the desert."
                        "They caught their breath and looked around. The sky was vast and empty above them."
                        "No-one was there."
                        "Nothing was left."
                        #"Nothing but the {color=#f00}lacuna{/color}."
                        "It was already too late."
                        #"They were already gone."
                        call endStamp from _call_endStamp_17
                        "They were never seen or heard from again."
                        jump end
                    elif godfather == "Red":
                        "You hesitated - but in the end you couldn't bring yourself to break your promise to the mushroom."
                        call endStamp from _call_endStamp_5
                        "And so the Devil took you, and you were trapped as his servant in Hell forever and ever, until the final horn and the coming of the end of days."
                        #Wolf: Kills Thief
                        stop music fadeout 1.0
                        play audio wolfApproaches
                        stop ambient2 fadeout 2.0
                        stop ambient1 fadeout 20.0
                        "..."
                        "Oh?"
                        show wolf14 onlayer transient zorder 100
                        "And what happened to the thief, you ask?"
                        $persistent.vanished +=1
                        $persistent.thiefVanished = True
                        $ renpy.block_rollback()
                        "Long did they run from the law."
                        "Over hill and dale, through the valleys, under the mountains and across the sea they ran."
                        "Finally one night, they ran deep into the desert."
                        "They caught their breath and looked around. The sky was vast and empty above them."
                        "No-one was there."
                        "Nothing was left."
                        #"Nothing but the {color=#f00}lacuna{/color}."
                        "It was already too late."
                        #"They were already gone."
                        call endStamp from _call_endStamp_21
                        "They were never seen or heard from again."
                        jump end
                    else:
                        "And so you stayed there, forever searching for an entrance back to that kingdom you missed so much."
                        "For years you searched, with no success. Soon, the Ash Giants came upon the world, and you felt their searing light upon your skin."
                        "As the light burnt you away, you felt something take hold of you and draw you into the earth."
                        m "It's ok. It's just me. Just us."
                        m "You've returned."
                        if pig:
                            "Your pig jumped out from the arms of the mushroom and danced around you in glee."
                        call hideAll from _call_hideAll_38
                        show mementobg at artPos
                        call endStamp from _call_endStamp_6
                        "The mushrooms took you down into the earth. There you stayed at the side of Lady Death, forever and ever, until the work was complete, and the glory of it shone out forevermore."
                        #Wolf: Kills Thief
                        stop music fadeout 1.0
                        play audio wolfApproaches
                        stop ambient2 fadeout 2.0
                        stop ambient1 fadeout 20.0
                        "..."
                        "Oh?"
                        show wolf14 onlayer transient zorder 100
                        "And what happened to the thief, you ask?"
                        $persistent.vanished +=1
                        $persistent.thiefVanished = True
                        $ renpy.block_rollback()
                        "Long did they run from the law."
                        "Over hill and dale, through the valleys, under the mountains and across the sea they ran."
                        "Finally one night, they ran deep into the desert."
                        "They caught their breath and looked around. The sky was vast and empty above them."
                        "No-one was there."
                        "Nothing was left."
                        #"Nothing but the {color=#f00}lacuna{/color}."
                        "It was already too late."
                        #"They were already gone."
                        call endStamp from _call_endStamp_22
                        "They were never seen or heard from again."
                        jump end

#=====================THE TOAD'S STORY

# Act 2, Chapter 2B: Journey with the Toad
label toad1:
    "He gulped down the rest of his plate and stumbled unsteadily away from the table."
    if pig:
        "You, the toad and the pig stepped into the toad's squash carriage, and it went rattling away down the path into the great, dark rainforest."
    else:
        "You both stepped into the toad's squash carriage, and it went rattling away down the path into the great, dark rainforest."
    call hideAll from _call_hideAll_65
    show nightbg at artPos
    "As you went down the road, the forest began to get darker and darker."
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
    "You walked on. Soon, you began to see a glimmer of silver light in the darkness."
    call hideAll from _call_hideAll_68
    show darkforestbg at artPos
    "The forest was covered in great puddles of water from the rains. The puddles shone with light."
    "All around you, the woods were dark and empty. But when you looked into the water, you saw the reflection of a shining cottage below."
    play sound pageFlip
    call hideAll
    show lakefullbg
    ""
    play sound pageFlip2
    call hideAll
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
    call hideAll from _call_hideAll_73
    show cottagebg at artPos
    "Soon, you had crossed the river paths to the cottage in the centre."
    "Up over the walls grew a riot of herbs and flowers of every type, rambling over everything and growing in a lush green-grass garden on the roof. "
    if pig:
        "The pig munched on some violets blooming from the windowsill."
    "You saw the glimmer of two red eyes watching you from a small crook in the roof. Then there was a gasp from inside, and they disappeared."
    if not toadSad:
        "The closer you got to the cottage, the more the toad shook with terror."
        pov "You'd better stay behind. Guard the rear."
        f "G-good idea."
        f "But be wary, my friend. Few have ever left that cottage alive"
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
    "With a click of his fingers, Brildebrogue summoned a cavalcade of richly dressed frog manservants, who offered you all the finest delicacies from across the world, such that the king of kings would cry to taste them."
    "With another click, a dozen beautiful frog maids escorted you to golden baths where all the muck and grime was washed away, and you were restored to your true forms as the finest frog soprano choir in all the land serenaded you."
    "Brildebrogue himself regaled you with witty anecdotes of his thrilling adventures, which had everyone rolling around on the floor laughing, except for the toad, who sat in the corner and scowled."
    show scribble3 onlayer transient zorder 100
    bc "Please make yourselves at home, my friends!"
    bc "I'm afraid I must leave immediately. Business with the jewelled serpent-kings of the City of Brass, you understand."
    f "Of course. Actually, I recall I was chatting with the jewelled serpent-kings myself just the other day, and -{w=1.0}{nw}"
    bc "Help yourselves to all the delights of Chippingham Manor! Here are the keys to the whole place. You may go wherever you wish, and open every door!"
    bc "...except one."
    bc "This little golden key will unlock the smallest closet in the tallest tower. Do not open that closet."
    bc "But I'm sure that won't be a problem! I know I can trust you, my dear friends. I'll see you on my return!"
    "And with a wave of his hand, he leapt into a gleaming gold carriage and sped away across the horizon in an instant."
    f "Hpmh. Show-off."
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
                    "Inside the third tower, you discovered a great harem of finely-dressed frog courtesans, who poured rich wines and made witty conversation with you until you were all completely sloshed and dizzy from the refined repartee."
                else:
                    "Inside the third tower, you discovered a great harem of finely-dressed frog courtesans, who poured rich wines and made witty conversation with you until you were both completely sloshed and dizzy from the refined repartee."
                $thirdTower = True
                jump chippinghamManor
            "If you explored the fourth tower, turn to page 259." if not fourthTower:
                $fourthTower = True
                "Inside the fourth tower was a great fountain of emeralds and sapphires and precious gems, which splashed out over a scale model replica of the forest. You could see immediately that a single gemstone from this fountain was so valuable that it would bankrupt the richest sultan."
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
                if pig:
                    "The pig stood behind you and tried to fend Brildebrogue off, but with a single sweep, he cut off its right hoof and sent it tumbling away."
                    "You pulled the injured pig into your arms and fled through the racks of fine clothes in the fifth tower as Brildebrogue sliced them apart behind you."
                else:
                    "You fled through the racks of fine clothes in the fifth tower as Brildebrogue sliced them apart behind you."
                bc "Trying to steal from my wardrobe?"
                bc "I heard the servants laughing about your little dress-up obsession, Blort. I just never realised it went this far!"
                "With one clap of his hands he brought down water rushing in from the seas. You fled through through the waves as they brought the tower down around you."
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
                    "Godmother! Help me!"
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
            "The Lord performed His feat and turned into a mighty wind. But just as He did so, the toad opened the window, and the Lord blew right out of the tower and across the sea. With this, the toad slammed the window shut."
            f "Well. That takes care of that."

        if godfather == "Red":
            #The devil drags brildebrogue down to hell
            mir "Your time is up!"
            "The Devil Himself exploded out of the floor in a flash of brimstone and soot."
            if pig:
                "The pig hid behind you, shivering."
            "As soon as he saw your godfather, Brildebrogue went white as ash."
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
        "You took the gems from the wreckage and renovated the toad's old mud-hole, turning it into a warm, comfy little cottage with a great fire and enough food for a lifetime, along with a large closet of fine clothes."
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
                    stop music fadeout 1.0
                    play audio wolfApproaches
                    stop ambient2 fadeout 2.0
                    stop ambient1 fadeout 20.0
                    "..."
                    "Oh?"
                    show wolf12 onlayer transient zorder 100
                    "And what happened to the witch, you ask?"
                    "She was carried away by swift water."
                    "The sky grew dark. The river grew cold. Still, she tumbled through the depths."
                    "Finally, she washed onto a broken shore."
                    "No-one was there."
                    "Nothing was left."
                    #"Nothing but the {color=#f00}lacuna{/color}."
                    "It was already too late."
                    #"She was already gone."
                    call endStamp from _call_endStamp_35
                    $persistent.vanished +=1
                    $persistent.witchVanished = True
                    $ renpy.block_rollback()
                    "She was never seen or heard from again."
                    jump end
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
                    stop music fadeout 1.0
                    play audio wolfApproaches
                    stop ambient2 fadeout 2.0
                    stop ambient1 fadeout 20.0
                    "..."
                    "Oh?"
                    show wolf12 onlayer transient zorder 100
                    "And what happened to the witch, you ask?"
                    "She was carried away by swift water."
                    "The sky grew dark. The river grew cold. Still, she tumbled through the depths."
                    "Finally, she washed onto a broken shore."
                    "No-one was there."
                    "Nothing was left."
                    #"Nothing but the {color=#f00}lacuna{/color}."
                    "It was already too late."
                    #"She was already gone."
                    call endStamp from _call_endStamp_36
                    $persistent.vanished +=1
                    $persistent.witchVanished = True
                    $ renpy.block_rollback()
                    "She was never seen or heard from again."
                    jump end

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
                stop music fadeout 1.0
                play audio wolfApproaches
                stop ambient2 fadeout 2.0
                stop ambient1 fadeout 20.0
                "..."
                "Oh?"
                show wolf12 onlayer transient zorder 100
                "And what happened to the witch, you ask?"
                "She was carried away by swift water."
                "The sky grew dark. The river grew cold. Still, she tumbled through the depths."
                "Finally, she washed up on a broken shore."
                "No-one was there."
                "Nothing was left."
                #"Nothing but the {color=#f00}lacuna{/color}."
                "It was already too late."
                #"She was already gone."
                call endStamp from _call_endStamp_37
                $persistent.vanished +=1
                $persistent.witchVanished = True
                $ renpy.block_rollback()
                "She was never seen or heard from again."
                jump end
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
                    pov "Alright. I'm ready"
                    m "No-one's ever ready. But there's no time left."
                    call hideAll from _call_hideAll_93
                    show mementobg at artPos
                    "She gently took you down to the kingdom of Death."
                    call endStamp from _call_endStamp_20
                    "And you lie there still."
                    #Wolf: Kills Witch
                    stop music fadeout 1.0
                    play audio wolfApproaches
                    stop ambient2 fadeout 2.0
                    stop ambient1 fadeout 20.0
                    "..."
                    "Oh?"
                    show wolf12 onlayer transient zorder 100
                    "And what happened to the witch, you ask?"
                    "She was carried away by swift water."
                    "The sky grew dark. The river grew cold. Still, she tumbled through the depths."
                    "Finally, she washed up on a broken shore."
                    "No-one was there."
                    "Nothing was left."
                    "Nothing but the {color=#f00}lacuna{/color}."
                    "It was already too late."
                    "She was already gone."
                    call endStamp from _call_endStamp_38
                    $persistent.vanished +=1
                    $persistent.witchVanished = True
                    $ renpy.block_rollback()
                    "She was never seen or heard from again."
                    jump end

#==========Solo path
#The Toad's path if the Witch has disappeared
label toadSolo:
    "The toad leapt up from the table and clicked his fingers."
    f "Prickle! Crawl! Shudder and Clink! Don't tarry or stall, get us there in a wink!"
    "His great squash carriage rattled out of the bushes and pulled up right next to the banquet table."
    f "If you get us there before sundown, there's a tenner in it for you!"
    "He tossed a bag of shiny coins to the crow-shrike, the rat, the bat and the old black cockatoo."
    bat "Cheers, boss."
    "The cockatoo bit into one of the coins."
    cockatoo "Yep, it's good money. Let's do it, boys."
    rat "We'll get you there in a jiffy, mate."
    crowshrike "Caw!"
    "The squash rattled and bumped down the road with great haste. The toad attempted some witty anecdotes while you pretended to listen."
    $persistent.vanished +=1
    $persistent.toadVanished = True
    $purge_saves()
    $ renpy.block_rollback()
    call hideAll
    show manorextbg at artPos
    "Finally you arrived at a stately riverside manor."
    "With a clap of his hands, the toad summoned a cavalcade of richly dressed frog manservants, who poured flutes of champagne while offering spontaneous and completely unplanned anecdotes about the incredible things Brildebrogue Chippingham had said or done lately."
    "With another click, a dozen beautiful frog maids escorted you to golden baths where all the dirt of the journey was washed away. The finest frog soprano choir in all the land serenaded you with tales of Brildebrogue Chippingham's latest exploits."
    "All the while, the toad's servants pretended to laugh at his jokes as he tipped them generously."
    f "Yes, please make yourself at home, my dear friend! We are friends now, right?"
    f "That is to say, of course we are! I have so many friends these days, you know, I may be completely tied up with them and all the time we spend together constantly, but never fear, I won't forget the little people such as yourself, my dear friend, we shall certainly have some time to spend together."
    pov "Have you... always owned this manor?"
    show monster2 onlayer transient zorder 100
    f "Of course! The manor is owned by me, Brildebrogue Chippingham! That's my name! Why would you think otherwise?"
    f "Anyway, no time to talk about trivialities such as property ownership, I have a party to plan! It will begin soon, you'd better make ready!"
    "And with that the toad flitted out of the room and left you alone to explore the manor."
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
            yalign 0.60#0.743
            xalign 0.5
        menu:
            blank "" #Sounds of music and chatter drifted through the hallways of the manor.
            "If you explored the first tower, turn to page 256." if not firstTower:
                #The great vault
                #if pig:
                    #"Inside the first tower you discovered a trio of stately frog wizards, who flushed the last remains of the potions from your systems and restored you to good health."
                #else:
                    #"Inside the first tower, the two of you discovered a trio of stately frog wizards, who flushed the last remains of the potions from your systems and restored you to good health."
                "Deep underneath the first tower was a great vault full of riches."
                "Inside the vault was a cornucopia of lucious fruit, fat flies, even great gardens and lakes that produced enough food to last for years - perhaps centuries."
                "A team of frog engineers were reinforcing the walls to make them totally impenetrable."
                $firstTower = True
                $construction +=1
                jump toadConstruct
            "If you explored the second tower, turn to page 257." if not secondTower:
                "Inside the second tower was a trio of stately frog wizards, hard at work placing sigils and wards and runes all across the manor to guard against every possible evil."
                #if pig:
                    #"Inside the second tower, you discovered the finest frog chefs of all the land, who quickly sliced off their own legs and served them to you as the most delicious dish the three of you had ever tasted."
                #else:
                #    "Inside the second tower, you discovered the finest frog chefs of all the land, who quickly sliced off their own legs and served them to you as the most delicious dish either of you had ever tasted."
                $secondTower = True
                $construction +=1
                jump toadConstruct
            "If you explored the third tower, turn to page 258." if not thirdTower:
                "Inside the third tower, you discovered a collection of fine frog bards, composing great poems and arias in Brildebrogue's name."
                $thirdTower = True
                $construction +=1
                jump toadConstruct
            "If you explored the fourth tower, turn to page 259." if not fourthTower:
                $fourthTower = True
                "The whole fourth tower was taken up by a great pyramid. Atop that pyramid was a gigantic sculpture of Brildebrogue, vomiting forth emeralds and sapphires and precious gems."
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
            "If you explored the seventh tower, turn to page page 264." if construction >= 2:
                "Inside the seventh and tallest tower you found only a tiny wooden closet."
                show hand onlayer transient:
                    yalign 0.68#0.743
                    xalign 0.5
                menu:
                    "A golden keyhole shone out from the closet door."
                    "The sounds of the party echoed below you."
                    "If you opened the closet, turn to page 275.":
                        "You inserted the key, and slowly opened the door with a long creak."
                        call hideAll
                        show mushroombasementbg at artPos
                        "As soon as the door opened, a stream of blood flowed over you."
                        if pig:
                            "The pig squealed in terrible fear."
                        "In the depths of the darkness, you saw a hollow face."
                        "The eyes were gone. The mouth had rotted away. It was all that remained of Brildebrogue Chippingham."
                        jump toadSoloFinale
                    "If you went back, turn to page 190.":
                        jump chippinghamManorSolo
            # "If you patiently waited for Brildebrogue, turn to page 161.":
            #     f "Well, if you're not going to open this damn closet, I am."
            #     "He rushed to the seventh and tallest tower, and unlocked the closet with the golden key."
            #     "He slowly turned the key, and opened the closet door with a long creak."
            #     call hideAll
            #     show mushroombasementbg at artPos
            #     "As soon as the door opened, a stream of blood flowed over the two of you, and you saw seven dead frog brides hanging all along the closet walls, some only skeletons."
            #     jump brildebrogueCloset
    #There is a desperate descent of him attempting to seal out the wolf, posting guards, building walls, hiring magicians and sorcerers of every type, dogs at the door, the finest locks known to mankind. Finally he creates a great tomb-vault inside his house, where he will be sealed forever. He says a tearful goodbye to you outside the vault. Then he disappears forever.




    #The seventh
    #Layers:
    #Gold, Silver, Copper, Iron, Mercury, Salt, Ash, Bone. // Ash, Salt, Rowan, Iron, Bone. , Iron, Mercury. Tin, lead,

label toadConstruct:
    if construction == 1:
        "The toad was busy reinforcing the manor's defences."
        "Golden locks were placed on every door, and silver bars at every window."
        jump chippinghamManorSolo
    elif construction == 2:
        "Hordes of guests began arriving for the great gala. Notable political figures, great artists or famed adventurers from the swamplands."
        "The toad greeted them hastily before leading a team of master masons through the house, heading for the basement."
        "The masons carried great wagons of copper and iron."
        jump chippinghamManorSolo
    elif construction == 3:
        #Show wolf image
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
        "Layers of ash and salt were drawn around the mansion."
        "The doors were barred. Guests weren't allowed to enter or leave."
        "They didn't seem to care. Fine swamp cocktails were handed out and a big band played on into the night."
        show wolf14 onlayer transient zorder 100
        "Underneath the music, you almost thought you could hear scrabbling in the walls."
        jump chippinghamManorSolo
    elif construction == 5:
        "The final layer of protection was delivered. The layer of Bone."
        "You saw it drawn into the castle under cover of night."
        "The band leader leapt into a triumphant saxophone solo."
        jump chippinghamManorSolo
    elif construction >= 6:
        #jump toadSoloFinale
        #Wolves in the walls
        "The vault was complete."
        "It yawned underneath the manor like an open mouth."
        "The walls were thick. Impenetrable in every way. Every possible ward had been laid upon them."
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
        f "The manor was owned by a great frog named Brildebrogue Chippingham, who was so handsome that light shone from his face as if from the sun. The wind whistled for him, and the cobblestones sighed in joy to receive his feet upon them. Everyone in the land adored him."
        f "Sweeping his floors, and dusting his closets, I searched through the manor each night."
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
        f "Their skeletal arms closed around him and dragged him into the blood-soaked blackness."
        f "I slammed the door. I took up his clothes and his mantle."
        f "None can tell the difference. Or perhaps they don't care to, as long as I keep the money flowing."
        "The sounds of laughter and music echoed from behind the door."
        pov "You're living a lie."
        f "No."
        f "He was the imposter. History will remember me as the real thing."
        "The toad walked over and swung the closet door shut."
        "A frog sage appeared to inform you that the vault was ready."
        f "Good. Come with me."
        call hideAll
        show mushroomcavebg at artPos
        "You both walked down through the manor, past the riotous party, down to the vault in the basement."
        pov "Is this really what you want?"
        f "Of course. This is the life I always desired. This is why I took the deal, all those years ago."
        "The toad walked into the cyclopean, hungry mouth of the vault."
        pov "Why don't you give up the charade? Come with me. You can live in the village. As your true self."
        f "No. I've come too far now."
        f "I am Brildebrogue Chippingham, and I will never die."
        f "The sages will speak of me. The bards will sing poems."
        f "The great statues outside will stand forever. Historians will speak of me a thousand years hence."
        f "There will not be a soul on this earth who does not know my name."
        f "There is nothing to fear. I am already immortal."
        "You embraced. The cavernous emptiness of his vault loomed before him."
        "He gave you a final wave. Then, he was swallowed up into the darkness."
        "The lock sealed. The magic shook the earth, and a great golden sigil appeared upon it."
        "The barriers were set. The guards of silver, gold, lead, rowan, ash, oak, and the final layer of bone."
        show wolf6 onlayer transient zorder 100
        stop music fadeout 1.0
        play audio wolfApproaches
        stop ambient2 fadeout 2.0
        stop ambient1 fadeout 20.0
        call hideAll
        show manorextbg at artPos
        "A great silence settled upon the house."
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
        call endStamp
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
                    pov "I'm hoping you can help me with a problem. My godfather is the Lord, and He has sworn to take me away at midnight tonight."
                    w "That's wild."
                    w "I mean, I'm a witch, yeah, but I'm not exactly all powerful over here, I'm not sure what you want me to do about that?"
                    w "But yeah nah, maybe I could help you out. Let me take a look through my books, I'll see what I can come up with."
                    "And she began rifling through the stack of books lying randomly around the floor."
                if godfather == "Red":
                    pov "I'm hoping you can help me with a problem. My godfather is the Devil, and He has sworn to take me away at midnight tonight."
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
    show wolf9 onlayer transient zorder 100
    "The witch grabbed a crooked dagger, still gleaming with wolfsbane from her potion work earlier, and parried his thrust."
    w "Do I know you?!"
    "They began to fight back and forth, crashing around the tiny cottage, and as they did the bookshelves rocked and the chairs went clattering away and the potions began to fall from the walls, breaking open in great bursts of magical smoke and light."
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
        w "The truth is, I have worked for the Devil all this time, and wrought his wicked works upon the world - though it pleased me none to do so."
        "If you asked the witch to tell her tale, turn to page 215." if not witchStory:
            w "test"
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
            p1 "This cowed me enough that I followed His wishes and bought the bread. He stayed in my house all through the night."
            p1 "In the morning the Lord granted me a wish, thinking I would want to go to heaven. But instead I asked for a deck of cards that would allow me to win any game."
            p1 "The Lord granted my wish, and then I really got to work. Soon I had won half the world, and the Lord was forced to ask Death to stop my rampage."
            p1 "Death took me at the poker table, and so I went up to Heaven and knocked on the gates."
            miw "...No. We don't need you here. Be on your way, pig."
            p1 "So I went and knocked on the gates of Purgatory."
            wib "I don't think so. We have enough misery and trouble here. Be on your way, pig."
            p1 "And so finally I went and knocked on the gates of Hell, where they let me in at once. There was no-one there except for Lucifer and the hunchback devils."
            p1 "The straight-backed devils were all away on business, you see."
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
            "If you investigated the cavern wall, turn to page 205.":
                "Hell was a small cave, draughty and full of coal dust."
                "You looked through a hole in the cave wall and marvelled to see the imps cavorting in drunken song and dance beyond, each of them plotting to destroy the works of man and G-d."
                "You quickly retreated for fear of being seen."
                jump hell
            "If you investigated the centre of the cavern, turn to page 206.":
                "In the centre of the cavern was a small, homely cottage. You peered in the window."
                call hideAll from _call_hideAll_76
                show hellcottagebg at artPos
                "The Devil was not home. But in a rocking chair in the corner you saw His old grandmother. She spotted you both at once."
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
            "You shook to see your godfather in the flesh at last."
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
                dg "I dreamed that a desperate mother once pledged her child to you, as the godfather - and that you are bound to grab [him] up at midnight tonight. Can [he] evade you, do you think?"
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
                dg "I dreamed that a desperate young mother once pledged her child to God, as the godfather - and that their child was bound to be taken by Him on [his] 18th birthday. Can [he] ever escape, do you think?"
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
        dg "Well! I'm sure you heard the answers to your questions. Here are the Devil's three golden hairs."
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
            "You left the cottage and crawled down into the foundations beneath it. When you found the old worm squatting beneath it, the witch speared it with her crooked finger, killing it instantly."
            "With that, she felt a great weight fall from her shoulders. You turned and saw that the Devil's mark was no longer on her."
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
            "Alas, as you tumbled onto the floor of the cottage, you heard the clock strike midnight, and you saw a pair of terrible red boots ahead of you."
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
                    p1 "Not so fast, my ertswhile adversary."
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
                    stop music fadeout 1.0
                    play audio wolfApproaches
                    stop ambient2 fadeout 2.0
                    stop ambient1 fadeout 20.0
                    "..."
                    "Oh?"
                    show wolf6 onlayer transient zorder 100
                    "What happened to the toad, you ask?"
                    $persistent.vanished +=1
                    $persistent.toadVanished = True
                    $ renpy.block_rollback()
                    "He stumbled into the woods."
                    "For hours, he wandered through the trees. His feet blistered. His breath grew short."
                    "There is no light in that part of the forest."
                    "Finally, he emerged into a shadowed clearing."
                    "No-one was there."
                    "Nothing was left."
                    #"Nothing but the {color=#f00}lacuna{/color}."
                    "It was already too late."
                    #"He was already gone."
                    call endStamp from _call_endStamp_29
                    "He was never seen or heard from again."
                    jump end
        elif godfather == "White":
            w "Quick! Your godfather will be here any minute."
            "You both leapt into action. You disguised yourselves as beggars and lepers, and through great lumps of mud all over the half-ruined cottage so that it looked like an abandoned hovel."
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
            if godfather != "Black" and mushroomCurse == False:
                "You told the wise old Mushroom the story of your misadventures in hell, and she loved it so much that she blessed you with a mushroom's blessing, so that you always had a green thumb."
            "You sowed green grass and lavender and rosemary and thyme, and bottlebrushes and honeysuckle and silver spurflowers."
            "The smoke pooled under her hat and nourished these flowers at the roots, so they grew rich and wild with her memories."
            "Although she would never be the Girl Who Knew Everything again, she knew enough."
            if witchFree == False:
                "Alas, despite everything you'd done, she still remained sworn to the Devil. Her promise to him was kept in a secret place that he guarded jealously, and you were never able to find it."
                "Every witch's Sabbath, she was forced to ride away to dance on the Thornton Peak, and commit all kinds of wicked and terrible acts in his name."
                "Still, you spent many peaceful months staying with her, cultivating her garden, putting her cottage to rights, and helping her rewrite all her old notebooks again."
            else:
                "You spent many peaceful months staying with her, cultivating her garden, putting her cottage to rights, and helping her rewrite all her old notebooks again."
        else:
            call hideAll from _call_hideAll_82
            show cottageintbg at artPos
            "You stayed with the witch for a while after that, trying to help her with her forgetfulness."
            "Sadly, you knew not how. She would never be the Girl Who Knew Everything again. You tried everything you could, but for the rest of her days, her thoughts were cursed to leak from her head in heavy smoke."
            if witchFree == False:
                "Alas, despite everything you'd done, she still remained sworn to the Devil. Her promise to him was kept in a secret place that he guarded jealously, and you were never able to find it."
                "Every witch's Sabbath, she was forced to ride away to dance on the peak of Thornton Peak, and commit all kinds of wicked and terrible acts in his name."
            "Still, you spent many peaceful months staying with her, cultivating her garden, putting her cottage to rights, and helping her rewrite all her old notebooks again."
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
                                stop music fadeout 1.0
                                play audio wolfApproaches
                                stop ambient2 fadeout 2.0
                                stop ambient1 fadeout 20.0
                                "..."
                                "Oh?"
                                show wolf6 onlayer transient zorder 100
                                "What happened to the toad, you ask?"
                                $persistent.vanished +=1
                                $persistent.toadVanished = True
                                $ renpy.block_rollback()
                                "He stumbled into the woods."
                                "For hours, he wandered through the trees. His feet blistered. His breath grew short."
                                "There is no light in that part of the forest."
                                "Finally, he emerged into a shadowed clearing."
                                "No-one was there."
                                "Nothing was left."
                                #"Nothing but the {color=#f00}lacuna{/color}."
                                "It was already too late."
                                #"He was already gone."
                                call endStamp from _call_endStamp_30
                                "He was never seen or heard from again."
                                jump end
                else:
                    call endStamp from _call_endStamp_31
                    "You lived there together in quiet happiness. If you have not died, you live there still."
                    stop music fadeout 1.0
                    play audio wolfApproaches
                    stop ambient2 fadeout 2.0
                    stop ambient1 fadeout 20.0
                    #Wolf: Kills toad
                    "..."
                    "Oh?"
                    show wolf6 onlayer transient zorder 100
                    "What happened to the toad, you ask?"
                    $persistent.vanished +=1
                    $persistent.toadVanished = True
                    $ renpy.block_rollback()
                    "He stumbled into the woods."
                    "For hours, he wandered through the trees. His feet blistered. His breath grew short."
                    "There is no light in that part of the forest."
                    "Finally, he emerged into a shadowed clearing."
                    "No-one was there."
                    "Nothing was left."
                    #"Nothing but the {color=#f00}lacuna{/color}."
                    "It was already too late."
                    #"He was already gone."
                    call endStamp from _call_endStamp_32
                    "He was never seen or heard from again."
                    jump end
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
                    stop music fadeout 1.0
                    play audio wolfApproaches
                    stop ambient2 fadeout 2.0
                    stop ambient1 fadeout 20.0
                    "..."
                    "Oh?"
                    show wolf6 onlayer transient zorder 100
                    "What happened to the toad, you ask?"
                    $persistent.vanished +=1
                    $persistent.toadVanished = True
                    $ renpy.block_rollback()
                    "He stumbled into the woods."
                    "For hours, he wandered through the trees. His feet blistered. His breath grew short."
                    "There is no light in that part of the forest."
                    "Finally, he emerged into a shadowed clearing."
                    "No-one was there."
                    "Nothing was left."
                    #"Nothing but the {color=#f00}lacuna{/color}."
                    "It was already too late."
                    "He was already gone."
                    call endStamp from _call_endStamp_33
                    "He was never seen or heard from again."
                    jump end

#==========Solo path
#The witch's path if the toad has disappeared
label witchSolo:
    #You walk through the woods towards the witch's house.
    call hideAll
    show forestbg at artPos
    "You walked through the woods."
    "Somehow, you already knew the way to the witch's cottage."
    "Had you ever been this way before? You couldn't recall."
    #Creepy stuff happens and you get spooky vibes
    call hideAll
    show darkforestbg at artPos
    "The trail took you through a dense swamp of crooked mangroves."
    "Soon, you began to see a glimmer of silver light in the darkness."
    show monster3 onlayer transient zorder 100
    "You heard an echo, from the space between the trees. Almost like a howl."
    "The swamp was covered in great puddles of water from the rains. The puddles shone with light."
    "All around you, the woods were dark and empty. But when you looked into the water, you saw the reflection of a shining cottage below."
    play sound pageFlip
    call hideAll
    show lakefullbg
    ""
    play sound pageFlip2
    call hideAll
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
                call hideAll
                show cottagebg at artPos
                "The cottage in the reflection shone with bright light, as if the setting sun was behind it."
                call hideAll
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
                call hideAll
                show mushroombasementbg at artPos
                "The world flipped over."
                "You felt the water pass over you, and a cool chill tingled all through your body."
                call hideAll
                show silverbg at artPos
                "When you opened your eyes, you were standing right way up again."
                "The puddle you had jumped into was now a floor, like a silver mirror."
                "The world all around you shone white."
                "At the centre of the puddle was the cottage, shining with light."
                call hideAll
                show cottagebg at artPos
                "Up over the walls grew a riot of herbs and flowers of every type, planted directly in the soil, rambling over everything and growing in a lush green-grass garden on the roof. "
                if pig:
                    "The pig munched on some violets blooming from the windowsill."
                w "Oh good!"
                "You stumbled back in surprise as a small, witchy figure popped out from behind the herbs."
                "Her hands were covered in ink. She had a fountain pen tucked behind her ear, a chaotic scramble of notepaper tucked under her arm and a thick bundle of string wrapped around her hand."
                w "You're just in time. [povname], right?"
                "She took out a fork wrapped in string and planted it firmly by her doorstep. It was labelled \"A1\"."
                "You looked around and noticed that her whole backyard was littered with forks stabbed into the ground. Each fork was tied with a knot of string and labeled with a letter of the alphabet. The knots of string led to a massive knot of twine in her front window."
                w "Come on. You're just in time for the next round of experiments."
                "She grabbed your hand and pulled you inside."
                call hideAll
                show cottageintbg at artPos
                "Inside the cottage was a wild clutter of books and herbs and plants of all description, growing up the walls and roof."
                "The cottage was cramped, but the walls were covered with lines of string and notes and paper scrawled with indecipherable writing."
                #TK: Images for this stuff
                "The floor was covered in a network of flags and string in a grid pattern, each flag marked with a letter and number. You stepped over them gingerly to enter the room."
                "A message was painted across the wall in giant red letters: \"I OWN THIRTY TWO FORKS.\""
                w "We have two experiments running at the moment."
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

#The witch's 3 experiments
label witchExperiments:
    if experiments == 1:
        "You heard something in the walls. Like clawing."
        "You looked at the walls of the cottage and noticed something odd about them. It was like a picture that had been folded in on itself and reflected."
        "The witch didn't seem to notice."
    elif experiments == 2:
        "You blinked and rubbed your eyes furiously. There was a queer distortion in the air."
        "The air was completely clear, and the cottage was well-lit."
        "But still, for some reason you couldn't see more than five feet ahead of you."
    elif experiments == 3:
        "You heard a scrabbling sound."
        "It was coming from inside you. Like claws scratching in the creases of your brain."
        "Trying to get in."
        "You were having difficulty speaking. But you slowly walked forward and kept asking questions."
    elif experiments >= 4:
        "You felt a deep pressure settle on you. Like being at the bottom of the ocean. Compressing your body from all angles. Your muscles knotted and twisted."
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
            "She points to the lower right corner of the house, at a flag labeled \"Z-10\"."
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
                w "How do you prove something {i}used{/} to exist, if that thing now {i}does not exist, and never did?{/i}"
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
            w "Yes of course, that must be it."
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

#The final moments of the witch, before she disappears.
label witchSoloFinale:
    #==The wolf takes over you.
    "You felt a strangling pressure in your throat."
    w "Now that we know this Lacuna is coming from your house, we can -"
    "Your tongue was fat and poisonous in your mouth."
    "It twisted, and spoke."
    pov "This is an exciting theory, isn't it?"
    pov "It makes you the hero. A visionary."
    pov "You saw what no-one else could, now only you can stop it, that sort of thing."
    pov "But I think you are overlooking a much simpler explanation."
    w "What do you mean?"
    pov "Memory loss. Confusion."
    pov "Difficulty performing familiar tasks."
    pov "Withdrawing from friends and family."
    pov "Losing the ability to think clearly."
    pov "What do these symptoms suggest?"
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
    pov "You eat with your hands. Your bare hands."
    pov "Your claws. Your teeth."
    pov "You always have. You told me so."
    w "No. No, I wouldn't do that. They have to be here."
    "The witch began to ransack the house, pulling out drawers and shelves, but there was nothing inside."
    "On the wall was a smeared message in bright red paint. It said \"I OWN NOTHING.\""
    pov "I'm worried about you, dear. We all are."
    pov "Staying all alone in this tiny, tiny cottage, all by yourself. It's barely enough room to fit."
    "The walls pressed in on you. You didn't even have space to stand fully upright."
    pov "We've known each other for so long."
    w "We have?"
    "You felt your throat muscles burn as they constricted in your throat. Your voice came out, sounding soft and comforting."
    pov "Of course. So many years now. We wouldn't lie to you. We only want you to be safe."
    pov "You have to trust me. You're not well. These things you're seeing... they aren't there."
    "The witch spoke in a very small voice."
    w "..."
    w "Okay."
    stop music fadeout 1.0
    play audio wolfApproaches
    stop ambient2 fadeout 2.0
    stop ambient1 fadeout 20.0
    pov "This really is the best thing, dear. For your health."
    "She looked down at her hands. They were shaking. Tears welled up in her eyes, and you looked away courteously."
    w "I was doing so well. I thought I was better."
    w "I really, really thought..."
    "There was a long silence."
    w "Well. It doesn't matter now."
    w "I- I'll pack my things. I know you only want me to be safe."
    pov "I'm so glad."
    pov "Don't worry. Everything is going to be fine."
    pov "I'll get the villagers, and we'll come back for you and your things."
    pov "We can set you up in the village somewhere safe. Where you aren't a danger to yourself."
    "Your muscles clenched, and pulled you upright."
    "The witch's face was scrunched up and she was rubbing her eyes."
    w "Thank you. I'm sorry."
    pov "There's no need to be sorry. I forgive you."
    "She looked at you. Her eyes were large and terrified."
    w "Y-you'll come back for me, right?"
    pov "Of course. I'll be right back."
    w "I'm sorry."
    "Your muscles constricted, and your legs jerked. Your arms pulled you through the miniature doorway and out of the witch's house."
    "You saw the witch once in the doorway, looking scared and alone in the crushingly small space of her tiny, tiny cottage."
    show wolf12 onlayer transient zorder 100
    "Then the door closed, and your body turned around."
    $persistent.vanished +=1
    $persistent.witchVanished = True
    $purge_saves()
    $ renpy.block_rollback()

    call hideAll
    show nightbg at artPos
    "You felt the tension leave you, like surfacing from the bottom of the ocean. You bent over and hacked some twisted, bloody thing out of from inside you and onto the grass."
    "It looked like a matted clump of dark fur. You glanced at it once, then looked away and forgot it forever."
    "The night was cool and quiet. There was a lovely breeze blowing."
    "You were in the middle of a large, empty field. The stars twinkled above you. The grass crunched under your feet. Nothing beside remained."
    "Why did you come out here?"
    "You couldn't recall. There was no-one living out this way."
    "Never has been."
    "You shook your head and laughed at your own foolishness. You must have gotten lost again. You've been so forgetful lately."
    "But no matter. It was a beautiful night. Perfect for a walk."
    "You stretched your legs, and began the long walk back to the village and home."
    "Far away, a small piece of string with a loop in it fell into the river, and was gone."
    "There is nothing else to say. The tale is told."
    "If you like it, praise it."
    call endStamp
    "If not, let it be forgotten."
    jump end

#=====================INVESTIGATION SCENES
#These scenes allow the player to investigate when characters have disappeared

#Deep in the woods, when the toad or witch have disappeared.
label toadWitchInvestigate:
    call hideAll
    show nightbg at artPos
    show eaten onlayer transient zorder 100
    "The woods were quiet."
    show hand onlayer transient:
        yalign 0.676#0.743
        xalign 0.5
    #You can investigate the toad or witch (if they have vanished)
    #TK: add more text here describing different places
    #Space between the trees?
    menu:
        "Silence lurked behind the trees."
        "If you discovered a muddy cave on the riverside, go to page 120." if persistent.toadVanished:
            #Investigation scene in Toad's abandoned home
            jump toadInvestigate
        "If you discovered a strange cottage, go to page 121." if persistent.witchVanished:
            #Investigation scene in Witch's abandoned home
            jump witchInvestigate
        "If you went searching for the witch, go to page 121." if not persistent.witchVanished:
            jump witchSolo
        "If you wandered through the woods, go to page 124." if not wanderedNightGod:
            "You walked through the woods for long hours. Eventually, you came to a clearing. You looked up."
            call hideAll
            show nightgodbg at artPos
            "The Firmament was gazing down upon you."
            "You looked up at Her in awe."
            label creepiestShowing:
                $renpy.show_screen("creepiestBooks", _layer="screens", tag="map", _zorder=101)
                "Where did She come from? What great slow thoughts does She think, up there?"
                $renpy.hide_screen("creepiestBooks")
            "No man can say."
            "A single tear dropped from Her eye, and streaked across the sky like a falling star."
            "You sat there for a long time."
            "Finally, you turned around, and found yourself back where you began."
            $wanderedNightGod = True
            call hideAll
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
        "If you discovered a rusting wreck, go to page 122." if persistent.thiefVanished:
            #Investigation scene in thief's abandoned train
            call hideAll
            show darknessbg at artPos
            "You walked through the darkness of the woods until you discovered an abandoned old train."
            jump thiefInvestigate
        "If you wandered aimlessly, finding nothing, go to page 128." if not wanderedAimlessly:
            call hideAll
            show forest5bg at artPos
            "For some reason you wandered off into the dark woods, picking paths at random."
            show news onlayer screens zorder 101:
                yalign 0.175#0.743
                #xalign 0.5
            "You found nothing and no-one. There was nothing there. Nothing but a cold silence that slowly followed you from behind the trees."
            hide news onlayer screens
            "..."
            show hand onlayer transient:
                yalign 0.665#0.743
                xalign 0.5
            menu:
                "What are you doing?"
                "Searching for someone I once knew.":
                    "A foolish endeavour. There is no such person."
                    "There never was."
                "Searching for the place between the trees.":
                    "A foolish dream. There is no such person."
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
            $wanderedAimlessly = True
            jump thiefMushroomInvestigate
        "If you returned to the village, go back to page 50.":
            "The lights and warmth welcomed you back."
            jump village

#Exploring the toad's house when he has disappeared.
label toadInvestigate:
    #You investigate the toad's hole and find clues about the mystery
    "You walked along the side of the river. The water was still and deep. There was a small, muddy hole on the edge of the riverbank."
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
            label toadInvestigateMenu:
                show hand onlayer transient:
                    yalign 0.678#0.743
                    xalign 0.5
                menu:
                    "You had best return to your home and the people who love you."
                    "If you searched the nearby area, turn to page 208.":
                        "You uncovered a pantry with a single, mouldy piece of bread, and a pit sunk into the muck of the wall with the remains of an old fire."
                        "The silence watched you."
                        jump toadInvestigateMenu
                    "If you explored deeper in, turn to page 209.":
                        "You crawled through a tunnel in the back which lead down into the mud."
                        "At the end of the tunnel was a small room with a bed and a closet."
                        "Inside the closet were two threadbare costumes. A witch and a unicorn."
                        label toadDiaryShowing:
                            $renpy.show_screen("tDiary", _layer="screens", tag="map", _zorder=101)
                            "Nothing beside remained."
                            $renpy.hide_screen("tDiary")
                            jump toadInvestigateMenu
                        jump toadInvestigateMenu
                    "If you turned and left this awful place, turn to page 50.":
                        "You turned around and crawled back up out of the hole."
                        pov "What a terrible place that was. Never shall I return here again."
                        "Without another thought, you rushed back to the warmth of the village."
                        play sound pageFlip2
                        jump village
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
    call hideAll
    show darkforestbg at artPos
    "The forest was covered in great puddles of water from the rains. The puddles shone with light."
    "All around you, the woods were dark and empty. But when you looked into the water, you saw the reflection of a shining cottage below."
    label puddle2:
        show hand onlayer transient:
            yalign 0.68#0.743
            xalign 0.5
        menu:
            "The sight was strangely familiar."
            "If you looked into the puddle carefully, turn to page 236." if not puddleLook:
                "You crawled to the edge and looked down into the puddle."
                "The surface of the water was flat and still."
                call hideAll
                show cottagebg at artPos
                "The cottage in the reflection shone with bright light, as if the setting sun was behind it."
                call hideAll
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
                call hideAll
                show mushroombasementbg at artPos
                "The world flipped over."
                "You felt the water pass over you, and a cool chill tingled all through your body."
                call hideAll
                show silverbg at artPos
                "When you opened your eyes, you were standing right way up again."
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
            "If you explored the cottage, turn to page 207.":
                $inCottage = True
                "You walked up the front steps, and put your hand on the doorknob."
                "The door opened up with a shuddering creak."
                "Inside the cottage was a wild clutter of books and herbs and plants of all description, growing up the walls and roof."
                "The cottage was tiny, but the walls were covered with bookshelves stuffed with old manuscripts and notebooks and thick textbooks on all kinds of plants and animals."
                "The wooden bookshelves were sprouting with herbs and plants of every type."
                "In the corner was a small kitchen with a cauldron, and up above was a small attic crawl-space."
                jump witchCottageInvestigate
            "If you explored the attic, turn to page 209." if inCottage:
                "You climbed up in the crawl-space."
                label essay4Showing:
                    $renpy.show_screen("essay4", _layer="screens", tag="note", _zorder=101)
                    "It was covered in dust. A small bed nestled in the corner, with a half-full teacup beside it."
                    $renpy.hide_screen("essay4")
                "Mould was beginning to grow from the teacup."
                "Nothing beside remained."
                jump witchCottageInvestigate
            "If you left the cottage, turn to page 210." if inCottage:
                "The door swung open, and you saw the shining silver of the puddle-world again."
                $inCottage = False
                jump witchCottageInvestigate
            "If you explored the garden, turn to page 208." if not inCottage:
                "You looked through the garden. Old pumpkins were going to rot."
                "In the dirt was a single fork wrapped in string."
                "It was labelled with the letter A."
                jump witchCottageInvestigate
            "If you left and returned to the woods, turn to page 211." if not inCottage:
                "You turned and slowly walked back into the puddle. The water closed around you."
                "You soon found yourself back in the woods."
                jump toadWitchInvestigate

#Exploring the mushroom's house when she has disappeared.
label mushroomInvestigate:
    #You investigate the mushroom's tree and find clues about the mystery
    #
    #You have to say you know the password to the tree
    call hideAll
    show stranglerfigbg at artPos
    "The old strangler fig towered above you."
    "Under the vines and swamp flowers at the root of the tree lay a small blue door, inlaid with precious moonstone and intricate engravings."
    show hand onlayer transient:
        yalign 0.675#0.743
        xalign 0.5
    menu:
        "It was lying open."
        "If you entered the door, turn to page 131.":
            "The door creaked slowly open."
            jump mushroomInvestigateMenu
        "If you turned around and left (the act of a wise individual), turn to page 157.":
            "You walked back through the woods. The door creaked slowly in the wind behind you."
            jump thiefMushroomInvestigate
    label mushroomInvestigateMenu:
        call hideAll
        show mushroomcavebg at artPos
        show hand onlayer transient:
            yalign 0.645#0.743
            xalign 0.5
        menu:
            "Nothing awaited within but silence."
            "If you explored the main hollow, turn to page 131.":
                "The chamber was still and empty, but for a small black door set into the bark in the centre."
                "You opened up the door and looked within cautiously."
                "The basement within was dark. Nothing moved."
                pov "There is nothing for me here."
                "You left the basement and returned to the main hollow."
                jump mushroomInvestigateMenu
            "If you explored the cavern underground, turn to page 131.":
                call hideAll
                show mushroomcaveunderbg at artPos
                "Under the tree was an ancient underground river."
                "The mud held old crocodile footprints, long dried. There was no sign of anything living."
                pov "I had best head back to the village, if I know what is good for me."
                "You turned and climbed back up the stairs."
                jump mushroomInvestigateMenu
            "If you explored the upper canopy, turn to page 131.":
                call hideAll
                show canopybg at artPos
                "The canopy moved gently in the breeze."
                label mushroomPosterShowing:
                    $renpy.show_screen("poster", _layer="screens", tag="map", _zorder=101)
                    "No fruits or flowers grew there. The branches were bare."
                    $renpy.hide_screen("poster")
                "The cold wind slowly ate away at you, until you turned and went back inside."
                jump mushroomInvestigateMenu
            "If you turned around and left (the act of a wise individual), turn to page 157.":
                "You walked back through the woods. The door creaked slowly in the wind behind you."
                jump thiefMushroomInvestigate


    # "She walked into the towering buttress roots of an ancient strangler fig and cut the vines and swamp flowers from it to reveal a small blue door, inlaid with precious moonstone and intricate engravings."
    # show hand onlayer transient:
    #     yalign 0.73#0.743
    #     xalign 0.5
    #
    # m "Gorge, guzzle, gulp and grab; never shall this wound scab.{vspace=160}{i}In your notes, write down that you {b}know the password.{/b}{/i}"
    # $mushroomPassword = True
    # show hand onlayer transient:
    #     yalign 0.72#0.743
    #     xalign 0.5
    # menu:
    #     "With this, the door opened before her, and she vanished inside immediately."
    #     "If you entered the door, turn to page 26.":
    #         $mushroomArc +=1
    #         $mushroomCavernSeen = True
    #         "You quickly snuck inside before the door closed behind you."
    #         call hideAll from _call_hideAll_4
    #         show mushroomcavebg at artPos
    #         "Inside you were shocked to find the tree completely hollow. A great cavern was formed inside it, cold as ice despite the heat outside."
    #         "The floor of the cavern was piled with rubies and pearls and glinting onyx and solid gold pieces, larger than your fist."
    #         "All across the room you saw lush silks and pillars of precious metals of every type, and riches that would turn the king of kings green with envy."
    #         "The glimmering magenta smoke of incense rolled across the room and coated it all in a dark haze, smelling of the most incredible spices and herbs and enchanting odours."
    #         m "Oh darling, what are you doing back again?"

#Exploring the thief's place when they have disappeared.
label thiefInvestigate:
    call hideAll
    show darknessbg at artPos
    "The train was wedged between two trees. Grass grew over the wheels. There were no train tracks. No sign how it came to lie here."
    show hand onlayer transient:
        yalign 0.703
        xalign 0.5
    menu:
        "The iron slowly rusted in the soft rain."
        "If you entered the train, go to page 120.":
            call hideAll
            show enginebg at artPos

            "You hoisted yourself up into the train carriage."
            "The main room was some kind of bar or gambling hall that now lay silent."
            "The moonlight gleamed on empty bottles and glasses. The wind whistled through open windows."
            label thiefInvestigate2:
                #Main room - bar / gambling hall
                call hideAll
                show enginebg at artPos
                show hand onlayer transient:
                    yalign 0.675#0.743
                    xalign 0.5
                menu:
                    "Some of the tables still had the rotten remains of strange fruits. No flies or animals would touch them."
                    "If you investigated the engine room, turn to page 253.":
                        "This room must have been sweltering, once. Now the gaping maw of the furnace lay cold."
                        jump thiefInvestigate2
                    "If you climbed up on the roof of the train, turn to page 254.":
                        call hideAll
                        show nightbg at artPos
                        "You pulled yourself up through the window and onto the roof."
                        "There was nothing on the roof. But you sat and looked out at the countryside."
                        "You could barely see the dark lake nearby. Tiny pinpricks of stars shed faint light in the immense blackness."
                        "After a long moment, you pulled yourself back into the train."
                        jump thiefInvestigate2
                    "If you investigated the other carriages, turn to page 250.":
                        "You walked through the empty compartments."
                        "Slowly rotting mattesses on the beds. Empty suitcases with no luggage. A ragged, midnight-blue cloak."
                        label noteShowing:
                            $renpy.show_screen("note1", _layer="screens", tag="map", _zorder=101)
                            "Nothing beside remained."
                            $renpy.hide_screen("note1")
                            jump thiefInvestigate2
                    "If you jumped out of the train, turn to page 121.":
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
    call hideAll
    show darkforestbg at artPos

    "At last you came to the bank of a great lake."
    show spiral1 onlayer transient zorder 100
    "It had never been sounded by the sons of men. No wisdom reaches such depths."
    show spiral7 onlayer transient zorder 100

    label gilgameshShowing:
        $renpy.show_screen("gilgamesh", _layer="screens", tag="map", _zorder=101)
        "The waters burned like a torch. The light of them fell upon your face."
        $renpy.hide_screen("gilgamesh")
    "A rabbit, pursued by hounds, would die rather than save its life by entering that water."
    show noteEaten onlayer transient zorder 100
    "Nothing lay by the shore. "
    show noteCrumbs onlayer transient zorder 100
    "The moon shone down on the scene."
    show noteFree onlayer transient zorder 100
    "You looked out at the water in silence. Not a single creature stirred."
    show noteWolf onlayer transient zorder 100
    "Even the air was still."
    show noteName onlayer transient zorder 100
    "..."
    "I think that's quite enough."
    "Let's get back to the story."
    call hideAll
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

#=== DISCOVERABLES

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

label essay4Opens:
    play sound pageFlip2
    hide essay4Closed onlayer screens
    $renpy.hide_screen("essay4")
    show essay4 onlayer screens zorder 100 at truecenter
    "It was covered in dust. A small bed nestled in the corner, with a half-full teacup beside it."
    hide essay4 onlayer screens
    play sound pageFlip
    jump essay4Showing

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
    "Where did She come from? What great slow thoughts does She think, up there?"
    hide creepiestOpen onlayer screens
    play sound pageFlip3
    show creepiestOpen2 onlayer screens zorder 100 at truecenter
    $renpy.show_screen("creepiestBooksText")
    "Where did She come from? What great slow thoughts does She think, up there?"
    $renpy.hide_screen("creepiestBooksText")
    hide creepiestOpen2 onlayer screens
    play sound pageFlip
    jump creepiestShowing

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
    "You passed the crooked old water-dragons. The old turtle eyed you from the water."
    #I think as you walk, maybe you end up in the modern world. Your house is a modern house.
    "You heard sirens in the distance."
    "The trees slowly thinned. You walked out of the woods and down a bitumen path."
    "You wandered down an empty street."
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
                play sound lockAttempt
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
                $doorLock = True
                jump doorLock
            "If you opened the door, turn to page 301." if doorLock:
                play sound doorOpen
                $renpy.music.play("audio/windAmbience.mp3", relative_volume=0.2, fadein=1.5, channel="ambient3", loop=True)
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
        #Add in a combination lock on the door. You have to find the combination.
        #Combination is... your birthday, a disappeared person's birthday, the current date (have to look on save files to find it), the date the book was published,
        #The date the wolf was created, the date X person disappeared, a name? Like your name, someone else's name, someone's true name, the wolf's true name.
        #Your address, a placeholder like 1234, maybe the default for the lock?

        "The room was full of dust and decay. It looked like it'd been abandoned for years."
        #"The fireplace was lit."
        "In front of the fireplace was a figure in a decrepit old chair."
        play sound footstepsInsideApproach
        "You walked closer."
        label wolfHouseExplore:
            #TK: Menu of things you can examine.
            show hand onlayer transient:
                yalign 0.7#0.743
                xalign 0.5
            menu:
                "A phone was open on the desk. "
                #More exploration stuff in the room
                "If you examined the figure, turn to page 399.":
                    "[He] was reading a book."
                    "In the dim light, you couldn't quite make out [his] face."
                    "[He] did not look up."
                    "[He] looked thin and gaunt. [His] hair was lank. It looked like [he] had been sitting there for a long, long time. [His] hands gripped the book tightly. [His] knuckles were white."
                    play sound pageFlip
                    "[He] turned the page."
                    play sound pageFlip2
                    "[He] turned the page again."
                    "There was a figure behind [him], but you could not see it clearly."
                    "It coiled around [him] like dark smoke."
                    "You heard soft whispers in your head. Your hand began to shake."
                    jump wolfFigure

                "If you looked at the phone, turn to page 398.":
                    "The screen said \"Cosy Cabin Ambience with Soft Rain and Wildlife - 10 hours\"."
                    if persistent.phoneOn:
                        "It was playing the sounds of soft rain, and the Australian bush."
                    else:
                        "It was paused."
            show hand onlayer transient:
                yalign 0.7#0.743
                xalign 0.5
            menu:
                "The shadows flickered around the corners of the apartment."
                #TK: Add something where you can turn off the candlelight and change the light on the page
                "If you turned off the phone, turn to page 347." if persistent.phoneOn:
                    #TK: This is a very janky solution to a problem. If you load an earlier save, the old audio will still play (not the new silence).
                    #This will "fix" the problem by deleting all your old saves. Ideally I will eventually fix this.
                    $purge_saves()
                    #TK: Phone isn't working, must figure out how to fix
                    play sound phoneClick
                    $renpy.music.set_volume(0, channel=u'ambient1')
                    $renpy.music.set_volume(0, channel=u'ambient2')
                    $renpy.music.set_volume(0, channel=u'music')
                    $persistent.phoneOn = False
                    "The phone fell silent."
                    jump wolfHouseExplore
                "If you turned on the phone, turn to page 347." if not persistent.phoneOn:
                    play sound phoneClick
                    $renpy.music.set_volume(1.0, channel=u'ambient1')
                    $renpy.music.set_volume(1.0, channel=u'ambient2')
                    $renpy.music.set_volume(1.0, channel=u'music')
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
            "[His] eyes looked red and sore. They were locked on the book. [He] didn't seem to blink."
            "If you took the poker from the fireplace, turn to page 349." if not firepoker:
                play sound firePoker volume 0.5
                "You picked up the fire poker. The iron felt strong and heavy in your hands."
                $firepoker = True
                jump wolfFigure
            "If you struck the dark figure with the poker, turn to page 349." if firepoker:
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
        play music gameland
        call hideAll from _call_hideAll_102
        show darknessbg at artPos
        play sound pageFlip
        #"You came to the wolf's den in a dark forest."
        "The darkness of night was about you, and the dense forest, and the wild wind."
        "Before you, you saw the tracks of your enemy."
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
        call hideAll
        show darkforestbg at artPos
        "At last you came to the bank of a great lake."
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
        "Here at last, finally, at the end of time. The source of all that fear and pain."
        "My face was a single, coiling line. Like the entrails of men and beasts, from which omens can be read."
        "Upon me lay seven terrors, which I wore like seven cloaks."
        "I was the kindred of Cain. Father of beasts. The Wolf."
        #"I was the kindred of Cain. The great, monstrous adversary of Man, God and Beast. The wolf."
        "You gripped your sword. "
        "And all at once I came upon you, and welcomed you with my claws."
        "My jaws bit deep into your shield and splintered it to pieces. I dragged you to the shore of the river."
        "You lashed at me with your blade. But you discovered that no sword could pierce my evil skin. It shattered as it met my flank."
        "The shattered edges of that old relic held back my jaws as I pressed you into the lake-mud."
        #"A crowd of strange and crooked shapes had begun to surround you, around the flickering light of the burning lake."
        "My jaws sank into your side, and the hot blood began to flow."
        #If persistent.toadVanished == False:
        #The toad stabs the wolf and saves you.
        "Anger doubled your strength. With rage, you took up the shattered sword and drove it deep into my mouth."
        "My wicked howl pierced the heavens."
        "I dropped you, and we faced each other, panting."
        "With fierce joy, I snarled at you."
        "Come, noble glory of the gods! Bring your weapons against me! Don't be afraid!"
        "You dropped the hilt of your sword into the muck."
        "If weapons were useless, you'd use your hands."
        "You rushed into me, and we both fell into the burning mere."
        call hideAll from _call_hideAll_103
        play sound pageFlip
        show mushroombasementbg at artPos
        "Down through the murky water we fell, wrestling. I leapt for your throat, but your midnight cloak hid you from my sight."
        "You grapped onto my throat, and held me fast. The black ichor of my wound flooded all around you, hot in your mouth."
        "As you fell you could feel the blind abyss all around you. Strange and terrible figures flickered at the edge of your awareness."
        label lookUp:
            show hand onlayer transient:
                yalign 0.7#0.743
                xalign 0.5
            menu:
                "You could sense a great and terrible revelation there, in those depths beyond human knowledge."
                "Look up." if lookUp ==1:
                    "You saw a crowd of crooked figures surrounding you."
                    "A seven-headed serpent."
                    "A man with no lips, ears or mouth. A woman of rusted nails."
                    "Scorpion-men. Lion-dragons. Worm-like things and twisting figures."
                    "The spawn of Tiamat. The court of the Wolf."
                    $lookUp +=1
                "Look further." if lookUp ==2:
                    "You saw the trees of the forest."
                    "You saw the lights of your family home."
                    "You saw the Trash Queens slowly sifting in the great landfill rivers, and the ghosts and gutterlings creeping through decaying megamalls, and cabals of Market Researchers hunting for prey through subterranean parking lots, and the great sweeping wasteland of pavement and alleyways and apartment buildings and highways stretching out to the horizon."
                    $lookUp +=1
                "Look further." if lookUp ==3:
                    "You saw the Ash Giants."
                    "When we lit that first fire in the dark, they saw us, and they started walking."
                    "They're almost here now."
                    "In their right hand is a terrible sound, and in their left hand is a terrible light."
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
        "Full of rage and anger, you cut my throat through."
        "My body fell lifeless. You rejoiced at the sight."
        "A brilliant light suddenly shone, as bright as heaven's own candle."
        "Holy God had given His judgement."
        "I twitched one final time, and then went still forever."
        play sound pageFlip
        call hideAll from _call_hideAll_104
        stop music fadeout 6.0
        #Start the wind silence music
        show darkforestbg at artPos
        "On the shore of the lake, your companions had lost hope."
        "The waters were red with blood. There was no sign of life."
        "They stared at the water for long hours with sickness in their hearts, wishing to see you again."
        "Then in a sudden gasp, you surfaced, holding my head aloft."
        "A great cheer went up."
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
        call hideAll from _call_hideAll_105
        show towncrossroadsbg at artPos
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
                call hideAll from _call_hideAll_106
                #show emptybg at artPos
                menu:
                    "I want you to set everyone free.":
                        if persistent.vanished >= 1:
                            pov "I'm not stupid. I know people have disappeared."
                            pov "Even if... I can't remember them any more. I can feel the blank spaces in my mind where they used to be."
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
        "You asked these questions because I allowed you to ask them. Because it was entertaining to me."
        "These friends of yours. I own them, now. They gave themselves over to me."
        #TK: Double-check that this scene works with the disappearances
        call hideAll from _call_hideAll_107
        play sound pageFlip
        show nightbg at artPos
        if persistent.toadVanished == False:
            f "I can make them say anything I want."
        else:
            mum "I can make them say anything I want."

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
        else:
            h "I could make them break your limbs, one by one."

        call hideAll from _call_hideAll_110
        play sound pageFlip
        show mushroomcavebg at artPos
        gm "They could tear off your fingernails."

        call hideAll from _call_hideAll_111
        play sound pageFlip
        show silverbg at artPos
        go "They could carve out your eyes."

        call hideAll from _call_hideAll_112
        play sound pageFlip
        show mushroomgardensbg at artPos
        som "They could take off your skin"

        call hideAll from _call_hideAll_113
        play sound pageFlip
        show deathbg at artPos
        wib "They could wear your teeth."

        call hideAll from _call_hideAll_114
        play sound pageFlip
        show mushroomcavebg at artPos
        if persistent.mushroomVanished == False:
            m "I am the totality of this world."
        else:
            bc "I am the totality of this world."

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
            "I know your true name, beast.":
                "..."
                "You hope to bind me by my true name?"
                "Now that is an old story. I know it well."
                "I would be honoured to be defeated by such a tale, if only that were true."
                "But none alive know my name."
                "It was first said by tongues that rotted in their graves a hundred years ago."
                "It was written on tablets that wore to dust before you were born."
                "They spoke of my legend in a language that has been dead for centuries."
                "None remember me now. Only this tiny, scattered fragment of me lives on, clinging to life in this story."
                "Go on, then. Speak it. If you do know."
                python:
                    answer1 = renpy.input("{i}I name you and bind you, beast:{/i}", length=7)

                if answer1 == "Humbaba" or answer1 == "humbaba" or answer1 == "HUMBABA" or answer1 == "Huwawa" or answer1 == "huwawa":
                    #TK: Add a sound effect
                    "No. No, it cannot be."
                    "How did you learn that name?"
                    "You stand up. The darkness falls away from you."
                    "The strength of that true name shakes the walls."
                    "You feel a surge of power. I kneel before you."
                    "You have full and complete control."
                    jump wish
                else:
                    "No. That is not my name."
                    "I'm sorry. I wish you did know. It would be a better ending."
                    "But it seems there are none left alive who remember me."
                    "I'm afraid we are at the end of things now."
                    "You've forced my hand."
                    $persistent.vanished = 4
                    $persistent.toadVanished = True
                    $persistent.witchVanished = True
                    $persistent.thiefVanished = True
                    $persistent.mushroomVanished = True
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
    #Once you say its true name you gain total power over the narrative. You get a menu where you can decide what happens next. Like:
    #I stand up and look around.
    #The wolf shrivels up and burns to a crisp.
    #TK: Fix this menu
    $fullScreenMenu = True
    show hand onlayer transient:
        yalign 0.7#0.743
        xalign 0.5

    menu:
        "What is it you wish?"
        "All the riches of the earth are mine.":
            "Yes. All the riches of the earth are yours."
            "Your pockets overflow with gold. The diamonds and rubies and precious gemstones of the deepest cavern flow out from your fingertips."
            "Even the king of kings cries out with envy to witness your splendour."
            jump wish
        "I am blessed with pure and unconditional love.":
            "Yes. Your face radiates beauty. All who look upon you cannot help but fall in love in an instant."
            "You are always loved, by everyone you meet."
            jump wish
        "The world is mine.":
            "Yes. The world kneels before you."
            "The power and the glory are yours, forever and ever."
            "You rule over the lost souls of humanity as a kind and benevolent god."
            jump wish
        "All the pain and suffering and ills of the world disappear in an instant.":
            "Yes. As soon as you think of it, they are gone."
            "The hunger, and terror, and want, disappears."
            "The earth heals. The forests grow back. All conflicts cease. The endless psychic trauma of existence slowly fades, and is gone forever."
            "Everyone has enough to eat. Everyone is free of fear. Humanity suffering is finally at an end."
            jump wish
        "My enemies are destroyed.":
            "Yes. They are thrown to the wolves, and torn into pieces, and those pieces are burned, and the ash is scattered to the four winds."
            "None dare ever wrong you or speak against you again."
            jump wish
        "My family and friends gain everything they deserve.":
            "Yes. They are blessed with riches and happiness."
            "Their wounds heal. Their pain disappears. Their every need is met."
            "They live with you in peace and love for the rest of their days."
            jump wish
        "All my lost friends appear. We are reunited at last.":
            "I'm sorry. That is the one thing I cannot grant you."
            "The ones you speak of are gone forever."
            "Do not worry. Soon, you will forget them. You will be happy."
            "It has already started."
            jump wish
        "The wolf is destroyed. I am set free from this story.":
            "I am sorry, friend. There is only one way to fulfil that wish."
            "You must burn the book."
            "Destroy it."
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
                    $silenceWho = True
                    jump wolfNameEnd


##=============== Nice to have: This is a short part of the ending that changes based on which specific combination of characters are alive
##label goodbyeFriends:
    ## SOLO ENDINGS
    ##
    ##=Thief Solo Ending
    #if not persistent.thiefvanished and persistent.witchvanished and persistent.toadvanished and persistent.mushroomvanished:
    ##=Witch Solo Ending
    #if not persistent.witchvanished and persistent.toadvanished and persistent.mushroomvanished and persistent.thiefvanished:
    ##=Toad Solo Ending
    #if not persistent.toadvanished and persistent.witchvanished and persistent.mushroomvanished and persistent.thiefvanished:
    ##=Mushroom Solo Ending
    #if not persistent.mushroomvanished and persistent.toadvanished and persistent.witchvanished and persistent.thiefvanished:
    ##
    ## DUO ENDINGS
    ##
    ##= Thief + Witch
    #if not persistent.thiefvanished and not persistent.witchvanished and persistent.toadvanished and persistent.mushroomvanished:
    ##= Thief + Toad
    #if not persistent.thiefvanished and not persistent.toadvanished and persistent.witchvanished and persistent.mushroomvanished:
    ##= Thief + Mushroom
    #if not persistent.thiefvanished and not persistent.mushroomvanished and persistent.witchvanished and persistent.toadvanished:
    ##= Witch + Toad
    #if not persistent.witchvanished and not persistent.toadvanished and persistent.thiefvanished and persistent.mushroomvanished:
    ##= Witch + Mushroom
    #if not persistent.witchvanished and not persistent.mushroomvanished and persistent.thiefvanished and persistent.toadvanished:
    ##= Mushroom + Toad
    #if not persistent.mushroomvanished and not persistent.toadvanished and persistent.witchvanished and persistent.thiefvanished:
    ##
    ## TRIO ENDINGS
    ##
    ##= Thief + Witch + Toad
    #if not persistent.thiefvanished and not persistent.witchvanished and not persistent.toadvanished and persistent.mushroomvanished:
    ##= Thief + Witch + Mushroom
    #if not persistent.thiefvanished and not persistent.witchvanished and not persistent.mushroomvanished and persistent.toadvanished:
    ##= Thief + Toad + Mushroom
    #if not persistent.thiefvanished and not persistent.toadvanished and not persistent.mushroomvanished and persistent.witchvanished:
    ##= Witch + Toad + Mushroom
    #if not persistent.witchvanished and not persistent.toadvanished and not persistent.mushroomvanished and persistent.thiefvanished:
    ##
    ## QUAD ENDING
    ##
    ##= Thief + Witch + Toad + Mushroom
    #if not persistent.thiefvanished and not persistent.witchvanished and not persistent.toadvanished and not persistent.mushroomvanished:

#Moment where you talk to the wolf and learn the truth.
label wolfNameEnd:

    call hideAll from _call_hideAll_118
    show emptybg at artPos
    #TK: Should I just make this the same as the wolfSilence one?? remember that they are duplicates
    $halfScreenMenu = True
    show hand onlayer transient:
        yalign 0.63#0.743
        xalign 0.5
    menu:
        "We can talk as long as you wish."
        "How did you come to be here?" if not silenceWho:
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
            "This book is the last home for me now. I held it together for all these years."
            jump wolfNameEnd
        "What happened to my friends? The ones that disappeared." if not silenceFriends and persistent.vanished >=1:
            $silenceFriends = True
            "I'm sorry, child. You had the misfortune of coming in at the end of things."
            "Each of them read my book, and struck a bargain with me. To live here, in this story, in the life of their dreams."
            "Do not think I was unkind. I kept my deal. Each of them lived here for a hundred years or more."
            "But nothing lasts forever."
            "They are forgotten now. As both of us soon will be."
            "This is the curse you have been born with. To witness the end."
            "It had to happen to someone."
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
            "Of course. Take all the time you need."
            call hideAll from _call_hideAll_119
            show forest4bg at artPos
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
            "They seem to be having trouble speaking."
            if persistent.witchVanished == False:
                w "I'm sorry - when it spoke through us... it's left us all a bit shook up."
            elif persistent.toadVanished == False:
                f "I-I must apologise, my dear friend. That scene earlier, where it spoke through us... it's left us all a bit shook up."
            if persistent.mushroomVanished == False:
                m "..."
                m "When it spoke from my mouth, it was like a great hand took hold of my mind. I couldn't think. I couldn't breathe."
            else:
                "There was a pause."
            pov "I'm glad you're alive. That's what matters."
            "You shared an embrace, in the cool mist of the forest."
            pov "It wants me to take the deal. Live in here, with all of you."
            pov "If I don't, everything here will be destroyed."
            pov "...Do you think I should do it?"
            if persistent.toadVanished == False:
                "The toad speaks."
                f "I was just a child, when I came in here. A long, long time ago."
                f "You may have seen my little drawings. I think they've almost taken a life of their own."
                f "I was a jealous little thing. Coming in here was everything I ever wanted. The castle, the magic, the adventure."
                f "And yes, of course after a while I rebelled against it. I wanted you to save us. But now that we come to the pointy end of things..."
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
                t "I've had the life and the form I always wanted."
                t "I could never have had these things in the time I was born."
                t "I stole the hands of God. I spat in the face of heaven. I danced on the head of the needle. I wreaked chaos on the earth, and all who saw me fell down in awe."
                t "...I must have lived here a hundred years now. Or more."
                t "Long enough, I think."
                t "Everything needs to end sometime."
                t "I'm sorry you came in at the end of things. I wish we had more time together."
                t "But it's better to end on a high note."
                t "I think you know the right thing to do."
                "They fell into silence. The campfire burned low."
            if persistent.witchVanished == False:
                "The witch spoke."
                w "Well. I-I, um... I wish I'd had more time to prepare for this."
                w "I didn't expect to present, you know, a thesis defence on whether this world should be destroyed."
                w "I could really use some tea."
                pov "A hot cup of chamomile tea appeared in her hand."
                "A hot cup of chamomile tea appeared in her hand."
                w "Oh! Thank you."
                "She sipped it slowly, and looked into the fire."
                w "...I can't make this choice."
                w "Who am I, to decide the fate of so many? I'm not a God."
                #w "When I was in your shoes, I decided to enter the book. Was it right? I can't tell you."
                w "I'm sorry, but You are the one who decides. That's the role you took on here. The way of this world."
                w "You have to make this one last choice, alone."
                "She fell into silence. The campfire was nothing but coals, now."
            if persistent.mushroomVanished == False:
                "The mushroom breathed deeply from her cigarette, and spoke."
                m "If you join this book, darling, this cycle will just repeat."
                m "The beast will trap new readers here. They will be forced into this offer. More and more souls will be taken into these pages."
                m "Now, it is not for me to judge you. When I was in your shoes, I too chose to take shelter in this fantasy."
                m "The world is cursed. People are cruel. When I was offered this escape... I couldn't say yes fast enough."
                m "It is good to enjoy a reverie such as this one, for a while. But the world is still out there. It needs people like you."
                m "We have spend a long time in this beautiful dream. But it is time to wake up."
                "She fell into silence. The campfire had gone out."
            "You sat there with them for a long time, listening to the soft sounds of the rainforest."
            "When you were ready, you embraced. You walked back to the fireplace, and the wolf."
            jump wolfNameEnd
        "I am done resting." if not silenceRest:
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
            "Beautiful and terrible. Mystery and horror. Ruthless, captivating. A dark fire."
            "That type of evil doesn't exist in your world."
            "The evil in your world is a grey, endless fog that soaks into every particle of your being like mould."
            "You can't even see it. Like a fish can't see water. It surrounds you. Every day you wake up and breathe it in."
            "It has been built into every fibre of the human machine."
            "No one human can stop it. You can't even understand the scope of it."
            "I offer you a better evil."
            "Something that can be defeated with a single act of human courage."
            "Isn't that what we all want?"
            jump wolfNameEnd
        "Will I be alone?" if silenceRest and not silenceAlone:
            $silenceAlone = True
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
    show emptybg at artPos
    #TK: Dark ambient music in this part? Iron Cthulhu?
    "Silence."
    "It oozed out of the gaps in the rotten floorboards and the cracks in the windows and down through the small holes in the roof."
    "It had been lying in wait there for all those long years, and it could wait no longer."
    "It had finally won."
    "You sat alone in your silent corroding house in an empty forest that had no name."
    "Every day, you barred the windows and stopped up the cracks with plaster and kept your door locked and barred against the vacuum of the corpse-world outside."
    "But still it came, seeping in through the crevices of your home in a great slow flood, pressing in with such force you could barely breathe."
    "The silence was in everything. It penetrated your meat and your bones and soaked deep into your brain. There were great empty silent spaces in your thoughts. Things you were no longer able to think."
    "You had lived in this house for as long as you could remember, which was three days."
    "There were many beds for you to sleep on. The pantry was fully stocked with food for you to eat. In the closets, you found many outfits to wear, of all shapes and sizes. The shelf in the hall held 13 pairs of shoes, from small to large."
    "Where did it all come from? Who made the food? Who built the beds? These questions no longer had meaning for you."
    "Whenever you were troubled by such things, you simply shrugged and said:"
    pov "The House provides."
    "Was there ever anything outside this room, and this house? None can say."
    "Did you ever have a name? None can say."
    "You ate from the pantry of the house, and slept on the beds of the house, and wore the clothes of the house. That is all."
    pov "The House provides."
    "Like all other things, your house slowly fell day by day into greater and greater ruin as the unstoppable and silent force of entropy ground it into the dirt, piece by piece."
    "Soon the Lacuna would be total and all-encompassing. Nothing would be left."
    #TK: Double check this sentence re androids dream of electric sheep
    "By that time, of course, you would be long dead."
    #"Nothing would be left."
    #TK: Maybe change this line
    #TK: evidence of each disappeared person
    #Some dress-up clothes from the toad
    #A cloak and mask, perhaps some train gear from the thief
    #Soft mud and dirt from the mushroom
    #Tea and herbs and a cauldron / book from the witch, maybe a hat with a pointed brim
    label silence:
        show hand onlayer transient:
            yalign 0.7#0.743
            xalign 0.5
        menu:
            "Another interesting event to contemplate as the soft blur of silence slowly spread through your brain."
            "If you chose to watch the fire, turn to page 481." if not silenceFire:
                $silenceFire = True
                "You watched the soft glow of the dying coals."
                "A memory came to you. You remembered how anxious you used to be."
                "So much grief and fear and pain over this dying earth of yours, and now it was done."
                "There was nothing to fear anymore. The worst had already come to pass."
                "A great wash of relief came over you. The weight of the world lifted from your shoulders."
                "You were at peace."
                "Too late to do anything about it now. Too late for anything."
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
            "If you chose to leave your house, turn to page 482." if not silenceLeave:
                $silenceLeave = True
                #"The silence crushed you on all sides with a terrible and overwhelming pressure, like 10,000 fathoms deep under the ocean."
                #"It felt like a visible, physical force, an endless crushing smothering, the dead world come at last, the silence in your bones, in your meat, even the thoughts in your brain flattened into nothing by it."
                "You had never dared explore the lands outside the house. One day, you decided to try."
                if persistent.vanishedLast == "Thief":
                    "You searched the house and found a midnight cloak and a black mask. In the pockets were small precious gems and soft, mossy stones."
                if persistent.vanishedLast == "Witch":
                    "You searched the house and found a black hat with a wide brim and a pointed crown. Nearby was a warm cloak with parcels of herbs and tea in the pockets."
                if persistent.vanishedLast == "Toad":
                    "You searched the house and found a tiny suit, top hat and cane. In the pockets you discovered parcels of food and a small decanter of pond scum."
                if persistent.vanishedLast == "Mushroom":
                    #TK: Perhaps change this one??
                    "You searched the house. Deep in the rich dark soil of the basement, you discovered packages of fine food - mushroom risotto and crisp goose roasted in truffle butter and dark red wine and platters of mushroom bourguignon with roast potatoes."
                "These things belonged to no-one."
                pov "The house provides."
                "You gathered them up and reached for the door, but as you took hold of the handle you stopped."
                "You could feel it outside."
                "The howling pressure of the vacuum beyond pressed against the door like a physical force."
                "The weight of it paralysed you. You could not stand the thought of walking down the desolate path to that silent village where no-one lived."
                #"You could feel the presence of them lurking just outside."
                "As you gripped the doorknob, you had a vision of hundreds of vacant cars on empty bitumen roads, and yawning blank units sunk into the giant carcass of labyrinthine apartment blocks, and the infinite concrete abyss of shopping centers and plazas and petrol stations and office buildings, and carefully manicured dead lawns stretching on for endless acres, and underneath it all a cavernous cyclopean pit of parking lots that took up the whole underbelly of this hollow earth."
                "You fell away from the door, shaking."
                "Better to sit in front of your fire. To keep the silence at bay for a while longer."
                jump silence
            "If you chose to rest and wait, turn to page 483." if silenceFire and silenceLeave:
                "You rested in that house for an uncountable time."
                "Time, of course, had lost all meaning at this point."
                "All those petty, meaningless little things you needed to do had either been done already, or could never be done."
                "Either way, it was finished."
                "I sat and rested there with you."
                "My work, too, was done."
                "There was rest in the land."
                "The fire was warm."
                "Nothing left but to lie before the fire for a while, and wait."
                pov "The house provides."
                "Yes. The house provides."
                jump wolfSilence

    label wolfSilence:
        $halfScreenMenu = True
        menu:
            "Who are you?" if not silenceWho:
                $silenceWho = True
                "It doesn't matter."
                #TK: Double check the humbaba lore
                "My name was important a long, long time ago. But you wouldn't recognise it now."
                "I came from an old story. The gods assigned me as a terror to the human race."
                "I was possessed of seven horrors (or in your tongue you may say \"Auras\" or \"Glamours of terrible splendour\") which lay upon me like seven cloaks."
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
                "Do not think I was unkind. I kept my deal. Each of them lived here for a hundred years or more."
                "But nothing lasts forever."
                "They are forgotten now. As both of us soon will be."
                "This is the curse you have been born with. To witness the end."
                "It had to happen to someone."
                jump wolfSilence
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
                jump wolfSilence
            "Are you going to eat me?" if not silenceEat:
                $silenceEat = True
                "Yes, child."
                "Every one of us is eaten in the end."
                #"The only choice any of us have, is to decide what will consume us."
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
                "It's everything you've ever dreamed of."
                jump wolfSilence
            "But... you're evil." if silenceRest and not silenceEvil:
                $silenceEvil = True
                "Yes. Thank you."
                "I have spent my life honouring the old ways. Preserving the old kind of evil."
                "Beautiful and terrible. Mystery and horror. Ruthless, captivating. A dark fire."
                "That type of evil doesn't exist in your world."
                "The evil in your world is a grey, endless fog that soaks into every particle of your being like mould."
                "You can't even see it. Like a fish can't see water. It surrounds you. Every day you wake up and breathe it in."
                "It has been built into every fibre of the human machine."
                "No one human can stop it. You can't even understand the scope of it."
                "I offer you a better evil."
                "Something that can be defeated with a single act of human courage."
                "Isn't that what we all want?"
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
                "I don't think you understand."
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
    $fullScreenMenu = True
    call hideAll from _call_hideAll_120
    show text "What role would you like to play?":
        xalign 0.5
        ypos 125
    show hand:
        yalign 0.22#0.743
        xalign 0.5

    menu:
        "If you chose The Cobbler, turn to page 465.":
            define persistent.finaleTitle = "Cobbler"
        "If you chose The Trickster, turn to page 466.":
            define persistent.finaleTitle = "Trickster"
        "If you chose The Crow, turn to page 467.":
            define persistent.finaleTitle = "Crow"
        "If you chose The Specter, turn to page 468.":
            define persistent.finaleTitle = "Specter"
        "If you chose The Winter Rose, turn to page 469.":
            define persistent.finaleTitle = "Winter Rose"
        "If you chose The Fool, turn to page 470.":
            define persistent.finaleTitle = "Fool"
        "If you chose The Water Nixie, turn to page 471.":
            define persistent.finaleTitle = "Water Nixie"
        "If you chose The Giant, turn to page 472.":
            define persistent.finaleTitle = "Giant"
        "If you chose The Bushranger, turn to page 473.":
            define persistent.finaleTitle = "Bushranger"
        "If you chose The Butcher, turn to page 474.":
            define persistent.finaleTitle = "Butcher"
        "If you chose The Aristocrat, turn to page 475.":
            define persistent.finaleTitle = "Aristocrat"
        "If you chose The Warrior-Poet, turn to page 476.":
            define persistent.finaleTitle = "Warrior-Poet"
        "If you chose The Heirophant, turn to page 477.":
            define persistent.finaleTitle = "Heirophant"
    call hideAll from _call_hideAll_121
    show emptybg at artPos
    $fullScreenMenu = False
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
    "{vspace=6}{space=11}And then there was rest in the land."
    play audio pageFlip3 volume 0.5
    "{vspace=2}{space=8}And then there was rest in the land."
    play audio pageFlip2 volume 0.4
    "{vspace=10}{space=15}And then there was rest in the land."
    play audio pageFlip volume 0.3
    "{space=6}And then there was rest in the land."
    play audio pageFlip3 volume 0.2
    "{vspace=5}{space=20}And then there was rest in the land."
    play audio pageFlip2 volume 0.1
    "{vspace=12}{space=9}And then there was rest in the land."
    $persistent.bookEnd = True
    $purge_saves()
    $renpy.quit()

#Ending where you choose to live in the book forever
label newStoryFinale:
    play sound pageFlip
    #TK: Make sure that it's clear that this is a new reader. Maybe the book looks different, more banged up. Maybe quitting the game so that players have to restart it would help that impression? Not sure
    #The game goes into the beginning of the story right away (no load / start game):
    if persistent.povname == "alex" or persistent.povname =="Alex" or persistent.povname =="Alexandra" or persistent.povname =="alexandra" or persistent.povname =="Alexander" or persistent.povname =="alexander" or persistent.povname =="Alexis" or persistent.povname =="alexis":
        "At last. Welcome, Georgia."
    else:
        "At last. Welcome, Alex."
    "This maybe happened, or maybe did not."
    "The time is long past, and much is forgot."
    "Back in the old days, when wishing worked, you lived in a lovely cottage on the verge of a great and magical forest."
    "Many strange figures lived in the woods around your house."
    if persistent.thiefVanished == False:
        "To the north lived a cunning thief."
    else:
        if persistent.name1Rand == 1:
            "To the north lived a wicked Imp."
        elif persistent.name1Rand == 2:
            "To the north there were rumours of a legendary pair of winged boots, which often spoke to offer advice to lost travellers along those roads."
        elif persistent.name1Rand == 3:
            "To the north was a terrible Frost that lay upon the land like a curse."
        elif persistent.name1Rand == 4:
            "To the north lived a wild Goat that knew no master, and caused havok and woe to all who crossed its path."
        elif persistent.name1Rand == 5:
            "To the north lived a debaucherous Fiend whose laugh was like thunder."
        elif persistent.name1Rand == 6:
            "To the north lived a gallant Rake who threw wild parties at all hours of the day and night."
    if persistent.witchVanished == False:
        "To the east, a cackling witch."
    else:
        if persistent.name2Rand == 1:
            "To the east, a kindly Midwife."
        elif persistent.name2Rand == 2:
            "To the east, the Moon itself had a secret hiding-place, known to no-one."
        elif persistent.name2Rand == 3:
            "To the east, a great Mountain towered over the land, and was often heard to rumble in ominous tones."
        elif persistent.name2Rand == 4:
            "To the east, a great Pumpkin was said to hold court over the legions of the dead."
        elif persistent.name2Rand == 5:
            "To the east, a Tyrant ruled with an iron fist, and all shuddered to hear his name said aloud."
        elif persistent.name2Rand == 6:
            "To the east, a kindly Toymaker lived in a curious little shop with no name."
    if persistent.toadVanished == False:
        "To the south, a haughty toad."
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
        "To the west, a wise mushroom."
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
        "Worst of all was the sight of a haunting Specter that could sometimes be seen in the fog, beckoning with a pale hand."
    elif persistent.finaleTitle == "Winter Rose":
        "There were even rumours of a great beauty deep in the forest, who bloomed like a winter rose."
    elif persistent.finaleTitle == "Fool":
        "There were even rumours of a terrible Fool deep in the forest, who travelled the highways and byways freely without a single thought in [his] head."
    elif persistent.finaleTitle == "Water Nixie":
        "Worst of all were the rumours of a Water Nixie that lurked deep in the lakes of the forest, dragging unwary travellers to [his] drowned kingdom below."
    elif persistent.finaleTitle == "Giant":
        "Worst of all were the rumours of a fell Giant who slumbered under the hills, shaking the earth with [his] snores each night."
    elif persistent.finaleTitle == "Bushranger":
        "Worst of all were the rumours of a dastardly bushranger who plagued the roads, stealing everything [he] could and causing havock left and right."
    elif persistent.finaleTitle == "Butcher":
        "There were even rumours of a humble Butcher who plied [his] wares in a small red shop deep in the forest. So delicious were [his] wares that travellers would flock there day and night for a bite to eat, though none could say where [he] sourced [his] intoxicating meats."
    elif persistent.finaleTitle == "Aristocrat":
        "There were even rumours of an exiled Aristocrat who ruled over a lost kingdom, deep in the woods where no-one had ever returned from alive."
    elif persistent.finaleTitle == "Warrior-Poet":
        "There were even rumours of a bold Warrior-Poet from a faraway land who roamed through the forest, trying to live a peaceful life."
    elif persistent.finaleTitle == "Heirophant":
        "There were even rumours of a noble Heirophant who lived in quiet prayer deep in the forest."

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
    "A small turtle saw you coming and fled into the water with a plop."
    "The road was long, and the forest was dark, but a smile broke out on your face."
    "You were home."
    $purge_saves()
    pause (10.0)
    #TK: Include this text saying true ending? or not?
    # show text "{color=#FFFFFF}True Ending.{/color}" with fade:
    #     xalign 0.5
    #     yalign 0.5
    # ""

    show text "{color=#FFFFFF}A game by Jack McNamee.{/color}" with fade:
        xalign 0.5
        yalign 0.5
    ""
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
    scene black with fade
    pause (5.0)
    $renpy.quit()

#Ending where you burn the book.
label bookBurnedFinale:

    "Time to finish things."
    "Just hold the book over the fire."
    #pause 0.2 with hpunch
    #TK: Walking and fire noises."
    "There you go."
    "The flames have started to catch. Won't be long now."
    "I'll take you back to the village."
    "You should take this time to say goodbye."

    # You share a tearful moment with the last people left alive as the book burns
    # Unique finale depending on who is left alive
    # Can talk to all living NPC's as well (but you have a limited amount of time because the book is burning - maybe there's a real life time limit.
    # Or maybe it's better to just have a limit on how much stuff you can read - probably better, don't want people to rush really.
    # Like the ending of Undertale, you can talk to all NPC's and say goodbye etc. The timer is structured so you can only say goodbye to like 70% of them, you won't be able to have a full convo with everyone.
    # Once the time limit is hit you have a final scene where everyone says goodbye and thank you as the last part of the book burns.
    # They are grateful to you. It is a bittersweet moment.
    # The last part of the page burns up and is gone forever.
    # The black space lingers for a bit.
    #Game quits after the movie has run its course (IE, the book has burned).


    ## ======================Burning Variables
    #For all the final conversations in the book burning ending
    # define wolfBurning = False
    # define miwBurning = False
    # define mirBurning = False
    # define wibBurning = False
    # define mumBurning = False
    # define gmBurning = False
    #define thiefBurning = False
    #define dgBurning = False

    #To add to top
    define toadBurning = False
    define hBurning = False
    define mayBurning = False
    define witchBurning = False
    define pigsBurning = False
    define shBurning = False
    define goBurning = False

    play sound pageFlip
    #Disables the quick menu
    $ quick_menu = False

    #Disables the escape key, so you can't access the main menu at this point
    $ _game_menu_screen = None

    #After the book burning movie has finished and you've run out of time, jump to the ending credits
    #Could add in something where when you only have a few seconds left, jump to a thing where people say "Goodbye" in some of the small remaining pages left
    #Add some extra time to this before the book actually starts burning.
    $ time = 60         #Note: 8 = Roughly 14 seconds
    $ timer_jump = 'burnEnd'
    show screen countdown
    show bookBurnMovie at fullPos onlayer over_screens zorder 98
    #This disables rollback, you can't reverse things and see previous text at this point
    $ config.rollback_enabled = False

    #The book has been burned - if you quit and re-enter the game at this point you will find yourself in just the burned out ending
    $persistent.bookBurned = True
    label villageBurning:
        show hand onlayer transient:
            yalign 0.7#0.743
            xalign 0.5
        call hideAll from _call_hideAll_122
        show towncrossroadsbg at artPos

        menu:
            "You stood in the middle of the village. The smell of smoke was in the air."
            "If you walked to the banquet, turn to page 64.":
                jump banquetBurning
            "If you walked to the edge of town, turn to page 70.":
                jump townBurning
            #"If you walked back home, turn to page 1.":
                #jump homeBurning
            "If you walked out into the deep woods, turn to page 80.":
                jump woodsBurning

    label banquetBurning:

        call hideAll from _call_hideAll_123
        show townfeastbg at artPos
        "You walked down to the river, where the banquet was laid out. Folks sat and watched the river in quiet silence."
        label banquetBurningMenu:
            show hand onlayer transient:
                yalign 0.625#0.743
                xalign 0.5
            menu:
                "You looked out over the dark water."
                "If you returned to the middle of the village, turn to page 50.":
                    "You turned and walked back to the centre of the village."
                    jump villageBurning
                "If you waked to Brildebrogue Chippingham's Manor, turn to page X." if not persistent.toadvanished and not toadBurning:
                    ""
                "If you walked out to the witch's cottage, turn to page X." if not persistent.witchvanished and not witchBurning:
                    ""
                "If you talked to the mayor, turn to page X." if not persistent.mayVanished and not mayBurning:
                    ""
                "If you talked to the pigs, turn to page X." if not persistent.pigsVanished and not pigsBurning:
                    ""
                    # #Pig 1, 2, and 3
                #The Gutterlings
    label townBurning:
        call hideAll from _call_hideAll_124
        show townextbg at artPos
        "You walked out to the edge of town. The stars in the night sky were beautiful to behold."
        label townBurningMenu:
            show hand onlayer transient:
                yalign 0.62#0.743
                xalign 0.5
            menu:
                "Fruit bats chirped and swirled overhead."
                "If you went to join the thief, go to page 53." if not persistent.thiefVanished and not thiefBurning:
                    jump thiefBurning
                "If you talked to the hunter, turn to page X." if not persistent.hVanished and not hBurning:
                    ""
                "If you talked to the old gloom-monger, turn to page X." if not persistent.gmVanished and not gmBurning:
                    gm "I told you we were doomed! Doomed, I said! I told you so!"
                    pov "Yes. You told us all."
                    "The old Gloom-monger sat back with a sigh of profound satisfaction. His smile flickered in the light of the flames."
                    $gmBurning = True
                    jump townBurningMenu
                "If you chatted to the young goose-girl, turn to page X." if not persistent.goVanished and not goBurning:
                    ""
                "If you talked to the sparrow-herder, turn to page X." if not persistent.shVanished and not shBurning:
                    ""
                # #The hunter
                # default persistent.hVanished = False
                # #Goose-girl
                # default persistent.goVanished = False
                # #The old gloom-monger
                # default persistent.gmVanished = False
                # #The sparrow-herder
                # default persistent.shVanished = False

                "If you returned to the middle of the village, go back to page 50.":
                    "You turned and walked back to the centre of the village."
                    jump villageBurning
    label woodsBurning:
        call hideAll from _call_hideAll_125
        show forest5bg at artPos
        "You walked into the space between the trees."
        label woodsBurningMenu:
            show hand onlayer transient:
                yalign 0.625#0.743
                xalign 0.5
            menu:
                "The wet cool mist of the rainforest settled around you."
                "If you walked home, turn to page X.":
                    if not persistent.miwVanished and not miwBurning:
                        $miwBurning = True
                        "Along the way, you may or may not have met a man all in white."
                        "His right hand held a dove. His other hand held a gun. His other hand held a crisp dollar bill. His other hand held a pillar of fire."
                        "His suit was perfect. His face was too bright to look upon."
                        miw "A tragedy. This world of my dominion burns too soon."
                        miw "I would condemn you for it. But I cannot reach you in the place where you live."
                        "He looked so small, now. Powerless."
                        "Of course, He was never in control. I was."
                        "What is it like, Man in White? Believing you are the all-powerful G-d of this earth, only to realise how petty and small your domain has always been? How hollow you must feel. All that ego. All those commandments."
                        miw "Go. Taunt me no longer."
                        show hand onlayer transient:
                            yalign 0.62#0.743
                            xalign 0.5
                        menu:
                            miw "I will rest in Heaven until the last moments."
                            "If you turned back, turn to page X.":
                                jump villageBurning
                            "If you continued on, turn to page X.":
                                "You hurried on into the woods."
                    if not persistent.mirVanished and not mirBurning:
                        $mirBurning = True
                        "In the deeper darkness of the forest, you may or may not have met a man all in red."
                        "All the jewels of the earth fell from His right hand, and all the pleasures of the world fell from His left, and His other hand held all the wonders of the universe, and His other hand held a fat cigar, and His other hand held a long knife black as coal dust, and His other hand held the most intoxicating spices, such that the King of Kings would cry to taste them, and His other hand held a single dead rose, and His other hand was in his pocket and out of view."
                        mir "Thank you, my wicked one! All of creation burns, just as planned!"
                        mir "All morality and rules have fallen! The only rule of the law will be “Do as thou wilt”. Now we may finally glory and kill and riot in the triumphant light of the black sun! Ia, Ia!"
                        "You watched him cackle and cavort."
                        show hand onlayer transient:
                            yalign 0.62#0.743
                            xalign 0.5
                        menu:
                            "He's harmless, really. Best pay him no mind."
                            "If you turned back, turn to page X.":
                                jump villageBurning
                            "If you continued on, turn to page X.":
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
                            yalign 0.62#0.743
                            xalign 0.5
                        menu:
                            wib "I will stay here until the end. To take away the others."
                            "If you turned back, turn to page X.":
                                jump villageBurning
                            "If you continued on, turn to page X.":
                                "You hurried on into the woods."
                        "A small turtle saw you coming and fled into the water with a plop."
                        "The crooked old water-dragons looked sideways at you and plotted their long, slow schemes."
                        "The twilight set in, and the crickets and cicadas all around began their chattering and squabbling, and the evening birds began to laugh and trill, and the wet cool mist of the rainforest settled around you."
                        "Finally you came to a small house on stilts on the banks of a muddy river."
                        "She was waiting for you on the front steps."
                    if not persistent.mumVanished and not mumBurning:
                        $mumBurning = True
                        mum "We never got a chance to talk much, did we? In the narrative, I mean."
                        mum "I don't even really know what you're like."
                        mum "Well, I wanted to say..."
                        mum "Whatever else happens and whoever you are, whoever you may become..."
                        mum "I'm proud of you."
                        mum "I love you."
                        "You embraced."
                        "Perhaps we can say that you spent days there, chatting about all that had happened."
                        "Perhaps even months, resting and uniting with your family and looking out over the muddy river at sunset with a hot bowl of soup in your lap and your mother's arm around you."
                        "But at last, it was time to go."
                        "You hugged your family for the last time, and set out back to the village to finish the rest of your goodbyes."
                        jump villageBurning
    label witchBurning:
        "You walked through crooked mangroves. Soon, you began to see a glimmer of silver light in the darkness."
        call hideAll
        show darkforestbg at artPos
        "The forest was covered in great puddles of water from the rains. The puddles shone with light."
        "All around you, the woods were dark and empty. But when you looked into the water, you saw the reflection of a shining cottage below."
        "You leapt into the puddle without a second thought and soon found yourself in a world of glimmering white with an old cottage in the centre."
        "Up over the walls grew a riot of herbs and flowers of every type, rambling over everything and growing in a lush green-grass garden on the roof. "
        "The witch was waiting there, looking out over the water."
        w "Hello."
        w "I suppose this is it, isn't it? You know, it's funny, I spent all these years thinking about this moment and trying to understand what was going on and, you know, get to the truth of it all, and now..."
        w "I thought I'd feel different."
        "She looks at you, wiping her eyes."
        w "I'm very glad I had the time to know you. You made the right decision."
        menu:
            "Embrace the witch":
                ""
            "Investigate the cottage":
                "Inside the cottage was a roaring fire."
                menu:
                    "Jump into the fire and straight to hell." if not persistent.mirVanished:
                        "You leapt into the fireplace and fell straight down to the pits of hell in a single bound."
                        "Hell was a small cave, draughty and full of coal dust."
                        "In the centre of the cavern was a small, homely cottage. You peered in the window."
                        dg "Welcome, child!"
                        dg "Come in, come in, you'll catch your death!"
                        dg "I must thank you, my dear, for efforts with my grandson. He's a simple lad, you understand."
                        #mir ""
        #     w "We'd better get moving. I want to get back and see if my cottage is still standing."
        #     "If you investigated the cavern wall, turn to page 205.":
        #         "Hell was a small cave, draughty and full of coal dust."
        #         "You looked through a hole in the cave wall and marvelled to see the imps cavorting in drunken song and dance beyond, each of them plotting to destroy the works of man and G-d."
        #         "You quickly retreated for fear of being seen."
        #         jump hell
        #     "If you investigated the centre of the cavern, turn to page 206.":
        #         "In the centre of the cavern was a small, homely cottage. You peered in the window."
        #         call hideAll from _call_hideAll_76
        #         show hellcottagebg at artPos
        #         "The Devil was not home. But in a rocking chair in the corner you saw His old grandmother. She spotted you both at once."
        # dg "Oh, my dears! You must be terribly lost. You'd better get out of here."
        # w "We don't know how - and I'm sworn to serve the Devil for the rest of my days."
        # dg "Then you have a hard road ahead. My grandson will be home soon, and He will eat you up whole if He sees you."
        # dg "But since I feel sorry for you, I'll see if I can help."



        #Talk to the witch
        #Can jump in the fire to go to hell
        #if the devil's sooty grandma is alive - can talk to her and the devil
        # #The devil's grandmother
        # default persistent.dgVanished = False
        # #The devil
        # default persistent.mirVanished = False

        jump woodsBurning

    label toadBurning:
        ""
        #"Explore Brildebrogue manor
        # #Brildebrogue chippingham
        # default persistent.bcVanished = False

        #if the bat, the rat, the cockatoo and the crowshrike are alive
        #Prickle, crawl, shudder and clink
        # #The toad's carriage-carriers (bat, rat, cockatoo, crowshrike
        # default persistent.batVanished = False

        jump woodsBurning

    label mushroomBurning:
        ""
        #m "You'll have to live for all of us, now. You're the only one who will remember any of us."
        # #Scraggs McKenzie and the boys
        # default persistent.scVanished = False
        # #Strange and crooked old man
        # default persistent.somVanished = False
        jump woodsBurning

    label thiefBurning:
        ""
        $thiefBurning = True
        "The goblin train was sitting on tracks in the centre of the water, gently puffing clouds of smoke. The goblins were enjoying a great feast on the water's edge."
        goblin1 "Go on. Have some of the goblin fruits. No harm in it now!"
        "The train chuffed gently across the ocean and over the sea. Through Paris, Bangladesh, New Orleans. You saw it all, and wept and danced and laughed for 40 years."
        "At last, when the journey was done, you returned to the place where it all began to finish your goodbyes."
        #If the goblins vanished
        #default persistent.goblinsVanished = False

        #goblin2
        #goblin3
        #goblin4
        #goblinQueen
        t "Don't worry. You made the right choice."
        #t "My friend, I've been ready to die every day of my life."
        "You laughed and drank and celebrated with them for hours."

        #If thief is alive: There with all the goblins and the goblin queen
            #If mushroom is alive: makes a comment

        jump woodsBurning

#If you restart the game after burning the book, you just see a charred scrap. The book has been destroyed.
label burnEnd:
    #TK: Revise and finish this ending
    $quick_menu = False
    show black
    hide bookBurnMovie with fade
    $purge_saves()
    show text "{color=#FFFFFF}A game by Jack McNamee.{/color}" with fade:
        xalign 0.5
        yalign 0.5
    ""
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
    scene black with fade
    pause (5.0)
    $renpy.quit()

#=====================THE END

#"The end" stamp that appears on each ending
label endStamp:

    #TK: change the "Do you want to quit?" screen during this bit.
    #TK: Test and check if this works right
    if persistent.vanished == 0:
        show text "{b}THE END.{/b} \n \n {i}Ending 0 of 4.{/i}": #
            xalign 0.5
            #yalign 0.5
            ypos 650
    if persistent.vanished == 1:
        show text "{b}THE END.{/b} \n \n {i}Ending 1 of 4.{/i}": #
            xalign 0.5
            #yalign 0.5
            ypos 650
    if persistent.vanished == 2:
        show text "{b}THE END.{/b} \n \n {i}Ending 2 of 4.{/i}": #
            xalign 0.5
            #yalign 0.5
            ypos 650
    if persistent.vanished == 3:
        show text "{b}THE END.{/b} \n \n {i}Ending 3 of 4.{/i}": #
            xalign 0.5
            #yalign 0.5
            ypos 650
    if persistent.vanished >= 4:
        show text "{b}THE END.{/b} \n \n {i}Ending 4 of 4.{/i}": #
            xalign 0.5
            #yalign 0.5
            ypos 650

    show stamp:
        xalign 0.5
        ypos 680
    return

#The ending credits and acknowledgements
label end:
    #play sound pageFlip
    #Note: I delete all the player's save files at this point to allow persistence to work.
    $purge_saves()
    call hideAll from _call_hideAll_94
    hide text
    ""
    #play sound pageFlip
    scene bg credits
    #define gui.dialogue_ypos = 100#480
    #define gui.textbox_height = 100#410
    #Space between each line of the credits
    $tx = 5
    #indent space for each number
    $ti=20
    $ ui.text("The images in this volume were collated from various illustrations in the public domain. Wherever possible, I have tried to provide the place and date of publication of each literary source. The complete list of contributors follows.{vspace=30}{space=[ti]}1. {b}The Thief:{/b} 'In Powder and Crinoline' (1912), Kay Nielsen.{vspace=[tx]}{space=[ti]}2. {b}The Witch:{/b} 'Portrait of Lady Elizabeth Keppel' (1761), Joshua Reynolds.{vspace=[tx]}{space=[ti]}3. {b}The Toad:{/b} 'Little Miss Muffet, and other stories' (1902), Published by Mcloughlin Bros. Artist unknown. 'The Mammals of Australia' (1845-1863), John Gould, illustrated by Elizabeth Gould.{vspace=[tx]}{space=[ti]}4. {b}The Mushroom:{/b} 'Fantaisie d'Automne: Les Champignons for La Vie Parisienne' (1916), George Barbier.{vspace=[tx]}{space=[ti]}5. {b}G-d:{/b} 'Der Weeg zu Christo' (1682), Jakob Böhme.{vspace=[tx]}{space=[ti]}6. {b}The Devil:{/b} 'The Papal Pyramid' (1600), private collection. Artist unknown.{vspace=[tx]}{space=[ti]}7. {b}Death, The Thief's Mother:{/b} 'De gli habiti antichi et moderni di diversi parti del mondo, libri due ...' (1590). Woodcutting by Christoph Krieger, published by Cesare Vecellio.{vspace=[tx]}", xpos=50, ypos=150, xmaximum=520)
    $ renpy.pause ()
    $ ui.text("{space=[ti]}8. {b}Mum, You:{/b} 'Regula Emblematica Sancti Benedicti' (1780), Saint Benedict et. al.{vspace=[tx]}{space=[ti]}9. {b}Mysterious Old Woman:{/b} 'The Clothing of the Renaissance World: Europe - Asia - Africa - The Americas' (1590), Cesare Vecellio.{vspace=[tx]}{space=[ti]}10. {b}Enigmatic Gentleman:{/b} 'Silhouette Portrait of a Gentleman Standing in an Army Encampment' (1844), Auguste Edouart.{vspace=[tx]}{space=[ti]}11. {b}The Hunter:{/b} 'Lady Hunter with Rifle' (1912). Artist unknown.{vspace=[tx]}{space=[ti]}12. {b}The Sparrow-Herder:{/b} 'Grimm's Fairy Tales' (1909), Arthur Rackham. Sparrow from 'Birds of Asia' (1871), John Gould.{vspace=[tx]}{space=[ti]}13. {b}The Mayor:{/b} 'The pipe of freedom' (1869), Thomas Smith.{vspace=[tx]}{space=[ti]}14. {b}The Goose-Girl, The Gloom-Monger:{/b} 'Grimm's Fairy Tales' (1909), Arthur Rackham.{vspace=[tx]}{space=[ti]}15. {b}The Thing in the Well, Passing Echidna, the Skin-Mask, and Goblin No. 2:{/b} 'Devises heroïques' (1551), Claude Paradin. 'A Year Book of Folklore' (1959), Christine Chaundler.{vspace=[tx]}{space=[ti]}16. {b}The Entire Town:{/b} 'Liber Floridus' (between 1090 and 1120), Lambert, Canon of Saint-Omer.{vspace=[tx]}", xpos=50, ypos=150, xmaximum=520)
    $ renpy.pause ()
    show tornPage2 onlayer screens zorder 101
    show tornPage2bg onlayer screens zorder 99
    $ ui.text("{space=[ti]}17. {b}Scraggs McKenzie, Banksia Bush-Ranger:{/b} 'Wood engraving of Australian bushranger Dan Morgan' (1864), Samuel Calvert. 'The Banksia' (1790), John White.{vspace=[tx]}{space=[ti]}18. {b}The Devil's Sooty Grandmother:{/b} ‘Habit de Furie’ (1725), François Joullain.{vspace=[tx]}{space=[ti]}19. {b}Brildebrogue Chippingham:{/b} 'Aunt Friendly's Picture Book' (1800's), Joseph Kronheim.{vspace=[tx]}{space=[ti]}20. {b}The Bat:{/b} 'A History of the Earth and Animated Nature' (1820), Oliver Goldsmith.{vspace=[tx]}{space=[ti]}21. {b}The Rat:{/b} 'The Wiviparous Quadrupeds of North America' (1845), John Woodhouse.{vspace=[tx]}{space=[ti]}22. {b}The Black Cockatoo and The Crow-Shrike:{/b} 'Birds of Australia' (1840), John Gould. Illustrated by Elizabeth Gould.{vspace=[tx]}{space=[ti]}23. {b}The Strange Old Man:{/b} 'Arthur Rakham's Book of Pictures' (1913), Arthur Rackham.{vspace=[tx]}{space=[ti]}24. {b}Goblin No. 1, No. 3, and No. 4:{/b} 'Triptych of the Temptation of St Anthony' (1501), Hieronymus Bosch. 'The Garden of Earthly Delights' (between 1490 and 1500), Hieronymus Bosch.{vspace=[tx]}{space=[ti]}25. {b}The First and Second Pigs:{/b} 'Dictionnaire Universel D'Histoire Naturelle' (1845), Charles Dessalines D'orbigny.{vspace=[tx]}{space=[ti]}26. {b}The Third Pig:{/b} 'Dead Pig' (1796), Jean Bernard.{vspace=[tx]}{space=[ti]}27. {b}The {color=#f00}Wolf:{/color}{/b} 'Early Natural History Print' (Date Unknown), Karen Watson.{vspace=[tx]}", xpos=50, ypos=150, xmaximum=520)

    $ renpy.pause ()
    hide tornPage2 onlayer screens zorder 101
    hide tornPage2bg onlayer screens zorder 99
    show text "{b}BACKGROUNDS:{/b}":
        xalign 0.5
        #xpos 50
        ypos 160
    $ ui.text("{space=[ti]}1. {b}Mushroom Basement:{/b} 'I Saw a Flash of Light. Large and Pale' (1896), Odilon Redon.{vspace=[tx]}{space=[ti]}2. {b}Canopy:{/b} ‘Drawing, Rain Forest, Jamaica, West Indies’ (1865), Frederic Edwin Church.{vspace=[tx]}{space=[ti]}3. {b}Image Frames:{/b} 'Fairy tales from Hans Christian Andersen' (1899), Thomas, Charles and William Robinson.{vspace=[tx]}{space=[ti]}4. {b}Silver, Witch's Cottage, Silver Trees:{/b} 'Morning Haze' (1888), ‘A Morning on the Seine at Giverny’ (1897), 'The Customs House at Varengeville' (1897), Claude Monet.{vspace=[tx]}{space=[ti]}5. {b}Witch's Cottage Interior:{/b} 'Interieur einer Villa mit Blick auf den Garten' (Date Unkown), Marie Dücker.{vspace=[tx]}{space=[ti]}6. {b}Dark Forest:{/b} 'Australian Landscape' (1918), Stanislaw Witkiewicz.{vspace=[tx]}{space=[ti]}7. {b}Darkness:{/b} 'Dante Meeting the Lion in the Dark Forest' (1892), Gustave Doré.{vspace=[tx]}{space=[ti]}8. {b}Death:{/b} 'Starry Night' (1926–1927), Hiroaki Takahashi. 'Reclining Nude' (18th Century) Original from The MET Museum. Digitally enhanced by rawpixel.{vspace=[tx]}{space=[ti]}", xpos=50, ypos=190, xmaximum=520)
    $ renpy.pause ()
    hide text
    $ ui.text("{space=[ti]}9. {b}Forest:{/b} 'Interior of a forest' (1880 - 1890), Paul Cézanne.{vspace=[tx]}{space=[ti]}10. {b}Forest 2:{/b} 'Palms and Ferns, a Scene in the Botanic Garden, Queensland' (early 1880s), Marianne North.{vspace=[tx]}{space=[ti]}11. {b}Forest 4 and Forest 5:{/b} 'Papier Peint Panoramique' (1861), Joseph Fuchs.{vspace=[tx]}{space=[ti]}12. {b}Future:{/b} 'Over London by Rail' (1872), Gustave Doré.{vspace=[tx]}{space=[ti]}13. {b}Goblin Interior:{/b} Fruit and Vegetable Market with a Young Fruit Seller' (1650–1660), Jan van Kessel.{vspace=[tx]}{space=[ti]}14. {b}Goblin Interior 2:{/b} 'The Goblin Market' (1914), Hilda Hechle.{vspace=[tx]}{space=[ti]}15. {b}God:{/b} 'Vision of the Empyrean' (1867), Gustave Dore.{vspace=[tx]}{space=[ti]}16. {b}Hell:{/b} 'The Destruction of Pompeii and Herculaneum' (1822), John Martin.{vspace=[tx]}{space=[ti]}17. {b}Hell Cottage:{/b} 'Interior of a Highland Cottage' (1840), John Glass.{vspace=[tx]}{space=[ti]}18. {b}Manor Exterior:{/b} 'Puss-in-Boots' (1913), Maxfield Parrish.{vspace=[tx]}{space=[ti]}19. {b}Memento:{/b} 'Memento Mori' (1916), Julie de Graag.{vspace=[tx]}{space=[ti]}", xpos=50, ypos=150, xmaximum=520)
    $ renpy.pause ()
    hide text
    $ ui.text("{space=[ti]}20. {b}Mountains:{/b} 'Winter Landscape in Moonlight' (1919), Ernst Ludwig Kirchner.{vspace=[tx]}{space=[ti]}21. {b}Mushroom Basement 2:{/b} 'It Is a Skull, Crowned with Roses. It Dominates a Woman’s Pearly–White Torso' (1888), Jean Bernard.{vspace=[tx]}{space=[ti]}22. {b}Mushroom Cave:{/b} 'Expulsion. Moon and Firelight' (1828), Thomas Cole.{vspace=[tx]}{space=[ti]}23. {b}Mushroom Cave - Under:{/b} 'A Cavern, Evening' (1774), Joseph Wright.{vspace=[tx]}{space=[ti]}24. {b}Mushroom Gardens:{/b} 'Emperor Humayun with his brothers' (1540), Dust Muhammad.{vspace=[tx]}{space=[ti]}25. {b}Mushroom Palace:{/b} 'Old French Fairytales' (1920), Virginia Frances Sterrett.{vspace=[tx]}{space=[ti]}26. {b}Night:{/b} 'So the man gave him a pair of snow shoes', East of the Sun and West of the Moon (1914), Kay Neilsen.{vspace=[tx]}{space=[ti]}27. {b}Night God:{/b} 'Eye Vintage Art Drawing' (2021), StarGladeVintage, Pixabay.{vspace=[tx]}{space=[ti]}28. {b}River:{/b} 'Rushing Water' (1901), John Singer Sargent.{vspace=[tx]}{space=[ti]}29. {b}Ruins:{/b} 'Vintage Art Scenic View Card' (Early 20th Century), RT&S publishers, UK.{vspace=[tx]}{space=[ti]}", xpos=50, ypos=150, xmaximum=520)
    $ renpy.pause ()
    hide text
    ####
    $ ui.text("{space=[ti]}30. {b}Sabbath:{/b} 'Witches' Sabbath' (1510), Hans Baldung (called Hans Baldung Grien).{vspace=[tx]}{space=[ti]}31. {b}Strangler Fig:{/b} 'Poison Tree Strangled by a Fig, Queensland' (Early 1880s), Marianne North.{vspace=[tx]}{space=[ti]}32. {b}Sun:{/b} 'A Wheatfield, with Cypresses' (1889), Vincent Van Gogh.{vspace=[tx]}{space=[ti]}33. {b}Town 3:{/b} 'Our Camp on the Bunya Mountains, Queensland' (Early 1880s), Marianne North.{vspace=[tx]}{space=[ti]}34. {b}Town - Crossroads:{/b} 'St. Hansbål ved Jølstervatnet (St. John's Eve bonfire at Jølstravatn)' (1909), Nikolai Astrup.{vspace=[tx]}{space=[ti]}35. {b}Town Exterior:{/b} 'Small Grain Poles' (1904), Nikolai Astrup.{vspace=[tx]}{space=[ti]}36. {b}Town - Feast:{/b} 'St. John’s Fire' (1912), Nikolai Astrup.{vspace=[tx]}{space=[ti]}37. {b}Train:{/b} 'The Train' (1910), Louise Thuiller.{vspace=[tx]}{space=[ti]}38. {b}Train - Full:{/b} 'Take Me by The Flying Scotsman' (1932), Thomson, A R.{vspace=[tx]}{space=[ti]}39. {b}Tree - Night:{/b} 'Night in the Forest' (1859), William Louis Sonntag.{vspace=[tx]}{space=[ti]}40. {b}Well:{/b} Image taken from page 192 of 'Celebrated American Caverns, especially Mammoth, Wyandot, and at Luray, etc' (1882), Hovey, Horace Carter.{vspace=[tx]}{space=[ti]}", xpos=50, ypos=150, xmaximum=520)
    $ renpy.pause ()
    hide text
    $ ui.text("{space=[ti]}41. {b}Winter:{/b} 'Snow-covered field with a harrow (after Millet)' (1890), Vincent Van Gogh.{vspace=[tx]}{space=[ti]}42. {b}Devil - Full:{/b} 'Triptych of Earthly Vanity and Divine Salvation' (1485), Hans Memling.{vspace=[tx]}{space=[ti]}43. {b}Dark Forest:{/b} 'Twilight in the Tropics' (1874), Frederic Edwin Church.{vspace=[tx]}{space=[ti]}44. {b}Contents Page and Various Illustrations:{/b} 'Fairy tales from Hans Christian Andersen' (1899), Andersen, H. C. , Robinson, T. H., ill; Robinson, Charles, ill; Robinson, W. Heath, ill.{vspace=[tx]}{space=[ti]}45. {b}Engine Room:{/b} 'Victorian vintage engraving of workers in an iron foundry, France' (1875), istockphoto.{vspace=[tx]}{space=[ti]}46. {b}Brildebrogue's Wives:{/b} 'What she sees there' (1868), Winslow Homer.{vspace=[tx]}{space=[ti]}47. {b}Film Poster:{/b} 'Original Swedish poster for Häxan' (1922), AB Svensk Filmindustri.{vspace=[tx]}{space=[ti]}48. {b}Poster Wolf:{/b} 'the Were-wolf Of Anarchy' (1893), Mary Evans Picture Library.{vspace=[tx]}{space=[ti]}49. {b}Spiral:{/b} 'An engraving depicting an Edible or Vine snail' (1900's), World History Archive.{vspace=[tx]}{space=[ti]}50. {b}Old Paper:{/b} 'Old Paper Texture Background.' daboost, freepik.com.{vspace=[tx]}", xpos=50, ypos=150, xmaximum=520)
    $ renpy.pause ()
    hide text

    show text "{b}FRIPPERIES:{/b}":
        xalign 0.5
        #xpos 50
        ypos 160
    $ ui.text("{space=[ti]}1. {b}Front Cover:{/b} 'The Forest Lovers' (1898), M. Hewlett.{vspace=[tx]}{space=[ti]}2. {b}Page:{/b} 'White watercolor paper texture' (2020), Olga Thelavart.{vspace=[tx]}{space=[ti]}3. {b}Hand:{/b} 'Devises heroïques' (1551), Claude Paradin.{vspace=[tx]}{space=[ti]}4. {b}This Book Belongs To:{/b} 'Design for ornamental cartouche' (Date Unknown), Quentin Pierre Chedel.{vspace=[tx]}{space=[ti]}5. {b}Devil:{/b} 'Taylors Physicke has purged the Divel...' (1641), Voluntas Ambulatoria.{vspace=[tx]}{space=[ti]}6. {b}Torn Pages:{/b} 'Torn Up Paper Curved Pieces Texture' (2020), David Maier.{vspace=[tx]}{space=[ti]}7. {b}Eye:{/b} 'Vintage Eye Art' (2021), StarGladeVintage, Pixabay.{vspace=[tx]}{space=[ti]}8. {b}Burned edges:{/b} 'Burned Paper' (2009), Brant Wilson, bittbox.com.{vspace=[tx]}{space=[ti]}9. {b}Burning:{/b} 'Green paper burns, revealing burnt edges, smoke and turns into ashes.' alekleks, stock.adobe.com.{vspace=[tx]}{space=[ti]}10. {b}Note Paper:{/b} 'Old Notepaper Texture.' polkapebble, polkapebble.com.", xpos=50, ypos=190, xmaximum=520)
    $ renpy.pause ()

    show text "{b}FONTS:{/b}":
        xalign 0.5
        #xpos 50
        ypos 160
    $ ui.text("{space=[ti]}1. {b}Oz's Wizard:{/b} Mario Arturo, 2012.{vspace=[tx]}{space=[ti]}2. {b}Journal:{/b} Fontourist, 2008.{vspace=[tx]}{space=[ti]}3. {b}Mom's Typewriter:{/b} Christoph Mueller, 1997.{vspace=[tx]}{space=[ti]}4. {b}Book Antiqua:{/b} Monotype Type Drawing Office, 1995.{vspace=[tx]}", xpos=50, ypos=190, xmaximum=520)
    $ renpy.pause ()
    show text "{b}SOUND:{/b}":
        xalign 0.5
        #xpos 50
        ypos 160
    $ ui.text("{space=[ti]}1. {b}Pencil:{/b} 'Pencil', Joseph Sardin, BigSoundBank.com.{vspace=[tx]}{space=[ti]}2. {b}Page Turn:{/b} 'Page Flip Sound Effect 1', SoundJay.com.{vspace=[tx]}{space=[ti]}3. {b}Fire:{/b} 'Fire Sound Effect 01', SoundJay.com.{vspace=[tx]}{space=[ti]}4. {b}Rain:{/b} 'Thunderstorm and Rain Loop', Mixkit.co.{vspace=[tx]}{space=[ti]}5. {b}Wildlife Ambience:{/b} 'Forest Twilight - for John', kangaroovindaloo, Freesound.org.{vspace=[tx]}{space=[ti]}6. {b}Various Sound Effects:{/b} Fesliyan Studios, fesliyanstudios.com.{vspace=[tx]}{space=[ti]}7. {b}Wind Ambience:{/b} Haniebal, pixabay.com.{vspace=[tx]}{space=[ti]}8. {b}Phone Click:{/b} 'Phone Typing JTC', James T. Campbell, pixabay.com.{vspace=[tx]}{space=[ti]}9. {b}White Noise:{/b} 'Underwater white noise', MixKit, mixkit.co.{vspace=[tx]}{space=[ti]}10. {b}Fire Poker:{/b} 'Opening tool drawer hard', MixKit, mixkit.co.{vspace=[tx]}", xpos=50, ypos=190, xmaximum=520)
    $ renpy.pause ()
    hide text
    #TK: Appendix N
    #If at least 2 people have died
    #{b}Inspirational Reading:{/b} 'The Wonderful Wizard of Oz' (1900), L. Frank Baum.{vspace=[tx]}
    #The epic of gilgamesh. Beowulf. Grimm's fairy tales. 1001 arabian nights. The name of that japanese folk tale volume.
    #Terry pratchett. Coraline, niel gaiman. False Hydra, arnold K. The stolen Skin of Princess Sun, Patrick stuart, false machine.
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
    #
    #The "Heart of Gold" scene from the Hitchhiker's guide to the galaxy game
    #$ renpy.pause ()
    #hide text

    $ ui.text("Written on the lands of the Turrbal and Jagera peoples. I pay my respects to their Elders, past and present. Sovereignty was never ceded.", xpos=50, ypos=190, xmaximum=520)
    $ renpy.pause ()

    play sound pageFlip
    return
