*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html
*** Test Cases ***
#Handling iframes
#    Open Browser  ${url}  chrome
#    Maximize Browser Window
#    Sleep    2s
#    Select Frame    id=singleframe
#    Input Text    xpath=//input[@type='text']    Nike
#    Sleep    3s
#    Unselect Frame
#    Close Browser
Handling nested iframes
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Click Element    xpath=//a[text()='Iframe with in an Iframe']
    Select Frame    xpath=//iframe[@src='MultipleFrames.html']
    Select Frame    xpath=//iframe[contains(@src,'SingleFrame')]
    Input Text    xpath=//input[@type='text']    Nike
    Sleep    3s
    Unselect Frame
    Unselect Frame
    Close Browser