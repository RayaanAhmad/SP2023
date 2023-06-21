import tkinter as tk

# Dropdown menu options
site_options = ["Bay", "A", "B", "C", "D"] # Site

xaxis_options = ["Date", "Dissolved Oxygen", "pH", "Salinity",
                 "Secchi Depth", "Water Depth", "Water Temp"] # X-Axis
## Y-Axis is dynamic to be the same list as xaxis-options minus the selected choice

window = tk.Tk() # Main window
window.mainloop() # Run the window
