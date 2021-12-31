from __future__ import annotations
from utils.utils import file_to_collection
from typing import NamedTuple


def extract_reboot_steps(reboot_step_string: str):
    on_or_off, coordinates = reboot_step_string.split()
    x, y, z = coordinates.split(",")
    x = list(map(int, x.replace("x=", "").split("..")))
    y = list(map(int, y.replace("y=", "").split("..")))
    z = list(map(int, z.replace("z=", "").split("..")))
    x_inc = 1 if x[1] >= x[0] else -1
    y_inc = 1 if y[1] >= y[0] else -1
    z_inc = 1 if z[1] >= z[0] else -1
    x.append(x_inc)
    y.append(y_inc)
    z.append(z_inc)
    return on_or_off, x, y, z


def get_reboot_steps(input_file):
    return map(extract_reboot_steps, file_to_collection(input_file))


def part1(input_file):
    result = set()
    for on_or_off, x_range, y_range, z_range in get_reboot_steps(input_file):
        for x in range(x_range[0], x_range[1] + x_range[2], x_range[2]):
            if x > 50 or x < -50:
                continue
            for y in range(y_range[0], y_range[1] + y_range[2], y_range[2]):
                if y > 50 or y < -50:
                    continue
                for z in range(z_range[0], z_range[1] + z_range[2], z_range[2]):
                    if z > 50 or z < -50:
                        continue
                    if on_or_off == "on":
                        result.add((x, y, z))
                    elif on_or_off == "off" and (x, y, z) in result:
                        result.remove((x, y, z))
    return len(result)

def calculate_volume(x_range, y_range, z_range):
    x = x_range[1] - x_range[0]
    y = y_range[1] - y_range[0]
    z = z_range[1] - z_range[0]
    return x * y * z


class RectangularPrism:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        x = self.x[1] - self.x[0]
        y = self.y[1] - self.y[0]
        z = self.z[1] - self.z[0]
        return x * y * z

    def __contains__(self, item):
        if item.x[0] >= self.x[0] and \
                item.x[1] <= self.x[1] and \
                item.y[0] >= self.y[0] and \
                item.y[1] <= self.y[1] and \
                item.z[0] >= self.z[0] and \
                item.z[1] <= self.z[1]:
            return True

    def intersect(self, item):
        intersect = [None, None, None]
        current = tuple(self.__dict__.values())
        other = tuple(item.__dict__.values())
        for idx in range(len(current)):
            if current[idx][1] > other[idx][0] and other[idx][1] > current[idx][0]:
                intersect[idx] = True
        return all(intersect)

    def subtract(self, other):
        if not self.intersect(other):
            return [self]
        if self in other:
            return []

        x = sorted((self.x[0], self.x[1], other.x[0], other.x[1]))
        y = sorted((self.y[0], self.y[1], other.y[0], other.y[1]))
        z = sorted((self.z[0], self.z[1], other.z[0], other.z[1]))
        result = []
        for min_x, max_x in zip(x, x[1:]):
            for min_y, max_y in zip(y, y[1:]):
                for min_z, max_z in zip(z, z[1:]):
                    rectangular_prism = RectangularPrism((min_x, max_x), (min_y, max_y), (min_z, max_z))
                    if rectangular_prism in self and not rectangular_prism.intersect(other):
                        result.append(rectangular_prism)
        return result


def part2(input_file):
    steps = get_reboot_steps(input_file)
    prisms = []
    for step in steps:
        state, x, y, z = step
        rect_prism = RectangularPrism((x[0], x[1] + 1), (y[0], y[1] + 1), (z[0], z[1] + 1))
        temp = []
        for prism in prisms:
            temp += prism.subtract(rect_prism)
        if state == 'on':
            temp.append(rect_prism)
        prisms = temp
    return sum(prism.volume() for prism in prisms)
