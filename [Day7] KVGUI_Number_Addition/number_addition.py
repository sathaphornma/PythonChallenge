from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

Window.size = (400,150)
class addition(GridLayout):
    def __init__(self , **kwargs):
        super(addition ,self).__init__(**kwargs)
        self.cols = 2
        
        self.textA = Label(text = "variable A :")
        self.add_widget(self.textA)
        self.varA = TextInput(multiline=False ,hint_text = "Please enter number var A.")
        self.add_widget(self.varA)
        
        self.textB = Label(text = "variable B :")
        self.add_widget(self.textB)
        self.varB = TextInput(multiline=False ,hint_text = "Please enter number var B.")
        self.add_widget(self.varB)
        
        self.result = Label(text = "")
        self.add_widget(self.result)
        self.cal = Button(text = "Addition")
        self.add_widget(self.cal)
        self.cal.bind( on_press = self.getCal)
        
        self.em = Label(text = "")
        self.add_widget(self.em)
        
        self.cr = Button(text = "Clear")
        self.add_widget(self.cr)
        self.cr.bind( on_press = self.getClear)

    def getCal(self, obj):
        self.sum = int(self.varA.text) + int(self.varB.text)
        self.result.text = str(self.sum)
        
    def getClear(self, obj):
        self.result.text = ""
        self.varA.text = ""
        self.varB.text = ""
        
class MainApp(App):
    def build(self):
        return addition()

if __name__ == "__main__":
    app = MainApp()
    app.run()