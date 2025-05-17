# CSV-To-XML-with-Python

CSV to XML Data Transformation – Custom Python Script
This Python script transforms CSV data into a structured XML format based on a predefined tag mapping. It is designed to help users convert tabular CSV data (such as user records, login info, or product entries) into a well-formed XML file with clean and readable nodes. The output XML structure can be easily customized to match your own schema.

Prerequisites
Before running the script, make sure you have:
- Python 3.x installed
- Required modules (csv, xml.etree.ElementTree, logging, os, datetime) – all are part of Python’s standard library
- A valid .csv file with headers and data (a sample is included)

 CSV Format Example
 - Login Email, 
 - Identifier, 
 - One-time password, 
 - Recovery code, 
 - First name, 
 - Last name, 
 - Department
   
Destination XML Format (simplified)
![image](https://github.com/user-attachments/assets/bfdb9fd2-c765-40d5-9334-9392c97d9dc2)


You can freely modify the XML root tag, record tag, and attribute mappings within the code.

You will be prompted to:
Enter the folder path [Uploading output.xml…]()

Provide the CSV file name 
Choose a delimiter (e.g. ,, ;, :)
Once processed, the resulting XML will be saved as output.xml

Customization
You can modify:
The xml_mapping dictionary inside createXMLfile() to change tag names
The root tag (<users>) or record tag (<user>)
Add custom attributes like timestamps, types, etc.
Extend the script to handle complex XML schemas (e.g. nested nodes, arrays, etc.)







