# Clone the repository
git clone https://github.com/BrijeshRanchod/Expense_Tracker.git

# Install Python 
# For Windows
winget install Python.Python.3.10

# For Mac
brew install python

# For Linux
sudo apt update
sudo apt install python3

# Navigate into the project directory
cd TodoApp

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate

# Install the dependencies from requirements.txt
pip install -r requirements.txt

# Set up the database by running the app (this will create the necessary tables)
python3 app.py

# Run the Flask app
python3 app.py
