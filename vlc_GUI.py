# coding:utf-8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from kivy.lang.builder import Builder

Builder.load_string('''
<MainScreen>:
    orientation: "vertical"
    Button:
        text: "hello"
    Button:
        text: "everyone"
    
    
    Slider:
        id:vol_bar
        max:  100
        value:  0
        on_value:root.volume_change(self.value)
    
''')

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MainApp(App):
    def build(self):
        return MainScreen()

if __name__=="__main__":
    MainApp().run()