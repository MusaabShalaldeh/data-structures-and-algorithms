from stack_queue_brackets import __version__
from stack_queue_brackets.stack_queue_brackets import ValidateBrackets


def test_version():
    assert __version__ == '0.1.0'


def test_stack_is_balanced():
    # Arange
    expected = True
    string = "()[]"
    # Actual
    actual = ValidateBrackets(string)
    # Assert
    assert actual == expected



def test_stack_is_not_balanced():
    # Arange
    expected = False
    string = "()[}]"
    # Actual
    actual = ValidateBrackets(string)
    # Assert
    assert actual == expected


def test_stack_balanced_empty():
    # Arange
    expected = True
    string = ""
    # Actual
    actual = ValidateBrackets(string)
    # Assert
    assert actual == expected


def test_stack_balanced_one_bracket():
    # Arange
    expected = False
    string = "("
    # Actual
    actual = ValidateBrackets(string)
    # Assert
    assert actual == expected


def test_stack_balanced_one_closing_bracket():
    # Arange
    expected = False
    string = "}"
    # Actual
    actual = ValidateBrackets(string)
    # Assert
    assert actual == expected


def test_stack_is_balanced_with_text():
    # Arange
    expected = True
    string = "{}{Code}[Fellows](())"
    # Actual
    actual = ValidateBrackets(string)
    # Assert
    assert actual == expected



def test_stack_is_not_balanced_with_text():
    # Arange
    expected = False
    string = "{}{Code}[Fellows]((}))"
    # Actual
    actual = ValidateBrackets(string)
    # Assert
    assert actual == expected



def test_stack_is_balanced_wrong_input():
    # Arange
    expected = None
    string = 5
    # Actual
    actual = ValidateBrackets(string)
    # Assert
    assert actual == expected

