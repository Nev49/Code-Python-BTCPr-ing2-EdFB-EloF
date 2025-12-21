# Code-Python-BTCPr-ing2-EdFB-EloF

Fichier ReadMe : Analyse de données bactériennes chez la souris
1.	Description du projet
Notre code Python a pour objectif d’analyser des données issues de fichiers CSV contenant des mesures de quantité de bactéries vivantes dans différentes parties (fécal, cæcal, iléal) du système digestif de souris soumises à différents traitements (ABX, cocktail d’antibiotiques ou Placebo). Il va ainsi générer automatiquement trois graphiques : une courbe temporelle pour les analyses fécales et deux graphiques en violon différents pour les données caecales et iléales.
Les graphiques sont ensuite sauvegardés dans un dossier dédié.
2.	Structure du projet.
Notre projet va être structuré de la façon suivante : le fichier de données data_small.csv se trouve à la racine du projet. Puis, nous pouvons retrouver notre script principal, main.py avant de voir les fichiers input/, contenant une copie du fichier CSV. Puis, le dossier contenant les graphiques sera créé : images/.
Pour cela, nous avons dû faire appel à la bibliothèques matplotlib, pandas, math, shutil et os.
3.	Instructions pour lancer le code
Il faut d’abord cloner le dépôt et vérifier la présence du fichier data_small.csv. Le script dépendant de ce fichier, il doit être placé à la racine du projet.
Puis, il faut exécuter le scripte principal avant de pouvoir observer les résultats sous formes de graphes générés. 
4.	Fonctionnement interne
Le script lit le CSV et récupère la liste des souris uniques. Puis, pour chaque souris, on lit le fichier CSV (donc ligne par ligne) avant d’en extraire des valeurs selon le type d’échantillon. Enfin, on génère les graphiques demandés et on les sauvegarde dans un fichier adapté.
Néanmoins, on peut voir que les dossiers input/ et images/ sont supprimés puis recréés à chaque exécution.
5.	Limitations fonctionnelles
Dans ce devoir, nous nous sommes retrouvés confrontés à des difficultés, que nous avons surmontées en passant parfois par des lignes de codes supplémentaires, et prenant sur le temps d’exécution du code. Par exemple, Le fichier CSV étant relu entièrement pour chaque souris, le temps d’exécution de code n’en est que plus long. 
De plus, dans notre code, aucune gestion d’erreurs n’est prévue, comme en cas de fichier manquant, du fichier CSV mal formaté, ou de valeurs invalides.

