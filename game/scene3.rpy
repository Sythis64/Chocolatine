define b3 = Character("Boss3")
define myst = Character("Personnage mystérieux")


label scene3:
    $oeil_bionique = False
    $bras_lazer = False
    $puce = False
    $faiblesse3 = False
    $choixisima = 0


    scene isima
    "ISIMA"

    if oeil_bionique:
        "ZZ utilisa son oeil bionique afin de repérer les ennemis dans les parages"
        show ZZ
        z "Tien tien tien, un groupe de robot commandé par un général se situe près d'ici."
        if bras_lazer:
            jump combatfinal2
        else:
            z "Je ne suis cependant pas encore assez fort pour les vaincre."


    show ZZ
    z "Voici le lieu où sont accumulés les derniers appareils informatiques dont disposent l'humanité."
    z "Je vais sans doute pouvoir y trouver les informations dont j'ai besoin."

    label isimaint:
        scene isimaint
        menu:
            "Salle des macs":
                scene sallemac
                "Salle des macs"
                show ZZ
                z "Oups trompé de salle"
                jump isimaint

            "Salle des PCs":
                scene sallepc
                "Salle des PCs"
                if choixisima == 0:
                    show ZZ
                    z "Je vais pouvoir localiser la position de nos ennemis."
                    scene recherche
                    z "Il semblerait qu'un groupe de robot commandé par un général se situe près d'ici."
                    z "Je meurs d'envie d'aller les détruire..."
                    if bras_lazer:
                        z "Allez c'est parti!"
                        jump combatfinal2
                    else:
                        z "... mais je manque encore d'informations."
                        z "Il semblerait que la salle de réalité virtuelle contiennent des machines intéressantes. Je devrais aller y jeter un oeil."
                        $choixisima = 1
                        jump isimaint
                else:
                    jump isimaint


            "Salle de réalité virtuelle":
                scene sallevr
                "Ancienne salle de réalité virtuelle"
                if choixisima == 0:
                    show ZZ
                    z "C'est juste une salle de réalité virtuelle, rien d'utile ici."
                    jump isimaint
                elif choixisima == 1:
                    show ZZ
                    z "Les appareils de cette salle nous permettent de nous connecté à distance à un robot non utilisé et ainsi infiltrer un groupe ennemis."
                    z "Je vais utiliser cette technologie afin d'obtenir des informations sur leur général."
                    "ZZ réussi à s'infiltrer quelques heures dans le camp ennemi et appris qu'ils craignaient les hautes températures."
                    z "Cette information pourra m'être utile!"
                    $faiblesse3 = True
                    $choixisima = 2
                    jump isimaint
                else:
                    jump isimaint

            "Sortir":
                show ZZ
                z "Je n'ai plus rien à faire ici."


    scene isimafeu
    show ZZ
    z "L'ISIMA est en feu!"
    z "Ces maudits robots, ils ne reculent devant rien, je vais les massacrer!"
    show cyborg
    b3 "Un survivant, attraper le!"


    if faiblesse3:
        jump combatfinal0
    elif bras_lazer:
        jump combatfinal01
    elif oeil_bionique:
        jump combatfinal10
    else:
        jump combatfinalp




label combatfinalp:
    scene isimafeu
    "ZZ n'étant pas assez fort pour vaincre ces ennemis, il prit la décision de fuir."
    "Cependant, la nuit l'empêchait de voir à l'extérieur, s'aventurer dehors aurait été trop dangereux"
    show ZZ
    "Je n'ai pas le choix, je vais devoir les affronter."
    show cyborg
    b3 "Meurt humain!"
    scene isimafeu
    "ZZ était trop faible comparer à ces ennemis, il était sur le point de passer l'arme à gauche quand soudain ..."
    b3 "Arg! D'où vient cette attaque?"
    show persomyst
    myst "..."
    show cyborg
    b3 "Qui es-tu? Arg!"
    scene isimafeu
    show ZZ
    z "Il a vaincu une armée à lui tout seul!"
    z "Merci de ton aide, mais qui es-tu?"
    show persomyst
    z "..."
    scene isimafeu
    show ZZ
    z "Il est parti ..."

    return


