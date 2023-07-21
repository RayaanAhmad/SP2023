import os
import tkinter as tk
from PIL import ImageTk, Image
import analyze

# DROPDOWN MENUS
site_options = ["Bay", "A", "B", "C", "D"] # Site

xaxis_options = ["Date", "Dissolved Oxygen", "pH", "Salinity",
                "Secchi Depth", "Water Depth", "Water Temp"] # X-Axis

yaxis_options = ["Date", "Dissolved Oxygen", "pH", "Salinity",
                "Secchi Depth", "Water Depth", "Water Temp"] # Y-Axis ## TEMP ##
# Y-Axis is dynamic to be the same list as xaxis-options minus the selected choice

png_name = "compare.png"

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

img = Image.open(png_name) # Create image
img = img.resize((900, 600)) # Resize the image
img = ImageTk.PhotoImage(img) # Make it into a photoimage to be added to window

img_label = tk.Label(window, image=img)
img_label.grid(row=0, column=0, rowspan=5) # Have it fill column 1 and all rows

## UPDATE + VARS

option_to_title = { # Adds labels to param to be called in DF
    "Date" : "Read_Date",
    "Dissolved Oxygen" : "Dissolved Oxygen (mg/L)",
    "pH" : "pH (standard units)",
    "Salinity" : "Salinity (ppt)",
    "Secchi Depth" : "Secchi Depth (m)",
    "Water Depth" : "Water Depth (m)",
    "Water Temp" : "Water Temp (?C)"
}

site_param = None
xaxis_param = None
yaxis_param = None


# Returns the name of the png we need
# @ Param : NONE
# @ Returns : string - Name of the png_file
#             string - Bad file read
def get_png_name():
    dirr = os.getcwd() # Get the current directory we are in
    for file in os.listdir(dirr): # Get the PNG File
        if file.endswith(".png"):
            return file
    return "No Images"


# Updates site_param variable
# @ Param: change_site - new site location
# @ Returns: NONE
def new_site(change_site):
    global site_param
    site_param = change_site
    update()
    return


# Update xaxis_param variable
# @ Param: change_x - new xaxis param
# @ Returns: NONE
def new_xaxis(change_x):
    global xaxis_param
    xaxis_param = change_x
    update()
    return

# Update yaxis_param variable
# @ Param: change_y - new yaxis param
# @ Returns: NONE
def new_yaxis(change_y):
    global yaxis_param
    yaxis_param = change_y
    update()
    return


# Checks that params are filled
# @ Param : NONE
# @ Returns: boolean - False is any is none, True if all are not None
def params_filled():
    if (site_param is None) or (xaxis_param is None) or (yaxis_param is None):
        return False
    return True

# Takes in new button values and updates the image
def update():
    # Make Sure Params Are Filled #
    if not params_filled(): # Don't change anything
        return

    # Get New DF #
    # Delete Old Image #
    # Set New Image #
    pass
##

window.mainloop() # Run the window

