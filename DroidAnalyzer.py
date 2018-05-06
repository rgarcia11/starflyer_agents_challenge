"""
Analyses Droids
"""
def create_structure(hash):
    """
    Recursive method that creates a JSON-like structure from a hash.
    Refer to Starflyers.py for the input
    Parameters
        hash. A hash expression
    Returns
        base_structure. The structure of the given hash. Dictionary.
    """
    index = 0
    character = hash[index]
    base_structure = {}
    if character.islower():
        while character != ',' and character != '(' and index < len(hash):
            character = hash[index]
            index = index + 1
        if character == ',':
            base_structure = create_structure(hash[index:])
            if 'constant' not in base_structure:
                base_structure['constant'] = 1
            else:
                base_structure['constant'] = base_structure['constant'] + 1
        elif character == '(':
            second_index = index
            parenthesis = 1
            while parenthesis > 0:
                character = hash[second_index]
                if character == '(':
                    parenthesis = parenthesis + 1
                elif character == ')':
                    parenthesis = parenthesis - 1
                second_index = second_index + 1
            if second_index+1 < len(hash):
                if hash[second_index] == ',':
                    base_structure = create_structure(hash[second_index+1:])
            if 'function' not in base_structure:
                base_structure['function'] = {}
                base_structure['function']['1'] = create_structure(hash[index:second_index-1])
            else:
                function_index = 1
                existe = 1
                while existe:
                    if str(function_index) not in base_structure['function']:
                        existe = 0
                    function_index = function_index + 1
                base_structure['function'][str(function_index)] = create_structure(hash[index:second_index-1])
        elif index == len(hash):
            if 'constant' not in base_structure:
                base_structure['constant'] = 1
            else:
                base_structure['constant'] = base_structure['constant'] + 1
        else:
            print('Fatal error. This droid is doin me a bamboozle.')
    else:
        while character != ',' and character != '(' and index < len(hash):
            character = hash[index]
            index = index + 1
        if character == ',':
            base_structure = create_structure(hash[index:])
            if 'variable' not in base_structure:
                base_structure['variable'] = 1
            else:
                base_structure['variable'] = base_structure['variable'] + 1
        elif index == len(hash):
            if 'variable' not in base_structure:
                base_structure['variable'] = 1
            else:
                base_structure['variable'] = base_structure['variable'] + 1
        else:
            print('Fatal error. This droid is doin me a bamboozle.')
    return base_structure

def compare_structure(base_structure, comparable_structure):
    """
    Compares two structures created with the create_structure method.
    """
    guilty = 0
    for element in base_structure.keys():
        if element not in comparable_structure:
            guilty = 1
            break
        elif element == 'function':
            functions = base_structure[element].keys()
            comparable_functions = comparable_structure[element].keys()
            if len(functions) != len(comparable_functions):
                guilty = 1
                break
            else:
                for function in functions:
                    sub_guilty = 0
                    match_function = ''
                    comparable_functions = comparable_structure[element].keys()
                    for comparable_function in comparable_functions:
                        sub_guilty = compare_structure(base_structure[element][function],comparable_structure[element][comparable_function])
                        if not sub_guilty:
                            match_function = comparable_function
                            break
                    if sub_guilty:
                        guilty = 1
                        break
                    else:
                        comparable_structure[element].pop(comparable_function)
        else:
            if base_structure[element] != comparable_structure[element]:
                guilty = 1
    return guilty

def analyze_droid(hashes):
    """
    Every droid has a history of software updates and each software update is tagged with a hash.
    A hash is a term built recursively from variable, constant, and function symbols as follows:
    • any variable and any constant is a hash;
    • if each h1, . . . , hk is a hash and f is a function symbol, then f(h1, . . . , hk) is a hash.
    As a security measure, a well-kept secret from the general population, the Commonwealth enforces the following policy on droid software updates:
    for each droid, the tags of any software updates must be compatible.
    Two hashes h1 and h2 are compatible if there is a mapping θ from variables to hashes such that h1θ = h2θ, where h1θ (resp., h2θ) denotes the simultaneous replacement of any occurrence of each variable x in h1 (resp., h2) with the hash θ(x).
    A sequence of hashes h1, . . . , hn is compatible if there is θ such that h1θ, . . . , hnθ are all equal.
    For example, assume that X, Y, Z are variables, c, d are constants, and f, g are function symbols, and consider the hashes h1, h2, and h3 as follows:
    h1 : f(X, g(c)) h2 : f(f(Y ), Z) h3 : f(c, g(Y, d))
    Observe that h1 and h2 are compatible because the mapping θ = {X → f(Y ), Z → g(c)} satisfies h1θ = h2θ.
    However, any other pair from h1, h2, and h3 is not compatible.
    Therefore, any sequence of hashes containing h1, h2, and h3 is not compatible because there is no mapping θ such that h1θ = h2θ = h3θ.

    A droid is found guilty when not all of its hashes are compatible.

    Parameters
        hashes. List of hashes of a droid
    Returns
        1 if guilty
        0 if analysis is inconclusive.
    """
    guilty = 0
    base_structure = {}
    for hash in hashes:
        if not base_structure:
            base_structure = create_structure(hash)
        else:
            comparable_structure = create_structure(hash)
            guilty = compare_structure(base_structure,comparable_structure)
            if guilty:
                break
    return guilty
