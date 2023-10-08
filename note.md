# Downloading Data

## csv.reader()

+ `csv.reader()` take `list` as attrgument.
+ `reader = csv.reader()` return a `reader object` contain individual list.
+ ya jaha bhi (,) comma dekha ta  ha uska pehala ka item ko list ma covert kar deta ha and usa list ko reader object ma add kar deta ha.

## next()

+ `next()` take `reader object` as arrgument.
+ each time `next(reader)` return a next item or list.

```python
result:
['STATION', 'NAME', 'DATE', 'TAVG', 'TMAX', 'TMIN']
```

## enumerate() function

+ `enumerate()` return: index of item and item value.
+ `enumerate()` take `list` a arrgument.

for index, column_header in enumerate(header_row):
    print(index, column_header)

## looping throught reader object

```python
for row in reader_obj:
    print(row)

result:
['USW00025333', 'SITKA AIRPORT, AK US', '2021-07-18', '', '63', '57']
['USW00025333', 'SITKA AIRPORT, AK US', '2021-07-19', '', '70', '55']
['USW00025333', 'SITKA AIRPORT, AK US', '2021-07-01', '', '61', '53']
['USW00025333', 'SITKA AIRPORT, AK US', '2021-07-02', '', '60', '52']
['USW00025333', 'SITKA AIRPORT, AK US', '2021-07-03', '', '66', '54']
['USW00025333', 'SITKA AIRPORT, AK US', '2021-07-04', '', '60', '55']
['USW00025333', 'SITKA AIRPORT, AK US', '2021-07-31', '', '66', '48']

```
