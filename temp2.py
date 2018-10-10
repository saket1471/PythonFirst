from dateutil import parser

dates = [
    '2015-08-24',
    '2015-08-30',
    '2015-8-22',
    '2015-08-1',
    '2015 08 25',               # Cant be parsed
    '2015_08_29',               # Cant be parsed
]

# Convert All other parser

print(list(map(
    lambda d: parser.parse(d),
    dates
)
))


# print(list(map(
#     lambda d: "{0:02}-{1:02}-{2}".format(d.month, d.day, d.year),
#     map(
#         lambda d: parser.parse(d),
#         dates
#     )
# ))
# )
#
# print(list(map(
#     lambda d: "{0}-{1}-{2}".format(d.month, d.day, d.year),
#     map(
#         lambda d: parser.parse(d),
#         dates
#     )
# ))
# )
#
