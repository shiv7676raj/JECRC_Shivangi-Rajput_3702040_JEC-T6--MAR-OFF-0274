*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/homepage_locators.robot
*** Keywords ***
Log in to application
    [Documentation]  to login the existing user
    [Arguments]  ${mail}  ${pwd}
    Click Element    ${account}
    Log    Clickig on login link
    Input Text    ${email}    ${mail}
    Log     Entering email
    Input Text    ${password}    ${pwd}
    Log     Entering password
    Click Element    ${btn}
    Page Should Contain    Account
    Page Should Contain Element    xpath=//a[text()="Log out"]