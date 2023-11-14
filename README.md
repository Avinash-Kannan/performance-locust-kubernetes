# **⚠️⚠️ README Under Construction ⚠️⚠️**
---------------------------------

# Locust Performance test as code with Distributed Load Testing using Docker and Kubernetes
-------------------------------------------------------------------------------------------

## Rough Draft Steps  
- Install python, docker/Colima, minikube, kubectl
- Draft a locust test skeleton
- pull locust image
   Run => `docker pull locustio/locust`
- build required docker image
   Run => `docker build -t blazedemo/locust:v2 .`
- Minikube is a lightweight Kubernetes implementation that creates a VM on your local machine and deploys a simple cluster containing only one node
   Run => `minikube start`
- Create a namespace for the local cluster 
   Run => `kubectl create namespace locust`
- To deploy helm templates
   Run => `helm upgrade --install local-perf-locust locust-helm-chart --set image.tag=v2 --namespace locust`
- Check if master and worker pods are up and running 
   => `kubectl get pods -n locust`
- Log into Pods
   => `kubectl exec local-perf-locust-master-56bdc45f64-r7nmt -it sh -n locust`

- To access WEB UI :
  => `kubectl --namespace locust port-forward service/local-perf-locust 8089:8089`
  => URL : http://localhost:8089
- To  uninstall Helm templates
   Run => `helm uninstall local-perf-locust -n locust`