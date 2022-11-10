from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager
# import google_sheet_api
import mysql.connector

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window() 
time.sleep(5)



li = ["https://www.zomato.com/pune/shri-swami-samartha-pure-veg-kothrud/order",

"https://www.zomato.com/pune/mcdonalds-shaniwar-peth/order",
"https://www.zomato.com/pune/mathura-pure-veg-jm-road/order",
"https://www.zomato.com/pune/little-italy-shivaji-nagar/order",]

# "https://www.zomato.com/pune/dominos-pizza-rasta-peth/order",

# "https://www.zomato.com/pune/rk-pure-veg-vishrantwadi/order",

# "https://www.zomato.com/pune/garva-biryani-sadashiv-peth/order",

# "https://www.zomato.com/pune/amritsari-kulcha-and-delhi-chaap-kalyani-nagar/order",

# "https://www.zomato.com/pune/burger-king-1-senapati-bapat-road/order",

# "https://www.zomato.com/pune/pizza-hut-shukrawar-peth/order"



# data = pd.read_csv("links.csv")

# print("length of data",data)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#zecData12345",
    database="restraunt_data"
    )

mycursor = mydb.cursor()


for n,i in enumerate(li):
    driver.get(i)
    print("================")
    time.sleep(10)



def Data():

    try:
        name = driver.find_element(By.CLASS_NAME,'sc-7kepeu-0.sc-eilVRo.eAhpQG').text
        print("Name => ",name)
    except:
        name = None

    try:
        address = driver.find_element(By.CLASS_NAME,'sc-cpmLhU.fDVcNc').text
        print("Address name => ",address)
    except:
        address = None


    try:
        times = driver.find_element(By.CLASS_NAME,'sc-fhYwyz.fRKkxr').text.split('(')
    
        print("Time => ",times[0])
        time2 = times[0]
    except:
        time2 = None

    try:
        review=driver.find_elements(By.CLASS_NAME,'sc-1q7bklc-1.cILgox')

        dining_review = review[0].text
        
        delivery_review = review[1].text
    
    except:
            dining_review=None
            delivery_review = None




    driver.execute_script('scrollTo(0,1000)')
    time.sleep(5)
    read_k=driver.find_elements(By.CLASS_NAME,'sc-ya2zuu-0.SWRrQ')
    for i in read_k:
        try:
            i.click()
            time.sleep(2)
        except:
            print("except")
            pass
    m=[]
    D_Name = []
    divs = driver.find_elements(By.CLASS_NAME,'sc-1s0saks-17.bGrnCu')
    for div in divs:
        Down_list = []
        try:
            Dname = div.find_element(By.CLASS_NAME,'sc-1s0saks-15.iSmBPS').text
            Down_list.append(Dname)
            print("Dname => ",Dname)
        except:
            Dname = None
            Down_list.append(Dname)

        try:
            Dvotes = div.find_element(By.CLASS_NAME,'sc-z30xqq-4.hTgtKb').text
            Down_list.append(Dvotes)
            print("votes => ",Dvotes)
        except:
            Dvotes = None
            Down_list.append(Dvotes)

        try:
            Dprice = div.find_element(By.CLASS_NAME,'sc-17hyc2s-1.cCiQWA').text
            Down_list.append(Dprice)
            print("Dprice => ",Dprice)
        except:
            Dprice = None
            Down_list.append(Dprice)

        try:
            Ddiscrib = div.find_element(By.CLASS_NAME,'sc-1s0saks-12.hcROsL').text
            Down_list.append(Ddiscrib)
            print("Ddiscrib => ",Ddiscrib)
        except:
            Ddiscrib = None
            Down_list.append(Ddiscrib)
        D_Name.append(Down_list)


    for i, n in enumerate(D_Name):
        if n not in m:
            m.append(n)





    # mycursor.execute("CREATE TABLE  zomatodata(item_id INT(11) NOT NULL PRIMARY KEY,res_name VARCHAR(50),res_address VARCHAR(50),open_time VARCHAR(50),Dining_reviews FLOAT(10),Delivery_reviews FLOAT(10),Dishes_name TEXT)")
    data_insert = "INSERT INTO zomatodata1 (res_name, res_address,open_time,Dining_reviews,Delivery_reviews,Dishes_name) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (name,address,time2,dining_review,delivery_review,str(m))
    mycursor.execute(data_insert, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")



        

    
    # if len(m)>=100:
    #     F_D_data=[m[0:99]]
    #     L_D_data=[m[99:]]
    # else:
    #     L_D_data = None
    #     F_D_data=[m]
    # print(m)  
    # value1 = [name, address, time2, dining_reviews, delivery_reviews, str(F_D_data), str(L_D_data)]
    # google_sheet_api.append_googlesheet1(value1)




def click():

    for i in li:
        print("In click function")
        driver.get(i)
        time.sleep(5)
       
        Data()

click()