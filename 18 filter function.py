## contoh penggunaan filter function
# contoh 1
import statistics

data = [1.3, 2.2, -0.4, 2.7, 4.1, 4.0]
rata2 = statistics.mean(data)
print(rata2)

a = list(filter(lambda x: x>rata2, data))
print(a)
print('\n')


# contoh 2 remove missing data
negara = ['', 'indonesia', 'amerika', 'india', '', '', 'kanada', 'jerman', '']
b = list(filter(None, negara))
print(b)