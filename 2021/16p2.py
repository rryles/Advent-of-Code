#!/usr/bin/python3


class Packet:
    def __init__(self, data):
        self.version = int(data[:3], 2)
        self.type = int(data[3:6], 2)
        self.data_used = 6
        data = data[6:]

        self.literal = None
        self.children = []

        if self.type == 4:
            # Literal value
            self.literal = 0
            done = False
            while not done:
                done = data[0] == "0"
                self.literal *= 16
                self.literal += int(data[1:5], 2)
                self.data_used += 5
                data = data[5:]
        else:
            self.len_mode = int(data[0])
            if self.len_mode == 0:  # length in bits
                self.len = int(data[1:16], 2)
                self.data_used += 16
                data = data[16:]
                children_data_used = 0
                while self.len > children_data_used:
                    child = Packet(data)
                    self.data_used += child.data_used
                    children_data_used += child.data_used
                    data = data[child.data_used:]
                    self.children.append(child)

            else:   # Length in packets
                self.len = int(data[1:12], 2)
                self.data_used += 12
                data = data[12:]
                for _ in range(self.len):
                    child = Packet(data)
                    self.data_used += child.data_used
                    data = data[child.data_used:]
                    self.children.append(child)

    def get_version_total(self):
        return self.version + sum([child.get_version_total() for child in self.children])

    def evaluate(self):
        if self.type == 0:
            return sum([child.evaluate() for child in self.children])
        if self.type == 1:
            product = 1
            for child in self.children:
                product *= child.evaluate()
            return product
        if self.type == 2:
            return min([child.evaluate() for child in self.children])
        if self.type == 3:
            return max([child.evaluate() for child in self.children])
        if self.type == 4:
            return self.literal
        if self.type == 5:
            first = self.children[0].evaluate()
            second = self.children[1].evaluate()
            return 1 if first > second else 0
        if self.type == 6:
            first = self.children[0].evaluate()
            second = self.children[1].evaluate()
            return 1 if first < second else 0
        if self.type == 7:
            first = self.children[0].evaluate()
            second = self.children[1].evaluate()
            return 1 if first == second else 0


with open('16.txt') as input:
    data = ""

    for c in input.readline().rstrip():
        if c == "0":
            data += "0000"
        elif c == "1":
            data += "0001"
        elif c == "2":
            data += "0010"
        elif c == "3":
            data += "0011"
        elif c == "4":
            data += "0100"
        elif c == "5":
            data += "0101"
        elif c == "6":
            data += "0110"
        elif c == "7":
            data += "0111"
        elif c == "8":
            data += "1000"
        elif c == "9":
            data += "1001"
        elif c == "A":
            data += "1010"
        elif c == "B":
            data += "1011"
        elif c == "C":
            data += "1100"
        elif c == "D":
            data += "1101"
        elif c == "E":
            data += "1110"
        elif c == "F":
            data += "1111"

    packet = Packet(data)

    print(packet.evaluate())
