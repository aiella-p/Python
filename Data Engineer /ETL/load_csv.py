import boto3
import logging
from datetime import datetime

# logfile setup
now = datetime.now() # In this function, the datetime module with now() method we can get current date and time.
timestr = now.strftime("%Y%m%d%H%M%S") # converting datetime in to string format time
log_file_name = 'local_to_redshift_{}'.format(timestr)
logging.basicConfig(filename=log_file_name, filemode='w', level=logging.INFO)

try:
    #create session , AWS session
    session = boto3.Session(
        aws_access_key_id = '',
        aws_secret_access_key = '', 
    )
    #assign AWS S3 resource
    s3 = session.resource('s3')

    # upload file to S3
    s3.meta.client.upload_file(Filename = 'C:\\Data Engineer Role\\ETL\\sales_data_sample.csv', Bucket = 'data-query-proj1', Key = 'sales_data_sample.csv')
    # note the 'key' here is the folders are files inside the aws bucket to be defined.
    # store logs
    logging.info('File uploaded Successfully')

except Exception as e:
    # store log on error
     logging.exception(e)
