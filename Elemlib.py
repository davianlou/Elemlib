
def parse_element(iterator):
    line = iterator.__next__()
    fields = line.split()
    element = {}
    element["chemical_symbol"] = fields[0]
    element["molar_mass"] = fields[1]
    element["atomic_number"] = fields[2]
    element["density"] = fields[3]
    num_isotope = int(fields[4])
    element["num_isotopes"] = num_isotope 
    element["isotopes"] = []
    for _ in range(num_isotope):
        isotope = parse_isotope(iterator)
        element["isotopes"].append(isotope)
    return (fields[0], element)

def parse_isotope(iterator):
    line = iterator.__next__()
    fields = line.split()
    isotope = {}
    isotope["mass_number"] = int(fields[0])
    isotope["atomic_abundance"] = float(fields[1])
    return isotope

def parse_file(filename):
    elements = {}
    with open(filename) as f:
        lines = f.readlines()
        iterator = iter(lines)
        try:
            while 1:
                element_name, element_dict = parse_element(iterator)
                elements[element_name] = element_dict
        except StopIteration:
            pass
    return elements
