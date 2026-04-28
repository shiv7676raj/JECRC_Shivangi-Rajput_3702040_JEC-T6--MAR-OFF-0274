*** Settings ***
Library           RequestsLibrary
Library           Collections
*** Variables ***
${BASE_URL}       https://petstore.swagger.io/v2
*** Test Cases ***
Pet Inventories
    [Documentation]    Get pet inventories by status
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=    GET On Session  petapi  /store/inventory
    Should Be Equal As Integers    ${response.status_code}    200
    ${body}=    Set Variable    ${response.json()}
    Log To Console    ${body}
    Log To Console   ${response.status_code}

Place Order
    [Documentation]    Place an order for a pet
    Create Session    petapi    ${BASE_URL}  verify=True
    ${payload}=    Create Dictionary
    ...   id=12345
    ...   petId=54321
    ...   quantity=1
    ...   shipDate=2024-06-01T12:00:00.000Z
    ...   status=placed
    ...   complete=true
    ${response}=    POST On Session  petapi  /store/order  json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200
    ${body}=    Set Variable    ${response.json()}
    Should Be Equal As Integers    ${body}[id]    12345
    Should Be Equal As Strings    ${body}[status]    placed
    Log To Console    ${body}
    Log To Console   ${response.status_code}
    Set Suite Variable    ${ORDER_ID}    ${body}[id]

Get Order By Id
    [Documentation]    Get order by ID
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=    GET On Session  petapi  /store/order/${ORDER_ID}
    Should Be Equal As Integers    ${response.status_code}    200
    ${body}=    Set Variable    ${response.json()}
    Should Be Equal As Integers    ${body}[id]    ${ORDER_ID}
    Should Be Equal As Strings    ${body}[status]    placed
    Log To Console    ${body}
    Log To Console   ${response.status_code}

Delete Order By Id
    [Documentation]    Delete order by ID
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=    DELETE On Session  petapi  /store/order/${ORDER_ID}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console   ${response.status_code}

E2E
    Create Session    e2eapi    ${BASE_URL}  verify=True
    ${payload}=    Create Dictionary
    ...   id=18
    ...   petId=54
    ...   quantity=1
    ...   shipDate=2024-06-02T12:00:00.000Z
    ...   status=placed
    ...   complete=true
    ${res1}=    POST On Session  e2eapi  /store/order  json=${payload}
    Should Be Equal As Integers    ${res1.status_code}    200
    ${body}=    Set Variable    ${res1.json()}
    Set Suite Variable    ${ORDER_ID}   ${body}[id]
    Log To Console    Created an order
    ${res2}=    GET On Session  e2eapi  /store/order/${ORDER_ID}
    Should Be Equal As Integers    ${res2.status_code}    200
    Log To Console    Retrieved the order
    ${res3}=    DELETE On Session  e2eapi  /store/order/${ORDER_ID}
    Should Be Equal As Integers    ${res3.status_code}    200
    Log To Console    Deleted the order