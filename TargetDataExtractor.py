from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import timedelta
from datetime import date
import pandas as pd
import os
import numpy as np

#Get Dates for the date fill in portion
today = date.today()
EndDateSubtraction = timedelta(4)
EndDate = today - EndDateSubtraction
enddatestr = str(EndDate)

StartDateSubtraction = timedelta(6)
StartDate = EndDate - StartDateSubtraction
startdatestr = str(StartDate)

 #Password and username to be used to log in
usernamestr = 'InputUsername'
passwordstr = 'InputPassword'
options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\UserDataLocationforChromedirectory")
options.add_experimental_option("prefs", {"download.default_directory": r"H:\Directory\Where you want to download the file",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
  })
options.add_experimental_option("excludeSwitches", ['enable-automation'])

w = webdriver.Chrome(options=options)

  #Start drilling into the website
try:
    w.get('https://partnersonline.com')
    
    username = w.find_element_by_id('loginID')
    username.click()
    username.send_keys(usernamestr)

    password = w.find_element_by_id('pass')
    password.send_keys(passwordstr)

    signinbtn = w.find_element_by_class_name('submit-button')
    signinbtn.click()
    time.sleep(6)
    print('Sign in Complete....')
     
    appsbtn = w.find_element_by_xpath('//*[@id="root"]/div[3]/header/div/div[2]/a[2]')
    appsbtn.click()
    time.sleep(3)

    iqbtn = w.find_element_by_link_text('Vendor IQ Dashboard')
    iqbtn.click()    
    w.switch_to.window(w.window_handles[-1])
    time.sleep(3)
       
    loginbtn = w.find_element_by_xpath('//*[@id="root"]/div/div/button')
    loginbtn.click()
    time.sleep(3)

    hamburgerbtn = w.find_element_by_id('toggleMainMenuBtn')
    hamburgerbtn.click()

    cardsbtn = w.find_element_by_id('sideNavListItemText-Cards')
    cardsbtn.click()
    time.sleep(2)

    listingbtn = w.find_element_by_class_name('edit-card-link')
    listingbtn.click()
    time.sleep(5)

    datebtn = w.find_element_by_class_name('time-period-label')
    datebtn.click()

    timeperiodbtn = w.find_element_by_id('time-period-btn')
    timeperiodbtn.click()
           
    enddateform = w.find_element_by_id('end-date')
    enddateform.click()
    enddateform.send_keys(Keys.CONTROL + 'a')
    enddateform.send_keys(Keys.DELETE)
    time.sleep(1)
    
    startdateform = w.find_element_by_id('start-date')
    startdateform.click()
    startdateform.send_keys(Keys.CONTROL + 'a')
    startdateform.send_keys(Keys.DELETE)    
    time.sleep(1)
    
    enddateform.send_keys(enddatestr)
    startdateform.send_keys(startdatestr)
    
    selectbtn = w.find_element_by_id('apply-calendar-dates')
    selectbtn.click()
    
    applybtn = w.find_element_by_id('apply-time-period-btn')
    applybtn.click()
    

    extramenu = w.find_element_by_id('card-view-more')
    extramenu.click()
    time.sleep(2)

    exportbtn = w.find_element_by_xpath('/html/body/div[3]/div[3]/ul/a[1]/li')
    exportbtn.click()
    time.sleep(10)

    w.quit()
    print('Webdriver portion complete')
    
    today = date.today()
    subDays = timedelta(4)
    
    execdate = today - subDays
    strexecdate = str(execdate) 
    
    #Delete first row
    path = r'H:\\File Path of CSV'
    print('File Opened....')
    
    df = pd.read_csv(path + 'Sales By Week 2.csv', sep=',', index_col=False, encoding = 'utf-8')
    
    N = 9
    df.drop(index = df.index[-N:], axis=0, inplace=True)
        
    df['TCIN'] = df['TCIN'].fillna(0).apply(np.int64)

    df.to_csv(path + 'Sales By Day ' + startdatestr + ' thru ' + enddatestr + '.csv', index=False, sep= ',', encoding = 'utf-8')
    print('File Saved...')
    
        
    del df    
    os.remove(path + 'Sales By Week 2.csv')
 
except Exception as e:
    print(e)
    
