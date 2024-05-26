import tkinter as tk  # Import the Tkinter library for GUI
import requests  # Import the requests library to make HTTP requests

def fetch_weather():
    city = city_entry.get()  # Get the city name entered by the user
    api_key = "96ee4ceecf30cefaa07a8b9ef4f1cce1"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  # Construct the API request URL
    response = requests.get(url)  # Send a GET request to the OpenWeatherMap API
    weather_data = response.json()  # Convert the response to JSON format

    if weather_data["cod"] == 200:  # Check if the response status code is 200 (OK)
        weather_desc = weather_data["weather"][0]["description"]  # Get the weather description
        temp = weather_data["main"]["temp"]  # Get the temperature
        humidity = weather_data["main"]["humidity"]  # Get the humidity
        wind_speed = weather_data["wind"]["speed"]  # Get the wind speed

        # Update the label with weather information
        result_label.config(text=f"Weather: {weather_desc}\nTemperature: {temp}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s")
    else:
        # If city not found, display an error message
        result_label.config(text="City not found")

# GUI setup
root = tk.Tk()  # Create the main application window
root.title("Weather App")  # Set the title of the window

city_label = tk.Label(root, text="Enter city:")  # Create a label for the city entry field
city_label.pack()  # Add the label to the window

city_entry = tk.Entry(root)  # Create an entry field for the user to enter the city
city_entry.pack()  # Add the entry field to the window

fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)  # Create a button to fetch weather data
fetch_button.pack()  # Add the button to the window

result_label = tk.Label(root, text="")  # Create a label to display weather information
result_label.pack()  # Add the label to the window

root.mainloop()  # Start the GUI event loop
