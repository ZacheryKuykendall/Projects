#!/bin/bash

# de-provision Kubernetes resources
kubectl delete -f deployment.yaml

# delete EKS cluster
aws eks delete-cluster --name my-test-cluster

echo "Deprovisioning completed."
