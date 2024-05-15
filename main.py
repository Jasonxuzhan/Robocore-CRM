import login
import index
from ttkbootstrap import *
from ttkbootstrap.constants import *


theme_names = ["sandstone", "united", "lumen", "solar", "superhero", "darkly"]
    

# Main Root
root = Window(themename=theme_names[4])
root.title("Robocore CRM System V1.0")
root.iconbitmap()
root.geometry("1700x800")





if __name__ == "__main__":
    robocore = index.Index_Page(root, user_name="Jason", user_type="Adminstrator")
    root.mainloop()

