# Assignment 3

Panagiotis Pallis
csdp1476

# 1.

## a.

I extended yaml to limit each pod to 20% CPU and 256MB RAM I used the resources field

```
 resources:
  requests:
    cpu: 200m
    memory: 256Mi
  limits:
    cpu: 200m
    memory: 256Mi
```

## b.
In the specific manifest I defined minimum pods to be 1 and maximum 8 using minReplicas and maxReplicas fields.

## Benchmarks
I found a tool called Apache Benchmarks (ab) for running http benchmarks.
First I ran the port forwarding command to bind it to my local 8081 port
`kubectl port-forward svc/hello 8080:8080`

So using that port I ran the benchmarks
For 1 client I used:
`ab -n 1000 -c 1 http://localhost:8081/hello`
Results:
```
Concurrency Level:      1
Time taken for tests:   506.911 seconds
Complete requests:      1000
Failed requests:        0
Non-2xx responses:      1000
Total transferred:      448000 bytes
HTML transferred:       177000 bytes
Requests per second:    1.97 [#/sec] (mean)
Time per request:       506.911 [ms] (mean)
Time per request:       506.911 [ms] (mean, across all concurrent requests)
Transfer rate:          0.86 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:   506  507   0.4    507     511
Waiting:        5    6   0.3      6      11
Total:        506  507   0.4    507     511

Percentage of the requests served within a certain time (ms)
  50%    507
  66%    507
  75%    507
  80%    507
  90%    507
  95%    507
  98%    508
  99%    508
 100%    511 (longest request)
```

For 1 client I used:
`ab -n 1000 -c 100 http://localhost:8081/hello`
Results:
```
Concurrency Level:      100
Time taken for tests:   5.576 seconds
Complete requests:      1000
Failed requests:        0
Non-2xx responses:      1000
Total transferred:      448000 bytes
HTML transferred:       177000 bytes
Requests per second:    179.35 [#/sec] (mean)
Time per request:       557.581 [ms] (mean)
Time per request:       5.576 [ms] (mean, across all concurrent requests)
Transfer rate:          78.46 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.1      0       5
Processing:   505  533  53.6    509     693
Waiting:        4   25  37.2      8     182
Total:        505  534  54.2    510     697

Percentage of the requests served within a certain time (ms)
  50%    510
  66%    514
  75%    523
  80%    536
  90%    597
  95%    692
  98%    695
  99%    696
 100%    697 (longest request)
```

I also atached screenshots regarding this in screenshots/

# 2.
To implement this I first created a helm project using
`helm create helm-hello`
Then I use the helm install command:
`helm install goodbye ./helm-hello --set message="Goodbye world!" --set endpoint="/goodbye" --set resources.limits.cpu="250m" --set autoscaling .maxReplicas=20`

Then I checked if everything worked with
`kubectl get deploy,svc,ingress,hpa`

# 3.
First I disabled ingress
`minikube addons disable ingress`
Then I used the following commands to add nginx from the cli:
1. `helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx`
2. `helm repo update`
3. `helm install ingress-nginx ingress-nginx/ingress-nginx --namespace ingress-nginx --create-namespace` (I created a new namespace for this command)

I also added
`ingressClassName: nginx`
to the yaml config because the chart wasnt marked as default and it didnt handle the ingress without the specific definition of classname
