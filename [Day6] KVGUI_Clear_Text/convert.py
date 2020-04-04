from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

Window.size = (500, 50)
class Cleartext(GridLayout):
    def __init__(self, **kwargs):
        super(Cleartext ,self).__init__(**kwargs)
        self.cols = 2
        
        self.input = TextInput(multiline=True, hint_text = "Please enter any text.")
        self.add_widget(self.input)
        
        self.bnt = Button(text = "Clear")
        self.bnt.bind( on_press = self.on_Clear )
        self.add_widget(self.bnt)
    
    def on_Clear(self, obj):
        self.input.text = ""
        print("Success!!")

class MainApp(App):
    def build(self):
        return Cleartext()
    

if __name__ == "__main__":
    app = MainApp()
    app.run()