import kivy
from kivy.app import App
kivy.require('1.11.1')
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests
import json
import random


class NorrisJokes(BoxLayout):

    def get_joke(self):
        url = 'http://api.icndb.com/jokes/random/'
        data = requests.get(url).json()
        joke = data['value']['joke']
        if '&quot;' in joke:
            self.lbl.text = joke.replace('&quot;', ' ')
        else:
            self.lbl.text = joke



class ChuckApp(App):
    def build(self):
        self.text = 'Chuck Norris Joke Generator'
        return NorrisJokes()


if __name__ == '__main__':
    ChuckApp().run()
