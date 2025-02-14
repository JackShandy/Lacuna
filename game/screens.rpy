﻿################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    #Not showing the text box
    #background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    #Not showing the name box
    #background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input" color((25, 16, 0, 100)) font("fonts/journal.ttf") size(30)

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):


    window:
        style_prefix "choice"

        #Change for larger menus with lots of options
        if fullScreenMenu:
            yalign -0.3
        if halfScreenMenu:
            yalign -0.1
        if wolfMenu:
            yalign -0.02

        vbox:
            for i in items:
                #textbutton i.caption action i.action activate_sound "audio/page-flip.mp3" hover_sound "audio/pencil.wav"
                #Force an autosave and trigger renpy fixed choice each time the player makes a choice (which locks them in to the path they have chosen)
                textbutton i.caption action i.action activate_sound "audio/page-flip.mp3" hover_sound "audio/pencil.wav" #, renpy.fix_rollback() #, renpy.force_autosave()]

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

# if persistent.vanished >= 4:
#     style choice_vbox:
#         xalign 0
#         ypos 580
#         yanchor 0.6
#         spacing gui.choice_spacing
#
# else:
style choice_vbox:
    xalign 0
    ypos choice_menu_ypos
    yanchor 0.6
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            #textbutton _("Menu") action MainMenu()
            textbutton _("Back") action Rollback()
            #Removing history for now
            #textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            #textbutton _("Save") action ShowMenu('save')
            #textbutton _("Load") action FileLoad("quitsave", slot=True) #action ShowMenu('load')
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            textbutton _("Preferences") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    fixed:
        style_prefix "navigation"

        #xpos gui.navigation_xpos
        #yalign 0.5

        #spacing gui.navigation_spacing

        # if main_menu:
        #
        #     #textbutton _("Start") action Start()
        #
        #     #Image button for the start menu
        #     imagebutton auto "gui/mm_start_%s.png" xpos 25 ypos 321 focus_mask True action Play("sound", "audio/page-flip.mp3"), Start() hovered [ Play("sound", "audio/pencil.wav") ]
        #
        #     imagebutton auto "gui/mm_load_%s.png" xpos 20 ypos 354 focus_mask True action Play("sound", "audio/page-flip.mp3"), ShowMenu("load") hovered [ Play("sound", "audio/pencil.wav") ]
        #
        #     imagebutton auto "gui/mm_preferences_%s.png" xpos 20 ypos 387 focus_mask True action Play("sound", "audio/page-flip.mp3"), ShowMenu("preferences") hovered [ Play("sound", "audio/pencil.wav") ]
        #
        #     if _in_replay:
        #
        #         textbutton _("End Replay") action EndReplay(confirm=True)
        #
        #     elif not main_menu:
        #
        #         textbutton _("Main Menu") action MainMenu()
        #
        #     #textbutton _("About") action ShowMenu("about")
        #
        #     imagebutton auto "gui/mm_about_%s.png" xpos 25 ypos 421 focus_mask True action Play("sound", "audio/page-flip.mp3"), ShowMenu("about") hovered [ Play("sound", "audio/pencil.wav") ]
        #
        #     if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
        #
        #         ## Help isn't necessary or relevant to mobile devices.
        #         #textbutton _("Help") action ShowMenu("help")
        #         imagebutton auto "gui/mm_help_%s.png" xpos 29 ypos 454 focus_mask True action Play("sound", "audio/page-flip.mp3"), ShowMenu("help") hovered [ Play("sound", "audio/pencil.wav") ]
        #
        #     if renpy.variant("pc"):
        #
        #         ## The quit button is banned on iOS and unnecessary on Android and
        #         ## Web.
        #         #textbutton _("Quit") action Quit(confirm=not main_menu)
        #         imagebutton auto "gui/mm_quit_%s.png" xpos 27 ypos 485 focus_mask True action Play("sound", "audio/page-flip.mp3"), Quit(confirm=not main_menu) hovered [ Play("sound", "audio/pencil.wav") ]
        #
        # else:

        if persistent.sfw:
            add "gui/bookmark-s.png"
        else:
            add "gui/bookmark.png"


        if main_menu:
            #add "gui/saveCrossOff.png"
            imagebutton auto "gui/mm_menu_%s.png" xpos 25 ypos 241 focus_mask True action Play("sound", "audio/page-flip.mp3"), Return() hovered [ Play("sound", "audio/pencil.wav") ]
        else:
            #imagebutton auto "gui/mm_menu_%s.png" xpos 25 ypos 241 focus_mask True action Play("sound", "audio/page-flip.mp3"), Start("splashscreen") hovered [ Play("sound", "audio/pencil.wav") ]
            if burnMenu == False:
                imagebutton auto "gui/mm_menu_%s.png" xpos 25 ypos 241 focus_mask True action Play("sound", "audio/page-flip.mp3"), MainMenu() hovered [ Play("sound", "audio/pencil.wav") ]
        #Main Menu

        #Save
        #imagebutton auto "gui/mm_save_%s.png" xpos 22 ypos 283 focus_mask True action Play("sound", "audio/page-flip.mp3"), ShowMenu("save") hovered [ Play("sound", "audio/pencil.wav") ]

        #Load
        #imagebutton auto "gui/mm_save_%s.png" xpos 24 ypos 319 focus_mask True action Play("sound", "audio/page-flip.mp3"), LoadMostRecent() hovered [ Play("sound", "audio/pencil.wav") ] #ShowMenu("load")
        #Old
        #imagebutton auto "gui/mm_save_%s.png" xpos 24 ypos 319 focus_mask True action Play("sound", "audio/page-flip.mp3"), FileLoad("quitsave", slot=True) hovered [ Play("sound", "audio/pencil.wav") ] #ShowMenu("load")

        #Return button
        imagebutton auto "gui/mm_return_%s.png" xpos 24 ypos 279 focus_mask True action Play("sound", "audio/page-flip.mp3"), Return() hovered [ Play("sound", "audio/pencil.wav") ]


        #Preferences #old ypos: 356
        imagebutton auto "gui/mm_pref2_%s.png" xpos 24 ypos 316 focus_mask True action Play("sound", "audio/page-flip.mp3"), ShowMenu("preferences") hovered [ Play("sound", "audio/pencil.wav") ]

        #About old ypos: 389
        imagebutton auto "gui/mm_about2_%s.png" xpos 22 ypos 355 focus_mask True action Play("sound", "audio/page-flip.mp3"), ShowMenu("about") hovered [ Play("sound", "audio/pencil.wav") ]

        #Help old ypos: 430
        imagebutton auto "gui/mm_help2_%s.png" xpos 23 ypos 393 focus_mask True action Play("sound", "audio/page-flip.mp3"), ShowMenu("help") hovered [ Play("sound", "audio/pencil.wav") ]


        #TK: Look at the game on smartphones, figure it out
        if renpy.variant("pc"):

            #Quit old ypos: 466
            imagebutton auto "gui/mm_quit2_%s.png" xpos 24 ypos 430 focus_mask True action Play("sound", "audio/page-flip.mp3"), Quit(confirm=not main_menu) hovered [ Play("sound", "audio/pencil.wav") ]

            #TK: Remove commented out sections


            #textbutton _("History") action ShowMenu("history")

            #textbutton _("Save") action ShowMenu("save")






        #textbutton _("Load") action ShowMenu("load")
        #textbutton _("Preferences") action ShowMenu("preferences")


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    if persistent.continueButton:
        add gui.main_menu_background
    else:
        add gui.main_menu_noContinue_background

    if persistent.vanished >=1:
        add "gui/star1.png"
    if persistent.vanished >=2:
        add "gui/star2.png"
    if persistent.vanished >=3:
        add "gui/star3.png"
    if persistent.vanished >=4:
        add "gui/star4.png"
    #$ renpy.music.play("audio/rain.wav", channel="ambient1", loop=True)
    #$ renpy.music.play("audio/fire.mp3", channel="ambient2", loop=True) #fadein=0.5
    #renpy.sound.play("audio/rain.wav", loop=True)
    #renpy.sound.play("audio/fire.mp3", loop=True)
    ## This empty frame darkens the main menu.
    #frame:
        #style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    #use navigation

    if persistent.continueButton == False:
        imagebutton auto "gui/mm_start_%s.png" xpos 25 ypos 321 focus_mask True action Play("sound", "audio/page-flip.mp3"), Start() hovered [ Play("sound", "audio/pencil.wav") ]

    if persistent.continueButton == True:
        imagebutton auto "gui/mm_load_%s.png" xpos 20 ypos 354 focus_mask True action Play("sound", "audio/page-flip.mp3"), LoadMostRecent() hovered [ Play("sound", "audio/pencil.wav") ] #ShowMenu("load")
    #Old
    #imagebutton auto "gui/mm_load_%s.png" xpos 20 ypos 354 focus_mask True action Play("sound", "audio/page-flip.mp3"), FileLoad("quitsave", slot=True) hovered [ Play("sound", "audio/pencil.wav") ] #ShowMenu("load")

    imagebutton auto "gui/mm_preferences_%s.png" xpos 20 ypos 387 focus_mask True action Play("sound", "audio/page-flip.mp3"), ShowMenu("preferences") hovered [ Play("sound", "audio/pencil.wav") ]

    imagebutton auto "gui/mm_about_%s.png" xpos 25 ypos 421 focus_mask True action Play("sound", "audio/page-flip.mp3"), ShowMenu("about") hovered [ Play("sound", "audio/pencil.wav") ]

    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

        ## Help isn't necessary or relevant to mobile devices.
        #textbutton _("Help") action ShowMenu("help")
        imagebutton auto "gui/mm_help_%s.png" xpos 29 ypos 454 focus_mask True action Play("sound", "audio/page-flip.mp3"), ShowMenu("help") hovered [ Play("sound", "audio/pencil.wav") ]

    #Credits / Acknowledgements
    imagebutton auto "gui/mm_acknowledgements_%s.png" xpos 24 ypos 485 focus_mask True action Play("sound", "audio/page-flip.mp3"), Hide("main_menu"), Jump("credits")  hovered [ Play("sound", "audio/pencil.wav") ]
    #475
    #Hide(main_menu())


    if renpy.variant("pc"):

        ## The quit button is banned on iOS and unnecessary on Android and
        ## Web.
        #textbutton _("Quit") action Quit(confirm=not main_menu)
        imagebutton auto "gui/mm_quit_%s.png" xpos 27 ypos 520 focus_mask True action Play("sound", "audio/page-flip.mp3"), Quit(confirm=not main_menu) hovered [ Play("sound", "audio/pencil.wav") ]

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 132
    yfill True

    #background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -9
    xmaximum 375
    yalign 1.0
    yoffset -9

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

