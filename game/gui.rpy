﻿################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
#Game resolution
init python:
    gui.init(600, 850)



################################################################################
## GUI Configuration Variables
################################################################################


## Colors ######################################################################
##
## The colors of text in the interface.

## An accent color used throughout the interface to label and highlight text.
define gui.accent_color = u'#cc6600'

## The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = u'#808080'#u'#aaaaaa'

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define gui.idle_small_color = u'#888888'

## The color that is used for buttons and bars that are hovered.
define gui.hover_color =u'#FF5733' # u'#cc6600'

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define gui.selected_color = u'#555555'

## The color used for a text button when it cannot be selected.
define gui.insensitive_color = u'#aaaaaa7f'

## Colors used for the portions of bars that are not filled in. These are not
## used directly, but are used when re-generating bar image files.
define gui.muted_color = u'#e0a366'
define gui.hover_muted_color = u'#eac199'

## The colors used for dialogue and menu choice text.
define gui.text_color = u'#404040'
define gui.interface_text_color = u'#404040'

## Fonts and Font Sizes ########################################################

## The font used for in-game text.
define gui.text_font = "fonts/Book Antiqua.ttf"

## The font used for character names.
define gui.name_text_font = "fonts/OzsWizard-TinWoodman.ttf"

## The colour used for character names.
define gui.name_text_color = u'#404040'

## The font used for out-of-game text.
define gui.interface_text_font = "fonts/Book Antiqua.ttf"

## The size of normal dialogue text.
define gui.text_size = 21

## The size of character names.
define gui.name_text_size = 40

## The size of text in the game's user interface.
define gui.interface_text_size = 21

## The size of labels in the game's user interface.
define gui.label_text_size = 22

## The size of text on the notify screen.
define gui.notify_text_size = 18

## The size of the game's title.
define gui.title_text_size = 24


## Main and Game Menus #########################################################

## The images used for the main and game menus.
define gui.main_menu_background = "gui/main_menu.png"
define gui.main_menu_noContinue_background = "gui/main_menu2.png"
define gui.game_menu_background = "gui/game_menu.png"
# if persistent.vanished >= 4:
#     define gui.about_background = "gui/aboutEmpty.png"
# else:
#     define gui.about_background = "gui/about.png"

## Dialogue ####################################################################
##
## These variables control how dialogue is displayed on the screen one line at a
## time.

## The height of the textbox containing dialogue.
define gui.textbox_height = 410

## The placement of the textbox vertically on the screen. 0.0 is the top, 0.5 is
## center, and 1.0 is the bottom.
define gui.textbox_yalign = 0.0


## The placement of the speaking character's name, relative to the textbox.
## These can be a whole number of pixels from the left or top, or 0.5 to center.
define gui.name_xpos = -5
#TK: Double Check
define gui.name_ypos = -4#0

## The horizontal alignment of the character's name. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.name_xalign = 0.0

## The width, height, and borders of the box containing the character's name, or
## None to automatically size it.
define gui.namebox_width = None
define gui.namebox_height = None

## The borders of the box containing the character's name, in left, top, right,
## bottom order.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## If True, the background of the namebox will be tiled, if False, the
## background of the namebox will be scaled.
define gui.namebox_tile = False


## The placement of dialogue relative to the textbox. These can be a whole
## number of pixels relative to the left or top side of the textbox, or 0.5 to
## center.
define gui.dialogue_xpos = 50#110
define gui.dialogue_ypos = 480

## The maximum width of dialogue text, in pixels.
define gui.dialogue_width = 500#400

## The horizontal alignment of the dialogue text. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.dialogue_text_xalign = 0.0


## Buttons #####################################################################
##
## These variables, along with the image files in gui/button, control aspects of
## how buttons are displayed.

## The width and height of a button, in pixels. If None, Ren'Py computes a size.
define gui.button_width = None
define gui.button_height = None

