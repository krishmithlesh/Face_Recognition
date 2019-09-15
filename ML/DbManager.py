from pymongo import MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017')

db = client['mydatabse']

print(db)


class DbManagers:
	def insert(self,name,time,imagepath):
		self.name = name
		self.time = time
		self.imagepath = imagepath
		# // write a code to insert record into database
		print(name,time,imagepath)
		post_data = {
    	'name': name,
    	'time': time,
    	'imagepath': imagepath
		}
		result = db.posts.insert_one(post_data)
		print('One post: {0}'.format(result.inserted_id))


	def checkExistingAtt(self,name,time):
		self.name = name
		self.time = time
		# //check name and time from database
		try:
			found = db.posts.find_one({'name': name,'time':time})
			print("found",found)	
			if found is not None:
				return True
			else:
				return False


		except Exception as e:
			print("foundException",e)

	

	def __init__(self,name,imagepath,time):
		self.name = name
		self.time = time
		self.imagepath = imagepath
		try:
			check = self.checkExistingAtt(name)
			print(check)

			if check is False:
				self.insert(name,time,imagepath)
				
		except Exception as e:
			print("Exception",e)

	