#    use game_menu(_("Preferences"), scroll="viewport"):
#screen game_menu("Preferences", scroll="viewport", yinitial=0.0):
screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    #TK: This is going wrong somehow.
    #if main_menu:
        #add gui.main_menu_background
    #else:
        #add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation
    #{color=#000000}{/color}
    #textbutton _("{size=+5}Return{/size}"):
        #style "return_button"

        #action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 15
    top_padding 57

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 132
    yfill True

style game_menu_content_frame:
    left_margin 19
    right_margin 10
    top_margin 5

style game_menu_viewport:
    xsize 432

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 5

style game_menu_label:
    xpos 0#24
    xalign -342
    ypos 25#57

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.return_xpos
    yalign 1.0
    yoffset -38  #-14


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    if persistent.vanished >= 4:
        add "gui/aboutEmpty.png"
    else:
        add "/gui/about.png"

    #add gui.about_background
    #add "gui/about.png"
    #background "gui/about.png"

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_(""), scroll="viewport"):

        style_prefix "about"

        vbox ypos 373 xpos 15:
            #label "[config.name!t]"
            #text _("Version [config.version!t]\n")
            #yalign 0.5
            ## gui.about is usually set in options.rpy.
            #if gui.about:
            #If 4 people have vanished, the "About the author" text vanishes
            if persistent.vanished >= 4:
                text "{alpha=0.9}{size=-4}\n{/size}{/alpha}" #
            elif persistent.vanished == 3:
                text "{alpha=0.9}{size=-4}JACK MCNAMEE is a writer and game designer. {b}{color=#f00}H{/b}{/color}is other works incl{b}{color=#f00}U{/b}{/color}de the {b}{color=#f00}M{/b}{/color}egagames God Emperor and We Are Not Alone. He lives {b}{color=#f00}B{/b}{/color}ehind {b}{color=#f00}A{/b}{/color} keyboard in {b}{color=#f00}B{/b}{/color}risbane, {b}{color=#f00}A{/b}{/color}ustralia. He hears me in the pipes now. It's too late for him. For more information on Jack McNamee, please visit {a=https:/www.ashtowngames.com/}www.ashtowngames.com{/a}.\n{/size}{/alpha}"  #
            elif persistent.vanished == 2:
                text "{alpha=0.9}{size=-4}JACK MCNAMEE is a writer and game designer. {color=#f00}H{/color}is other works incl{color=#f00}u{/color}de the {color=#f00}m{/color}egagames God Emperor and We Are Not Alone. He lives {color=#f00}b{/color}ehind {color=#f00}a{/color} keyboard in {color=#f00}B{/color}risbane, {color=#f00}A{/color}ustralia. Hurry. There isn't much time left. For more information on Jack McNamee, please visit {a=https:/www.ashtowngames.com/}www.ashtowngames.com{/a}.\n{/size}{/alpha}"  #
            elif persistent.vanished == 1:
                text "{alpha=0.9}{size=-4}JACK MCNAMEE is a writer and game designer. {color=#6d3d23}H{/color}is other works incl{color=#6d3d23}u{/color}de the {color=#6d3d23}m{/color}egagames God Emperor and We Are Not Alone. He lives {color=#6d3d23}b{/color}ehind {color=#6d3d23}a{/color} keyboard in {color=#6d3d23}B{/color}risbane, {color=#6d3d23}A{/color}ustralia. I began whispering to him some time ago. This text is the result. For more information on Jack McNamee, please visit {a=https:/www.ashtowngames.com/}www.ashtowngames.com{/a}.\n{/size}{/alpha}"  #
            elif persistent.vanished == 0:
                text "{alpha=0.9}{size=-4}JACK MCNAMEE is a writer and game designer. His other works include the megagames God Emperor and We Are Not Alone. He lives behind a keyboard in Brisbane, Australia. For more information on Jack McNamee, please visit {a=https:/www.ashtowngames.com/}www.ashtowngames.com{/a}.\n{/size}{/alpha}"  #
            text _("{alpha=0.9}{size=-4}A note on the translation: This story survives mostly by chance. A single copy of the original manuscript was recovered from a fire in the eighteenth century and then adapted. Some sections have been lost forever. The broken lines seen throughout indicate lacunae in the text.\n\nMade with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]. [renpy.license!t]{/size}{/alpha}")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## My screens #######################################################
