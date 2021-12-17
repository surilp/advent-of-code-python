from utils.utils import file_to_collection
from collections import deque
from functools import reduce

class Packet:
    HEX_TO_BIN_MAP = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }

    def get_binary(self):
        binary = []
        for hex in self.transmission:
            binary.append(Packet.HEX_TO_BIN_MAP[hex])
        return ''.join(binary)

    def __init__(self, transmission, current_idx=[0], queue=deque()):
        self.transmission = transmission
        self.current_idx = current_idx
        self.queue = queue
        self.packet_version = self.get_packet_version_and_type_id()
        self.packet_type_id = self.get_packet_version_and_type_id()
        self.sub_packets = []
        self.literal_value = self.get_literal_value()
        pass

    def __add__(self, other):
        return self.literal_value + other

    def __radd__(self, other):
        return self.literal_value + other

    def __rmul__(self, other):
        return self.literal_value * other

    def __mul__(self, other):
        return self.literal_value * other.literal_value


    def get_literal_value(self):
        if self.packet_type_id == 4:
            return self.literal_value_helper()
        else:
            self.process_operator_packet()

        if self.packet_type_id == 0:
            return sum(self.sub_packets)
        elif self.packet_type_id == 1:
            return reduce(lambda a, b: a * b, self.sub_packets)
        elif self.packet_type_id == 2:
            return min(self.sub_packets, key = lambda a: a.literal_value).literal_value
        elif self.packet_type_id == 3:
            return max(self.sub_packets, key = lambda a: a.literal_value).literal_value
        elif self.packet_type_id == 5:
            return 1 if self.sub_packets[0].literal_value > self.sub_packets[1].literal_value else 0
        elif self.packet_type_id == 6:
            return 1 if self.sub_packets[0].literal_value < self.sub_packets[1].literal_value else 0
        elif self.packet_type_id == 7:
            return 1 if self.sub_packets[0].literal_value == self.sub_packets[1].literal_value else 0

    def literal_value_helper(self):
        bin_result = []
        while self.current_idx[0] < len(self.transmission):
            self.fill_queue(5)
            bits = []
            while len(bits) < 5:
                bits.append(self.queue.popleft())
            if len(bits) == 5:
                for idx in range(1, 5):
                    bin_result.append(bits[idx])
                if bits[0] == '0':
                    break
        return int(''.join(bin_result), 2)

    def process_operator_packet(self):
        self.fill_queue(1)
        length_type_id = self.queue.popleft()
        if length_type_id == "0":
            len_sub_packets = self._process_bits(15)
            bits_to_be_processed = len_sub_packets
            while bits_to_be_processed > 0:
                start_bits = (len(self.transmission) - self.current_idx[0]) * 4 + len(self.queue)
                self.sub_packets.append(Packet(self.transmission, self.current_idx, self.queue))
                end_bits = (len(self.transmission) - self.current_idx[0]) * 4 + len(self.queue)
                bits_to_be_processed -= start_bits - end_bits
        else:
            num_of_sub_packets = self._process_bits(11)
            current_packet = 0
            while current_packet < num_of_sub_packets:
                self.sub_packets.append(Packet(self.transmission, self.current_idx, self.queue))
                current_packet += 1

    def _process_bits(self, size):
        self.fill_queue(size)
        bits = []
        while len(bits) < size:
            bits.append(self.queue.popleft())
        return int(''.join(bits), 2)

    def get_packet_version_and_type_id(self):
        self.fill_queue(3)
        version_binary = []
        while len(version_binary) < 3:
            version_binary.append(self.queue.popleft())
        return int(''.join(version_binary), 2)

    def fill_queue(self, min_size):
        while self.current_idx[0] < len(self.transmission) and len(self.queue) < min_size:
            hex = self.transmission[self.current_idx[0]]
            for binary in Packet.HEX_TO_BIN_MAP[hex]:
                self.queue.append(binary)
            self.current_idx[0] += 1


class PacketDecoder:

    def __init__(self, input_file, idx = 0):
        self.transmissions = list(map(list, file_to_collection(input_file)))
        self.packet = Packet(self.transmissions[idx], [0], deque())

    def get_version_sum(self):
        sum = [0]
        self._dfs(self.packet, sum)
        return sum[0]

    def packet_literal_value(self):
        return self.packet.literal_value

    def _dfs(self, packet, sum):
        if packet.packet_version:
            sum[0] += packet.packet_version
        for sub_packet in packet.sub_packets:
            self._dfs(sub_packet, sum)
