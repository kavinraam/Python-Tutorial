"""
===============================================
PYTHON UNICODE SYSTEM - LEARNING GUIDE
===============================================

This file contains comprehensive examples and explanations
about Python's Unicode System for future reference.

Topics Covered:
1. What is Unicode?
2. Code Points
3. Character Encoding (UTF-8, UTF-16, UTF-32)
4. Python Unicode Support
5. Encoding (String → Bytes)
6. Decoding (Bytes → String)
7. Practical Examples

Author: Learning Guide
Date: 2026
===============================================
"""

# ===============================================
# 1. WHAT IS UNICODE?
# ===============================================

print("\n" + "="*50)
print("1. WHAT IS UNICODE?")
print("="*50)

print("""
Unicode is a standard system for representing ALL characters
from ALL languages in the world.

Examples of Unicode characters:
- English: A, B, C, hello
- French: é, à, ù
- Japanese: 日, 本, 語
- Hebrew: א, ב, ג
- Hindi: अ, आ, इ
- Emoji: 😀, 😂, ❤️

Before Unicode:
- Different languages used different systems
- English program couldn't display Japanese text
- French program couldn't display Arabic text
- MESS! 

With Unicode:
- One standard for ALL languages
- Any program can display any language
- Clean and organized! 
""")


# ===============================================
# 2. CODE POINTS
# ===============================================

print("\n" + "="*50)
print("2. CODE POINTS")
print("="*50)

print("""
Code Point = A number assigned to each character

Range: U+0000 to U+10FFFF (1,114,111 total characters)

Examples:
- 'A' → Code point U+0041 (65 in decimal)
- 'a' → Code point U+0061 (97 in decimal)
- '₹' → Code point U+20B9 (8377 in decimal)
- '日' → Code point U+65E5 (26085 in decimal)
""")

# Example: Displaying characters using Unicode code points
print("\nExample: Using Unicode Code Points")
print("-" * 40)

char_A = "\u0041"  # 'A'
char_a = "\u0061"  # 'a'
rupee = "\u20B9"   # '₹'
kanji = "\u65E5"   # '日'

print(f"U+0041 → {char_A}")
print(f"U+0061 → {char_a}")
print(f"U+20B9 → {rupee} (Rupee symbol)")
print(f"U+65E5 → {kanji} (Japanese character)")


# ===============================================
# 3. CHARACTER ENCODINGS
# ===============================================

print("\n" + "="*50)
print("3. CHARACTER ENCODINGS")
print("="*50)

print("""
Character Encoding = Rules for converting code points to bytes

Problem: Code points are numbers. How to store in memory as bytes?
Solution: Use encoding standards

Three Main Encodings:

1. UTF-8 (Most Popular) 
   - Uses 1 to 4 bytes per character
   - Variable length
   - English: 1 byte
   - Other languages: 2-4 bytes
   - Most efficient for English text
   - Default in Python 3

2. UTF-16
   - Uses 2 or 4 bytes per character
   - Used by Windows internally

3. UTF-32
   - Uses always 4 bytes per character
   - Fixed length but wasteful

UTF = Unicode Transformation Format
""")


# ===============================================
# 4. PYTHON UNICODE SUPPORT
# ===============================================

print("\n" + "="*50)
print("4. PYTHON UNICODE SUPPORT")
print("="*50)

print("""
Python 3.0 onwards has built-in Unicode support!

Key Points:
- str type contains Unicode characters
- Any string (single, double, or triple-quoted) is Unicode
- Default encoding for Python source code is UTF-8
- You can use literal characters or Unicode escape sequences
""")

# Example 1: Unicode characters displayed directly
print("\nExample 1: Direct Unicode Characters")
print("-" * 40)

var1 = "3/4"  # Literal character
print(f"Literal: {var1}")

var2 = "\u00BE"  # Unicode code point
print(f"Unicode \\u00BE: {var2}")


# Example 2: String from Unicode values
print("\nExample 2: Creating String from Unicode Values")
print("-" * 40)

var3 = "\u0031\u0030"  # \u0031 = '1', \u0030 = '0'
print(f"\\u0031\\u0030 → {var3}")

