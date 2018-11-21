#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:01:00 2018

@author: olaf
"""

import os
import csv
import pandas as pd

#Name of the file
file_name='tuc20181021vsec.sec'

def sec_2_df(file_name):
    
    #Separate file from extension
    filename, file_extension = os.path.splitext(file_name)
    
    #Read the .sec file, discard the header and keep the data
    a=open(file_name,'r')
    b=a.read()
    c=b.split('\n')
    data=c[18:]           
    
    
    #Create a dictionary from the data list
    fecha=[]
    hora=[]
    dd=[]
    h=[]
    d=[]
    z=[]
    f=[]
    lv=[]
    
    #Loop para crear diccionario
    for x in range(ldat):
        val=data[x].split(' ')
        lval=len(val)
        
        val2=[]
        for cc in range(lval):
            
            comp=val[cc]==''
            if comp == False:
                val2.append(val[cc])
          
        fecha.append(val2[0])
        hora.append(val2[1])
        dd.append(val2[2])
        h.append(val2[3])
        d.append(val2[4])
        z.append(val2[5])
        f.append(val2[6])
    #Crear diccionario    
    data_dict={}
    data_dict['date']=fecha
    data_dict['time']=hora
    data_dict['day_of_year']=dd
    data_dict['h']=h
    data_dict['d']=d
    data_dict['z']=z
    data_dict['f']=f
    
    #Transform to dataframe
    df=pd.DataFrame(data_dict)
    
    #Column names
    headers=['date','time','day_of_year','h','d','z','f']
    
    #change column names
    df=df[headers]
    
    #Correct dtypes
    df['date']=df['date'].astype(str)
    df['day_of_year']=df['day_of_year'].astype(int)
    df['h']=df['h'].astype(float)
    df['d']=df['d'].astype(float)
    df['z']=df['z'].astype(float)
    df['f']=df['f'].astype(float)
    
    
    #Separate date column for year,month and day 
    fecha=df['date']
    year=[]
    month=[]
    day=[]
    
    for fs in fecha:    
        ymd=fs.split('-')
        year.append(ymd[0])
        month.append(ymd[1])
        day.append(ymd[2])
    
    df['year']=year
    df['month']=month
    df['day']=day
    #Correct dtypes
    df['year']=df['year'].astype(int)
    df['month']=df['month'].astype(int)
    df['day']=df['day'].astype(int)
    
    #df=df.drop(['date'],axis=1)
    
    #Separate time column for hour, minute and second
    tiempo=df['time']
    hour=[]
    minute=[]
    second=[]
    
    for tt in tiempo:    
        hms=tt.split(':')
        hour.append(hms[0])
        minute.append(hms[1])
        second.append(hms[2])
    
    df['hour']=hour
    df['minute']=minute
    df['second']=second
    #Correct dtypes
    df['hour']=df['hour'].astype(int)
    df['minute']=df['minute'].astype(int)
    df['second']=df['second'].astype(float)
    
    #Rearrange columns order and discard date and time columns
    df=df.loc[:,['year','month','day','day_of_year','hour','minute','second','h','d','z','f']]
    
#    print(df.head())
#    print(df.tail())
    return df
    
base=sec_2_df(file_name)