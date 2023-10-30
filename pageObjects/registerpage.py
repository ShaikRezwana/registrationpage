class Registerpage:
    textbox_firstname_id="input-firstname"
    textbox_last_name_id="input-lastname"
    textbox_email_id="input-email"
    textbox_telephone_id="input-telephone"
    textbox_password_id="input-password"
    textbox_confirm_password_id="input-confirm"
    register_xpath="/html/body/div[1]/div[5]/div[1]/div/aside/div/a[2]"
    box_xpath="/html/body/div[1]/div[5]/div[1]/div/div/form/div/div/div/label"
    button_xpath="/html/body/div[1]/div[5]/div[1]/div/div/form/div/div/input"
    myaccount_xpath="/html/body/div[1]/div[5]/header/div[3]/div[1]/div/div[3]/nav/div/ul/li[6]/a/div/span"

    def __init__(self,driver):
        self.driver=driver

    def clickmyaccount(self):
        self.driver.find_element("xpath",self.myaccount_xpath).click()

    def clickregister(self):
        self.driver.find_element("xpath",self.register_xpath).click()

    def enterfirstname(self,firstname):
        self.driver.find_element("id",self.textbox_firstname_id).clear()
        self.driver.find_element("id",self.textbox_firstname_id).send_keys(firstname)

    def enterlastname(self,lastname):
        self.driver.find_element("id",self.textbox_last_name_id).clear()
        self.driver.find_element("id",self.textbox_last_name_id).send_keys(lastname)

    def enteremail(self,email):
        self.driver.find_element("id",self.textbox_email_id).clear()
        self.driver.find_element("id",self.textbox_email_id).send_keys(email)

    def entertelephone(self,telephone):
        self.driver.find_element("id",self.textbox_telephone_id).clear()
        self.driver.find_element("id", self.textbox_telephone_id).send_keys(telephone)

    def enterpassword(self,password):
        self.driver.find_element("id",self.textbox_password_id).clear()
        self.driver.find_element("id",self.textbox_password_id).send_keys(password)

    def enterconfirmpassword(self,confirm_password):
        self.driver.find_element("id",self.textbox_confirm_password_id).clear()
        self.driver.find_element("id",self.textbox_confirm_password_id).send_keys(confirm_password)

    def checkbox(self):
        self.driver.find_element("xpath",self.box_xpath).click()

    def clickcontunue(self):
        self.driver.find_element("xpath",self.button_xpath).click()





