import json
import pandas as pd
def read_file_into_list_of_dicts(file_path : str):
    return [json.loads(line) for line in open(file_path)]

if __name__ == '__main__':
    records = read_file_into_list_of_dicts('bitly_usa_gov.txt')
    frame = pd.DataFrame(records)
    #print(frame.head())
    #print(frame.info())
    #print(type(frame['tz']))
    #print(frame['tz'][:10])
    #drop all the time zones having '' in the value
    #print(type(frame['tz'] != ''))
    #print(frame['tz'] != '')
    #frame = frame[frame['tz'] != '']
    #value_count() sorts by default
    tz_counts = frame['tz'].value_counts()
    print(tz_counts[:20])
    clean_tz = frame['tz'].fillna('missing')
    #print(clean_tz == '')
    #below is a bit tricky to understand
    clean_tz[clean_tz == ''] = 'unknowns'
    clean_tz_counts = clean_tz.value_counts()
    print(clean_tz_counts[:20])
