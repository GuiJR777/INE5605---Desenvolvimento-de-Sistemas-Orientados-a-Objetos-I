import pytest

from ordenacao import Ordenacao


class TestOrdenacao:
    def test_when_given_a_empty_list_should_return_a_empty_list(self):
        # Arrange
        list_to_order = []
        expected_result = ""

        # Act
        result = Ordenacao(list_to_order).ordena()

        # Assert
        assert result == expected_result

    def test_when_given_a_list_with_one_element_should_return_the_same_list(
        self,
    ):
        # Arrange
        list_to_order = [1]
        expected_result = "1"

        # Act
        result = Ordenacao(list_to_order).ordena()

        # Assert
        assert result == expected_result

    def test_when_given_a_ordered_list_should_return_the_same_ordered_list(
        self,
    ):
        # Arrange
        list_to_order = [1, 2, 3, 4, 5]
        expected_result = "1,2,3,4,5"

        # Act
        result = Ordenacao(list_to_order).ordena()

        # Assert
        assert result == expected_result

    def test_when_given_a_unordered_list_should_return_a_ordered_list(self):
        # Arrange
        list_to_order = [4, 1, 3, 5, 2]
        expected_result = "1,2,3,4,5"

        # Act
        result = Ordenacao(list_to_order).ordena()

        # Assert
        assert result == expected_result

    def test_when_given_a_inverted_ordered_list_should_return_a_ordered_list(
        self,
    ):
        # Arrange
        list_to_order = [5, 4, 3, 2, 1]
        expected_result = "1,2,3,4,5"

        # Act
        result = Ordenacao(list_to_order).ordena()

        # Assert
        assert result == expected_result

    def test_when_given_a_list_with_repeated_elements_should_return_a_ordered_list_without_repeated_elements(
        self,
    ):
        # Arrange
        list_to_order = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
        expected_result = "1,1,2,2,3,3,4,4,5,5"

        # Act
        result = Ordenacao(list_to_order).ordena()

        # Assert
        assert result == expected_result
