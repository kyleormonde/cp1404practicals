from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Kyle', 'Jeremy', 'Jason', 'Greg']

    def build(self):
        self.title = "Names App"
        self.root = Builder.load_file('very_simple_app.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=str(name))
            self.root.ids.entries_box.add_widget(temp_label)


DynamicWidgetsApp().run()
