import pandas as pd

naive_times = pd.date_range(start='2017', end='2018', freq='1h')
coordinates = [(30, -110, 'Tucson', 700, 'Etc/GMT+7'),
                   (40, -120, 'San Francisco', 10, 'Etc/GMT+8'),
                   (35, -105, 'Albuquerque', 1500, 'Etc/GMT+7'),
                   (50, 10, 'Berlin', 34, 'Etc/GMT-1')]

print(naive_times)
print(coordinates[0])