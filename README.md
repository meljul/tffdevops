/!\ sudo iptables -P FORWARD ACCEPT pour accepter le forward réseau sur raspi après un reboot

---
---
# TFF DevOps
=> Voir le fichier ***[requirements.txt](https://github.com/meljul/tffdevops/blob/main/requirements.txt)*** pour les outils python nécessaires. <=
## Créer des images multiplatformes
Utiliser ***buildx*** (par défaut dans docker) et ***QEMU***.
> Installer les composants **binfmt_misc** :
- [Wiki](https://en.wikipedia.org/wiki/Binfmt_misc)
- [GitHub](https://github.com/tonistiigi/binfmt)

```sh
docker run --privileged --rm tonistiigi/binfmt --install all
```

> Créer un nouvel environement de build :

```sh
docker buildx create --name raspibuilder
```

> Voir les environemetns de build :

```sh
docker buildx ls
```

> Switcher sur l'environement de build nouvellement créé :

```sh
docker buildx use raspibuilder
```

> Activer et inspecter le nouvel environement :

```sh
docker buildx inspect --bootstrap
```

> Se connecter sur Dockerhub :

```sh
docker login
```

> Lancer le build et le push sur docker hub. /!\ obligation de mettre en ligne pour image multi plateformes

```sh
docker buildx build --platform linux/arm64,linux/amd64 --tag melaen/flaskalk:multi --push .
```
---
---
# JENKINS
## Installer Jenkins sur Kubernetes pour déployer automatiquement :
Installation de Jenkins via un fichier YML pour faciliter les prochaines installations.
Installation faite sur Raspberry Pi, dans Kubernetes.
## Ajout des plugins nécessaires :
Aller dans la gestion des plugins pour ajouter ou vérifier l'existence de ces plugins : 
- Git plugin
- Kubernetes
- Docker plugin
- (D'autres à signaler ?)

## Automatiser la récupération du repo Github :
Créer une tâche Jenkins pour que chaque modification dans la branche "Main" du repo Github soit prise en compte par Jenkins et soit prête pour envoyer vers DockerHub.
Le système est automatisé et scrute les changements sur Github chaque minute.

Étape SSH sur sreenshot
Programmer récupération : 
- New freestyle project
- Description : Automatisation de la récupération du repo Github
- Cocher Supprimer anciens Builds (7 jours max)
- Gestion de code source avec Git et lier user Jenkins(SSH Github)
- (Ajouter un nom ou laisser jenkins en créer un aléatoire)
- Spécifier branch to build : */main
- Ce qui déclenche le build : Scrutation de l'outil de gestion de version : * * * * * (/minute)
(TEST)
Action à la suite du build : Notifier par email : Introduire email et cocher envoyer si build instable
APPLY + SAVE

## Créer une image docker avec le dernier repo récupérer et l'envoyer vers DockerHub :
Nécessite plugin Docker

Aller dans Manage Jenkins -> Manage crendential -> global -> add credential :
- Entrer les identifiants DockerHub

Créer un new pipeline multibranch : 
- Name : DockerHub
- Branch Sources: Github (ajouter repo et pas creds)
- Laisser le reste par défaut et save
## Configurer Kubernetes pour déployer automatiquement la dernière image de DockerHub :
bla bla
blabla

---
---
# Docker
pour installer docker, dl le script offciel via la commande :

```sh
 curl -fsSL https://get.docker.com -o get-docker.sh
```

> Executer : 

```sh
 sudo sh get-docker.sh
```

> Se rajouter au groupe docker :

```sh
sudo usermod -aG docker <your-user>
```

