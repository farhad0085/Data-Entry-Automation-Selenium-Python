from selenium import webdriver
import os
import time
import testcsv as c

driver = webdriver.Firefox()

driver.implicitly_wait(15)
driver.get("http://127.0.0.1:5000/submit")

for i in range(c.totalRows()-1):
	driver.find_element_by_id("id").send_keys(str(c.getVal(i+1, 0)))
	driver.find_element_by_id("name").send_keys(str(c.getVal(i+1, 1)))
	driver.find_element_by_id("regno").send_keys(str(c.getVal(i+1, 2)))
	driver.find_element_by_id("dpt").send_keys(str(c.getVal(i+1, 3)))
	driver.find_element_by_id("cgpa").send_keys(str(c.getVal(i+1, 4)))
	driver.find_element_by_id("submit").click()
	print(str(i+1) + " Added record")

print("Complete!")