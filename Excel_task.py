import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from datetime import datetime
 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)
 
driver.maximize_window()
driver.get("https://carepro-training.ihmafrica.com/")
driver.implicitly_wait(30)
 
driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("tester")
time.sleep(1)
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("tester2023!")
time.sleep(1)
 
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
 
 
elem = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'Select Facility')]")))
 
 
time.sleep(1)
 
Province = driver.find_element(By.XPATH,'//select[@placeholder="Enter Province"]')
 
ProvinceDD = Select(Province)
 
firstwebelement = ProvinceDD.first_selected_option
print("First web element is ",firstwebelement.text)
 
listDD = ProvinceDD.options
print(len(listDD))
for ele in listDD:
    print("Value is ",ele.text)
    if ele.text=="Lusaka":
        ele.click()
        break
 
DistrictDC = driver.find_element(By.XPATH,'//select[@placeholder="Enter District"]')
time.sleep(1)
DistrictDC.click()
DistrictDC.click()
time.sleep(1)
 
District = driver.find_element(By.XPATH,'//select[@placeholder="Enter District"]')
DistrictDD = Select(District)
firstwebelement = DistrictDD.first_selected_option
print("First web element is ",firstwebelement.text)
 
listDD = DistrictDD.options
print(len(listDD))
for ele in listDD:
    print("Value is ",ele.text)
    if ele.text=="Lusaka":
        ele.click()
        break
 
driver.find_element(By.XPATH,'//input[@placeholder="Search facility"]').click()
time.sleep(1)
suggestionns_List = driver.find_elements(By.XPATH,"//div[@class='border border-borderColor text-textColor hover:bg-borderColor !text-[10px] 2xl:!text-[12px] text-xs cursor-pointer !px-3 py-1 2xl:py-1.5']")
 
print("Total number of list elements",len(suggestionns_List))
 
for ele in suggestionns_List:
    print(ele.text)
    if ele.text=="Dr. Watson Dental Clinic":
        ele.click()
        print("Record Found")
        break
 
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(1)
 
elem = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.XPATH,'//input[@inputmode="numeric"]')))
driver.find_element(By.XPATH,'//input[@inputmode="numeric"]').send_keys("111111111")
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
 
elem = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'shadow')]//span[contains(text(),'Date of Birth')]")))
 
driver.find_element(By.XPATH,"//button[contains(text(),'Attend to Patient')]").click()
time.sleep(5)
 
elem = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.XPATH,"//div//a[contains(@href,'/vitals')]")))
 
driver.find_element(By.XPATH,"//div//a[contains(@href,'/vitals')]").click()
 
elem = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.XPATH,'//button[@type="button" and @class]')))
 ###Extract Excel Table Data###
 
f = open("Sample Dataset.csv", "r")
# first_iteration =True
# for line in f:
#         # Strip the line to remove leading and trailing whitespaces
#     cleaned_line = line.strip()
#     # Now you can process the cleaned line as needed
#     #print(cleaned_line)
#     if not first_iteration:
#         Date_Time_Value = cleaned_line.split(",")[1]
#         print(Date_Time_Value)
#         Date_Value = Date_Time_Value.split(" ")[0]
#         print(Date_Value)
#         Time_Value = cleaned_line.split(",")[2]
#         print(Time_Value)
#         Weight_Value = cleaned_line.split(",")[3]
#         print(Weight_Value)
#         Height_Value = cleaned_line.split(",")[4]
#         print(Height_Value)
#         Temperature_Value = cleaned_line.split(",")[5]
#         print(Temperature_Value)
#         Systolic_Value = cleaned_line.split(",")[6]
#         print(Systolic_Value)
#         Diastolic_Value = cleaned_line.split(",")[7]
#         print(Diastolic_Value)
#         Pulse_Rate_Value = cleaned_line.split(",")[8]
#         print(Pulse_Rate_Value)
#         Respiratory_Rate_Value = cleaned_line.split(",")[9]
#         print(Respiratory_Rate_Value)
#         Oxygen_Saturation_Value = cleaned_line.split(",")[10]
#         print(Oxygen_Saturation_Value)
#     first_iteration = False
time.sleep(4)

 
 
