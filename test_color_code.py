from color_code import get_color_from_pair_number, get_pair_number_from_color
from reference_manual import generate_reference_manual

def test_number_to_pair(num, exp_major, exp_minor):
    major, minor = get_color_from_pair_number(num)
    assert major == exp_major and minor == exp_minor

def test_pair_to_number(major, minor, exp_num):
    assert get_pair_number_from_color(major, minor) == exp_num

def test_manual():
    lines = generate_reference_manual().splitlines()
    assert lines[0].startswith("1: White Blue")
    assert lines[-1].startswith("25: Violet Slate")

if __name__ == "__main__":
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    test_manual()
    print("All tests passed!")
