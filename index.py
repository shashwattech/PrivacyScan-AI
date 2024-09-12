import tkinter as tk
from tkinter import ttk

def scan_action(tab_name):
    print(f"Scanner button pressed on {tab_name} tab")

def set_placeholder(entry, placeholder):
    # Insert placeholder text
    entry.insert(0, placeholder)
    entry.config(fg='grey')
    
    def on_click(event):
        # Remove placeholder text on click if it is still there
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg='black')
            
    def on_focusout(event):
        # Restore placeholder text if the entry is empty
        if entry.get() == '':
            set_placeholder(entry, placeholder)
        else:
            entry.config(fg='black')
            
    entry.bind("<FocusIn>", on_click)
    entry.bind("<FocusOut>", on_focusout)

# Create the main window
root = tk.Tk()
root.title("GUI with Tabs")

# Configure the root window to expand
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create a Notebook (tab manager)
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, sticky='nsew')

# Create the first tab
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Local')

# Create the second tab
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='GitHub')

# Add widgets to the first tab
privacy_label1 = tk.Label(tab1, text="PrivacyScan AI", font=("Arial", 18, "bold"), fg="blue")
privacy_label1.grid(row=0, column=0, padx=20, pady=(10, 5), sticky='nsew')

input_label1 = tk.Label(tab1, text="Enter local repository path:", font=("Arial", 12))
input_label1.grid(row=1, column=0, padx=20, pady=(0, 5), sticky='w')

input_box1 = tk.Entry(tab1, borderwidth=2, relief="groove")
set_placeholder(input_box1, "Enter local repository path")
input_box1.grid(row=2, column=0, padx=20, pady=(0, 10), sticky='ew')

scan_button1 = tk.Button(tab1, text="Scan", command=lambda: scan_action("Local"), bg="lightblue", borderwidth=2, relief="raised")
scan_button1.grid(row=3, column=0, padx=20, pady=(5, 10), sticky='ew', ipadx=10, ipady=5)

# Add widgets to the second tab
privacy_label2 = tk.Label(tab2, text="PrivacyScan AI", font=("Arial", 18, "bold"), fg="blue")
privacy_label2.grid(row=0, column=0, padx=20, pady=(10, 5), sticky='nsew')

input_label2 = tk.Label(tab2, text="Enter GitHub repository URL:", font=("Arial", 12))
input_label2.grid(row=1, column=0, padx=20, pady=(0, 5), sticky='w')

input_box2 = tk.Entry(tab2, borderwidth=2, relief="groove")
set_placeholder(input_box2, "Enter GitHub repository URL")
input_box2.grid(row=2, column=0, padx=20, pady=(0, 10), sticky='ew')

scan_button2 = tk.Button(tab2, text="Scan", command=lambda: scan_action("GitHub"), bg="lightblue", borderwidth=2, relief="raised")
scan_button2.grid(row=3, column=0, padx=20, pady=(5, 10), sticky='ew', ipadx=10, ipady=5)

# Configure rows and columns to expand
tab1.grid_rowconfigure(2, weight=1)  # Input box expands
tab1.grid_rowconfigure(3, weight=0)  # Button does not expand
tab1.grid_columnconfigure(0, weight=1)  # Expand horizontally

tab2.grid_rowconfigure(2, weight=1)  # Input box expands
tab2.grid_rowconfigure(3, weight=0)  # Button does not expand
tab2.grid_columnconfigure(0, weight=1)  # Expand horizontally

# Add footer
footer = tk.Label(root, text="Hackathon 2024 | Q2 Software Inc.", font=("Arial", 10), anchor='s')
footer.grid(row=1, column=0, sticky='ew', pady=5)

# Ensure footer expands with window width
root.grid_rowconfigure(1, weight=0)
root.grid_columnconfigure(0, weight=1)

# Run the application
root.mainloop()
