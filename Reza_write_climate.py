
'''Canadian data extraction module: write functions 
    Copyright (C) 2007  Reza Hosseini, reza2357@yahoo.ca
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
Also add information on how to contact you by electronic and paper mail.

If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode:

    <program>  Copyright (C) <year>  <name of author>
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.'''



''' Modify the address of the data files in the 3rd and 5th line of the code'''



import sys
from Reza_canadian_data import *
stations=get_station_list("d:\Data")
value="MAX_TEMP","MIN_TEMP","ONE_DAY_RAIN","ONE_DAY_SNOW","ONE_DAY_PRECIPITATION","SNOW_ON_THE_GROUND" 
Topdirectory='d:\Data'
def write_a_month(f,s,year,month,val):
    value="MAX_TEMP","MIN_TEMP","ONE_DAY_RAIN","ONE_DAY_SNOW","ONE_DAY_PRECIPITATION","SNOW_ON_THE_GROUND" 
    data=s.get_data(year,value[val])
    num=s.stationnumber
    dis=s.district
    index=s.index_record
    Jan=range(0,31)
    Feb=range(31,60)
    Mar=range(60,91)
    Apr=range(91,121)
    May=range(121,152)
    Jun=range(152,182)
    Jul=range(182,213)
    Aug=range(213,244)
    Sep=range(244,274)
    Oct=range(274,305)
    Nov=range(305,335)
    Dec=range(335,366)
    x=Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec
    y='Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'
    if data!=0:
            fdata=data[1]
            rdata=data[0]
            m=month-1
            f.write(str(num)+','+str(dis)+','+str(index[3])+','+str(index[4])+','+str(index[5])+','+str(val)+','+str(year)+','+y[m])
            for i in x[m]:
                    if fdata[i]==15:
                        f.write(','+'NA')
                    elif fdata[i]==2:
                        f.write(','+'Tr')
                    elif i==59 and fdata[i]!=14:
                        f.write(','+'MFeb')
                    elif i==59 and abs(round(rdata[i]))>900:
                        f.write(','+'NA')
                    else:
                        f.write(','+str(round(rdata[i],2)))    
            f.write('\n') 
          
                 
def write_a_year(f,s,year,val):
    for i in range(12):
        write_a_month(f,s,year,i+1,val)

        
def write_all_value(f,s,val):
    years=range(1800,2003)
    for year in years:
        write_a_year(f,s,val)

def write_all(f,s):
    years=range(1800,2003)
    for year in years:
        for val in range(5):
            write_a_year(f,s,year,val)


def write_monthly(f,s,year,val):
    value="MAX_TEMP","MIN_TEMP","ONE_DAY_RAIN","ONE_DAY_SNOW","ONE_DAY_PRECIPITATION","SNOW_ON_THE_GROUND"  
    data=s.get_data(year,value[val])
    num=s.stationnumber
    dis=s.district
    index=s.index_record
    if data!=0:
        mdata=data[2][0:12]
        msgdays=data[2][12:24] 
        f.write(str(num)+','+str(dis)+','+str(index[3])+','+str(index[4])+','+str(index[5])+','+str(val)+','+str(year))
        for i in range(12):
            if msgdays[i]==0:
                f.write(','+str(round(mdata[i],2)))
            else:
                f.write(','+'NA')
        f.write('\n')        
        

def write_all_monthly(f,s,val):
    years=range(1880,2006)
    for year in years:
        write_monthly(f,s,year,val)

        
# R needs equal rows. We modify the functions for daily data.
def write_a_month_for_R(f,s,year,month,val):
    value="MAX_TEMP","MIN_TEMP","ONE_DAY_RAIN","ONE_DAY_SNOW","ONE_DAY_PRECIPITATION","SNOW_ON_THE_GROUND"  
    data=s.get_data(year,value[val])
    num=s.stationnumber
    dis=s.district
    index=s.index_record
    Jan=range(0,31)
    Feb=range(31,60)
    Mar=range(60,91)
    Apr=range(91,121)
    May=range(121,152)
    Jun=range(152,182)
    Jul=range(182,213)
    Aug=range(213,244)
    Sep=range(244,274)
    Oct=range(274,305)
    Nov=range(305,335)
    Dec=range(335,366)
    x=Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec
    y='Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'
    if data!=0:
            fdata=data[1]
            m=month-1
            f.write(str(num)+','+str(dis)+','+str(index[3])+','+str(index[4])+','+str(index[5])+','+str(val)+','+str(year)+','+y[m])
            for i in x[m]:
                    if fdata[i]==15:
                        f.write(','+'NA')
                    elif fdata[i]==2:
                        f.write(','+'Tr')
                    elif i==59 and fdata[i]!=14:
                        f.write(','+'MFeb')
                    elif i==59 and abs(round(data[0][i]))>900:
                        f.write(','+'NA')
                    else:
                        f.write(','+str(round(data[0][i],2)))    
            k=31-len(x[m]) 
            for i in range(k):
                f.write(','+'NOT')
            f.write('\n') 
            

