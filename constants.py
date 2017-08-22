#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Erlend Ekern <dev@ekern.me>
#
# Distributed under terms of the MIT license.

"""
Constants used in gpa_fetcher.py
"""

class Location(object):
    CHROME_BINARY = '/usr/bin/google-chrome'
    STUDENTWEB_INDEX = 'https://fsweb.no/studentweb/login.jsf?inst=FSNTNU'
    STUDENTWEB_RESULTS = 'https://fsweb.no/studentweb/resultater.jsf'

class Selector(object):
    FEIDE_LINK = '//div[@class="login-module-box login-name-feide"]/form/a[@class="link"]'
    SELECT_INSTITUTION = '//select[@name="org"]/option[@value="ntnu.no"]'
    SELECT_INSTITUTION_SUBMIT = '//input[@id="submit"]'
    USERNAME_INPUT = '//input[@id="username"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    LOGIN_SUBMIT = '//input[@type="submit"]'
    RESULTS = '//table[@id="resultatlisteForm:HeleResultater:resultaterPanel"]/tbody/tr[td[@class="col6Resultat textAlignRight"]/div[@class="infoLinje"]/span[not(@class="vurderingsdelInfo")]]'
    GRADE = './/td[@class="col6Resultat textAlignRight"]/div[@class="infoLinje"]/span'
    COURSE = './/td[@class="col2Emne"]/div[@class="column-info"]/div[@class="infoLinje"]'
    CREDITS = './/td[@class="col7Studiepoeng textAlignRight"]/span[not(@class="ui-column-title")]'
