*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/search_locator.robot
*** Keywords ***
Searching a product
    [Documentation]  to search a product
    Click Element    ${search_btn}
    Log    Clicking on search button
    Input Text    xpath=//input[@id="Search-In-Template"]    Sportwear
    Press Key    xpath=//input[@id="Search-In-Template"]    ENTER
    Log  Searched a product