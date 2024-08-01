#!/bin/bash

# Get the kubeconfig from Terraform output
KUBECONFIG=$(terraform output -raw kubeconfig)

# Create the .kube directory if it doesn't exist
mkdir -p ~/.kube

# Save the kubeconfig to ~/.kube/config
echo "$KUBECONFIG" > ~/.kube/config

# Set the correct permissions for the kubeconfig file
chmod 600 ~/.kube/config

echo "Kubeconfig has been saved to ~/.kube/config"
