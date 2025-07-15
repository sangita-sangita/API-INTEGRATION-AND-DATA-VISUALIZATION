# API-INTEGRATION-AND-DATA-VISUALIZATION
COMPANY NAME:CODTECH IT SOLUTIONS
NAME : SANGITA KUMARI
INTERN ID: CTO6DF1191
DOMAIN:PYTHON PROGRAMMING
DURATION:6 WEEKS
MENTOR:NEELA SANTHOSH




Weather Dashboard with Python, Requests, and Seaborn

This project demonstrates how to build a simple weather dashboard using the OpenWeatherMap API, Python's requests library, and data visualization with matplotlib and seaborn. The dashboard displays the current temperatures of various global cities in a visually intuitive bar chart.

📌 Project Overview
The goal of this project is to:

* Fetch real-time weather data for a list of cities using the OpenWeatherMap API.

* Extract and process temperature data.

* Visualize the data using a bar chart for quick and clear comparisons.

* This type of application is useful for understanding real-time temperature patterns across different geographical locations and can be extended for more detailed weather analytics.

🧰 Technologies Used
Python 3

* Requests: For making HTTP requests to the OpenWeatherMap API.

* Matplotlib: For creating plots and visualizations.

* Seaborn: A visualization library based on matplotlib for enhanced aesthetics.

🗺️ Cities Covered
The following cities are included in the dashboard:

* New York

* London

* Tokyo

* Delhi

* Sydney

* Cape Town

* Ramgarh

* Ranchi

These were chosen to represent a variety of climates and continents.

🔧 How It Works
* API Configuration:
The script starts by defining the OpenWeatherMap API endpoint and your API key. The units=metric parameter ensures that temperatures are returned in Celsius.

* Data Collection:The script loops through a predefined list of cities and sends individual requests for each city’s current weather data. On a successful response, the current temperature is extracted and stored.

* Error Handling:
If a city’s data cannot be fetched, a relevant error message is printed.

* Visualization:
After collecting data, the script uses Seaborn and Matplotlib to create a bar chart showing the current temperature in each city. The colors used (coolwarm palette) intuitively represent the temperature range, from cool blues to warm reds.

* Output:
The final chart is displayed and saved as weather_dashboard.png for future reference or sharing.

🖼️ Example Output
The bar chart shows city names on the x-axis and temperatures in Celsius on the y-axis, with each bar color-coded according to temperature. It provides a quick visual insight into temperature variations across regions.

🚀 How to Run
* Clone this repository or copy the script into your Python environment.

* Make sure the required libraries are installed:

* bash
Copy code
pip install requests matplotlib seaborn
Replace the placeholder API key (API_KEY) with your own OpenWeatherMap API key.

* Run the script:

* bash
Copy code
python weather_dashboard.py
View the generated weather_dashboard.png image or check the plotted chart on screen.

📈 Future Improvements
* Add humidity, wind speed, or weather descriptions.

* Include support for hourly or 5-day forecasts.

* Make the list of cities configurable via a file or user input.

* Build a web-based dashboard using Flask or Streamlit.

📬 License
This project is open for educational and non-commercial use. Attribution appreciated if shared publicly.
