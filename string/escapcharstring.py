# List of common escape characters in Python strings with examples
# "\n"  : Newline (e.g., "Hello\nWorld" -> prints on two lines)
# "\t"  : Tab (e.g., "Hello\tWorld" -> inserts a tab space)
# "\r"  : Carriage Return (e.g., "Hello\rWorld" -> "Worldo")
# "\'"  : Single Quote (e.g., 'It\'s' -> It's)
# "\""  : Double Quote (e.g., "She said \"Hi\"" -> She said "Hi")
# "\\"  : Backslash (e.g., "C:\\path\\to\\file")
# "\b"  : Backspace (e.g., "Hello\bWorld" -> "HellWorld")
# "\f"  : Form Feed (rarely used)
# "\v"  : Vertical Tab (rarely used)
# "\a"  : Bell/Alert (may make a sound)
# "\0"  : Null Character
# "\N{name}" : Unicode Character by Name (e.g., "\N{GREEK CAPITAL LETTER DELTA}")
# "\uXXXX"   : Unicode Character (16-bit hex, e.g., "\u03A9" -> Ω)
# "\UXXXXXXXX": Unicode Character (32-bit hex, e.g., "\U0001F600" -> 😀)
# "\xXX"     : Character with hex value XX (e.g., "\x41" -> A)
# "\ooo"     : Character with octal value ooo (e.g., "\101" -> A)
# Examples demonstrating each escape character in action
examples = [
    "Hello\\nWorld",                # Newline
    "Hello\\tWorld",                # Tab
    "Hello\\rWorld",                # Carriage Return
    "It\\'s a test",                # Single Quote
    "She said \\\"Hi\\\"",          # Double Quote
    "C:\\\\path\\\\to\\\\file",     # Backslash
    "Hello\\bWorld",                # Backspace
    "Hello\\fWorld",                # Form Feed
    "Hello\\vWorld",                # Vertical Tab
    "Bell sound: \\a",              # Bell/Alert
    "Null\\0Character",             # Null Character
    "Greek: \\N{GREEK CAPITAL LETTER DELTA}",  # Unicode by name
    "Omega: \\u03A9",               # Unicode 16-bit hex
    "Smile: \\U0001F600",           # Unicode 32-bit hex
    "Letter A: \\x41",              # Hex value
    "Letter A: \\101",              # Octal value
]

print("\n--- Escape Character Examples ---")
for example in examples:
    print(f"Raw:   {example}")
    print(f"Output:", end=" ")
    try:
        print(eval(f'f"{example}"'))
    except Exception as e:
        print(f"(Error: {e})")
    print()


#     --- Escape Character Examples ---
# Raw:   Hello\nWorld
# Output: Hello
# World

# Raw:   Hello\tWorld
# Output: Hello   World

# Raw:   Hello\rWorld
# Worldt: Hello

# Raw:   It\'s a test
# Output: It's a test

# Raw:   She said \"Hi\"
# Output: She said "Hi"

# Raw:   C:\\path\\to\\file
# Output: C:\path\to\file

# Raw:   Hello\bWorld
# Output: HellWorld

# Raw:   Hello\fWorld
# Output: Hello
#              World

# Raw:   Hello\vWorld
# Output: Hello
#              World

# Raw:   Bell sound: \a
# Output: Bell sound: 

# Raw:   Null\0Character
# Output: NullCharacter

# Raw:   Greek: \N{GREEK CAPITAL LETTER DELTA}
# Output: Greek: Δ

# Raw:   Omega: \u03A9
# Output: Omega: Ω

# Raw:   Smile: \U0001F600
# Output: Smile: 😀

# Raw:   Letter A: \x41
# Output: Letter A: A

# Raw:   Letter A: \101
# Output: Letter A: A
