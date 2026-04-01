*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://testautomationpractice.blogspot.com/
*** Test Cases ***
#Simple Alert
#    Open Browser  ${url}  chrome
#    Maximize Browser Window
#    Sleep    2s
#    Click Button    xpath=//button[@onclick='myFunctionAlert()']
#    Sleep    5s
#    Handle Alert
#    Sleep    2s
#    Page Should Contain    I am an alert box!
#    Close Browser
#Confirmation Alert
#    Open Browser  ${url}  chrome
#    Maximize Browser Window
#    Sleep    2s
#    Click Button    xpath=//button[@onclick='myFunctionConfirm()']
#    Sleep    5s
#    Handle Alert
#    Page Should Contain    Press a button!
#    Sleep    2s
#    Close Browser
Prompt Alert
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Click Button    xpath=//button[@onclick='myFunctionPrompt()']
    Sleep    5s
    Input Text Into Alert  gggg  action=DISMISS
    Page Should Contain    Please enter your name:
    ${text}=  Get Text    xpath=//p[@id='demo']
    Sleep    2s
    Close Browser