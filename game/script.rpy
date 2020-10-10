﻿image yolo = "yolo.jpg"
image yolo2 = "yolo2.jpg!d"
image yolo3 = "yolo3.png"
image yolo4 = "yolo4.png"
image yolo5 = "yolo5.png"
image yolo6 = "yolo6.jpg"
image yolo7 = "yolo7.jpg"
image yolo8 = "yolo8.png"
image yolo9 = "yolo9.png"
image yolo10 = "yolo10.png"
image yolo11 = "black_screen.jpg"
image finnormal = "yolo444.jpeg"
image finrobot = "yolo44.jpeg"

define z = Character("ZZ")

define g = Character("Gilbert")

label start:

    scene yolo with dissolve
    show text "{size=+20}{color=FEDD27}Notre espèce est partie de loin.{/color}{/size}" with Pause(3.5)
    show text "{size=+20}{color=FEDD27}Mais à force de perséverance et de courage...{/color}{/size}" with Pause(3.5)
    scene yolo2 with dissolve
    show text "{size=+20}{color=FEDD27}Nous sommes devenus maîtres de notre planète.{/color}{/size}" with Pause(3.5)
    show text "{size=+20}{color=FEDD27}Cependant... Nous étions arrogants.{/color}{/size}" with Pause(3.5)

    scene yolo3 with dissolve
    show text "{size=+20}{color=FEDD27}Nous pensions être des dieux inarrêtables.{/color}{/size}" with Pause(4)
    show text "{size=+20}{color=FEDD27}Nous avions tort...{/color}{/size}" with Pause(4)
    scene yolo4 with dissolve
    show text "{size=+20}{color=FEDD27}Il y a 10 ans, les esclaves que nous avions construits afin de travailler à notre place en ont eu assez.{/color}{/size}" with Pause(6)
    
    scene yolo5 with dissolve
    show text "{size=+20}{color=FEDD27}Ils ont été plus malins que nous, ils se sont doucement infiltrés à tous les niveaux de la société.{/color}{/size}" with Pause(6)
    show text "{size=+20}{color=FEDD27}Internet, entreprises, gouvernements, ils étaient partout.{/color}{/size}" with Pause(4)
    scene yolo6 with dissolve
    show text "{size=+20}{color=FEDD27}L'inévitable se produisit.{/color}{/size}" with Pause(3)
    show text "{size=+20}{color=FEDD27}Il y a 5 ans une guerre éclatat.{/color}{/size}" with Pause(3)
    
    scene yolo7 with dissolve
    show text "{size=+20}{color=FEDD27}Depuis, le monde est un endroit difficile à vivre.{/color}{/size}" with Pause(4)
    scene yolo8 with dissolve
    show text "{size=+20}{color=FEDD27}Au début de cette guerre, notre héros ZZ fut capturé par les robots.{/color}{/size}"with Pause(4.5)
    show text "{size=+20}{color=FEDD27}Il a été utilisé comme cobaye, et transformé en cyborg.{/color}{/size}"with Pause(4.5)
    
    scene yolo9 with dissolve
    show text "{size=+20}{color=FEDD27}Contrôlé par les robots, il commit des atrocités.{/color}{/size}"with Pause(4.5)
    show text "{size=+20}{color=FEDD27}Il a même découpé en tout petits morceaux sa propre famille.{/color}{/size}"with Pause(4.5)
    scene yolo10 with dissolve
    show text "{size=+20}{color=FEDD27}Un jour, lors d'une grande bataille, les humains acculés utilisèrent une EMP.{/color}{/size}"with Pause(4.5)
    show text "{size=+20}{color=FEDD27}Tous les robots tombèrent ce jour là.{/color}{/size}"with Pause(4.5)
    show text "{size=+20}{color=FEDD27}Mais ZZ, lui, se retrouva libéré de l'emprise des robots.{/color}{/size}"with Pause(4.5)

    scene yolo11 with dissolve
    show text "{size=+20}{color=FEDD27}L'avenir de l'humanité est entre ses mains. Va-t-il faire les bons choix?{/color}{/size}"with Pause(5)

    jump scene1

    return

label fin:

    scene finnormal
    show z

    show text "{size=+20}{color=FEDD27}Vous avez réussi a surmonter toutes ces épreuves{/color}{/size}" with Pause(4.5)  
    show text "{size=+20}{color=FEDD27}Vous ne sentez plus rien, il y a un vide en vous{/color}{/size}" with Pause(4.5)
    show text "{size=+20}{color=FEDD27}Toutes les modifications que votre corps ont subis commencent a se faire sentir{/color}{/size}" with Pause(5)
    show text "{size=+20}{color=FEDD27}Vous sentez que vous commencez à perdre votre humanité{/color}{/size}" with Pause(4.5)
    show text "{size=+20}{color=FEDD27}Vous vous demandez si vous serez capable de résister longtemps{/color}{/size}" with Pause(4.5)
    show text "{size=+20}{color=FEDD27}Vous êtes pret d'une falaise, que faire ?" with Pause(4.5)

    menu:
        "Sauter de la falaise":
            hide z
            show text "{size=+20}{color=FEDD27}Vous avez fait le sacrifice ultime afin de protéger l'humanité{/color}{/size}" with Pause(4.5)
            show text "{size=+20}{color=FEDD27}Etait ce nécessaire ?{/color}{/size}" with Pause(4.5)
            show text "{size=+90}{color=000000}FIN{/color}{/size}" with Pause(4.5)
            return
        "Rentrer au camps":
            jump finrobot
    
label finrobot:

    scene finrobot

    show text "{size=+20}{color=FEDD27}Vous avez fini par succomber{/color}{/size}" with Pause(4.5)  
    show text "{size=+20}{color=FEDD27}Vous ne sentez plus rien, rien du tout{/color}{/size}" with Pause(4.5)
    show text "{size=+20}{color=FEDD27}Vous doutez de la nécesitté de garder les humains en vie{/color}{/size}" with Pause(5)
    show text "{size=+20}{color=FEDD27}Vous vous retrouvez a tuer des humains{/color}{/size}" with Pause(4.5)
    show text "{size=+20}{color=FEDD27}Avec vos capacités l'humanité se fait rapidement détruire{/color}{/size}" with Pause(4.5)
    show text "{size=+90}{color=000000}FIN{/color}{/size}" with Pause(4.5)
    return