*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://www.amazon.in/
*** Test Cases ***
Amazon Products
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep  2s
    #Click Element  xpath=//a[text()=' Electronics ']
    Select From List By Label  id=searchDropdownBox  Electronics
    Click Button  id=nav-search-submit-button
    Sleep  2s
    Scroll Element Into View  xpath=//span[text()='boAt']
    Sleep  2s
    Click Element  xpath=//span[text()='boAt']/preceding-sibling::div
    Sleep  2s
    ${product_name}=  Get Text  xpath=(//a//h2//span)[4]
    Log To Console  ${product_name}
    Click Element  xpath=(//a//h2//span)[4]
    Switch Window  NEW
    Wait Until Page Contains Element  id=productTitle  15s
    ${title}=  Get Text  id=productTitle
    Page Should Contain  ${title}
    ${actual_price}=  Get Text  xpath=(//span[@class='a-offscreen']/following-sibling::span)[7]
    Log To Console  ${actual_price}
    ${discount_price}=  Get Text  xpath=//span[@class='a-price-whole'][1]
    Log To Console  ${discount_price}
    ${discount_percent}=  Get Text  xpath=//span[@class="apex-savings-container"]//span[contains(text(),'%')]
    Log To Console  ${discount_percent}
    Sleep    2s
    Scroll Element Into View  id=add-to-cart-button
    Click Button  id=add-to-cart-button
    Click Element  xpath=//a[@id='nav-cart']
    ${cart_product}=  Get Text  xpath=//span[@class='a-truncate-cut']
    Page Should Contain  ${cart_product}
    Close Browser