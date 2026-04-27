*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/addtocart_locator.robot

*** Keywords ***
Adding a product to cart
    [Documentation]  to add a product in the cart
    Click Element    ${product}
    Log    Clicking on a product
    Click Element    ${size}
    Click Element    ${gender}
    Click Element    ${quantity}
    Log  Selecting filters for the product
    Click Element    ${cart}
    Log    Adding the product to cart