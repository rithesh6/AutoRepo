import sys
import os
from selenium import webdriver

print("doing")
Path = r"C:\Users\Rithesh kunchakuri\Github\Myprojects"
browser = webdriver.Chrome(executable_path=r"C:\Users\Rithesh kunchakuri\Github\chromedriver.exe")
#executable_path=r"C:\Users\Rithesh kunchakuri\Github\Myprojects\chromedriver.exe"
browser.get("https://github.com/login")

def create():
    #folderName = str(sys.argv)
    #print(len(sys.argv))
    #os.makedirs(Path + str(sys.argv))
    python_button = browser.find_elements_by_xpath("/html/body/div[3]/main/div/div[4]/form/input[2]")[0]
    python_button.send_keys('rithesh6')
    python_button = browser.find_elements_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[1]")[0]
    python_button.send_keys('IcwU357%')
    python_button = browser.find_elements_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[12]")[0]
    python_button.click()
    browser.get('https://github.com/new')
    python_button = browser.find_elements_by_xpath("/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input")[0]
    python_button.send_keys('folderName')

if __name__ == "__main__":
    create()    
