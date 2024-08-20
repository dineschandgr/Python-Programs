import csv
from pathlib import Path

def main():
    data = []

    #file reading
    with open('test.csv') as csv_file_input:
        csv_reader = csv.reader(csv_file_input)
        count = 0
        for row in csv_reader:
            if count == 0:
               print("header row ",row)
            else:
                print("data row ",row)
                print("ID ",row[0])
                print("Product ",row[1])
                print("Amount ",row[2])
                print("Quantity ",row[3])
                print("GST ",row[4])
            count += 1
            data.append(row)
        print("data ", data)

    #file writing
    myfile = Path('test-output.csv')
    with open(myfile, 'w') as csv_file_output:
        writer = csv.writer(csv_file_output)
        count = 0
        for row in data:
             writer.writerow(row)
    print("Script Completed")


main()
