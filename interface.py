import tkinter as tk

# Dropdown menu options
site_options = ["Bay", "A", "B", "C", "D"] # Site

xaxis_options = ["Date", "Dissolved Oxygen", "pH", "Salinity",
                "Secchi Depth", "Water Depth", "Water Temp"] # X-Axis

yaxis_options = ["Date", "Dissolved Oxygen", "pH", "Salinity",
                "Secchi Depth", "Water Depth", "Water Temp"] # Y-Axis ## TEMP ##

## Y-Axis is dynamic to be the same list as xaxis-options minus the selected choice

## MAIN BODY OF WINDOW

window = tk.Tk() # Main window
window.geometry("1200x800") # Make the window bigger
window.columnconfigure(0, weight=3) # Two columns, w/ ratio 3:1 Left-> Right
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1) # Five rows, w/ ratio 1:1:1:1:1 Top -> Bottom
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)

## DROPDOWN MENUS

site_button = tk.StringVar() # Button for site options
site_button.set("Please select a site") # Default Text

site_drop = tk.OptionMenu(window, site_button, *site_options) # Make it a dropdown menu
site_drop.grid(row=0, column=1) # Place it in the ui

xaxis_button = tk.StringVar() # Button for x-param options
xaxis_button.set("Please select a parameter") # Default Text

xaxis_drop = tk.OptionMenu(window, xaxis_button, *xaxis_options) # Make it a dropdown menu
xaxis_drop.grid(row=2, column=1) # Place it in the ui

yaxis_button = tk.StringVar() # Button for y-param options
yaxis_button.set("Please select a parameter") # Default Text

yaxis_drop = tk.OptionMenu(window, yaxis_button, *yaxis_options) # Make it a dropdown menu
yaxis_drop.grid(row=4, column=1) # Place it in the ui

##

window.mainloop() # Run the window
