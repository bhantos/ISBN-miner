# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

start = time.time()

def check_exists_by_xpath(driver,xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def open_mokka(driver):
    driver.get("http://www.mokka.hu/web/guest")
    o_keres = "/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div[1]/form/div[2]/a"
    act1 = driver.find_element_by_xpath(o_keres)
    act1.click()
    act1.click()
    act1.click()
    act1.click()
    act1.click()

def query(isbn,driver):
    szerzo = ''
    cim = ''
    megjelenes = ''
    sorozat = ''

    open_mokka(driver)
    
    if (check_exists_by_xpath(driver,'/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/h3')):
        while (driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/h3').text == 'Hiba: érvénytelen állapot.'):
            open_mokka(driver)
            
    # select 'ISBN' from dropdown list     
    isbn_gomb = "/html/body/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/form/div[2]/div[1]/div[1]/select/option[10]"
    act2 = driver.find_element_by_xpath(isbn_gomb)
    act2.click()
    
    # fill out box with ISBN 
    box = '//*[@id="term0"]'
    act3 = driver.find_element_by_xpath(box)
    act3.send_keys(isbn)
    act3.submit()
    
    # details of the book, change pane
    driver.wait = WebDriverWait(driver,30)
    peek = 'html.ltr.yui3-js-enabled.gecko.js.firefox.firefox68.firefox68-0.win body.orangeAndBlue.controls-visible.guest-community.signed-out.public-page div.top_bg div#wrapper div#content div#main-content.columns-2 div.portlet-layout div#column-1.aui-w70.portlet-column.portlet-column-first div#layout-column_column-1.portlet-dropzone.portlet-column-content.portlet-column-content-first div#p_p_id_DisplayResult_WAR_akfweb_.portlet-boundary.portlet-boundary_DisplayResult_WAR_akfweb_.portlet-static.portlet-static-end div.portlet-borderless-container div.portlet-body div#displayResult.mainPortlet div#result form div.resultTableDiv table.resultTable tbody tr.odd td div#recordContent1.recordRow table tbody tr td a#showLinkId1'
    act4 = driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,peek)))
    act4.click()

    pane_teljes = '//*[@id="long.html"]'
    act5 = driver.find_element_by_xpath(pane_teljes)
    act5.click()
    
    if driver.find_elements_by_css_selector('html.ltr.yui3-js-enabled.gecko.js.firefox.firefox68.firefox68-0.win body#aui_3_2_0_1130.orangeAndBlue.controls-visible.guest-community.signed-out.public-page div#aui_3_2_0_1135.top_bg div#wrapper div#content div#main-content.columns-2 div#aui_3_2_0_1134.portlet-layout div#column-1.aui-w70.portlet-column.portlet-column-first div#layout-column_column-1.portlet-dropzone.portlet-column-content.portlet-column-content-first div#p_p_id_DisplayRecord_WAR_akfweb_.portlet-boundary.portlet-boundary_DisplayRecord_WAR_akfweb_.portlet-static.portlet-static-end div#aui_3_2_0_1133.portlet-borderless-container div#aui_3_2_0_1132.portlet-body div#displayRecord.displayRecord.manifestation.mainPortlet div.recordAll div.record.bordered.fadeColorBackground div#recordContent table tbody tr td a'):
        szerzo = driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'html.ltr.yui3-js-enabled.gecko.js.firefox.firefox68.firefox68-0.win body#aui_3_2_0_1130.orangeAndBlue.controls-visible.guest-community.signed-out.public-page div#aui_3_2_0_1135.top_bg div#wrapper div#content div#main-content.columns-2 div#aui_3_2_0_1134.portlet-layout div#column-1.aui-w70.portlet-column.portlet-column-first div#layout-column_column-1.portlet-dropzone.portlet-column-content.portlet-column-content-first div#p_p_id_DisplayRecord_WAR_akfweb_.portlet-boundary.portlet-boundary_DisplayRecord_WAR_akfweb_.portlet-static.portlet-static-end div#aui_3_2_0_1133.portlet-borderless-container div#aui_3_2_0_1132.portlet-body div#displayRecord.displayRecord.manifestation.mainPortlet div.recordAll div.record.bordered.fadeColorBackground div#recordContent table tbody tr td a'))).text
    if check_exists_by_xpath(driver,'/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div/div/div[4]/div[1]/div[1]/table/tbody/tr[3]/td[2]'):
        cim = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div/div/div[4]/div[1]/div[1]/table/tbody/tr[3]/td[2]').text
    if check_exists_by_xpath(driver,'/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div/div/div[4]/div[1]/div[1]/table/tbody/tr[4]/td[2]'):
        megjelenes = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div/div/div[4]/div[1]/div[1]/table/tbody/tr[4]/td[2]').text
    if check_exists_by_xpath(driver,'/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div/div/div[4]/div[1]/div[1]/table/tbody/tr[8]/td[2]'):
        sorozat = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[1]/div/div[1]/div/div/div/div[4]/div[1]/div[1]/table/tbody/tr[8]/td[2]').text
    return [isbn,szerzo,cim,megjelenes,sorozat]
    

df = pd.read_excel(r"C:\Users\balin\Desktop\konyvek_1polc.xlsx", header=None, names = ["isbn"])

driver = webdriver.Firefox(executable_path="C:\WebScraping\geckodriver.exe")
konyvek = []

for i in range(1):
    konyvek.append(query(df["isbn"][i][6:],driver))

end = time.time()

df.to_excel(r"C:\Users\balin\Desktop\WebScraping\ISBN grabber\konyv-isbn.xlsx", sheet_name="Sheet1")
print("It took", end-start," seconds to finish.")