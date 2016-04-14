def parse_material(iterator):
    line = iterator.__next__()
    fields = line.split()
    material = {}
    material["material_name"] = fields[0]
    material["density"] = fields[1]
    num_elements = int(fields[2])
    material["num_elements"] = fields[2]
    material["elements"] = []
    for _ in range(num_elements):
        element = parse_element(iterator)
        material["elements"].append(element)
    return (fields[0], material)

def parse_element(iterator):
    line = iterator.__next__()
    fields = line.split()
    element = {}
    element["chemical_symbol"] = fields[0]
    element["mass_fraction"] = fields[1]
    element["atomic_number"] = fields[2]
    return element

def parse_file(filename):
    materials = {}
    with open(filename) as f:
        lines = f.readlines()
        iterator = iter(lines)
        try:
            while 1:
                material_name, material_dict = parse_material(iterator)
                materials[material_name] = material_dict
        except StopIteration:
            pass
    return materials

Materials = parse_file("materials.txt")
