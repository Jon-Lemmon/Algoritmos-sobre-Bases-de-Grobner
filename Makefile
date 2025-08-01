inicializar_ambiente:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt

executar:
	.venv/bin/python main.py
