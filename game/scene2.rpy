image abandonne1 = "abandonne1.jpg"
image abandonne2 = "abandonne2.jpg"
image abandonne3 = "abandonne3.jpg"
image abandonne4 = "abandonne4.jpg"
image abandonne4a = "abandonne4.1.jpg"
image black_screen = "black_screen.jpg"
image objection = "objection.jpg"
image abandonne5 = "abandonne5.jpg"
image arene_pokemon = "arene_pokemon.jpg"

label scene2:
    scene abandonne4
    z "On va se reposer ici."
    "ZZ entre dans un batiment attaqué par la corrosion."
    scene abandonne4a with Dissolve(1.5)
    pause(0.5)
    scene abandonne1 with Dissolve(1.5)
    pause(0.5)
    g "C'est dangereux, le batiment peur s'effondrer à n'importe quel moment !"
    z "C'est encore plus risqué de rester dehors avec ces robots."
    "ZZ appercoit quelqu'un au loin."
    if oeil_bionique:
        "Il y a un enfant caché qui vous regarde."
        z "Viens, je ne vais pas te faire de mal."
        "L'enfant s'approche, timide."
        z "Il y a d'autres personnes ici ?"
        "Enfant" "Je... Qui êtes-vous ? Vous êtes un robot ?"
        z "Non, moi je detruis les robots.{p}Tu veux bien m'amener à ta famille ?"
        "L'enfant hésite, mais accepte."
        scene abandonne3 with Dissolve(1.0)
        jump Rencontre_humains

    else:
        z "Qui êtes-vous ?"
        "Aucune réponse"
        z "{cps=20}VENEZ ICI {p=0.3}TOUT DE SUITE !{/cps}"
        "Un enfant s'enfuit en pleurant."
        menu:
            "Le suivre":
                z "Reviens ici !"
                "ZZ s'élance à sa poursuite."

            "Continuer d'explorer":
                z "Il y a des gens qui vivent ici ?"
                "ZZ explore le batiment."

    g "Va chercher par la droite, je vais voir sur la gauche."

    scene black_screen with Dissolve(1.0)

    "{i}Quelques minutes plus tard.{i}"

    scene abandonne3 with Dissolve(1.0)

    z "Gilbert ! Je n'ai rien trouv...{p=1} Qu'est-ce qui se passe !"

    "Gilbert tend son arme vers un groupe d'humains appeurés."

    z "Pourquoi tu les attaque ?"

    g "Je... Je... Pour rien, c'est bon."

    "ZZ regarde le groupe d'humains."

    z "Excusez-le..."

    jump Rencontre_humains

label Rencontre_humains:

    z "Vous avez l'air perdu."

    "Femme" "Vous êtes un robot, ou un humain ?"

    z "Vous me comparer avec ces tas de ferraille !? Je suis un humain, un vrai !"
    z "Ils ont tué ma famille, il m'ont enrollé de force, j'ai tout perdu à cause d'eux.{p}JAMAIS je ne leur pardonnerait !"

    "Femme" "Pardon, nous... nous en avons assez de combattre, nous voulons juste que les combats s'arretent."

    menu:
        "{i}S'énerver{/i}":
            z "{b}Tous{/b} les robots doivent mourir !{p}C'est juste de la vermine qui doit disparaitre !"
            z "Si tu n'est pas {b}contre eux{/b}, tu es avec{b} avec eux{/b}"
            "Femme" "Pardon, pardon... Pitié..."

        "{i}Acquiescer{/i}":
            z "Vous avez raison, cette guerre n'a que trop duré..."
            z "C'est pourquoi nous devons y mettre un terme, maintenant !"

    "Enfant" "Vous allez battre le grand robot ?"

    z "De quoi parles-tu ? Un grand robot ?"

    "Femme" "Il nous empeche de sortir d'ici."
    "Femme" "Cela fait des jours qu'on est coincé dans cet endroit."
    "Femme" "Le dernier qui a essayé s'est fait... {p=1}Pardon."
    g "Nous devons tous y aller ! Certains tomberont, mais les autres réussiront à se debarraser de ce robot !"
    "Femme" "C'est impossible, ils nous attendent. dès qu'on sortira, on se fera massacrer !"
    g "N'importe quoi ! Nous avons avec nous ZZ !"
    g "C'est un humain avec un corps robot ! Rien ne peut lui résister !"
    "Femme" "Nous allons tous y passer ! C'est un piege !"
    g "Moi, je suis sûr qu'on peut y arriver, mais il faut que vous soyez tous avec nous !"
    "Femme" "Ils vous ont laissé entrer ici. Si on sort, personne ne survivra."
    "Enfant" "Maman j'ai peur !"

    menu:
        "Il faut y aller. Ce n'est pas en restant ici qu'on va s'echapper.":
            jump plan_G


        "Il faut eviter le massacre à tout prix":
            jump choise1


        "Gilbert, tu veux nous envoyer à la mort !":
            jump choise2


