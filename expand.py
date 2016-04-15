import Elemlib
import Matlib

def get_isotope_percentage(target_isotope, all_isotopes):
    # print(target_isotope, all_isotopes)
    target_abundance = target_isotope["atomic_abundance"]
    sum_abundance = 0
    for isotope in all_isotopes:
        sum_abundance += isotope["atomic_abundance"]
    return target_abundance / sum_abundance

def expand_material(material, elements=Elemlib.Elements):
    components = { }
    for __element in material["elements"]:
        chemical_symbol = __element["chemical_symbol"]
        element = elements[chemical_symbol]
        for isotope in element["isotopes"]:
            isotope_identifier = "Z%sA%s" % (isotope["mass_number"], element["atomic_number"])
            isotope_amount = float(material["density"]) * float(__element["mass_fraction"]) * get_isotope_percentage(isotope, element["isotopes"]) / float(element["molar_mass"])
            if isotope_identifier in components:
                components[isotope_identifier] = components[isotope_identifier] + isotope_amount
            else:
                components[isotope_identifier] = isotope_amount
    return components

sample_material = Matlib.Materials["water"]
print(expand_material(sample_material))

