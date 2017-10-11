from Roundoff import roundoff

taxRate = 0.10
importedTaxRate = 0.05


def getItemTax(qty, taxStatus, imported, itemPrice):
    itemPrice = float(itemPrice)
    itemPrice *= qty
    if taxStatus :
        if imported :
            itemPrice += itemPrice * taxRate + itemPrice * importedTaxRate

            #itemPrice  = round(itemPrice, 2)
            #print "after import tax ", itemPrice
            itemPrice = roundoff(itemPrice,taxStatus, imported)
            #print "after roundoff ", itemPrice
            return itemPrice
        else:
            itemPrice += itemPrice * taxRate
            itemPrice = roundoff(itemPrice,taxStatus, imported)
            return itemPrice
    else :
        if imported :
            #print "before import tax ", itemPrice
            itemPrice += itemPrice * importedTaxRate
            #print "after import tax ", itemPrice
            itemPrice = roundoff(itemPrice,taxStatus, imported)
            #print "after round off ", itemPrice
            return itemPrice
        else :
            return itemPrice
