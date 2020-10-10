define m = Character('Michellambda')
define g = Character('Gilbert')
define b1 = Character('Boss1')
image destroyed-city = "destroyed-city.jpg"
image black_screen = "black_screen.jpg"
image hangar = "hangar.jpg"
image porte-hangar = "porte-hangar.jpg"
image destroyed-andro = "destroyed-android.jpg"
image couloir = "couloir-hangar.jpg"
image boss1 = "robot_mechant.jpg"
image gilbert = "gilbert.jpg"
image zz = "zz.jpg"
image mi = "michellambda.jpg"

label scene1:
    show text "Des cris\nL'odeur de la poudre et du sang" with Dissolve(0.5)
    pause 3.0
    show text "La violence, partout" with Dissolve(0.5)
    pause 3.0
    show text "{color=ff0000}{size=55}Détruire... je dois détruire{/size}{/color}" with Dissolve(0.5)
    pause 3.0
    m "ZZ ! ZZ, tu m'entends ? Réveille-toi !" with Dissolve(0.5)
    scene destroyed-city with Dissolve(3)
    show m with Dissolve(1.5)
    "ZZ émerge d'un sommeil trop court pour être récupérateur"
    m "J'ai enfin trouvé !" with Dissolve(0.5)
    z "Quoi ? Une piste ?" with Dissolve(0.5)
    m "Mieux ! J'ai pu apercevoir l'entrée de leur centre de reconditionnement." with Dissolve(0.5)
    z "Bordel, enfin ! J'en ai marre de moisir dans cette planque croulante. Avec un peu de chance, y'aura de la bouffe là-bas !" with Dissolve(0.5)
    m "Rêve toujours, ces tas de feraille font un régime strict d'électricté ; mais libre à toi d'essayer." with Dissolve(0.5)
    z "On aurait vraiment dû prendre plus de provisions en partant..." with Dissolve(0.5)
    m "Concentre-toi un peu, il s'agit de ne pas se planter : c'est peut-être notre seule chance de mettre la main sur un haut-gradé." with Dissolve(0.5)
    z "T'as raison, je me vois mal attendre qu'il se blesse à nouveau pour passer à l'action." with Dissolve(0.5)
    m "Il ne fait pas encore complètement jour... on y va maintenant ou on attend encore un peu ?" with Dissolve(0.5)
    menu:
        "Pas de temps à perdre !":
            jump nuit

        "Attendons d'y voir plus clair":
            jump jour

label jour:
    z "Leur vision nocturne est bien meilleure que la notre, évitons de leur offrir une chance supplémentaire de nous repérer" with Dissolve(0.5)
    m "Bonne idée. Mais restons vigilants en attendant, ce n'est pas le moment de  faire une erreur." with Dissolve(0.5)
    scene black_screen with Dissolve(1.5)
    show text "Quelques heures plus tard..." with Dissolve(2.5)
    scene destroyed-city with Dissolve(0.5)
    m "Bon, on devrait y voir suffisament clair. On y va ?" with Dissolve(0.5)
    z "C'est parti, allons exploser ces boîtes de conserve !"

label nuit:
    m "Mort aux andros ! Yeah !" with Dissolve(0.5)
    scene black_screen with Dissolve(1.5)
    scene hangar with Dissolve(1.5)
    m "Tiens ? On dirait que c'est vide..." with Dissolve(0.5)
    z "C'est louche, reste derrière moi" with Dissolve(0.5)
    hide m with Dissolve(0.5)
    m "Là ! La porte ! Elle s'ouvre !" with Dissolve(0.5)
    scene porte-hangar with Dissolve(0.5)
    z "Mais c'est... Les andros... Ils sont tous en veille" with Dissolve(0.5)
    show mi with Dissolve(1.5)
    m "Peu importe." with Dissolve(0.5)
    scene black_screen with Dissolve(1.5)
    show text "{color=ff0000}{size=55}PAN ! PAN ! PAN !{/size}{/color}" with Dissolve(2.5)
    scene destroyed-andro with Dissolve(1.5)
    menu:
        "Il faut qu'on parte.":
            jump boss1

        "Pourquoi t'as fait ça ?":
            jump pourquoi

        "Saleté d'android.":
            jump andronul

