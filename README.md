## Introduction

Welcome to Parapharmacy Finder, an innovative application that allows you to search for the nearest retail location selling over-the-counter (OTC) medications across Italy. Additionally, you can check the availability of your desired product (either SOP or OTP) and plan your trip by adding multiple stops, receiving a precise itinerary.

## Features

- **Product Search:** Easily find the OTC medications you need.
- **Parapharmacy Filtering:** Filter search results to show only parapharmacies in your area.
- **Directions to Arrival:** Get detailed directions to your selected parapharmacy.
- **User-friendly Interface:** Enjoy an intuitive and easy-to-navigate interface.

# Techonologies Used 
- **Flask (FrontEnd) - FastAPI (BackEnd)**
- **HTML**: Used for the structure of the web page.
- **CSS**: Used for the style and layout of the web page.
- **Bootstrap**: CSS library for responsive design and predefined components.
- **Leaflet**: JavaScript library for interactive maps.
- **Leaflet Routing Machine**: Plugin for Leaflet for routing and directions.
- **JavaScript**: Used for the logic and interactivity of the page.
- **Fetch API**: Used to make HTTP requests to retrieve data from a server.
- **OpenStreetMap**: Used for maps and address geocoding via API.
- **Nominatim**: Geocoding service used with OpenStreetMap to convert addresses into geographic coordinates.
- **Bootstrap JS**: JavaScript library for Bootstrap functionalities.

# CSV Datasets Used in the Project

This section outlines the essential datasets to run the project:

- **Parafarmacie.csv:** List of all parapharmacies in Italy.
- **SOP-OTP.csv:** List of all SOP or OTP products that can be sold by parapharmacies.


# Step to run 

## Step 1: Clone the Repository
Open a terminal and clone the repository:

**git clone https://github.com/paolomaizza/LSPD_parapharmacy_finder.git**
**cd LSPD_parapharmacy_finder**

## Step 2: Set Up the Environment
Create and activate a virtual environment to manage dependencies, use the method you prefer.

### Step 2A:  Python Method 

**python3 -m venv**
**python3 -m venv venvv** 
**source venvv/bin/activate**
**pip instore -r backend/requirements.txt**
**pip instore -r frontend/requirements.txt**
**python backend/app/main.py**
**python frontend/app/main.py**

### Step 2B:  Docker Method 

**cd lspd**
**docker-compose up --build**

## Step 3: Access the Application
Open a web browser and navigate to the appropriate URL: **http://localhost:8080**

# Contributing

The Parapharmacy Finder project was developed entirely by **Paolo Maizza, a student at Ca' Foscari University of Venice and H-Farm College**. Suggestions and feedback for improving the application are welcome. The next steps for the app will include providing more information on the products available in parapharmacies and enhancing the search efficiency.

Please feel free to fork the repository and submit a pull request for any improvements. 

 
## Contacts 
For any inquiries or further assistance, Project Lead: **890579@stud.unive.it**
