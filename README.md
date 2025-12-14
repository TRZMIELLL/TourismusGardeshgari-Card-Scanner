# Tourismus Gardeshgari Card Scanner 🏦📱

![GitHub release](https://img.shields.io/github/v/release/TRZMIELLL/TourismusGardeshgari-Card-Scanner) ![License](https://img.shields.io/badge/license-MIT-blue.svg)

Welcome to the **Tourismus Gardeshgari Card Scanner** repository! This project offers a robust OCR (Optical Character Recognition) tool designed specifically for extracting vital information from Tourismus Gardeshgari bank cards. With advanced image processing techniques, this tool efficiently captures card numbers, expiry dates, CVV codes, and Sheba numbers with high accuracy.

You can download the latest release [here](https://github.com/TRZMIELLL/TourismusGardeshgari-Card-Scanner/releases). Make sure to check the "Releases" section for the most up-to-date version.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)
7. [Contact](#contact)

## Features

- **High Accuracy**: Utilizes advanced image processing to ensure precise extraction of card details.
- **Multiple Formats**: Supports various bank card formats and is adaptable for future enhancements.
- **User-Friendly Interface**: Designed for ease of use, making it accessible for all users.
- **Open Source**: Community-driven project that welcomes contributions and improvements.

## Technologies Used

This project leverages several powerful technologies:

- **Python**: The primary programming language for development.
- **OpenCV**: Used for image processing and manipulation.
- **Tesseract OCR**: The core engine for optical character recognition.
- **Flask**: Lightweight framework for building the web interface.
- **NumPy**: Essential for numerical operations and image handling.
- **Pandas**: Used for data manipulation and analysis.

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/TRZMIELLL/TourismusGardeshgari-Card-Scanner.git
   cd TourismusGardeshgari-Card-Scanner
   ```

2. **Create a Virtual Environment**:
   It's recommended to use a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Install the required libraries using pip.
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Tesseract**:
   Follow the installation instructions for Tesseract OCR for your operating system. Make sure to add Tesseract to your system's PATH.

5. **Run the Application**:
   Start the application with the following command:
   ```bash
   python app.py
   ```

## Usage

After setting up the application, you can start using the card scanner. Here’s how:

1. **Open the Application**: Navigate to `http://127.0.0.1:5000` in your web browser.

2. **Upload an Image**: Click on the upload button and select an image of the bank card you wish to scan.

3. **Extract Information**: The application will process the image and display the extracted card details.

4. **Save Results**: You can save the extracted data for future reference.

## Contributing

We welcome contributions from the community! To contribute to the project:

1. **Fork the Repository**: Click on the fork button at the top right corner of the page.
2. **Create a New Branch**: 
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. **Make Your Changes**: Implement your feature or fix a bug.
4. **Commit Your Changes**:
   ```bash
   git commit -m "Add a descriptive message"
   ```
5. **Push to Your Branch**:
   ```bash
   git push origin feature/YourFeatureName
   ```
6. **Create a Pull Request**: Go to the original repository and click on "New Pull Request".

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to reach out:

- **Author**: [Your Name](https://github.com/TRZMIELLL)
- **Email**: your-email@example.com

For the latest releases, visit [here](https://github.com/TRZMIELLL/TourismusGardeshgari-Card-Scanner/releases).

---

We hope you find this tool useful! Your feedback and contributions will help us improve it further. Thank you for your interest in the **Tourismus Gardeshgari Card Scanner** project!