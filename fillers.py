import numpy as np

def fill_by_appending(structure):
    """
    Fills the structure with 25 random integers
    from [0, 300] range

    """

    for _ in range(25):
        structure.append(np.random.randint(0, 301))
    return structure

def fill_mixed(structure):
    """
    Fills the list once with append, then with insert """
    i = 0
    while i < 25:
        structure.append(np.random.randint(0, 301))
        i += 1
        if i == 25:
            break
        else:
            structure.insert(np.random.randint(0, 301))
            i += 1

def fill_random(structure):
    """ Fills the list randomly, either at start, or beggining """
    i = 0
    while i < 25:
        rand = np.random.random_sample(1)
        if rand < 0.5:
            structure.append(np.random.randint(0, 301))
            i += 1
        else:
            structure.insert(np.random.randint(0, 301))
            i += 1
    return structure
