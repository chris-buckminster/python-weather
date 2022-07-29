"""
Chris Buckminster
CIS245 Final Project - ROUGH DRAFT
weatherITWORKS.py

We will be creating an application to interacts with a webservice in order to obtain data. Your program will use all of the information you’ve learned in the class in order to create a useful application.

Requirements:

- Your program must prompt the user for their city or zip code and request weather forecast data from openweathermap.org. 
- Your program must display the weather information in an READABLE format to the user.
- Ask the user for their zip code or city.
- Use the zip code or city name in order to obtain weather forecast data from: http://openweathermap.org
- Display the weather forecast in a readable format to the user.
- Use comments within the application where appropriate in order to document what the program is doing.
- Use functions including a main function.
- Allow the user to run the program multiple times.
- Validate whether the user entered valid data. If valid data isn’t presented, notify the user.
- Use the Requests library in order to request data from the webservice.
- Use Python 3.
- Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful.

STILL TO DO (based on small # of user testing)

- Be more explicit in user prompts
- Put somewhere in prompts that these are US cities only (Paris, TX, not Paris, France)
- Put a cool box around the weather output
- ...?
"""

import requests # importing the requests library

def get_web_data(zip=None, city=None): # function to call website and fetch data

    baseUrl = "http://api.openweathermap.org/data/2.5/weather?units=imperial" 

    apikey = "4acfc90510c428d87cef423f37188e19" # here is the API key

    if zip is not None: 

        baseUrl += "&zip="+str(zip)+",us" # "US" to select American cities

    else:

        baseUrl += "&q="+str(city)+",us"

    baseUrl += "&appid="+str(apikey) 

    r = requests.get(baseUrl) # actually make the GET request 

    return r # response is returned here

def display(resp):

    if resp.status_code == 200: # successful request yields the following

        data = resp.json()

        print(f"""{data['name']}'s weather:

        Conditions: {data['weather'][0]['description']}

        Wind Speed : {data['wind']['speed']} miles/hr

        Visibility : {data['visibility']} m

        Low temperature : {data['main']['temp_min']} Fahrenheit

        High temperature : {data['main']['temp_max']} Fahrenheit

        """)

    else:

        print("Request Failed, Error: ", resp.status_code)

def main():

    while True: 

        choice = int( # Prompt the user for a selection

            input("Find out the weather!\nHow do you want to search?\n1. By Zip Code\n2. By City Name\n3. Exit\n"))

        if choice == 1: # Zip code block

            try:

                zipCode = int(input("Enter the zip code: "))

                resp = get_web_data(zipCode, None) # Get data

                display(resp) # Display response

            except Exception as ex:

                print("Error: ", ex)
                    
        elif choice == 2: # City name block

            try:

                cityName = input("Enter city name: ")

                resp = get_web_data(None, cityName) # Get data
                
                display(resp) # Display response

            except Exception as ex:
                
                print("Error: ", ex)

        elif choice == 3:

            break

        else:

            print("Invalid Choice. Please try again.\n")

if __name__ == "__main__":

    main()