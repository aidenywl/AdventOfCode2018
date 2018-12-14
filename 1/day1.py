

def part_1(file: str):
    return sum(map(int, file))


def part_2(input_data: str):
    past_frequencies = set()
    frequency = 0
    data = list(map(int, input_data))

    while True:
        for change in data:
            frequency += change

            if frequency in past_frequencies:
                return frequency

            past_frequencies.add(frequency)


if __name__ == "__main__":
    part1_input = open("input.txt", 'r')
    print(f"Answer for part 1: {part_1(part1_input)}")

    part2_input = open("input2.txt", 'r')
    print(f"Answer for part 2: {part_2(part2_input)}")


