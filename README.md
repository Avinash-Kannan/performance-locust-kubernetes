# **README Under Construction**
---------------------------------

# Locust Performance test as code with Distributed Load Testing using Docker and Kubernetes
-------------------------------------------------------------------------------------------

## Rough Draft Steps  
- Install pythin, docker/Colima, minikube, kubectl
- Install pythin, docker, minikube, kubectl
- Draft a locust test skeleton
- pull locust image
- docker pull locustio/locust
- build required docker image
- docker build -t blazedemo/locust:v2 .
- minikube start
- kubectl create namespace locust
- deploy helm templates
- helm upgrade --install local-perf-locust locust-helm-chart --set image.tag=v2 --namespace locust
- Check if master and worker pods are up and running 
   => kubectl get pods -n locust
- Log into Pods
   => kubectl exec local-perf-locust-master-56bdc45f64-r7nmt -it sh -n locust

- To access WEB UI :
  => kubectl --namespace locust port-forward service/local-perf-locust 8089:8089
  => URL : http://localhost:8089
- Helm uninstall 
- helm uninstall local-perf-locust -n locust