label choise1:
    z "Non, Gilbert. Il faut que tout le monde survive."
    z "On trouvera un moyen"
    "Femme" "En fait, je crois savoir comment on peut s'échapper, mais..."
    z "Mais ?"
    "Femme" "C'est vraiment dangereux, celui qui ira a peu de chance de reussir..."
    menu:
        "{i}Faire le plan de Gilbert{/i}":
            z "Il faut y aller. Ce n'est pas en restant ici qu'on va s'echapper."
            jump plan_G

        "{i}Faire le plan de la femme{/i}":
            jump plan_F

label choise2:
    g "Mais non, c'est le seul moyen de s'echapper."
    "Femme" "Jamais on pourra battre ce robot !"
    g "ZZ ! Tu n'as plus confiance en moi ?"
    menu:
        "{i}Ecouter Gilbert{/i}":
            z "Il faut y aller. Ce n'est pas en restant ici qu'on va s'echapper."
            jump plan_G

        "{i}Ecouter la femme{/i}":
            "Femme" "Ce Gilbert ne m'inspire vraiment pas confiance"
            menu:
                "J'écoute votre plan, mais Gilbert est mon ami, il a ma confiance":
                    "Femme" "D'accord, mais qu'il ne s'approche pas de moi"
                    jump plan_F


                "Gilbert ne vous aime pas beaucoup non plus...":
                    "Je n'aime pas les conflits."
                    menu:
                        "Tuer la femme":
                            z "Voila une bonne chose de faite !"
                            jump plan_G

                        "Tuer Gilbert":
                            jump trahison

label plan_G:
    z "Mes frères ! Il nous faut fuir d'ici ! Si nous restons, nous mourrerons tous. Courrons tous affronter ce robot."
    z "Certains y laisseront la vie, mais leurs actes héroïques permettront aux autres de survivre !"
    z "Soyez avec moi, mes frères."
    "Les hommes et les femmes se lèvent les uns après les autres, le regard rempli de confiance."
    "Femme" "Non ! Non ! Il ne faut pas y aller !"
    jump combat_boss2


label plan_F:
    "Femme" "Merci, suivez moi, je vais vous montrer."
    jump hacker_boss2


label trahison:
    g "Mais pourquoi ?"
    z "Tu veux envoyé à la mort des humains !{p}Notre but est de detruire les robots."
    g "Mais, nous sommes amis..."
    scene objection
    pause(1.5)
    scene abandonne3
    z "Tu pensais que je ne l'avais pas remarquer !{p=2.0} Tu voulais tous nous tuer !"
    z "En réalité, j'avais tout prévu DEPUIS LE DEBUT !"
    z "En effet, j'avais compris ta trahison, car en fait TU EST DANS LE CAMPS DES ROBOTS !"
    "Femme" "Comment ? Comment avez vous su ?"
    z "J'avais remarqué que tu essayais de nous envoyer DANS UN GUETTE-APENT !"
    g "Bravo, mais as-tu prévu que j'allais prévoir que tu allais prévoir que nous prévoyons la prévision !"
    z "Et oui ! Parce qu'en fait je suis la réincarnation de Sherlock Holmes 300 ans dans LE FUTUR !"
    g "Oh mon dieu ! Mais c'est impossible !"
    z "Bien sur que si ! Parce que cette fin doit être finie en 10 min, le dev a plus le temps de faire un scénario crédible !"
    z "C'est pourquoi, avec mon bras gatlling en scénarium, je viens me brancher à l'interieur de ta tête !"
    z "Car je savais aussi que tu étais un humain controlé par les robots depuis le début !"
    z "Voilà pourquoi je peux me connecter à ton cerveau ! ET AINSI PIRATER LE TERMINAL !"
    z "Et voilà ! J'ai pirater le terminal des robots, et je les detruits tous !"
    z "L'humanité à gagnée !"
    return


