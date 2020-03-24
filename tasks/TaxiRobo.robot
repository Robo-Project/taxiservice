*** Settings ***
Library          ../pythonscripts/TaxiService.py
Library          Collections


*** Tasks ***

Drive taxi
    @{results}      Create List
    ${results}      Drive taxi
    Log     ${results}

# Run taxi job
# Keywords as method names
