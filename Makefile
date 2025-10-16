inicializar_ambiente:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt

executar_teste:
	.venv/bin/python teste.py

executar_terminal:
	.venv/bin/python -i -c "import buchberger"
