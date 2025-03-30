from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    output_text = StringProperty("0.0")
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        miles = self.get_validated_miles()
        result = miles * MILES_TO_KM
        self.root.ids.output_label.text = f"{result:.3f}"

    def handle_increment(self, change):
        """
        handle up/down button press, update the text input with new value, call calculation function
        :param change: the amount to change
        """
        miles = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()

    def get_validated_miles(self):
        """
        get text input from text entry widget, convert to float
        :return: 0 if error, float version of text if valid
        """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()