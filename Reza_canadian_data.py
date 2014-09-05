
'''Canadian data extraction module
    Copyright (C) 2007  Reza Hosseini, reza2357@yahoo.ca
    This is a modification of
    Toolbox for Data structures on Canadian climate data CDs.
    1999 Bernhard Reiter 
    

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


import sys
import os.path	# portable path manipulations
import struct
import array	
Index_File_header_fmt= ( "<" + # indicates little-endian data
	"4s" + 		# ID
	"HH" +		# MaxLat, MinLat
	"HH" +		# MaxLong, MinLong
	"hh" +		# MaxElev, MinElev
	"HH" +		# EarliestYear, LatestYear
	"H"  +		# Number of Stations in the district
	"3s" +		# District ID
	"42s"		# District Name
	)

Index_File_data_fmt=  ( "<" + # indicates little endian data
	"4s" +		# CSN, the last four characters of the 7-char statHon ID
	"24s" +		# StationName
	"3s" +		# Airport
	"HH" +		# Lat, Long
	"h"  +		# Elevation
	"7H" +		# First Year
	"7H" +		# Last Year
	"H"		# [20] Starting Record Number
	)


Data_File_header_fmt= ( "<" +
	"4s" +		# Data file version id (should be "WWWW")
	"7s" +		# CSN = station ID number
	"24s" +		# Station Name
	"3s" +		# Airport
	"HH" +		# Lat, Long
	"H"  +		# Elevation
	"HH" +		# First Year, Last Year    for station
	"300H" +	# Record Num for each year's 1st element starting w 1801
	"300B" +	# Available indicator, left to right 6 bit of each byte
	"123x" )	# 

Data_File_data_fmt= (  "<" + 
	"732s" +	# contains array of short ints: one day's value
	"183s" +	# contains array of nybbles: one day's flag
	"156s" )	# contains 12 month summaries a 13 bytes

Record_size=struct.calcsize(Data_File_data_fmt)
if Record_size != struct.calcsize(Data_File_header_fmt) or Record_size != 1071:
    sys.stderr("Something wrong with the internal record structure formats!\n")
    sys.exit(5)
    

Maximum_Temperature_fmt = (  "<" + 
        "12h"  +	#  Mean Max for Month 
        "12B"  +	#  # Days Missing 
        "12B"  +	#  # Days with Max above 0  
        "12h"  +	#  Maximum Max for Month 
        "12B"  +	#  Date of Maximum Max 
        "12h"  +	#  Minimum Max for Month 
        "12B"  +	#  Date of Minimum Max 
        "12B"  +	#  Max # Days in a Row with Missing Data 
        "12B"  +	#  # Days with Misg Mean Temperature 
        "12B"  )	#  Maximum # Days in a row with Misg Mean Temperature 

Minimum_Temperature_fmt = ( "<" +
        "12h"  +	# Mean Minimum for Month 
        "12B"  +	# # Days Missing 
        "12B"  +	# # Days with Min above 0  
        "12h"  +	# Maximum Min for Month 
        "12B"  +	# Date of Maximum Min 
        "12h"  +	# Minimum Min for Month 
        "12B"  +	# Date of Minimum Min 
        "12B"  +	# Max # Days in a Row with Missing Data 
        "12h"  )	# Mean Temperature 

Precipitation_fmt = ( "<" + 
        "12H"  +	# Total for Month 
        "12B"  +	# # Days Missing 
        "12B"  +	# # Days with > 0 cm/mm 
        "12H"  +	# Max one-day total for Month 
        "12B"  +	# Date of Max 
        "12B"  +	# # Days with > Trace 
        "12B"  +	# # Days with > 1 cm 
        "12B"  +	# # Days with Uncrtn/accum pcpn 
        "12B"  +	# Maximum # Days in a row with Uncrtn/accum Pcpn 
        "24x" )

Snow_on_the_Ground_fmt = ( "<" + 
        "12H"  +	# Median for Month 
        "12B"  +	# # Days Missing 
        "12B"  +	# Days with >0 cm 
        "12H"  +	# Max for Month 
        "12B"  +	# Date of Max 
        "12H"  +	# Min for Month 
        "12B"  +	# Date of Min 
        "12B"  +	# Days with > Trace 
        "12B"  +	# Days with > 1 cm 
        "12x" )

################################################################################
#
#

def read_all_records(file,fmt):
    """Return list containing all records read from the monotoniously build file.
    
    	Parameter:
    		file	an open file object (seeked to the right place)
    		fmt 	a struct module format string
    	
    	This routine will read till end of the file and 
    	give a message if the last read count was not 0.
    """
    list=[]
    size=struct.calcsize(fmt)

    while 1:
        s=file.read(size)
	if len(s) == size:
		list.append(struct.unpack(fmt,s))
		continue

	if len(s)!=0:
		sys.stderr.write("Only got %d bytes on last read!" % len(s))
	return list



def build_file_index(topdirectory):
    """ Returns list of (index filename, data filename, district) tuples.
    
    Reads the "index.all" file in the topdirectory and calculates all other
    index filenames.
    """
    file=open(os.path.join(topdirectory,"index.all"),"rb")
    list=read_all_records(file,Index_File_header_fmt)
    file.close()

    # Okay, using a lambda construct and map is a bit complicated, but elegant
    def create_index_name(topdir):
    	return lambda x,td=topdir: \
	    ( os.path.join(td,x[10][0],"Index."+x[10]),
	    os.path.join(td,x[10][0],"Data."+x[10]),
	    x[10])

    return map(create_index_name(topdirectory),list)


################################################################################
#
class weather_station:
    

    avail= { 
    "MAX_TEMP":(1,10.0,Maximum_Temperature_fmt),
    "MIN_TEMP":(1<<1,10.0,Minimum_Temperature_fmt),
    "ONE_DAY_RAIN":(1<<2,10.0,Precipitation_fmt),
    "ONE_DAY_SNOW":(1<<3,10.0,Precipitation_fmt),
    "ONE_DAY_PRECIPITATION":(1<<4,10.0,Precipitation_fmt),
    "SNOW_ON_THE_GROUND":(1<<5,10.0,Snow_on_the_Ground_fmt)
    }
# flags explanation out of cdcd.doc, values out of format description
#  0   (no flag)
#  7-13 unused
# 14   29th of February in non leap years
#  5 A Amount accumulated over more than one day; Previous value's flag was
#    C or L
#  3 C Precipitation occurred; amount is uncertain; recorded value is 0;
#      value displayed is the word "Yes"
#  1 E Estimated
#  6 F Amount accumulated over more than one day and estimated
#  4 L Precipitation may or may not have occurred; amount is unknown;
#      recorded value is 0; value displayed is the word "Maybe"
# 15 M Missing
#  2 T A trace occurred; recorded value is zero


    
    def __init__(self,filetuple,index_record):
        """Initialise instance variables."""
	self.index_record=index_record
	self.indexfilename=filetuple[0]
	self.datafilename=filetuple[1]
	self.district=filetuple[2]
	self.startrecord=self.index_record[20]
	self.stationnumber=self.district+self.index_record[0]
	self.datafileopen=0
	self.dataindex=[]

    def activate(self):
        """Make sure the datafile is open and we have the dataindex."""
    	if not self.datafileopen:
		self.datafile=open(self.datafilename,"rb")
		self.datafileopen=1
	if not self.dataindex:
		self.datafile.seek((self.startrecord-1)*Record_size)
		string=self.datafile.read(Record_size)
		self.dataindex=struct.unpack(Data_File_header_fmt,string)


    def deactivate(self):
        """Close the datafile if necessary."""
    	if self.datafileopen:
		self.datafile.close()
		self.datafileopen=0

    def AvailFor(self,year):
        """Return tuple with recordindex and availabilty flags or null."""
	self.activate()

    	recnumb_index=year-1801+9
	dataavail_index=year-1801+309

	firstrec= self.dataindex[recnumb_index]
	if firstrec:
		return(firstrec, self.dataindex[dataavail_index])
	else:
		return 0


    def get_data(self,year,what):
        """Returns list w [values,flags,summaries] for wanted year and item.

	All non-missing values have been turned into normal representation.
	The missing values are undefined.
	"""
	
    	tuple=self.AvailFor(year)
	if (not tuple) or (not self.avail[what][0] & tuple[1]):
		return 0

	# seek to the right datablock
	j=0
	while not self.avail[what][0] & (1<<j) and j<=5:
                j=j+1
                
        i=0
        for l in range(j):
            if (1<<l) & tuple[1]:
                i=i+1
                
       	self.datafile.seek((self.startrecord+tuple[0]+i-1)*Record_size)

	# get datablock, unpack it
	string=self.datafile.read(Record_size)
	r=struct.unpack(Data_File_data_fmt,string)

	raw_values=array.array("h")
	raw_values.fromstring(r[0])
	flags=array.array("B")
	for i in range(183):
		flags.append(ord(r[1][i])>>4&15)
		flags.append(ord(r[1][i])&15)

	# sanity check:
	if len(raw_values)!=len(flags):
		sys.stderr.write("Arg! Something is very wrong! :-( \n")
		sys.exit(10)

	# transform values into normal representation
	def trans_into_value(denominator):
		return lambda v, d=denominator: v/d

	values=array.array("f")
	values.fromlist(map(trans_into_value(self.avail[what][1]),raw_values))

	# unpack summaries
	summaries=struct.unpack(self.avail[what][2],r[2])

	return [values,flags,summaries]


    
#
# END of class 
################################################################################


def decode_avail_flags(avail_flags):
    """ Returns unordered list of text representations of avail flags. 
    
    Needs the avail_flags integer value as argument.
    """
    items=[]
    for repr in weather_station.avail.keys():
        if weather_station.avail[repr][0] & avail_flags:
            items.append(repr)
    return items


def get_station_list(topdirectory):
    """ Return list of weather_station objects."""

    files=build_file_index(topdirectory)
    wlist=[]
    
    for filetuple in files:
	# read index file
        file=open(filetuple[0],"rb")
	string=file.read(struct.calcsize(Index_File_header_fmt))
	Index_File_header=struct.unpack(Index_File_header_fmt,string)

	Index_File_data_list=read_all_records(file,Index_File_data_fmt)
	if len(Index_File_data_list) != Index_File_header[9]:
		sys.stderr.write("Found %d out of %d!\n" % 
			(len(Index_File_data_list), Index_File_header[9]) )
        file.close()

	for record in Index_File_data_list:
            wlist.append(weather_station(filetuple,record))

    return wlist

