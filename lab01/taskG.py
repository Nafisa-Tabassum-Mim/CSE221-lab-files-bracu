from datetime import datetime

def sort_trains(n, schedules):
    train_data = []
    index = 0
    while index < n:
        schedule = schedules[index]
        parts = schedule.split(' will departure for ')
        train_name = parts[0]
        destination, time_str = parts[1].rsplit(' at ', 1)
        departure_time = datetime.strptime(time_str, '%H:%M')
        train_data.append((train_name, departure_time, index, schedule))
        index += 1

    for i in range(len(train_data)):
        for j in range(len(train_data) - i - 1):
          
            if (train_data[j][0] > train_data[j + 1][0]) or (
                train_data[j][0] == train_data[j + 1][0] and train_data[j][1] < train_data[j + 1][1]
            ) or (
                train_data[j][0] == train_data[j + 1][0] and train_data[j][1] == train_data[j + 1][1] and train_data[j][2] > train_data[j + 1][2]
            ):
                train_data[j], train_data[j + 1] = train_data[j + 1], train_data[j]

    return [item[3] for item in train_data]

n = int(input())
schedules = [input().strip() for _ in range(n)]
sorted_trains = sort_trains(n, schedules)
for train in sorted_trains:
        print(train)