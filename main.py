from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import random

# Replace with your sonybraviaremote library setup
from sonybraviaremote import TV, TVConfig

from TVRemote import send_command


def generate_random_color():
    while True:
        r = random.randint(0, 1)
        g = random.randint(0, 1)
        b = random.randint(0, 1)
        if (r, g, b) != (0, 0, 0):  # Check if the color is not black
            break
    a = 1  # Random alpha value between 0 and 1
    return (r, g, b, a)


class RemoteApp(App):
    tv = None

    def on_auth(self):
        return input('Pincode: ')

    def connect_to_tv(self, instance):
        # Attempt to connect to the TV when the button is pressed
        try:
            config = TVConfig('192.168.1.183', 'Sony Bravia')
            self.tv = TV.connect(config, self.on_auth)
            self.connect_button.text = 'Connected'
            print("Connected to TV.")
        except Exception as e:
            self.connect_button.text = 'Connect to TV'
            print(f"Could not connect to TV: {e}")

    def send_command(self, command_func):
        # Send a command if the TV is connected
        try:
            if self.tv and self.tv.is_on():
                command_func()
        except Exception as e:
            print(f"Failed to send command: {e}")

    def build(self):
        # Window.size = (1000, 1000)
        # Window.resizable = True

        # Create the main layout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Add a button to connect to the TV
        self.connect_button = Button(
            text="Connect to TV", size_hint_y=None, height=50)
        self.connect_button.bind(on_press=self.connect_to_tv)
        main_layout.add_widget(self.connect_button)

        # Define other buttons with their actions and styles
        other_buttons = {
            "Netflix": {'action': lambda: self.send_command(self.tv.netflix), 'color': (1, 1, 1, 1), 'background_color': (1, 0, 0, 1)},
            "Home": {'action': lambda: self.send_command(self.tv.home), 'color': (1, 1, 1, 1), 'background_color': (0, 0, 1, 1)},
            "Volume +": {'action': lambda: self.send_command(self.tv.volume_up), 'color': (1, 1, 1, 1), 'background_color': (0, 1, 0, 1)},
            "Channel +": {'action': lambda: self.send_command(self.tv.channel_up), 'color': (1, 1, 1, 1), 'background_color': (0, 1, 0, 1)},
            "Volume -": {'action': lambda: self.send_command(self.tv.volume_down), 'color': (1, 1, 1, 1), 'background_color': (1, 0, 0, 1)},
            "Channel -": {'action': lambda: self.send_command(self.tv.channel_down), 'color': (1, 1, 1, 1), 'background_color': (1, 0, 0, 1)},
            # ... more buttons
        }

        # Create and add other buttons to the layout
        other_buttons_layout = GridLayout(cols=2, size_hint_y=None)
        other_buttons_layout.bind(
            minimum_height=other_buttons_layout.setter('height'))
        for name, details in other_buttons.items():
            btn = Button(text=name, color=details['color'], background_normal='',
                         background_color=details['background_color'], size_hint_y=None, height=50,
                         on_press=details['action'])
            other_buttons_layout.add_widget(btn)

        main_layout.add_widget(other_buttons_layout)

        select_buttons = {
            'blank1': {'action': lambda *args: None, 'color': (0, 0, 0, 0), 'background_color': (0, 0, 0, 0)},
            '^': {'action': lambda: send_command(tv.num1), 'color': (0, 0, 0, 1), 'background_color': generate_random_color()},
            'blank2': {'action': lambda *args: None, 'color': (0, 0, 0, 0), 'background_color': (0, 0, 0, 0)},
            '<': {'action': lambda: send_command(tv.num2), 'color': (0, 0, 0, 1), 'background_color': generate_random_color()},
            'Enter': {'action': lambda: send_command(tv.num2), 'color': (0, 0, 0, 1), 'background_color': generate_random_color()},
            '>': {'action': lambda: send_command(tv.num2), 'color': (0, 0, 0, 1), 'background_color': generate_random_color()},
            'blank3': {'action': lambda *args: None, 'color': (0, 0, 0, 0), 'background_color': (0, 0, 0, 0)},
            'v': {'action': lambda: send_command(tv.num2), 'color': (0, 0, 0, 1), 'background_color': generate_random_color()},
            'blank4': {'action': lambda *args: None, 'color': (0, 0, 0, 0), 'background_color': (0, 0, 0, 0)},
        }

        # Create and add select buttons to the layout
        select_layout = GridLayout(cols=3, size_hint_y=None)
        select_layout.bind(minimum_height=select_layout.setter('height'))
        for num, details in select_buttons.items():
            btn = Button(text=num, color=details['color'], background_normal='',
                         background_color=details['background_color'], size_hint_y=None, height=100,
                         on_press=details['action'])
            select_layout.add_widget(btn)

        main_layout.add_widget(select_layout)

        # Define number buttons with their actions and styles
        number_buttons = {
            '1': {'action': lambda: send_command(tv.num1), 'color': (0, 0, 0, 1), 'background_color': generate_random_color()},
            '2': {'action': lambda: send_command(tv.num2), 'color': (0, 0, 0, 1), 'background_color': generate_random_color()},
            '3': {'action': lambda: send_command(tv.num3), 'color': (0, 0, 0, 1), 'background_color': generate_random_color()},
            '4': {'action': lambda: send_command(tv.num4), 'color': (0, 0, 0, 1), 'background_color': generate_random_color()},
            '5': {'action': lambda: send_command(tv.num5), 'color': (0, 0, 0, 1), 'background_color': generate_random_color()},
            '6': {'action': lambda: send_command(tv.num6), 'color': (0, 0, 0, 1), 'background_color': generate_random_color()},
            '7': {'action': lambda: send_command(tv.num7), 'color': (0, 0, 0, 1), 'background_color': generate_random_color()},
            '8': {'action': lambda: send_command(tv.num8), 'color': (0, 0, 0, 1), 'background_color': generate_random_color()},
            '9': {'action': lambda: send_command(tv.num9), 'color': (0, 0, 0, 1), 'background_color': generate_random_color()},
            'blank1': {'action': lambda *args: None, 'color': (0, 0, 0, 0), 'background_color': (0, 0, 0, 0)},
            '0': {'action': lambda: send_command(tv.num0), 'color': (0, 0, 0, 1), 'background_color': generate_random_color()},
            'blank2': {'action': lambda *args: None, 'color': (0, 0, 0, 0), 'background_color': (0, 0, 0, 0)},
        }

        # Create and add number buttons to the layout
        number_layout = GridLayout(cols=3, size_hint_y=None)
        number_layout.bind(minimum_height=number_layout.setter('height'))
        for num, details in number_buttons.items():
            btn = Button(text=num, color=details['color'], background_normal='',
                         background_color=details['background_color'], size_hint_y=None, height=100,
                         on_press=details['action'])
            number_layout.add_widget(btn)

        main_layout.add_widget(number_layout)

        return main_layout


if __name__ == '__main__':
    RemoteApp().run()
