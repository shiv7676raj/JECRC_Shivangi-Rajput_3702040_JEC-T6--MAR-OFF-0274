*** Settings ***
Resource  ../../locators/search_locator.robot
Resource  ../../resources/common_resources.robot
Resource  ../../resources/pages/search_page.robot

Suite Setup  Load Environment
Test Setup  Open Application    https://gullylabs.com/
Task Teardown  Close Application
*** Test Cases ***
TC03 Search product
    [Documentation]  searching a product
    [Tags]  functional

    Searching a product