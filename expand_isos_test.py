from expand import expand_material


def test_expand():
    element1 = {
                "chemical_symbol" : "Te",
                "molar_mass" : "10",
                "atomic_number" : 1,
                "isotopes" : [
                    {
                        "atomic_abundance" : 1/1000.0,
                        "mass_number" : 2
                    },
                    {
                        "atomic_abundance" : 2/1000.0,
                        "mass_number" : 3
                    }
                ]
            }

    element2 = {
                "chemical_symbol" : "St",
                "molar_mass" : "20",
                "atomic_number" : 4,
                "isotopes" : [
                    {
                        "atomic_abundance" : 1/1000.0,
                        "mass_number" : 5
                    },
                    {
                        "atomic_abundance" : 2/1000.0,
                        "mass_number" : 6
                    }
                ]
            }

    material = {
            "density" : '1.00',
            "elements" : [{
                    "chemical_symbol" : "Te",
                    "mass_fraction" : "0.3",
                            },
                            {
                    "chemical_symbol" : "St",
                    "mass_fraction" : "0.7",
                            }]
            }

    elements = {
            "Te":element1,
            "St":element2
            }
    result = expand_material(material, elements) 
    assert(result["Z2A1"] == 1.00 * 0.3 * 1/3.0 / 10)
    assert(result["Z3A1"] == 1.00 * 0.3 * 2/3.0 / 10)
    assert(result["Z5A4"] == 1.00 * 0.7 * 1/3.0 / 20)
    assert(result["Z6A4"] == 1.00 * 0.7 * 2/3.0 / 20)
