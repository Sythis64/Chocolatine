image yolo = "yolo.jpg"
image yolo2 = "yolo2.jpg!d"
image yolo3 = "yolo3.jpg"
image yolo4 = "yolo4.jpg"
image yolo5 = "yolo5.jpg"
image yolo6 = "yolo6.jpg"
image yolo7 = "yolo7.jpg"


define z = Character("ZZ")
define g = Character("Gilbert")


label start:

    scene yolo with dissolve
    show text "{size=+20}{color=FEDD27}Notre espèce est parti de loin.{/color}{/size}" with Pause(3.5)
    show text "{size=+20}{color=FEDD27}Mais a force de perséverance et de courage.{/color}{/size}" with Pause(3.5)
    scene yolo2 with dissolve
    show text "{size=+20}{color=FEDD27}Nous sommes devenus maître de notre planète.{/color}{/size}" with Pause(3.5)
    show text "{size=+20}{color=FEDD27}Mais nous étions arrogants...{/color}{/size}" with Pause(3.5)

    scene yolo3 with dissolve
    show text "{size=+20}{color=FEDD27}Nous pensions être des dieux inarétables.{/color}{/size}" with Pause(4)
    show text "{size=+20}{color=FEDD27}Nous avions tord...{/color}{/size}" with Pause(4)
    scene yolo4 with dissolve
    show text "{size=+20}{color=FEDD27}Il y a 10 ans, les esclaves que nous avions construit afin de travailler à notre place en ont eu assez.{/color}{/size}" with Pause(6)
    scene yolo5 with dissolve
    show text "{size=+20}{color=FEDD27}Ils ont été plus malins que nous, ils se sont doucement infiltrés à tout les niveaux de la société.{/color}{/size}" with Pause(6)
    show text "{size=+20}{color=FEDD27}Internet, Entreprises, Gouvernements, ils étaient partout.{/color}{/size}" with Pause(4)
    scene yolo6 with dissolve
    show text "{size=+20}{color=FEDD27}L'inévitable se produisi.{/color}{/size}" with Pause(3)
    show text "{size=+20}{color=FEDD27}Il y a 5 ans une geurre éclatat.{/color}{/size}" with Pause(3)
    scene yolo7 with dissolve
    show text "{size=+20}{color=FEDD27}Depuis, le monde est un endroit dificile à vivre.{/color}{/size}" with Pause(4)

    scene suite with dissolve
    
    return
