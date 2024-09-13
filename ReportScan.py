# import os
# import sys
# import requests

# # OpenAI API configurations
# API_KEY = "9d5bcffba65648fcafc63d8a95a06c83"  # Replace with your actual API key
# ENDPOINT = "https://sdk-team-opnai-eus-poc.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2023-03-15-preview"

# def is_not_code_file(filename):
#     _, file_extension = os.path.splitext(filename)
    
#     if file_extension not in ['.java', '.cpp', '.py', '.go']:
#         return True 
#     else:
#         return False

# # Function to scan files in a directory
# def scan_folder_for_pii(directory):
#     pii_report = []
    
#     # Walk through the folder and its subfolders
#     for root, dirs, files in os.walk(directory):
#         for file_name in files:
#             file_path = os.path.join(root, file_name)

#             # Skip binary files
#             if is_not_code_file(file_path):
#                 print(f"Skipping binary file: {file_name}")
#                 continue

#             # Open and read the content of the file
#             try:
#                 with open(file_path, 'r', encoding='utf-8') as file:
#                     file_content = file.read()
#                     print(f"Reading the file:: {file_name}")
#             except UnicodeDecodeError:
#                 # Handle files that cannot be read as UTF-8 by trying another encoding or skipping
#                 try:
#                     with open(file_path, 'r', encoding='ISO-8859-1') as file:
#                         print(f"Reading the file after decrypting:: {file_name}")
#                         file_content = file.read()
#                 except Exception as e:
#                     print(f"Error reading file {file_name}: {str(e)}")
#                     continue  # Skip the file if it can't be read

#             # Check for PII in the file content
#             pii_data = check_for_pii(file_content, file_name)
#             if pii_data:
#                 pii_report.append({
#                     'file': file_name,
#                     'pii_detected': pii_data
#                 })

#     # Generate PII report
#     generate_report(pii_report)

# def check_for_pii(file_content, file_name):
#     headers = {
#         "Content-Type": "application/json",
#         "api-key": API_KEY
#     }

#     data = {
#         "messages": [
#             {
#                 "role": "user", 
#                 "content": f"""
# You are given a file containing code: {file_content}. Your task is to scan the file for any instances where Personal Identifiable Information (PII) is shared with third-party entities. The PII data you need to check includes the following fields:

# - PHONE_NUMBER
# - NAME
# - EMAIL_ADDRESS
# - DATE_OF_BIRTH

# The goal is to identify sections of the code where these PII fields are being shared with external or third-party systems (e.g., APIs, external services, logging systems, etc.).

# For each identified instance, return a JSON response in the following format:
# - line_number: The line number where PII is being shared.
# - pii_type: The type of PII (e.g., "PHONE_NUMBER", "EMAIL_ADDRESS", etc.).
# - third_party: The name or identifier of the third party (e.g., external API name, logging service).
# - context: A brief snippet of the code where the sharing occurs.

# The JSON response should include all instances of PII data being shared with third parties. If no PII sharing is found, return an empty JSON array.
#                 """
#             }
#         ],
#         "max_tokens": 1000,
#         "temperature": 0.3  # Lower temperature for more deterministic output
#     }

#     response = requests.post(ENDPOINT, headers=headers, json=data)

#     if response.status_code == 200:
#         try:
#             # Extract PII-related information from the response
#             result = response.json()
#             pii_data = result['choices'][0]['message']['content']
#             return pii_data
#         except (KeyError, IndexError) as e:
#             print(f"Error parsing response for file {file_name}: {e}")
#     else:
#         print(f"API request failed for file {file_name}: {response.status_code} - {response.text}")

#     return None

# # Function to generate a report for PII data
# def generate_report(pii_report):
#     report_path = "pii_report.txt"
    
#     with open(report_path, 'w', encoding='utf-8') as report_file:
#         for report in pii_report:
#             report_file.write(f"File: {report['file']}\n")
#             report_file.write(f"PII Detected: {report['pii_detected']}\n")
#             report_file.write("\n" + "-"*50 + "\n\n")

#     print(f"PII report generated at: {report_path}")

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python scan_script.py <directory>")
#         sys.exit(1)

#     folder_path = sys.argv[1]
#     scan_folder_for_pii(folder_path)

import os
import sys
import requests
import time

# OpenAI API configurations
API_KEY = "9d5bcffba65648fcafc63d8a95a06c83"  # Replace with your actual API key
ENDPOINT = "https://sdk-team-opnai-eus-poc.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2023-03-15-preview"

def is_not_code_file(filename):
    _, file_extension = os.path.splitext(filename)
    
    if file_extension not in ['.java', '.cpp', '.py', '.go', '.txt']:
        return True 
    else:
        return False

# Function to scan files in a directory
def scan_folder_for_pii(directory):
    pii_report = []
    
    print(f"Starting scan in directory: {directory}", flush=True)
    
    # Walk through the folder and its subfolders
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Skip binary files
            if is_not_code_file(file_path):
                print(f"Skipping binary file: {file_name}", flush=True)
                time.sleep(2)  # Simulate time spent scanning a file
                continue

            # Open and read the content of the file
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                    print(f"Reading the file:: {file_name}", flush=True)
                    time.sleep(2)  # Simulate time spent scanning a file
            except UnicodeDecodeError:
                # Handle files that cannot be read as UTF-8 by trying another encoding or skipping
                try:
                    with open(file_path, 'r', encoding='ISO-8859-1') as file:
                        print(f"Reading the file after decrypting:: {file_name}", flush=True)
                        time.sleep(2)  # Simulate time spent scanning a file
                        file_content = file.read()
                except Exception as e:
                    print(f"Error reading file {file_name}: {str(e)}", flush=True)
                    time.sleep(2)  # Simulate time spent scanning a file
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
                "content": f"""
You are given a file containing code: {file_content}. Your task is to scan the file for any instances where Personal Identifiable Information (PII) is shared with third-party entities. The PII data you need to check includes the following fields:

- PHONE_NUMBER
- NAME
- EMAIL_ADDRESS
- DATE_OF_BIRTH

The goal is to identify sections of the code where these PII fields are being shared with external or third-party systems (e.g., APIs, external services, logging systems, etc.).

For each identified instance, return a JSON response in the following format:
- line_number: The line number where PII is being shared.
- pii_type: The type of PII (e.g., "PHONE_NUMBER", "EMAIL_ADDRESS", etc.).
- third_party: The name or identifier of the third party (e.g., external API name, logging service).
- context: A brief snippet of the code where the sharing occurs.

The JSON response should include all instances of PII data being shared with third parties. If no PII sharing is found, return an empty JSON array.
                """
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
            return pii_data
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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scan_script.py <directory>")
        sys.exit(1)

    folder_path = sys.argv[1]
    scan_folder_for_pii(folder_path)