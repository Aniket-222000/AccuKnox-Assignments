#!/usr/bin/env bash
set -euo pipefail
DOMAIN=${1:-wisecow.local}
CERT_DIR=./certs
mkdir -p $CERT_DIR
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \\
  -keyout $CERT_DIR/tls.key \\
  -out $CERT_DIR/tls.crt \\
  -subj "/CN=$DOMAIN/O=$DOMAIN"
echo "Created certs in $CERT_DIR"
echo "Base64 encoded cert:"
base64 -w0 $CERT_DIR/tls.crt || true
echo
echo "Base64 encoded key:"
base64 -w0 $CERT_DIR/tls.key || true
