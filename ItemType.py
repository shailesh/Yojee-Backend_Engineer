inp = open("inputs/TaxExemptedGoods.txt",'r')

# used " at " as delimiter and not "at" to avoid erraneous splitting like chocol'at'es
tax_excluded_items = [line.strip() for line in inp]

inp.close()


def getTaxStatus(itemName):
    taxApplied = True

    for ele in tax_excluded_items:
        if(itemName.find(ele)!=-1):
            taxApplied = False
            break

    if(itemName.find('imported')!=-1):
        imported = True
    else:
        imported = False

    if(taxApplied):
        if(imported):
            return True, True  # sales tax not applied but item is imported.
        else:
            return True, False # Item gets normal tax but not imported.

    else:
        if(imported):
            return False, True
        else:
            return False, False
