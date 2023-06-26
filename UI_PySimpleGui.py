# windowed weather app 

import PySimpleGUI as sg

#sg.Window(title="Hello World", layout, margins=(500, 300)).read()

#booty = [[sg.Text(text='A Fashionable Weather App',
#   font=('Arial Bold', 16),
#   size=20, expand_x=True,
#   justification='center')],
#   [sg.Image('images/sun.png', size = (100,100))],
#   [sg.Image('images/week_weather.png',
#   expand_x=True)]
#]

booty= [
   [sg.color = 'red', size = (200,215)]
]

window = sg.Window("Basic Layout", booty, size = (715, 500), keep_on_top = True)
while True:
   event, values = window.read()
   print(event, values)
   if event in (None, 'Exit'):
      break
   
window.close()