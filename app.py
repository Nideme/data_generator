import os
import csv
import json
import pandas as pd
import re
from langchain_openai import ChatOpenAI

# Setup LangChain ChatOpenAI
openai_api_key = "YOUR_OPENAI_KEY"  # Ensure you have set your OpenAI API Key
model = ChatOpenAI(api_key=openai_api_key)



def identify_start_row(file_path):
    start_row = 0
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        for i, row in enumerate(csvfile):
            if "Produkt" in row:  # Adjust based on how products are identified
                start_row = i + 1  # Assuming headers are right before the first product
                break
    return start_row


def read_products_from_csv(file_path, start_row):
    products = []
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for _ in range(start_row):
            next(reader)
        headers = next(reader)  # Assuming the next row contains headers
        for row in reader:
            product = {headers[i]: row[i] for i in range(min(len(headers), len(row)))}
            products.append(product)
    return products



def process_csv_file(file_path):
    start_row = identify_start_row(file_path)
    products = read_products_from_csv(file_path, start_row)
    return products

def generate_prompt(product):
    prompt_parts = [f"{key}: {value}" for key, value in product.items()]
    prompt = "Extract the relevant attributes of the product based on the following details:\n" + "\n".join(prompt_parts)
    return prompt

def parse_response(response):
    # Placeholder for response parsing logic based on your specific needs
    return json.loads(response) if response else {}

def process_products(products):
    processed_products = []
    for product in products:
        prompt = generate_prompt(product)
        messages = [{"role": "user", "content": prompt}]
        try:
            response = model.invoke(messages)
            processed_product = parse_response(response.content)
            processed_products.append(processed_product)
        except Exception as e:
            print(f"Error invoking the model: {e}")
    return processed_products

def main():
    base_path = './CSV1'  # Corrected base path
    output_filename = 'processed_products.json'

    all_products = []
    for filename in os.listdir(base_path):
        if filename.endswith('.csv'):  # Extend conditions for other formats
            full_path = os.path.join(base_path, filename)
            print(f"Processing {filename}...")
            products = process_csv_file(full_path)
            # Assuming process_products function here to send products for OpenAI processing
            all_products.extend(products)  # Change this to processed_products if using OpenAI

    # Save to JSON file
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(all_products, f, indent=4)
    print(f"Successfully processed files and generated {output_filename}")

if __name__ == '__main__':
    main()
