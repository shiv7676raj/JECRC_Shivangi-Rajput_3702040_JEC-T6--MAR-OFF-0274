*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/logout_locator.robot
*** Keywords ***
Logout of application
    [Documentation]  to logout the user
    Click Element    ${account}
    Log    Clicking on account element
    Element Should Be Visible   ${logout}
    Click Element    ${logout}
    Log  Logging out