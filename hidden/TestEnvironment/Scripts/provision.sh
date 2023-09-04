#!/bin/bash

# create EKS cluster
aws eks create-cluster --name my-test-cluster --role-arn arn:aws:iam::049134394008:role/AmazonEKSClusterPolicy --resources-vpc-config subnetIds=subnet-0d62628560993ed9d,securityGroupIds=sg-0a68677c9e6879d13

# configure kubectl
aws eks update-kubeconfig --region us-west-2 --name my-test-cluster

echo "Provisioning completed."
