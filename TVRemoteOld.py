from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.image import AsyncImage
from kivy.clock import Clock
from PIL import Image

# Replace with your sonybraviaremote library setup
from sonybraviaremote import TV, TVConfig

def on_auth():
    return input('Pincode: ')

# config = TVConfig('192.168.1.183', 'Sony Bravia')
# tv = TV.connect(config, on_auth)

def send_command(command_func):
    if tv.is_on():
        command_func()

class RemoteApp(App):
    def build(self):
        # Set the fixed window size
        self.window_width, self.window_height = 350, 1000
        Window.size = (self.window_width, self.window_height)
        Window.resizable = False

        self.layout = FloatLayout(size=(self.window_width, self.window_height))

        # Schedule the setup to occur after the window is fully initialized
        Clock.schedule_once(self.setup_ui)

        return self.layout

    def setup_ui(self, dt):
        # Load the image to get its size and aspect ratio
        image_path = 'remote.jpg'  # Update with the path to your image
        original_image = Image.open(image_path)
        orig_aspect_ratio = original_image.width / original_image.height

        # Calculate the new size to fit the window while maintaining aspect ratio
        if orig_aspect_ratio > (self.window_width / self.window_height):
            # Image is wider than window
            scaled_width = self.window_width
            scaled_height = scaled_width / orig_aspect_ratio
        else:
            # Image is taller than window
            scaled_height = self.window_height
            scaled_width = scaled_height * orig_aspect_ratio

        # Load and add the remote image, scaled to fit the window
        self.img = AsyncImage(source=image_path,
                              allow_stretch=True,
                              keep_ratio=True,  # Maintain aspect ratio
                              size_hint=(None, None),
                              size=(scaled_width, scaled_height),
                              pos=((self.window_width - scaled_width) / 2, (self.window_height - scaled_height) / 2))
        self.layout.add_widget(self.img)

        # Define buttons and their corresponding TV functions with relative positions
        self.buttons = {
            "Netflix": (lambda: send_command(tv.netflix), (0.1, 0.8)),
            "Home": (lambda: send_command(tv.home), (0.1, 0.7)),
            "Volume Up": (lambda: send_command(tv.volume_up), (0.1, 0.6)),
            "Volume Down": (lambda: send_command(tv.volume_down), (0.1, 0.5)),
            # ... more buttons
        }

        self.create_buttons()

    def create_buttons(self):
        # Calculate button positions based on scaled image size
        for name, (action, relative_position) in self.buttons.items():
            scaled_x = (self.window_width - self.img.width) / 2 + relative_position[0] * self.img.width
            scaled_y = (self.window_height - self.img.height) / 2 + relative_position[1] * self.img.height
            btn = Button(text=name, size_hint=(None, None), size=(80, 30),
                         pos=(scaled_x, scaled_y), on_press=action)
            self.layout.add_widget(btn)

if __name__ == '__main__':
    RemoteApp().run()
