#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Erlend Ekern <dev@ekern.me>
#
# Distributed under terms of the MIT license.

"""
A script that fetches your grades from StudentWeb and calculates your GPA
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from gui import GPAFetcherGUI
from constants import Selector, Location
import threading
import atexit
import time

class GPAFetcher(object):
    GRADE_VALUES_ASC = { "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 0 }
    GRADE_VALUES_DESC = { "a": 5, "b": 4, "c": 3, "d": 2, "e": 1, "f": 0 }

    def __init__(self):
        self.gui = GPAFetcherGUI(login=self._login, set_gpa=self._set_gpa)
        self.grades = []
        self.driver = None

        self._driver_setup()
        self.gui.run()

        atexit.register(self.driver.quit)

    def _driver_setup(self):
        options = webdriver.ChromeOptions()
        options.binary_location = Location.CHROME_BINARY
        options.add_argument('headless')
        prefs = {'profile.managed_default_content_settings.images': 2}
        options.add_experimental_option('prefs', prefs)

        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.set_window_size(1,1)

    def _login(self):
        def login_callback():
            self.gui.disable_element(self.gui.mid_frame)

            self.gui.update_status('Waiting for fsweb.no ...')
            self.driver.get(Location.STUDENTWEB_INDEX)
            self.driver.find_element_by_xpath(Selector.FEIDE_LINK).click()

            self.gui.update_status('Selecting institution ...')
            self.driver.find_element_by_xpath(Selector.SELECT_INSTITUTION).click()
            self.driver.find_element_by_xpath(Selector.SELECT_INSTITUTION_SUBMIT).click()

            username = self.gui.username_input.get()
            password = self.gui.password_input.get()

            self.gui.update_status("Logging in as {} ...".format(username))
            username_field = self.driver.find_element_by_xpath(Selector.USERNAME_INPUT)
            password_field = self.driver.find_element_by_xpath(Selector.PASSWORD_INPUT)
            username_field.send_keys(username)
            password_field.send_keys(password)
            self.driver.find_element_by_xpath(Selector.LOGIN_SUBMIT).click()

            self.gui.update_status("Fetching grades ...")
            self.driver.get(Location.STUDENTWEB_RESULTS)
            results = self.driver.find_elements_by_xpath(Selector.RESULTS)
            self.grades = {}
            max_course_len = 0
            for result in results:
                course_element = result.find_element_by_xpath(Selector.COURSE)
                grade_element = result.find_element_by_xpath(Selector.GRADE)
                credits_element = result.find_element_by_xpath(Selector.CREDITS)

                course = course_element.text
                grade = grade_element.text.lower()
                credits = float(credits_element.text.replace(',', '.'))

                if grade not in self.GRADE_VALUES_DESC.keys():
                    continue

                if len(course) > max_course_len:
                    max_course_len = len(course)

                self.grades[course] = (grade, credits)

            self.gui.update_status("Found single-letter grades in {} courses:".format(len(self.grades)))
            for course, tup in self.grades.items():
                grade, credits = tup
                self.gui.update_status("Course: {} | Grade: {} | Credits: {}".format(course.ljust(max_course_len), grade.upper(), credits))
                time.sleep(.05)

            self.gui.update_status("Calculating GPA ...")
            self._set_gpa()
            self.gui.update_status("Finished!")
            self.gui.enable_element(self.gui.mid_frame)
            self.driver.close()

        t = threading.Thread(target=login_callback)
        t.start()

    def _set_gpa(self):
        if self.grades:
            if self.gui.is_desc():
                grade_values = [self.GRADE_VALUES_DESC[tup[0]] * tup[1] for tup in self.grades.values()]
            else:
                grade_values = [self.GRADE_VALUES_ASC[tup[0]] * tup[1] for tup in self.grades.values()]

            gpa = sum(grade_values)/sum(tup[1] for tup in self.grades.values())
            self.gui.gpa_label['text'] = "{:.5f}".format(gpa)

if __name__ == '__main__':
    gpa_fetcher = GPAFetcher()
