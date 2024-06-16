# Parapharmacy Finder

Welcome to Parapharmacy Finder, an innovative application designed to help you locate the nearest retail locations selling over-the-counter (OTC) medications across Italy. Additionally, you can check the availability of your desired product (either SOP or OTP) and plan your trip by adding multiple stops, receiving a precise itinerary.

<details>
<summary><strong>Features</strong></summary>

- **Product Search:** Easily find the OTC medications you need.
- **Parapharmacy Filtering:** Filter search results to show only parapharmacies in your area.
- **Directions to Arrival:** Get detailed directions to your selected parapharmacy.
- **User-friendly Interface:** Enjoy an intuitive and easy-to-navigate interface.

</details>

<details>
<summary><strong>Technologies Used</strong></summary>

- **Flask (Frontend)**
- **FastAPI (Backend)**
- **HTML:** Used for the structure of the web page.
- **CSS:** Used for styling and layout.
- **Bootstrap:** CSS library for responsive design and predefined components.
- **Leaflet:** JavaScript library for interactive maps.
- **Leaflet Routing Machine:** Plugin for Leaflet for routing and directions.
- **JavaScript:** Used for page logic and interactivity.
- **Fetch API:** Used for making HTTP requests to retrieve data from a server.
- **OpenStreetMap:** Used for maps and geocoding addresses via API.
- **Nominatim:** Geocoding service used with OpenStreetMap to convert addresses into geographic coordinates.
- **Bootstrap JS:** JavaScript library for Bootstrap functionalities.

</details>

<details>
<summary><strong>CSV Datasets Used in the Project</strong></summary>

This section outlines the essential datasets to run the project:

- **parafarmacie.csv:** List of all parapharmacies in Italy.
- **SOP-OTP.csv:** List of all SOP or OTP products that can be sold by parapharmacies.

</details>

<details>
<summary><strong>Steps to Use</strong></summary>

To use the application from the GitHub repository, follow these steps:

```bash
# Step 1: Clone the Repository
Open a terminal and clone the repository:

git clone https://github.com/paolomaizza/LSPD_parapharmacy_finder.git
cd LSPD_parapharmacy_finder

# Step 2: Set Up the Environment
Create and activate a virtual environment to manage dependencies:

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required Python packages:

pip install -r requirements.txt

# Step 3: Set Up Docker (If Applicable)
If your project uses Docker, ensure Docker is installed and running. Build and run the Docker containers:

docker-compose up --build

# Step 4: Run the Application
If not using Docker, run the application directly. This might involve starting a web server or running a main script. For example:

python backend/app/main.py

# Step 5: Access the Application
Open a web browser and navigate to the appropriate URL: http://localhost:8080
</details>
<details>
<summary><strong>Contributing</strong></summary>
The Parapharmacy Finder project was developed entirely by Paolo Maizza, a student at Ca' Foscari University of Venice and H-Farm College. Suggestions and feedback for improving the application are welcome. The next steps for the app will include providing more information on the products available in parapharmacies and enhancing search efficiency.

Please feel free to fork the repository and submit a pull request for any improvements.

</details>
<details>
<summary><strong>Contacts</strong></summary>
For any inquiries or further assistance, contact Project Lead: 890579@stud.unive.it.

</details>