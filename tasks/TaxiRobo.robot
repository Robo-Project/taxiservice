*** Settings ***
Library          ../pythonscripts/TaxiService.py
Library          Collections


*** Tasks ***

Drive taxi
    ${length}  Return length
    ${price}  Return price
    ${time}  Return time
    Log  ${length}
    Log  ${price}
    Log  ${time}



# Run taxi job
# Keywords as method names
