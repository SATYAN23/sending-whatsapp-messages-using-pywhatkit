import pywhatkit as pwt
import time
import datetime
import pandas as pd
import os
import numpy as np

location = os.getcwd()+ './data_info.csv'
data = pd.read_csv(location)
data1 = np.array(data['Name']).reshape(-1,1).tolist()

data2 = np.array(data['Phonenumber']).reshape(-1,1).tolist()
data3 = np.array(data['Message']).reshape(-1,1).tolist()
data4 = np.array(data['Picture']).reshape(-1,1).tolist()
 
# using now() to get current time

current_time = datetime.datetime.now()
 

def main():

    X=current_time.hour
    
    Y=current_time.minute
    

 
    for phonenumber in data2:
        x = data2.index(phonenumber)
        phonenumber = str(phonenumber)
        msg =data3[x]
        pic = data4[x]
        for i in msg:
            msg = str(i)
        for i in pic:
            pic = i
        X = X
        Y = Y+1
        pic = os.getcwd() + pic
        caption = "please subscribe to my channel link is: https://www.youtube.com/channel/UCRwABdvUtddSbidtpZWMiTQ"
        pwt.sendwhats_image(phonenumber ,pic,caption ,X+1)
        
   
main()

