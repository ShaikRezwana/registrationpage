import pytest
from selenium import webdriver
import logging

from pageObjects.registerpage import Registerpage
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.loginfunction import Login

class Test_002_loginpage:
    baseurl = ReadConfig.getbaseurl()
    email=ReadConfig.enteremail()
    password=ReadConfig.enterpassword()

    logger = LogGen.loggen()

    def test_loginfunc(self,setup):
        self.logger.info("************* login functionality check**********")
        self.driver=setup
        self.logger.info("*********1***********")
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver)
        self.lp.clickmyaccount()
        self.lp.clicklinklogin()
        self.lp.enterusername(self.email)
        self.lp.enterpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("************ login successful ************")
