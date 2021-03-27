from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import schedule

addr = "http://xgsm.hitsz.edu.cn/zhxy-xgzs/xg_mobile/shsj/loginChange"
name = ''
password = ''
def Report(browser, addr,name,password):
    try:
        browser.get(addr)
        sleep(1)
    except Exception as e:
        print(e)
        print("打开browser失败")
    try:
        loginbox = browser.find_element_by_class_name('login-box')
        uauth = loginbox.find_element_by_css_selector('button[onclick="tongyishenfen()"]')
        uauth.click()
        sleep(1)
    except Exception as e:
        print(e)
        print("没有找到登录按钮")
        return 0

    try:
        username = browser.find_element_by_id('username')
        username.send_keys(name)
        sleep(1)
        passwd = browser.find_element_by_name('password')
        passwd.send_keys(password)
        sleep(1)
        loginbtn = browser.find_element_by_class_name('login_box_landing_btn')
        loginbtn.click()
        print("登录成功")
        sleep(1)
    except Exception as e:
        print(e)
        print("没有找到登录窗口")
        return 0

    try:
        dailyReport = browser.find_element_by_id('mrsb')
        dailyReport.click()
        print("添加记录")
        sleep(1)
    except Exception as e:
        print(e)
        print("没有找到疫情上报")
        return 0

    try:
        addnewbtn = browser.find_element_by_class_name('right_btn')
        addnewbtn.click()
        sleep(1)
    except Exception as e:
        print(e)
        print("没有找到登录窗口")
        return 0

    try:

        alerttext = browser.switch_to.alert.text
        print(alerttext)
        if(alerttext == '今日已生成疫情上报！'):
            print("今天已提交")
            browser.switch_to.alert.accept()
            return 1
    except Exception as e:
        print(e)
        print("今天未提交")

    try:
        iread = browser.find_element_by_id('txfscheckbox')
        iread.click()
        print("我已阅读")
        sleep(1)
    except Exception as e:
        print(e)
        print("没有我已阅读")
        return 0
    try:
        sendup = browser.find_element_by_class_name('right_btn')
        sendup.click()
        print("提交")
        sleep(1)
    except Exception as e:
        print(e)
        print("没有我已阅读")
        return 0
    return 1

def dailydo():
    print("Reporting")
    try:
        browser = webdriver.Chrome()
    except Exception as e:
        print(e)
        print("打开browser失败")
    Report(browser,addr,name,password)
    browser.quit()
    print("success")
# browser = webdriver.Chrome()
# alert = Report(browser,addr,name,password)
# schedule.every(30).seconds.do(dailydo)
schedule.every().day.at('09:05').do(dailydo)
while True:
        schedule.run_pending()