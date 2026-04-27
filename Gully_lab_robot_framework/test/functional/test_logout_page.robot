*** Settings ***
Resource  ../../locators/logout_locator.robot
Resource  ../../resources/common_resources.robot
Resource  ../../resources/pages/logout_page.robot
Resource    ../../resources/pages/home_page.robot

Suite Setup  Load Environment
Test Setup  Open Application    https://gullylabs.com/
Task Teardown  Close Application
*** Test Cases ***
TC02 Logout User
    [Documentation]  check if the user is able to logout
    [Tags]  functional

    Log in to application    ${USER_EMAIL}    ${USER_PWD}
    Logout of application