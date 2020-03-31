*** Settings ***
Library          ../pythonscripts/TaxiService.py
Library          Collections


*** Tasks ***

Drive taxi
    ${result}  return json
    Log  ${result}

*** Keywords ***

Return And Log Length
    
# Run taxi job
# Keywords as method names
