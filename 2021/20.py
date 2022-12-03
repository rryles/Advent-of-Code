#!/usr/bin/python3


class Image:
    def __init__(self, lines=None, width=None, height=None, background="."):
        self.background = background
        if lines:
            self.rows = [line.rstrip() for line in lines]
            self.width = len(self.rows[0])
            self.height = len(self.rows)
        else:
            self.width = width
            self.height = height
            self.lines = [[background] * width] * height

    def __str__(self):
        return "\n".join(self.rows)

    def get_pixel(self, x, y):
        if (0 <= x < self.width) and (0 <= y < self.height):
            return self.rows[y][x]
        return self.background

    def get_binary(self, x, y):
        result = 0
        for dy in range(3):
            for dx in range(3):
                result *= 2
                if self.get_pixel(x + dx - 2, y + dy - 2) == "#":
                    result += 1
        return result

    def count_set_pixels(self):
        count = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.rows[y][x] != self.background:
                    count += 1
        return count


class Rule:
    def __init__(self, line):
        self.rule = line.rstrip()
        assert(len(self.rule) == 512)

    def apply(self, input: Image):
        w = input.width + 2
        h = input.height + 2
        rows = ["".join([self.rule[input.get_binary(x, y)] for x in range(w)]) for y in range(h)]
        if input.background == ".":
            background = self.rule[0]
        else:
            background = self.rule[511]
        return Image(lines=rows, background=background)


if __name__ == "__main__":
    with open('20.txt') as input:
        rule = Rule(input.readline())

        input.readline()  # Ignore blank line

        image = Image(input.readlines())

        for _ in range(2):
            image = rule.apply(image)

        print(image.count_set_pixels())

        for _ in range(48):
            image = rule.apply(image)

        print(image.count_set_pixels())
