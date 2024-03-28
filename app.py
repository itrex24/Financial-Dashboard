import tkinter as tk
from scripts.dashboard import setup_layout
from scripts.utils import update_data, draw_charts

# Main window setup
root = tk.Tk()
root.title("Financial Dashboard")
root.geometry("1366x768")  # Set this to your preferred size

# Setup the layout using the function from dashboard module
setup_layout(root)

# Call the update and draw functions
update_data()
draw_charts()

# Start the main loop
root.mainloop()

