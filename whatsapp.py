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

 
# using now() to get current time

current_time = datetime.datetime.now()
 
# Printing attributes of now()msg = ''
def main():

    X=current_time.hour
    
    Y=current_time.minute
    
    for phonenumber in data2:
        x = data2.index(phonenumber)
        phonenumber = str(phonenumber)
        msg =data3[x]
        for i in msg:
            msg = str(i)
        X = X
        Y = Y+1
        pwt.sendwhatmsg(phonenumber, msg ,X,Y)
   
main()

