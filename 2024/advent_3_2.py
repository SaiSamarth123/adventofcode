import re

data = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""


def process_memory(memory):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, data)
    result = 0

    mul_enabled = True

    instructions = re.findall(r"[a-zA-Z]+\([^\)]*\)", memory)

    for instr in instructions:
        if instr == "do()":
            mul_enabled = True
        elif instr == "don't()":
            mul_enabled = False
        elif instr.startswith("mul") and mul_enabled:
            nums = re.findall(r"\d+", instr)
            if len(nums) == 2:
                print(nums[0], " ", nums[1])
                result += mul(int(nums[0]), int(nums[1]))
                print("result: ", result)

    return result


def mul(a, b):
    print(a * b)
    return a * b


total = process_memory(data)

print(total)
