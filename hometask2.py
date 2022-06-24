import csv

logfilename = "E:\\Temp\\2022.06.24\\syslog"
csvfilename = "E:\\Temp\\2022.06.24\\csvlog.csv"
final_list = []

with open(logfilename, "r", encoding='utf-8') as file:
    content = file.readlines()

for line in content:
    if "NOTICE kernel:" in line:
        target_line = line.split("NOTICE kernel:")
        datetime_line = target_line[0].split(",")
        final_list.append([datetime_line[0], target_line[1]])
print(final_list)

with open(csvfilename, 'w', newline="") as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["date", "message"])
    writer.writerows(final_list)
