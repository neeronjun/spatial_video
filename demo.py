import csv
from geopy.distance import great_circle
from datetime import datetime
newport_ri = (41.49008, -71.312796)
desti = (0, 0)
startpt = (0, 0)
cleveland_oh = (41.499498, -81.695391)
#print(great_circle(newport_ri, cleveland_oh).miles)
with open('akron1.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    trip_count = 0
    trip_id = 0
    interval = [0]
    totaldist = great_circle(0,0)
    i=0
    for row in csv_reader:
        #trip_id = row[0]
        #lati = row[1]
        #longi = row[2]
        if line_count == 0:
            line_count +=1
        else:
            #print(f'\t{row[0]} works in the {row[1]} department, was born in {row[2]}.')
            if trip_id != row[0]:
                trip_id = row[0]
                i += 1
                #if desti[1]!=0 and desti[0] != 0:
                 #   print(f'trip length ={great_circle(startpt, desti)}, time ={row[3]}')
                  #  print(f'time: {endtime - starttime}')
                startpt = (row[1],row[2])
                date_string = row[3]
                starttime = datetime.strptime(row[3], '%m/%d/%Y %H:%M')
                #print(startpt)
                trip_count = trip_count + 1
            else:
                desti = (row[1],row[2])
                endtime = datetime.strptime(row[3], '%m/%d/%Y %H:%M')
                #print(f'time: {starttime - endtime}')
                distance = great_circle(startpt, desti)
                totaldist = totaldist + distance
                if distance > 1:
                    duration = (endtime - starttime).seconds #+ (endtime - starttime).m * 60
                    interval.append(duration)
                    #interval.append(duration)
                    #print(great_circle(startpt, desti).miles)
                    #print(starttime)
                    print(endtime)
                    starttime = endtime
                    startpt = desti
                    desti = 0
                    distance = 0
                    #i += 1
                    #interval.append(6)
                line_count += 1
        
    print(f'processed {line_count} lines.')
    print(f'trip count = {trip_count}')
    for x in interval:
        print(x)
    s = (41.07974, -81.518152)
    t = (41.09623, -81.51242)
    print(f'{great_circle({41.0939685, -81.5126645},{41.102838, -81.5151155})}')
    print(totaldist)
41.102149,-81.51612

    #41.07974, -81.518152
    #41.09623, -81.51242