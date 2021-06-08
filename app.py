# TABHAY
from selenium import webdriver
from time import sleep
from flask import Flask, render_template, request
from selenium.webdriver.chrome.options import Options
import pandas as pd
datainput = pd.read_excel("hackkrega.xlsx")
email = list(datainput['email'])
password = list(datainput['password'])

#print(email)
#print(password)

idx_start = 0
curidx =0

def loginIntoFacebook(usr,pwd):
    if usr:
        options = Options()  
       # options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path = './chromedriver.exe', chrome_options = options)
        driver.get('https://www.facebook.com/')
        print(usr)
        print(pwd)
        email_in = driver.find_element_by_id('email')
        email_in.send_keys(usr)
        pass_in = driver.find_element_by_id('pass')
        pass_in.send_keys(pwd)
        login_div = driver.find_element_by_class_name('_6ltg')   # choose this carefully ... it keeps on changing lol XD
        login_button = login_div.find_element_by_tag_name('button')
        login_button.submit()
        sleep(1)
        return
    pass

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    global idx_start,curidx
    if not email or len(email) <0:
        print("Error In Email or All emails have been iterated")
        return 'Error In Email or All emails have been iterated'
    if len(email) -1 < idx_start:
        idx_start = 0
    curidx = idx_start
    idx_start+=1
    print(curidx)
    return render_template('index.html',email = email[curidx],password = password[curidx])
    
@app.route('/', methods = ['POST'])
def go():
    global idx_start,email,password,curidx
    logemail = email[curidx]
    logpassword = password[curidx]
    loginIntoFacebook(logemail, logpassword)
    idx_start+=1
    return '''
            <script>
            alert('Success :)');
            window.location = "/";
            </script>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=False,threaded=True)