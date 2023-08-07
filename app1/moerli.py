import random

class number():
    def __init__(self, max=256, bin=""):
        if bin != "":
            self.value = self.bin_to_dec(bin)
        else :    
            self.value =int(random.random()*max)

    def __str__(self):
        return str(self.value)
    
    def get_bin(self):
        bin_value = ""
        int_value = self.value
        while int_value > 0:
            bin_value = str(int_value%2) + bin_value
            int_value //= 2
        return bin_value.zfill(8)
    
    def get_dec(self):
        return self.value

    def is_bin(self, eingabe):
        int_value = self.bin_to_dec(eingabe)
        return (self.value==int_value)
    
    @staticmethod
    def bin_to_dec(eingabe):
        eingabe = eingabe.replace(" ", "").replace("." ,"", 1).replace("l", "1")
        int_value = 0
        for i in eingabe:
            int_value = int_value * 2 + int(i) 
        return int_value
    
#zahl = number()
#print(zahl, zahl.get_bin())
#print(zahl.is_bin(input("Binary: ")))