##
##
## Reset the game ####
screen on_key_screen():
    zorder 9999
    key "0" action Jump("resetGame")





## Map ####

screen map: #Preparing the imagemap
    imagemap:
        idle "mapClosed.png"
        hover "mapClosedHover.png"

        hotspot (0, 0, 600, 496) clicked Jump("mapOpens") hovered [ Play ("sound", audio.pageFlip3)]

## Humbaba Back Photo ####

screen humbaba1: #Preparing the imagemap
    imagemap:

        idle "photo-1.png"
        hover "photo-2.png"

        hotspot (0, 736, 213, 115) clicked Show("humbaba2"), Hide("humbaba1"), [ Play ("sound", audio.pageFlip2)], SetVariable("humbabaShowing",False) hovered [ Play ("sound", audio.pageFlip3)]

screen humbaba2:
    imagemap:

        idle "photo-3.png"
        hover "photo-4.png"

        hotspot (75, 13, 450, 470) clicked Show("humbaba3"), Hide("humbaba2"),[ Play ("sound", audio.pageFlip2)] hovered [ Play ("sound", audio.pageFlip3)]

screen humbaba3:
    imagemap:

        idle "photo-5.png"
        hover "photo-6.png"

        hotspot (75, 13, 450, 470) clicked Hide("humbaba3"), [ Play ("sound", audio.pageFlip2)], SetVariable("humbabaShowing",True) hovered [ Play ("sound", audio.pageFlip3)]


