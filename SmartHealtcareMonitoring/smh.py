import random
import time
import pandas as pd


# Function to simulate IoT sensor data
def generate_iot_data(samples=50):
    """
    Generates simulated IoT sensor data including temperature, humidity, and air quality index.
   
    Parameters:
    samples (int): Number of data points to generate.
   
    Returns:
    pd.DataFrame: A DataFrame containing simulated IoT data.
    """
    data = []
    for i in range(samples):

        sensor_id = f"Sensor_{i+1}"
        temperature = round(random.uniform(15.0, 40.0), 2)  # Temperature in Celsius
        humidity = random.randint(30, 90)  # Humidity percentage
        air_quality = random.randint(30, 250)  # AQI Index
        co2_level = random.randint(300, 600)  # CO2 levels in parts per million
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')  # Current timestamp
       
        data.append([sensor_id, temperature, humidity, air_quality, co2_level, timestamp])
        time.sleep(2)  # Simulate real-time data collection # Changes data collection interval to every 2 seconds

   
    return pd.DataFrame(data, columns=["Sensor ID", "Temperature (°C)", "Humidity (%)", "Air Quality Index (AQI)", "CO2 Level", "Timestamp"])


# Generate and display simulated IoT data
iot_data = generate_iot_data(50)
print(iot_data)

iot_data.to_csv("iot_data.csv", index=False)