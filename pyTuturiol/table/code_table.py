#  write a program tpo print the table from 2 to 20  in displaytable floder


def generateTable(n):
    table = ""
  
    for i in range(1,11):
        table += f"{i} x {n} = {n*i}\n"

    with open(f"pyTuturiol/table/displaytable{n}.txt", "w") as f:
        f.write(table)


for i in range (2,21):
    generateTable(i)