## Introduction

Welcome to Parapharmacy Finder, an innovative application that allows you to search for the nearest retail location selling over-the-counter (OTC) medications across Italy. Additionally, you can check the availability of your desired product (either SOP or OTP) and plan your trip by adding multiple stops, receiving a precise itinerary.

# Features

- **Product Search:** Easily find the OTC medications you need.
- **Parapharmacy Filtering:** Filter search results to show only parapharmacies in your area.
- **Directions to Arrival:** Get detailed directions to your selected parapharmacy.
- **User-friendly Interface:** Enjoy an intuitive and easy-to-navigate interface.

# Techonologies Used 
- **Flask (FrontEnd) -Fast API (BackEnd)**
- **HTML**: Utilizzato per la struttura della pagina web.
- **CSS**: Utilizzato per lo stile e il layout della pagina web.
- **Bootstrap**: Libreria CSS per un design reattivo e componenti predefiniti.
- **Leaflet**: Libreria JavaScript per mappe interattive.
- **Leaflet Routing Machine**: Plugin per Leaflet per il routing e le direzioni.
- **JavaScript**: Utilizzato per la logica della pagina e l'interattività.
- **Fetch API**: Utilizzato per effettuare richieste HTTP per recuperare dati da un server.
- **OpenStreetMap**: Utilizzato per le mappe e il geocoding degli indirizzi tramite API.
- **Nominatim**: Servizio di geocoding utilizzato con OpenStreetMap per convertire indirizzi in coordinate geografiche.
- **Bootstrap JS**: Libreria JavaScript per funzionalità di Bootstrap.

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
Create and activate a virtual environment to manage dependencies:

**python3 -m venv venvv**
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required Python packages:

**pip install -r requirements.txt**

## Step 3: Set Up Docker (If Applicable)
If your project uses Docker, ensure Docker is installed and running. Build and run the Docker containers:

**docker-compose up --build**

## Step 4: Run the Application
If not using Docker, run the application directly. This might involve starting a web server or running a main script. For example:

**python backend/app/main.py**

## Step 5: Access the Application
Open a web browser and navigate to the appropriate URL: **http://localhost:8080**

# Contributing

The Parapharmacy Finder project was developed entirely by **Paolo Maizza, a student at Ca' Foscari University of Venice and H-Farm College**. Suggestions and feedback for improving the application are welcome. The next steps for the app will include providing more information on the products available in parapharmacies and enhancing the search efficiency.

Please feel free to fork the repository and submit a pull request for any improvements. 

 
# Contacts 
For any inquiries or further assistance, Project Lead: **890579@stud.unive.it**
