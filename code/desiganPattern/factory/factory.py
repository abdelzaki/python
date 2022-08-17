"""
Factory design pattern to decouple object creation from object usage
"""
import filecmp
import json
from typing import Dict
import xml.etree.ElementTree as etree
import os


class JsonDataExtractor():
    def __init__(self, filePath) -> None:
        self.data: Dict = dict()
        with open(filePath, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsedData(self):
        return self.data


class XMLDataExtactor():
    def __init__(self, filePath: str) -> None:
        self.tree = etree.parse(filePath)

    @property
    def parsedData(self):
        return self.tree


def dataExtractionFactory(filePath: str):
    if filePath.endswith("json"):
        extractor = JsonDataExtractor
    elif filePath.endswith("xml"):
        extractor = XMLDataExtactor
    return extractor(filePath)


# json factory
path = os.path.dirname(__file__)
path = os.path.join(path, "moives.json")
jsonObj = dataExtractionFactory(path)
jsonData = jsonObj.parsedData
for data in jsonData:
    print(data.get("year"))

# xml factory
path = os.path.dirname(__file__)
path = os.path.join(path, "person.xml")
xmlObj = dataExtractionFactory(path)
xmlData = xmlObj.parsedData
liars = xmlData.findall(f".//person[lastName='Liar']")
for liar in liars:
    firstname = liar.find('firstName').text
    print(f'first name: {firstname}')
    lastname = liar.find('lastName').text
    print(f'last name: {lastname}')