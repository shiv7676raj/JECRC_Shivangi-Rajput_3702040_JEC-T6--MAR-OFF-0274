#flags-> -t=to run a particular test case by giving its name
         -i=to include grouping
         -e=to exclude
*** Settings ***
#importing packages and libraries
Documentation  Opening of browsers
Library  SeleniumLibrary
*** Variables ***
#defining variables
#scalar vaiables=store ionly 1 value
${url}  https://www.cricbuzz.com/
#list variables=store multiple values
@{bikes}  ktm  yamaha  honda  pulsar
#dictioary variables=store values in key-value pair
&{cars}  mercedes=benz  honda=city
*** Test Cases ***
#writing test scripts/scenarios
Open cricbuzz in chrome
    Opening Chrome Browser
Opening Firefox Headless Browser
    [Documentation]  firefox browser navigating to https://www.cricbuzz.com/
    Open Browser  https://www.cricbuzz.com/  headlessfirefox
    Maximize Browser Window
    Log    navigated to cricbuzz
    Log To Console    navigated to cricbuzz
    Sleep    3s
    Close Browser
Opening Edge Browser
    [Documentation]  Edge browser navigating to https://www.cricbuzz.com/
    Open Browser  ${url}  edge
    Maximize Browser Window
    Log    navigated to cricbuzz
    Log To Console    ${bikes}[1]
    Log To Console    ${cars.honda}
    Sleep    3s
    Close Browser
*** Keywords ***
#user defined keywords,not built-in ones
Opening Chrome Browser
    [Documentation]  Chrome browser navigating to https://www.cricbuzz.com/
    [Tags]  smoke  reg          #are used to group test cases
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Log    navigated to cricbuzz
    Log To Console    navigated to cricbuzz
    Sleep    3s                             #5 minutes 30s
    Close Browser