# Task 3 Weather App - CITS9786 Dasari Vanaja
import tkinter as tk
from tkinter import messagebox
import requests
def get_weather():
    city = city_entry.get()
    try:
        url = f"https://wttr.in/{city}?format=j1"
        res = requests.get(url).json()
        curr = res['current_condition'][0]
        result_label.config(text=f"City: {city}\nTemp: {curr['temp_C']}C\n{curr['weatherDesc'][0]['value']}\nHumidity: {curr['humidity']}%\nWind: {curr['windspeedKmph']} km/h")
    except Exception as e:
        messagebox.showerror("Error", str(e))
root = tk.Tk()
root.title("Weather App CITS9786")
root.geometry("400x350")
root.config(bg="#87CEEB")
tk.Label(root, text="WEATHER APP", font=("Arial", 18, "bold"), bg="#87CEEB").pack(pady=15)
tk.Label(root, text="Dasari Vanaja CITS9786", bg="#87CEEB").pack()
city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
city_entry.pack(pady=10)
tk.Button(root, text="Get Weather", command=get_weather, bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12), bg="white", padx=20, pady=20)
result_label.pack(pady=10, fill="x", padx=20)
root.mainloop()
