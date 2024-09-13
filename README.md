# PrivacyScan AI

## Overview

PrivacyScan AI is a tool designed to scan repositories and directories for potential personal identifiable information (PII) sharing. It combines a graphical user interface with LLM capabilities to detect and report instances of sensitive data exposure.

## Features

- Clone and scan GitHub repositories directly from the GUI
- Real-time progress updates during scans
- User-friendly interface with tabbed navigation
- Automatic detection of various types of PII including phone numbers, names, email addresses, and dates of birth

## Installation

To use PrivacyScan AI, you'll need to have Python installed on your system. The recommended way to install the required dependencies is via pip:
pip install -r requirements.txt


Additionally, you'll need to obtain an OpenAI API key for the PII detection functionality. Please replace API_KEY in scanner.py with your actual API key before using the tool.

## Usage

### Command-line Interface

You can run the scan using the command-line interface:

python download-repo.py <repository-url>


This will clone the specified repository and perform a scan.

### Graphical User Interface

Alternatively, you can use the graphical user interface:

1. Run the frontend application:
python frontend.py

2. Choose between scanning a GitHub repository or a local directory.

3. Enter the required details and click "Download Repository" or "Scan Local Directory".

4. Wait for the scan to complete and view the results in the log window.

## How It Works

1. The download-repo.py script handles cloning repositories from GitHub URLs.
2. The scanner.py module contains the core scanning logic, utilizing OpenAI's API to detect PII.
3. The tkinterfrontend.py provides a graphical interface for users to interact with the tool.
4. The frontend.py script combines the functionality of download-repo.py and tkinterfrontend.py.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or issues.