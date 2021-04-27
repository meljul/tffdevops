/!\ sudo iptables -P FORWARD ACCEPT pour accepter le forward réseau sur raspi après un reboot

---
---
# TFF DevOps
=> Voir le fichier ***[requirements.txt](https://github.com/meljul/tffdevops/blob/main/requirements.txt)*** pour les outils python nécessaires. <=
=> Consultez le ***[DockerHub](https://hub.docker.com/r/melaen/flaskalk)***<=
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

Créer une tâche Jenkins pour que chaque modification dans la branche "Main" du repo Github soit prise
en compte par Jenkins et soit prête pour envoyer vers DockerHub.
Le système est automatisé, Github envoie une notification à Jenkins qui procède à la récupération.

## Ajouter les crendentials nécessaires:

- Manage Credential -> Global -> Add Crendentials
- Type : SSH Username Private Key
- ID : GitHubSSH
- Username : Jenkins User
- Private key : Enter directly : [PASTE KEY]
- Passphrase : [PASSWORD]
- OK

## Programmer récupération - build - push sur DockerHub: 

- New freestyle project

- Description : Auto récupération du repo Github, build et push image sur DockerHub
- Cocher GitHub Project
- Ajouter URL projet : https://github.com/meljul/tffdevops/
- Cocher Supprimer anciens Builds
- Supprimer anciens builds après 7j

- Gestion de code source avec Git et lier user Jenkins(SSH Github)
- Spécifier branch to build : */main
- Ce qui déclenche le build : GitHub hook trigger for GITScm polling (notification GiHub)

- Environnements de build : Use secret text(s) or file(s)
- Username and password (seperated) -> Ajout des variables utilisées + lier compte DockerHub
- Ajouter éxécution script shell : 
---
virtualenv venv
. venv/bin/activate 
pip install -r requirements.txt
pytest 

- Ajouter éxécution second script shell : 
---
docker login -u $username_dockerhub -p $passwd_dockerhub
docker buildx build --platform linux/arm64,linux/amd64 --tag melaen/flaskalk:multi --push .
docker logout


- Action à la suite du build : Notifier par email : Add email et cocher envoyer si build instable

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

