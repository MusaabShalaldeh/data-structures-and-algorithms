from stack_queue_animal_shelter import __version__
from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter, EmptyQueue, WrongShelterInput
import pytest


def test_version():
    assert __version__ == '0.1.0'



def test_animal_shelter_happy_path():
    # Arrange
    shelter = AnimalShelter()
    shelter.enqueue("CAT")
    shelter.enqueue("CAT")
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    shelter.enqueue("dog")
    expected = "cat"

    # Actual
    actual = shelter.dequeue("cat")

    # Assert
    assert actual == expected


def test_expected_failure():
    # Arrange
    with pytest.raises(EmptyQueue) as excinfo:
        #Actual
        dequeue_fail_on_shelter()

    #Assert
    assert str(excinfo.value) == "Animal Shelter Queue is empty, can't remove or return a value!"



def dequeue_fail_on_shelter():
    shelter = AnimalShelter()
    shelter.dequeue("cat")



def test_wrong_input():
    # Arrange
    with pytest.raises(WrongShelterInput) as excinfo:
        #Actual
        wrong_shelter_input()

    #Assert
    assert str(excinfo.value) == "Wrong Input, has to be either cat or dog!"



def wrong_shelter_input():
    shelter = AnimalShelter()
    shelter.enqueue("5")