## Note 1 ####

screen note1: #Preparing the imagemap
    imagemap:

        idle "note1Closed.png"
        hover "note1ClosedHover.png"

        hotspot (0, 0, 600, 696) clicked Jump("note1Opens") hovered [ Play ("sound", audio.pageFlip3)]

## Toad's Diary ####

screen tDiary: #Preparing the imagemap
    imagemap:
        idle "diaryClosed.png"
        hover "diaryClosedHover.png"

        hotspot (0, 0, 600, 696) clicked Jump("tDiaryOpens") hovered [ Play ("sound", audio.pageFlip3)]

## Mushroom's Poster ####

screen poster: #Preparing the imagemap
    imagemap:
        idle "posterClosed.png"
        hover "posterClosedHover.png"

        hotspot (0, 0, 600, 810) clicked Jump("posterOpens") hovered [ Play ("sound", audio.pageFlip3)]

## Witch Essays ####
screen essay1: #Preparing the imagemap
    imagemap:
        idle "essayClosed.png"
        hover "essayClosedHover.png"

        hotspot (0, 0, 600, 810) clicked Jump("essay1Opens") hovered [ Play ("sound", audio.pageFlip3)]

screen essay2: #Preparing the imagemap
    imagemap:
        idle "essayClosed.png"
        hover "essayClosedHover.png"

        hotspot (0, 0, 600, 810) clicked Jump("essay2Opens") hovered [ Play ("sound", audio.pageFlip3)]

