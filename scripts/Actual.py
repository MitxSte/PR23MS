from datetime import datetime, timedelta


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



def odstrani_neveljavne(data):
    valid_data = []
    for alarm in data:
        ura = datetime.strptime(alarm['ura'], '%H:%M').time()
        datum = datetime.strptime(alarm['datum'], '%Y.%m.%d').date()

        if ura >= datetime.strptime('03:00', '%H:%M').time() and ura <= datetime.strptime('15:00', '%H:%M').time() and datum >= datetime.strptime('2020.01.01', '%Y.%m.%d').date() and datum <= datetime.strptime('2023.06.01', '%Y.%m.%d').date():
            valid_data.append(alarm)

    return valid_data






def dodaj_prost(data):
    for alarm in data:
        alarm['prost'] = 0

    return data

def dodaj_prost_values(data, start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y.%m.%d').date()
    end_date = datetime.strptime(end_date, '%Y.%m.%d').date()

    for alarm in data:
        alarm_date = datetime.strptime(alarm['datum'], '%Y.%m.%d').date()
        if start_date <= alarm_date <= end_date:
            alarm['prost'] = 1

    return data


def dodaj_prost_values_0(data, start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y.%m.%d').date()
    end_date = datetime.strptime(end_date, '%Y.%m.%d').date()

    for alarm in data:
        alarm_date = datetime.strptime(alarm['datum'], '%Y.%m.%d').date()
        if start_date <= alarm_date <= end_date:
            alarm['prost'] = 0

    return data

def nastavi_prost_vikend(data):
    for alarm in data:
        day_of_week = alarm['dan']
        matura = alarm['matura']
        izpitno = alarm['izpitno']
        if (day_of_week == "Sun" or day_of_week == "Sat") and matura != 1 and izpitno != 1:
            alarm['prost'] = 1
    return data







def dodaj_letniCas(data):
    for row in data:
        datum_str = row['datum']
        datum = datetime.strptime(datum_str, '%Y.%m.%d')
        letni_cas = ''
        if (datum.month >= 1 and datum.month <= 2) or (datum.month == 12 and datum.day >= 21) or (datum.month == 3 and datum.day < 21):
            letni_cas = 'zima'
        elif (datum.month >= 3 and datum.month <= 5) or (datum.month == 6 and datum.day < 21) or (datum.month == 3 and datum.day >= 21):
            letni_cas = 'pomlad'
        elif (datum.month >= 6 and datum.month <= 8) or (datum.month == 9 and datum.day < 23) or (datum.month == 6 and datum.day >= 21):
            letni_cas = 'poletje'
        elif (datum.month >= 9 and datum.month <= 11) or (datum.month == 12 and datum.day < 21) or (datum.month == 9 and datum.day >= 23):
            letni_cas = 'jesen'
        row['letniCas'] = letni_cas

    return data



def dodaj_vikend(data):
    for alarm in data:
        datum = datetime.strptime(alarm['datum'], '%Y.%m.%d')
        day_of_week = datum.weekday()
        if day_of_week == 5 or day_of_week == 6:
            alarm['vikend'] = 1
        else:
            alarm['vikend'] = 0

    return data




def dodaj_izpitna(data):
    for alarm in data:
        datum = datetime.strptime(alarm['datum'], '%Y.%m.%d').date()
        if (datum >= datetime.strptime('2023.01.13', '%Y.%m.%d').date() and datum <= datetime.strptime('2023.01.31', '%Y.%m.%d').date()) or \
           (datum >= datetime.strptime('2022.05.31', '%Y.%m.%d').date() and datum <= datetime.strptime('2022.06.13', '%Y.%m.%d').date()) or \
           (datum >= datetime.strptime('2022.01.17', '%Y.%m.%d').date() and datum <= datetime.strptime('2022.01.31', '%Y.%m.%d').date()):
            alarm['izpitno'] = 1
        else:
            alarm['izpitno'] = 0

    return data



def dodaj_matura(data):
    for alarm in data:
        datum = datetime.strptime(alarm['datum'], '%Y.%m.%d').date()
        if (datum >= datetime.strptime('2021.05.29', '%Y.%m.%d').date() and datum <= datetime.strptime('2021.06.18', '%Y.%m.%d').date()):
            alarm['matura'] = 1
        else:
            alarm['matura'] = 0

    return data








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






def povprecje_na_season(data):
    season_times = {'zima': [], 'pomlad': [], 'poletje': [], 'jesen': []}

    for alarm in data:
        season = alarm['letniCas']
        total_minutes = alarm['ura_total_minute']
        season_times[season].append(total_minutes)

    average_times = {}
    for season, times in season_times.items():
        if times:
            total_minutes = sum(times)
            average_minutes = total_minutes / len(times)
            average_time = f"{int(average_minutes / 60):02d}:{int(average_minutes % 60):02d}"
            average_times[season] = average_time

    return average_times




def povprecje_prva_do_zadnja(data):
    dnevni_casi = {}

    for alarm in data:
        date = alarm['datum']
        time = alarm['ura_total_minute']

        if date not in dnevni_casi:
            dnevni_casi[date] = {'count': 0, 'total_duration': 0, 'start_time': time, 'end_time': time}
        else:
            dnevni_casi[date]['count'] += 1
            dnevni_casi[date]['total_duration'] += time - dnevni_casi[date]['start_time']
            dnevni_casi[date]['end_time'] = time

    total_duration = 0
    total_days = 0

    for date, durations in dnevni_casi.items():
        if durations['count'] > 1:
            average_duration = durations['total_duration'] / (
                        durations['count'] - 1)
            dnevni_casi[date]['average_duration'] = average_duration
            total_duration += average_duration
            total_days += 1
        else:
            dnevni_casi[date]['average_duration'] = 0

    overall_average_duration = total_duration / total_days

    overall_average_duration = -overall_average_duration

    print(f"Povprecen cas med prvo in zadnjo budilko: {overall_average_duration} minut\n")

    return dnevni_casi


def filter_alarms_prvi_v_dnevu(podatki):
    last_turned_off = {}

    for alarm in podatki:
        datum = alarm['datum']
        ura_total_minute = alarm['ura_total_minute']

        if datum in last_turned_off:
            if ura_total_minute < last_turned_off[datum]['ura_total_minute']:
                last_turned_off[datum] = alarm
        else:
            last_turned_off[datum] = alarm

    prvi_turned_off_alarms = list(last_turned_off.values())

    return prvi_turned_off_alarms



def average_matura(data):
    total_time = 0
    count = 0
    for alarm in data:
        if int(alarm['matura']) == 1:
            total_time += alarm['ura_total_minute']
            count += 1

    if count > 0:
        average_time = total_time / count
        return average_time
    else:
        return 0


def average_izpitno(data):
    total_time = 0
    count = 0

    for alarm in data:
        if int(alarm['izpitno']) == 1:
            total_time += alarm['ura_total_minute']
            count += 1

    if count > 0:
        average_time = total_time / count
        return average_time
    else:
        return 0



def prost(data):
    filtered_alarms = [alarm for alarm in data if alarm['prost'] == 1]
    return filtered_alarms


def vikend(data):
    filtered_alarms = [alarm for alarm in data if alarm['vikend'] == 1]
    return filtered_alarms

def neprostnevikend(data):
    filtered_alarms = [alarm for alarm in data if (alarm['vikend'] == 0 and alarm['prost'] == 0)]
    return filtered_alarms


def to_hh_mm(minutes):
    ure = int(minutes // 60)
    minute = int(minutes % 60)
    return f"{ure:02d}:{minute:02d}"


def povprecen_cas(data):
    total_minutes = sum(alarm['ura_total_minute'] for alarm in data)
    average_minutes = total_minutes / len(data)
    average_time = to_hh_mm(average_minutes)
    return average_time






podatki = preberi_podatke("test.txt")
print(len(podatki))


podatki = odstrani_neveljavne(podatki)
print(len(podatki))



podatki = dodaj_letniCas(podatki)
podatki = dodaj_matura(podatki)
podatki = dodaj_izpitna(podatki)
podatki = dodaj_vikend(podatki)
podatki = dodaj_prost(podatki)

print(podatki)

#podatki = nastavi_prost_vikend(podatki)

podatki = dodaj_prost_values(podatki, '2020.07.01', '2020.08.31')

podatki = dodaj_prost_values(podatki, '2020.10.26', '2020.10.30') #poc
podatki = dodaj_prost_values(podatki, '2020.12.24', '2021.01.01')
podatki = dodaj_prost_values(podatki, '2021.04.26', '2021.04.30')

podatki = dodaj_prost_values(podatki, '2021.06.19', '2021.09.30')   #konec srednje

podatki = dodaj_prost_values(podatki, '2022.02.01', '2022.02.11')   #izpitno early
podatki = dodaj_prost_values(podatki, '2021.06.14', '2021.09.30')   #1. letnik konec

podatki = dodaj_prost_values(podatki, '2021.04.26', '2021.04.30')

podatki = dodaj_prost_values_0(podatki, '2022.08.01', '2022.08.05')
podatki = dodaj_prost_values_0(podatki, '2022.08.08', '2022.08.12')
podatki = dodaj_prost_values_0(podatki, '2022.08.15', '2022.08.19')









podatki_zadnji = filter_alarms_zadnji_v_dnevu(podatki)


#VIZUALIZACIJA

izrisi(podatki)


izrisi(podatki_zadnji)

podatki_izpitno_22 = filter_alarms_by_date_range(podatki, '2022.01.16', '2022.02.05')

izrisi(podatki_izpitno_22)


podatki_poletje = filter_alarms_by_date_range(podatki, '2022.07.20', '2022.08.30')

izrisi(podatki_poletje)



#ANALIZA

#mesec
print()
test = get_average_alarm_time_by_month(podatki_zadnji)

for month_name, average_time_formatted in test.items():
    print(f'{month_name}: {average_time_formatted}')

#letni cas
print()
test2 = povprecje_na_season(podatki_zadnji)

for season, time in test2.items():
    print(f"{season}: {time}")


#povprecje cas zbujanja
print()
povpPrvaDoZadnja = povprecje_prva_do_zadnja(podatki)


#matura / izpitna | prvi only

prvidnevni = filter_alarms_prvi_v_dnevu(podatki)

print(prvidnevni)

print(to_hh_mm(average_matura(prvidnevni)))
print(to_hh_mm(average_izpitno(prvidnevni)))




#prost
#vikend
#ne prost ne vikend


prst = povprecen_cas(prost(podatki_zadnji))
viknd = povprecen_cas(vikend(podatki_zadnji))
neprstneviknd = povprecen_cas(neprostnevikend(podatki_zadnji))

print()

print(prst)
print(viknd)
print(neprstneviknd)