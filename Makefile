makemigrations:
	@docker-compose run --rm app sh -c "python manage.py makemigrations"

migrate:
	@docker-compose run --rm app sh -c "python manage.py migrate"

createsuperuser:
	@docker-compose run --rm app sh -c "python manage.py createsuperuser"

shell:
	@docker-compose run --rm app sh -c "python manage.py shell"

