
import pytest
from eva_data_analysis import text_to_duration

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

test_text_to_duration_float()
test_text_to_duration_integer()