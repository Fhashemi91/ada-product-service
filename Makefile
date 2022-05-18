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

deploy:
	gcloud builds submit --tag gcr.io/ada-return/product-service
	gcloud run deploy --image gcr.io/ada-return/product-service --platform managed

# end
