import os
import csv
import json
import pandas as pd
import xml.etree.ElementTree as ET
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Assuming the setup of LangChain as previously discussed
model = ChatOpenAI()
prompt_template = ChatPromptTemplate.from_template("Provide a detailed analysis of the product in German language: {description}")
chain = prompt_template | model

def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

def read_xlsx(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict('records')

def read_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []
    for item in root.findall('.//product'):  # Adjust based on your XML structure
        data.append({
            'name': item.find('name').text,
            'category': item.find('category').text,
            'price': item.find('price').text,
            'description': item.find('description').text,
        })
    return data

def enrich_data(item):
    print("Starting to enrich data for item:", item)
    input_data = {"description": item.get('description', '')}
    try:
        result = chain.invoke(input_data)
        item['description_enriched'] = result.content
        print("Enrichment successful for item.")
    except Exception as e:
        print(f"Error enriching data: {e}")
        item['description_enriched'] = item.get('description', '')
    return item

def process_data(data):
    return [enrich_data(item) for item in data]

def generate_json(data):
    return json.dumps(data, indent=4)

def main():
    base_path = "./CSV1"
    for filename in os.listdir(base_path):
        if filename.endswith(('.xlsx', '.xml', '.csv')):
            full_path = os.path.join(base_path, filename)
            print(f"Processing {filename}...")
            if filename.endswith('.xlsx'):
                data = read_xlsx(full_path)
            elif filename.endswith('.xml'):
                data = read_xml(full_path)
            elif filename.endswith('.csv'):
                data = read_csv(full_path)
            else:
                continue  # Skip unsupported file formats
            
            processed_data = process_data(data)
            json_output = generate_json(processed_data)
            
            # Optional: Save the JSON output to a file
            json_filename = os.path.splitext(filename)[0] + ".json"
            with open(os.path.join(base_path, json_filename), 'w', encoding='utf-8') as f:
                f.write(json_output)
            print(f"Processed and saved data for {filename} as {json_filename}")

if __name__ == "__main__":
    main()


