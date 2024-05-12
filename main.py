import login
import index
from ttkbootstrap import *
from ttkbootstrap.constants import *

theme_name_light = ["sandstone", "united", "lumen" ]
theme_name_dark = ["solar", "superhero", "darkly"]

# Main Root
root = Window(themename=theme_name_dark[1])
root.title("Robocore CRM System V1.0")
root.iconbitmap()
root.geometry("1700x800")





if __name__ == "__main__":
    robocore = index.Index_Page(root, user_name="Jason", user_type="Adminstrator")
    root.mainloop()

