SimpleOTP Generator 

● Project Title

SimpleOTP Generator

● Overview of the Project

The SimpleOTP Generator is a lightweight Python class designed to create secure, fixed-length, random strings suitable for use as One-Time Passwords (OTPs) or temporary codes. It utilizes Python's built-in random and string modules to ensure high entropy and allows the developer to easily select the desired character set (e.g., digits only, alphanumeric) for the generated OTP.

● Features

The SimpleOTP class provides the following features through easy-to-access @property decorators:

1.Digits Only: Generates an OTP composed exclusively of numerical digits (0-9).

2.Uppercase Alphanumeric: Generates an OTP composed of uppercase letters (A-Z) and digits (0-9).

3.Lowercase Alphanumeric: Generates an OTP composed of lowercase letters (a-z) and digits (0-9).

4.All Characters: Generates an OTP using a mix of lowercase letters, uppercase letters, and digits.

5.Customizable Length: The length of the generated OTP is defined when initializing the SimpleOTP class.

● Technologies/Tools Used

Language: Python 3.x

Standard Library Modules:

   random: Used for cryptographic-quality random selection of characters.

   string: Used to easily access predefined character sets (e.g., ascii_lowercase, digits).

● Steps to Install & Run the Project

Since this is a single, self-contained Python script, no special installation is required beyond having a standard Python 3 interpreter.

Save the Code: Save the provided code into a file named simple_otp.py.

Execute the Script: Open your terminal or command prompt, navigate to the directory where you saved the file, and run:

                      python simple_otp.py



The script will execute the demonstration code at the bottom, printing four different types of generated OTPs to the console.

● Instructions for Testing

To verify that the generator is working correctly and securely, follow these testing steps:

1. Verify Length: Check that all four output strings have the length specified during initialization (7 in the provided example).

2. Verify Randomness: Run the script multiple times (at least 5-10 times). The output OTPs for each property should be unique every time.

3. Verify Character Sets (Per Property):

      digits: Confirm that the output only contains characters from 0 through 9.

      uppercase_digits: Confirm the output contains only characters from A-Z and 0-9. It should not contain any lowercase letters.

      smallcase_digits: Confirm the output contains only characters from a-z and 0-9. It should not contain any uppercase letters.

      all: Confirm the output can contain a mix of uppercase, lowercase, and digits.

● Screenshots (Output Example)

<img width="303" height="93" alt="Screenshot 2025-11-25 021135" src="https://github.com/user-attachments/assets/55aced31-c475-43bb-bf86-127338c951d1" />
