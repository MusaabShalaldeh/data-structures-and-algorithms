from code_challenges.hashmap_repeated_word.hashmap_repeated_word import repeated_word




def test_repeated_word():
    # Arrange
    string = "Once upon a time, there was a brave princess who..."
    expected = "a"
    # Actual
    actual = repeated_word(string)
    # Assert
    assert actual == expected


def test_repeated_word_two():
    # Arrange
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    expected = "it"
    # Actual
    actual = repeated_word(string)
    # Assert
    assert actual == expected

def test_repeated_word_three():
    # Arrange
    string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    expected = "summer"
    # Actual
    actual = repeated_word(string)
    # Assert
    assert actual == expected


def test_repeated_word_edge_case_one():
    # Arrange
    string = ""
    expected = ""
    # Actual
    actual = repeated_word(string)
    # Assert
    assert actual == expected


def test_repeated_word_edge_case_two():
    # Arrange
    string = "-1 -5 allo -5 allo"
    expected = "allo"
    # Actual
    actual = repeated_word(string)
    # Assert
    assert actual == expected
