from test_color_code import test_number_to_pair, test_pair_to_number, test_manual
from reference_manual import print_reference_manual

if __name__ == "__main__":
    # Run strong tests for color code logic and manual
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    test_manual()
    print("All tests passed!\n")
    # Print the reference manual for wiring personnel
    print_reference_manual()
