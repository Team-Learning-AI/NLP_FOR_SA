###############################################
#Script to connect and create on mongo db atlas
###############################################

#Connect to cluster and database 
from pymongo import MongoClient
connection_string = "mongodb+srv:#INSERT CREDENTIALS HERE#"
client = MongoClient(connection_string)


#Create database and collection
db = client['#INSERT DB NAME HERE#']
new_col = db.create_collection('#INSERT COLLECTION NAME HERE#')
#mongodb can show error if user tries to create an empty collection
