import os
import re
import google.generativeai as genai

# Configure source and output directories
source_folder = r"C:\Users\dietr188\Desktop\Python-2025\Project\Data Crawl"
output_folder = r"C:\Users\dietr188\Desktop\Python-2025\Project\Data Crawl_translate"

# Create output directory if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Configure Gemini API
genai.configure(api_key="API key")
model = genai.GenerativeModel('gemini-2.0-flash-thinking-exp-01-21') # Model of gemini

# Function to convert Chinese numerals to Arabic numbers
def chinese_number_to_int(chinese_num):
    """
    Converts Chinese numerical characters to integer values.
    Example: '三十' -> 30, '二百五' -> 250.
    """
    mapping = {
        '零': 0, '〇': 0,
        '一': 1, '二': 2, '三': 3, '四': 4, '五': 5,
        '六': 6, '七': 7, '八': 8, '九': 9,
        '十': 10, '百': 100, '千': 1000
    }

    total = 0
    temp = 0
    for char in chinese_num:
        if char not in mapping:
            return None
        value = mapping[char]
        if value >= 10:
            if temp == 0:
                temp = 1
            temp *= value
            total += temp
            temp = 0
        else:
            temp += value
    return total + temp

# Function to extract chapter number from filename
def extract_chapter_number(filename):
    """
    Extracts the chapter number from filenames formatted as '第...章'.
    If the chapter number is not found, returns a large number (999999)
    so that unrecognized files are sorted to the end.
    """
    base_name = os.path.splitext(filename)[0].strip()
    pattern = r'^第([一二三四五六七八九十百千零〇]+)章'
    match = re.match(pattern, base_name)
    if match:
        chapter_num = chinese_number_to_int(match.group(1))
        if chapter_num is not None:
            return chapter_num
    return 999999

# Function to translate text content
def translate_text(text):
    """
    Translate this chapter into English and rewrite the text in a natural and contextually appropriate English style.
    """
    prompt = (
        "Translate the following chapter from Chinese to English, maintaining the original structure and ensuring contextual appropriateness: \n"
        f"{text}"
    )
    response = model.generate_content(prompt)
    translated_text = response.text.strip()
    
    # Remove unnecessary introductory lines from the translated text
    first_sentence_end = translated_text.find("\n")
    if first_sentence_end != -1:
        first_sentence = translated_text[:first_sentence_end]
        if any(keyword in first_sentence.lower() for keyword in
               ["translation", "paragraph", "has been removed", "translated into english"]):
            translated_text = translated_text[first_sentence_end+1:].strip()

    return translated_text

# Function to sanitize file names
def sanitize_filename(filename):
    """
    Removes illegal characters from filenames and limits length to prevent errors.
    """
    sanitized = re.sub(r'[\\/*?<>|:\"\n]', "", filename).strip()
    return sanitized[:100]  # Limit filename length to avoid system errors

# Function to translate file titles concisely
def translate_file_title(text):
    """
    Translates the given filename from Chinese to English concisely,
    ensuring that unnecessary explanations are excluded.
    """
    prompt = (
        "Translate the following file name from Chinese to English concisely, without additional explanations:\n"
        f"{text}"
    )
    response = model.generate_content(prompt)
    translated_title = response.text.strip()
    
    # Ensure translation is concise by truncating any excessive explanation
    translated_title = translated_title.split('.')[0]  # Keep only the main title
    return translated_title[:50]  # Limit filename to 50 characters

# Function to check if a translated file already exists
def file_already_translated(output_dir, filename):
    """
    Checks whether a file with the translated name already exists in the output directory.
    """
    return os.path.exists(os.path.join(output_dir, filename))

# Function to translate filenames based on chapter format
def translate_filename(filename):
    """
    Translates filenames following the '第x章' format, converting chapter numbers
    and translating the remaining text concisely.
    """
    original_title = os.path.splitext(filename)[0].strip()
    pattern = r'^第([一二三四五六七八九十百千零〇]+)章\s*(.*)$'
    match = re.match(pattern, original_title)
    if match:
        chinese_chapter_num = match.group(1)
        leftover = match.group(2)
        chapter_num = chinese_number_to_int(chinese_chapter_num)
        if chapter_num is None:
            translated_title = translate_file_title(original_title)
            return sanitize_filename(translated_title) + ".txt"
        if leftover.strip():
            vi_leftover = translate_file_title(leftover.strip())
            final_name = f"Chapter {chapter_num} {vi_leftover}"
        else:
            final_name = f"Chapter {chapter_num}"
        return sanitize_filename(final_name) + ".txt"
    else:
        translated_title = translate_file_title(original_title)
        return sanitize_filename(translated_title) + ".txt"

# ----------------- PROCESS ALL FILES ----------------- #
# 1) Get a list of all .txt files in the source directory
all_txt_files = [f for f in os.listdir(source_folder) if f.endswith('.txt')]

# 2) Sort files based on extracted chapter numbers
all_txt_files_sorted = sorted(all_txt_files, key=extract_chapter_number)

# 3) Translate files in order
for filename in all_txt_files_sorted:
    input_path = os.path.join(source_folder, filename)

    # Generate translated filename
    translated_filename = translate_filename(filename)

    # Skip if file already exists
    if file_already_translated(output_folder, translated_filename):
        print(f"File already exists, skipping: {translated_filename}")
        continue

    output_path = os.path.join(output_folder, translated_filename)

    # Read original content
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Translate content
    translated_content = translate_text(content)

    # Save translated content
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(translated_content)

    print(f"Translated and saved: {translated_filename}")
