# wisecow - Docker + Kubernetes + CI/CD (sample)

This project contains Dockerfile, Kubernetes manifests, TLS helper and a GitHub Actions workflow
to containerize and deploy the Wisecow shell app (original source: https://github.com/nyrahul/wisecow).

NOTE: The repository must already contain `wisecow.sh` (from the original project). This packaging
assumes you add these new files to that same repo and push.

## Files added
- Dockerfile
- k8s/deployment.yaml
- k8s/service.yaml
- k8s/ingress.yaml
- k8s/tls-secret.yaml (example using self-signed cert)
- scripts/generate-self-signed-cert.sh
- .github/workflows/ci-cd.yml

## How to use locally
1. Build image:
   docker build -t youruser/wisecow:latest .
2. Run locally:
   docker run --rm -p 4499:4499 youruser/wisecow:latest

## How to deploy to cluster (manual)
1. Apply manifests:
   kubectl apply -f k8s/
2. If using Ingress TLS with self-signed secret create the TLS secret first (or apply k8s/tls-secret.yaml)

## CI/CD (GitHub Actions)
- The workflow builds and pushes the Docker image to Docker Hub (requires DOCKER_USERNAME & DOCKER_PASSWORD secrets).
- It can also deploy to a cluster if you set `KUBE_CONFIG` secret to your base64-encoded kubeconfig.
