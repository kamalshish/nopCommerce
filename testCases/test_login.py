import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremailL()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def testHomePageTitle(self,setup):

        self.logger.info("***************** Test_001_Login ******************")
        self.logger.info("***************** verifying homepage title ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("***************** homepage title test case passed ******************")
        else:
            self.driver.save_screenshot("C://Users/Lenovo/PycharmProjects/nopcommerceApp/Screenshots"
                                        "/testHomePageTitle.png")
            self.driver.close()
            self.logger.error("***************** homepage title test case failed ******************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self,setup):
        self.logger.info("***************** verifying login test case ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("***************** login test case passed ******************")
        else:
            self.driver.save_screenshot("C://Users//Lenovo//PycharmProjects//nopcommerceApp//Screenshots//test_Login.png")
            self.driver.close()
            self.logger.warn("***************** login test case passed ******************")
            assert False




