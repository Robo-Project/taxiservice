*** Settings ***
Library          ../pythonscripts/TaxiService.py
Library          Collections


*** Tasks ***

Drive taxi
    #${length}  Return length
    Return And Log Length
    ${price}  Return price
    ${time}  Return time
    #Log  ${length}
    Log  ${price}
    Log  ${time}


*** Keywords ***

Return And Log Length
    ${length}  Return length
    Log  ${length}
# Run taxi job
# Keywords as method names
