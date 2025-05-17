import os
import csv
import xml.etree.ElementTree as ET
import logging
from cfg import CONFIG
import time
import datetime

logging.basicConfig(
    level = getattr(logging, CONFIG["LOG_LEVEL"]),
    format = "%(asctime)s - %(levelname)s - %(message)s",
    handlers = [
        logging.StreamHandler(),
        logging.FileHandler(CONFIG["LOG_FILE"], mode='a', encoding='utf-8')
    ]
)

logger = logging.getLogger(__name__)

delimiter_list = [",", ";", ":"]
current_timestamp = str(datetime.datetime.now())


def getCSVfile():
    while True:
        csvpath = input(str("Enter folder path: ")).strip()
        file = input(str("Please enter file CSV file to convert XML: "))
        csvfile = os.path.join(csvpath,file)
        extension = file.split('.')[-1]

        if not extension.lower().endswith("csv"):
            logger.warning("This is not a CSV file. Please entera file ends with csv extension")
            continue
        if not os.path.exists(csvfile):
            logger.warning("File could not find under this folder. Please check it again")
            continue

        logger.info(f"Available delimiters are : {delimiter_list}")
        delimiter = input(str("please select one of these delimiters: "))
        if delimiter not in delimiter_list:
            logger.warning("Invalid delimiter. Please select again")
            continue

        with open(csvfile, newline = '', encoding="utf-8") as f:
            firstline = f.readline()
            if not firstline.strip():
                logger.warning("This CSV file is empty")
                continue
        return csvfile, delimiter

def readCSVfile(csvfile,delimiter):
    try:
        with open(csvfile, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter = delimiter)
            rows = list(reader)
            logger.info("File is opened and reading...")
            return rows

    except Exception as e:
        logger.warning("Error reading file")

def createXMLfile(rows, current_timestamp):
    xml_mapping = {
        "Login email": "loginEmail",
        "Identifier": "identifier",
        "One-time password": "oneTimePassword",
        "Recovery code": "recoveryCode",
        "First name": "firstName",
        "Last name": "lastName",
        "Department": "department",
        "location": "location"
    }

    #Create the XML root element
    root = ET.Element("users", creation = current_timestamp)

    for row in rows:
        user = ET.SubElement(root, "user", type="full")
        for csv_key, xml_tag in xml_mapping.items():
            tag = ET.SubElement(user, xml_tag)
            tag.text = row.get(csv_key, "").strip()

    tree = ET.ElementTree(root)
    textfile = CONFIG["OUTPUT_NAME"]
    tree.write(textfile, encoding="utf-8", xml_declaration=True)   
    logger.info(f"CSV file successfully written in {textfile}")     


if __name__ == "__main__":
    csvfile, delimiter = getCSVfile()
    rows = readCSVfile(csvfile, delimiter)
    if rows:
        createXMLfile(rows, current_timestamp)
        logger.info("XML conversion completed successfully 🎉")
