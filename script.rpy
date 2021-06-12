# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Miko")
define k = Character("Kit")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Welcome to the shrine, Kit"

    e "If pass the spirit test, you can join us as a messenger.."

    "Kit's ears perk up."

    show kit happy

    k "Excellent"
    # This ends the game.

    return
