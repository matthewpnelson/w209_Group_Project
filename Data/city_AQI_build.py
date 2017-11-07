

import csv
import os
# import subprocess

# Grab file names from the folder (specify the folder)
def get_file_names():
    file_list = []
    for filename in os.listdir("C:/Users/User/Documents/Berkeley/data_visualizations/Final Project/Data/EPA AQI - Daily - City"):
        file_list.append("C:/Users/User/Documents/Berkeley/data_visualizations/Final Project/Data/EPA AQI - Daily - City/"+str(filename))
    return file_list

# Delete and Create the Output File

# try:
#     os.remove("C:/Users/User/Documents/Berkeley/data_visualizations/Final Project/Data/EPA AQI - Daily - County/county_AQI.csv")
# except:
#     pass

# # Make sub directories (if not already created)
# bash_call = "mkdir "+str(uncompressed_folder)+"success"
# subprocess.call(bash_call, shell=True)


# Get file names in current folder
file_names = get_file_names()

def mygen(row, year):
    # for row in reader:
        # print(year + "," + row)
        yield year + "," + row

with open("C:/Users/User/Documents/Berkeley/data_visualizations/Final Project/Data/EPA AQI - Daily - City/city_AQI.csv", 'wt+') as fout:
    linewriter = csv.writer(fout, delimiter=',',# newline=''
                            quoting=csv.QUOTE_MINIMAL, lineterminator='\r')
    total_rows_imported = 0
    for each in file_names:
        year = str(each[-8:-4])
        file_rows_imported = 0
        try:
            if (int(year) > 1979) and (int(year) < 2018):
                print(year)
                # print(each)
                with open(each, 'rt') as fin:
                    linereader = csv.reader(fin, delimiter=',')

                    # Add header if no rows imported yet
                    if total_rows_imported == 0:
                        for row in linereader:
                            linewriter.writerow(row)
                            total_rows_imported += 1
                            break
                    for row in linereader:
                        # Skip Header Row
                        if file_rows_imported == 0:
                            file_rows_imported += 1
                            total_rows_imported += 1
                            continue
                        # Add all Rows
                        else:
                            linewriter.writerow(row)
                            file_rows_imported += 1
                            total_rows_imported += 1
                        # linewriter.writerow(mygen(row, year))

            else:
                continue
        except:
            continue
        print("Rows Imported %i" %file_rows_imported)
        print("Total Rows Imported %i" %total_rows_imported)
