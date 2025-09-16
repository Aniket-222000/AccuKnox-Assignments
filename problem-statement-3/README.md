# kubearmor-zero-trust

Sample Kubernetes workload + KubeArmor "zero-trust / least permissive" policy.

How to use:
1. Ensure you have a running Kubernetes cluster and KubeArmor installed.
2. `cd k8s && kubectl apply -f .`
3. Run `./scripts/test-violations.sh` to trigger policy violations.
4. Use `karmor logs` (or check KubeArmor logs/relay) to capture policy violation alerts.
