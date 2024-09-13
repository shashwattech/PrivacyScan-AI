import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import git
import os
import subprocess
import threading
import sys

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

        # Call the external Python script with the directory path and pipe the output
        process = subprocess.Popen(
            [sys.executable, "ReportScan.py", local_dir],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Read the output from the subprocess in real-time
        for line in iter(process.stdout.readline, ''):
            output_text.insert(tk.END, line)
            output_text.see(tk.END)  # Auto-scroll to the bottom
            output_text.update()  # Ensure the GUI updates in real-time

        process.stdout.close()
        process.wait()

        if process.returncode == 0:
            messagebox.showinfo("Scan Completed", "The scan has been completed successfully.")
        else:
            messagebox.showerror("Error", "An error occurred during scanning.")
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run scan script: {str(e)}")

# Function to browse for a directory
def browse_directory(entry):
    dir_path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, dir_path)

# Main window setup
root = tk.Tk()
root.title("GitHub Repo Cloner and Scanner")

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
repo_url_entry = tk.Entry(tab1, width=50)
repo_url_entry.pack(pady=5)

# Directory label and entry for Tab 1
tk.Label(tab1, text="Local Directory:").pack(pady=5)
dir_entry_download = tk.Entry(tab1, width=50)
dir_entry_download.pack(pady=5)

# Button to browse for directory for Tab 1
browse_btn1 = tk.Button(tab1, text="Browse", command=lambda: browse_directory(dir_entry_download))
browse_btn1.pack(pady=5)

# Button to download the repository for Tab 1
download_btn = tk.Button(tab1, text="Download Repository", command=download_repo)
download_btn.pack(pady=5)

# Button to scan the repository for Tab 1
scan_btn1 = tk.Button(tab1, text="Scan Repository", command=lambda: scan_repo(dir_entry_download.get()))
scan_btn1.pack(pady=20)

### --- Tab 2: Scan Local Directory --- ###

# Directory label and entry for Tab 2
tk.Label(tab2, text="Local Directory:").pack(pady=5)
dir_entry_scan = tk.Entry(tab2, width=50)
dir_entry_scan.pack(pady=5)

# Button to browse for directory for Tab 2
browse_btn2 = tk.Button(tab2, text="Browse", command=lambda: browse_directory(dir_entry_scan))
browse_btn2.pack(pady=5)

# Button to scan the repository for Tab 2 (without downloading)
scan_btn2 = tk.Button(tab2, text="Scan Local Repository", command=lambda: scan_repo(dir_entry_scan.get()))
scan_btn2.pack(pady=20)

### --- Shared Log Output --- ###
# Text widget to display script output (logs) common to both tabs
output_text = tk.Text(root, height=15, width=80)
output_text.pack(pady=10, padx=10)

root.mainloop()