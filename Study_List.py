a = [['FE','SEM1'],['FE','SEM2'],['SE','SEM3'],['SE','SEM4'],['TE','SEM5'],['TE','SEM6'],['BE','SEM7'],['BE','SEM8']]
b = ['1' , '2']
gen = ((x, y) for x in a for y in b)

for u, v in gen:
    print(u, v)