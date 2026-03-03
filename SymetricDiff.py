def get_set_from_user(set_number):
    """
    Prompts the user to enter elements for a set.
    Returns a Python set of integers.
    """
    user_input = input(f"Enter elements of Set {set_number} separated by spaces: ")
    
    # Convert input string into a set of integers
    try:
        result_set = set(map(int, user_input.split()))
        return result_set
    except ValueError:
        print("Please enter only integers separated by spaces.")
        return get_set_from_user(set_number)


def find_symmetric_difference(set1, set2):
    """
    Returns the symmetric difference of two sets.
    """
    return set1 ^ set2


def main():
    print("=== Symmetric Difference Finder ===")
    
    set1 = get_set_from_user(1)
    set2 = get_set_from_user(2)
    
    result = find_symmetric_difference(set1, set2)
    
    print("\nSet 1:", set1)
    print("Set 2:", set2)
    print("Symmetric Difference:", result)


if __name__ == "__main__":
    main()