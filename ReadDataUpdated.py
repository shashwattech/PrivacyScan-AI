import os
import requests
import json
import re
import sys

# OpenAI API configurations
API_KEY = "9d5bcffba65648fcafc63d8a95a06c83"  # Replace with your actual API key
ENDPOINT = "https://sdk-team-opnai-eus-poc.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2023-03-15-preview"

def is_not_code_file(filename):
    _, file_extension = os.path.splitext(filename)
    
    if file_extension not in ['.java', '.cpp', '.py', '.go']:
        return True 
    else:
        return False

# Function to scan files in a directory
def scan_folder_for_pii(directory):
    pii_report = []
    
    # Walk through the folder and its subfolders
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Skip binary files
            if is_not_code_file(file_path):
                print(f"Skipping binary file: {file_name}")
                continue

            # Open and read the content of the file
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                    print(f"Reading the file:: {file_name}")
            except UnicodeDecodeError:
                # Handle files that cannot be read as UTF-8 by trying another encoding or skipping
                try:
                    with open(file_path, 'r', encoding='ISO-8859-1') as file:
                        print(f"Reading the file after decrypting:: {file_name}")
                        file_content = file.read()
                except Exception as e:
                    print(f"Error reading file {file_name}: {str(e)}")
                    continue  # Skip the file if it can't be read

            # Check for PII in the file content
            pii_data = check_for_pii(file_content, file_name)
            if pii_data:
                pii_report.append({
                    'file': file_name,
                    'pii_detected': pii_data
                })

    # Generate PII report
    generate_report(pii_report)

def check_for_pii(file_content, file_name):
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY
    }

    data = {
    "messages": [
        {
            "role": "user", 
            "content": (
                f"You are given a file containing code: {file_content}. Your task is to scan the file for any instances where Personal Identifiable Information (PII) is shared with third-party entities. The PII data you need to check includes the following fields:\n\n"
                "PHONE_NUMBER\n"
                "NAME\n"
                "EMAIL_ADDRESS\n"
                "DATE_OF_BIRTH\n\n"
                "The goal is to identify sections of the code where these PII fields are being shared with external or third-party systems (e.g., APIs, external services, logging systems, etc.).\n\n"
                "For each identified instance, return a JSON response in the following format:\n\n"
                '{\n'
                '  "line_number": "<line number where PII is being shared>",\n'
                '  "pii_type": "<type of PII (PHONE_NUMBER, NAME, EMAIL_ADDRESS, DATE_OF_BIRTH)>",\n'
                '  "third_party": "<name or identifier of the third-party system (API, external service, etc.)>",\n'
                '}\n\n'
                "The JSON response should include all instances of PII data being shared with third parties. If no PII sharing is found, return an empty JSON array ([]).\n\n"
                "Important: Do not return any output other than the JSON response."
            )
        }
    ],
    "max_tokens": 1000,
    "temperature": 0.3  # Lower temperature for more deterministic output
}


    response = requests.post(ENDPOINT, headers=headers, json=data)

    if response.status_code == 200:
        try:
            # Extract PII-related information from the response
            result = response.json()
            pii_data = result['choices'][0]['message']['content']
            print(pii_data)
            json_pattern = r'\{.*?\}'
            # Use re.search to find the first match of the JSON object
            match = re.search(json_pattern, pii_data, re.DOTALL)

            if match:
                json_str = match.group(0)
                
                try:
                    json_data = json.loads(json_str)
                    print("Extracted JSON:", json_data)
                    return json_data
                except json.JSONDecodeError:
                    print("Invalid JSON format.")
            else:
                print("No JSON object found in the string.")
            # extract json from above text where json can exist at any place in the text
            

            
        except (KeyError, IndexError) as e:
            print(f"Error parsing response for file {file_name}: {e}")
    else:
        print(f"API request failed for file {file_name}: {response.status_code} - {response.text}")

    return None

# Function to generate a report for PII data
def generate_report(pii_report):
    report_path = "pii_report.txt"
    
    with open(report_path, 'w', encoding='utf-8') as report_file:
        for report in pii_report:
            report_file.write(f"File: {report['file']}\n")
            report_file.write(f"PII Detected: {report['pii_detected']}\n")
            report_file.write("\n" + "-"*50 + "\n\n")

    print(f"PII report generated at: {report_path}")

# Main function
if __name__ == "__main__":
    arg = sys.argv[1]
    scan_folder_for_pii(arg)