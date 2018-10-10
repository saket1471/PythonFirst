from datetime import datetime
#from pprint import pprint


def convert_timestamp(ts, from_pattern, to_pattern):
    dt = datetime.strptime(ts, from_pattern)
    return datetime.strftime(dt, to_pattern)


timestamps = [
    '2015-08-24 00:00:00',
    '2015-08-30 00:00:00',
    '2015-08-22 00:00:00',
    '2015-08-21 00:00:00',
    '2015-08-25 00:00:00',
    '2015-08-29 00:00:00',
    ]

date_strings = [convert_timestamp(ts, '%Y-%m-%d %H:%M:%S', '%m-%d-%Y') for ts in timestamps]
print(date_strings)
date_strings2 = [convert_timestamp(ts, '%Y-%m-%d %H:%M:%S', '%Y-%m-%d') for ts in timestamps]
print(date_strings2)
date_strings3 = [convert_timestamp(ts, '%Y-%m-%d %H:%M:%S', '%Y_%m_%d') for ts in timestamps]
print(date_strings3)

["{0:02}-{1:02}-{2}".format(d.month, d.day, d.year) for d in map(lambda d: parser.parse(d), dates)]