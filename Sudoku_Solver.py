import csv

Choice=int(input("Enter 1 to input sudoku as an array, Enter 2 to input sudoku in excel file: "))

if Choice==1:
    rows = eval(input("Enter sudoku"))
elif Choice==2:
    excel=open("Sudoku.csv","r")
    read=csv.reader(excel)
    rows = []
    for readrow in read:
        row=[]
        for i in range(9):
            num=int(readrow[i])
            row.append(num)
        rows.append(row)
array = rows

def square(x, y, z):
    global array
    myarr = []
    for i in range((y//3)*3, (y//3)*3+3):
        for j in range((x//3)*3, (x//3)*3+3):
            myarr.append(array[i][j])
    if z not in myarr:
        return True
    else:
        return False


def row(y, z):
    global array

    for i in array[y]:
        if i == z:
            return False
    return True


def column(x, z):
    global array
    for i in range(9):
        if array[i][x] == z:
            return False
    return True

con=True
def check():
    global con
    while con:
        for i in range(9):
            for j in range(9):
                if array[i][j] == 0:
                    for h in range(1, 10):
                        if row(i, h) and column(j, h) and square(j, i, h):
                            array[i][j] = h
                            check()
                            array[i][j] = 0
                    return
        print(*array, sep="\n")
        con=False
        break
    if Choice==2:
        excel=open("Sudoku_Solution.csv","w", newline="\n")
        type=csv.writer(excel)
        type.writerows(array)
        excel.close()
check()
