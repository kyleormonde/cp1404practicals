from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesToKilometers(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('m_to_km.kv')
        return self.root

    def handle_calculate(self):
        miles = self.get_validated_miles()
        kilometers = miles * MILES_TO_KM
        self.root.ids.output_label.text = str(kilometers)

    def handle_increment(self, difference):
        increment = self.get_validated_miles() + difference
        self.root.ids.input_miles.text = str(increment)

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKilometers().run()
