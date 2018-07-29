from datetime import datetime
from dateutil import tz
from crontab import CronTab
import getpass
from mysql.connector import (connection)
import logging


def fetchSchedule():
	servername = "127.0.0.1";
	username = "root";
	password = "12345678";
	dbname = "ishaoffering";
	query = "SELECT name, schedule, status FROM EVENTBRITE_CONFIG where status='ACTIVE'";
	cnx = connection.MySQLConnection(user=username, password=password, host=servername, database=dbname);
	cursor = cnx.cursor();
	cursor.execute(query,());
	sch = "";
	for (name, schedule, status) in cursor:
		logging.info("Job {} scheduled at {} is now {}".format(name, schedule, str(status)));
		sch = schedule;
		break;
	cursor.close();
	cnx.close();
	return sch;

if __name__ == "__main__":
	try:
		logging.basicConfig(filename='/Users/shaktikumar/projects/isha-offering-sessions/scheduler.log',level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
		logging.info('# Schedule script start with user: %s', getpass.getuser());
		my_cron = CronTab(user=getpass.getuser());
		for job in my_cron:
			if job.comment == 'ishaoffering':
				# print('# Removed:' + job.comment);
				my_cron.remove(job);
		job = my_cron.new(command='/Library/Frameworks/Python.framework/Versions/3.6/bin/python3 /Users/shaktikumar/projects/isha-offering-sessions/test.py',comment='ishaoffering');
		job.setall(fetchSchedule());
		my_cron.write();
		logging.info('# Job created successfully with comment: %s', job.comment);
		print('1');
	except Exception as e:
		logging.error('Error while scheduling job by user: %s, error: %s',getpass.getuser(),str(e));
		print('-1');

