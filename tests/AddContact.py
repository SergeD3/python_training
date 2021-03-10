# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.application import Application
import unittest
from model.group import AddContact2


class AddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application()
    
    def test_add_contact(self):
        self.login(username="admin", password="secret")
        self.fill_contact_form(AddContact2(middle_name="middle name 1", first_name="name 1", last_name="last name 1", user_nick="nick 1", user_title="title 1", user_company="wrum",
                               user_adress="lazer 5, Moscow", user_home="784763587643", user_mob="746358746357", user_email="weuyrt@iwer.ri", user_bday="17", user_bmonth="October",
                               user_byear="1980", user_group="new group2", user_addr2="lazer 5, Russian Federation", user_phone2="rgegregreg", user_note="notes from user"))
        self.logout()

    def logout(self):
        # выпиливаемся из системы
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def login(self, username, password):
        # представляемся системе
        wd = self.wd
        self.open_homepage()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()


if __name__ == "__main__":
    unittest.main()
