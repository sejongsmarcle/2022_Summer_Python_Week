from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.yes24.com/Templates/FTLogin.aspx?ReturnURL=http://ticket.yes24.com/Pages/MyPage/MyPageMain.aspx")

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#SMemberID")
id.click()
pyperclip.copy("qkrtlgus1120")
pyautogui.hotkey("ctrl","v")
time.sleep(2)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#SMemberPassword")
pw.click()
pyperclip.copy("Samsung980618!")
pyautogui.hotkey("ctrl","v")
time.sleep(2)

# 로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, "#btnLogin")
login_btn.click()

# 검색
search = driver.find_element(By.CSS_SELECTOR, "#searchWord")
search.click()
search.send_keys("삼총사")

search_btn = driver.find_element(By.CSS_SELECTOR, "#perform-top > div.pf-right > div.pf-top-srch > a")
search_btn.click()

three = driver.find_element(By.CSS_SELECTOR, "#viewPerf > div.srch-list > div:nth-child(1) > div:nth-child(2) > p.item-tit > a")
three.click()

# 탭 전환
driver.switch_to.window(driver.window_handles[1])

# 공연 선택
day = driver.find_element(By.CSS_SELECTOR, "#rncalendar > div > table > tbody > tr:nth-child(5) > td:nth-child(6) > a")
day.click()

times = driver.find_element(By.CSS_SELECTOR, "#PerfPlayTime > a")
times.click()

reservation = driver.find_element(By.CSS_SELECTOR, "#mainForm > div.renew-wrap.rw2 > div > div.rn-05 > a.rn-bb03")
reservation.click()

# 탭 전환
driver.switch_to.window(driver.window_handles[2])

# 좌석 선택
seatselect = driver.find_element(By.CSS_SELECTOR, "#btnSeatSelect")
seatselect.click()

#좌선 선택 창 iframe 이동
driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@id='divFlash']/iframe[@name='ifrmSeatFrame']"))

seat = driver.find_element(By.CSS_SELECTOR, "#t700031")
seat.click()

booking = driver.find_element(By.CSS_SELECTOR, "#form1 > div.bx_seatbg > div.seatinfo > div > div.btn > p:nth-child(2)")
booking.click()

complete = driver.find_element(By.CSS_SELECTOR, "#form1 > div.bx_seatbg > div.seatinfo > div > div.btn > p:nth-child(2)")
complete.click()

#원래 팝업 프레임으로 돌아가기
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.ID,'StepCtrlBtnPanel'))

#step3  할인/쿠폰 다음 단계
nextstep_3= driver.find_element(By.CSS_SELECTOR, "#StepCtrlBtn03 > a:nth-child(2)")
nextstep_3.click()


#step4 수령 방법 단계
nextstep_4= driver.find_element(By.CSS_SELECTOR, "#StepCtrlBtn04 > a:nth-child(2)")
nextstep_4.click()

#stpe 5 결제 방법
selmeth= driver.find_element(By.CSS_SELECTOR, "#rdoPays22")
selmeth.click()

#select 선택
dropdown = Select(driver.find_element(By.ID,'selBank'))
dropdown.select_by_visible_text("국민은행")

#개인 정보 동의
infoagree= driver.find_element(By.CSS_SELECTOR, "#cbxCancelFeeAgree")
infoagree.click()

#결제하기
nextstep_5= driver.find_element(By.CSS_SELECTOR, "#imgPayEnd")
nextstep_5.click()