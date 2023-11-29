*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${wikipeda login}    RobotTests
${wiki password}    RobotFramework
${error_message}  Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz..

*** Keywords ***

*** Test Cases ***
Log in Wikipedia
    OPEN BROWSER    https://pl.wikipedia.org
    click element    id:pt-login-2
    input text    id:wpName1    ${wikipeda login}
    Checkbox Should Not Be Selected    id:wpRemember
    select checkbox    id:wpRemember
    input password    id:wpPassword1    ${wiki password}
    click button    id:wpLoginAttempt
    sleep    3
    close browser

Unsuccessful login
    OPEN BROWSER    https://pl.wikipedia.org
    click element    id:pt-login-2
    input text    id:wpName1    ${wikipeda login}
    Checkbox Should Not Be Selected    id:wpRemember
    select checkbox    id:wpRemember
    input password    id:wpPassword1    qwwe
    click button    id:wpLoginAttempt
    Wait Until Element Is Visible  css:.mw-message-box-error  timeout=7
    ${my_error_message}  Get Text  css:.mw-message-box-error
    log    ${my_error_message}
    log to console    ${my_error_message}
    should be equal as strings    ${my_error_message}   ${error_message}
    close browser