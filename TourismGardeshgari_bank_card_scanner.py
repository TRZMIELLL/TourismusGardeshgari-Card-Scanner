import cv2
import numpy as np
import pytesseract
import re
import json
import os

# تنظیم مسیر Tesseract OCR در ویندوز
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# کدهای رنگی برای نمایش بهتر خروجی در ترمینال
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# ساختار داده‌ای برای ذخیره اطلاعات کارت
data_card = {
    'full_name': None,
    'card_number': None,
    'sheba_number': None,
    'exp': None,
    'cvv': None
}

def save_to_json_without_id(data, file_path="card_data_without_id.json"):
    """
    ذخیره اطلاعات کارت در فایل JSON بدون ID و جلوگیری از تکرار
    """
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            all_data = json.load(f)
    else:
        all_data = []

    # بررسی تکراری نبودن داده
    for entry in all_data:
        if entry["card_number"] == data["card_number"]:
            return

    all_data.append(data)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=4, ensure_ascii=False)

def save_to_json_with_id(data, file_path="card_data_with_id.json"):
    """
    ذخیره اطلاعات کارت در فایل JSON با ID خودکار
    """
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            all_data = json.load(f)
    else:
        all_data = []

    data_with_id = {"id": len(all_data) + 1}
    data_with_id.update(data)
    all_data.append(data_with_id)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=4, ensure_ascii=False)

def print_card_data(field=None):
    """
    نمایش اطلاعات کارت در خروجی
    """
    if field:
        print(data_card.get(field, "فیلد وجود ندارد"))
    else:
        json_data = json.dumps(data_card, indent=4, ensure_ascii=False)
        print(json_data)

def generate_sheba_number(extracted_text):
    """
    استخراج و تولید شماره شبا از متن استخراج شده
    """
    prefix = ""
    numbers = []

    # جستجوی پیشوند IR و ارقام
    for line in extracted_text.splitlines():
        if "IR" in line or "1R" in line:
            prefix = "IR"
            start_index = line.index("IR") + 2 if "IR" in line else line.index("1R") + 2
            numbers.extend([char for char in line[start_index:] if char.isdigit()])

            # جمع‌آوری ارقام از خطوط بعدی در صورت نیاز
            for next_line in extracted_text.splitlines()[extracted_text.splitlines().index(line) + 1:]:
                numbers.extend([char for char in next_line if char.isdigit()])
                if len(numbers) >= 24:
                    break
            break

    # تکمیل شماره شبا به 24 رقم
    if len(numbers) < 24:
        additional_digits_needed = 24 - len(numbers)
        numbers.extend(['0'] * additional_digits_needed)

    return prefix + ''.join(numbers[:24])

def extract_expiry_and_cvv(extracted_text):
    """
    استخراج تاریخ انقضا و CVV از متن
    """
    expiry_date = None
    cvv = None
    
    # جستجوی تاریخ انقضا (5 رقم)
    expiry_pattern = r'(\d{5})'
    expiry_match = re.search(expiry_pattern, extracted_text)
    
    if expiry_match:
        expiry_str = expiry_match.group(0).strip()
        if len(expiry_str) == 5:
            month = expiry_str[3:5]
            year = expiry_str[0:2]
            
            if len(month) == 1:
                month = '0' + month
            
            expiry_date = f"{month}/{year}"

        # جستجوی CVV بعد از تاریخ انقضا
        cvv_pattern = r'(?<=\d{5}\s)(\d{3,4})'
        cvv_match = re.search(cvv_pattern, extracted_text)
        
        if cvv_match:
            cvv = cvv_match.group(0)

    return expiry_date, cvv

def extract_large_numbers(text):
    """
    استخراج اعداد بزرگتر از 3 رقم از متن
    """
    pattern = r'\b\d{3,}\b'
    matches = re.findall(pattern, text)
    return matches

def convert_persian_to_english(number_str):
    """
    تبدیل اعداد فارسی به انگلیسی
    """
    persian_to_english_map = {
        '۰': '0', '۱': '1', '۲': '2', '۳': '3',
        '۴': '4', '۵': '5', '۶': '6', '۷': '7',
        '۸': '8', '۹': '9'
    }
    return ''.join(persian_to_english_map.get(char, char) for char in number_str)

def process_image(image_path):
    """
    پردازش تصویر و استخراج اطلاعات کارت
    """
    # خواندن و پیش‌پردازش تصویر
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # روش اول: پردازش با آستانه‌گذاری باینری معکوس
    _, binary_thresh1 = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY_INV)
    denoised1 = cv2.medianBlur(binary_thresh1, 3)
    cv2.imwrite("../processed_image_method1.png", denoised1)

    # استخراج متن با OCR
    custom_oem_psm_config = "--oem 1 --psm 6 -l fas+eng"
    extracted_text1 = pytesseract.image_to_string(denoised1, config=custom_oem_psm_config)
    lines1 = extracted_text1.splitlines()
    line_count1 = len(lines1)

    # استخراج اطلاعات از متن روش اول
    sheba_number1 = generate_sheba_number(extracted_text1)
    expiry_date, cvv_code = extract_expiry_and_cvv(extracted_text1)
    large_numbers = extract_large_numbers(extracted_text1)
    
    # پردازش اعداد بزرگ
    for index, number in enumerate(large_numbers[-2:], start=1):
        english_number = convert_persian_to_english(number)
        formatted_number = english_number
        
        if len(formatted_number) == 5:
            formatted_number = formatted_number[:2] + '/' + formatted_number[3:]

        if index == 1:
            data_card["exp"] = str(formatted_number)
        if index == 2:
            data_card["cvv"] = str(formatted_number)

    # روش دوم: پردازش با OTSU و عملیات مورفولوژیکی
    _, binary_thresh2 = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((2, 2), np.uint8)
    processed2 = cv2.morphologyEx(binary_thresh2, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite("../processed_image_method2.png", processed2)
    os.remove("../processed_image_method1.png")

    # استخراج متن با OCR از روش دوم
    extracted_text2 = pytesseract.image_to_string(processed2, config=custom_oem_psm_config)
    os.remove("../processed_image_method2.png")
    lines2 = extracted_text2.splitlines()
    line_count2 = len(lines2)

    # استخراج اطلاعات از متن روش دوم
    if len(lines2) >= 4:
        data_card["card_number"] = lines2[2]
        data_card["full_name"] = lines2[3].strip()

    sheba_number2 = generate_sheba_number(extracted_text2)
    if sheba_number2 != "000000000000000000000000":
        data_card['sheba_number'] = sheba_number2

    # نمایش نتایج
    print_card_data()
    input("enter for exit")

# اجرای برنامه
process_image("image.jpg")
