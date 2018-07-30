def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # your code here

    index = text.find(symbol, 0, len(text))
    if index == -1:
        return None
    index2 = text.find(symbol, index + 1, len(text))
    if index2 == -1:
        return None
    else:
        return index2



if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')