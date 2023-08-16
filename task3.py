import requests
import tkinter as tk
from tkinter import messagebox

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast App")
        self.root.geometry("300x300")
        self.root.configure(bg="#f0f0f0")

        heading_label = tk.Label(root, text="Welcome to My App!", font=("Helvetica", 16, "bold"), fg="red")
        heading_label.pack(pady=10)

        self.city_label = tk.Label(root, text="Enter City:", font=("Helvetica", 12))
        self.city_label.pack(pady=10)

        self.city_entry = tk.Entry(root, font=("Helvetica", 12))
        self.city_entry.pack()

        self.submit_button = tk.Button(root, text="Get Weather", command=self.get_weather, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f0f0")
        self.result_label.pack()

    def get_weather(self):
        city = self.city_entry.get()
        weather_data = self.fetch_weather(city)
        if weather_data:
            self.display_weather(weather_data)
        else:
            messagebox.showerror("Error", "City not found")

    def fetch_weather(self, city):
        api_key = "0cee03c8706611dc20089c5f6f055a4e"  
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
                "q": city,
                "appid": api_key,
                "units": "metric"
        }
        response = requests.get(base_url, params=params)
        print(response.json())  
        if response.status_code == 200:
           return response.json()
        else:
           return None


    def display_weather(self, weather_data):
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        description = weather_data["weather"][0]["description"]

        result_text = f"Temperature: {temperature}°C\n"
        result_text += f"Humidity: {humidity}%\n"
        result_text += f"Wind Speed: {wind_speed} m/s\n"
        result_text += f"Description: {description}"

        self.result_label.config(text=result_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
