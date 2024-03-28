import tkinter as tk
from tkinter import ttk

def setup_layout(root):
    # Layout frames
    left_frame = ttk.Frame(root)
    left_frame.pack(side="left", fill="y")

    center_frame = ttk.Frame(root)
    center_frame.pack(side="left", fill="y")

    right_frame = ttk.Frame(root)
    right_frame.pack(side="left", fill="y")

    # Add widgets to the left frame (example)
    available_funds_label = ttk.Label(left_frame, text="Available Funds")
    available_funds_label.pack()

    # ... Add more widgets to frames similarly