screen essay3: #Preparing the imagemap
    imagemap:
        idle "essayClosed.png"
        hover "essayClosedHover.png"

        hotspot (0, 0, 600, 810) clicked Jump("essay3Opens") hovered [ Play ("sound", audio.pageFlip3)]

screen essay4: #Preparing the imagemap
    imagemap:
        idle "essayClosed.png"
        hover "essayClosedHover.png"

        hotspot (0, 0, 600, 810) clicked Jump("essay4Opens") hovered [ Play ("sound", audio.pageFlip3)]

screen essay5: #Preparing the imagemap
    imagemap:
        idle "essayClosed.png"
        hover "essayClosedHover.png"

        hotspot (0, 0, 600, 810) clicked Jump("essay5Opens") hovered [ Play ("sound", audio.pageFlip3)]

screen essay6: #Preparing the imagemap
    imagemap:
        idle "essayClosed.png"
        hover "essayClosedHover.png"

        hotspot (0, 0, 600, 810) clicked Jump("essay6Opens") hovered [ Play ("sound", audio.pageFlip3)]

## Top Ten Creepiest Books ####

screen creepiestBooks: #Preparing the imagemap
    imagemap:
        idle "creepiestClosed.png"
        hover "creepiestClosedHover.png"

        hotspot (0, 0, 600, 810) clicked Jump("creepiestOpens") hovered [ Play ("sound", audio.pageFlip3)]

screen creepiestBooksText:
    zorder 101
    #vbox:
    #    xalign 0.5
    #    ypos 335
    frame:
        #background Frame("creepiestOpen2.png", 5, 5,)
        has hbox:
            spacing 5
            box_wrap True
            xpos 317
            ypos 400
            xalign 0.5
            yalign 0.5
            xsize 360
            ysize 300
            transform:
                rotate 3.5
                text birthdayNote

## Scrap of information about Gilgamesh ####
screen gilgamesh: #Preparing the imagemap
    imagemap:
        idle "gilgameshClosed.png"
        hover "gilgameshClosedHover.png"

        hotspot (0, 0, 600, 810) clicked Jump("gilgameshOpens") hovered [ Play ("sound", audio.pageFlip3)]

screen gilgameshText:
    zorder 101
    #vbox:
    #    xalign 0.5
    #    ypos 335
    frame:
        #background Frame("creepiestOpen2.png", 5, 5,)
        has hbox:
            spacing 5
            box_wrap True
            xpos 280
            ypos 750
            xalign 0.5
            yalign 0.5
            xsize 530
            ysize 300
            transform:
                rotate 2.0
                text gilText size 16 font "fonts/segoesc.ttf" color "#45413c" textalign 0.1 #alpha "0.6"
                alpha 0.9

## Secret Gilgamesh Path ####

screen gilPath: #Preparing the imagemap
    imagemap:
        idle "gilgameshPathClosed.png"
        hover "gilgameshPathClosedHover.png"

        hotspot (0, 0, 600, 900) clicked Jump("gilgameshPathOpens") hovered [ Play ("sound", audio.pageFlip3)]

screen gilPathOpen: #Preparing the imagemap
    imagemap:
        idle "gilgameshPathOpen.png"
        hover "gilgameshPathOpenHover.png"

        hotspot (0, 0, 600, 900) clicked Jump("gilgameshStory") hovered [ Play ("audio", audio.pencil)]


## Contents page ####