## The borders on each side of the button, in left, top, right, bottom order.
define gui.button_borders = Borders(2, 2, 2, 2)

## If True, the background image will be tiled. If False, the background image
## will be linearly scaled.
define gui.button_tile = False

## The font used by the button.
define gui.button_text_font = gui.interface_text_font

## The size of the text used by the button.
define gui.button_text_size = gui.interface_text_size

## The color of button text in various states.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.button_text_xalign = 0.0


## These variables override settings for different kinds of buttons. Please see
## the gui documentation for the kinds of buttons available, and what each is
## used for.
##
## These customizations are used by the default interface:

define gui.radio_button_borders = Borders(9, 2, 2, 2)

define gui.check_button_borders = Borders(9, 2, 2, 2)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(5, 2, 5, 2)

define gui.quick_button_borders = Borders(20, 2, 5, 10)
define gui.quick_button_text_size = 16
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## You can also add your own customizations, by adding properly-named variables.
## For example, you can uncomment the following line to set the width of a
## navigation button.

# define gui.navigation_button_width = 250


## Choice Buttons ##############################################################
##
## Choice buttons are used in the in-game menus.

define gui.choice_button_width = None#371
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(47, 3, 42, 3)
define gui.choice_button_text_font = "fonts/book-antiqua-italic.ttf"#gui.text_font
define gui.choice_button_text_size = gui.text_size
#define gui.choice_button_text_yalign = 0
define gui.choice_button_text_xalign = 0#0.5
#define gui.choice_button_text_idle_color = "#cccccc"
#define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#aaaaaa7f"
#define gui.text_color = u'#aaaaaa7f'


## File Slot Buttons ###########################################################
##
## A file slot button is a special kind of button. It contains a thumbnail
## image, and text describing the contents of the save slot. A save slot uses
## image files in gui/button, like the other kinds of buttons.

## The save slot button.
define gui.slot_button_width = 375#130
define gui.slot_button_height = 35#97
define gui.slot_button_borders = Borders(5, 5, 5, 5)
define gui.slot_button_text_size = 17
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

#define gui.choice_button_text_font = "fonts/book-antiqua-italic.ttf"

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 0#120
define config.thumbnail_height = 0#68

## The number of columns and rows in the grid of save slots.
define gui.file_slot_cols = 1 #3
define gui.file_slot_rows = 7 #2


## Positioning and Spacing #####################################################
##
## These variables control the positioning and spacing of various user interface
## elements.

## The position of the left side of the navigation buttons, relative to the left
## side of the screen.
define gui.navigation_xpos = 19

## The position of the Return button
define gui.return_xpos = 40

## The vertical position of the skip indicator.
define gui.skip_ypos = 5

## The vertical position of the notify screen.
define gui.notify_ypos = 22

## The spacing between menu choices.
define gui.choice_spacing = 11

## Buttons in the navigation section of the main and game menus.
define gui.navigation_spacing = 2

## Controls the amount of spacing between preferences.
define gui.pref_spacing = 5

## Controls the amount of spacing between preference buttons.
define gui.pref_button_spacing = 0

## The spacing between file page buttons.
define gui.page_spacing = 0

## The spacing between file slots.
define gui.slot_spacing = -11#5

## The position of the main menu text.
define gui.main_menu_text_xalign = 1.0


## Frames ######################################################################
##
## These variables control the look of frames that can contain user interface
## components when an overlay or window is not present.

## Generic frames.
define gui.frame_borders = Borders(2, 2, 2, 2)

## The frame that is used as part of the confirm screen.
define gui.confirm_frame_borders = Borders(19, 19, 19, 19)

## The frame that is used as part of the skip screen.
define gui.skip_frame_borders = Borders(8, 3, 24, 3)

## The frame that is used as part of the notify screen.
define gui.notify_frame_borders = Borders(8, 3, 19, 3)

## Should frame backgrounds be tiled?
define gui.frame_tile = False


