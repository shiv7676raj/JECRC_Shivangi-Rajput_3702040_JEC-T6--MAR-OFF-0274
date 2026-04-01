*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://the-internet.herokuapp.com/
*** Test Cases ***
Implicit wait
    Open Browser  ${url}  chrome
    ${before}  Get Selenium Implicit Wait   #returns the time of implicit wait
    Log To Console    ${before}
    Set Selenium Implicit Wait    5s    #to set the wait usually in seconds
    ${after}  Get Selenium Implicit Wait
    Log To Console    ${after}
    Close Browser
#set browser implicit wait=to set implicit wait for one browser instance, if there are multiple
#browsers then it will be confined to that broswer