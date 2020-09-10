def enumerate(number,values=0):
    n = values
    for element in number:
        yield n, element
        n += 1

seasons = ['Spring','Summer','Fall','Winter']
print(list(enumerate(seasons)))

seasons_per_sequence = ['one','two','three','four']
seasons = ['Spring','Summer','Fall','Winter']

for numbers,values in zip(seasons_per_sequence,seasons):
    print('numbers:{},values:{}'.format(numbers,values))

numbers:one,values:Spring
numbers:two,values:Summer
numbers:three,values:Fall
numbers:four,values:Winter