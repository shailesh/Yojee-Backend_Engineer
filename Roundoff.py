from __future__ import division


def roundoff(itemPrice, taxStatus, imported):
    nearestRoundoff = 1 / 0.05
    nearestValue =  round((itemPrice*nearestRoundoff)/nearestRoundoff, 2)


    # According to testcases if last digit is betweem 1 to 5 we have to round to 0.05 but if greater than 5 and less than 9 then roundoff to 0.09
    lastDigit = int((nearestValue*100)%10)

    # Add trailing zeroes
    if lastDigit == 0:
        return str(nearestValue)+'0'

    # round off to nearest 0.05
    if(lastDigit >=1 and lastDigit <5):
        error = (5.0 - lastDigit) /100
        nearestValue += error
    return str(nearestValue)
