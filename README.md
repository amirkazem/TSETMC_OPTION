# TSETMC_OPTION
Version1
Tehran Stock Exchange Trading Options Package
This package provides an API and a web interface (using Flask) for interacting with Tehran Stock Exchange (TSE) trading options data, including buy and sell permissions. It allows you to fetch, analyze, and visualize stock market data programmatically or through a user-friendly web interface.

Features:
Tehran Stock Exchange (TSE) Trading Options API: Access buy/sell options data via a RESTful API.
Web Interface: A Flask-based web application that dynamically displays trading options data in a table format, with search and export features.
Real-Time Data Updates: The API fetches real-time data, updating every 5 seconds for accuracy.
Excel Export: Export the trading data tables to Excel for further analysis.
Setup Instructions:
Prerequisites:
Create a Virtual Environment:

In your terminal, navigate to the project directory and run:
bash
Copy code
python -m venv venv
Activate the Virtual Environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install Dependencies:

Install the required libraries by running:
bash
Copy code
pip install -r requirements.txt
Running the Flask Web Application:
After activating the virtual environment and installing dependencies, start the Flask application by running:

bash
Copy code
flask run
The web application will be accessible at http://127.0.0.1:5000/ in your browser, where you can interact with the dynamic tables and visualize the data.

Using the API:
To use the API directly, you can make HTTP requests to the following endpoints:

GET /api/data_call: Fetch call option data.
GET /api/data_put: Fetch put option data.
Example using curl:

bash
Copy code
curl http://127.0.0.1:5000/api/data_call
The API returns a JSON response with the relevant trading data.