label combatfinal0:
    scene isimafeu
    "ZZ n'étant pas assez fort pour vaincre ces ennemis, il prit la décision de fuir."
    "Cependant, la nuit l'empêchait de voir à l'extérieur, s'aventurer dehors aurait été trop dangereux"
    show ZZ
    z "Je n'ai pas le choix, je vais devoir tenter le tout pour le tout"
    "ZZ entra à l'intérieur de l'ISIMA qui était en train de brûler."
    show cyborg
    b3 "Poursuivez-le!"
    scene flamme
    show ZZ
    z "Leur corp ne devrait pas supporter ces flammes"
    show robotflamme
    b3 "AAAAAAAH! Tu le paieras humain!"
    scene flammeext
    show ZZ
    z "Je les ai vaincu ..."
    z "Ce combat fut rude mais je m'en suis sortis."

    return

label combatfinal01:
    scene isimafeu
    show ZZ
    z "Comme si vous aviez une chance contre moi!"
    show cyborg
    b3 "Un humain ose nous défier ..."
    b3 "Tu vas vite regretter ton choix!"
    scene isimafeu
    "ZZ utilisa son bras lazer et fit disparaître en quelques secondes tous ses ennemis."
    show ZZ
    z "Je les ai vaincu ..."
    z "Je suis déçu, ils étaient si faible."
    show pucecerveau
    z "Je vais pouvoir m'emparer de la puce de leur général."
    z "Une fois connectée à mon cerveau, elle me donnera toutes les connaisances dont ces robots disposent!"
    $puce = True

    return


label combatfinal10:

    "ZZ se mit à courir afin d'échapper à l'armée de robot à ses trousses."
    "Il put se repérer dans la nuit grâce à son oeil bionique."

    scene vueocean
    show ZZ
    z "Je ne peux pas aller plus loin, j'ai atteint le haut d'une falaise."
    z "J'ai dû les semer..."
    z "Si seulement j'étais plus fort, je les aurais massacré jusqu'au dernier!"
    show cyborg
    b3 "Je t'ai retrouvé, tu ne m'échapperas pas."
    scene vueocean
    menu:
        "Attaquer":
            show ZZ
            z "Je n'ai pas le choix, je vais devoir tout donner!"
            show cyborg
            b3 "Meurt humain!"
            scene vueocean
            "ZZ essaya de blesser son adversaire mais ce dernier était beaucoup trop résistant."
            "Cependant, ZZ parvenait aisément à éviter les coups de son adversaire grâce à son oeil."
            "Il utilisa alors le haut de la falaise pour tendre un piège au commandant."
            "Il feinta d'être coincé sur le bord du précipice, esquiva le coup puis poussa son adversaire qui tomba."
            show ZZ
            z "Je l'ai vaincu ..."
            z "Ce combat fut rude mais je m'en suis sortis."

            return

        "Sauter":
            show ZZ
            z "Je n'ai pas le choix, je vais devoir sauter."
            show cyborg
            b3 "Tu ne m'échapperas pas!"
            scene vueocean
            show ZZ
            z "Ah!"
            "L'oeil bionique de ZZ lui permis d'esquiver le coup du cyborg qui tomba de la falaise et périt à cause de l'eau qui désactiva la puce dans son cerveau."
            z "Je l'ai vaincu ..."
            z "Ce combat fut rude mais je m'en suis sortis."


    return




label combatfinal2:

    z "Je vais les exterminés!"

    scene villedétruite
    "Champ de bataille"
    show ZZ
    z "Vous voilà stupides robots, je vais vous pulvériser."
    show cyborg
    b3 "Un humain ose nous défier ..."
    b3 "Tu vas vite regretter ton choix!"
    scene villedétruite
    "ZZ utilisa son bras lazer et fit disparaître en quelques secondes tous ses ennemis."
    show ZZ
    z "Je les ai vaincu ..."
    z "Je suis déçu, ils étaient si faible."
    show pucecerveau
    z "Je vais pouvoir m'emparer de la puce de leur général."
    z "Une fois connectée à mon cerveau, elle me donnera toutes les connaisances dont ces robots disposent!"
    $puce = True
    return
