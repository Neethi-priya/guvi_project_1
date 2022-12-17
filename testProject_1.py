from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Test_Data import project_1
import pytest
import time 

class Test_Project:
    url = "https://opensource-demo.orangehrmlive.com" 

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Edge()
        yield
        self.driver.close() 
        
    def test_login_01(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=project_1.Project_Selectors.input_box_username).send_keys(project_1.Project_Data.username)
        self.driver.find_element(by=By.NAME, value=project_1.Project_Selectors.input_box_password).send_keys(project_1.Project_Data.password)
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.login_xpath).click()
        print("The user is logged in successfully") 
        
    def test_login_02(self, booting_function): 
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=project_1.Project_Selectors.input_box_username).send_keys(project_1.Project_Data.username)
        self.driver.find_element(by=By.NAME, value=project_1.Project_Selectors.input_box_password).send_keys(project_1.Project_Data.wrong_password)
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.login_xpath).click()
        print("A valid error message for invalid credentials is displayed") 
        
    def test_PIM_01(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=project_1.Project_Selectors.input_box_username).send_keys(project_1.Project_Data.username)
        self.driver.find_element(by=By.NAME, value=project_1.Project_Selectors.input_box_password).send_keys(project_1.Project_Data.password)
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.login_xpath).click() 
        time.sleep(5)
        
        #for clicking pim 
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.pim_xpath).click() 
        time.sleep(5)
        #print("pim is clicked") 
        
        #add employee click 
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.add_employee_xpath).click() 
        time.sleep(4)
        
        #filling the fields 
        self.driver.find_element(by=By.NAME,value=project_1.Project_Selectors.employee_box_firstname).send_keys(project_1.Project_Data.employee_firstname)
        time.sleep(2)
        self.driver.find_element(by=By.NAME,value=project_1.Project_Selectors.employee_box_middlename).send_keys(project_1.Project_Data.employee_middlename)
        time.sleep(2)
        self.driver.find_element(by=By.NAME,value=project_1.Project_Selectors.employee_box_lastname).send_keys(project_1.Project_Data.employee_lastname)
        time.sleep(2)
        data=self.driver.find_element(by=By.XPATH,value=project_1.Project_Selectors.employee_id_box)
        data.click()
        data.send_keys(Keys.CONTROL + "a")
        data.send_keys(Keys.DELETE)
        data.send_keys(project_1.Project_Data.emp_id)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.save_button).click()
        time.sleep(2) 
        print("Employee is added successfully..!")
        
        
    def test_PIM_02(self,booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=project_1.Project_Selectors.input_box_username).send_keys(project_1.Project_Data.username)
        self.driver.find_element(by=By.NAME, value=project_1.Project_Selectors.input_box_password).send_keys(project_1.Project_Data.password)
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.login_xpath).click() 
        time.sleep(5)
        
        #for clicking pim 
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.pim_xpath).click() 
        time.sleep(5)
        
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.employee_list_xpath).click() 
        time.sleep(3) 
        
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.employee_name).send_keys(project_1.Project_Data.emp_name)
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.employee_id_box_2).send_keys(project_1.Project_Data.emp_id)
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.search_xpath).click()
        time.sleep(10)
        
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.profile_click_xpath).click()
        time.sleep(10)
        data2=self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.dob_field).send_keys(project_1.Project_Data.dob)
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.bullet_button).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.save_button_edit_employee).click() 
        time.sleep(3)
        print("Successfully Added Employee Details !.")
        
       
        
        
        
    def test_PIM_03(self,booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=project_1.Project_Selectors.input_box_username).send_keys(project_1.Project_Data.username)
        self.driver.find_element(by=By.NAME, value=project_1.Project_Selectors.input_box_password).send_keys(project_1.Project_Data.password)
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.login_xpath).click() 
        time.sleep(5)
        
        #for clicking pim 
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.pim_xpath).click() 
        time.sleep(5)
        
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.employee_list_xpath).click() 
        time.sleep(3) 
        
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.employee_name).send_keys(project_1.Project_Data.emp_name)
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.employee_id_box_2).send_keys(project_1.Project_Data.emp_id)
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.search_xpath).click()
        time.sleep(5)
        
        
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.deleting_button).click() 
        time.sleep(5)
        
        self.driver.find_element(by=By.XPATH, value=project_1.Project_Selectors.deleting_button_confirmation).click() 
        time.sleep(5)
        print("Successfull Deletion..!")
     