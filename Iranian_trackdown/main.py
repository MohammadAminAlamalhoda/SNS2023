import csv
from sqlite3 import Row

main_table = 'Table.csv'
parsed_table_foreigner = 'ParsedTableForeigner.csv'
parsed_table_iranian = 'ParsedTableIranian.csv'

# read a csv file and return a list of lists    
def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)

# write a list to a csv file
def write_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)

Rows = read_csv(main_table)

# write_csv(parsed_table, Rows[0])

unpaid_list_foreigner = []
unpaid_list_iranian = []
unpaid_list = []

unpaid_list_foreigner.append(Rows[0])
unpaid_list_iranian.append(Rows[0])
unpaid_list.append(Rows[0])

for row in Rows:
    if row[-2] == '0':
        paid = False
        for row_check in Rows:
            if row_check[1] == row[1] and row_check[2] == row[2] and row_check[5] == row[5] and row_check[-2] == '1':
                paid = True
                break
        repeated = False
        if not paid:
            for row_double_check in unpaid_list:
                if row_double_check[1] == row[1] and row_double_check[2] == row[2] and row_double_check[5] == row[5]:
                    repeated = True
                    break

            if not repeated:
                if row[-1] == '0':
                    unpaid_list_iranian.append(row)
                else:
                    unpaid_list_foreigner.append(row)


            unpaid_list.append(row)


write_csv(parsed_table_foreigner, unpaid_list_foreigner)
write_csv(parsed_table_iranian, unpaid_list_iranian)
