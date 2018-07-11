from gas_pump import *
from bcca.test import should_print, with_inputs


@should_print
@with_inputs('ten', '20')
def test_input_dollars_ten_20(output):
    result = input_dollars()

    assert result == 20
    assert output == '''

dollars:ten
Please choose a valid option!
dollars:20
'''


@should_print
@with_inputs('40')
def test_is_valid_gallons(output):
    assert is_valid_gallons('10') == True
    assert is_valid_gallons('21') == True
    assert is_valid_gallons('') == False
    assert is_valid_gallons('ten') == False
    assert is_valid_gallons('0') == False
