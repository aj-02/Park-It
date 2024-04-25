# Parking Space Availability Notifier

## Overview
**Park-It** is an application that leverages OpenCV for parking space detection in a given area. It identifies free parking spaces in real-time using computer vision techniques. 
Once a free parking space is detected, it sends a notification message to the owners or relevant authorities via the Twilio API.

## Features
- **Real-time parking space detection** using OpenCV.
- Integration with **Twilio API** for sending SMS notifications.
- Adjustable parameters for **parking space detection** to accommodate different environments.
- Simple and intuitive interface.

## Requirements
- Python 3.x
- OpenCV library
- Twilio Python library

## Installation
1. Clone the repository:
git clone https://github.com/aj-02/Park-It.git

2. Install dependencies:
pip install -r requirements.txt

## Configuration
1. Obtain Twilio API credentials (Account SID, Auth Token, and Twilio phone number).
2. Configure Twilio credentials in the `config.py` file.

## Usage
1. Run the application:
python main.py

2. Follow the on-screen instructions to configure the detection parameters.

3. The application will start detecting free parking spaces and sending notifications via Twilio.

## Troubleshooting
- If the application is not detecting parking spaces accurately, try adjusting the detection parameters in the `config.py` file.
- Ensure that the Twilio API credentials are correctly configured in the `config.py` file.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
