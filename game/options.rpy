## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.


if persistent.vanished == 0:
    define config.name = _("The Thief, the Toad, the Witch & the Mushroom.")
elif persistent.vanished == 1:
    if persistent.thiefVanished:
        define config.name = _("The Toad, the Witch & the Mushroom.")
    if persistent.toadVanished:
        define config.name = _("The Thief, the Witch & the Mushroom.")
    if persistent.witchVanished:
        define config.name = _("The Thief, the Toad & the Mushroom.")
    if persistent.mushroomVanished:
        define config.name = _("The Thief, the Toad & the Witch.")
elif persistent.vanished == 2:
    if persistent.thiefVanished && persistent.toadVanished:
        define config.name = _("The Witch & the Mushroom.")
    if persistent.thiefVanished && persistent.witchVanished:
        define config.name = _("The Toad & the Mushroom.")
    if persistent.thiefVanished && persistent.mushroomVanished:
        define config.name = _("The Toad & the Witch.")
    if persistent.toadVanished && persistent.witchVanished:
        define config.name = _("The Thief & the Mushroom.")
    if persistent.toadVanished && persistent.mushroomVanished:
        define config.name = _("The Thief & the Witch.")
    if persistent.witchVanished && persistent.mushroomVanished:
        define config.name = _("The Thief & the Toad.")
elif persistent.vanished == 3:
    if not persistent.thiefVanished:
        define config.name = _("The Thief.")
    if not persistent.toadVanished:
        define config.name = _("The Toad.")
    if not persistent.witchVanished:
        define config.name = _("The Witch.")
    if not persistent.mushroomVanished:
        define config.name = _("The Mushroom.")
elif persistent.vanished == 4:
    define config.name = _("The Wolf.")


#else:
    #define config.name = _("TestFailed.") #


#TK: Edit the config name so that it changes based on who's been killed (IE The Thief, the Toad, & the witch when the mushroom dies, etc)

define config.layers = ['master', 'transient', 'screens', 'over_screens', 'overlay']

## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.
#define gui.about = _p("""JACK MCNAMEE is a {color=#f00}w{/color}riter and game designer wh{color=#f00}o{/color} lives behind a keyboard in Brisbane, Australia. His other works inc{color=#f00}l{/color}ude the megagames God Emperor and We Are Not Alone. He hears something in the pipes. It’s here. {color=#f00}F{/color}or more information on Jack McNamee, please visit {a=https:/www.ashtowngames.com/}www.ashtowngames.com{/a}.
#""")

#

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "Thief-Toad-Witch-Mushroom"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

if persistent.bookBurned:
    define config.main_menu_music = ""
if persistent.phoneOn and persistent.vanished <=3:
    #define config.main_menu_music = "audio/Gymnopedies.mp3"
    define config.main_menu_music = "audio/cottagegore.mp3"

    #define config.main_menu_music = "audio/wildlife2.mp3"
elif persistent.bookEnd:
    #define config.main_menu_music = "audio/Gymnopedies.mp3"
    define config.main_menu_music = "audio/cottagegore.mp3"

    #define config.main_menu_music = "audio/wildlife2.mp3"
else:
    define config.main_menu_music = "audio/windAmbience.mp3"
## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "TheWitchtheThieftheToadandtheMushroom-1614593982"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
