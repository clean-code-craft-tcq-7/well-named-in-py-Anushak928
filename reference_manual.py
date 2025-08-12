from color_code import MAJOR_COLORS, MINOR_COLORS, get_color_from_pair_number

def generate_reference_manual():
    return "\n".join(
        f"{n}: {maj} {minr}"
        for n in range(1, len(MAJOR_COLORS) * len(MINOR_COLORS) + 1)
        for maj, minr in [get_color_from_pair_number(n)]
    )

def print_reference_manual():
    print("25-Pair Color Code Reference Manual")
    print("-" * 40)
    print(generate_reference_manual())
