VENV_BIN=pymuse-venv/bin/python


test:
	$(VENV_BIN) -m pytest .
