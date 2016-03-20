OPPOSITE_DIR = {
    "SOUTH": "NORTH",
    "NORTH": "SOUTH",
    "WEST": "EAST",
    "EAST": "WEST",
}

def dirReduc(arr):
    stack = []
    for direction in arr:
        if stack and stack[-1] == OPPOSITE_DIR[direction]:
            stack.pop()
        else:
            stack.append(direction)
    return stack