def write_a_year_for_R(f,s,year,val):
    for i in range(12):
        write_a_month_for_R(f,s,year,i+1,val)

def write_all_value_for_R(f,s,val):
    years=range(1800,2003)
    for year in years:
        write_a_year_for_R(f,s,year,val)



#writing a year as one vector.
def write_the_year_vector(f,s,year,val):
    value="MAX_TEMP","MIN_TEMP","ONE_DAY_RAIN","ONE_DAY_SNOW","ONE_DAY_PRECIPITATION","SNOW_ON_THE_GROUND" 
    data=s.get_data(year,value[val])
    rdata=data[0]
    fdata=data[1]
    for i in range(365):
        if fdata[i]==15:
            f.write('NA'+',')
        elif fdata[i]==2:
            f.write('Tr'+',')
        elif i==59 and fdata[i]!=14:
            f.write('MFeb'+',')
        elif i==59 and abs(round(rdata[i]))>900:
            f.write('NA'+',')
        else:
            f.write(str(round(rdata[i],2))+',')   
    if fdata[365]==15:
         f.write('NA')
    elif fdata[365]==2:
         f.write('Tr')
    else:
        f.write(str(round(rdata[365],2))) 
        
#Writing a function that writes a file for a bunch of stations, for a fixed year and month.

def write_bunch(f,bunch,val,year,month):
    value="MAX_TEMP","MIN_TEMP","ONE_DAY_RAIN","ONE_DAY_SNOW","ONE_DAY_PRECIPITATION","SNOW_ON_THE_GROUND"  
    for b in bunch:
        s=stations[b]
        data=s.get_data(year,value[val])
        num=s.stationnumber
        dis=s.district
        index=s.index_record
        if data!=0:
            mdata=data[2][0:12]
            msgdays=data[2][12:24] 
            f.write(str(num)+','+str(dis)+','+str(index[3])+','+str(index[4])+','+str(index[5])+','+str(val)+','+str(year))
        if msgdays[month-1]==0:
            f.write(','+str(round(mdata[month-1],2)))
        else:
            f.write(','+'NA')
        f.write('\n') 


#Let us wite a function that gives the vector from y1 to y2 years.
def vec(f,s,val,y1,y2):
    value="MAX_TEMP","MIN_TEMP","ONE_DAY_RAIN","ONE_DAY_SNOW","ONE_DAY_PRECIPITATION","SNOW_ON_THE_GROUND" 
    for year in range(y1,y2-1):
        data=s.get_data(year,value[val])
        num=s.stationnumber
        dis=s.district
        index=s.index_record
        if data!=0:
           mdata=data[2][0:12]
           msgdays=data[2][12:24]
           for i in range(12):
                   if msgdays[i]==0:
                       f.write(str(round(mdata[i],2))+',')
                   else:
                       f.write('NA'+',')
        if data==0:
             f.write('NA'+','+'NA'+','+'NA'+','+'NA'+','+'NA'+','+'NA'+','+'NA'+','+'NA'+','+'NA'+','+'NA'+','+'NA'+','+'NA')
    data=s.get_data(y2,value[val])
    num=s.stationnumber
    dis=s.district
    index=s.index_record
    if data!=0:
       mdata=data[2][0:12]
       msgdays=data[2][12:24]
       for i in range(11):
              if msgdays[i]==0:
                  f.write(str(round(mdata[i],2))+',')
              else:
                  f.write('NA'+',')
       if msgdays[11]==0:
           f.write(str(round(mdata[11],2)))
       else:
          f.write('NA') 
    if data==0:
       f.write('NA'+','+'NA'+','+'NA'+','+'NA'+','+'NA'+','+'NA'+','+'NA'+','+'NA'+','+'NA'+','+'NA'+','+'NA'+','+'NA')
            








