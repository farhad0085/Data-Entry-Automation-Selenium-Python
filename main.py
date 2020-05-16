from selenium import webdriver
import os
import time

# Setting firefox not to alert for save the xlsx files
# rather automatically save the file to the disk
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList",2);
profile.set_preference("browser.download.manager.showWhenStarting", False);
profile.set_preference("browser.download.dir","C:\\Users\\Farhad\\Downloads"); # Download location where to be saved the file
profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
profile.update_preferences()

driver = webdriver.Firefox(firefox_profile=profile)

driver.implicitly_wait(15)
driver.get("https://pdftables.com/")

# File path of the file to be uploaded
file_path = "C:\\Users\\Farhad\\Desktop\\Data Entry Automation\\student.pdf"
driver.find_element_by_name("files").send_keys(file_path)
driver.find_element_by_id("download-excel").click()

print("When xlsx file is ready, press Enter...", end=" ")
data = input("")
exit()