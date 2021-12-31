# TEST
# Projet de Synthèse : Big Data, Text Processing et Machine Learning 
Analyse de sentiment de tweets Covid19
## Partie Big Data
 &nbsp;&nbsp;&nbsp;Ce projet de synthèse donne le "sentiment" de tweets sur covid19 stockés sur un cluster MongoDB; les données sont distribuées sur plusieurs shards du cluster. 
PyMongo est utilisé pour explorer les documents mongo qui représentent les tweets.
## Partie Text Processing
 &nbsp;&nbsp;&nbsp;Diverses méthodes de prétraitement de texte sont utilisées par la suite pour préparer les tweets pour la phase machine learning
## Partie Machine Learning 
 &nbsp;&nbsp;&nbsp;En dernier lieu, un modèle de classification de régression logistique est construit, entraîné et évalué. La fonctionnalité d'analyse de sentiment mais également les services de reconnaissance d'entités nommées, token et lemmma et résumé de corpus de texte sont finalement déployés via Streamlit. Pour information, Streamlit n'est ici q'un outil de déploiement et n'est pas un composant essentiel de ce projet.
 ## Partie Déploiement : Application streamlit

 #### Fonctionnalité Sentiment analysis
 ![image](https://user-images.githubusercontent.com/62526508/107958666-a0e9e400-6fa2-11eb-8048-46d0fb2221b4.png)
 
