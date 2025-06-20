import io
import base64
import math
import matplotlib.pyplot as plt

def text_to_rules(text):
    rules = {}
    for rule in text.split(', '):
        key, value = map(str.strip, rule.split("->"))
        rules[key] = value
    return rules


def derivation(rules, axiom, steps):
    derived = axiom
    for _ in range(steps):
        derived = ''.join(rules.get(char, char) for char in derived)
    return derived

def generate_coordinates(sequence, seg_length, initial_heading, angle_increment):
    x, y = 0, 0
    heading = initial_heading
    coordinates = [(x, y)]
    stack = []
    for command in sequence:
        if command in "FGRL":
            x += seg_length * math.cos(math.radians(heading))
            y += seg_length * math.sin(math.radians(heading))
            coordinates.append((x, y))
        elif command == "+":
            heading -= angle_increment
        elif command == "-":
            heading += angle_increment
        elif command == "[":
            stack.append((x, y, heading))
        elif command == "]":
            x, y, heading = stack.pop()
            coordinates.append((x, y))
    return coordinates

def generate_image(params):
    rules = text_to_rules(params.rules)
    axiom = params.axiom
    iterations = params.iterations
    segment_length = params.segment_length
    initial_heading = params.initial_heading
    angle_increment = params.angle_increment
    thickness = params.thickness
    color = params.color


    final_sequence = derivation(rules, axiom, iterations)
    coordinates = generate_coordinates(final_sequence, segment_length, initial_heading, angle_increment)

    plt.figure(figsize=(8, 8))
    plt.plot(*zip(*coordinates), linewidth=thickness, color=color)
    plt.axis("equal")
    plt.axis("off")
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()


    return image_base64

