# -*- coding: utf-8 -*-
"""
Banque de contenu ORIGINAL par catégorie de magasin.
Chaque catégorie a plusieurs variantes (intro, conseils, rayons, FAQ) qui sont
pigées de façon déterministe (selon le slug du magasin) pour que deux magasins
de la même catégorie n'affichent jamais exactement la même combinaison de textes.
"""

CATEGORIES = {
    "Épicerie": {
        "intros": [
            "Chaque semaine, {nom} renouvelle son cahier de circulaire avec de nouveaux prix sur l'épicerie de base, les produits frais et quelques incontournables du garde-manger. Voici comment s'y retrouver avant votre prochaine liste d'épicerie.",
            "La circulaire {nom} de {periode} regroupe les spéciaux hebdomadaires en épicerie : viande, produits laitiers, fruits et légumes et une sélection d'articles du centre du magasin. On vous résume l'essentiel pour planifier vos repas.",
            "Envie de savoir ce qui s'en vient chez {nom} avant d'aller faire l'épicerie ? Cette page rassemble les grandes lignes de la circulaire {periode}, section par section, pour vous éviter de fouiller.",
            "{nom} publie une nouvelle circulaire {periode}. On y retrouve généralement des rabais sur les produits de saison, la viande et quelques articles emballés. Petit tour d'horizon avant de préparer votre liste.",
        ],
        "rayons": [
            [("Fruits et légumes", "Les arrivages de la semaine et les produits de saison sont habituellement les premiers à changer de prix."),
             ("Viandes et volailles", "C'est souvent ici que se trouvent les meilleurs rabais au kilo, surtout en fin de semaine."),
             ("Produits laitiers et œufs", "Lait, fromage et yogourt reviennent régulièrement dans les circulaires hebdomadaires."),
             ("Boulangerie", "Pain frais et pâtisseries maison font partie des incontournables de plusieurs succursales."),
             ("Épicerie et conserves", "Pâtes, conserves, céréales : de bons moments pour faire des réserves quand le prix baisse.")],
            [("Poissonnerie", "Selon la succursale, le poisson frais et les fruits de mer font parfois l'objet de promotions ciblées."),
             ("Charcuterie et fromagerie", "Le comptoir de charcuterie propose souvent des combos ou des rabais à la coupe."),
             ("Surgelés", "Repas préparés, légumes congelés et crème glacée reviennent fréquemment dans les aubaines."),
             ("Produits de santé et beauté", "Certaines semaines incluent aussi des rabais hors alimentation, dans la section pharmacie ou hygiène."),
             ("Boissons", "Café, jus et boissons gazeuses figurent souvent parmi les articles vedettes.")],
            [("Aliments du monde", "Plusieurs succursales élargissent leur offre internationale avec des rabais ponctuels."),
             ("Produits en vrac et format familial", "Les gros formats sont parfois plus avantageux durant la semaine de circulaire."),
             ("Collations et boîte à lunch", "Barres tendres, fruits en portions et grignotines pour les lunchs de la semaine."),
             ("Articles de nettoyage", "Certaines circulaires combinent l'alimentation avec des produits ménagers en rabais."),
             ("Boulangerie et pâtisserie", "Gâteaux, viennoiseries et pains spéciaux font partie des classiques de la semaine.")],
        ],
        "conseils": [
            "Comparez toujours le prix par 100 g ou par litre plutôt que le prix affiché : un format plus gros n'est pas toujours le meilleur deal.",
            "Planifiez vos repas de la semaine autour des viandes et légumes en rabais : c'est la façon la plus simple de réduire la facture sans sacrifier la variété.",
            "Gardez un œil sur les produits qui reviennent en spécial toutes les 4 à 6 semaines pour savoir quand faire vos réserves de garde-manger.",
            "Les fruits et légumes de saison sont presque toujours moins chers et plus frais : la circulaire est un bon indicateur de ce qui est disponible localement.",
        ],
        "faqs": [
            [("La circulaire {nom} change-t-elle chaque semaine ?",
              "Oui, la plupart des épiceries renouvellent leur circulaire chaque semaine, généralement du jeudi au mercredi suivant."),
             ("Les prix sont-ils les mêmes dans toutes les succursales {nom} ?",
              "Pas nécessairement. Certaines promotions peuvent varier d'une région à l'autre ou être offertes seulement dans certaines succursales participantes."),
             ("Puis-je voir la circulaire de la semaine prochaine à l'avance ?",
              "Quand elle est disponible en primeur, on l'affiche sur la page « semaine prochaine » du magasin, avant même son entrée en vigueur.")],
            [("À quelle fréquence les aubaines changent-elles chez {nom} ?",
              "La circulaire hebdomadaire est le format le plus courant, avec parfois des dépliants supplémentaires pour des occasions spéciales."),
             ("Les rabais s'appliquent-ils aux produits en ligne ?",
              "Cela dépend de la politique du magasin ; certains rabais en circulaire s'appliquent aussi en ligne, d'autres seulement en succursale."),
             ("Comment savoir quand la nouvelle circulaire est publiée ?",
              "La transition se fait habituellement le jeudi matin, moment où la semaine « prochaine » devient la semaine « en cours ».")],
        ],
    },
    "Épicerie santé": {
        "intros": [
            "{nom} met à jour sa circulaire {periode} avec des rabais sur les produits naturels, biologiques et les suppléments les plus populaires.",
            "La circulaire {periode} de {nom} regroupe généralement des promotions sur les aliments biologiques, les produits sans allergènes et les soins naturels.",
            "Amateurs d'alimentation santé : voici un résumé de ce que propose habituellement la circulaire {nom} cette semaine.",
        ],
        "rayons": [
            [("Suppléments et vitamines", "Les rabais sur les vitamines et probiotiques reviennent régulièrement."),
             ("Aliments biologiques", "Fruits, légumes et produits certifiés bio font partie des vedettes fréquentes."),
             ("Produits sans allergènes", "Options sans gluten, sans lactose ou végétaliennes sont souvent mises de l'avant."),
             ("Soins naturels", "Cosmétiques et soins corporels naturels complètent souvent l'offre alimentaire."),
             ("Vrac et grains", "Légumineuses, noix et grains entiers en vrac sont un classique de ce type de commerce.")],
        ],
        "conseils": [
            "Comparez les certifications (biologique, sans OGM, équitable) pour vous assurer que le rabais correspond vraiment à ce que vous cherchez.",
            "Les suppléments se conservent longtemps : c'est souvent le bon moment pour renouveler votre stock quand ils sont en spécial.",
            "Les produits en vrac sont généralement plus économiques que leur équivalent préemballé, même hors promotion.",
        ],
        "faqs": [
            [("Les produits {nom} sont-ils tous certifiés biologiques ?",
              "Pas nécessairement tous, mais une bonne partie de l'inventaire de ce type de magasin met l'accent sur les produits naturels et biologiques."),
             ("La circulaire couvre-t-elle les suppléments et les cosmétiques ?",
              "Oui, en plus de l'alimentation, ces circulaires incluent souvent des rabais sur les vitamines, suppléments et soins corporels.")],
        ],
    },
    "Pharmacie": {
        "intros": [
            "La circulaire {nom} de {periode} propose habituellement des rabais sur les produits de santé, beauté et quelques articles d'épicerie de dépannage.",
            "Chaque semaine, {nom} publie une nouvelle circulaire avec des aubaines sur les cosmétiques, les soins personnels et parfois des points de récompense bonifiés.",
            "Voici un aperçu de ce que contient généralement la circulaire {periode} de {nom} : beauté, santé et quelques surprises saisonnières.",
        ],
        "rayons": [
            [("Beauté et cosmétiques", "Maquillage, soins de la peau et parfums sont souvent au cœur des promotions hebdomadaires."),
             ("Santé et pharmacie", "Produits en vente libre, vitamines et articles de premiers soins reviennent fréquemment."),
             ("Soins personnels", "Shampoing, hygiène buccale et rasage font partie des classiques de circulaire."),
             ("Points de récompense", "Plusieurs semaines incluent des multiplicateurs de points sur des achats ciblés."),
             ("Saisonnier", "Articles de saison (rentrée, fêtes, été) s'ajoutent selon la période de l'année.")],
        ],
        "conseils": [
            "Les programmes de fidélité multiplient souvent les points certains jours précis : vérifiez le calendrier de la semaine avant d'acheter.",
            "Les cosmétiques et soins de la peau sont parmi les catégories les plus rentables à acheter uniquement en circulaire.",
            "Empilez les rabais en circulaire avec les coupons du fabricant quand c'est permis, pour maximiser l'économie.",
        ],
        "faqs": [
            [("Les rabais {nom} incluent-ils les points de récompense ?",
              "Souvent oui : plusieurs circulaires de pharmacie combinent un rabais en argent avec des points bonifiés sur certains achats."),
             ("La circulaire est-elle la même dans toutes les provinces ?",
              "Pas toujours ; les pharmacies ajustent parfois leur offre selon la province ou la région desservie.")],
        ],
    },
    "Quincaillerie & réno": {
        "intros": [
            "La circulaire {nom} de {periode} met généralement l'accent sur les outils, les matériaux de construction et les produits saisonniers d'extérieur.",
            "Projet de rénovation en vue ? Voici un résumé de ce que propose habituellement la circulaire {periode} de {nom}.",
            "{nom} publie chaque semaine une sélection d'aubaines sur les outils, la quincaillerie et l'entretien extérieur. Voici les grandes lignes de {periode}.",
        ],
        "rayons": [
            [("Outils et quincaillerie", "Outils à main et électroportatifs figurent souvent parmi les vedettes de la semaine."),
             ("Matériaux de construction", "Bois, isolant et matériaux de base font partie des promotions récurrentes."),
             ("Extérieur et jardin", "BBQ, mobilier de patio et articles de jardinage varient selon la saison."),
             ("Peinture et finition", "Peinture, teinture et accessoires de finition reviennent régulièrement en rabais."),
             ("Chauffage et entretien saisonnier", "Selon la saison, chauffage, déneigement ou climatisation prennent le relais.")],
        ],
        "conseils": [
            "Les gros travaux (peinture, bois, isolant) valent la peine d'être planifiés autour des semaines de circulaire pour économiser sur les quantités.",
            "Les outils électroportatifs sont souvent vendus en combo (outil + batterie + chargeur) à meilleur prix qu'à l'unité.",
            "Les articles saisonniers (BBQ, déneigement) sont généralement moins chers juste avant ou juste après la haute saison.",
        ],
        "faqs": [
            [("La circulaire {nom} couvre-t-elle tous les rayons du magasin ?",
              "Généralement non : elle met l'accent sur une sélection de produits vedettes, souvent liés à la saison en cours."),
             ("Puis-je réserver un article en rabais avant sa sortie en magasin ?",
              "Cela dépend du magasin ; certaines succursales permettent une mise de côté, d'autres non.")],
        ],
    },
    "Meubles & maison": {
        "intros": [
            "La circulaire {nom} de {periode} présente habituellement des rabais sur le mobilier, la literie et la décoration.",
            "Meubler ou redécorer une pièce ? Voici un aperçu de ce que propose généralement {nom} dans sa circulaire {periode}.",
            "{nom} renouvelle sa sélection de promotions {periode} : salon, chambre, salle à manger et accessoires déco.",
        ],
        "rayons": [
            [("Salon", "Sofas, fauteuils et tables basses reviennent souvent dans les circulaires saisonnières."),
             ("Chambre et literie", "Matelas, ensembles de lit et accessoires de chambre font partie des classiques."),
             ("Salle à manger", "Tables, chaises et vaisselliers sont régulièrement mis en vedette."),
             ("Décoration", "Coussins, luminaires et accessoires complètent souvent l'offre de meubles."),
             ("Électroménagers", "Certaines circulaires incluent aussi des rabais sur les gros électroménagers.")],
        ],
        "conseils": [
            "Les rabais sur les ensembles complets (chambre, salle à manger) sont souvent plus avantageux que l'achat de pièces séparées.",
            "Les changements de saison sont un bon moment pour surveiller les rabais sur les matelas et la literie.",
            "Vérifiez toujours les frais de livraison et d'assemblage, qui peuvent varier même quand le meuble est en rabais.",
        ],
        "faqs": [
            [("Les meubles en circulaire sont-ils toujours en stock ?",
              "Pas garanti : les quantités sont parfois limitées, surtout pour les articles très populaires."),
             ("{nom} offre-t-il un financement sur les meubles en rabais ?",
              "Plusieurs détaillants de meubles proposent des options de financement, en plus des rabais affichés en circulaire.")],
        ],
    },
    "Grande surface": {
        "intros": [
            "La circulaire {nom} de {periode} couvre habituellement plusieurs catégories : épicerie, maison, vêtements et électronique.",
            "{nom} publie chaque semaine une circulaire multi-catégories. Voici un résumé de ce qu'on y retrouve généralement pour {periode}.",
        ],
        "rayons": [
            [("Épicerie", "Une sélection de produits alimentaires accompagne souvent les autres catégories."),
             ("Maison et cuisine", "Petits électroménagers et articles de cuisine reviennent régulièrement."),
             ("Vêtements et saisonnier", "L'offre vestimentaire change selon la saison en cours."),
             ("Électronique", "Certaines semaines incluent des rabais ciblés sur l'électronique grand public.")],
        ],
        "conseils": [
            "Dans un magasin à grande surface, la circulaire est souvent divisée par catégorie : parcourez chaque section pour ne rien manquer.",
            "Les rabais électronique sont souvent limités en quantité : mieux vaut vérifier tôt dans la semaine.",
        ],
        "faqs": [
            [("La circulaire {nom} est-elle la même partout au pays ?",
              "Pas toujours ; certaines promotions varient selon la province ou la succursale."),
             ("Les prix en circulaire s'appliquent-ils aussi en ligne ?",
              "Cela dépend de la politique du détaillant, mais c'est fréquemment le cas pour les grandes surfaces.")],
        ],
    },
    "Entrepôt": {
        "intros": [
            "La circulaire {nom} de {periode} met l'accent sur les formats familiaux et les rabais en gros volume.",
            "{nom} propose habituellement une sélection d'aubaines en formats entrepôt pour {periode} — idéal pour les réserves.",
        ],
        "rayons": [
            [("Alimentation en gros format", "Viande, produits secs et surgelés en grand format sont la spécialité de ce type de commerce."),
             ("Articles de maison", "Produits ménagers et articles pratiques en format économique."),
             ("Saisonnier", "Certaines périodes de l'année amènent des rabais ponctuels sur des articles spéciaux.")],
        ],
        "conseils": [
            "Le format entrepôt est avantageux seulement si vous avez la capacité de conserver ou congeler les grandes quantités.",
            "Comparez le prix unitaire avec celui d'une épicerie standard : l'économie n'est pas automatique sur tous les articles.",
        ],
        "faqs": [
            [("Faut-il une carte de membre pour profiter des rabais {nom} ?",
              "Selon le commerce, un abonnement ou une carte de membre peut être nécessaire pour accéder à certains prix."),
             ("Les formats sont-ils toujours plus économiques au kilo ?",
              "Pas systématiquement : il vaut la peine de comparer le prix par unité avant d'acheter en grande quantité.")],
        ],
    },
    "Électronique": {
        "intros": [
            "La circulaire {nom} de {periode} regroupe habituellement les meilleurs prix sur l'électronique grand public et les accessoires.",
            "{nom} publie chaque semaine une sélection d'aubaines tech pour {periode}. Voici un aperçu des catégories les plus souvent visées.",
        ],
        "rayons": [
            [("Audio et vidéo", "Écouteurs, haut-parleurs et téléviseurs figurent souvent parmi les vedettes."),
             ("Informatique", "Ordinateurs portables et accessoires reviennent régulièrement en rabais."),
             ("Jeux et divertissement", "Consoles, jeux et accessoires de gaming complètent souvent l'offre."),
             ("Photo", "Appareils photo et accessoires sont parfois mis en vedette selon la saison.")],
        ],
        "conseils": [
            "Les rabais électronique sont souvent limités en quantité : agir tôt dans la semaine augmente vos chances.",
            "Comparez toujours le modèle exact en circulaire avec les versions plus récentes avant d'acheter.",
        ],
        "faqs": [
            [("Les garanties sont-elles incluses sur les articles en circulaire ?",
              "La garantie du fabricant s'applique généralement, peu importe si l'article est acheté en rabais."),
             ("Puis-je faire mettre un article de côté avant sa sortie en circulaire ?",
              "Cela dépend de la politique de la succursale ; ce n'est pas garanti partout.")],
        ],
    },
    "Animalerie": {
        "intros": [
            "La circulaire {nom} de {periode} propose habituellement des rabais sur la nourriture, les accessoires et les soins pour animaux.",
            "{nom} renouvelle son offre {periode} avec des promotions sur l'alimentation animale et les accessoires les plus populaires.",
        ],
        "rayons": [
            [("Nourriture pour chiens et chats", "Les grands formats de nourriture sont souvent les vedettes de la semaine."),
             ("Accessoires", "Jouets, laisses et litières reviennent régulièrement en rabais."),
             ("Soins et santé animale", "Produits de toilettage et suppléments complètent souvent l'offre."),
             ("Petits animaux et aquariophilie", "Selon la succursale, une sélection dédiée aux petits animaux peut être incluse.")],
        ],
        "conseils": [
            "La nourriture sèche se conserve bien : c'est souvent avantageux d'en profiter pour acheter un plus gros format en rabais.",
            "Vérifiez la date de péremption même sur les formats en spécial, surtout pour la nourriture humide.",
        ],
        "faqs": [
            [("Les rabais {nom} s'appliquent-ils à toutes les marques ?",
              "Non, la circulaire cible généralement une sélection de marques précises chaque semaine."),
             ("Y a-t-il un programme de fidélité chez {nom} ?",
              "Plusieurs animaleries offrent un programme de points ou de carte-fidélité en plus des rabais hebdomadaires.")],
        ],
    },
    "Sport & plein air": {
        "intros": [
            "La circulaire {nom} de {periode} met généralement de l'avant l'équipement sportif et de plein air selon la saison.",
            "{nom} publie chaque semaine des aubaines sur le sport et le plein air. Voici les grandes lignes pour {periode}.",
        ],
        "rayons": [
            [("Vêtements techniques", "Manteaux, chaussures et vêtements de sport varient selon la saison."),
             ("Équipement de plein air", "Camping, randonnée et sports d'eau reviennent selon la période de l'année."),
             ("Sports d'équipe et individuels", "Articles liés aux sports populaires de la saison sont souvent mis en vedette.")],
        ],
        "conseils": [
            "L'équipement saisonnier (ski, camping) est souvent moins cher juste avant ou après la haute saison.",
            "Comparez les rabais sur les vêtements techniques avec la qualité des matériaux, pas seulement le prix affiché.",
        ],
        "faqs": [
            [("Les tailles limitées sont-elles fréquentes en circulaire ?",
              "Oui, les articles vedettes en rabais peuvent avoir un choix de tailles restreint selon la succursale."),
             ("{nom} offre-t-il une politique de retour sur les articles en rabais ?",
              "Généralement oui, mais les conditions peuvent varier ; il est préférable de vérifier en succursale.")],
        ],
    },
    "Jardinage": {
        "intros": [
            "La circulaire {nom} de {periode} propose habituellement des rabais sur les végétaux, la terre et les accessoires de jardin.",
            "{nom} renouvelle son offre horticole {periode}. Voici un résumé des catégories les plus fréquentes.",
        ],
        "rayons": [
            [("Végétaux et semences", "Fleurs, arbustes et semences varient selon la saison de plantation."),
             ("Terreau et engrais", "Produits d'entretien du sol reviennent régulièrement en rabais au printemps et à l'été."),
             ("Accessoires de jardin", "Outils et mobilier extérieur complètent souvent l'offre.")],
        ],
        "conseils": [
            "Les végétaux se vendent souvent moins cher en fin de saison : une bonne option si vous pouvez les hiverner.",
            "Comparez la qualité et la garantie des plants avant de choisir uniquement selon le prix.",
        ],
        "faqs": [
            [("Les végétaux en circulaire sont-ils garantis ?",
              "Plusieurs jardineries offrent une garantie de reprise sur les végétaux, sous certaines conditions."),
             ("La circulaire {nom} varie-t-elle selon le climat régional ?",
              "Oui, l'offre végétale est souvent ajustée selon la zone de rusticité et la période de plantation locale.")],
        ],
    },
    "Auto & outils": {
        "intros": [
            "La circulaire {nom} de {periode} regroupe généralement des rabais sur les outils, les pièces et l'entretien automobile.",
            "{nom} publie chaque semaine une sélection d'aubaines pour l'auto et l'atelier. Voici un aperçu pour {periode}.",
        ],
        "rayons": [
            [("Outils", "Outils à main et électroportatifs reviennent régulièrement en rabais."),
             ("Entretien automobile", "Huile, pneus et accessoires saisonniers varient selon la période de l'année."),
             ("Rangement et atelier", "Coffres à outils et systèmes de rangement complètent souvent l'offre.")],
        ],
        "conseils": [
            "Les pneus et l'entretien saisonnier sont souvent moins chers juste avant le changement de saison.",
            "Les outils vendus en ensemble sont généralement plus avantageux que l'achat à l'unité.",
        ],
        "faqs": [
            [("Les rabais {nom} incluent-ils l'installation ?",
              "Pas toujours ; certains rabais couvrent uniquement la pièce ou l'outil, pas la main-d'œuvre."),
             ("Puis-je comparer les prix entre succursales avant d'acheter ?",
              "Certains détaillants permettent une comparaison en ligne, d'autres non ; il est préférable de vérifier directement.")],
        ],
    },
    "Bureau & loisirs": {
        "intros": [
            "La circulaire {nom} de {periode} met souvent l'accent sur les fournitures scolaires, de bureau et les loisirs créatifs.",
            "{nom} renouvelle son offre {periode} avec des rabais sur le matériel de bureau et les loisirs. Voici les grandes lignes.",
        ],
        "rayons": [
            [("Fournitures scolaires", "Cahiers, crayons et sacs à dos sont particulièrement visés en période de rentrée."),
             ("Bureau à domicile", "Papeterie, mobilier de bureau et technologie complètent souvent l'offre."),
             ("Loisirs créatifs", "Matériel d'artisanat et jeux figurent parfois dans la sélection hebdomadaire.")],
        ],
        "conseils": [
            "La période de rentrée scolaire est habituellement le moment le plus avantageux pour les fournitures de base.",
            "Achetez les articles non périssables (cahiers, crayons) en plus grande quantité quand le rabais est intéressant.",
        ],
        "faqs": [
            [("Les fournitures scolaires sont-elles rabaissées toute l'année ?",
              "Les meilleurs rabais se concentrent généralement autour de la rentrée scolaire, l'été et le début d'année."),
             ("{nom} offre-t-il des rabais pour les enseignants ?",
              "Certains détaillants proposent un programme spécifique ; il est préférable de vérifier directement en succursale.")],
        ],
    },
    "Magasin général": {
        "intros": [
            "La circulaire {nom} de {periode} couvre généralement plusieurs catégories à bas prix : maison, saisonnier et articles de tous les jours.",
            "{nom} publie chaque semaine une sélection variée d'aubaines. Voici un aperçu pour {periode}.",
        ],
        "rayons": [
            [("Maison et cuisine", "Articles pratiques du quotidien à bas prix, renouvelés chaque semaine."),
             ("Saisonnier", "Décorations et articles liés aux occasions de l'année."),
             ("Tous les jours", "Une sélection variée qui change fréquemment selon les arrivages.")],
        ],
        "conseils": [
            "Dans un magasin à bas prix, les meilleures aubaines changent souvent rapidement : mieux vaut consulter la circulaire tôt dans la semaine.",
            "Comparez tout de même les formats et quantités, même à bas prix, pour confirmer l'économie réelle.",
        ],
        "faqs": [
            [("Les articles en circulaire {nom} sont-ils toujours disponibles en succursale ?",
              "Les quantités peuvent être limitées, surtout pour les articles saisonniers ou très populaires."),
             ("Le prix affiché est-il garanti dans toutes les succursales ?",
              "Généralement oui pour les rabais nationaux, mais certaines variations locales sont possibles.")],
        ],
    },
    "Alcool": {
        "intros": [
            "La circulaire {nom} de {periode} propose habituellement des rabais sur une sélection de vins, bières et spiritueux.",
        ],
        "rayons": [
            [("Vins", "Une sélection de vins rouges, blancs et rosés change chaque semaine."),
             ("Bières et cidres", "Formats variés en rabais, souvent liés à la saison."),
             ("Spiritueux", "Une sélection ciblée de spiritueux complète généralement l'offre hebdomadaire.")],
        ],
        "conseils": [
            "Comparez le prix par litre plutôt que le prix à la bouteille pour évaluer le rabais réel.",
            "La disponibilité peut varier d'une succursale à l'autre selon les stocks régionaux.",
        ],
        "faqs": [
            [("Faut-il un âge minimum pour consulter cette circulaire ?",
              "L'achat de produits alcoolisés est réservé aux personnes majeures, conformément à la loi provinciale."),
             ("Les prix sont-ils les mêmes partout dans la province ?",
              "Pas toujours ; certains rabais peuvent varier selon la région ou le type de succursale.")],
        ],
    },
}

# alias for any type not explicitly listed
CATEGORIES.setdefault("Autre", CATEGORIES["Magasin général"])
