import sys

code_path = "/Users/rz13/Dropbox/main/codes/python/extract-canadian-climate-data/"
fn = code_path + "extract.py"
exec(
    open(fn).read(),
    globals())

data_path = "/Users/rz13/Documents/data/cd2002east/"
stations = get_station_list(data_path)
len(stations)

# lets look at one station info
s = stations[0]
s.index_record


## writing a stations data to disk 
fn = "/Users/rz13/Documents/test.csv"
f = open(fn, "w")
s = stations[0]
write_years(f=f, s=s, val=1, years=range(1800, 2018))
f.close()

# write a file with info about stations
fn = "/Users/rz13/Documents/test_stations_info.csv"
f = open(fn, "w")
write_stations_info(f=f, stn_ids=range(10), val=1, year=1950, month=1)
f.close()

