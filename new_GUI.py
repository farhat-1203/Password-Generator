import random
import math
import tkinter as tk
from tkinter import messagebox

# Function to generate password with custom or fixed length
def generate_password():
    try:
        if var_choice.get() == "Custom":
            pass_len = int(entry_length.get())
            if pass_len < 8 or pass_len > 16:
                raise ValueError("Password length should be between 8 and 16 characters.")
        else:  # Fixed length option
            pass_len = 16  # Fixed length of 16 characters

        alpha = "abcdefghijklmnopqrstuvwxyz"
        num = "0123456789"
        special = "@#$%&*"
        
        # Length of password by 50-30-20 formula
        alpha_len = pass_len // 2
        num_len = math.ceil(pass_len * 30 / 100)
        special_len = pass_len - (alpha_len + num_len)

        password = []

        def generate_pass(length, array, is_alpha=False):
            for i in range(length):
                index = random.randint(0, len(array) - 1)
                character = array[index]
                if is_alpha:
                    case = random.randint(0, 1)
                    if case == 1:
                        character = character.upper()
                password.append(character)

        # Generate parts of the password
        generate_pass(alpha_len, alpha, True)
        generate_pass(num_len, num)
        generate_pass(special_len, special)

        # Shuffle the generated password list
        random.shuffle(password)

        # Convert List To string
        gen_password = "".join(password)
        label_result.config(text=f"Generated Password: {gen_password}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Set up the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x350")

# Title label
label_title = tk.Label(root, text="Password Generator", font=("Arial", 16))
label_title.pack(pady=10)

# Choice for fixed or custom length
var_choice = tk.StringVar(value="Custom")
radio_fixed = tk.Radiobutton(root, text="Fixed Length (16 characters)", variable=var_choice, value="Fixed", font=("Arial", 12))
radio_fixed.pack(pady=5)
radio_custom = tk.Radiobutton(root, text="Custom Length", variable=var_choice, value="Custom", font=("Arial", 12))
radio_custom.pack(pady=5)

# Length input label (only visible when 'Custom' is selected)
label_length = tk.Label(root, text="Enter Password Length (8-16):", font=("Arial", 12))
label_length.pack(pady=5)

# Length input field (only visible when 'Custom' is selected)
entry_length = tk.Entry(root, font=("Arial", 12))
entry_length.pack(pady=5)

# Generate password button
button_generate = tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password)
button_generate.pack(pady=10)

# Result label
label_result = tk.Label(root, text="Generated Password: ", font=("Arial", 12))
label_result.pack(pady=20)

# Run the GUI
root.mainloop()
