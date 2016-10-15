#!/bin/bash
set -e

echo "Waiting for database to be ready"
mysqladmin -h $DB_HOST -u $DB_USERNAME -p$DB_PASSWORD  --silent --wait=30 ping
if [[ "$ENV" == "dev" ]]; then
  echo "Loading development data"
  # mysql -h $DB_HOST -u $DB_USERNAME -p$DB_PASSWORD pinfo < dev-data.sql
fi

exec "$@"
