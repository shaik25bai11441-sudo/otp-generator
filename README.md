

import random
import string


S_chars = string.ascii_lowercase 
B_chars = string.ascii_uppercase 
D_chars = string.digits

ALL_chars = S_chars + B_chars + D_chars

class SimpleOTP:
 
    def __init__(self, length):
      
        self.length = length

    def generate_otp(self, char_set):

        return "".join(random.choices(char_set, k=self.length))


    @property
    def digits(self):
        
        return self.generate_otp(D_chars)

    @property
    def uppercase_digits(self):
       
        return self.generate_otp(B_chars + D_chars)

    @property
    def smallcase_digits(self):
       
        return self.generate_otp(S_chars + D_chars)

    @property
    def all(self):
      
        return self.generate_otp(ALL_chars)


otp_generator = SimpleOTP(7) 




print("OTP (Digitss Only): " + otp_generator.digits)
print("OTP (Upper & Digits): " + otp_generator.uppercase_digits)
print("OTP (Lower & Digits): " + otp_generator.smallcase_digits)
print("OTP (All Chars): " + otp_generator.all)
