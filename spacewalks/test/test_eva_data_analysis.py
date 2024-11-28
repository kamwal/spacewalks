
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


def test_calculate_crew_size (): # FIXME
    """
    Test that the code is calulating the number of the crew size.
      It is checking what particular crue member is on board#FIXME
    """

    # Typical value 1
    actual_result = calculate_crew_size("Mike Collins;") #FIXME
    expected_result = 1 #FIXME
    assert actual_result == expected_result

    # Typical value 2
    actual_result =  calculate_crew_size("Owen Garriott;Allen Bean;") #FIXME
    expected_result = 2 #FIXME
    assert actual_result == expected_result

# Edge cases
def test_calculate_crew_size_edge_cases(): # FIXME
    """
    Test that check that there is no crew present  #FIXME
    """

    # Typical value 1
    actual_result =  test_calculate_crew_size_edge_cases("")#FIXME
    #expected_result = 0 #FIXME
    assert actual_result == None

test_text_to_duration_float()
test_text_to_duration_integer()
test_calculate_crew_size()
test_calculate_crew_size_edge_cases()