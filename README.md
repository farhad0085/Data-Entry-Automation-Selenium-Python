# Data Entry Automation - Selenium

This project is for automation the data entry using python and selenium. This application is capable to read a pdf file and then extract the table which includes the data you want to save to database. The automation is done with Selenium and Python.

## PIP COMMANDS
```
pip install selenium
pip install xlrd
pip install flask
pip install flask-wtf
```

## Procedure
1. Enable venv
	- open cmd and type `cd venv/scripts`
	- `activate`
2. Run following commands
	```
	cd ../..
	python
	from app import db
	db.create_all()
	exit()
	```
3. Run `python run.py`
4. Open another cmd and activate `venv` again
5. Run `python main.py`
6. Run `python submit.py`
6. Find resulted database at `app/info.db`
