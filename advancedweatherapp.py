import requests
import tkinter as tk
from tkinter import messagebox

# Function to fetch weather data from the API
def fetch_weather():
    city = city_entry.get()
    api_key = "YourAPIKey"  # Replace with your OpenWeatherMap API Key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"].capitalize()
            temperature = data["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius
            humidity = data["main"]["humidity"]

            weather_label.config(text=f"Weather: {weather_description}")
            temperature_label.config(text=f"Temperature: {temperature:.2f} °C")
            humidity_label.config(text=f"Humidity: {humidity}%")
        else:
            messagebox.showerror("Error", "City not found. Please try again.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main application window
app = tk.Tk()
app.title("Weather App")

# Create and arrange GUI elements
city_label = tk.Label(app, text="Enter City:")
city_label.pack()
city_entry = tk.Entry(app)
city_entry.pack()
fetch_button = tk.Button(app, text="Fetch Weather", command=fetch_weather)
fetch_button.pack()

weather_label = tk.Label(app, text="")
weather_label.pack()
temperature_label = tk.Label(app, text="")
temperature_label.pack()
humidity_label = tk.Label(app, text="")
humidity_label.pack()

app.mainloop()
