# FHDA Course Notification System
[FHDA CourseNotify](http://coursenotify.com) 
is a notification system built for Foothill & De Anza College students that allows students
to monitor course availability and get notified when it is available.

Built with **Flask+MongoDB+Vue.js** and hosted on **AWS with Docker**

#Build
Setup configuration file ```config.prod.py``` and ```manager.prod.yaml``` for backend managers 
and save under directory ```instance/prod/```.

Base config can be find under ```instance/```.

Run the following script
```
git clone https://github.com/Larryun/coursenotify_web.git

# Copy configuration files
cp -r instance coursenotify_web
cp docker-compose.prod.yaml coursenotify_web

cd coursenotify_web

# build docker image
sudo docker-compose -f docker-compose.prod.yaml down
sudo docker images prune
sudo docker volume prune
sudo docker-compose -f docker-compose.prod.yaml build
sudo docker-compose -f docker-compose.prod.yaml up -d

# wait for mongodb to be ready
sleep 3
sudo docker-compose -f docker-compose.prod.yaml up -d web
```
