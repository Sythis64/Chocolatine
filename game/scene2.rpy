label scene2:
    z "On va se reposer ici."
    "ZZ entre dans le batiment attaqué par la corrosion."
    g "C'est dangereux, le batiment peur s'effondrer à n'importe quel moment !"
    z "C'est encore plus risqué de rester dehors avec ces robots."
    "ZZ appercoit quelqu'un au loin."
    $ oeil_bionique = False
    if oeil_bionique:
        "Il y a un enfant caché qui vous regarde."
        z "Viens, je ne vaispas te faire de mal"
        "L'enfant s'approche, timide."
        z "Il y a d'autres personnes ici ?"
        "Enfant" "Je... Qui êtes-vous ? Vous êtes un robot ?"
        z "Non, moi je detruis les robots.{p}Tu veux bien m'amener à ta famille ?"
        "L'enfant hésite, mais accepte."
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

    "{i}Quelques minutes plus tard.{i}"

    z "Gilbert ! Je n'ai rien trouv...{p=0.5}Qu'est-ce qui se passe !"

    "Gilbert tend son arme vers un groupe d'humains appeurés."

    z "Pourquoi tu les attaque ?"

    g "Je... Je... Pour rien, c'est bon."

    "ZZ regarde le groupe d'humains."

    z "Excusez-le..."
