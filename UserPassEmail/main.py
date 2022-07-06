import csv
from send_mail import send_mail
main_table = 'snss2022.csv'
corrected_table = 'sns2022_correct.csv'

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

file_name = "email.html"
file_name_en = "email_en.html"
num_emails = 5

for i, row in enumerate(Rows[242:]):
    if len(row[2])<10:
        num_zeros = 10-len(row[2])
        for i in range(num_zeros):
            row[2] = "0"+row[2]
    if '\xa0' in row[0]:
        row[0] = row[0].replace('\xa0', '')
    
    print(row)
    try:
        # if i<221:
        #     # send_mail(row, file_name)
        #     print("Sent - fa", '\n')
        # else:
            send_mail(row, file_name_en)
            print("Sent - en", '\n')

    except AssertionError as error:
        print(error, '\n')