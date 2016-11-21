# Dublin-masterclass (demo2)
-----

This demo covers the deployment of our application and database but using docker compose.
	
Check the services defined in the docker-compose.yml file to become familiar with the options used. 

Check also the application file (my_app/app.py) to see how the application is connecting to the MongoDB database:

	app.config['MONGO_HOST'] = '172.20.0.3'
	app.config['MONGO_PORT'] = 27017
	app.config['MONGO_DBNAME'] = 'flask_demo'

Deploy the containers with a single docker-compose command:

	docker-compose up -d

Check the running containers:

	docker ps

Now with our containers running, go to the Flask app at:

http://localhost:8080

Insert some users into the MongoDB database with the command below:

	mongo --port 27017 < users.js

Refresh the browser so that the new users will show up.

Great, now with docker-compose is even easier to get our containers and application running!
