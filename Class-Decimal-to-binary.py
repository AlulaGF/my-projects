class DecimalToBinary:
    def __init__(self, decimal_number):
        self.decimal_number = decimal_number

    def convert(self):
        # Special case for 0
        if self.decimal_number == 0:
            return "0"

        binary = ""
        number = self.decimal_number

        while number > 0:
            remainder = number % 2
            binary = str(remainder) + binary
            number = number // 2

        return binary

    def display(self):
        binary_number = self.convert()
        print(f"Decimal Number: {self.decimal_number}")
        print(f"Binary Number : {binary_number}")

converter = DecimalToBinary(13)
converter.display()