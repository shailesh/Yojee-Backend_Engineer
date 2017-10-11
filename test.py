from Inputs import getInput
from ItemType import getTaxStatus
from ItemTax import getItemTax

import csv

def csv_writer(data):

    with open("output.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        header=['SaleTax','Total']
        writer.writerow(header)
        content=list()
        #for line in data:
            #content+=line
        writer.writerow(data)

while True:
    filename = raw_input('Enter \'Filename\' or \'Done\' to exit\t')
    print "\n"
    if filename.lower()=='done':
        break
    all_items = getInput(filename)

    total_without_tax = 0
    total_with_tax = 0

    for item in all_items:
        qty = int(item[0][0])
        taxStatus, imported = getTaxStatus(item[0]) # Returns True if tax is applied on item and True if item is imported.
        itemTax = getItemTax(qty, taxStatus, imported, item[1])
        total_without_tax += float(item[1])
        total_with_tax += float(itemTax)
        print item[0], " : ", itemTax

    salesTax = total_with_tax - total_without_tax
    salesTax = format(salesTax)
    total_with_tax = format(total_with_tax)
    datalist=list()
    datalist=[salesTax,total_with_tax];

    csv_writer(datalist)



    print "Sales Taxes : ", salesTax

    print "Total : ", total_with_tax,"\n"

