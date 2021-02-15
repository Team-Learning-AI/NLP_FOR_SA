# Projet de Synthèse : Big Data, Text Processing et Machine Learning 
Analyse de sentiment de tweets Covid19
## Partie Big Data
 &nbsp;&nbsp;&nbsp;Ce projet de synthèse donne le "sentiment" de tweets sur covid19 stockés sur un cluster MongoDB; les données sont distribuées sur plusieurs shards du cluster. 
PyMongo est utilisé pour créer la base de données et la collection hôte MongoDB. Apache PySpark est utilisé pour faire un premier traitement des tweets et explorer via un requêtage distribué.
## Partie Text Processing
 &nbsp;&nbsp;&nbsp;Diverses méthodes de prétraitement de texte sont utilisées par la suite pour préparer les tweets pour la phase machine learning
## Partie Machine Learning 
 &nbsp;&nbsp;&nbsp;En dernier lieu, un modèle de classification de régression logistique est construit, entraîné et évalué. La fonctionnalité d'analyse de sentiment mais également les services de reconnaissance d'entités nommées, token et lemmma et résumé de corpus de texte sont finalement déployés via Streamlit. Streamlit n'est qest ici q'un outil de déploiement et n'est pas un composant esentiel de ce projet.
 ## Application streamlit
 
  ![image](https://user-images.githubusercontent.com/62526508/107960027-641eec80-6fa4-11eb-9f86-67ee2d8085e2.png)
 ## Sentiment analysis
 ![image](https://user-images.githubusercontent.com/62526508/107958666-a0e9e400-6fa2-11eb-8048-46d0fb2221b4.png)
  ## Named Entity
![image](https://user-images.githubusercontent.com/62526508/107958787-d262af80-6fa2-11eb-879e-08061a0a4610.png)
 ## Token & Lemma 
![image](https://user-images.githubusercontent.com/62526508/107958702-b19a5a00-6fa2-11eb-8ff2-984af9de07fd.png)

 
