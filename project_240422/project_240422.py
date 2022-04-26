import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config
from kivy.uix.textinput import TextInput

Config.set('graphics', 'resizable', True)

class Pos_Size_App(App):

    def build(self):
        # A Relative Layout with a size of (300, 300) is created
        rl = RelativeLayout(size=(10, 20))


        # creating button
        # size of button is 20 % by height and width of layout
        # position is 'center_x':.7, 'center_y':.5
        b1 = Button(size_hint=(.1, .1), pos_hint={'center_x': .7, 'top_y': .5}, text="rehercher")
        #creating label for the name's city
        ar = Label(text="Ville:", size_hint=(.2, .1), pos_hint={'x': 20, 'y': 30})
        name = TextInput(multiline=False, size_hint=(.2, .08), pos_hint={'center_x': .3, 'top_y': .4})



        # adding button to widget
        rl.add_widget(b1)
        rl.add_widget(ar)
        rl.add_widget(name)





        # returning widget
        return rl


# run the App
if __name__ == "__main__":
    Pos_Size_App().run()