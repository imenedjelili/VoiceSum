import speech_recognition as sr 
import tkinter as tk
import customtkinter as ctk

rec = sr.Recognizer()

# Initialize customtkinter
ctk.set_appearance_mode("dark")  # Dark theme
ctk.set_default_color_theme("dark-blue")  # Accent color theme

# Create the main window
wind = ctk.CTk()
wind.title("Calculator")
wind.geometry("400x600")
wind.configure(bg="#000000")
wind.resizable(False, False)

# Define fonts
display_font = ("Helvetica", 36, "bold")
button_font = ("Helvetica", 20, "bold")

# Input box
box = ctk.CTkEntry(
    wind,
    font=display_font,
    justify="right",
    corner_radius=15,
    height=70,
    width=380,  # Set width here
    fg_color="#1C1C1E",  # Dark gray
    text_color="white",
)
box.place(x=10, y=50)

# Button dimensions
button_width = 80
button_height = 90
button_gap = 5

# Button positions
x_start = 10
y_start = 140

# Add buttons
buttons = [
    # Row 1 (AC, +/- conversion, %, division)
    ("AC", "#FF3B30", 0, 0),
    ("+/-", "#2C2C2E", 1, 0),
    ("%", "#2C2C2E", 2, 0),
    ("/", "#FF9500", 3, 0),
    # Row 2 (7, 8, 9, multiplication)
    ("7", "#2C2C2E", 0, 1),
    ("8", "#2C2C2E", 1, 1),
    ("9", "#2C2C2E", 2, 1),
    ("*", "#FF9500", 3, 1),
    # Row 3 (4, 5, 6, subtraction)
    ("4", "#2C2C2E", 0, 2),
    ("5", "#2C2C2E", 1, 2),
    ("6", "#2C2C2E", 2, 2),
    ("-", "#FF9500", 3, 2),
    # Row 4 (1, 2, 3, addition)
    ("1", "#2C2C2E", 0, 3),
    ("2", "#2C2C2E", 1, 3),
    ("3", "#2C2C2E", 2, 3),
    ("+", "#FF9500", 3, 3),
    # Row 5 (0, comma, equal)
    ("0", "#2C2C2E", 0, 4, 2),  # Spanning 2 columns
    (".", "#2C2C2E", 2, 4),
    ("=", "#FF9500", 3, 4),
]

# Add buttons to the window
for button in buttons:
    text, bg_color, col, row = button[:4]
    colspan = button[4] if len(button) > 4 else 1

    ctk.CTkButton(
        wind,
        text=text,
        font=button_font,
        corner_radius=20,  # Rounded corners
        fg_color=bg_color,
        text_color="white",
        hover_color="#444444",  # Subtle hover effect
        command=lambda t=text: button_click(t),  # Bind `text` to `t` here
        width=button_width * colspan + button_gap * (colspan - 1),  # Pass width here
        height=button_height,  # Pass height here
    ).place(
        x=x_start + (button_width + button_gap) * col,
        y=y_start + (button_height + button_gap) * row,
    )

def button_click(button_number):
    if button_number == "AC":
        button_clear()
    elif button_number == "=":
        button_equal()
    elif button_number == "+":
        button_add()
    elif button_number == "-":
        button_subtract()
    elif button_number == "*":
        button_multiply()
    elif button_number == "/":
        button_divide()
    elif button_number == "%":
        button_percentage()
    else:
        print(button_number)
        current_text = box.get()
        box.delete(0, tk.END)
        box.insert(0, current_text + button_number)
def button_clear():
    box.delete(0, tk.END)
def button_add():
    first_number_str = box.get()
    global first_number 
    global operation 
    first_number = float(first_number_str)
    operation = "+"
    box.delete(0, tk.END)
def button_subtract():
    first_number_str = box.get()
    global first_number 
    global operation 
    first_number = float(first_number_str)
    operation = "-"
    box.delete(0, tk.END)
def button_multiply():
    first_number_str = box.get()
    global first_number 
    global operation 
    first_number = float(first_number_str)
    operation = "*"
    box.delete(0, tk.END)
def button_divide():
    first_number_str = box.get()
    global first_number 
    global operation 
    first_number = float(first_number_str)
    operation = "/"
    box.delete(0, tk.END)
def button_percentage():
    first_number_str = box.get()
    global first_number 
    global operation 
    first_number = float(first_number_str)
    operation = "%"
    box.delete(0, tk.END)
def button_equal():
    second_number = float(box.get())
    box.delete(0, tk.END)
    if operation == "+" :
        box.insert(0,first_number + second_number)
    elif operation == "-" :
        box.insert(0,first_number - second_number)
    elif operation == "/" :
        box.insert(0,first_number / second_number)
    elif operation == "*" :
        box.insert(0,first_number * second_number)
    elif operation == "%" :
        box.insert(0,first_number % second_number)
with sr.Microphone() as src :
    box.delete(0, tk.END)
    box.insert(0, "Speak Now...")
    print("Speak Now...")
    audio = rec.listen(src)
    try:
            text = rec.recognize_google(audio)
            print("You said:", text)

            # here we are going to check for operation keywords 
            if "plus" in text or "add" or "+" in text :
                # we extract the numbers and perform the addition 
                numbers = [int(word) for word in text.split() if word.isdigit()]
                if len(numbers) >= 2:
                    result = numbers[0] + numbers[1]
                    print(f"Result: {result}")
                    box.delete(0, tk.END)
                    box.insert(0, result)
            elif "subtract" in text or "minus" in text :
                # we extract the numbers and perform the addition 
                numbers = [int(word) for word in text.split() if word.isdigit()]
                if len(numbers) >= 2:
                    result = numbers[0] - numbers[1]
                    print(f"Result: {result}")
                    box.delete(0, tk.END)
                    box.insert(0, result)
            elif "multiply by" in text or "times" in text :
                # we extract the numbers and perform the addition 
                numbers = [int(word) for word in text.split() if word.isdigit()]
                if len(numbers) >= 2:
                    result = numbers[0] * numbers[1]
                    print(f"Result: {result}")
                    box.delete(0, tk.END)
                    box.insert(0, result)
            elif "divided by" in text or "over" in text :
                # we extract the numbers and perform the addition 
                numbers = [int(word) for word in text.split() if word.isdigit()]
                if len(numbers) >= 2:
                    result = numbers[0] / numbers[1]
                    print(f"Result: {result}")
                    box.delete(0, tk.END)
                    box.insert(0, result)
            else:
                print("No operation detected!")
                box.delete(0, tk.END)
                box.insert(0, "No operation detected!")
    except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            box.delete(0, tk.END)
            box.insert(0, "Sorry, I didn't catch that.")
    except sr.RequestError as e:
            print(f"Could not request results; {e}")
            box.delete(0, tk.END)
            box.insert(0, "Request error occurred!")
    
# Run the main loop
wind.mainloop()
