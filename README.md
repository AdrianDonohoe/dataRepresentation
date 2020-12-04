# Data Representation Project 2020
***

This repository contains my submission for the data representation module main project.

## US Presidential Election Results 2020 Python Flask App, with MySQL Database

This web application is a page that displays the an interactive map of the United States. Clicking on each individual state brings up a modal with the election results for that state. From this modal you can click the update button and change the election result through an update form. 

This will trigger an AJAX call to the server which will update the database with the new result. After the update, the app will return you to the main page and update the map.

The database object uses a connection pool to help stability of interactions to the MySQL database, although pythonanywhere does limit connections. The connection pool is configured for two connections due to the aforementioned limitation with python anywhere but this can be easily increased in a local version of the app.

The app can be run locally by downloading the repository and initialising the database with the create_db.sql and init_db_tables.sql.

Or it can be found hosted on my pythonanywhere site : [aidodo.pythonanywhere.com](http://aidodo.pythonanywhere.com/)


The web application is comprised of a Python Flask REST server (restserver.py), a MySQL DB Object (StatesDAO.py), a HTML frontend page (index.html).

This repository also contains scripts for making the database (create_db.sql and init_db.sql), a python requirements text file  (requirements.txt) and a script (nyt_scraper.py) for scraping election results from the [New York Times election website](https://www.nytimes.com/interactive/2020/11/03/us/elections/results-president.html)

## Installing the app locally

1.  Download the app from this repository.

2.  (Optional) Create a virtual environment for the app.

    $ python -m venv venv

    Activate the venv

    $ source venv/bin/activate

3. Install the requirements

    $ pip install -r requirements.txt

4. Create and populate the database using scripts

    $ mysql -u'your_username' -p < create_db.sql

    $ mysql -u'your_username' -p < init_db.sql

5. Start the REST server

    $ python server/restserver.py

6. Using browser open http://127.0.0.1:5000/




