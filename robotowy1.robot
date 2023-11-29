*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${wikipeda login}    RobotTests
${wiki password}    RobotFramework
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