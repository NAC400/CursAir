import subprocess
import os

def create_virtualenv():
    """Create a virtual environment named 'venv'."""
    try:
        subprocess.check_call(['python', '-m', 'venv', 'venv'])
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual environment: {e}")

def install_dependencies():
    """Install dependencies from requirements.txt."""
    try:
        subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")

def set_environment_variables():
    """Set environment variables if needed."""
    os.environ['SERVER_HOST'] = 'localhost'
    os.environ['SERVER_PORT'] = '9999'
    print("Environment variables set.")

def main():
    # Create virtual environment
    create_virtualenv()

    # Activate virtual environment (Windows)
    activate_cmd = os.path.join('venv', 'Scripts', 'activate')
    subprocess.check_call(activate_cmd, shell=True)

    # Install dependencies
    install_dependencies()

    # Set environment variables (optional)
    set_environment_variables()

    print("Setup completed.")

if __name__ == "__main__":
    main()
