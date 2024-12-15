# Password Generator

A simple and secure Python script to generate random passwords. This project provides two modes:

1. **Fixed-Length Password**: A 16-character password with a mix of letters, digits, and special characters.
2. **Custom-Length Password**: User inputs the desired length, and the password is generated using a 50-30-20 formula for letters, numbers, and special characters.

---

## Features

- **Two Modes of Operation**:
  - **Fixed-Length Mode**: Generates a secure 16-character password automatically.
  - **Custom-Length Mode**: Allows the user to specify a custom password length.
- **Character Sets**:
  - Includes uppercase and lowercase letters, digits, and special characters (`@#$%&*`).
- **Randomized Composition**:
  - Uses Python’s `random` module to ensure unpredictable and secure password generation.
  - Characters are shuffled for added randomness.
- **Customizable Formula**:
  - Default distribution: 50% letters, 30% numbers, 20% special characters.
  - Easy to modify based on user requirements.

---

## Tech Stack

- **Programming Language**: Python 3.x
- **Libraries Used**:
  - `random`: For generating random numbers and shuffling lists.
  - `string`: Provides predefined character sets such as letters, digits, and punctuation.
  - `math`: Used for calculating password component distribution.

---

### Steps to Run the Project

1. **Clone the repository**:
    ```bash
    git clone https://github.com/farhat-1203/password-generator.git
    cd google-translate-script
    ```
2. **Run the script**:
    ```bash
    python3 new_GUI.py
    ```

## Project Structure

```plaintext
python-password-generator/
├── new_GUI.py   # Main script for password generation
├── LICENSE                 # License (optional)
└── README.md               # Documentation
