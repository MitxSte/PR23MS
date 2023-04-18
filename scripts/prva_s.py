from datetime import datetime, timedelta


def filter_alarms_by_date_range(alarms, start_date, end_date):
    filtered_alarms = []
    start_date = datetime.strptime(start_date, '%Y.%m.%d').date()
    end_date = datetime.strptime(end_date, '%Y.%m.%d').date()

    for alarm in alarms:
        datum = datetime.strptime(alarm['datum'], '%Y.%m.%d').date()
        if start_date <= datum <= end_date:
            filtered_alarms.append(alarm)
    return filtered_alarms


def filter_alarms_zadnji_v_dnevu(podatki):
    last_turned_off = {}

    for alarm in podatki:
        datum = alarm['datum']
        ura_total_minute = alarm['ura_total_minute']

        if datum in last_turned_off:
            if ura_total_minute > last_turned_off[datum]['ura_total_minute']:
                last_turned_off[datum] = alarm
        else:
            last_turned_off[datum] = alarm

    last_turned_off_alarms = list(last_turned_off.values())

    return last_turned_off_alarms




def preberi_podatke(ime_datoteke):
    data = []

    with open(ime_datoteke, 'r') as file:
        # Skipaj prvo vrstico | imena
        next(file)

        for line in file:
            values = line.strip().split(',')

            # Dict za vsako vrstico
            row_data = {
                'datum': values[0],
                'ura': values[1],
                'dan': values[2]
            }

            # Dodas v podatke
            data.append(row_data)


    for alarm in data:
        ura = alarm['ura']
        ura_hours, ura_minutes = map(int, ura.split(':'))
        ura_total_minutes = ura_hours * 60 + ura_minutes
        alarm['ura_total_minute'] = ura_total_minutes


    return data



def izrisi(podatki):
    from matplotlib import pyplot as plt, dates as mdates

    x = [row['datum'] for row in podatki]
    y = [row['ura_total_minute'] for row in podatki]

    x = [datetime.strptime(date, '%Y.%m.%d').date() for date in x]

    #ax = plt.gca()

    plt.plot(x, y, 'o')

    plt.xlabel('Datum')
    plt.ylabel('Ura')

    y_ticks = plt.yticks()[0]
    y_labels = [f"{int(minutes/60):02d}:{int(minutes%60):02d}" for minutes in y_ticks]

    plt.yticks(y_ticks, y_labels)

    plt.xticks(rotation=90, ha='center')

    plt.show()







def get_average_alarm_time_by_month(alarms):
    alarms_by_month = {}
    for alarm in alarms:
        datum = datetime.strptime(alarm['datum'], '%Y.%m.%d')
        month_name = datum.strftime('%B')
        time = alarm['ura_total_minute']
        if month_name not in alarms_by_month:
            alarms_by_month[month_name] = {'total_minutes': 0, 'count': 0}
        alarms_by_month[month_name]['total_minutes'] += time
        alarms_by_month[month_name]['count'] += 1

    average_times_by_month = {}
    for month_name, month_data in alarms_by_month.items():
        average_minutes = month_data['total_minutes'] / month_data['count']
        average_time = timedelta(minutes=average_minutes)
        average_time_formatted = (datetime.min + average_time).time().strftime('%H:%M')
        average_times_by_month[month_name] = average_time_formatted

    month_order = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
    }


    sorted_dict = dict(sorted(average_times_by_month.items(), key=lambda x: month_order[x[0]]))


    return sorted_dict








data = preberi_podatke('test.txt')


zadnji_dnevni = filter_alarms_zadnji_v_dnevu(data)
print(len(zadnji_dnevni))

zadnji_dnevni_april_2022 = filter_alarms_by_date_range(zadnji_dnevni, '2022.04.01', '2022.04.30')
print(len(zadnji_dnevni_april_2022))
izrisi(zadnji_dnevni_april_2022)

zadnji_dnevni_2022 = filter_alarms_by_date_range(zadnji_dnevni, '2020.02.01', '2023.5.31')
print(len(zadnji_dnevni_2022))
izrisi(zadnji_dnevni_2022)


print("Do konca srednje avg")
do_konca_srednje = filter_alarms_by_date_range(zadnji_dnevni, '2020.03.01', '2021.7.01')
do_konca_srednje_avg = get_average_alarm_time_by_month(do_konca_srednje)
print(do_konca_srednje_avg)



print("Od zacetka faksa")
od_zacetka_faksa = filter_alarms_by_date_range(zadnji_dnevni, '2021.10.01', '2023.01.31')
od_zacetka_faksa_avg = get_average_alarm_time_by_month(od_zacetka_faksa)
print(od_zacetka_faksa_avg)



test = get_average_alarm_time_by_month(zadnji_dnevni)
print(len(test))
print(test)

for month_name, average_time_formatted in test.items():
    print(f'{month_name}: {average_time_formatted}')



vsi_konec_poletja_2020 = filter_alarms_by_date_range(data, '2020.08.25', '2020.9.15')
print(len(vsi_konec_poletja_2020))
izrisi(vsi_konec_poletja_2020)


vsi_drugi_lockdown_2020 = filter_alarms_by_date_range(data, '2020.10.2', '2020.12.01')
print(len(vsi_drugi_lockdown_2020))
izrisi(vsi_drugi_lockdown_2020)



