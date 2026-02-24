# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Single-file Python CLI application that fetches and displays current weather data from the OpenWeatherMap API. Users search by US zip code or city name.

## Setup & Running

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 python-weather.py
```

## Architecture

- `python-weather.py` — entire application in one file
  - `get_web_data(zip, city)` — builds the API URL and makes the GET request to OpenWeatherMap
  - `display(resp)` — parses JSON response and prints formatted weather data
  - `main()` — interactive loop with menu (zip code / city name / exit)
- Uses OpenWeatherMap `/data/2.5/weather` endpoint with imperial units (Fahrenheit, mph)
- Hardcoded to US-only city/zip lookups
