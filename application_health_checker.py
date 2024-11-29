import requests
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="app_health_report.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Application URL to check
APPLICATION_URL = "https://www.google.com"  

# Function to check application health
def check_application_health(url):
    """
    Checks the health of the application by sending an HTTP GET request
    and evaluating the response status code.
    """
    try:
        response = requests.get(url, timeout=5)  # Timeout after 5 seconds
        status_code = response.status_code

        # Determine health based on HTTP status code
        if 200 <= status_code < 300:
            message = f"Application is UP. Status Code: {status_code}"
            print(message)
            logging.info(message)
        else:
            message = f"Application is DOWN. Status Code: {status_code}"
            print(message)
            logging.warning(message)

    except requests.exceptions.ConnectionError:
        message = "Application is DOWN. Connection Error."
        print(message)
        logging.error(message)

    except requests.exceptions.Timeout:
        message = "Application is DOWN. Timeout occurred."
        print(message)
        logging.error(message)

    except Exception as e:
        message = f"Application is DOWN. An unexpected error occurred: {e}"
        print(message)
        logging.error(message)

# Main function
if __name__ == "__main__":
    print("Starting Application Health Checker...")
    check_application_health(APPLICATION_URL)
