#docker stop my_app mongo1 
#docker rm /my_app
docker build -t my_app -f my_app.dockerfile .
docker run --name my_app -p 80:80 -i -t my_app

docker rm /mongo1
docker run -d --hostname mongo1 --name mongo1 -p 27017:27017 mongodb mongod
#docker-compose stop; docker-compose rm -vf 
