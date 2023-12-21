from sonybraviaremote import TV, TVConfig
import tkinter as tk

def on_auth():
    return input('Pincode: ')

# Configure and connect to the TV
config = TVConfig('192.168.1.183', 'Sony Bravia')
tv = TV.connect(config, on_auth)

# Function to check if the TV is on and send a command
def send_command(command_func):
    if tv.is_on():
        command_func()

# Initialize the main window
root = tk.Tk()
root.title("Sony Bravia Remote")

# Create and place buttons
tk.Button(root, text='Netflix', command=lambda: send_command(tv.netflix)).grid(row=0, column=0)
tk.Button(root, text='Home', command=lambda: send_command(tv.home)).grid(row=0, column=1)
# other buttons for different functionalities

# Volume controls
tk.Button(root, text='Volume Up', command=lambda: send_command(tv.volume_up)).grid(row=1, column=0)
tk.Button(root, text='Volume Down', command=lambda: send_command(tv.volume_down)).grid(row=1, column=1)
# other control buttons like Channel Up/Down, Mute, etc.

# Run the GUI loop
root.mainloop()
