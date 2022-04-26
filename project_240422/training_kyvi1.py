import requests
import datetime as dt
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.image import Image



Builder.load_string(f""" 

#:import utils kivy.utils
<MyGridLayout>
    name:name
    GridLayout:
        cols:1
        size: root.width, root.height
        GridLayout:
            cols:2
            Label:
                pos: 400,30
                text: "Votre ville:"
                size_hint_y:None
                height:15
                size_hint_x:None
                width:200
            
            TextInput:
                pos: 0, 400
                id:name
                multiline:False
                size_hint_y:None
                height:25
                size_hint_x:None
                width:200
                font_size:10
                      
            Label:  
                text: f"km/h"
                pos:20,300       
            Image:
                source: "wind.png"
                
            Label:
                text:f""    
            Image:
                source: "cloud.png"
                pos:100, 200
                multiline:False
                size_hint_y:None
                height:25
                size_hint_x:None
                width:200

        Button:
            text: "Lancer"
            font_size: 15
            on_press: root.press()
            background_color:utils.get_color_from_hex("#fc0303")
            size_hint_y:None
            height:50
            size_hint_x:None
            width:200
            pos:100,10  
""")
class MyGridLayout(Widget):

    name= ObjectProperty(None)

    def press(self):
        name = self.name.text
        #self.add_widget(Label(text=f"hello, {name}, your pizza is {pizza}"))
        #to clear the  output
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        key = "c956f34308cf1ecb933aa5e907a01ac8"
        city = f"{name}"
        lang = "fr"
        url = base_url + "appid=" + key + "&q=" + city + "&lang=" + lang

        def kelvin_to_celsuis_fahrenheit(kelvin):
            celsuis = kelvin - 273.15
            fahrenheit = celsuis * (9 / 5) + 32
            return celsuis, fahrenheit

        response = requests.get(url).json()
        temp_kelvin = response['main']['temp']
        temp_celsius, temp_fahrenheit = kelvin_to_celsuis_fahrenheit(temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsuis_fahrenheit(feels_like_kelvin)
        wind_speed = response['wind']['speed']
        humidity = response['main']['humidity']
        description = response['weather'][0]['description']
        weather1 = response['weather'][0]['main']
        vue_distance = response['visibility']
        nuage_pourcent = response['clouds']['all']
        pression = response['main']['pressure']
        sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
        sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

        self.add_widget(Label(text=f"{wind_speed*3.6:.2f}",
                              pos=(30, 300)))

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()