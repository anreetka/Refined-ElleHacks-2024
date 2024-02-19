import csv
import os
from pymongo import MongoClient

#Setting up MongoDB server
mongo_uri = os.environ.get('MONGO_URI')

client = MongoClient(mongo_uri)
db = client['CSV-Shelter-Stop-data']
collection = db['Shelter-longitude-latitude']

csv_file_path = "staticFiles/Transit-Shelter-Data.csv"

def collect_coordinates_bus_shelter(csv_file_path):
    coordinates = []
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            geometry = eval(row['geometry'])
            if 'coordinates' in geometry:
                for coordinate in geometry['coordinates']:
                    if len(coordinate) == 2:
                        coordinates.append([coordinate[1], coordinate[0]])
    return coordinates


def insertDataInDatabase(coordinate):
    collection.insert_one({"longitude": coordinate[1], "latitude": coordinate[0]})
    return True

def extractDataFromDatabase():
    combined_columns = []

    cursor = collection.find()

    for document in cursor:
        document_columns = []

        longitude = document.get('longitude', None)
        latitude = document.get('latitude', None)

        document_columns.append(longitude)
        document_columns.append(latitude)

        combined_columns.append(document_columns)
    return combined_columns
