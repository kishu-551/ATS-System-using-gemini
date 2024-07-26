# ATS-System-using-gemini


# Python version - 3.10 Suported
# VS CODE Project


# Setting Up and Running the App

# Create and activate the virtual environment:

In the terminal, navigate to your project folder.
# Create a virtual environment:
python -m venv venv


# Activate the virtual environment:
On Windows (PowerShell):
.\venv\Scripts\Activate

On macOS/Linux:
source venv/bin/activate


#  Install the required packages:
pip install streamlit google-generativeai python-dotenv PyPDF2

# Create the .env file:
In your project folder, create a file named .env.
Add your Google API key to this file:
GOOGLE_API_KEY=your_google_api_key_here

# Run the Streamlit app:

In the terminal, ensure you are in your project directory and the virtual environment is activated.
Run the following command to start the Streamlit app:

streamlit run app.py

## This will launch the Streamlit server, and you should see output in the terminal indicating where the app is running (usually http://localhost:8501). You can open this URL in your web browser to access the application and use it to screen Mulesoft developer resumes against job descriptions.
