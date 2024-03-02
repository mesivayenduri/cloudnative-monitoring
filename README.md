# cloudnative-monitoring



# Creating EKS Cluster

-> eksctl create cluster --name px-npe2301 --nodegroup-name ng-default --node-type t3.micro --nodes 2

<!-- -> eksctl create cluster --name px-npe2302 --version 1.14 --nodegroup-name ng-default --node-type t3.micro --nodes 4 --managed -->

<!-- -> eksctl upgrade nodegroup --name=ng-default --cluster=px-npe2302 -->

<!-- -> eksctl delete nodegroup --cluster px-npe2301 --name ng-default -->

-> eksctl delete cluster --name px-npe2301


# Kubectl Commands

-> kubectl get nodes -A

-> kubectl get pods

-> kubectl get deployments

-> kubectl port-forward svc/cloudnative-monitoring-service 5000:5000

-> kubectl delete deploy cloudnative-monitoring-app

-> kubectl delete svc cloudnative-monitoring-service

# Basic Helm Commands (Not related to this project)

-> helm version

-> helm search repo

-> helm search repo nginx

-> helm search hub nginx

-> helm repo add bitnami https://charts.bitnami.com/bitnami

-> helm pull bitnami/nginx --untar=true
