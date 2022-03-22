##
#  Product Service
#
# @file
# @version 0.1

install:
	poetry install

run:
	uvicorn product_service.main:app --reload

db_upgrade:
	alembic -c product_service/migrations/alembic.ini upgrade head

# end
