﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define z = Character("ZZ")

define g = Character("Gilbert")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

<<<<<<< HEAD
=======
    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.


    z "You've created a new Ren'Py game."

    z "Once you add a story, pictures, and music, you can release it to the world!"

    z "Test Nathan "

    # This ends the game.

    jump scene3
>>>>>>> 20a7fa654db26986327c893e9f02831689bbdf55

    return
