from sonybraviaremote import TV, TVConfig
import tkinter as tk
from PIL import Image, ImageTk

def on_auth():
    return input('Pincode: ')

config = TVConfig('192.168.1.183', 'Sony Bravia')
tv = TV.connect(config, on_auth)

def send_command(command_func):
    if tv.is_on():
        command_func()

root = tk.Tk()
root.title("Sony Bravia Remote")

# Load the background image
image_path = "remote.jpg"  # Update with the path to your image
original_image = Image.open(image_path)

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the appropriate size to fit the screen
img_aspect_ratio = original_image.width / original_image.height
new_width = min(original_image.width, screen_width)
new_height = int(new_width / img_aspect_ratio)

# If the height is still too tall for the screen, adjust the width again
if new_height > screen_height:
    new_height = min(original_image.height, screen_height)
    new_width = int(new_height * img_aspect_ratio)

# Resize the image using the Lanczos resampling algorithm (previously ANTIALIAS)
resized_image = original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(resized_image)

# Set window size to match the resized image
root.geometry(f"{new_width}x{new_height}")

# Create a label to hold the background image
bg_label = tk.Label(root, image=photo)
bg_label.pack(fill=tk.BOTH, expand=tk.YES)

buttons = {
    "Netflix": (lambda: send_command(tv.netflix), (50, 100)),
    "Home": (lambda: send_command(tv.home), (100, 100)),
    "Volume Up": (lambda: send_command(tv.volume_up), (50, 200)),
    "Volume Down": (lambda: send_command(tv.volume_down), (100, 200)),
    # ... more buttons
}

def create_buttons():
    for name, (action, position) in buttons.items():
        scaled_x = int(position[0] * (new_width / original_image.width))
        scaled_y = int(position[1] * (new_height / original_image.height))
        btn = tk.Button(root, text=name, command=action, bg='white', fg='black')
        btn.place(x=scaled_x, y=scaled_y, width=80, height=30)

create_buttons()

# Run the GUI loop
root.mainloop()