first_iteration =True
for line in f:
        # Strip the line to remove leading and trailing whitespaces
    cleaned_line = line.strip()
    # Now you can process the cleaned line as needed
    #print(cleaned_line)
    if not first_iteration:
        driver.find_element(By.XPATH,'//button[@type="button" and @class]').click()
 
        elem = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH,"//h3[contains(text(),'Patient Information')]")))

        Date_Time_Value = cleaned_line.split(",")[1]
        print(Date_Time_Value)
        Date_Value = Date_Time_Value.split(" ")[0]
        print(Date_Value)
        Date_year_value = Date_Value.split("-")[0]
        Date_month_value = Date_Value.split("-")[1]
        Date_date_value = Date_Value.split("-")[2]
        Time_Value = cleaned_line.split(",")[2]
        print(Time_Value)
        Weight_Value = cleaned_line.split(",")[3]
        print(Weight_Value)
        driver.find_element(By.XPATH,"//input[@name='weight']").clear()
        driver.find_element(By.XPATH,"//input[@name='weight']").send_keys(Weight_Value)
        Height_Value = cleaned_line.split(",")[4]
        print(Height_Value)
        driver.find_element(By.XPATH,"//input[@name='height']").clear()
        driver.find_element(By.XPATH,"//input[@name='height']").send_keys(Height_Value)
        Temperature_Value = cleaned_line.split(",")[5]
        print(Temperature_Value)
        driver.find_element(By.XPATH,"//input[@name='temperature']").clear()
        driver.find_element(By.XPATH,"//input[@name='temperature']").send_keys(Temperature_Value)
        Systolic_Value = cleaned_line.split(",")[6]
        print(Systolic_Value)
        driver.find_element(By.XPATH,"//input[@name='systolic']").clear()
        driver.find_element(By.XPATH,"//input[@name='systolic']").send_keys(Systolic_Value)
        Diastolic_Value = cleaned_line.split(",")[7]
        print(Diastolic_Value)
        driver.find_element(By.XPATH,"//input[@name='diastolic']").clear()
        driver.find_element(By.XPATH,"//input[@name='diastolic']").send_keys(Diastolic_Value)
        Pulse_Rate_Value = cleaned_line.split(",")[8]
        print(Pulse_Rate_Value)
        driver.find_element(By.XPATH,"//input[@name='pulseRate']").clear()
        driver.find_element(By.XPATH,"//input[@name='pulseRate']").send_keys(Pulse_Rate_Value)
        Respiratory_Rate_Value = cleaned_line.split(",")[9]
        print(Respiratory_Rate_Value)
        driver.find_element(By.XPATH,"//input[@name='respiratoryRate']").clear()
        driver.find_element(By.XPATH,"//input[@name='respiratoryRate']").send_keys(Respiratory_Rate_Value)
        Oxygen_Saturation_Value = cleaned_line.split(",")[10]
        print(Oxygen_Saturation_Value)
        driver.find_element(By.XPATH,"//input[@name='oxygenSaturation']").clear()
        driver.find_element(By.XPATH,"//input[@name='oxygenSaturation']").send_keys(Oxygen_Saturation_Value)
        time.sleep(1)
        Date_click = driver.find_element(By.XPATH,'//input[@placeholder="dd-mm-yyyy"]').click()
        Date_year = driver.find_element(By.XPATH,'//select[@class="react-datepicker__year-select"]')
 
        yearDD = Select(Date_year)
       
        firstwebelement = yearDD.first_selected_option
        print("First web element is ",firstwebelement.text)
       
        listDD = yearDD.options
        print(len(listDD))
        for ele in listDD:
            if ele.text==Date_year_value:
                print("Value is ",ele.text)
                ele.click()
                break
        Date_month = driver.find_element(By.XPATH,'//select[@class="react-datepicker__month-select"]')
 
        monthDD = Select(Date_month)
       
        firstwebelement = monthDD.first_selected_option
        print("First web element is ",firstwebelement.text)
       
        Date_month_value_V2 = str(int(Date_month_value)-1)
        listDD = monthDD.options
        print(len(listDD))
        for ele in listDD:
            Month_value = ele.get_attribute("value")
            if Month_value==Date_month_value_V2:
                print("Value is ",ele.text)
                label_month_value = ele.text
                ele.click()
                break
        driver.find_element(By.XPATH,"//div[contains(@class,'--001') and contains(@aria-label,label_month_value)] ").click()
        time.sleep(1)
        driver.find_element(By.XPATH,'//input[@placeholder="hh:mm:ss"]').click()
        listElements = driver.find_elements(By.XPATH,'//li[@class="react-datepicker__time-list-item "]')

        
        time_obj = datetime.strptime(Time_Value, "%H:%M:%S")

        
        time_12hr = time_obj.strftime("%I:%M %p").lstrip("0")

        print(time_12hr)
        for ele in listElements:
            if ele.text.strip()==time_12hr:
                print("Value is ",ele.text)
                ele.click()
                break


        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)
    first_iteration = False
 
time.sleep(10)
