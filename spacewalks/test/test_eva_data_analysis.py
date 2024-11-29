
import pytest
from eva_data_analysis import(text_to_duration, calculate_crew_size)

def test_text_to_duration_float():
    """ Test that text_to_duration returns expected ground truth values
    for typical durations with a non-zero minute component
    """     
    #input_value = "10:20"
    assert abs(text_to_duration("10:20") - 10.33333333) < 1e-5

def test_text_to_duration_integer():
    """
    Test that...
    """
    assert text_to_duration("10:00") == 10

# refactor version
def test_calculate_crew_size():
    """
    Test that calculate_crew_size returns expected ground truth values
    for typical crew values
    """
    actual_result = calculate_crew_size("Valentina Tereshkova;")
    expected_result = 1
    assert actual_result == expected_result

    actual_result = calculate_crew_size("Judith Resnik; Sally Ride;")
    expected_result = 2
    assert actual_result == expected_result


@pytest.mark.parametrize("input_value, expected_result", [
    ("Valentina Tereshkova;", 1),
    ("Judith Resnik; Sally Ride;", 2),
])
def test_calculate_crew_size2(input_value, expected_result):
    ""
    Test that calculate_crew_size returns expected ground truth values
    for typical crew values
    ""
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result


# Edge cases
def test_calculate_crew_size_edge_cases():
    """
    Test that calculate_crew_size returns expected ground truth values
    for edge case where crew is an empty string
    """
    actual_result = calculate_crew_size("")
    assert actual_result is None

test_text_to_duration_float()
test_text_to_duration_integer()
test_calculate_crew_size()
#test_calculate_crew_size2('input_value', 'expected_result')
test_calculate_crew_size_edge_cases()