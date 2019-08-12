# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 21:59:49 2019

@author: sreekar
"""


from selenium import webdriver
import pandas as pd


     
     
     
driver = webdriver.Chrome(executable_path=r"C:\Users\sreekar\Desktop\software\Chrome Driver\chromedriver.exe")

driver.get("https://www.holidify.com/explore/")
c=[]
link = []

for element in driver.find_elements_by_tag_name('h2'):
       a = element.text
       link.append(a)
       b=a.split(",")
       c.append(b)

c.remove(c[0])
c.remove(c[0])
df =pd.DataFrame(c)
link.remove(link[0])
link.remove(link[0])
for i in range(0,59):
    f = df[0][i]
    e=f.split('.')
    df[0][i] = e[1]
print(df)
df.rename(columns={0: "City", 1: "State"})
Q = []

def informaton(city):
    Link = city
    l = driver.find_element_by_link_text(Link)
    l.click()
    weather = driver.find_element_by_class_name("currentWeather").text
    Q.append(weather)
   

for i in link:
    q = informaton(i)
    driver.back()
country = ['India' for i in range(60)]
df['Weather']= Q
df['Country'] = country
df.to_csv('data.csv')