label combat_boss2:

    scene abandonne5 with Dissolve(0.3)

    z "COUREZ ! VITE !"
    "Le groupe d'humains se fait désintégré par un robot menaçant."
    z "Tu les as tous tuer !"
    "Robot menaçant" "AH-AH-AH,-JE-SUIS-MALEFIQUE"
    g "Espèce de monstre !"
    "Robot menaçant" "AH-AH-AH,-JE-SUIS-UN-MONSTRE"
    g "Je vais te détruire !"
    "Robot menaçant" "C'EST-PARTI-POUR-UN-BLIND-TEST-DES-ANNEES-80-!"
    g "Attend quoi ?"

    scene arene_pokemon with Dissolve(0.5)

    pause(1.5)

    "On a plus le temps, déso"
    "Alors, bravo, vous avez gagné votre combat ! Et vous gagné un bras bionique lazer !"
    $ bras_lazer = True


label hacker_boss2:

    "Femme" "Venez, c'est par là"
    scene abandonne2 with Dissolve(1.0)
    pause(1.0)
    scene abandonne5 with Dissolve(0.5)

    "Femme" "C'est ici. Le robot se recharge sur ce terminal."
    "Femme" "Il faut le pirater pour atteindre le point faible du robot"
    z "Je vais le faire"
    menu:
        "Piraterle terminal":
            "C'était compliquer ?"
            z "Non, pas vraiment..."
            "Normal, le dev avait plus le temps de programmer un truc..."
            "Bon...{p} Et sinon, sa va toi ?"
            "Alors, tu veux la suite ?"
            "Il va falloir être plus gentil que sa..."
            "Prends bien le temps de lire tous les dialgues"
            "Ah ouais ? Tu me lis plus ?"
            "{cps=30}Je peux écrire lentement, comme sa, là c'est enervant, hein ?{/p}"
            "Bon, aller, salut a +"
            "ZZ continue son histoire"
            z "Ok, j'ai pirater le terminal"
            "Femme" "Parfait ! Maintenant le robot ne peux plus nous faire de mal !"
            "Le robot se reveille alors"
            "Robot menaçant" "QUI-ETES-VOUS-?-JE-VAIS-VOUS-DETRUIRE-!"
            "Le robot menaçant s'effondre"
            "Robot menaçant" "QU'EST-CE-QUE-VOUS-M'AVEZ-FAIT-?"
            z "Je ne te detruit pas, je ne prend pas tes pièces, mais laisse nous partir"
            "ZZ et tous les humains s'enfuient en courant"
            "Femme" "Merci ! Merci beaucoup ! Grace à vous, on va pouvoir s'echapper de cet enfer"
            z "Partez vite, avant que d'autres robots n'arrivent !"
            jump scene3


        "Ne rien faire":
            "On ne peut pas avancer si vous ne faites rien..."
            "Revenez en arrière avec la touche {i}retour{/i} parce que le dev avait la flemme de faire une boucle."
            pause(60.0)
            "c bien, vous êtes encore là, vous avez vraiment rien a faire..."
            jump fin_de_merde

label fin_de_merde

    "Bravo, vous avez gagné..."
    "Non je rigole, recommencez depuis le debut"
    jump start
