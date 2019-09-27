from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

''' This class provides a LoginScreen for users to Login with their personal Accounts'''

class LoginScreen(GridLayout):

    # Constructor
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        
        self.add_widget(Label(text="Nutzername: "))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
                        
        self.add_widget(Label(text="Passwort:"))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)
        
class SimpleApp(App):
    def build(self):
        return LoginScreen()
    
if __name__ == "__main__":
    SimpleApp().run()
    
