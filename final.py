import time
from datetime import datetime
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
import pyautogui

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) 
web= webdriver.Chrome(options=options)

#輸入可以搶票的那天時間
execution_time = "2024-11-06 00:00:00.000"  
execution_datetime = datetime.strptime(execution_time, "%Y-%m-%d %H:%M:%S.%f") 

while True:
    current_datetime = datetime.now()
    time_difference = (execution_datetime - current_datetime).total_seconds()
    
    if time_difference > 0:

        print(f"Time difference: {time_difference} seconds") 
        time.sleep(0.00001)  # Sleep for 1 second
    else:  
                
            def run_webdriver(url):
                
                    web.get(url)
            
            
                    js_code = """
                        console.log('Running JavaScript code');
                        var checkbox = document.querySelector('input[type="checkbox"][value="1"]');
                        if (checkbox) {
                            checkbox.click();
                        }

                        var selectElements = document.querySelectorAll('select[name="roomCount[]"]');
                        if (selectElements.length >= 2) { 
                            selectElements[1].value = "1";
                        }

                        document.querySelector('input[value="下一步"]').click();
                    """

                    web.execute_script(js_code)


            def run_webdriver2(url):
                 #57 輸入名字   #64 輸入電話   #71 輸入email     #89 輸入名字      #64 輸入電話   #64 輸入電話
                    web.get(url)
                    js_code2 = """
                    var appNameInput = document.querySelector('input[name="app_name"]');
                
                    appNameInput.value = "李小潔"; 
                    
                    console.log("app_name:", appNameInput.value);
                    
                    
                    var app_tel = document.querySelector('input[name="app_tel"]');
                    
                    app_tel.value = "0912345678";
                    
                            console.log("app_tel:", app_tel.value);
                        
                        
                            var app_email = document.querySelector('input[name="app_email"]');
                        
                            app_email.value = "NAME@gmail.com";
                            
                            console.log("app_email:", app_email.value);
                            
                            var checkbox = document.querySelector('input[name="applicant_type"][value="4"]');
                            
                            checkbox.click();
                            
                            console.log("Checkbox is checked:", checkbox.checked);
                            
                            var other_reason = document.querySelector('input[name="other_reason"]');
                        
                            other_reason.value = "考試";
                            
                            
                            var cardRadio = document.querySelector('input[name="paymethod"][value="card"]');
                            cardRadio.checked = true;

                            document.querySelector('input[name="contact_name[]"]').value = "李小潔";

                            var checkbox = document.querySelector('input[name="applicant_type"][value="4"]');
                            
                            checkbox.click();
                            
                            const selectElement = document.querySelector('select[name="adult[]"]');

                        const options = selectElement.querySelectorAll('option');
                        
                        
                        options.forEach(option => {
                            if (option.value === '2') {
                            option.selected = true;
                            }  
                        });
                        
                        var checkbox = document.getElementById("iagree");
                            
                            checkbox.checked = true; 
                        
                        
                            
                        
                        var submitButton = document.querySelector("input[type='submit']");
                        if (submitButton) {
                        submitButton.click();
                        setTimeout(function() {
                            keyboard.press_and_release('enter');
                        }, 1); 
                        }
            
                    """

                    web.execute_script(js_code2)


            def run_webdriver3( ):
         #132 137 145 150 輸入卡號   #159 輸入安全碼   #167 輸入expiry_month ( 0->1月 1->2月...)   #173 輸入expiry_year( 0->2024 1->2025...)
                    js_code3 = """
                            
                    const inputElement = document.getElementById("card_1");

                    inputElement.value = "1234";
                    
                    
                    const inputElement1 = document.getElementById("card_2");

                    inputElement1.value = "5678";




                    const inputElement2 = document.getElementById("card_3");


                    inputElement2.value = "1234";

                    const inputElement3 = document.getElementById("card_4");


                    inputElement3.value = "5678";





                    var cvv2Input = document.getElementById("cvv2");


                    cvv2Input.value = "123";




                    var selectElement = document.querySelector('select[name="expiry_month"]');


                    selectElement.value = "1"; 
                    

                    var selectElement1 = document.querySelector('select[name="expiry_year"]');


                    selectElement1.value = "2"; 
            
            
                    """

                    web.execute_script(js_code3)

            def run_webdriver4( ):
                
                    js_code4 = """
                    console.log(1);

                    var btnSubmitForm = document.getElementById("btnSubmitForm");
                    console.log(2);

                    if (btnSubmitForm) { 
                        btnSubmitForm.click();
                    }
                    console.log(3);

                    """

                    web.execute_script(js_code4)

            if __name__ == '__main__':
                #輸入你的訂房日期
                url = "https://affairs-guesths.vm.nthu.edu.tw/guest10/index.php?liveFromYear=2025&liveFromMonth=2&liveFromDay=4&liveEndYear=2025&liveEndMonth=2&liveEndDay=5" 
                target_url = "https://affairs-guesths.vm.nthu.edu.tw/guest10/order.php"
                target_url2 = "https://webauthen.nccc.com.tw/acsn2_kernel/2/browser/challenge-request"

                run_webdriver(url)

                response = requests.get(target_url, verify=False)
                if response.status_code == 200:
                    run_webdriver2(target_url)
                    pyautogui.press('enter')
                    run_webdriver3()
                    pyautogui.press('enter')

                response2 = requests.get(target_url2)
                if response2.status_code == 200:
                    run_webdriver4()

                driver.quit()

            