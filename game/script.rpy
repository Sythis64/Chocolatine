# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image yolo = "yolo.jpg"
image yolo2 = "yolo2.jpg!d"
image yolo3 = "yolo3.jpg"

define z = Character("ZZ")

define g = Character("Gilbert")



# The game starts here.

label start:

    scene yolo with dissolve
    show text "Notre espèce est parti de loin." with Pause(3.5)
    show text "Mais a force de perséverance et de courage." with Pause(3.5)
    scene yolo2 with dissolve
    show text "Nous sommes devenus maître de notre planète." with Pause(3.5)
    show text "Mais nous étions arrogants..." with Pause(3.5)

    scene yolo3 with dissolve
    show text "Nous pensions être des dieux inarétables, nous avions tord." with Pause(3.5)
    scene yolo4 with dissolve
    show text "Il y a 10 ans, les esclaves que nous avions construit afin de travailler à notre place en ont eu assez." with Pause(5)
    scene yolo5 with dissolve
    show text "Ils ont été plus malins que nous, ils se sont doucement infiltrés à tout les niveaux de la société." with Pause(5)

    scene yolo6 with dissolve
    show text "Internet, Entreprises, Gouvernements, ils étaient partout." with Pause(3.5)
    scene yolo7 with dissolve
    show text "L'inévitable se produit, il y a 5 ans une geurre éclatat." with Pause(3.5)
    scene yolo8 with dissolve
    show text "Depuis, le monde est un endroit dificile à vivre." with Pause(3.5)

    scene suite with dissolve
    show ZZ happy

    # These display lines of dialogue.

<<<<<<< HEAD

    z "You've created a new Ren'Py game."

    z "Once you add a story, pictures, and music, you can release it to the world!"

    z "Test Nathan "


=======
    
    "Alors que la société" 
>>>>>>> 0bbeb95c2eb27e9ebe05a665e80ad850bf7940a3
    # This ends the game.



<<<<<<< HEAD
    z "Test Nathan "

    # This ends the game.

    jump scene2

    return
    z "test 1,2,1,2"
=======
    return
>>>>>>> 0bbeb95c2eb27e9ebe05a665e80ad850bf7940a3
