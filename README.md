# Project Title
League of Legend

## Overview
Briefly describe what the project does and its purpose. Include any unique features or problems it solves.

## Features
- Feature 1: Describe the feature and its benefit.
- Feature 2: Highlight another feature and why it's useful.
- Feature 3: If applicable, describe another key aspect of the project.

## Installation
Provide step-by-step instructions on how to get a development environment running.

```bash
git clone https://github.com/username/projectname.git
cd projectname
pip install -r requirements.txt

## Dataset 
Proviennent du site principal op.gg : "https://www.op.gg"
Voici le lien des datasets : https://drive.google.com/drive/folders/1Y5bTnNGTyBFWbEuXdc0BFq9fFeXZresH?usp=share_link
Pour l'instant, un seul dataset sur les caractéristiques des champions a été téléchargé. Nous souhaitons par la suite scrapper des données sur l'historique des parties, mes aussi les points forts et les points faibles des champions. 


#Présentation du jeu

League of Legends est un jeu multijoueur dans lequel deux équipes de 5 joueurs s'affrontent.
La vue de la partie sera aérienne et la carte peut être considérée comme symétrique.
La durée moyenne d'une partie est d'environ 25 minutes.
Les différents joueurs incarneront un rôle particulier et un personnage appelé champion.
Chaque champion possède généralement d'un passif, de 3 compétences classiques et d'une compétence ultime.
Le but est de détruire la base ennemie, plus spécifiquement le bâtiment appelé nexus.
La carte est composée de 3 lignes et d'une jungle entre chaque ligne.
Chaque ligne est composée de plusieurs tourelles qui vont ralentir la progression ennemie vers le nexus.
Des vagues de sbires apparaissent afin d'aider le joueur à détruire les tours adverses.
Les champions reviennent en vie dans leur base après leur mort, avec une certaine attente qui augmente au fur et à mesure de la partie.
Les joueurs vont aussi combattre des monstres épiques dans la jungle afin de gagner des puissants bonus d'équipes.
Les joueurs peuvent acquérir de la puissance en tuant les champions adverses, des tourelles, des sbires et des monstres afin de gagner en puissance et en équipement.
La sélection des champions se fait en amont: on peut savoir les différents champions en jeu juste avant le lancement de la partie.
Dans le mode classé solo(qui sera le mode choisi), on ne peut pas prendre un personnage déjà pris et il y a 5 champions bannis par équipes.


#But du projet

Prédire les chances de victoire avant le lancement de la partie afin de savoir s'il vaut mieux "dodge"(esquiver) la partie au lieu de la jouer.
Réaliser un algorithme qui permettra de prédire les chances de victoire avec pour seules informations la composition des deux équipes.
Bonus: Plusieurs facteurs complémentaires intéressant mais complexe comme les contres, les synergies et les meilleurs "ban"(champion banni)


#Sélection des datasets
Tous les datasets proviennent du site op.gg.
1er dataset: chiffres clés sur chaque personnage(taux de victoire,"pick" rate, ban rate).
2e dataset: scrapping de milliers de parties avec la composition des deux équipes et quelle équipe a gagné.
Source des datasets: OP.GG (un site de référence dans le jeu)
Le 1er dataset sert plus pour avoir les intuitions de base alors que le deuxième servira à l'algorithme de Machine Learning(probablement classification).