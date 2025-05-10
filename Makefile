run:
	python index.py

server_run:
	python server.py

clean:
	rm -rf __pycache__

install:
	pip install -r requirements.txt
