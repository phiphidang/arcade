# Depends on ~/src/geometric/square_example.py

sqrs = []

a_t = [['1', '1', '1', '1', '1', '1', '1', '0'], ['1', '0', '0', '1', '0', '0', '1', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '1', '1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0']]

characters = {
    'a': [['0', '0', '1', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '1', '0', '1', '0', '0', '0'], ['0', '1', '1', '0', '1', '0', '0', '0'], ['0', '1', '0', '0', '0', '1', '0', '0'], ['0', '1', '1', '1', '1', '1', '0', '0'], ['0', '1', '0', '0', '0', '1', '0', '0'], ['1', '1', '1', '0', '1', '1', '1', '0'], ['0', '0', '0', '0', '0', '0', '0', '0']]
  , 'b': [['1', '1', '1', '1', '1', '1', '0', '0'], ['0', '1', '0', '0', '0', '0', '1', '0'], ['0', '1', '0', '0', '0', '0', '1', '0'], ['0', '1', '0', '0', '0', '0', '1', '0'], ['0', '1', '1', '1', '1', '1', '0', '0'], ['0', '1', '0', '0', '0', '0', '1', '0'], ['0', '1', '0', '0', '0', '0', '1', '0'], ['0', '1', '0', '0', '0', '0', '1', '0'], ['1', '1', '1', '1', '1', '1', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0']]
  , 'c': [['0', '0', '1', '1', '1', '1', '0', '0'], ['0', '1', '0', '0', '0', '0', '1', '0'], ['1', '0', '0', '0', '0', '0', '0', '0'], ['1', '0', '0', '0', '0', '0', '0', '0'], ['1', '0', '0', '0', '0', '0', '0', '0'], ['1', '0', '0', '0', '0', '0', '0', '0'], ['1', '0', '0', '0', '0', '0', '0', '0'], ['0', '1', '0', '0', '0', '0', '1', '0'], ['0', '0', '1', '1', '1', '1', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0']]
  , 't': [['1', '1', '1', '1', '1', '1', '1', '0'], ['1', '0', '0', '1', '0', '0', '1', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '1', '1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0']]
}

a_t = characters['c']

for row in range(len(a_t)):
    for char in range(len(a_t[row])):
        #print "At pos: (%i,%i) is the value: %s" % (row, char, a_t[row][char])
        if int(a_t[row][char]):
            sqrs.append(
                Rect.Square((char + 5,row + 5))
            )
