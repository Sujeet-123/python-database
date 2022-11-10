from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
# import google_sheet_api
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector


driver = webdriver.Chrome(ChromeDriverManager().install())



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#zecData12345",
    database="restraunt_data"
    )

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE link1(links_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,links VARCHAR(200)")


driver.get("https://www.zomato.com/pune")
time.sleep(5)


driver.maximize_window()
time.sleep(5)

def see_more():
    print("Clicked See More button ")
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(5)


    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_UP)
    time.sleep(5)
    
    # click on see more button                                            
    divs = driver.find_elements(By.CLASS_NAME,'sc-rbbb40-0.iwHbVQ')
    print("=========================")

    divs[5].click()
    time.sleep(6)

def city_links():

    get_links()

    time.sleep(5)
    print("Collect links of restraunts ")
    see_more()
    # driver = webdriver.Chrome(ChromeDriverManager().install())

    city_links = []

    div1 = driver.find_elements(By.CLASS_NAME,'sc-bke1zw-1.gLbmAn a')

    for i in div1:
        hrf = i.get_attribute('href')
        city_links.append(hrf)
        print(hrf)


    div1 = driver.find_elements(By.CLASS_NAME,'sc-bke1zw-1.gGzIKR a')

    for i in div1:
        hrf = i.get_attribute('href')
        city_links.append(hrf)
        print(hrf)



    div1 = driver.find_elements(By.CLASS_NAME,'sc-bke1zw-1.jdRPl a')

    for i in div1:
        hrf = i.get_attribute('href')
        city_links.append(hrf)
        print(hrf)

    print("city_links_len = > ",len(city_links))
    # driver.maximize_window()

    for n,i in enumerate(city_links):
        if n==2:
            break
        print("Number of citys : ",n)
        time.sleep(2)
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(i)
        driver.maximize_window()
        time.sleep(3)
        get_links()
        time.sleep(5)

# ===========================================================================================================================================


links_list = []

main_link_list = []

def get_links():
    time.sleep(5)
    for i in range(5):
        
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(5)
        print(i)
        if(i==15):
            driver.execute_script('scrollTo(0,700)')
            time.sleep(2)

    time.sleep(2)
    driver.execute_script('scrollTo(0,700)')
    time.sleep(3)
    links = driver.find_elements(By.CLASS_NAME,'jumbo-tracker a')
    time.sleep(3)    
    driver.minimize_window()
    print("total links : ",len(links))
    
    for n,i in enumerate(links):
        link = i.get_attribute("href")
        links_list.append(link)
        print("count : ",n)
      
    print("links_list : ",len(links_list))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    sub='order'
    

    for n, k in enumerate(links_list):
        if (sub in k ) and (k not in main_link_list):
            mycursor.execute('insert into LINKS_TABLE(total_links) values("{}")'.format(k))
            main_link_list.append(k)
            print("done")  
            # value1 = [k]
            # google_sheet_api.append_googlesheet10(value1)
           

            print(mycursor.rowcount, "record inserted.")

        else:
            continue

    print("main_link_list : ",len(main_link_list))


    print("Get link")


# get_links()
city_links()


mydb.commit()
mydb.close()

# print(main_link_list)
# print("main_link_list : ",len(main_link_list))

# df = pd.DataFrame(main_link_list)
# for row in df.itertuples():
#     mycursor.execute("INSERT INTO LINKS_TABLE (total_links) VALUES (%s)", (row))
driver.quit()

# df = pd.DataFrame(main_link_list)
# df.to_csv("A.csv",header=False,index=False)
