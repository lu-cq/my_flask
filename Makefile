WITH_ENV = env `cat .env 2>/dev/null | xargs`


COMMANDS = help clean install-deps lint docs docs-force
.PHONY: $(COMMANDS)

help:
	@echo "commands: $(COMMANDS)"

shell:
	@$(WITH_ENV) ipython manage.py shell

init:
	@$(WITH_ENV) python manage.py db init

migrate:
	@$(WITH_ENV) python manage.py db migrate

upgrade:
	@$(WITH_ENV) python manage.py db upgrade

downgrade:
	@$(WITH_ENV) python manage.py db downgrade

start:
	@$(WITH_ENV) honcho start
