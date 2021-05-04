def comparison(a, b):
    if a > b:
        return 'Successfully'
    if a == b:
        return 'Nearly'
    if a < b:
        return 'Loser'


result = comparison(7, 9)
print(result)
