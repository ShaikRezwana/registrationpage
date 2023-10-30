import pytest
from selenium import webdriver
import logging

from pageObjects.registerpage import Registerpage
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen

class Test_01_register:
    baseurl = ReadConfig.getbaseurl()
    firstname=ReadConfig.enterfirstname()
    lastname=ReadConfig.enterlastname()
    email=ReadConfig.enteremail()
    telephone=ReadConfig.entertelephone()
    password=ReadConfig.enterpassword()
    confirm_password=ReadConfig.enterconfirmpassword()

    logger=LogGen.loggen()

    def test_title(self,setup):
        self.logger.info("------- Test_01_register ---------")
        self.logger.info("--------verify Test title ----------")
        self.driver=setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        print(act_title)


    def test_registration(self,setup):
        self.logger.info("--------verify Test registration ----------")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.obj=Registerpage(self.driver)
        self.obj.clickmyaccount()
        self.obj.clickregister()
        self.obj.enterfirstname(self.firstname)
        self.obj.enterlastname(self.lastname)
        self.obj.enteremail(self.email)
        self.obj.entertelephone(self.telephone)
        self.obj.enterpassword(self.password)
        self.obj.enterconfirmpassword(self.confirm_password)
        if self.password == self.confirm_password:
            assert True
            self.logger.info("-------- passwords matched ----------")
        else:
            self.driver.save_screenshot(
                r"C:\\Users\\rezwana.shaik\\PycharmProjects\\registerpage.py\\screenshots\\" + "test_registration.png")
            self.logger.error("-------- passwords doesnt matched ----------")
            assert False
        self.obj.checkbox()
        self.obj.clickcontunue()
        self.driver.close()


