def getInput(filename):
    filename = "inputs/"+filename+".txt"
    inp = open(filename,'r')

    # used " at " as delimiter and not "at" to avoid erraneous splitting like chocol'at'es
    all_items = [line.strip().split(' at ') for line in inp]

    inp.close()

    return all_items
