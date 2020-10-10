define b3 = Character("Boss3")

label scene3:

    scene isima
    "ISIMA"
    show ZZ
    z "Voici le lieu où est accumulé les derniers appareils informatiques dont disposent l'humanité."
    z "Je vais sans doute pouvoir y trouver les informations dont j'ai besoin."


    scene sallemac
    "Salle des macs"
    show ZZ
    z "Oups trompé de salle"

    scene sallepc
    "Salle des PCs"
    show ZZ
    z "Je vais pouvoir localiser la position de nos ennemis."
    scene recherche
    z "Il semblerait qu'un groupe de robot commandé par un général se situe près d'ici."
    z "Je meurs d'envie d'aller les détruire mais je manque encore d'informations."

    scene sallevr
    "Ancienne salle de réalité virtuelle"
    show ZZ
    z "Les appareils de cette salle nous permettent de nous connecté à distance à un robot non utilisé et ainsi infiltrer un groupe ennemis."
    z "Je vais utiliser cette technologie afin d'obtenir des informations sur leur général."


    scene isimafeu
    show ZZ
    z "L'ISIMA est en feu!"
    z "Ces maudits robots, ils ne reculent devant rien, je vais les massacrer!"
    show cyborg
    b3 "Un survivant, attraper le!"

    "ZZ se mit à courir afin d'échapper à l'armée de robot à ses trousses."


    scene vueocean
    show ZZ
    z "Je ne peux pas aller plus loin, j'ai atteint la côte."
    z "J'ai du les semer..."
    z "Si seulement j'étais plus fort, je les aurais massacré jusqu'au dernier!"
    show cyborg
    b3 "Je t'ai retrouvé, tu ne m'échapperas pas."
    scene vueocean
    show ZZ
    z "Je l'ai vaincu ..."
    z "Ce combat fut rude mais je m'en suis sortis."
    show pucecerveau
    z "Je vais pouvoir m'emparer de sa puce qui une fois connectée à mon cerveau me donnera toutes les connaisances dont ces robots disposent!"


    return
