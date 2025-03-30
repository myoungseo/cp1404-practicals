from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana"]

    def build(self):
        self.root = Builder.load_file("dynamic_labels.kv")
        main_layout = self.root.ids.main

        for name in self.names:
            temp_label = Label(text=name)
            main_layout.add_widget(temp_label)
        return self.root

DynamicLabelsApp().run()