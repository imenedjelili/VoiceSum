# VoiceSum

# Voice-Controlled Calculator

## Overview
This project is a **Voice-Controlled Calculator** built using Python, combining speech recognition and a graphical user interface (GUI). The calculator can perform basic arithmetic operations via button clicks or voice commands, making it user-friendly and accessible.

## Features
- **Voice Input:** Perform calculations by speaking commands like "add 5 and 3" or "divide 10 by 2."
- **GUI Interface:** Fully functional calculator with buttons for standard arithmetic operations.
- **Dark Mode Design:** CustomTkinter-based dark theme for a sleek and modern look.
- **Error Handling:** Handles unknown inputs and errors gracefully, providing feedback to the user.

## Technologies Used
- **Python**: Core programming language.
- **CustomTkinter**: For designing the GUI.
- **SpeechRecognition**: To process and recognize voice commands.
- **Tkinter**: For additional GUI components.

## Installation

1. Clone the repository:
2. Navigate to the project directory:
3. Install the required dependencies:
   pip install speechrecognition customtkinter

## Usage

1. Run the Python script:
   ```bash
   python calculator.py
   ```
2. Use the GUI buttons to perform operations or speak commands like:
   - "Add 7 and 5"
   - "Subtract 10 from 25"
   - "Multiply 6 by 3"
   - "Divide 20 by 4"

3. The result will appear in the input box and also in the terminal.

## Voice Command Keywords
- **Addition**: "add," "plus," "+"
- **Subtraction**: "subtract," "minus," "-"
- **Multiplication**: "multiply by," "times," "*"
- **Division**: "divided by," "over," "/"

## Key Functions
- **button_click(button_number):** Handles button inputs and updates the display.
- **button_clear():** Clears the input box.
- **button_equal():** Evaluates the arithmetic operation.
- **Speech Recognition Integration:** Detects and processes voice commands to extract numbers and operations.

## Known Issues
- The speech recognition feature might not work well in noisy environments.
- Voice commands need to follow the specific keyword patterns listed above.

## Future Improvements
- Add support for advanced mathematical operations (e.g., square root, exponents).
- Improve natural language processing for a wider variety of voice inputs.
- Support multiple languages for voice commands.

## Contact
For any questions or feedback, feel free to contact me at fatma.imene.djelili@ensia.edu.dz
