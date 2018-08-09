
# test script for work order upload
import csv

from salesforce_bulk import SalesforceBulk
from salesforce_bulk import CsvDictsAdapter

bulk = SalesforceBulk(username="thendricks@pfdrive.com", password="N0rC@1Life!")

job = bulk.create_insert_job("user__c", contentType='CSV', concurrency='Parallel')

reader = csv.DictReader(open('user__c.csv'))
disbursals = []
for row in reader:
    disbursals.append(row)

csv_iter = CsvDictsAdapter(iter(disbursals))
batch = bulk.post_bulk_batch(job, csv_iter)
bulk.wait_for_batch(job, batch)
bulk.close_job(job)

print("Done. Data Uploaded.")