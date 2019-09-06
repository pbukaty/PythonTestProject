# Created by p.bukatyj at 9/3/2019
Feature: Drive&Pay test

  @login
  Scenario: Login to Drive&Pay
    Given Login screen is loaded
    When type mobile phone
    And type password
    And set fast login checkbox state to "false"
    And tap Login button
    Then Main screen is opened