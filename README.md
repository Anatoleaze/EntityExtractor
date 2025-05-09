# Entity Extractor

Entity Extractor est une application web conçue pour extraire et analyser les entités nommées à partir d’un texte libre ou d’une URL. Le projet repose sur le framework **Django** pour la partie web et **Spacy** pour l’analyse linguistique.

## 🌟 À propos du projet

Ce projet passionnant consistait à récupérer et analyser les entités nommées d’un texte. Pour cela, j'ai utilisé :

- **Python** pour l’analyse de texte,
- **Django** pour créer une interface web conviviale,
- **Spacy** pour l’extraction des entités nommées (personnes, entreprises, lieux, etc.),
- Des **algorithmes personnalisés** pour identifier des entités spécifiques selon les besoins.

L'application permet :
- d'analyser un texte libre ou le contenu d'une URL,
- de visualiser les entités nommées extraites,
- de rechercher et filtrer les résultats de manière interactive.

Ce projet m'a permis de renforcer mes compétences en développement web et en traitement de texte avec Python.

## 🧰 Technologies utilisées

- Python 3.9
- Django
- Spacy
- Docker

## 🚀 Lancer l'application avec Docker

### Prérequis

- [Docker](https://www.docker.com/) installé sur votre machine.

### Étapes d'installation

1. **Cloner le dépôt :**

```bash
   git clone https://github.com/Anatoleaze/EntityExtractor.git
   cd EntityExtractor
```

2 .Construire l’image Docker :

```bash
   docker build -t entity-extractor .
```

3. Lancer le conteneur :

```bash
   docker run -p 5000:5000 entity-extractor
```

4.Accéder à l'application :

Ouvrir votre navigateur à l’adresse : http://localhost:5000


### 📄 Licence

Ce projet est open source. Vous pouvez le modifier et le redistribuer selon vos besoins.