Panagiotis Pallis
csdp1476

1.

a.
I used 
`sudo pacman -S kubectl minikube`
and then started minikube using
`minikube start`
Then I created a configuration for the pod in nginx.yaml and then used
`kubectl apply -f nginx.yaml`

and then I check if it is up:
`kubectl get pods`

b.
Then we would need to forward the port 80 to our machine and use & to background the process:
`kubectl port-forward pod/nginx 9090:80 &`
by navigating to the browser or using
`curl localhost:9090`
we can see it works

C.
By using
`kubectl logs nginx`
we can see the logs.
```
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2026/03/18 18:58:07 [notice] 1#1: using the "epoll" event method
2026/03/18 18:58:07 [notice] 1#1: nginx/1.29.5
2026/03/18 18:58:07 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0) 
2026/03/18 18:58:07 [notice] 1#1: OS: Linux 6.18.12-1-MANJARO
2026/03/18 18:58:07 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2026/03/18 18:58:07 [notice] 1#1: start worker processes
2026/03/18 18:58:07 [notice] 1#1: start worker process 30
2026/03/18 18:58:07 [notice] 1#1: start worker process 31
2026/03/18 18:58:07 [notice] 1#1: start worker process 32
2026/03/18 18:58:07 [notice] 1#1: start worker process 33
2026/03/18 18:58:07 [notice] 1#1: start worker process 34
2026/03/18 18:58:07 [notice] 1#1: start worker process 35
2026/03/18 18:58:07 [notice] 1#1: start worker process 36
2026/03/18 18:58:07 [notice] 1#1: start worker process 37
2026/03/18 18:58:07 [notice] 1#1: start worker process 38
2026/03/18 18:58:07 [notice] 1#1: start worker process 39
2026/03/18 18:58:07 [notice] 1#1: start worker process 40
2026/03/18 18:58:07 [notice] 1#1: start worker process 41
127.0.0.1 - - [18/Mar/2026:19:04:36 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0" "-"
2026/03/18 19:04:36 [error] 30#30: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 127.0.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:9090", referrer: "http://localhost:9090/"
127.0.0.1 - - [18/Mar/2026:19:04:36 +0000] "GET /favicon.ico HTTP/1.1" 404 153 "http://localhost:9090/" "Mozilla/5.0 (X11; Linux x86_64; rv:148.0) Gecko/20100101 Firefox/148.0" "-"
127.0.0.1 - - [18/Mar/2026:19:23:22 +0000] "GET / HTTP/1.1" 200 615 "-" "curl/8.18.0" "-"
```

d.
I used
`kubectl exec -it nginx -- sh`
to get a shell in the pod and then I used
`vi /usr/share/nginx/html/index.html`
to change the html file.
Then checking the site we can see it has been changed.

e.
To download the file I used
`curl localhost:9090 > index.html`
and then I changed it using
`vi index.html`
to something else I chose
`<p>test</p>`
then I used
`kubectl cp index.html nginx:/usr/share/nginx/html/index.html`
to copy it back to the pod
then I checked it again using
`curl localhost:9090`
and indeed the new file was returend

f.
Here I used one command to delete the pod and force it to stop
`kubectl delete pod nginx`

2.

a.
I used a simple sh script to download the website defined in download-csd.yaml
then I started the containers usign
`kubectl apply -f download-csd.yaml`
and checked the logs
`kubectl logs downlaod-csd`
and it seemed to work.

Note: I also included libraries, overrides (for insecure http) to mitigate issues along with cli interactiveness solutions issues

b.
I extended the previous config and also changed the container names to download-csd-extended. I added nginx and cronjobs and then portforwarded
`kubectl port-forward pod/download-csd-extended-nginx 9090:80 &`
and using the browser(or curl) I got the website. This is defined in download-csd-extended.yaml

c.
Here I extended the already extended config and created an new one `download-csd-extended-deployment.yaml`
Here I used the previous containers,jobs and added a init container to get and download the website and deploy it(similarly with b.) but I extended more controls like refresh etc..
I confirmed it by navigating to the browser and using `kubectl logs` to cehck if it works properly

3.

a.
Here I created a docker file and I used
`docker build -t panpas161/hy548-nginx-download-site:1.0 .`
to build it and then push it
`docker push panpas161/hy548-nginx-download-site:1.0`

In the docker file I used an environment variable that is being passed to the download script and downloads the site.

b. + c.
Defined in download-nginx-extended.yaml I merged questions b. and c. to avoid making excessive files.

After I created the yaml I performed some checks

First for validating dockerfile is correct with the load balancer

I applied the yaml and I used
`kubectl rollout status deployment/site-csd`
`minikube tunnel`
commands
and then cheked using
`kubectl get svc site-csd-svc`

After that I validated the ingress
I first enbled it
`minikube addons enable ingress`
I applied the config
`kubectl apply -f download-nginx-exnteded.yaml`
then I used the tunnel
`minikube tunnel`
finally when I used curl it worked for folders csd and math

