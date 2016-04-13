import Elemlib as el

def test_read_isotope():
    f = [
    """
                      1      0.999850E+02
    
    """]
    ite = iter(f)
    iso = el.parse_isotope(ite)
    assert iso["mass_number"] == 1
    assert iso["atomic_abundance"] == float("0.999850E+02")

def test_read_element():
    f = [
    """
h       0.100790E+01   1      0.899000E-04   2""" ,
"""     1      0.999850E+02""",
"""
                                                 2      0.150000E-01
    
    """]
    ite = iter(f)
    elem_name, elem = el.parse_element(ite)
    assert elem_name == "h"
    assert elem["chemical_symbol"] == "h"
    assert elem["molar_mass"] == "0.100790E+01"
    assert elem["atomic_number"] == "1"
    assert elem["density"] == "0.899000E-04"
    assert elem["num_isotopes"] == 2
    assert len(elem["isotopes"]) == 2
