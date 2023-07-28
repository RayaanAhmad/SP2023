import os
import tkinter as tk
from PIL import ImageTk, Image
import analyze

# TO DO LIST:
# 1) Make the graph able to read time (in analyze.py)

## MAIN BODY OF WINDOW

window = tk.Tk() # Main window
window.geometry("1200x800") # Make the window bigger

window.columnconfigure(0, weight=8) # Three columns, w/ ratio 8:1:1 Left-> Right
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(0, weight=5) # Four rows, w/ ratio 5:5:5:1 Top -> Bottom
window.rowconfigure(1, weight=5)
window.rowconfigure(2, weight=5)
window.rowconfigure(3, weight=1)

## LABELS

site_label = tk.Label(window, text="Site ID") # Label for SiteID
site_label.grid(row=0, column=1)

x_label = tk.Label(window, text="X-Axis Parameter") # Label for X-Axis
x_label.grid(row=1, column=1)

y_label = tk.Label(window, text="Y-Axis Parameter") # Label for Y-Axis
y_label.grid(row=2, column=1)

corr_labels = tk.Label(window,font=("Times New Roman", 18), text="") # Label for line of best fit and r^2 value
corr_labels.grid(row=3, column=0)

# Blank image for placeholding
blank_img = ImageTk.PhotoImage( Image.new(mode='RGB', size=(20,20), color="rgb(240,240,240)") )

im_label = tk.Label(window, image=blank_img)
im_label.grid(row=0, column=0, rowspan=5)

## UPDATE + VARS

site_options = ["Bay", "A", "B", "C", "D"] # Site

xaxis_options = ["Date", "Dissolved Oxygen", "pH", "Salinity",
                "Secchi Depth", "Water Depth", "Water Temp"] # X-Axis

yaxis_options = ["Dissolved Oxygen", "pH", "Salinity",
                "Secchi Depth", "Water Depth", "Water Temp"] # Y-Axis

labeler = { # Adds labels to param to be called in DF
    "Date" : "Read_Date",
    "Dissolved Oxygen" : "Dissolved Oxygen (mg/L)",
    "pH" : "pH (standard units)",
    "Salinity" : "Salinity (ppt)",
    "Secchi Depth" : "Secchi Depth (m)",
    "Water Depth" : "Water Depth (m)",
    "Water Temp" : "Water Temp (?C)"
}

# Global variables so easy to modify between functions
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
# @ Param : NONE
# @ Returns: NONE
def update():

    # Updates the global variables
    global site_param
    global xaxis_param
    global yaxis_param
    global window
    global im_label
    global corr_labels

    # Make Sure Params Are Filled And Not Duplicates #
    if (not params_filled()) or (xaxis_param == yaxis_param): # Don't change anything
        return

    # Save the old PNG name #
    old_name = get_png_name()

    # Get New DF #
    site_df = analyze.filter_site(site_param)
    params_df = analyze.pick_two(site_df, labeler[xaxis_param], labeler[yaxis_param])
    new_name, new_corrs, null = analyze.create_graph(params_df, site_param)

    # Delete Old Image IF it is not the same thing #
    if (old_name != "No Images") and (old_name != new_name): # Get rid of the old PNG file
        os.remove(old_name)

    # Set New Image #
    new_img = Image.open(new_name)  # Create image
    new_img = new_img.resize((900, 600))  # Resize the image
    new_img = ImageTk.PhotoImage(new_img)  # Make it into a photoimage to be added to window

    im_label.configure(image=new_img) # Update our image
    im_label.image = new_img

    corr_labels.config(text=new_corrs) # Update the label
    return

## DROPDOWN MENUS

site_button = tk.StringVar() # Button for site options
site_button.set("Please select a site") # Default Text

site_drop = tk.OptionMenu(window, site_button, *site_options, command=new_site) # Make it a dropdown menu
site_drop.grid(row=0, column=2) # Place it in the ui

xaxis_button = tk.StringVar() # Button for x-param options
xaxis_button.set("Please select a parameter") # Default Text

xaxis_drop = tk.OptionMenu(window, xaxis_button, *xaxis_options, command=new_xaxis) # Make it a dropdown menu
xaxis_drop.grid(row=1, column=2) # Place it in the ui

yaxis_button = tk.StringVar() # Button for y-param options
yaxis_button.set("Please select a parameter") # Default Text

yaxis_drop = tk.OptionMenu(window, yaxis_button, *yaxis_options, command=new_yaxis) # Make it a dropdown menu
yaxis_drop.grid(row=2, column=2) # Place it in the ui

## KILL IT

# Makes sure we exit the loop when we close it
# @ Param : NONE
# @ Returns: NONE
def kill():
    window.quit()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", kill) # Checks that we want to kill the window

window.mainloop() # Run the window
