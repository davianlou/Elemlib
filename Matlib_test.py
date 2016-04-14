import Matlib as ml

def test_read_material():
    f = [
    """
water    	    1.00   2""",
"""                              h  11.111        1""",
"""                              o  88.889        8
    """]
    ite = iter(f)
    material_name, mat = ml.parse_material(ite)
    assert material_name == "water"
    assert mat["material_name"] == "water"
    assert mat["density"] == "1.00"
    assert mat["num_elements"] == "2"
def test_read_element():
    f = [
    """
                              h  11.111        1""",
"""                              o  88.889        8
    """]
    ite = iter(f)
    elem = ml.parse_element(ite)
    assert elem["chemical_symbol"] == "h"
    assert elem["mass_fraction"] == "11.111"
    assert elem["atomic_number"] == "1"
    
