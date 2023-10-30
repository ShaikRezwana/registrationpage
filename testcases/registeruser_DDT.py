import pytest
from selenium import webdriver
import logging

from pageObjects.registerpage import Registerpage
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from utilities import XLUtils

class Test_02_register:
    baseurl = ReadConfig.getbaseurl()
    firstname=ReadConfig.enterfirstname()
    lastname=ReadConfig.enterlastname()
    email=ReadConfig.enteremail()
    telephone=ReadConfig.entertelephone()
    password=ReadConfig.enterpassword()
    confirm_password=ReadConfig.enterconfirmpassword()
    path="path of XLfile"

    logger=LogGen.loggen()


    def test_registration(self,setup):
        self.logger.info("--------verify Test registration ----------")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.obj.clickmyaccount()
        self.obj.clickregister()

        self.obj=Registerpage(self.driver)

        self.rows=XLUtils.getrowcount(self.path,"sheet1")
        print(self.rows)
        for r in range(2,self.rows+1):
            self.firstname=XLUtils.readData(self.path,"sheet1",r,1)
            self.lastname = XLUtils.readData(self.path, "sheet1", r, 2)
            self.email = XLUtils.readData(self.path, "sheet1", r, 3)
            self.telephone = XLUtils.readData(self.path, "sheet1", r, 4)
            self.password = XLUtils.readData(self.path, "sheet1", r, 5)
            self.confirm_password = XLUtils.readData(self.path, "sheet1", r, 6)

            self.obj.firstname(self.firstname)
            self.obj.lastname(self.lastname)
            self.obj.email(self.email)
            self.obj.telephone(self.telephone)
            self.obj.password(self.password)
            self.obj.confirmpassword(self.confirm_password)

            self.obj.checkbox()
            self.obj.clickcontunue()
            time.sleep(5)

            act_title=""

