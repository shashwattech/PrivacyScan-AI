import tkinter as tk
from tkinter import ttk

def apply_styles(root):
    """Apply general styles to the GUI"""

    # Configure the root window (background color)
    root.configure(bg="#f5f6fa")

    # Create a style object
    style = ttk.Style()
    
    # Choose a theme (e.g., 'clam', 'alt', 'default', etc.)
    style.theme_use("clam")

    # Button style
    style.configure("TButton",
                    font=("Helvetica", 12),
                    background="#0984e3",
                    foreground="#ffffff",
                    padding=10)

    # Label style
    style.configure("TLabel",
                    font=("Helvetica", 12),
                    background="#f5f6fa",
                    foreground="#2d3436",
                    padding=5)

    # Entry style
    style.configure("TEntry", padding=5)

    # Notebook tab styles
    style.configure("TNotebook.Tab", font=("Helvetica", 12))

    # Text widget style (though this widget doesn't support ttk styling)
    root.option_add('*TEntry*background', '#dfe6e9')
    root.option_add('*TEntry*foreground', '#2d3436')

    # Frame background (to match the root background)
    style.configure("TFrame", background="#f5f6fa")

def apply_button_hover_effect(button):
    """Apply hover effect to a button"""

    def on_enter(event):
        button.config(background="#74b9ff")

    def on_leave(event):
        button.config(background="#0984e3")

    # Bind hover events
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

