*** Settings ***
Library           RequestsLibrary
Library           Collections
Library           JSONLibrary
*** Variables ***
${BASE_URL}       https://petstore.swagger.io/v2
*** Test Cases ***
Add Pet
    [Documentation]    Add a new pet to the store
    Create Session    petapi    ${BASE_URL}  verify=True
    ${payload}=    Load Json From File    ${CURDIR}/../data/add_pet.json
    ${response}=    POST On Session  petapi  /pet  json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}
Update existing pet
    [Documentation]    Update an existing pet in the store
    Create Session    petapi    ${BASE_URL}  verify=True
    ${payload}=    Load Json From File    ${CURDIR}/../data/update_pet.json
    ${response}=    PUT On Session  petapi  /pet  json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}
Get Pet By Id
    [Documentation]    Get pet by ID
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=    GET On Session  petapi  /pet/55
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}
Get Pet By Status
    [Documentation]    Get pets by status
    Create Session    petapi    ${BASE_URL}  verify=True
    ${qp}=    Create Dictionary  status=available
    ${response}=    GET On Session  petapi  /pet/findByStatus  params=${qp}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}
Upload an Image
    [Documentation]    Upload an image for a pet
    Create Session    petapi    ${BASE_URL}  verify=True
    ${form_data}=    Create Dictionary  additionalMetadata=My pet image
    ${file_path}=    Set Variable    ${CURDIR}/../data/pet_image.jpg
    ${file}=  Evaluate  {'file': open($file_path, 'rb')}
    ${response}=    POST On Session  petapi  /pet/55/uploadImage
    ...  data=${form_data}
    ...  files=${file}
    Should Be Equal As Integers    ${response.status_code}    200
#    Log To Console    ${response.json()}
Update pet in store
    Create Session    petapi    ${BASE_URL}     verify=True
    ${payload}=  Load Json From File    ${CURDIR}/../data/update_pet.json
    ${response}=    POST On Session   petapi  /pet  json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}

Delete pet
    Create Session    petapi    ${BASE_URL}     verify=True
    ${response}=    DELETE On Session   petapi  /pet/55
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    Pet with ID 55 deleted successfully

