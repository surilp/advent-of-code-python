from utils.utils import file_to_collection


class BinaryDigit():
    def __init__(self, size):
        self.ones = 0
        self.zeros = 0
        self.size = size
        self.gamma_bit = None
        self.epsilon_bit = None

    def process_digit(self, digit):
        if self.gamma_bit and self.epsilon_bit:
            return
        if digit == '1':
            self.ones += 1
        elif digit == '0':
            self.zeros += 1
        if self.ones > self.size // 2:
            self.gamma_bit = '1'
            self.epsilon_bit = '0'
        elif self.zeros > self.size // 2:
            self.gamma_bit = '0'
            self.epsilon_bit = '1'


def binary_diagnostic(input_file):
    data = file_to_collection(input_file)
    if data:
        binary_digits = [BinaryDigit(len(data)) for _ in range(len(data[0]))]
    for item in data:
        for idx, digit in enumerate(item):
            binary_digits[idx].process_digit(digit)
    gamma_bits = ''.join([digit.gamma_bit for digit in binary_digits])
    epsilon_bits = ''.join([digit.epsilon_bit for digit in binary_digits])
    return int(gamma_bits, 2) * int(epsilon_bits, 2)


def binary_diagnostic2(input_File):
    data = file_to_collection(input_File)
    oxygen_bits = ''.join(oxygen_CO2(data, 0, "O"))
    co2_bits = ''.join(oxygen_CO2(data, 0, "CO2"))
    return int(oxygen_bits, 2) * int(co2_bits, 2)


def oxygen_CO2(data, idx, type):
    if len(data) == 1:
        return data
    zeros = list(filter(lambda item: item[idx] == "0", data))
    ones = list(filter(lambda item: item[idx] == "1", data))
    if type == "O":
        if len(ones) >= len(zeros):
            return oxygen_CO2(ones, idx + 1, type)
        else:
            return oxygen_CO2(zeros, idx + 1, type)
    elif type == "CO2":
        if len(ones) < len(zeros):
            return oxygen_CO2(ones, idx + 1, type)
        else:
            return oxygen_CO2(zeros, idx + 1, type)
