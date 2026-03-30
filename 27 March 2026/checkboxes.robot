*** Settings ***
Documentation  handling checkboxes
Library  SeleniumLibrary
*** Variables ***
${url}  https://the-internet.herokuapp.com/
*** Test Cases ***
#Handling Checkboxes
#    [Documentation]  herokuapp checkboxes
#    Open Browser  ${url}  chrome
#    Maximize Browser Window
#    Sleep    2s
#    Click Element    xpath=//a[text()='Checkboxes']
#    Page Should Contain Checkbox   xpath=(//input[@type="checkbox"])[1]
#    Select Checkbox    xpath=(//input[@type="checkbox"])[1]
#    Sleep    2s
#    Unselect Checkbox    xpath=(//input[@type="checkbox"])[2]
#    Sleep    2s
#    Close Browser

Checkboxes
    [Documentation]  checkboxes
    Open Browser  https://testautomationpractice.blogspot.com/  chrome
    Maximize Browser Window
    Sleep    2s
    Page Should Contain Checkbox   xpath=//input[@id='tuesday']
    Select Checkbox    xpath=//input[@id='tuesday']
    Sleep    2s
    Select Checkbox    xpath=//input[@id='monday']
    Sleep    2s
    Select Radio Button    gender    female
    Sleep    3s
    Close Browser