screen contents():
    #add "/images/contents.png"
    #add "images/contents_note.png" #onlayer 101

    default screenvar = False
    imagemap:
        #ground "contents_note.png"
        #show image "contents_note.png"
        auto "images/contents_%s.png"

        #idle "c_name_idle.png"
        #hover "c_name_hover.png"
        #selected_idle "c_name_hover.png"

        #Click the text box to enter text
        #hotspot (195,424,207,28) action SetScreenVariable("screenvar",True)
        #define gui.text_font = "fonts/ShoppingScript.ttf"
            #imagebutton auto "gui/mm_quit_%s.png" xpos 27 ypos 485 focus_mask True action Play("sound", "audio/page-flip.mp3"), Quit(confirm=not main_menu) hovered [ Play("sound", "audio/pencil.wav") ]

        input default persistent.povname pos(215,410) length(19) color((25, 16, 0, 100)) font("fonts/journal.ttf") size(35) changed name_func

        #She / Her pronoun button
        hotspot (200,452,55,28) hovered [ Play("sound", "audio/pencil.wav") ] action [Play("sound", "audio/page-flip.mp3"),Hide("text_input_screen"), SetVariable("persistent.nameSet", "True"),SetVariable("persistent.he", "she"), SetVariable("persistent.He", "She"), SetVariable("persistent.his", "her"), SetVariable("persistent.His", "Her"), SetVariable("persistent.him", "her"), SetVariable("persistent.Him", "Her"), SetVariable("persistent.Hes", "She's"), SetVariable("persistent.hes", "she's"), Jump("splashscreen2")]

        #He / Him pronoun button
        hotspot (272,454,53,36) hovered [ Play("sound", "audio/pencil.wav") ] action [Play("sound", "audio/page-flip.mp3"),Hide("text_input_screen"),SetVariable("persistent.nameSet", "True"),SetVariable("persistent.he", "he"),SetVariable("persistent.He", "He"),SetVariable("persistent.his", "his"),SetVariable("persistent.His", "His"),SetVariable("persistent.him", "him"),SetVariable("persistent.Him", "Him"),SetVariable("persistent.Hes", "He's"),SetVariable("persistent.hes", "he's"),Jump("splashscreen2")]

        #They / Them pronoun button
        hotspot (338,453,64,38) hovered [ Play("sound", "audio/pencil.wav") ] action [Play("sound", "audio/page-flip.mp3"),Hide("text_input_screen"),SetVariable("persistent.nameSet", "True"),SetVariable("persistent.he", "they"),SetVariable("persistent.He", "They"),SetVariable("persistent.his", "their"),SetVariable("persistent.His", "Their"),SetVariable("persistent.him", "them"),SetVariable("persistent.Him", "Them"),SetVariable("persistent.Hes", "They are"),SetVariable("persistent.hes", "they are"),Jump("splashscreen2")]

        #add "images/contents_note.png"

        #if screenvar == True:
        #persistent.nameSet = True:
        #else:
            #text "{color=(25, 16, 0, 100)}{size=30}{font=journal.ttf}[persistent.povname]{/font}{/size}{/color}" #at #(195,416) #length(20) color((25, 16, 0, 100)) font("fonts/journal.ttf") size(30)
            #povname = renpy.input("", length=32)
            #



## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

# screen save():
#
#     tag menu
#
#     use file_slots(_("Save"))


# screen load():
#
#     tag menu
#
#     use file_slots(_("Load"))


