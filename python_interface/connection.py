import psycopg2

class Connection:

	def __init__(self, database, user, password='elykips+233', host='localhost', port='5432'):
		self.cursor = None
		connection = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
		self.cursor = connection.cursor()

	def query(self, query):
		self.cursor.execute(query)
		return self

	def fetch_one(self):
		return self.cursor.fetchone()

	def fetch_all(self):
		return self.cursor.fetchall()



if __name__ =='__main__':
	db=Connection('dvdrental','postgres')
	

	add_actor = db.query("INSERT INTO actor (first_name, last_name) VALUES('MEST', 'elykips')")

	# actors_and_film_count = db.query("SELECT first_name, COUNT(actor.actor_id) FROM actor JOIN film_actor ON film_actor.actor_id = actor.actor_id JOIN film ON film.film_id = film_actor.film_id GROUP BY first_name").fetch_all()
	actors = db.query('SELECT first_name, last_name from actor WHERE last_name LIKE "%elykips%"').fetch_all()
	for actor in actors:
		print("Name: {}\n".format(*actors))