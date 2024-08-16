# Pre-Requisites
 - Install Docker Desktop in your local system and enable kubernetes
 - Create a Free Trial account - GCP
 - Install Kubectl - https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html

- Install Gcloud CLI - https://cloud.google.com/sdk/docs/install#mac
- mac - `brew install --cask google-cloud-sdk`
- Getting Started with creation of GKE clusters - https://k21academy.com/docker-kubernetes/create-a-gke-cluster/

# Connecting Local Kubectl with Gcloud
- Pre-requisite : Install gcloud cli from above
- run command `gcloud auth login`
- Optionall set the default project using the below command:
`gcloud config set project <project-id>`
- Connect to Kubernetes Cluster by running the command from GKE Screen
`gcloud container clusters get-credentials cka-certification --zone us-central1-c --project civic-rhythm-404204`


# Install Kubectl locally


# Running an App on Kubernetes

- List Nodes in K8s cluster

```
kubectl get nodes
kubectl config use-context docker 
```
- Deploy the application defined in pod.yml
```

kubectl apply -f pod.yml
kubectl describe pod first-pod # get detailed info about running pod

kubectel get pods # display all the pods in the namespace
kubectl get pod first-pod

kubectl apply -f svc-cloud.yml # Deploy the service 

kubectl get services

kubectl get svc # Check external IP of the service

kubectl get pods --all-namespaces -o wide

kubectl delete pod first-pod

kubectl delete svc cloud-lb

kubectl delete pods --all

kubectl apply -f deploy.yml

kubectl get deployment catgif

kubectl delete deployment catgif

kubectl delete svc cloud-lb

kubectl get pods -o wide

kubectl get pods -o yaml

kubectl describe pods first-pod

kubectl logs first-pod

kubectl logs firstpod --container first_container # incase of Multi container


kubectl exec first-pod -- ps
kubectl exec -it first-pod -- sh
apk add curl
curl localhost:5000


kubectl config get-contexts

kubectl config delete-cluster my-cluster

kubectl config delete-context my-cluster-context


kubectl config use-context docker-desktop

```


# Other Basic Commands
```
kubectl run nginx --image=nginx   # Run container images on kubernetes pods


```