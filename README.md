# tffdevops
Voir le fichier requierment.txt pour les outils pythons nécessaires


#creer des images multiplatformes
Utiliser buildx (par défaut dans docker) et QEMU
Installer les composants binfmt_misc (https://en.wikipedia.org/wiki/Binfmt_misc https://github.com/tonistiigi/binfmt)
docker run --privileged --rm tonistiigi/binfmt --install all

Créer un nouvel environement de build :
docker buildx create --name raspibuilder

Voir les environemetns de build :
docker buildx ls

Switcher sur l'environement de build nouvellement créé :
docker buildx use raspibuilder

Activer et inspecter le nouvel environement :
docker buildx inspect --bootstrap

Lancer le build et le push sur docker hub. /!\ obligation de mettre en ligne pour image multi plateformes
docker buildx build --platform linux/arm64,linux/amd64 --tag melaen/flaskalk:multi --push .

-------
JENKINS
-------

Une fois Jenkins configuré, s'y connecter.


Ajout des plugins nécessaires :


Aller dans la gestion des plugins pour ajouter ou vérifier l'existence de ces plugins : 

- Git plugin
- Kubernetes
- Docker plugin
(D'autres à signaler ?)


Automatiser la récupération du repo Github :


Créer une tâche Jenkins pour que chaque modification dans la branche "Main" du repo Github soit prise
en compte par Jenkins et soit prête pour envoyer vers DockerHub.
Le système est automatisé et scrute les changements sur Github chaque minute.

Créer une image docker avec le dernier repo récupérer et l'envoyer vers DockerHub :

Lier Jenkins avec Kubernetes pour déployer automatiquement:

Configurer Kubernetes pour déployer automatiquement la dernière image de DockerHub :

-------
Docker
-------
pour installer docker, dl le script offciel

 curl -fsSL https://get.docker.com -o get-docker.sh

execute: 

 sudo sh get-docker.sh

se rajouter au groupe docker:

sudo usermod -aG docker <your-user>

-------
Minikube
-------
Dowload du package:

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_arm64.deb

installation du package
sudo dpkg -i minikube_latest_arm64.deb


-------
Kubectl
-------

Ajout des package pré-requis:

sudo apt-get install -y apt-transport-https ca-certificates curl


download de la clés public du cloud de Google

sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg


Ajout du repository de Kubernetes:

echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list


Intallation de Kubectl:

sudo apt-get update
sudo apt-get install -y kubectl