## Bars, Scrollbars, and Sliders ###############################################
##
## These control the look and size of bars, scrollbars, and sliders.
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

## The height of horizontal bars, scrollbars, and sliders. The width of vertical
## bars, scrollbars, and sliders.
define gui.bar_size = 12
define gui.scrollbar_size = 6
define gui.slider_size = 12

## True if bar images should be tiled. False if they should be linearly scaled.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Horizontal borders.
define gui.bar_borders = Borders(2, 2, 2, 2)
define gui.scrollbar_borders = Borders(2, 2, 2, 2)
define gui.slider_borders = Borders(2, 2, 2, 2)

## Vertical borders.
define gui.vbar_borders = Borders(2, 2, 2, 2)
define gui.vscrollbar_borders = Borders(2, 2, 2, 2)
define gui.vslider_borders = Borders(2, 2, 2, 2)

## What to do with unscrollable scrollbars in the gui. "hide" hides them, while
## None shows them.
define gui.unscrollable = "hide"


## History #####################################################################
##
## The history screen displays dialogue that the player has already dismissed.

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

## The height of a history screen entry, or None to make the height variable at
## the cost of performance.
define gui.history_height = None#66#  #

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.history_name_xpos = 73
define gui.history_name_ypos = 0
define gui.history_name_width = 73
define gui.history_name_xalign = 1.0

#The default position of the choice menu
define choice_menu_ypos = 700

## The position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 80
define gui.history_text_ypos = 1
define gui.history_text_width = 347
define gui.history_text_xalign = 0.0


## NVL-Mode ####################################################################
##
## The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

## The borders of the background of the NVL-mode background window.
define gui.nvl_borders = Borders(0, 5, 0, 10)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 6

## The height of an NVL-mode entry. Set this to None to have the entries
## dynamically adjust height.
define gui.nvl_height = 54

## The spacing between NVL-mode entries when gui.nvl_height is None, and between
## NVL-mode entries and an NVL-mode menu.
define gui.nvl_spacing = 5

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.nvl_name_xpos = 202
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 71
define gui.nvl_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 211
define gui.nvl_text_ypos = 4
define gui.nvl_text_width = 277
define gui.nvl_text_xalign = 0.0

## The position, width, and alignment of nvl_thought text (the text said by the
## nvl_narrator character.)
define gui.nvl_thought_xpos = 113
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 366
define gui.nvl_thought_xalign = 0.0

## The position of nvl menu_buttons.
define gui.nvl_button_xpos = 211
define gui.nvl_button_xalign = 0.0

## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Mobile devices
################################################################################

init python:

    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    if renpy.variant("touch"):

        gui.quick_button_borders = Borders(19, 7, 19, 0)

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    if renpy.variant("small"):

        ## Font sizes.
        gui.text_size = 15
        gui.name_text_size = 17
        gui.notify_text_size = 12
        gui.interface_text_size = 15
        gui.button_text_size = 15
        gui.label_text_size = 16

        ## Adjust the location of the textbox.
        gui.textbox_height = 113
        gui.name_xpos = 38
        gui.dialogue_xpos = 43
        gui.dialogue_width = 516

        ## Change the size and spacing of various things.
        gui.slider_size = 17

        gui.choice_button_width = 582
        gui.choice_button_text_size = 15

        gui.navigation_spacing = 10
        gui.pref_button_spacing = 5

        #Change for history width bug
        gui.history_height = 90#None#
        gui.history_text_width = 324

        gui.quick_button_text_size = 10

        ## File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-mode.
        gui.nvl_height = 80

        gui.nvl_name_width = 143
        gui.nvl_name_xpos = 153

        gui.nvl_text_width = 429
        gui.nvl_text_xpos = 162
        gui.nvl_text_ypos = 3

        gui.nvl_thought_width = 582
        gui.nvl_thought_xpos = 10

        gui.nvl_button_width = 582
        gui.nvl_button_xpos = 10
