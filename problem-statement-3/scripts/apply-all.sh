#!/usr/bin/env bash
set -euo pipefail
kubectl apply -f k8s/00-deployment.yaml
kubectl apply -f k8s/01-service.yaml
kubectl apply -f k8s/10-kubearmor-policy.yaml
kubectl apply -f k8s/11-kubearmor-block-sa.yaml
echo "All resources created. Wait a few seconds for pods and KubeArmor policy to take effect."
kubectl get pods -l app=ps1-app -o wide
