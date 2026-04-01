*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
*** Variables ***
${url}  https://the-internet.herokuapp.com/
${check}  C:\\Users\\HP\\Downloads\\cat.jpg
*** Test Cases ***
#Upload
#    Open Browser  ${url}  chrome
#    Maximize Browser Window
#    Click Element    xpath=//a[@href='/upload']
#    Sleep    2s
#    ${path}  Normalize Path    ${CURDIR}/sample.txt
#    Choose File    id=file-upload    ${path}
#    Sleep    2s
#    Click Button    id=file-submit
Download
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Click Element    xpath=//a[@href='/download']

    Click Element    xpath=//a[text()='cat.jpg']
    Wait Until Created    ${check}  timeout=10s
    File Should Exist    ${check}
    Log To Console    Downloaded successfully
    Close Browser