# tffdevops
besoin de flask et de pytest


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
Cela va chercher l'image nécessaire a