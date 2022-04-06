import csv
from datetime import datetime
from pytz import timezone


def display_failure_records(records):
    for record in records:
        if record['responseCode'] != 200:
            print("%-25s%-50s%-5s%-25s%-1s" % (
                datetime.fromtimestamp(int(record['timeStamp'])).strftime("%Y-%m-%d %H:%M:%S"),
                record['label'],
                record['responseCode'],
                record['responseMessage'],
                'N/A' if not record['failureMessage'] else record['failureMessage']
            ))

if __name__ == '__main__':
    csv_file = "Jmeter_log1.jtl"

    with open(csv_file, 'r') as _fh:
        records = csv.DictReader(_fh)
        display_failure_records(records)