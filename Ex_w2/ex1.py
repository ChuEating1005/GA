dept = ['工工系', '運管系', '管科系', '資財系', '資管所', '科管所', '經管所', 
'GMBA', 'EMBA']
for i in range(9):
    if '系' in dept[i]:
        print(str(i+1) + ' : ' + dept[i] + '(所)')
    elif 'MBA' in dept[i]:
        print(str(i+1) + ' : ' + dept[i] + '(學程)')
    else:
        print(str(i+1) + ' : ' + dept[i])
