# Assignment 4

## 1.
### a.
I used the following commands for installing the custom resource:
`kubectl apply -f ex1/fruit-crd.yaml`

### b.
I then used the fruit-instance config for creating the instance
`kubectl apply -f ex1/fruit-apple.yaml`

### c.
The command for getting the instance and return it in a yaml format is:
`kubectl get fruit apple -o yaml`

### d.
`kubectl get fruits`

## 2.
## a.
I downloaded the controller.py and the otehr files from the repository and I created a Dockerfile.
I used the commands
`docker build ex2/`
to verify if everything was correct and then I uploaded it using:
`docker build -t panpas161/assignment4-ex2:latest .`
`docker push panpas161/assignment4-ex2:latest`

## b.
I created the greeting-controller.yaml file and maade sure to setup the correct permissions

## Verification Commands
I first applied the config:
`kubectl apply -f ex2/greeting-controller.yaml`
`kubectl apply -f ex2/greeting-crd.yaml`

To check if the pod is running I used the list command for the greetings-system namespace:
`kubectl get pods -n greetings-system`
And then checked the logs:
`kubectl -n greetings-system logs -l app=greeting-controller`

## 3.
I downloaded the files form the repository and then I changed them.
Specifically I changed controller.py to support https communication an changed the webhook.yaml to also support it.
I removed the nginx configuration since we wont be using nginx and instead I changed to rely on the deployment
To verify I used 
`kubectl apply -f webhook.yaml`
which returned an error that `cert-manager.io/v1` wasnt found so I isntalled it
`kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.16.2/cert-manager.yaml`
and I tried again which worked.

For verification I also used
`kubectl get pods,svc -n custom-label-injector`
for getting all teh pods and
`kubectl logs pod/controller-5f94b596c5-w68cc -n custom-label-injector`
for fetching the logs