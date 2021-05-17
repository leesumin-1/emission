import time
import selenium
from selenium import webdriver

URL = 'http://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1464&param=013'

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)

#연도 출력
driver.get(url=URL)
year_table=driver.find_elements_by_class_name("table_style_2")
# print(len(weather_table))

year_table_tbody=year_table[0].find_elements_by_tag_name("thead")
# print(len(weather_table_tbody))

year_table_tbody_tr_list=year_table_tbody[0].find_elements_by_tag_name("tr")
# print(len(weather_table_tbody_tr_list))

for year_table_tbody_tr in year_table_tbody_tr_list :
    year_table_tbody_tr_td_list=year_table_tbody_tr.find_elements_by_tag_name("th")
    for year_table_tbody_tr_td in year_table_tbody_tr_td_list :
        print("\t", year_table_tbody_tr_td.text ,end="")
    print("")
time.sleep(3)
