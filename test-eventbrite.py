import requests



def executeGet(path):
	resp = requests.get("https://www.eventbriteapi.com/v3"+path,
		headers = {
		"Authorization": "Bearer xxxxxxxxxxxxxxxxx",
		},verify = True,  # Verify SSL certificate
		);
	return resp;

def getEvents():
	response = executeGet("/users/me/owned_events/");
	events = response.json()['events'];
	evs = [];
	for event in events:
		ev = EBEvent(event);	
		evs.append(ev);
	return evs;
def getAttandeesEmailsForEvent(event):
	response = executeGet("/events/"+event.id+"/attendees/");
	attendees = response.json()['attendees'];
	ebAttandees = [];
	for attandee in attendees:
		ebAttandees.append(EBAttandee(attandee));
	return ebAttandees;

class EBEvent(object):
	"""__init__() functions as the class constructor"""
	def __init__(self, event=None):
		self.name = event['name']['text'];
		self.id = event['id'];
		self.startDate = event['start']['utc'];
		self.endDate = event['end']['utc'];

	def __repr__(self):
		return "EBEvent()"

	def __str__(self):
		return self.name + ' , #' + self.id + ' , ' + self.startDate + ' , ' + self.endDate;

class EBAttandee(object):
	"""__init__() functions as the class constructor"""
	def __init__(self, attandee=None):
		profile = attandee['profile'];
		self.name = profile['name'];
		self.id = attandee['id'];
		self.email = profile['email'];
		self.cell_phone = profile['cell_phone'];
		self.status = attandee['status'];

	def __repr__(self):
		return self.name + ' , ' + self.email + ' , ' + self.cell_phone + ' , ' + self.status + ' , ' + self.id;

	def __str__(self):
		return self.name + ' , ' + self.email + ' , ' + self.cell_phone + ' , ' + self.status + ' , #' + self.id;

if __name__ == "__main__":	
	for event in getEvents():
		# event = getEvents()[0];
		# ebAttandees = getAttandeesEmailsForEvent(event);
		# print("\"%s\"  %s" % (event, ebAttandees));
		print(event);








	#print(response.json());
	#print(map(lambda ev: ev['name'], events))
	

#['events'][0]['name']['text']

