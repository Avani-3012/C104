import csv
from collections import Counter
with open("SOCR-HeightWeight.csv") as r:
    reader = csv.reader(r)
    data = list(reader)

data.pop(0)
newData = []
for i in range(len(data)):
    num = data[i][1]
    newData.append(float(num))

#Mean
m= len(newData)
total = 0
for x in newData:
    total = total+x

mean = total/m
print(mean)

#Median
newData.sort()
if m%2 == 0:
    median1 = float(newData[m//2])
    median2 = float(newData[m//2 -1])
    median  =(median1 + median2)/2
else :
    median = float(newData[m//2])

print(median)

#Mode
data = Counter(newData)

mode_data_for_range = {
     "75-85": 0,"85-95":0,"95-105": 0, "105-115": 0,"115-125": 0,"125-135": 0,"135-145": 0, "145-155": 0,"155-165": 0, "165-175": 0
 }
for weight, occurence in data.items():
    if 75 < float(weight) < 85:
           mode_data_for_range["75-85"] += occurence
    elif 85 <  float(weight) < 95:
            mode_data_for_range["85-95"] += occurence
    elif 95 <  float(weight) < 105:
          mode_data_for_range["95-105"] += occurence
    elif 105 < float(weight) < 115:
          mode_data_for_range["105-115"] += occurence
    elif 115 <  float(weight) < 125:
          mode_data_for_range["115-125"] += occurence
    elif 125 <  float(weight)< 135:
            mode_data_for_range["125-135"] += occurence
    elif 135 <  float(weight) < 145:
         mode_data_for_range["135-145"] += occurence
    elif 145 <  float(weight) < 155:
            mode_data_for_range["145-155"] += occurence
    elif 155 <  float(weight)< 165:
         mode_data_for_range["155-165"] += occurence
    elif 165 <  float(weight) < 175:
         mode_data_for_range["165-175"] += occurence
   
modeRange,modeOccurence = 0,0

for range, occurence in mode_data_for_range:
    if occurence>modeOccurence:
        modeRange,modeOccurence = [int(range.split('-')[0]),int(range.split('-')[1])],occurence
    
mode = float((modeRange[0]+modeRange[1])/2)
print(mode)