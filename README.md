# Bank Card Information Extractor

A powerful Python-based OCR tool specifically designed for extracting information from Iranian bank cards and financial documents. This tool uses advanced image processing and OCR techniques to accurately extract card numbers, expiry dates, CVV codes, and other relevant information.

## Features

- 🔍 Advanced OCR processing with Tesseract
- 📝 Extracts multiple card details:
  - Card Number
  - Full Name
  - Sheba Number (IBAN)
  - Expiry Date
  - CVV Code
- 🔄 Dual processing methods for improved accuracy
- 💾 JSON data storage with duplicate prevention
- 🌐 Support for both Persian and English text
- 🎯 Specifically optimized for Iranian bank cards

## Requirements

- Python 3.x
- OpenCV (cv2)
- NumPy
- Pytesseract
- Tesseract OCR Engine

## Installation

1. Install Tesseract OCR:
   - Windows: Download and install from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - Linux: `sudo apt-get install tesseract-ocr`
   - macOS: `brew install tesseract`

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your card image in the project directory
2. Run the script:
```bash
python TourismusGardeshgari_bank_card_scanner.py
```

## Output

The script generates two JSON files:
- `card_data_with_id.json`: Contains card data with unique IDs
- `card_data_without_id.json`: Contains card data without IDs (prevents duplicates)

## Project Structure

```
├── TourismusGardeshgari_bank_card_scanner.py  # Main script
├── requirements.txt              # Python dependencies
├── LICENSE                       # MIT License
└── README.md                     # This file
```

## Features in Detail

### Image Processing
- Dual-method image processing for better accuracy
- Adaptive thresholding
- Morphological operations
- Image enhancement

### OCR Capabilities
- Persian text recognition
- English text recognition
- Number extraction
- Special character handling

### Data Management
- JSON storage
- Duplicate prevention
- Automatic ID generation
- Data validation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Keywords

OCR, Image Processing, Bank Card Reader, Iranian Bank Cards, Financial Document Processing, Tesseract OCR, OpenCV, Python OCR, Card Data Extraction, Sheba Number Extractor, CVV Extractor, Card Number Reader, Document Processing, Image Recognition, Text Extraction, Bank Card Scanner, Financial OCR, Card Information Reader, Automated Card Processing

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Gardeshgary

## Acknowledgments

- Tesseract OCR
- OpenCV
- Python community 