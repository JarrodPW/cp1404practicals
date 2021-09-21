"""
Write a GUI program that converts miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKilometresConversionApp(App):
    """MilesToKilometresConversionApp is a Kivy App for converting miles to kilometres."""
    km_output = StringProperty()

    def build(self):
        """Build the Kivy app from kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle calculation and output the result to the label."""
        value = self.get_miles()
        result = value * MILES_TO_KM
        self.km_output = str(result)

    def handle_change(self, amount):
        """Handle up/down button press and update the text input with new value."""
        value = self.get_miles() + amount
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_miles(self):
        """Get miles from user input, with exception handling."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKilometresConversionApp().run()
