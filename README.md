git clone https://github.com/aahadrahi/hhc.git

python -m venv hhcenv

source hhcenv/bin/activate

cd ..

cd hhc

pip install -r requirements.txt 

<!-- sudo apt-get install gdal-bin -->
python3 manage.py runserver

<!-- python manage.py migrate --run-syncdb -->
