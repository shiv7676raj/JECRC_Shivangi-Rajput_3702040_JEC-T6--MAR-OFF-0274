*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://in.bookmyshow.com/explore/home/jaipur
*** Test Cases ***
Screenshots
    Set Screenshot Directory    ${CURDIR}/Screenshots
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Capture Page Screenshot  fullpage.png
    Scroll Element Into View    xpath=//div[text()='Dhurandhar The Revenge']
    Capture Element Screenshot    xpath=//img[@alt="Dhurandhar The Revenge"]  movie.png
    Sleep    2s
    Close Browser