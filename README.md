# python-weather

A Python CLI app that fetches current US weather by zip code or city name using the [OpenWeatherMap API](https://openweathermap.org/).

## Setup

1. Get a free API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up)
2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Set your API key:
   ```bash
   export OPENWEATHER_API_KEY=your_key_here
   ```

## Usage

```bash
python3 python-weather.py
```

You'll be prompted to search by zip code or city name. The app displays current conditions, wind speed, visibility, and temperature range in Fahrenheit.
