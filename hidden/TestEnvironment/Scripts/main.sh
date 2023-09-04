#!/bin/bash

# run provision script
./provision.sh

# deploy application
kubectl apply -f deployment.yaml

# run tests
./run-tests.sh

# de-provision resources
./deprovision.sh

echo "Automation script completed."
