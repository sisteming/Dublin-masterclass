# Dublin-masterclass (demo1)
-----
Files used for the demos during the Dublin Masterclass session: **The rise of containers: from development to production using Docker**

This demo covers how we build a container image and run to containers working together.

Check the application file (my_app/app.py) to see how the application is connecting to the MongoDB database:

	app.config['MONGO_HOST'] = '192.168.1.101'
	app.config['MONGO_PORT'] = 27017
	app.config['MONGO_DBNAME'] = 'flask_demo'

Update the IP defined in app.config['MONGO_HOST'] for the current IP address.

Check the docker file used for our application: *my_app.dockerfile*
	
Build the docker image for the flask container:

	docker build -t my_app -f my_app.dockerfile .

Run the new container:

	docker run --name my_app -p 8080:80 -i -t my_app

Now that our app is running, execute the command below to start the mongoDB container

	docker run -d --hostname mongo1 --name mongo1 -p 27017:27017 marcob/mongodb-3.4.0-rc3 mongod

In a new terminal, confirm that both containers are running:

	docker ps

Now with our containers running, go to the Flask app at:

	http://localhost:8080

Insert some users into the MongoDB database with the command below:

	mongo --port 27017 < users.js

Refresh the browser so that the new users will show up.

Great, that means our containers are working as expected!
