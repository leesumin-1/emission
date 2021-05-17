import time
import selenium
from selenium import webdriver
import matplotlib.pyplot as plt
import matplotlib

URL = 'http://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1464&param=013'

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)

# 리스트
year_list = []
total_emission_list = []
a = []

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
        a.append(year_table_tbody_tr_td.text)
        #print("\t", year_table_tbody_tr_td.text ,end="")
        #print(a)
    #print("")
time.sleep(3)

# 온실가스 배출량 출력
driver.get(url=URL)
emission_table=driver.find_elements_by_class_name("table_style_2")
# print(len(weather_table))

emission_table_tbody=emission_table[0].find_elements_by_tag_name("tbody")
# print(len(weather_table_tbody))

emission_table_tbody_tr_list=emission_table_tbody[0].find_elements_by_tag_name("tr")
# print(len(weather_table_tbody_tr_list))

for emission_table_tbody_tr in emission_table_tbody_tr_list :
    emission_table_tbody_tr_td_list=emission_table_tbody_tr.find_elements_by_tag_name("td")
    for emission_table_tbody_tr_td in emission_table_tbody_tr_td_list :
        total_emission_list.append(emission_table_tbody_tr_td.text)
        #print("\t", emission_table_tbody_tr_td.text ,end=" ")
        #print(total_emission_list)
        break
    print("")
time.sleep(3)

driver.close()

for i in range(1,9):
    year_list.append(a[i])

print(year_list)
print(total_emission_list)


#그래프 만들기
matplotlib.rcParams["axes.unicode_minus"]=False #폰트 깨짐 대처
plt.rc('font', family='Malgun Gothic')
x=len(year_list)
plt.bar(range(x), total_emission_list)
plt.xticks(range(x),year_list)
plt.title('년도별 온실가스 총배출량')
plt.xlabel('년도')
plt.ylabel('총배출량')
plt.show()