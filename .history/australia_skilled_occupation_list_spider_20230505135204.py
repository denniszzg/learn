# name:      spider_multiprocess.py
# version:   0.2
# author:    Dennis
# desc:      This spider can get the name list of car license plate lottery.
#            It automatic download data by year, and merge into one csv file.
#            It also can show the repeated data, if it exists. 

from selenium import webdriver
from selenium.webdriver.support.select import Select
import multiprocessing as mp
import time
#import csv
import pandas as pd
import glob


#使用显式chrome
#driver = webdriver.Chrome()

#使用headless chrome
option = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
option.add_experimental_option("prefs",prefs)
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option)
driver.maximize_window()

#通用参数
path = "/home/dennis/Desktop"
outputFile = path + "/alldata.csv"
url = "http://apply.xkctk.jtys.tj.gov.cn/apply/norm/personQuery.html"
#issueList = [str(x) for x in range(201402, 201403)] #列表生成式生成期号列表


#生成每一页中申请编码和姓名对应的字典
def getContent():
    
    content = driver.find_elements_by_css_selector("td[style='border-bottom: 1px dashed #50AAB5;']")
    list = []
    for i in content:
        list.append(i.text)
    nameList = zip([issue]*pagesNum,list[0::2],list[1::2])  #期号，编码，姓名
    next = driver.find_element_by_xpath("//*[@class='pageturn']/ul/li[7]/a")
    next.click()
    #time.sleep(1) 

    return nameList
    
    
    
def writeCsv(d):
    file = path +r"\tmp\%s.csv"%issue
    # with open(file,'a+', newline="") as f:
        # w = csv.writer(f)
        # w.writerows(d)
    df = pd.DataFrame(d)
    df[1] = ["%s\t"% i for i in df[1]]  #编码列最后加"\t"以禁用科学计数法
    df.to_csv(file, mode='a', index=False, header=False, encoding="gbk")
    
            
    
#获取某一期的所有数据
def run(i):
    global issue, pagesNum
    issue = i
    start = time.time()
    init()
    pages = driver.find_element_by_xpath("//*[@class='float_right']/tbody/tr/td[3]/b/span").text
    pagesNum = eval(pages)
    for i in range(pagesNum):
        data = getContent()
        writeCsv(data)
        print("\r 期号 {} 共 {} 页，当前完成第 {} 页，进度 {:^4.1f}%".format(issue, pagesNum, i+1, ((i+1)/pagesNum)*100), end="")
    
    end = time.time()
    dtime = end - start
    print("\n 花费时间：{:.2f} 秒".format(dtime))


#选择期号并查询后，初始化首页
def init():
    
    driver.implicitly_wait(3)
    driver.get(url)
    sel = driver.find_element_by_xpath("//select[@id='issueNumber']")
    Select(sel).select_by_value(issue)
    driver.find_element_by_xpath("//a[@id='search']/img").click()
    #time.sleep(1)
    driver.find_element_by_id("num").click()
    driver.find_element_by_id("num").clear()
    driver.find_element_by_id("num").send_keys("1")
    driver.find_element_by_id("jumppage").click()
    #time.sleep(1)
    
#临时一次性函数，用于在csv文件中写入期号（0.1版本抓取时csv中未包含期号）
def insertIssueNo():
    csvList = glob.glob(path + r"\tmp\*.csv")
    for i in csvList:
        df = pd.read_csv(i,header=None, encoding='gbk')
        df[2] = i[-10:-4]   #文件第3列写入期号
        df.to_csv(i,mode='w',index=False, header=False,encoding='gbk')

    
#合并所有csv数据
def concat():
    csvList = glob.glob(path + r"\tmp\*.csv")   #full path
    print("本次共处理 %s 个CSV文件，处理中..."%len(csvList))
    for each_csv in csvList:
        df = pd.read_csv(each_csv, header=None, encoding="gbk")
        df.to_csv(outputFile, mode='a', index=False, header=False, encoding="gbk")
    print("处理完成")
    
#查询重复项
def checkDup():
    df = pd.read_csv(path+"\\alldata.csv", header=None, encoding="gbk")
    #dup = df[df.duplicated()] #提取重复值（标记为true的，不包括第一个）
    dup = df[df.duplicated(1, keep=False)] #根据第2列提取重复值（包括第一个）
    dup.to_csv(path+"\\dupdata.csv", mode='a', index=False, header=False, encoding="gbk")
    print(dup)
    
    
def main():
    
    pool = mp.Pool()
    pool.map(run, issueList)
    pool.close()
    pool.join()

    
if __name__ == '__main__':
    main()
    #concat()
    #checkDup()
    
    #insertIssueNo()

#driver.close()
#driver.quit()


