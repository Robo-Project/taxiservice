*** Settings ***
Library          ../pythonscripts/TaxiService.py
Library          Collections


*** Tasks ***

Drive taxi
    ${result}  Return Taxi Drive Details
    Log  ${result}