var4 = "\u0048\u0065\u006c\u006c\u006f"  # HELLO
print(f"Unicode H-e-l-l-o → {var4}")


# Example 3: Different language characters
print("\nExample 3: Different Language Characters")
print("-" * 40)

english = "Hello"
french = "Bonjour"
japanese = "こんにちは"
hindi = "नमस्ते"
emoji = "😀 😂 ❤️"

print(f"English: {english}")
print(f"French: {french}")
print(f"Japanese: {japanese}")
print(f"Hindi: {hindi}")
print(f"Emoji: {emoji}")


# ===============================================
# 5. ENCODING: STRING → BYTES
# ===============================================

print("\n" + "="*50)
print("5. ENCODING (String → Bytes)")
print("="*50)

print("""
encode() Method:
- Converts readable text (string) to bytes
- String is human-readable
- Bytes are binary data (computer-readable)
- Syntax: string.encode('encoding_type')

Common Encoding Types:
- 'utf-8' (most common)
- 'utf-16'
- 'utf-32'
- 'ascii'
""")

# Example 1: Simple encoding
print("\nExample 1: Encoding ASCII String")
print("-" * 40)

string1 = "Hello"
print(f"Original String: {string1}")
print(f"Type: {type(string1)}")

bytes1 = string1.encode('utf-8')
print(f"After encode('utf-8'): {bytes1}")
print(f"Type: {type(bytes1)}")


# Example 2: Encoding with special characters
print("\nExample 2: Encoding Special Characters")
print("-" * 40)

string2 = "Bonjour"  # French
bytes2 = string2.encode('utf-8')
print(f"Original: {string2}")
print(f"Encoded: {bytes2}")


# Example 3: Encoding with Rupee symbol
print("\nExample 3: Encoding Rupee Symbol (₹)")
print("-" * 40)

string3 = "₹100"
bytes3 = string3.encode('utf-8')
print(f"Original String: {string3}")
print(f"Encoded Bytes: {bytes3}")


# ===============================================
# 6. DECODING: BYTES → STRING
# ===============================================

print("\n" + "="*50)
print("6. DECODING (Bytes → String)")
print("="*50)

print("""
decode() Method:
- Converts bytes (binary) back to readable text
- Bytes are computer-readable
- String is human-readable
- Syntax: bytes_object.decode('encoding_type')

This is the opposite of encode()!
""")

# Example 1: Simple decoding
print("\nExample 1: Decoding Bytes")
print("-" * 40)

bytes_data = b'Hello'
print(f"Original Bytes: {bytes_data}")
print(f"Type: {type(bytes_data)}")

string_data = bytes_data.decode('utf-8')
print(f"After decode('utf-8'): {string_data}")
print(f"Type: {type(string_data)}")


# Example 2: Encode and Decode Cycle
print("\nExample 2: Complete Encode-Decode Cycle")
print("-" * 40)

original = "Hello World"
print(f"Step 1 - Original String: {original}")

encoded = original.encode('utf-8')
print(f"Step 2 - After encode(): {encoded}")

decoded = encoded.decode('utf-8')
print(f"Step 3 - After decode(): {decoded}")

print(f"Are they equal? {original == decoded}")


# ===============================================
# 7. PRACTICAL EXAMPLES
# ===============================================

print("\n" + "="*50)
print("7. PRACTICAL EXAMPLES")
print("="*50)

# Example 1: Rupee Symbol
print("\nExample 1: Working with Rupee Symbol (₹)")
print("-" * 40)

rupee_string = "\u20B9"  # Rupee symbol using Unicode code point
print(f"Step 1 - Create string with Rupee symbol: {rupee_string}")

rupee_bytes = rupee_string.encode('utf-8')
print(f"Step 2 - Encode to bytes: {rupee_bytes}")

rupee_decoded = rupee_bytes.decode('utf-8')
print(f"Step 3 - Decode back to string: {rupee_decoded}")


# Example 2: Multiple characters with different encodings
print("\nExample 2: Comparing Different Encodings")
print("-" * 40)

test_string = "Hello₹"
print(f"Original String: {test_string}")

