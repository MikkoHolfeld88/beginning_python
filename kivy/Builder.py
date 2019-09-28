from kivy.app import App
from kivy.lang import Builder

presentation = Builder.load_file("kv_file_for_builder.kv")

class MainApp(App):
    
    def build(self):
        return presentation

if __name__ == "__main__":
    MainApp().run()
