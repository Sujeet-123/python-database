from flask import Flask, jsonify

from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import google_sheet_api
from webdriver_manager.chrome import ChromeDriverManager





# flask minimal app

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



# ======================================================

main_link_list = []
data_list = []

def important_get_links():

    driver = webdriver.Chrome(ChromeDriverManager().install())

    

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
            print("None")
            time2 = None

        try:
            dining_reviews = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/section[3]/section/section/div/div/div/section/div[1]/div[1]/div/div/div[1]').text
            print("dining_reviews => ",dining_reviews)
        except:
            dining_reviews = None

        try:
            delivery_reviews = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/section[3]/section/section/div/div/div/section/div[3]/div[1]/div/div/div[1]').text
            print("delivery_reviews => ",delivery_reviews)
        except:
            delivery_reviews = None


        driver.execute_script('scrollTo(0,1000)')
        time.sleep(5)
        read_k=driver.find_elements(By.CLASS_NAME,'sc-ya2zuu-0.SWRrQ')
        for i in read_k:
            try:
                i.click()
                # time.sleep(2)
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

        if len(m)>=100:
            F_D_data=[m[0:99]]
            L_D_data=[m[99:]]
        else:
            L_D_data = None
            F_D_data=[m]
        

        value1 = [name, address, time2, dining_reviews, delivery_reviews, str(F_D_data), str(L_D_data)]
        google_sheet_api.append_googlesheet1(value1)


        result ={
            'Name':name,
            'Address':address,
            'time':time2,
            'Dining_reviews':dining_reviews,
            'Delivery_reviews':delivery_reviews,
            'Menu':m
            # 'F_D_data': F_D_data,
            # 'L_D_data':L_D_data
        }
        data_list.append(result)
    
    def click():
        
        for n,i in enumerate(main_link_list):
            print("In click function")
            if n==2:
                break
            driver.get(i)
            time.sleep(5)
            Data()




    driver.get("https://www.zomato.com/pune")
    time.sleep(5)


    def see_more():
        print("Clicked See More button ")
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(5)


        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_UP)
        time.sleep(3)
        
        # click on see more button                                            
        divs = driver.find_elements(By.CLASS_NAME,'sc-rbbb40-0.iwHbVQ')
        print("=========================")

        divs[5].click()
        time.sleep(6)

    def All_city_links():

        get_links()

        time.sleep(5)
        print("Collect links of restraunts ")
        see_more()

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

        for n,i in enumerate(city_links):
            print("Number of citys : ",n)
            if n==2:
                break
            time.sleep(2)
            driver.get(i)
            
            driver.maximize_window()
            time.sleep(3)
            get_links()
            time.sleep(3)

        click()

            # ===========================================================================================================================================


    links_list = []


    def get_links():

        # for i in range(30):
            
        #     driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        #     time.sleep(5)
        #     print(i)


        time.sleep(2)
        driver.execute_script('scrollTo(0,700)')
        time.sleep(3)
        links = driver.find_elements(By.CLASS_NAME,'jumbo-tracker a')
        time.sleep(3)    
        driver.minimize_window()
        # print("total links : ",len(links))
        
        for n,i in enumerate(links):
            link = i.get_attribute("href")
            links_list.append(link)
            print("count : ",n)
        
        print("links_list : ",len(links_list))
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        sub='order'

        for k in links_list:
            if (sub in k ) and (k not in main_link_list):
                main_link_list.append(k)
                # value1 = [k]
                # google_sheet_api.append_googlesheet10(value1)
            else:
                continue

        print("main_link_list : ",len(main_link_list))


        print("Get link")
            
    


    
    All_city_links()
    # get_links()



# ============================================================

# @app.route('/data',methods=["GET"])
# def important_get_data():



# @app.route('/data',methods=["GET"])


    # return None   

      

@app.route('/gt',methods=["GET"])
def main_fun():

   

    important_get_links()
    # api_links={

    #     'links':main_link_list
    # }

    # # return jsonify(api_links)
    return jsonify(data_list)

    


if __name__ == "__main__":
    app.run(debug=True)