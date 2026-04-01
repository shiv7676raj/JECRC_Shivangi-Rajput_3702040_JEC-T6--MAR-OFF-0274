*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://the-internet.herokuapp.com/javascript_alerts
*** Test Cases ***
#Simple Alert
#    Open Browser  ${url}  chrome
#    Maximize Browser Window
#    Sleep    2s
#    Click Button    xpath=//button[@onclick='jsAlert()']
#    Sleep    5s
#    Handle Alert
#    Sleep    2s
#    Close Browser
#Confirmation Alert
#    Open Browser  ${url}  chrome
#    Maximize Browser Window
#    Sleep    2s
#    Click Button    xpath=//button[@onclick='jsConfirm()']
#    Sleep    5s
#    Handle Alert  action=DISMISS
#    Sleep    2s
#    Close Browser
Prompt Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Click Button    xpath=//button[@onclick='jsPrompt()']
    Sleep    5s
    Input Text Into Alert    Hellewww  action=DISMISS
    Sleep    2s
    Close Browser