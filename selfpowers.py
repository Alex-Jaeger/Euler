
series = 0

for i in range(1,1001):
    series += i ** i

series_str = str(series)

result = series_str[-10:]

print result