utf8_bytes = test_string.encode('utf-8')
print(f"UTF-8 Encoding: {utf8_bytes} (length: {len(utf8_bytes)} bytes)")

utf16_bytes = test_string.encode('utf-16')
print(f"UTF-16 Encoding: {utf16_bytes} (length: {len(utf16_bytes)} bytes)")

utf32_bytes = test_string.encode('utf-32')
print(f"UTF-32 Encoding: {utf32_bytes} (length: {len(utf32_bytes)} bytes)")


# Example 3: Emoji handling
print("\nExample 3: Working with Emoji")
print("-" * 40)

emoji_string = "Python is fun! 🐍"
print(f"String with Emoji: {emoji_string}")

emoji_bytes = emoji_string.encode('utf-8')
print(f"Encoded Bytes: {emoji_bytes}")

emoji_decoded = emoji_bytes.decode('utf-8')
print(f"Decoded Back: {emoji_decoded}")


# Example 4: Multi-language text
print("\nExample 4: Multi-language Text Processing")
print("-" * 40)

texts = {
    "English": "Hello",
    "French": "Bonjour",
    "Spanish": "Hola",
    "Japanese": "こんにちは",
    "Hindi": "नमस्ते",
}

for language, text in texts.items():
    encoded = text.encode('utf-8')
    byte_count = len(encoded)
    print(f"{language:12} → {text:15} → {byte_count} bytes")


# ===============================================
# 8. IMPORTANT POINTS TO REMEMBER
# ===============================================

print("\n" + "="*50)
print("8. IMPORTANT POINTS TO REMEMBER")
print("="*50)

print("""
KEY CONCEPTS:

1. Unicode = International standard for all characters
2. Code Point = Number assigned to each character
3. UTF-8 = Most common encoding (variable 1-4 bytes)
4. String = Human-readable text (Unicode in Python 3)
5. Bytes = Binary data (computer-readable)
6. encode() = String → Bytes
7. decode() = Bytes → String

WHEN TO USE:

Use String When:
- Displaying text to users
- Working with text in Python
- Readable format needed

Use Bytes When:
- Storing in files
- Sending over network
- Binary format needed

PRACTICAL WORKFLOW:

User Input
    ↓
String (Unicode) - "Hello"
    ↓ encode()
Bytes - b'Hello'
    ↓
Store in file / Send over network
    ↓
Read from file / Receive
    ↓ decode()
String (Unicode) - "Hello"
    ↓
Display to user
""")


# ===============================================
# 9. PRACTICE EXERCISES
# ===============================================

print("\n" + "="*50)
print("9. PRACTICE EXERCISES")
print("="*50)

print("""
Try these exercises to practice Unicode concepts:

Exercise 1: Create a string with your name using Unicode
Solution:
name = "Your Name Here"
encoded = name.encode('utf-8')
decoded = encoded.decode('utf-8')
print(decoded)

Exercise 2: Use Unicode code points to display characters
Solution:
char1 = "\\u0048"  # H
char2 = "\\u0065"  # e
char3 = "\\u006c"  # l
char4 = "\\u006c"  # l
char5 = "\\u006f"  # o
print(char1 + char2 + char3 + char4 + char5)

Exercise 3: Encode and decode with special characters
Solution:
text = "Hello ₹ Emoji 🎉"
b = text.encode('utf-8')
s = b.decode('utf-8')
print(s)

Exercise 4: Compare byte sizes of different encodings
Solution:
text = "Python"
print(f"UTF-8: {len(text.encode('utf-8'))} bytes")
print(f"UTF-16: {len(text.encode('utf-16'))} bytes")
print(f"UTF-32: {len(text.encode('utf-32'))} bytes")
""")


# ===============================================
# END OF LEARNING GUIDE
# ===============================================

print("\n" + "="*50)
print("END OF UNICODE LEARNING GUIDE")
print("="*50)

print("""
This file covers all the important concepts of Unicode!

You can:
1. Run this file: python unicode_learning_guide.py
2. Read through the examples and outputs
3. Modify the examples to practice
4. Refer back to this file whenever needed
""")