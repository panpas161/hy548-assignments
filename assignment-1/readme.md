# 1.
## a)
We will use the following commands:
`docker pull nginx:1.29.5`
`docker pull nginx:1.29.5-alpine`

## b)
We use the following commands to compare sizes:
`docker images nginx:1.29.5`
`docker images nginx:1.29.5-alpine`
As we can see the first image contents are 65.8MB while the second one's is 26.9 MB

## c)
We run the container:
`docker run -d -p 80:80 nginx:1.29.5`

## d)
We confirm that the container is running:
`docker ps`

## e)
We use the container id (different each time) to check the logs:
`docker logs 3a6f19e671f2`

## f)
Now we stop the container:
`docker stop 3a6f19e671f2`

## g)
Starting the docker container:
`docker start 3a6f19e671f2`

## h)
Now we stop and remove the container
i) `docker stop 3a6f19e671f2`
ii) `docker rm 3a6f19e671f2`

# 2.
## a)
We run the container again:
`docker run -d -p 80:80 nginx:1.29.5`
and then we run the terminal inside the machine:
`docker exec -it db2424bce11 /bin/bash`
then we create a index.html file:
`echo "Welcome to MY nginx!" > /usr/share/nginx/html/index.html`

Now if we check the browser:

## b)
We download the file:
`docker cp db2424bce11:/usr/share/nginx/html/index.html .`
We replace the file locally in our computer:
`echo "<h1>Hello World!</h1>" > index.html`

and then we upload the new file:
`docker cp index.html db2424bce11:/usr/share/nginx/html/index.html`
Checking the browser we can see that it works

## c)
By stopping the container:
`docker stop db2424bce11`
`docker rm db2424bce11`
`docker run -d -p 80:80 nginx:1.29.5`
and checking the browser we see that the default page appears again, this is due to not implementing any persistent changes

## d)
We start the container and we mount the volume in the local directory test-site:
`docker run -d -p 80:80 -v /home/panos/courses/cs548/assignment1/test-site:/usr/share/nginx/html:ro nginx:1.29.5`

# 3.
## a)
By building the image without the changes with name "django-1" using the command `docker build django-1 .` and then building the image after the changes as "django-2" we can see:
django-1:latest                             bdee03d0a0fa       1.53GB          393MB        
django-2:latest                             408a71380fa6       1.54GB          395MB    

the size increase is due to vim-tiny being installed
Running the container will cause the container to have larger size due to volume files
## b)
Running containers with debug on and off using the commands:
`docker run -d --name django-debug -p 8000:8000 -v django-db-debug:/app/db django`

`docker run -d --name django-simple -p 8001:8000 -e DJANGO_DEBUG=0 -v django-db-simple:/app/db django`

that way we bind them to different ports on the host system.
we see that more details are included in the debug version such as errors and other information while in no debug it lacks those information.


## 4.
The github actions file has been included in the repo