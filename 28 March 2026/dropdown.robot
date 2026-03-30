*** Settings ***
Documentation  handling dropdowns
Library  SeleniumLibrary
*** Variables ***
${url}  https://the-internet.herokuapp.com/
*** Test Cases ***
Handling dropdown
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    1s
    Click Element    xpath=//a[text()="Dropdown"]
    Sleep    2s
    #Page Should Contain Element    id=dropdown
    Page Should Contain List    id=dropdown     #more accurate and prefered
    ${options}=  Get List Items    id=dropdown
    Log To Console    ${options}
    Select From List By Label  id=dropdown  Option 1
    ${select_option}=  Get Selected List Label    id=dropdown
    Log To Console    ${select_option}
    List Selection Should Be    id=dropdown  Option 1
    Sleep    3s
    Close Browser
