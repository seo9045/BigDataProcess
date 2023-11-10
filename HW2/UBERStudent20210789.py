import sys
from datetime import datetime

def count_trip(input_f, output_f):
    
    trip = {}

    with open(input_f, 'r') as f:
        lines = f.readlines()

    for line in lines:
        data = line.strip().split(',')
        location = data[0]
        date_str = data[1]
        car_count = int(data[2])
        trip_count = int(data[3])

        date = datetime.strptime(date_str, '%m/%d/%Y')
        day_name = date.strftime('%a').upper()

        if (location, day_name) in trip:
            trip[(location, day_name)]['car_count'] += car_count
            trip[(location, day_name)]['trip_count'] += trip_count
        else:
            trip[(location, day_name)] = {'car_count': car_count, 'trip_count': trip_count}

    sorted_result = sorted(trip.items(), key=lambda x: (x[0][0], ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'].index(x[0][1])))

    with open(output_f, 'w') as f:
        for (location, day_name), data in sorted_result:
            car_count = data['car_count']
            trip_count = data['trip_count']
            f.write(f"{location}, {day_name}, {car_count}, {trip_count}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Rewrite")
    else:
        input_f = sys.argv[1]
        output_f = sys.argv[2]
        count_trip(input_f, output_f)
