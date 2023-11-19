try:
    file = open('a_file.txt')
    a_dictionary = {"key": "value"}
    print(a_dictionary['asdasd'])

except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write('something')
    file.close()

except KeyError as e_msg:
    print(f'The key {e_msg} does not exist')

else:
    print('Program ran successfully')

finally:
    print('Program ending')
    raise TypeError('This is self raised error') # to raise exception