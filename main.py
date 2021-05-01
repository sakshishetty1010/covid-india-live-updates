from flask import Flask,render_template,request
app = Flask(__name__)
import requests
import bs4

import plyer
import time
import datetime
import threading

def vacdetails():
    info =[]
    url2 = "https://www.mohfw.gov.in/"
    html_data2 = get_html_data(url2)
    bs =  bs4.BeautifulSoup(html_data2.text,'html.parser')
    det = bs.find("div",class_="fullbol").find("span",class_="totalvac").get_text()
    info.append(det)
    info.append( bs.find("div",class_="fullbol").find("span",class_="coviddata").get_text())
    return info

def get_html_data(url):
    data = requests.get(url)
    return data

def get_html_data(url):
    data = requests.get(url)
    return data

def get_corona_detail():
    url = "https://www.mygov.in/covid-19/"
    html_data =get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text,'html.parser')
    info_div = bs.find("div",class_="information_row").find_all("div",class_="iblock_text")
    all_details=[]
    for block in info_div:
        count = (block.find("span",class_="icount").get_text())
        text = (block.find("div",class_="info_label").get_text())
        all_details.append(text)
        all_details.append(count)
        #all_details = (((all_details+text+" : "+count))).replace(" ","")+"\n"
    new = []
    for detail in all_details:
        new.append(detail.replace(" ","").replace("\n",""))
    return new

@app.route('/',methods=["GET","POST"])
def hello_world():
    return render_template('index.html',det = detail,info = info)

if __name__ == "__main__"    :
        
    detail=[]
    detail = get_corona_detail()
    info = vacdetails()
    app.run(debug = True)