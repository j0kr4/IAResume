Projet Résumé de news IT avec llama2

Ce projet est réalisé en python pour résumé l'actualité IT du jour.

Assurez-vous d'avoir Python 3 ainsi que pip d'installé. Si ce n'est pas le cas, installez-les.

Créer l'environnement virtuel python

cd /chemin/vers/le/projet
python -m venv venv
# Linux/MacOS
source venv/bin/activate
# Windows
source venv\Scripts\activate



Installer le model llama2 depuis Ollama.
Récupérer le model depuis le projet:
ollama pull llama2

Installer les librairies prérequises (feedparser et langchain)
pip install -r requirements.txt

Executer le programme
python main.py
