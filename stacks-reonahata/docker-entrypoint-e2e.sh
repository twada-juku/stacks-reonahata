#!/bin/sh

set -e

wait-for-it selenium_chrome:4444
wait-for-it db_test:5433

alembic upgrade head

exec "$@"

#push