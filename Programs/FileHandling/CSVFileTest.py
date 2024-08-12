import csv
from pathlib import Path

def main():
    print("Script Started")
    data = []
    with open('test.csv') as csv_file_output:
        csv_reader = csv.reader(csv_file_output)
        count = 0
        for row in csv_reader:
            if count == 0:
               row.append('Final Amount')
            else:
                  amount = int(row[2])
                  qty = int(row[3])
                  gst = int(row[4])
                  final_amount = amount * qty
                  gst_amount = final_amount * (gst/100)
                  final_total = final_amount + gst_amount
                  row.append(final_total)
            count = count + 1
            data.append(row)

        myfile = Path('output1.csv')
        with open(myfile, 'w') as csv_file_output:
            writer = csv.writer(csv_file_output)
            count = 0
            for each in data:
                if count == 0:
                  header = []
                  header.append("one")
                  header.append("two")
                  writer.writerow(header)
                else:
                    writer.writerow(each)
                count += 1
        print("Script Completed")


main()