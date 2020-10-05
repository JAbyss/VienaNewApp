from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.core.window import Window

Window.size = (382, 675)


class Frame(GridLayout):
    def maini(self):
        print(self.ids['cardi'].pos)
    pass


class MyApp(MDApp):

    title = 'Foggy Skies'

    def build(self):
        self.theme_cls.theme_style = 'Light'
        return Frame()


if __name__ == '__main__':
    MyApp().run()
