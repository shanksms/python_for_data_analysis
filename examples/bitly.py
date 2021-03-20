import json
from collections import defaultdict
from collections import Counter

def read_file_into_list_of_dicts(file_path : str):
    return [json.loads(line) for line in open(file_path)]
def count_most_often_occurring_timezones(records):
    time_zones = [rec['tz'] for rec in records if 'tz' in rec and rec['tz'] != '']
    time_zones_count_dict = get_time_zone_count(time_zones)
    return top_counts(time_zones_count_dict)
def get_time_zone_count(sequence : list):
    count = {}
    for tz in sequence:
        if tz in count:
            count[tz] += 1
        else:
            count[tz] = 1
    return count

def get_time_zone_count2(timezones : list):
    count = defaultdict(int) #values will be assigned to 0
    for tz in timezones:
        count[tz] += 1
    return count
def top_counts(count_dict, n = 10):
    value_key_pairs = [(count, tz)  for tz , count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
def top_counts_simplest(timezones : list):
    counter = Counter(timezones)
    return counter.most_common(2)

if __name__ == '__main__':
    path = 'bitly_usa_gov.txt'
    records = read_file_into_list_of_dicts(path)
    print(count_most_often_occurring_timezones(records))
    print(top_counts_simplest(['a', 'a', 'b', 'c', 'd', 'e', 'e']))
