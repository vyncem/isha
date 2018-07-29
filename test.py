from datetime import datetime
from dateutil import tz
import traceback
import logging
import getpass

if __name__ == "__main__":
	# date_1 = datetime.strptime('10/02/2018', '%d/%m/%Y');
	# date_2 = datetime.strptime('2018-06-10T12:30:00Z','%Y-%m-%dT%H:%M:%SZ').date();
	# date_3 = datetime.strptime('12/12/2018', '%d/%m/%Y');
	# comp = date_1 < date_2 < date_3;
	# print(comp);
	# print(datetime.strptime('2017-06-10T12:30:00Z','%Y-%m-%dT%H:%M:%SZ').date());
	try:
		logging.basicConfig(filename='/Users/shaktikumar/projects/isha-offering-sessions/test.log',level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
		logging.info('Test script start with user: '+getpass.getuser());
	except Exception as e:
		logging.error('Error while executing test script: '+ str(e));
		#logging.error(traceback.format_exc())
	    # Logs the error appropriately. 
