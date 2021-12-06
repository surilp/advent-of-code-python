from utils.utils import file_to_collection

class ComboBreaker:

    def __init__(self, file_name, subject_number):
        self.card_public_key = None
        self.door_public_key = None
        self.file_name = file_name
        self.subject_number = subject_number
        self.process_data()

    def process_data(self):
        raw_data = file_to_collection(self.file_name)
        self.card_public_key = int(raw_data[0])
        self.door_public_key = int(raw_data[1])

    def get_encryption(self):
        card_loop = self.find_loop(self.card_public_key)
        door_loop = self.find_loop(self.door_public_key)

        card_encryption = self.encryption(door_loop, self.card_public_key)
        door_encryption = self.encryption(card_loop, self.door_public_key)

        if card_encryption == door_encryption:
            return card_encryption
        raise Exception("No encrpytion found")


    def find_loop(self, target):
        value = 1
        i = 0
        while value != target:
            value = value * self.subject_number
            value = value % 20201227
            i += 1
        return i

    def encryption(self, loop_size, subject_number):
        value = 1
        while loop_size != 0:
            value = subject_number * value
            value = value % 20201227
            loop_size -= 1
        return value