import tkinter as tk
from PIL import ImageTk, Image
import analyze

# DROPDOWN MENUS
site_options = ["Bay", "A", "B", "C", "D"] # Site

xaxis_options = ["Date", "Dissolved Oxygen", "pH", "Salinity",
                "Secchi Depth", "Water Depth", "Water Temp"] # X-Axis

yaxis_options = ["Date", "Dissolved Oxygen", "pH", "Salinity",
                "Secchi Depth", "Water Depth", "Water Temp"] # Y-Axis ## TEMP ##

## Y-Axis is dynamic to be the same list as xaxis-options minus the selected choice

## MAIN BODY OF WINDOW

window = tk.Tk() # Main window
window.geometry("1200x800") # Make the window bigger

window.columnconfigure(0, weight=8) # Three columns, w/ ratio 8:1:1 Left-> Right
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(0, weight=1) # Three, w/ ratio 1:1:1 Top -> Bottom
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)


## LABELS

site_label = tk.Label(window, text="Site ID") # Label for SiteID
site_label.grid(row=0, column=1)

x_label = tk.Label(window, text="X-Axis Parameter") # Label for X-Axis
x_label.grid(row=1, column=1)

y_label = tk.Label(window, text="Y-Axis Parameter") # Label for Y-Axis
y_label.grid(row=2, column=1)

## DROPDOWN MENUS

site_button = tk.StringVar() # Button for site options
site_button.set("Please select a site") # Default Text

site_drop = tk.OptionMenu(window, site_button, *site_options) # Make it a dropdown menu
site_drop.grid(row=0, column=2) # Place it in the ui

xaxis_button = tk.StringVar() # Button for x-param options
xaxis_button.set("Please select a parameter") # Default Text

xaxis_drop = tk.OptionMenu(window, xaxis_button, *xaxis_options) # Make it a dropdown menu
xaxis_drop.grid(row=1, column=2) # Place it in the ui

yaxis_button = tk.StringVar() # Button for y-param options
yaxis_button.set("Please select a parameter") # Default Text

yaxis_drop = tk.OptionMenu(window, yaxis_button, *yaxis_options) # Make it a dropdown menu
yaxis_drop.grid(row=2, column=2) # Place it in the ui

## IMAGE OF GRAPH

img = Image.open("compare.png") # Create image
img = img.resize((900, 600)) # Resize the image
img = ImageTk.PhotoImage(img) # Make it into a photoimage to be added to window

img_label = tk.Label(window, image=img)
img_label.grid(row=0, column=0, rowspan=5) # Have it fill column 1 and all rows

## UPDATE + VARS

##

window.mainloop() # Run the window
