
'''Canadian data extraction module examples
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



import sys;sys.path.append("D:\School\Research\Climate\Python_code");from Reza_canadian_data import *;stations=get_station_list("d:\Data");value="MAX_TEMP","MIN_TEMP","ONE_DAY_RAIN","ONE_DAY_SNOW","ONE_DAY_PRECIPITATION","SNOW_ON_THE_GROUND" 

Topdirectory="D:\Data"

index=s.index_record
len(index)
#21
## Here is a list of what data is available in the index_record
#index[0] discrit
#index[1] name
#index[2]
#index[3]latitude
#index[4]longitude
#index[5]elevation
#index[6]MAX_T start
#index[7]MIN_T start
#index[8]MEAN_T start
#index[9]RF start
#index[10]SF start
#index[11]PR start
#index[12]SD start
#index[13]MAX_T end
#index[14]MIN_T end
#index[15]MEAN_T end
#index[16]RF end
#index[17]SF end
#index[18]PR end
#index[19]SD end
#index[20] availability
  

#How many stations in Alberta?
numalb=0;r=range(len(stations))
for i in range(len(stations)):
	t=stations[i]
        r[i]=0
	if t.stationnumber.startswith('30') and 1800<t.index_record[11]<2006 and 1800<t.index_record[18]<2006:
		numalb=numalb+1
                r[i]=i

albindex=range(numalb)
for i in range(numalb):
        for j in range(len(stations)):
                if r[j]!=0:
                    albindex[i]=r[j]                       
                    r[j]=0
                    break
#>1253 with available precipitation data.


###finding out which station has the largest range?

albyears=range(len(albindex))
for i in albyears:
	j=albindex[i]
        t=stations[j]
	index=t.index_record
	albyears[i]=index[18]-index[11]+1
	


m=max(albyears)
sum(albyears)/1253
#Answer: 123 for max and 20 for average

for i in range(len(albindex)):
	if albyears[i]==m:
		x=albindex[i]
#2436
#finding out how many stations have more than 50 years of data.
x=0
for i in range(len(albyears)):
	if albyears[i]>50:
		x=x+1
# 96 more than 50 years, 34 more than 75 and only 6 more than 100! #557 stations less than 10 years we should throw them away!
#6 stations are more than 100. We choose those three for some primary analysis. Let's find their number and call them
#lstn,lstn2,lstn3,lstn4,lstn5,lstn6

#Let's find out the mean of the first year and the last year
sum1=0
sum2=0
for i in range(numalb):
	t=stations[albindex[i]]
	a=t.index_record[11]
	b=t.index_record[18]
	sum1=sum1+a
	sum2=sum2+b

av1=sum1/numalb
av2=sum2/numalb
#av1=1965
#av2=1985
		
#Now let's extract the stations with more than 50 years
numalb50=0
for i in range(len(stations)):
	t=stations[i]
        r[i]=0
	if t.stationnumber.startswith('30') and 1800<t.index_record[11]<2006 and 1800<t.index_record[18]<2006 and t.index_record[18]-t.index_record[11]+1>50:
		numalb50=numalb50+1
                r[i]=i

albindex50=range(numalb50)
for i in range(numalb50):
        for j in range(len(stations)):
                if r[j]!=0:
                    albindex50[i]=r[j]                       
                    r[j]=0
                    break

# the av1 and av2 for this case is 1918 and 1990

#The same for the ones more than 100 years
numalb100=0
for i in range(len(stations)):
	t=stations[i]
        r[i]=0
	if t.stationnumber.startswith('30') and 1800<t.index_record[11]<2006 and 1800<t.index_record[18]<2006 and 1800<t.index_record[13]<2006 and 1800<t.index_record[6]<2006 and t.index_record[18]-t.index_record[11]+1>100 and t.index_record[13]-t.index_record[6]+1>100:
		numalb100=numalb100+1
                r[i]=i
albindex100=range(numalb100)
for i in range(numalb100):
        for j in range(len(stations)):
                if r[j]!=0:
                    albindex100[i]=r[j]                       
                    r[j]=0
                    break
#The list of the ones for more than a 100 is the following:
#albindex100=2436(calgary), 2483, 2488, 2497, 2516, 2633(banff)

#next task plotting the stations over alberta
#writing out the stations of alberta with position, the start and end year.

g=open('yl.txt','w')
for i in range(numalb):
    t=stations[albindex[i]]
    num=t.stationnumber
    ind=t.index_record
    g.write(str(num)+','+str(ind[3])+','+str(ind[4])+','+str(ind[5])+','+str(ind[11])+','+str(ind[18])+'\n')
g.close()    

#Now we want to find a station above 5300 with at least 80 years of data
numalb5300=0
for i in range(len(stations)):
	t=stations[i]
        r[i]=0
	if t.stationnumber.startswith('30') and t.index_record[3]>5300 and 1800<t.index_record[11]<2006 and 1800<t.index_record[18]<2006 and t.index_record[18]-t.index_record[11]+1>80:
		numalb5300=numalb5300+1
                r[i]=i
albindex5300=range(numalb5300)
for i in range(numalb5300):
        for j in range(len(stations)):
                if r[j]!=0:
                    albindex5300[i]=r[j]                       
                    r[j]=0
                    break
            
g=open('yl5300.txt','w')
for i in range(numalb5300):
    t=stations[albindex5300[i]]
    num=t.stationnumber
    ind=t.index_record
    g.write(str(num)+','+str(ind[3])+','+str(ind[4])+','+str(ind[5])+','+str(ind[11])+','+str(ind[18])+'\n')
g.close()



#we get the following result 2007, 2057, 2143, 2167, 2823, 2852, 3018, 3071
#3011120,5317,11351,720,1914,2003
#3012280,5353,11104,605,1912,1997
#3015400,5327,11139,686,1905,1991
#3015960,5353,11407,701,1906,2003
#3061200,5408,11441,671,1910,2003
#3062440,5322,11742,991,1917,2003
#3070560,5512,11924,745,1913,2003
#3072657,5843,11109,0,1883,1967


#Writing Calgary pcpn for one year as a vector. Here I have imported
#a writing command from write_cilmate

f=open('lstn1980.txt','w')
write_the_year_vector(f,lstn,1980,4)
f.close()


f=open('lstn1950.txt','w')
write_the_year_vector(f,lstn,1950,4)
f.close()

f=open('lstn2000.txt','w')
write_the_year_vector(f,lstn,2000,4)
f.close()


#Because there are too many stations alot of them have too much missing
#Sometimes we pick certain stations.
#Let us pick the stations which have more than 50 years and include 1980.

numalb1980=0;r=range(len(stations))
for i in range(len(stations)):
	t=stations[i]
        r[i]=0
	if t.stationnumber.startswith('30') and 1800<t.index_record[11]<2006 and t.index_record[18]-t.index_record[11]+1>50 and t.index_record[18]>1979:
		numalb1980=numalb1980+1
                r[i]=i
albindex1980=range(numalb1980)
for i in range(numalb1980):
        for j in range(len(stations)):
                if r[j]!=0:
                    albindex1980[i]=r[j]                       
                    r[j]=0
                    break

#Now to find the correlation as a function of distance, for all the above stations,
#we write for 1980. As the first three componenets we include the longitude,
#the latitude and the elevation.

f=open('50year.txt','w')
for i in albindex1980:
    s=stations[i]
    data=s.get_data(1980,'ONE_DAY_PRECIPITATION')
    ind=s.index_record
    if data!=0:
            rdata=data[0]
            fdata=data[1]
            f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
            for i in range(365):
                if fdata[i]==15:
                    f.write('-1.0'+',') #NA
                elif fdata[i]==2:
                    f.write('0.0'+',') #Trace
                elif i==59 and fdata[i]!=14:
                    f.write('-1.0'+',') #MFeb
                elif i==59 and abs(round(rdata[i]))>900:
                    f.write('-1.0'+',')
                else:
                    f.write(str(round(rdata[i],2))+',')   
            if fdata[365]==15:
                 f.write('-1.0')
            elif fdata[365]==2:
                 f.write('0.0') #Trace
            else:
                 f.write(str(round(rdata[365],2))) 

            f.write('\n')
                


#Finding special stations:
#Let us find the station with the highest elevation:
i=2436
for j in albindex:
        s=stations[j]
        ind1=s.index_record[5]
        t=stations[i]
        ind2=t.index_record[5]
        if ind1>ind2:
                i=j

        
        
#Analyzing S(2436)
f=open('S-MaxT.txt','w')
write_all_monthly(f,s,0)
f.close()
f=open('S-minT.txt','w')
write_all_monthly(f,s,1)
f.close()
f=open('S-rain.txt','w')
write_all_monthly(f,s,2)
f.close()
f=open('S-snow.txt','w')
write_all_monthly(f,s,3)
f.close()
f=open('S-PCPN.txt','w')
write_all_monthly(f,s,4)
f.close()
f=open('S-ground.txt','w')
write_all_monthly(f,s,5)
f.close()


## We want to see how the distribution of PCPN looks like at a
##fixed location and time. To do that we write a file jan 1st of S(2436)
f=open('distcheck.txt','w')
s=stations[2436]
val=4
years=range(1880,2006)
i=0
for year in years:
        data=s.get_data(year,value[val])
        if data!=0:
                d=data[0][i]
                fl=data[1][i]
                if fl==15:
                        f.write(','+'NA')
                elif fl==2:
                        f.write(','+'Tr')
                elif i==59 and fl!=14:
                        f.write(','+'MFeb')
                elif i==59 and abs(round(d))>900:
                        f.write(','+'NA')
                else:
                        f.write(','+str(round(d,2)))

f.close()

##Finding out the distribution of PCPN for monthly data.
f=open('mdistcheck.txt','w')
s=stations[2436]
val=4
years=range(1880,2006)
i=0
for year in years:
        data=s.get_data(year,value[val])
        if data!=0:
           mdata=data[2][i]
           msgday=data[2][12+i] 
           if msgday==0:
                f.write(','+str(round(mdata,2)))
           else:
                f.write(','+'NA')
                
f.close()        

                        


            

###Station ;ist of Alberta with available years.                
f=open('slist-alb.txt','w')
for i in albindex:
        s=stations[i]
        ind=s.index_record
        if 1800<ind[11]<2006 and 1800<ind[18]<2006:
                a=ind[18]-ind[11]
                f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+','+str(a))        
        else: 
                f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+','+'0')
        f.write('\n')        

f.close()                




#Number of days with PCPN per year for two stations:
s=stations[2436]## Calgary airport
f=open('s-pcpn-days.txt','w')
for i in range(1880,2002):
        data=s.get_data(i,'ONE_DAY_PRECIPITATION')
        if data==0:
                f.write(str(i)+','+'NA'+'\n')
                      
        else:
                d=data[0]
                fl=data[1]
                n=0
                for k in range(366):
                        if fl[k]==15:
                                n=n+1
                
                x=0
                for j in range(366):
                        if d[j]>0 and fl[j]!=14:
                                x=x+1
                if n>5:
                        f.write(str(i)+','+'NA'+'\n')
                else:
                        f.write(str(i)+','+str(x)+'\n')           

s=stations[2633] ##BANFF
f=open('s-pcpn-days2.txt','w')
for i in range(1880,2002):
        data=s.get_data(i,'ONE_DAY_PRECIPITATION')
        if data==0:
                f.write(str(i)+','+'NA'+'\n')
                      
        else:
                d=data[0]
                fl=data[1]
                n=0
                for k in range(366):
                        if fl[k]==15:
                                n=n+1
                
                x=0
                for j in range(366):
                        if d[j]>0 and fl[j]!=14:
                                x=x+1
                if n>5:
                        f.write(str(i)+','+'NA'+'\n')
                else:
                        f.write(str(i)+','+str(x)+'\n')
                                                                   
                                        



#Let us pick stations which include precipitation and max temp between 1960-2000
                        

numalb40=0;r=range(len(stations))
for i in range(len(stations)):
	t=stations[i]
        r[i]=0
	if t.stationnumber.startswith('30') and 1800<t.index_record[11]<1960 and 1999<t.index_record[18]<2007 and 1800<t.index_record[6]<1960 and 1999<t.index_record[13]<2007:
		numalb40=numalb40+1
                r[i]=i
albindex40=range(numalb40)
for i in range(numalb40):
        for j in range(len(stations)):
                if r[j]!=0:
                    albindex40[i]=r[j]                       
                    r[j]=0
                    break
                
f=open('40yearPCPN00.txt','w')
for i in albindex40:
    s=stations[i]
    data=s.get_data(1980,'ONE_DAY_PRECIPITATION')
    ind=s.index_record
    if data!=0:
            rdata=data[0]
            fdata=data[1]
            f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
            for i in range(365):
                if fdata[i]==15:
                    f.write('-1.0'+',') #NA
                elif fdata[i]==2:
                    f.write('0.0'+',') #Trace
                elif i==59 and fdata[i]!=14:
                    f.write('-1.0'+',') #MFeb
                elif i==59 and abs(round(rdata[i]))>900:
                    f.write('-1.0'+',')
                else:
                    f.write(str(round(rdata[i],2))+',')   
            if fdata[365]==15:
                 f.write('-1.0')
            elif fdata[365]==2:
                 f.write('0.0') #Trace
            else:
                 f.write(str(round(rdata[365],2))) 

            f.write('\n')
f.close()
f=open('40yearMAX00.txt','w')
for i in albindex40:
    s=stations[i]
    data=s.get_data(2000,'MAX_TEMP')
    ind=s.index_record
    if data!=0:
            rdata=data[0]
            fdata=data[1]
            f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
            for i in range(365):
                if fdata[i]==15:
                    f.write('-1000'+',') #NA
                elif fdata[i]==2:
                    f.write('0.0'+',') #Trace
                elif i==59 and fdata[i]!=14:
                    f.write('-1000'+',') #MFeb
                elif i==59 and abs(round(rdata[i]))>900:
                    f.write('-1000'+',')
                else:
                    f.write(str(round(rdata[i],2))+',')   
            if fdata[365]==15:
                 f.write('-1000')
            elif fdata[365]==2:
                 f.write('0.0') #Trace
            else:
                 f.write(str(round(rdata[365],2))) 

            f.write('\n')

                
####Correlation for 40 years analysis, make two files 40MAXcor and 40PCPNcor

for i in albindex40:
    s=stations[i]
    for year in range(1960,2000):
            data=s.get_data(year,'ONE_DAY_PRECIPITATION')
            ind=s.index_record
            f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
            if data!=0:
                    rdata=data[0]
                    data=data[1]
                    days=1,32,61,92,122,153,184,215,245,275,307,337
                    for i in range(days):
                            if fdata[i]==15:
                                    f.write('-1.0'+',') #NA
                            elif fdata[i]==2:
                                    f.write('0.0'+',') #Trace
                                                              
                            else:
                                    f.write(str(round(rdata[i],2))+',')   
            

    f.write('\n')
f.close()




for i in albindex40:
    s=stations[i]
    for year in range(1960,2000):
            data=s.get_data(year,'MAX_TEMP')
            ind=s.index_record
            f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
            if data!=0:
                    rdata=data[0]
                    data=data[1]
                    days=1,32,61,92,122,153,184,215,245,275,307,337
                    for i in range(days):
                            if fdata[i]==15:
                                    f.write('-1.0'+',') #NA
                                                                                         
                            else:
                                    f.write(str(round(rdata[i],2))+',')   
            

    f.write('\n')
f.close()


###Calgary and Banff daily PCPN and Max temp
s=stations[2436]
f=open('calgary-daily-pcpn.txt','w')
for year in range(1882,2003):
        data=s.get_data(year,'ONE_DAY_PRECIPITATION')
        ind=s.index_record
        if data!=0:
            rdata=data[0]
            fdata=data[1]
            f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+','+str(year)+',')
            for i in range(365):
                if fdata[i]==15:
                    f.write('-1000'+',') #NA
                elif fdata[i]==2:
                    f.write('0.0'+',') #Trace
                elif i==59 and fdata[i]!=14:
                    f.write('-1000'+',') #MFeb
                elif i==59 and abs(round(rdata[i]))>900:
                    f.write('-1000'+',')
                else:
                    f.write(str(round(rdata[i],2))+',')   
            if fdata[365]==15:
                 f.write('-1000')
            elif fdata[365]==2:
                 f.write('0.0') #Trace
            else:
                 f.write(str(round(rdata[365],2))) 

            f.write('\n')
f.close()




s=stations[2436]
f=open('calgary-daily-max.txt','w')
for year in range(1882,2003):
        data=s.get_data(year,value[0])
        ind=s.index_record
        if data!=0:
            rdata=data[0]
            fdata=data[1]
            f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+','+str(year)+',')
            for i in range(365):
                if fdata[i]==15:
                    f.write('-1000'+',') #NA
                
                elif i==59 and fdata[i]!=14:
                    f.write('-1000'+',') #MFeb
                elif i==59 and abs(round(rdata[i]))>900:
                    f.write('-1000'+',')
                else:
                    f.write(str(round(rdata[i],2))+',')   
            if fdata[365]==15:
                 f.write('-1000')
            
            else:
                 f.write(str(round(rdata[365],2))) 

            f.write('\n')
f.close()



s=stations[2633]
f=open('banff-daily-max.txt','w')
for year in range(1882,2003):
        data=s.get_data(year,value[0])
        ind=s.index_record
        if data!=0:
            rdata=data[0]
            fdata=data[1]
            f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+','+str(year)+',')
            for i in range(365):
                if fdata[i]==15:
                    f.write('-1000'+',') #NA
                
                elif i==59 and fdata[i]!=14:
                    f.write('-1000'+',') #MFeb
                elif i==59 and abs(round(rdata[i]))>900:
                    f.write('-1000'+',')
                else:
                    f.write(str(round(rdata[i],2))+',')   
            if fdata[365]==15:
                 f.write('-1000')
            
            else:
                 f.write(str(round(rdata[365],2))) 

            f.write('\n')
f.close()




##writing the min temp for calgary and banff

s=stations[2436]
f=open('calgary-daily-min.txt','w')
for year in range(1882,2003):
        data=s.get_data(year,value[1])
        ind=s.index_record
        if data!=0:
            rdata=data[0]
            fdata=data[1]
            f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+','+str(year)+',')
            for i in range(365):
                if fdata[i]==15:
                    f.write('-1000'+',') #NA
                
                elif i==59 and fdata[i]!=14:
                    f.write('-1000'+',') #MFeb
                elif i==59 and abs(round(rdata[i]))>900:
                    f.write('-1000'+',')
                else:
                    f.write(str(round(rdata[i],2))+',')   
            if fdata[365]==15:
                 f.write('-1000')
            
            else:
                 f.write(str(round(rdata[365],2))) 

            f.write('\n')
f.close()



s=stations[2633]
f=open('banff-daily-min.txt','w')
for year in range(1882,2003):
        data=s.get_data(year,value[1])
        ind=s.index_record
        if data!=0:
            rdata=data[0]
            fdata=data[1]
            f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+','+str(year)+',')
            for i in range(365):
                if fdata[i]==15:
                    f.write('-1000'+',') #NA
                
                elif i==59 and fdata[i]!=14:
                    f.write('-1000'+',') #MFeb
                elif i==59 and abs(round(rdata[i]))>900:
                    f.write('-1000'+',')
                else:
                    f.write(str(round(rdata[i],2))+',')   
            if fdata[365]==15:
                 f.write('-1000')
            
            else:
                 f.write(str(round(rdata[365],2))) 

            f.write('\n')
f.close()





#writing the pcpn daily for banff

s=stations[2633]
f=open('banff-daily-pcpn.txt','w')
for year in range(1882,2003):
        data=s.get_data(year,'ONE_DAY_PRECIPITATION')
        ind=s.index_record
        if data!=0:
            rdata=data[0]
            fdata=data[1]
            f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+','+str(year)+',')
            for i in range(366):
                if fdata[i]==15:
                    f.write('-1000'+',') #NA
                elif fdata[i]==2:
                    f.write('0.0'+',') #Trace
                elif i==59 and fdata[i]!=14:
                    f.write('-1000'+',') #MFeb
                elif i==59 and abs(round(rdata[i]))>900:
                    f.write('-1000'+',')
                else:
                    f.write(str(round(rdata[i],2))+',')   
            if fdata[365]==15:
                 f.write('-1000')
            elif fdata[365]==2:
                 f.write('0.0') #Trace
            else:
                 f.write(str(round(rdata[365],2))) 

            f.write('\n')
f.close()                



#### dist check for the first days of each month


f=open('calgay-daily-pcpn-distcheck.txt','w')
s=stations[2436]
val=4
years=range(1880,2006)
days=1,32,61,92,122,153,184,215,245,275,307,337
for i in days:
        for year in years:
           data=s.get_data(year,value[val])
           if data!=0:
                d=data[0][i]
                fl=data[1][i]
                if fl==15:
                        f.write('NA'+',')
                elif fl==2:
                        f.write('0.0'+',')
                else:
                        f.write(str(round(d,2))+',')
        f.write('\n')               
                        
f.close()





f=open('banff-daily-pcpn-distcheck.txt','w')
s=stations[2633]
val=4
years=range(1880,2006)
days=1,32,61,92,122,153,184,215,245,275,307,337
for i in days:
        for year in years:
           data=s.get_data(year,value[val])
           if data!=0:
                d=data[0][i]
                fl=data[1][i]
                if fl==15:
                        f.write('NA'+',')
                elif fl==2:
                        f.write('0.0'+',')
                else:
                        f.write(str(round(d,2))+',')
        f.write('\n')               
                        
f.close()



f=open('calgay-daily-max-distcheck.txt','w')
s=stations[2436]
val=0
years=range(1880,2006)
days=1,32,61,92,122,153,184,215,245,275,307,337
for i in days:
        for year in years:
           data=s.get_data(year,value[val])
           if data!=0:
                d=data[0][i]
                fl=data[1][i]
                if fl==15:
                        f.write('NA'+',')
                
                else:
                        f.write(str(round(d,2))+',')
        f.write('\n')               
                        
f.close()



f=open('calgay-daily-min-distcheck.txt','w')
s=stations[2436]
val=1
years=range(1880,2006)
days=1,32,61,92,122,153,184,215,245,275,307,337
for i in days:
        for year in years:
           data=s.get_data(year,value[val])
           if data!=0:
                d=data[0][i]
                fl=data[1][i]
                if fl==15:
                        f.write('NA'+',')
                
                else:
                        f.write(str(round(d,2))+',')
        f.write('\n')               
                        
f.close()





f=open('banff-daily-max-distcheck.txt','w')
s=stations[2633]
val=0
years=range(1880,2006)
days=1,32,61,92,122,153,184,215,245,275,307,337
for i in days:
        for year in years:
           data=s.get_data(year,value[val])
           if data!=0:
                d=data[0][i]
                fl=data[1][i]
                if fl==15:
                        f.write('NA'+',')
                
                else:
                        f.write(str(round(d,2))+',')
        f.write('\n')               
                        
f.close()


f=open('banff-daily-min-distcheck.txt','w')
s=stations[2366]
val=1
years=range(1880,2006)
days=1,32,61,92,122,153,184,215,245,275,307,337
for i in days:
        for year in years:
           data=s.get_data(year,value[val])
           if data!=0:
                d=data[0][i]
                fl=data[1][i]
                if fl==15 or fl==14:
                        f.write('NA'+',')
                
                else:
                        f.write(str(round(d,2))+',')
        f.write('\n')               
                        
f.close()

### We are going to check the bimodality which we have observed in PCPN in
#Banff for min temp.
f=open('banff-daily-min-distcheck-bimodal.txt','w')
s=stations[2366]
val=1
years=range(1880,2006)
days=2,3,4,5,33,34,35,36
for i in days:
        for year in years:
           data=s.get_data(year,value[val])
           if data!=0:
                d=data[0][i]
                fl=data[1][i]
                if fl==15 or fl==14:
                        f.write('NA'+',')
                
                else:
                        f.write(str(round(d,2))+',')
        f.write('\n')               
                        
f.close()










####Going back to the correlation structure. for the 40year list
####We look at the correlation for different days of the year
####The first day of each month.

years=range(1880,2003);days=1,32,61,92,122,153,184,215,245,275,307,337;val=4
files='jan1-pcpn-cor.txt','feb1-pcpn-cor.txt','mar1-pcpn-cor.txt','apr1-pcpn-cor.txt','may1-pcpn-cor.txt','jun1-pcpn-cor.txt','jul1-pcpn-cor.txt','aug1-pcpn-cor.txt','sep1-pcpn-cor.txt','oct1-pcpn-cor.txt','nov1-pcpn-cor.txt','dec1-pcpn-cor.txt'

for i in range(12):
        f=open(files[i],'w')
        day=days[i]
        for j in albindex40:
                s=stations[j]
                ind=s.index_record
                f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                for year in years:
                        data=s.get_data(year,value[val])
                        if data!=0:
                                d=data[0][day]
                                fl=data[1][day]
                                if fl==15 or fl==14:
                                        f.write('-1000'+',')
                                elif fl==2:
                                        f.write('0.0'+',')
                                else:
                                        f.write(str(round(d,2))+',')
                        else:
                                f.write('-1000'+',')
                f.write('-1000')
                f.write('\n')
        f.close()     
                

####Doing the same thing for MAX temp.

years=range(1880,2003);days=1,32,61,92,122,153,184,215,245,275,307,337;val=0
files='jan1-max-cor.txt','feb1-max-cor.txt','mar1-max-cor.txt','apr1-max-cor.txt','may1-max-cor.txt','jun1-max-cor.txt','jul1-max-cor.txt','aug1-max-cor.txt','sep1-max-cor.txt','oct1-max-cor.txt','nov1-max-cor.txt','dec1-max-cor.txt'

for i in range(12):
        f=open(files[i],'w')
        day=days[i]
        for j in albindex40:
                ind=s.index_record                
                s=stations[j]
                f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                for year in years:
                        data=s.get_data(year,value[val])
                        if data!=0:
                                d=data[0][day]
                                fl=data[1][day]
                                if fl==15 or fl==14:
                                        f.write('-1000'+',')
                                else:
                                        f.write(str(round(d,2))+',')
                        else:
                                f.write('-1000'+',')
                f.write('-1000')
                f.write('\n')
        f.close()


####Downloading the daily PCPN and max temp for all years for Calgary and Banff
####To make histograms for jan 1st to dec 1st.
f=open('calgay-daily-pcpn-boxplot.txt','w');s=stations[2436];val=4;years=range(1880,2006)
days=1,32,61,92,122,153,184,215,245,275,307,337
dates='01/01','01/02','01/03','01/04','01/05','01/06','01/07','01/08','01/09','01/10','01/11','01/12'
f.write('Year'+','+'Date'+','+'Value'+'\n')
for i in range(12):
        for year in years:
           f.write(str(year)+','+dates[i]+',')
           data=s.get_data(year,value[val])
           if data!=0:
                d=data[0][days[i]]
                fl=data[1][days[i]]
                if fl==15 or fl==14:
                        f.write('NA')
                elif fl==2:
                        f.write('0.0')
                else:
                        f.write(str(round(d,2)))
                       
           else:
                f.write('NA')
           f.write('\n')     
f.close()


f=open('banff-daily-pcpn-boxplot.txt','w');s=stations[2633];val=4;years=range(1880,2006)
days=1,32,61,92,122,153,184,215,245,275,307,337
dates='01/01','01/02','01/03','01/04','01/05','01/06','01/07','01/08','01/09','01/10','01/11','01/12'
f.write('Year'+','+'Date'+','+'Value'+'\n')
for i in range(12):
        for year in years:
           f.write(str(year)+','+dates[i]+',')
           data=s.get_data(year,value[val])
           if data!=0:
                d=data[0][days[i]]
                fl=data[1][days[i]]
                if fl==15 or fl==14:
                        f.write('NA')
                elif fl==2:
                        f.write('0.0')
                else:
                        f.write(str(round(d,2)))
                       
           else:
                f.write('NA')
           f.write('\n')     
f.close()

                        
###Same for max temp:

f=open('calgary-daily-max-boxplot.txt','w');s=stations[2436];val=0;years=range(1880,2006)
days=1,32,61,92,122,153,184,215,245,275,307,337
dates='01/01','01/02','01/03','01/04','01/05','01/06','01/07','01/08','01/09','01/10','01/11','01/12'
f.write('Year'+','+'Date'+','+'Value'+'\n')
for i in range(12):
        for year in years:
           f.write(str(year)+','+dates[i]+',')
           data=s.get_data(year,value[val])
           if data!=0:
                d=data[0][days[i]]
                fl=data[1][days[i]]
                if fl==15 or fl==14:
                        f.write('NA')
                else:
                        f.write(str(round(d,2)))
                       
           else:
                f.write('NA')
           f.write('\n')     
f.close()


f=open('banff-daily-max-boxplot.txt','w');s=stations[2633];val=0;years=range(1880,2006)
days=1,32,61,92,122,153,184,215,245,275,307,337
dates='01/01','01/02','01/03','01/04','01/05','01/06','01/07','01/08','01/09','01/10','01/11','01/12'
f.write('Year'+','+'Date'+','+'Value'+'\n')
for i in range(12):
        for year in years:
           f.write(str(year)+','+dates[i]+',')
           data=s.get_data(year,value[val])
           if data!=0:
                d=data[0][days[i]]
                fl=data[1][days[i]]
                if fl==15 or fl==14:
                        f.write('NA')
                else:
                        f.write(str(round(d,2)))
                       
           else:
                f.write('NA')
           f.write('\n')     
f.close()        
            



####Now we create a file that has all the daily data for all years for Calgary
##This is useful for extreme analysis.
f=open('calgay-daily-pcpn-all.txt','w')
s=stations[2436]
val=4
years=range(1880,2006)
days=range(0,366)
for year in years:
        for i in days:
           data=s.get_data(year,value[val])
           if data!=0:
                d=data[0][i]
                fl=data[1][i]
                if fl==15:
                        f.write('NA'+',')
                elif fl==14:
                        f.write('NA'+',')
                elif fl==2:
                        f.write('0.0'+',')
                else:
                        f.write(str(round(d,2))+',')
        f.write('\n')               
                        
f.close()



f=open('calgay-daily-maxtemp-all.txt','w')
s=stations[2436]
val=0
years=range(1880,2006)
days=range(0,366)
for year in years:
        for i in days:
           data=s.get_data(year,value[val])
           if data!=0:
                d=data[0][i]
                fl=data[1][i]
                if fl==15:
                        f.write('NA'+',')
                elif fl==14:
                        f.write('NA'+',')
                
                else:
                        f.write(str(round(d,2))+',')
        f.write('\n')               
                        
f.close()


###Writing the PCPN for 40-year stations. 
f=open('PCPN-40-all-locations.txt','w')
val=4
years=range(1961,2000)
for i in albindex40:
        s=stations[i]
        for year in years:
                
                data=s.get_data(year,value[val])
                if data!=0:
                        f.write(str(i)+','+str(year)+',')
                        for j in range(366):
                                d=data[0][j]
                                fl=data[1][j]
                                if fl==15:
                                        f.write('NA'+',')
                                elif fl==14:
                                        f.write('NA'+',')
                                elif fl==2:
                                        f.write('0.0'+',')
                                else:
                                        f.write(str(round(d,2))+',')
                f.write('\n')

     
f.close()

        
##same for max-temp

f=open('max-temp-40-all-locations.txt','w')
val=0
years=range(1961,2000)
for i in albindex40:
        s=stations[i]
        for year in years:
                
                data=s.get_data(year,value[val])
                if data!=0:
                        f.write(str(i)+','+str(year)+',')
                        for j in range(366):
                                d=data[0][j]
                                fl=data[1][j]
                                if fl==15:
                                        f.write('NA'+',')
                                elif fl==14:
                                        f.write('NA'+',')
                                
                                else:
                                        f.write(str(round(d,2))+',')
                f.write('\n')

     
f.close()

##writing joined for PCPN
f=open('PCPN-40-all-locations-joined.txt','w')
val=4
years=range(1961,2000)
for i in albindex40:
        s=stations[i]
        ind=s.index_record
        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
        for year in years:
                
                data=s.get_data(year,value[val])
                
                if data!=0:
                        
                        for j in range(366):
                                d=data[0][j]
                                fl=data[1][j]
                                if fl==15:
                                        f.write('NA'+',')
                                elif fl==14:
                                        f.write('NA'+',')
                                elif fl==2:
                                        f.write('0.0'+',')
                                else:
                                        f.write(str(round(d,2))+',')
                                        
                if data==0:
                        for i in range(366):
                                f.write('NA'+',')
        f.write('\n')                        

     
f.close()



##joined for max temp

f=open('max-temp-40-all-locations-joined.txt','w')
val=0
years=range(1961,2000)
for i in albindex40:
        s=stations[i]
        ind=s.index_record
        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
        for year in years:
                
                data=s.get_data(year,value[val])
                
                if data!=0:
                        
                        for j in range(366):
                                d=data[0][j]
                                fl=data[1][j]
                                if fl==15:
                                        f.write('NA'+',')
                                elif fl==14:
                                        f.write('NA'+',')
                                
                                else:
                                        f.write(str(round(d,2))+',')
                                        
                if data==0:
                        for i in range(366):
                                f.write('NA'+',')
        f.write('\n')                        

     
f.close()



###Writing the PCPN and Max temp for Nhu, we write these for the stations having data from 1960-2000.

f=open('coords-1960-2000.txt','w')
for i in range(numalb40):
        j=albindex40[i]
        s=stations[j]
        ind=s.index_record
        f.write(str(i+1)+','+ind[1]+','+str(ind[3])+','+str(ind[4])+','+str(ind[5]))
        f.write('\n')


f=open('PCPN-1960-2000.txt','w')
years=range(1880,2004)
for i in range(numalb40):
        j=albindex40[i]
        s=stations[j]
        ind=s.index_record
        val=4
        for year in years:
                data=s.get_data(year,value[val])
                if data!=0:
                        f.write(str(i+1)+','+str(year)+',')
                        for k in range(366):
                                d=data[0][k]
                                fl=data[1][k]
                                if fl==15:
                                        f.write('NA'+',')
                                elif fl==14:
                                        f.write('F'+',')
                                elif fl==2:
                                        f.write('T'+',')
                                else:
                                        f.write(str(round(d,2))+',')
                                        
                        f.write('\n')



f=open('Max-temp-1960-2000.txt','w')
years=range(1880,2004)
for i in range(numalb40):
        j=albindex40[i]
        s=stations[j]
        ind=s.index_record
        val=0
        for year in years:
                data=s.get_data(year,value[val])
                if data!=0:
                        f.write(str(i+1)+','+str(year)+',')
                        for k in range(366):
                                d=data[0][k]
                                fl=data[1][k]
                                if fl==15:
                                        f.write('NA'+',')
                                elif fl==14:
                                        f.write('F'+',')
                                else:
                                        f.write(str(round(d,2))+',')
                                        
                        f.write('\n')                        
                        

f=open('min-temp-1960-2000.txt','w')
years=range(1880,2004)
for i in range(numalb40):
        j=albindex40[i]
        s=stations[j]
        ind=s.index_record
        val=1
        for year in years:
                data=s.get_data(year,value[val])
                if data!=0:
                        f.write(str(i+1)+','+str(year)+',')
                        for k in range(366):
                                d=data[0][k]
                                fl=data[1][k]
                                if fl==15:
                                        f.write('NA'+',')
                                elif fl==14:
                                        f.write('F'+',')
                                else:
                                        f.write(str(round(d,2))+',')
                                        
                        f.write('\n')             



###Separability
#We pick stations with more than 100 years data.
f=open('PCPN-2436.txt','w');val=4;years=range(1880,2004);s=stations[2436];ind=s.index_record
for year in years:
                data=s.get_data(year,value[val])
                if data!=0:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                d=data[0][k]
                                fl=data[1][k]
                                if fl==15:
                                        f.write('-1000'+',')
                                elif fl==14:
                                        f.write('-1000'+',')
                                elif fl==2:
                                        f.write('0.0'+',')
                                else:
                                        f.write(str(round(d,2))+',')
                else:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                f.write('-1000'+',')
                                
                f.write('-1000')        
                        
                f.write('\n') 


                
                
f=open('PCPN-2483.txt','w');val=4;years=range(1880,2004);s=stations[2436];ind=s.index_record
for year in years:
                data=s.get_data(year,value[val])
                if data!=0:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                d=data[0][k]
                                fl=data[1][k]
                                if fl==15:
                                        f.write('-1000'+',')
                                elif fl==14:
                                        f.write('-1000'+',')
                                elif fl==2:
                                        f.write('0.0'+',')
                                else:
                                        f.write(str(round(d,2))+',')
                else:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                f.write('-1000'+',')
                                
                f.write('-1000')        
                        
                f.write('\n') 
        
        
        

##2436, 2483, 2488, 2497, 2516, 2633



f=open('PCPN-2488.txt','w');val=4;years=range(1880,2004);s=stations[2436];ind=s.index_record
for year in years:
                data=s.get_data(year,value[val])
                if data!=0:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                d=data[0][k]
                                fl=data[1][k]
                                if fl==15:
                                        f.write('-1000'+',')
                                elif fl==14:
                                        f.write('-1000'+',')
                                elif fl==2:
                                        f.write('0.0'+',')
                                else:
                                        f.write(str(round(d,2))+',')
                else:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                f.write('-1000'+',')
                                
                f.write('-1000')        
                        
                f.write('\n') 


f=open('PCPN-2516.txt','w');val=4;years=range(1880,2004);s=stations[2436];ind=s.index_record
for year in years:
                data=s.get_data(year,value[val])
                if data!=0:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                d=data[0][k]
                                fl=data[1][k]
                                if fl==15:
                                        f.write('-1000'+',')
                                elif fl==14:
                                        f.write('-1000'+',')
                                elif fl==2:
                                        f.write('0.0'+',')
                                else:
                                        f.write(str(round(d,2))+',')
                else:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                f.write('-1000'+',')
                                
                f.write('-1000')        
                        
                f.write('\n') 




f=open('PCPN-2633.txt','w');val=4;years=range(1880,2004);s=stations[2436];ind=s.index_record
for year in years:
                data=s.get_data(year,value[val])
                if data!=0:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                d=data[0][k]
                                fl=data[1][k]
                                if fl==15:
                                        f.write('-1000'+',')
                                elif fl==14:
                                        f.write('-1000'+',')
                                elif fl==2:
                                        f.write('0.0'+',')
                                else:
                                        f.write(str(round(d,2))+',')
                else:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                f.write('-1000'+',')
                                
                f.write('-1000')        
                        
                f.write('\n') 



f=open('PCPN-2497.txt','w');val=4;years=range(1880,2004);s=stations[2436];ind=s.index_record
for year in years:
                data=s.get_data(year,value[val])
                if data!=0:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                d=data[0][k]
                                fl=data[1][k]
                                if fl==15:
                                        f.write('-1000'+',')
                                elif fl==14:
                                        f.write('-1000'+',')
                                elif fl==2:
                                        f.write('0.0'+',')
                                else:
                                        f.write(str(round(d,2))+',')
                else:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                f.write('-1000'+',')
                                
                f.write('-1000')        
                        
                f.write('\n') 







f=open('maxt2436.txt','w');val=0;years=range(1880,2004);s=stations[2436];ind=s.index_record
for year in years:
                data=s.get_data(year,value[val])
                if data!=0:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                d=data[0][k]
                                fl=data[1][k]
                                if fl==15:
                                        f.write('-1000'+',')
                                elif fl==14:
                                        f.write('-1000'+',')
                                
                                        
                                else:
                                        f.write(str(round(d,2))+',')
                else:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                f.write('-1000'+',')
                                
                f.write('-1000')        
                        
                f.write('\n') 


f=open('maxt2483.txt','w');val=0;years=range(1880,2004);s=stations[2483];ind=s.index_record
for year in years:
                data=s.get_data(year,value[val])
                if data!=0:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                d=data[0][k]
                                fl=data[1][k]
                                if fl==15:
                                        f.write('-1000'+',')
                                elif fl==14:
                                        f.write('-1000'+',')
                                
                                        
                                else:
                                        f.write(str(round(d,2))+',')
                else:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                f.write('-1000'+',')
                                
                f.write('-1000')        
                        
                f.write('\n')


f=open('maxt2488.txt','w');val=0;years=range(1880,2004);s=stations[2488];ind=s.index_record
for year in years:
                data=s.get_data(year,value[val])
                if data!=0:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                d=data[0][k]
                                fl=data[1][k]
                                if fl==15:
                                        f.write('-1000'+',')
                                elif fl==14:
                                        f.write('-1000'+',')
                                
                                        
                                else:
                                        f.write(str(round(d,2))+',')
                else:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                f.write('-1000'+',')
                                
                f.write('-1000')        
                        
                f.write('\n')

f=open('maxt2497.txt','w');val=0;years=range(1880,2004);s=stations[2497];ind=s.index_record
for year in years:
                data=s.get_data(year,value[val])
                if data!=0:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                d=data[0][k]
                                fl=data[1][k]
                                if fl==15:
                                        f.write('-1000'+',')
                                elif fl==14:
                                        f.write('-1000'+',')
                                
                                        
                                else:
                                        f.write(str(round(d,2))+',')
                else:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                f.write('-1000'+',')
                                
                f.write('-1000')        
                        
                f.write('\n')

f=open('maxt2516.txt','w');val=0;years=range(1880,2004);s=stations[2516];ind=s.index_record
for year in years:
                data=s.get_data(year,value[val])
                if data!=0:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                d=data[0][k]
                                fl=data[1][k]
                                if fl==15:
                                        f.write('-1000'+',')
                                elif fl==14:
                                        f.write('-1000'+',')
                                
                                        
                                else:
                                        f.write(str(round(d,2))+',')
                else:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                f.write('-1000'+',')
                                
                f.write('-1000')        
                        
                f.write('\n')


f=open('maxt2633.txt','w');val=0;years=range(1880,2004);s=stations[2633];ind=s.index_record
for year in years:
                data=s.get_data(year,value[val])
                if data!=0:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                d=data[0][k]
                                fl=data[1][k]
                                if fl==15:
                                        f.write('-1000'+',')
                                elif fl==14:
                                        f.write('-1000'+',')
                                
                                        
                                else:
                                        f.write(str(round(d,2))+',')
                else:
                        f.write(str(ind[3])+','+str(ind[4])+','+str(ind[5])+',')
                        f.write(str(year)+',')
                        for k in range(366):
                                f.write('-1000'+',')
                                
                f.write('-1000')        
                        
                f.write('\n')                 
       
        


