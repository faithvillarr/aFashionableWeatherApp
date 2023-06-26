import tkinter as tk
import weatherInfo as wif

### define root - the two big frames
root = tk.Tk()
root.title('A Fashionable Weather App')
root.geometry('900x600')

root.columnconfigure(0, weight = 2)
root.columnconfigure(1, weight = 3)
root.rowconfigure(0, weight = 1)

#make frames
weather = tk.Frame(root)
apparel_sum = tk.Frame(root, background = 'sky blue')
#add to grid
weather.grid(row=0, column=0, sticky='nsew')
apparel_sum.grid(row=0, column=1, sticky='nsew')


### define weather side
#ALWAYS !!!! configure both columns and rows
weather.rowconfigure(0, weight= 4)
weather.rowconfigure(1, weight= 3)
weather.rowconfigure(2, weight= 5)
weather.rowconfigure(3, weight= 1)
weather.columnconfigure(0, weight=1)

#make frames
icon = tk.PhotoImage(file="images/cloud.png")#.resize((100,100))
wea_icon = tk.Label(weather, image = icon)
wea_week = tk.Frame(weather, background = 'blue')
wea_hourly = tk.Frame(weather, background = 'yellow')
wea_date = tk.Frame(weather, background = 'green')

#add to grid
wea_icon.grid(row=0, column=0, sticky='n')
wea_week.grid(row=1, column=0, sticky='nsew')
wea_hourly.grid(row=2, column=0, sticky='nsew')
wea_date.grid(row=3, column=0, sticky='nsew')




root.mainloop()