# screen file_slots(title):
#
#     #Background image
#     add "/gui/save_menu.png"
#
#     default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
#
#     use game_menu(title):
#
#         fixed:
#
#             ## This ensures the input will get the enter event before any of the
#             ## buttons do.
#             order_reverse True
#
#             ## The page name, which can be edited by clicking on a button.
#             button:
#                 style "page_label"
#                 #TK: Change? Maybe it shouldn't be possible to edit the page name?
#                 key_events True
#                 xalign 0.5
#                 action page_name_value.Toggle()
#
#                 input:
#                     style "page_label_text"
#                     value page_name_value
#
#             ## The grid of file slots.
#             grid gui.file_slot_cols gui.file_slot_rows:
#                 #style_prefix "page"
#                 style_prefix "slot"
#                 xalign 0#0.5
#                 xpos 40
#                 yalign 0 #0.5
#                 ypos 218
#
#                 spacing gui.slot_spacing
#
#                 for i in range(gui.file_slot_cols * gui.file_slot_rows):
#
#                     $ slot = i + 1
#
#                     button:
#
#                         action [FileAction(slot), Play("sound", "audio/pencil-2.mp3")]
#
#                         has vbox
#
#                         #add FileScreenshot(slot) xalign 0.5
#
#                         text FileTime(slot, format=_("[persistent.povname]"), empty=_("")): #%A,
#                         #text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("")):
#                             style "slot_time_text"
#                             font "fonts/journal.ttf"#gui.choice_button_text_font
#                             ypos 10
#                             xpos 60
#                             size 20
#
#                         text FileTime(slot, format=_("{#file_time}%b %d. %H:%M"), empty=_("")): #%A,
#                         #text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("")):
#                             style "slot_time_text"
#                             xpos 237
#                             ypos -15
#                             font "fonts/journal.ttf"#gui.choice_button_text_font
#                             size 20
#
#                         #text FileSaveName(slot):
#                             #style "slot_name_text"
#
#                         key "save_delete" action FileDelete(slot)
#
#             ## Buttons to access other pages.
#             hbox:
#                 style_prefix "page"
#
#                 xalign 0.5
#                 yalign 1.0
#
#                 spacing gui.page_spacing
#
#                 textbutton _("<") action FilePagePrevious()
#
#                 if config.has_autosave:
#                     textbutton _("{#auto_page}A") action FilePage("auto")
#
#                 if config.has_quicksave:
#                     textbutton _("{#quick_page}Q") action FilePage("quick")
#
#                 ## range(1, 10) gives the numbers from 1 to 9.
#                 for page in range(1, 10):
#                     textbutton "[page]" action FilePage(page)
#
#                 textbutton _(">") action FilePageNext()
#
#
# style page_label is gui_label
# style page_label_text is gui_label_text
# style page_button is gui_button
# style page_button_text is gui_button_text
#
# style slot_button is gui_button
# style slot_button_text is gui_button_text
# style slot_time_text is slot_button_text
# style slot_name_text is slot_button_text
#
#
#
# style page_label:
#     xpadding 24
#     ypadding 2
#
# style page_label_text:
#     text_align 0.5
#     layout "subtitle"
#     hover_color gui.hover_color
#
# style page_button:
#     properties gui.button_properties("page_button")
#
# style page_button_text:
#     properties gui.button_text_properties("page_button")
#
# style slot_button:
#     properties gui.button_properties("slot_button")
#
# style slot_button_text:
#     properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    add "/images/bg page.png"

    #if persistent.vanished >=2:
    #$renpy.show_screen("essay6", _layer="screens", tag="note", _zorder=101)

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox xpos 30 ypos 160: #20:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                #vbox:
                #    style_prefix "radio"
                #    label _("Rollback Side")
                #    textbutton _("Disable") action Preference("rollback side", "disable")
                #    textbutton _("Left") action Preference("rollback side", "left")
                #    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))


                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Ambience Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                        #label _("Self-Voicing Volume")

                        #hbox:
                            #bar value Preference("self voicing volume drop")



                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
                vbox:
                    style_prefix "radio"
                    label _("Safe For Work Mode")
                    textbutton _("Off") action SetVariable("persistent.sfw", False)
                    textbutton _("On") action SetVariable("persistent.sfw", True)

                vbox:
                    #style_prefix "radio"
                    #label _("Change Name & Pronouns")
                    textbutton _("Change Name & Pronouns") action Play("sound", "audio/page-flip.mp3"), ShowMenu("contents")
                    #textbutton _("Off") action call screen contents
                    #SetVariable("persistent.sfw", False)
                    #call screen contents


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 1

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 106

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 165

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 5

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 211


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    #python:
    #    renpy.play("audio/page-flip.mp3")

    tag menu

    add "/images/bg page.png"

    if persistent.vanished >=1 and humbabaShowing:
        use humbaba1

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox xpos 15 ypos 100: #20::
            spacing 8

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 4

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 118
    right_padding 10

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "choice"#"confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            ypos 430
            xpos 300
            spacing 15

            label _(message):
                style "confirm_prompt"
                #textbutton i.caption action i.action activate_sound "audio/page-flip.mp3" hover_sound "audio/pencil.wav"

                xalign 0.5

            hbox:
                xalign 0.5
                spacing 47

                textbutton _("Yes") action yes_action activate_sound "audio/page-flip.mp3" hover_sound "audio/pencil.wav"
                textbutton _("No") action no_action activate_sound "audio/page-flip.mp3" hover_sound "audio/pencil.wav"

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5

    #font "fonts/Moms_typewriter.ttf"
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 3

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 211

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 160

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 188

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 282
