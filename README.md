# PrivacyScan AI

## Authors

- **Shashwat Srivastava**

## Overview

PrivacyScan AI is a tool designed to scan repositories and directories for potential personal identifiable information (PII) sharing. It combines a graphical user interface with LLM capabilities to detect and report instances of sensitive data exposure.

## Features

- Clone and scan GitHub repositories directly from the GUI  
- Real-time progress updates during scans  
- User-friendly interface with tabbed navigation  
- Automatic detection of various types of PII including phone numbers, names, email addresses, and dates of birth  

## Installation

To use PrivacyScan AI, you'll need to have Python installed on your system. The recommended way to install the required dependencies is via pip:

```bash
pip install -r requirements.txt
```

Additionally:

- **Obtain an OpenAI API key** for the PII detection functionality.  
- **Replace the `API_KEY` in `scanner.py` with your actual key.**  
- **Replace any ChatGPT/OpenAI endpoints in `scanner.py` if using a custom or alternate LLM deployment.**

## Usage

### Command-line Interface

You can run the scan using the command-line interface:

```bash
python download-repo.py <repository-url>
```

This will clone the specified repository and perform a scan.

### Graphical User Interface

Alternatively, you can use the graphical user interface:

1. Run the frontend application:
   ```bash
   python tkinterfrontend.py
   ```
2. Choose between scanning a GitHub repository or a local directory.
3. Enter the required details and click "Scan Local Directory".
4. Wait for the scan to complete and view the results in the log window.
5. View the report by clicking on the **Open Report** button.

## How It Works

1. `download-repo.py` handles cloning repositories from GitHub URLs.  
2. `scanner.py` contains the core scanning logic, utilizing OpenAI's API (or another LLM endpoint) to detect PII.  
3. `tkinterfrontend.py` provides a graphical interface for users to interact with the tool.  
4. `frontend.py` combines the functionality of `download-repo.py` and `tkinterfrontend.py`.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or issues.
