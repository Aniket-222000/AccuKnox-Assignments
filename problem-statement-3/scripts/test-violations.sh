#!/usr/bin/env bash
set -euo pipefail

NS=default
POD=$(kubectl get pod -n $NS -l app=ps1-app -o jsonpath='{.items[0].metadata.name}')
echo "Target pod: $POD"

echo "1) Trying to read service account token (should be BLOCKED by ksp-ps1-block-sa-token) ..."
kubectl -n $NS exec -it $POD -- cat /var/run/secrets/kubernetes.io/serviceaccount/token || true

echo "2) Trying to run an unauthorized binary (e.g. /bin/ps) — should be blocked/audited by ksp-ps1-zero-trust ..."
kubectl -n $NS exec -it $POD -- ps aux || true

echo "3) Trying to curl an external site from /bin/sh (if curl binary is not allowed, it should be blocked by policy) ..."
kubectl -n $NS exec -it $POD -- /bin/sh -c "which curl && /usr/bin/curl -sSf --max-time 5 https://example.com || echo 'curl failing or not installed'"

echo "Done. Now view KubeArmor alerts (see README for karmor usage)."