label pourquoi:
    m "C'est ce truc et ses potes qui ont ruiné ma vie, et la tienne, s'il faut que je te le rappelle. Qu'est-ce qui te prend tout à coup ?" with Dissolve(0.5)
    z "..." with Dissolve(0.5)
    z "Rien, laisse tomber." with Dissolve(0.5)
    m "Allez, avance." with Dissolve(0.5)
    jump boss1

label andronul:
    m "Il a eu ce qu'il méritait." with Dissolve(0.5)
    z "Et bientôt, ils auront tous ce qu'ils méritent." with Dissolve(0.5)
    m "Bien dit."  with Dissolve(0.5)
    z "Allez, on enchaîne" with Dissolve(0.5)
    jump boss1

label boss1:
    scene couloir with Dissolve(1.5)
    show mi with Dissolve(0.5)
    z "Notre cible ne devrait pas être très loin. S'il est vraiment blessé, c'est pas étonnant qu'il se planque." with Dissolve(0.5)
    m "Ce couloir devient vraiment sombre... c'est loin d'être le meilleur endroit pour nous battre" with Dissolve(0.5)
    menu :
        "Non, reste derrière moi":
            m "Je sais me défendre, tu me prends pour qui ?" with Dissolve(0.5)
            z "Ne discute pas, je reste devant."  with Dissolve(0.5)
            jump boss1fight

        "Si ça peut te faire plaisir":
            z "Un jour, ça finira par te retomber dessus" with Dissolve(0.5)
            m "Ferme-la, pour une fois." with Dissolve(0.5)
            jump dilemme

label dilemme:
    show text "Un bruit survient, mais Michellambda ne l'entend pas" with Dissolve(2)
    menu:
        "Eh ! Y'a un truc derrière !":
            m "Qu'est-ce que... ?" with Dissolve(0.5)
            jump boss1fight

        "Se retourner":
            jump romance

label boss1fight:
    scene black_screen with Dissolve(0.5)
    show text "{color=0000ff}{size=55}KA-BOUUUUUM{/size}{/color}" with Dissolve(3)
    m "Ah... ah... ghh..." with Dissolve(0.5)
    hide mi
    z "MICHELLAMBDA ?!" with Dissolve(0.5)
    scene couloir-hangar  with Dissolve(0.5)
    show image boss1
    show text "{color=0000ff}{size=55}NOOOOOOOOOOOOOOOOON{/size}{/color}" with Dissolve(2)
    show text "ZZ fait feu au juger, fou de rage" with Dissolve(1)
    show text "Mais ça ne suffit pas, et il se fait percuter" with Dissolve(1)
    z "Ouch" with Dissolve(2)
    scene black_screen with Dissolve(1)
    show text "Devant ZZ se dresse l'android, immense et belliqueux, l'oeil brillant" with Dissolve(1)
    z "C'est la fin..." with Dissolve(0.5)
    z "Mais ? Que ?" with Dissolve(0.5)
    show image gilbert
    z "Gilbert ? C'est toi" with Dissolve(0.5)
    show text "L'inconnu envoie quelques rafales, avant d'empoigner la tête de l'android" with Dissolve(1)
    hide boss1
    show text "D'un coup de masse brutal, il lui éclate le crâne" with Dissolve(1)
    g "J'ai enfin eu cette saloperie..." with Dissolve(0.5)
    g "10 semaines que je traque cette enflure, j'ai enfin réussi à l'avoir" with Dissolve(0.5)
    z "Merci, tu m'as sauvé" with Dissolve(0.5)
    g "La prochaine fois, ce sera différent : tiens, voilà son oeil" with Dissolve(0.5)
    g "Cet objet bionique devrait te permettre d'augmenter tes capacités de combat, notamment en milieu obscure." with Dissolve(0.5)
    z "Merci, sincèrement." with Dissolve(0.5)
    z "Au fait, je recherche un android géant. Avec celui que tu as tué, il fait parti de ceux qui m'ont contrôlé et fait tuer ma famille." with Dissolve(0.5)
    z "Je suis prêt à tout pour me venger." with Dissolve(0.5)
    hide gilbert
    show text "Et ainsi, ils partirent à la chasse des autres androids." with Dissolve(5)
    jump scene2

label romance:
    return
