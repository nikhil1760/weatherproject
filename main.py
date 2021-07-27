# install the following the modules requests,tkinter
#We can use command like pip install module_name
#we use requests for json files
#tkinter for gui
import tkinter as tk,requests
def getWeather(canvas):
    city=textfield.get()
    api_key = '0ef6eb038d2503d71c313bde7c31a0e7'
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    #create variables to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    f='Description:  '+weather_desc
    g='temperature : '+str(temp_city)+' Celsius'+'\n'+'humidity  :'+str(hmdt)+'%'+'\n'+'wind speed :'+str(wind_spd)+'Km/h'+'\n'
    label1.config(text=f)
    label2.config(text=g)
canvas=tk.Tk() #Toplevel widget of Tk which represents mostly the main window of an application.
canvas.geometry("600x500") #Set geometry to NEWGEOMETRY of the form
canvas.title('Weather App')  # gives title
#fonts
f=('poppins',15,'bold')
t=('poppins',30,'bold')
textfield=tk.Entry(canvas,justify='center',font=t) #Construct an entry widget with the parent MASTER.

textfield.pack(pady=20) #Pack a widget in the parent widget

textfield.focus() #Direct input focus to this widget.

textfield.bind('<Return>',getWeather)

label1=tk.Label(canvas,font=t) #Construct a label widget with the parent MASTER.

label1.pack()
label2 = tk.Label(canvas,font=f) #Construct a label widget with the parent MASTER.

label2.pack()
canvas.mainloop()
