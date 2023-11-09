from datetime tmport datetime

def count_trip(input_f, output_f):
    week = {
        "Mon": "월",
        "Tue": "화",
        "Wed": "수",
        "Thu": "목",
        "Fri": "금",
        "Sat": "토",
        "Sun": "일"
    }

    trip = {}

    with open(input_f, 'r') as f:
        lines = f.readlines()

    for line in lines:
        data = line.strip().split(',')
        location = data[0]
        date_str = data[1]
        car = int(data[2])

        date = datetime.strptime(date_str, "%m/%d/%Y")
        day_name = date.strftime("%a")

        if day_name in week: 
            day_week = week[day_name] 

            if (location, day_name) in trip:
                trip[(location, day_week)]['trips'] += 1
                trip[(location, day_week)]['car'] += car
            else:
                trips_by_weekday[(location, day_week)] = {'trips': 1, 'car': car}

    with open(output_f, 'w') as f:
        for key, value in trip.items():
            location, day = key
            trips = value['trips']
            cars = value['car']
            f.write(f"{location},{day} {cars},{trips}\n")

input_f = "uber_exp.txt"
output_f = "output.txt"

count_trip(input_f, output_f)
