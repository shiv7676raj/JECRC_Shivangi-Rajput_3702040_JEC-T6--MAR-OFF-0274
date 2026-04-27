*** Settings ***
Resource  ../../locators/homepage_locators.robot
Resource  ../../resources/common_resources.robot
Resource  ../../resources/pages/home_page.robot

Suite Setup  Load Environment
Test Setup  Open Application    https://gullylabs.com/
Task Teardown  Close Application
*** Test Cases ***
TC01 Log In User
    [Documentation]  check if the user is able to login
    [Tags]  functional

    Log in to application  ${USER_EMAIL}  ${USER_PWD}