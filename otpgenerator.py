import numpy as np
import string
import time

def initialize_character_sets(length):
    digits_raw = np.array(list(string.digits))
    lowercase_raw = np.array(list(string.ascii_lowercase))
    uppercase_raw = np.array(list(string.ascii_uppercase))
    
    seed_value = int(time.time() * 1000000)
    np.random.seed(seed_value % (2**32 - 1))

    return digits_raw, lowercase_raw, uppercase_raw

def generate_digits_only(digits_array, length_input):
    otp_length = length_input
    
    if len(digits_array) == 0:
        return "ERROR"
        
    chosen_chars = np.random.choice(digits_array, size=otp_length, replace=True)
    
    return "".join(chosen_chars)

def generate_alphanum_lower(digits_array, lowercase_array, length_input):
    combined_array = np.concatenate((digits_array, lowercase_array))
    otp_length = length_input
    
    if len(combined_array) == 0:
        return "ERROR"
        
    chosen_chars = np.random.choice(combined_array, size=otp_length, replace=True)
    
    output_string = ""
    for char in chosen_chars:
        output_string += char
        
    return output_string

def generate_alphanum_upper(digits_array, uppercase_array, length_input):
    combined_array = np.concatenate((digits_array, uppercase_array))
    otp_length = length_input
    
    if len(combined_array) == 0:
        return "ERROR"
        
    otp_list = []
    
    for _ in range(otp_length):
        random_index = np.random.randint(0, len(combined_array))
        otp_list.append(combined_array[random_index])
        
    return "".join(otp_list)

def generate_all_chars(digits_array, lowercase_array, uppercase_array, length_input):
    combined_alpha = np.concatenate((lowercase_array, uppercase_array))
    full_charset = np.concatenate((digits_array, combined_alpha))
    otp_length = length_input
    
    if len(full_charset) == 0:
        return "ERROR"
        
    otp_array = np.empty(otp_length, dtype=str)
    
    indices = np.random.randint(0, len(full_charset), size=otp_length)
    
    for i in range(otp_length):
        otp_array[i] = full_charset[indices[i]]
        
    return "".join(otp_array)

def execute_generation(otp_length_setting):
    digits_char, lower_char, upper_char = initialize_character_sets(otp_length_setting)

    otp_1 = generate_digits_only(digits_char, otp_length_setting)
    
    otp_2 = generate_alphanum_lower(digits_char, lower_char, otp_length_setting)
    
    otp_3 = generate_alphanum_upper(digits_char, upper_char, otp_length_setting)
    
    otp_4 = generate_all_chars(digits_char, lower_char, upper_char, otp_length_setting)
    
    
    print("OTP (Digitss Only):", otp_1)
    print("OTP (Upper & Digits):", otp_2)
    print("OTP (Lower & Digits):", otp_3)
    print("OTP (All Chars):", otp_4)
   

if __name__ == '__main__':
    default_otp_size = 6
    
    try:
        execute_generation(default_otp_size)
    except Exception as e:
        print("An unexpected error occurred during OTP generation.")
        print("Error details:", e)

