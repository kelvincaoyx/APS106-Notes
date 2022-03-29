#####################################################
# APS106 Winter 2022 - Lab 7 - Chemical Eqn Checker #
#####################################################

######################################################
# PART 1 - Complete the function below to deocompose
#          a compound formula written as a string
#          in a dictionary
######################################################

def mol_form(compound_formula):
    """(str) -> dictionary
    When passed a string of the compound formula, returns a dictionary 
    with the elements as keys and the number of atoms of that element as values.
    
    >>> mol_form("C2H6O")
    {'C': 2, 'H': 6, 'O': 1}
    >>> mol_form("CH4")
    {'C': 1, 'H': 4}
    """
     
    # TODO your code here

    #creating the dictionary everything will be stored in
    mol_dict = dict()
    
    #collecting all the elements and their counts inside a list
    element_list = []
    element_count_list = []
    
    #a dummy variable for me to easily add to the list
    temp_element = ""
    temp_count = ""
    
    #iterating through the string
    for i in range(len(compound_formula)):
        #this block basically checks if the block are letters and then adds it to a dummy variable
        if compound_formula[i].isalpha():
            #adds to dummy variable
            temp_element += compound_formula[i]
            try: 
                #if the next number is a number, this means that the element name is done
                #and it shoudl be added to the element list
                if compound_formula[i+1].isnumeric():
                    element_list.append(temp_element)
                    temp_element = ""
                
                #if the next letter is a capital letter, it means that it is a new element. Add
                #what we have right now and then create a new dummy variable
                if compound_formula[i+1].isupper():
                    element_list.append(temp_element)
                    temp_element = ""
                    element_count_list.append(1)
            
            #this block is here to account for the last element of the string, If it goes over while
            #it is still alpha, it means that the count is 1. I just add this to the element list
            except:
                element_list.append(temp_element)
                element_count_list.append(1)
        
        #this block means that we are dealing with numbers/ the count of the elements
        else:
            #adds the number to a accumulator
            temp_count += str(compound_formula[i])
            
            #checks if next element is a letter, if so, add what we have to the list
            try: 
                if compound_formula[i+1].isalpha():
                    element_count_list.append(temp_count)
                    temp_count = ""
            
            #this block accounts for the last element of the string, if somehtign goes wrong, we know
            #that we can just add it to the count list
            except:
                element_count_list.append(temp_count)
    
    #iterates through both the element list and count list and adds it to the dictionary
    for i in range(len(element_list)):
        
        #since elements can end up in same formula muiple times (like H) we need to update the dictionary
        #instead of just adding it
        if element_list[i] not in mol_dict:
            mol_dict.update({element_list[i]:0})
        
        #updates the dictionary
        mol_dict.update({element_list[i]:int(element_count_list[i]) + mol_dict[element_list[i]]})     
    
    return mol_dict
            



######################################################
# PART 2 - Complete the function below that takes two 
#          tuples representing one side of a
#          chemical equation and returns a dictionary
#          with the elements as keys and the total
#          number of atoms in the entire expression
#          as values.
######################################################
    
def expr_form(expr_coeffs,expr_molecs):
    """
    (tuple (of ints), tuple (of dictionaries)) -> dictionary
    
    This function accepts two input tuples that represent a chemical expression,
    or one side of a chemical equation. The first tuple contains integers that
    represent the coefficients for molecules within the expression. The second
    tuple contains dictionaries that define these molecules. The molecule
    dictionaries have the form {'atomic symbol' : number of atoms}. The order
    of the coefficients correspond to the order of molecule dictionaries.
    The function creates and returns a dictionary containing all elements within
    the expression as keys and the corresponding number of atoms for each element
    within the expression as values.
    
    For example, consider the expression 2NaCl + H2 + 5NaF
    
    >>> expr_form((2,1,5), ({"Na":1, "Cl":1}, {"H":2}, {"Na":1, "F":1}))
    {'Na': 7, 'Cl': 2, 'H': 2, 'F': 5}
    
    """
    # TODO your code here
    
    #initializeing variable
    return_dict = dict()
    
    #iterating through the compounds
    for compound in range(len(expr_coeffs)):
        #iterating through each element in the compound
        for key in expr_molecs[compound]:
            #checks if the element is already in the dictionary, if not, it will add the element to it
            if key not in return_dict:
                return_dict.update({key:0})
            
            #updateds the element in the dictionary accounting for the coefficient
            new_number = return_dict[key] + expr_molecs[compound][key] * expr_coeffs[compound]
            #print(new_number)
            return_dict.update({key:new_number})
            
    return return_dict

