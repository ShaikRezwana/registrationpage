class Login:
    lnk_myaccount_xpath="/html/body/div[1]/div[5]/header/div[3]/div[1]/div/div[3]/nav/div/ul/li[6]/a/div/span"
    txt_email_id="input-email"
    txt_password_id="input-password"
    lnk_login_xpath="/html/body/div[1]/div[5]/div[1]/div/aside/div/a[1]"
    btn_login_xpath="/html/body/div[1]/div[5]/div[1]/div/div/div/div[2]/div/div/form/input"
    myaccount_xpath ="/html/body/div[1]/div[5]/header/div[3]/div[1]/div/div[3]/nav/div/ul/li[6]/a/div/span"


    def __init__(self,driver):
        self.driver=driver

    def clickmyaccount(self):
         self.driver.find_element("xpath",self.myaccount_xpath).click()

    def clicklinklogin(self):
        self.driver.find_element("xpath",self.lnk_login_xpath).click()

    def enterusername(self,email):
        self.driver.find_element("id",self.txt_email_id).clear()
        self.driver.find_element("id", self.txt_email_id).send_keys(email)

    def enterpassword(self,password):
        self.driver.find_element("id",self.txt_password_id).clear()
        self.driver.find_element("id", self.txt_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element("xpath",self.btn_login_xpath).click()

