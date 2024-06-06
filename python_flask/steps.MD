## Steps


Install virtualenv
```
pip install virtualenv

```

Create virtual environment.
```
python -m venv venv

```

```
source venv/bin/activate
```


```
. .venv/bin/activate
```

```
deactivate
```


```
pip install Flask
```

```
flask --app server run
```

<!-- Build the blog -->

Created templates folder to hold html templates.
Created static folder to hold static files (styles, images, etc). 
Added css to html file using 
`href="{{ url_for('static', filename= style.css')`
Add images
`src="{{ url_for('static', filename='home.jpg' ) }}`

To create


<!-- Database -->

Using sqllite because it's part of the standard library. 

Created schema.sql file and script init_db.py 

`python init_db.py`

This creates database.db