########################################################
# PART 3 - Check if two dictionaries representing
#          the type and number of atoms on two sides of
#          a chemical equation contain different
#          key-value pairs
########################################################

def find_unbalanced_atoms(reactant_atoms, product_atoms):
    """
    (Dict,Dict) -> Set
    
    Determine if reactant_atoms and product_atoms contain equal key-value
    pairs. The keys of both dictionaries are strings representing the 
    chemical abbreviation, the value is an integer representing the number
    of atoms of that element on one side of a chemical equation.
    
    Return a set containing all the elements that are not balanced between
    the two dictionaries.
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 1, "Cl" : 2})
    {'Na'}
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 2, "Cl" : 2})
    set()
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "F" : 2, "Cl" : 2})
    {'F', 'Na'}
    """
    
    # TODO your code here
    #creates a set that i will eventually return
    not_balanced_atoms = set()
    
    #this first line checks between both reactants and products, checking if there are any differences in them
    if len(set(reactant_atoms.keys()).difference(set(product_atoms.keys()))) != 0 or len(set(product_atoms.keys()).difference(set(reactant_atoms.keys()))) != 0:
        #print(set(reactant_atoms.keys()).difference(set(product_atoms.keys())))
        
        #if there are any differences, they will return the union of all the differences in a set
        return set(product_atoms.keys()).difference(set(reactant_atoms.keys())).union(set(reactant_atoms.keys()).difference(set(product_atoms.keys())) )
    
    #if there are not differences in the elements, this will iterate through both dictionary, making sure
    #the values matches each other. If they don't they are added to a set
    for element in reactant_atoms:
        if reactant_atoms[element] != product_atoms[element]:
            not_balanced_atoms.add(element)
    
    return not_balanced_atoms

    
########################################################
# PART 4 - Check if a chemical equation represented by
#          two nested tuples is balanced
########################################################

def check_eqn_balance(reactants,products):
    """
    (tuple,tuple) -> Set
    
    Check if a chemical equation is balanced. Return any unbalanced
    elements in a set.
    
    Both inputs are nested tuples. The first element of each tuple is a tuple
    containing the coefficients for molecules in the reactant or product expression.
    The second element is a tuple containing strings of the molecules within
    the reactant or product expression. The order of the coefficients corresponds
    to the order of the molecules. The function returns a set containing any
    elements that are unbalanced in the equation.
    
    For example, the following balanced equation
    C3H8 + 5O2 <-> 4H2O + 3CO2
    
    would be input as the following two tuples:
    reactants: ((1,5), ("C3H8","O2"))
    products: ((4,3), ("H2O","CO2"))
    
    >>> check_eqn_balance(((1,5), ("C3H8","O2")),((4,3), ("H2O","CO2")))
    set()
    
    Similarly for the unbalanced equation
    
    C3H8 + 2O2 <-> 4H2O + 3CO2
    
    would be input as the following two tuples:
    reactants: ((1,2), ("C3H8","O2"))
    products: ((4,3), ("H2O","CO2"))
    
    >>> check_eqn_balance(((1,2), ("C3H8","O2")),((4,3), ("H2O","CO2")))
    {'O'}
    
    """
    
    #TODO your code here

    #reactants dictionary creation
    reactants_dict = []
    
    #going through the reactants, creating the dictionary version of them
    for formula in reactants[1]:
        reactants_dict.append(mol_form(formula))
        
    #accounting for the coefficients of the reactants
    reactants_expr = expr_form(reactants[0], tuple(reactants_dict))
    
    #print(reactants_expr)
    
    #products dictionary creation
    product_dict = []
    
    #going through the products, creating the dictionary version of them
    for formula in products[1]:
        product_dict.append(mol_form(formula))
    
    #accounting for the coefficients of the reactants
    products_expr = expr_form(products[0], tuple(product_dict))
    
    #print(products_expr)

    #returning the differences between the reactants and the products, if there are any
    return find_unbalanced_atoms(reactants_expr,products_expr)

if __name__ == '__main__':
    import doctest
    doctest.testmod()