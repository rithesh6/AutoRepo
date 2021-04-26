import os
from selenium import webdriver

print("Enter new Github repository name ")
FolderName = input()
Parentpath = r"C:\Users\Rithesh kunchakuri\Github\Myprojects"
browser = webdriver.Chrome(executable_path=r"C:\Users\Rithesh kunchakuri\Github\chromedriver.exe")
browser.get("https://github.com/login")


if __name__ == "__main__":
    Path = os.path.join(Parentpath , FolderName)
    os.makedirs(Path)
    python_button = browser.find_elements_by_xpath("/html/body/div[3]/main/div/div[4]/form/input[2]")[0]
    python_button.send_keys('rithesh6')
    python_button = browser.find_elements_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[1]")[0]
    python_button.send_keys('IcwU357%')
    python_button = browser.find_elements_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[12]")[0]
    python_button.click()
    browser.get('https://github.com/new')
    python_button = browser.find_elements_by_xpath("/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input")[0]
    python_button.send_keys(FolderName)
    python_button = browser.find_elements_by_xpath("/html/body/div[4]/main/div/form/div[4]/div[4]/div[1]/label/input[2]")[0]
    python_button.click()  
    python_button = browser.find_elements_by_css_selector('button.first-in-line')[0]
    python_button.submit()  
