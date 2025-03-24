import os
import subprocess
import sys

def run_command(command, shell=False):
    """Run a shell command and handle errors"""
    try:
        subprocess.check_call(command, shell=shell)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

def main():
    # Step 1: Clone the repository
    repo_url = "https://github.com/BrijeshRanchod/Expense_Tracker.git"
    print(f"Cloning repository {repo_url}...")
    run_command(["git", "clone", repo_url])

    # Step 2: Install Python (Platform dependent)
    if sys.platform == "win32":
        print("Installing Python for Windows...")
        run_command(["winget", "install", "Python.Python.3.10"], shell=True)
    elif sys.platform == "darwin":
        print("Installing Python for macOS...")
        run_command(["brew install python3"], shell=True)
    elif sys.platform == "linux" or sys.platform == "linux2":
        print("Installing Python for Linux...")
        run_command(["sudo", "apt", "update"])
        run_command(["sudo", "apt", "install", "python3"])

    # Step 3: Navigate to the project directory
    project_dir = "Expense_Tracker"
    print(f"Navigating to {project_dir}...")
    os.chdir(project_dir)

    # Step 4: Create a virtual environment
    print("Creating virtual environment...")
    run_command(["python3", "-m", "venv", "venv"])

    # Step 5: Activate the virtual environment
    if sys.platform == "win32":
        print("Activating virtual environment for Windows...")
        run_command(["venv\\Scripts\\activate"], shell=True)
    else:
        print("Activating virtual environment for macOS/Linux...")
        run_command(["source venv/bin/activate"], shell=True)  # Correct command for zsh

    # Step 6: Install dependencies from requirements.txt (with the --break-system-packages flag)
    print("Installing dependencies from requirements.txt...")
    run_command(["pip3", "install", "--break-system-packages", "-r", "requirements.txt"])

    # Step 7: Set up the database and run the Flask app
    print("Setting up the database and running the Flask app...")
    run_command(["python3", "app.py"])

if __name__ == "__main__":
    main()
