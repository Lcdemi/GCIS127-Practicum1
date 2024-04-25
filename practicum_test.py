import practicum

def test_slice_1_9():
    #setup
    expected = [1, 3, 5, 7, 9]

    #invoke
    actual = practicum.slice([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 10, 2)

    #analyze
    assert expected == actual

def test_slice_empty():
    #setup
    expected = []

    #invoke
    actual = practicum.slice([], 0, 10, 2)

    #analyze
    assert expected == actual

def test_list_to_string_strings():
    #setup
    expected = "0 - a\n1 - b\n2 - c\n3 - d\n"

    #invoke
    actual = practicum.list_to_string(["a", "b", "c", "d"])

    #analyze
    assert expected == actual

def test_list_to_string_nums():
    #setup
    expected = "0 - 1\n1 - 2\n2 - 3\n3 - 4\n"

    #invoke
    actual = practicum.list_to_string([1, 2, 3, 4])

    #analyze
    assert expected == actual

def test_list_to_string_floats():
    #setup
    expected = "0 - 1.0\n1 - 2.0\n2 - 3.0\n3 - 4.0\n"

    #invoke
    actual = practicum.list_to_string([1.0, 2.0, 3.0, 4.0])

    #analyze
    assert expected == actual

def test_collatz_6():
    #setup
    expected = "6 3 10 5 16 8 4 2 1"

    #invoke
    actual = practicum.collatz(6)

    #analyze
    assert expected == actual

def test_collatz_1():
    #setup
    expected = "1"

    #invoke
    actual = practicum.collatz(1)

    #analyze
    assert expected == actual

def test_collatz_0():
    #setup
    expected = "Undefined"

    #invoke
    actual = practicum.collatz(0)

    #analyze
    assert expected == actual

def test_collatz_3():
    #setup
    expected = "3 10 5 16 8 4 2 1"

    #invoke
    actual = practicum.collatz(3)

    #analyze
    assert expected == actual