*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://testautomationpractice.blogspot.com/
*** Test Cases ***
Handling windows
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Scroll Element Into View    xpath=//button[@id='PopUp']
    Click Element    xpath=//button[@id='PopUp']
    Sleep    2s
    @{windows}  Get Window Handles
    @{titles}  Get Window Titles
    Log To Console    ${titles}
    Log To Console    ${windows}
    Switch Window  title=Selenium
    Page Should Contain    Selenium automates browsers. That's it!
    Page Should Contain Element    xpath=//h1
    #Sleep    3s
    Switch Window  title=Fast and reliable end-to-end testing for modern web apps | Playwright
    Page Should Contain    Playwright
    Page Should Contain Element    xpath=//span[text()='Playwright']
    Switch Window  title=Automation Testing Practice
    Sleep    3s