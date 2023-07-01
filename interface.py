import tkinter as tk


# Dropdown menu options
site_options = ["Bay", "A", "B", "C", "D"] # Site

xaxis_options = ["Date", "Dissolved Oxygen", "pH", "Salinity",
                "Secchi Depth", "Water Depth", "Water Temp"] # X-Axis

## Y-Axis is dynamic to be the same list as xaxis-options minus the selected choice

## MAIN BODY OF WINDOW

window = tk.Tk() # Main window
window.geometry("1200x800") # Make the window bigger

site_button = tk.StringVar() # Button for site options
site_button.set("Please select a site") # Default Text

site_drop = tk.OptionMenu(window, site_button, *site_options) # Make it a dropdown menu
site_drop.pack()

xaxis_button = tk.StringVar() # Button for site options
xaxis_button.set("Please select a parameter") # Default Text

xaxis_drop = tk.OptionMenu(window, xaxis_button, *xaxis_options) # Make it a dropdown menu
xaxis_drop.pack()


window.mainloop() # Run the window
