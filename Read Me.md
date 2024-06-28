### Projet d'Études - Bilal AMARA - MSI-1 C Cybersécurité - Création Tool Box ###
----------------------------------------------------------------------
  
# Objectif : 

Développer une boîte à outils interactive et automatisée visant à simplifier et automatiser les processus de tests d'intrusion, notamment les Pentests.

## Installation des pré-requis : 
  
La Tool Box : The Toolbox; Nécessite pour son utilisation quelques pré requis.

- Installer Pyhton sur le site oficiel de Python : https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe

- Utilisez le fichier d'installation "packages.bat" pour télécharger toutes les bibliothèques nécessaires. Assurez-vous que Python est bien ajouté au PATH du système lors de son installation, ce qui permettra l'exécution du fichier "packages.bat".

- Installez l'application Nmap, car notre tool box utilise la bibliothèque Nmap associée à Python, nécessitant l'application pour fonctionner correctement.
  

### Utilisation de la toolbox :
  
Pour utiliser notre Toolbox, exécutez simplement le fichier principal "The_Toolbox.py". Cette action lancera l'outil et vous dirigera vers le menu principal, où vous pourrez explorer les différentes fonctionnalités disponibles.

La navigation au sein de notre boîte à outils est intuitive, vous permettant de choisir les outils selon vos besoins spécifiques et les tâches que vous souhaitez accomplir.

Les commentaires dans le code sont en français pour en faciliter la compréhension ainsi que l'interface utilisateur. Pour une meilleure approche, il faudrait mettre cela en anglais ce qui permet une meilleure accessibilité et compatibilité avec les normes de l'industrie.

Notre Toolbox est conçue avec une architecture réfléchie et organisée, chaque outil étant soigneusement catégorisé et classifié pour faciliter votre exploration et utilisation efficace de notre gamme complète d'outils de sécurité.
  
The Toolbox :  

  Black Box Test :
     - Scan IP et OS
     - Scan Ports et Services
     - Scan Nom de Domaine
     - Recherche Exploits
     - Générer rapport 

  Grey Box Test :
     - Scan OS Vulnérabilités
     - Scan Ports Vulnérabilités
     - San Vulnérabilités CVE
     - Générer rapport

  White Box Test :
     - Gestion et Test de mot de passe
     - Brute force 
     - Générer rapport



#### Commentaires :

J'ai créé deux interfaces pour "The Tollbox" : une interface en ligne de commande (CLI) et une interface graphique web.

    Interface CLI :
    L'interface CLI est accessible via le fichier The_Toolbox.py. Cette interface est complète et opérationnelle, permettant l'utilisation de toutes les fonctionnalités de la toolbox.

    Interface graphique web :
    J'ai également commencé à développer une interface graphique web pour la toolbox. Bien que l'aspect design de cette interface soit terminé, je n'ai malheureusement pas pu finaliser l'aspect contenu. En particulier, je n'ai pas réussi à afficher le contenu des fonctionnalités Python sur les pages web correspondantes (Black Box Test, White Box Test, et Grey Box Test). Le problème réside principalement dans l'affichage du contenu.

Le manque de temps, de connaissances et de compétences en développement web, notamment sur les méthodes POST et GET, m'ont empêché de terminer cette interface graphique. Cependant, une solution possible pourrait être l'utilisation du serveur Flask pour gérer les requêtes et les réponses entre le front-end et le back-end. Flask pourrait faciliter la communication entre les fonctionnalités Python et l'interface web, rendant ainsi la toolbox pleinement fonctionnelle dans un environnement web.

Ce document vise à fournir une vue d'ensemble claire et concise de "The Toolbox", facilitant son installation et son utilisation pour les tests d'intrusion et les analyses de sécurité.

Structure de l'interface Web de la Toolbox : 

 /Application_Web_Toolbox
	/Page_Accueil_(1er)
	/Page_Choix_Test_(2eme)
	/Page_Black_Box_Test
	/Page_Grey_Box_Test
	/Page_White_Box_Test
	