import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import threading
import sys
import git
import os

# Import the style module
import guiStyles

# Function to clone the repository
def download_repo():
    repo_url = repo_url_entry.get()
    local_dir = dir_entry_download.get()

    if not repo_url or not local_dir:
        messagebox.showwarning("Input Error", "Please provide both repository URL and directory path.")
        return

    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    try:
        git.Repo.clone_from(repo_url, local_dir)
        messagebox.showinfo("Success", f"Repository cloned to {local_dir}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to clone repository: {str(e)}")

# Function to run the external Python script and update the logs in real-time
def scan_repo(local_dir):
    if not local_dir:
        messagebox.showwarning("Input Error", "Please provide the local directory path.")
        return

    # Start the scanning process in a separate thread to keep the GUI responsive
    threading.Thread(target=run_scan_process, args=(local_dir,), daemon=True).start()

# Function that handles the subprocess and logs the output
def run_scan_process(local_dir):
    try:
        # Clear the output text area
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)

        # Start the subprocess to run the scan
        process = subprocess.Popen(
            [sys.executable, "ReportScan.py", local_dir],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1  # Line-buffered output
        )

        # Read the output from the subprocess in real-time
        for line in iter(process.stdout.readline, ''):
            output_text.insert(tk.END, line)  # Insert log line in the Text widget
            output_text.see(tk.END)  # Scroll to the latest log line
            output_text.update_idletasks()  # Ensure the GUI updates immediately

        process.stdout.close()
        process.wait()

        # Trigger success message in a separate thread to avoid blocking the main thread
        if process.returncode == 0:
            threading.Thread(target=lambda: messagebox.showinfo("Scan Completed", "The scan has been completed successfully."), daemon=True).start()
        else:
            threading.Thread(target=lambda: messagebox.showerror("Error", "An error occurred during scanning."), daemon=True).start()

    except Exception as e:
        threading.Thread(target=lambda: messagebox.showerror("Error", f"Failed to run scan script: {str(e)}"), daemon=True).start()

# Function to browse for a directory
def browse_directory(entry):
    dir_path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, dir_path)

# Main window setup
root = tk.Tk()
root.title("PrivacyScan AI")

# Apply styles from the separate file
guiStyles.apply_styles(root)

# Create Notebook (tabs)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Tab 1: Download and scan a GitHub repository
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Download & Scan Repo')

# Tab 2: Scan a local directory
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Scan Local Repo')

### --- Tab 1: Download GitHub Repo and Scan --- ###

# Repo URL label and entry for Tab 1
tk.Label(tab1, text="Repository URL:").pack(pady=5)
repo_url_entry = ttk.Entry(tab1, width=50)
repo_url_entry.pack(pady=5)

# Directory label and entry for Tab 1
tk.Label(tab1, text="Local Directory:").pack(pady=5)
dir_entry_download = ttk.Entry(tab1, width=50)
dir_entry_download.pack(pady=5)

# Button to browse for directory for Tab 1
browse_btn1 = ttk.Button(tab1, text="Browse", command=lambda: browse_directory(dir_entry_download))
browse_btn1.pack(pady=5)

# Button to download the repository for Tab 1
download_btn = ttk.Button(tab1, text="Download Repository", command=download_repo)
download_btn.pack(pady=5)

# Button to scan the repository for Tab 1
scan_btn1 = ttk.Button(tab1, text="Scan Repository", command=lambda: scan_repo(dir_entry_download.get()))
scan_btn1.pack(pady=20)

# Apply hover effect on the buttons
guiStyles.apply_button_hover_effect(download_btn)
guiStyles.apply_button_hover_effect(scan_btn1)

### --- Tab 2: Scan Local Directory --- ###

# Directory label and entry for Tab 2
tk.Label(tab2, text="Local Directory:").pack(pady=5)
dir_entry_scan = ttk.Entry(tab2, width=50)
dir_entry_scan.pack(pady=5)

# Button to browse for directory for Tab 2
browse_btn2 = ttk.Button(tab2, text="Browse", command=lambda: browse_directory(dir_entry_scan))
browse_btn2.pack(pady=5)

# Button to scan the repository for Tab 2 (without downloading)
scan_btn2 = ttk.Button(tab2, text="Scan Local Repository", command=lambda: scan_repo(dir_entry_scan.get()))
scan_btn2.pack(pady=20)

# Apply hover effect on buttons
guiStyles.apply_button_hover_effect(browse_btn2)
guiStyles.apply_button_hover_effect(scan_btn2)

### --- Shared Log Output --- ###
# Text widget to display script output (logs) common to both tabs
output_text = tk.Text(root, height=15, width=80)
output_text.pack(pady=10, padx=10)

root.mainloop()