# Flaskerizer

## What is the Flaskerizer and what problem does it solve?

Bootstrap templates from websites like https://bootstrapmade.com/ are a fast way to get very dynamic website up and running, but bootstap templates typically don't work "out of the box" with the python web framework Flask and require some tedious directory building and broken link fixing before being functional with Flask. This is especially true if the bootstrap templates are for large multi-page websites. 

The Flaskerizer automates the necessary directory building and link creation needed to make Bootstrap templates work "out of the box" with Flask. The Flaskerizer also automatically creates a python script with the appropriate routes and basic error handling needed to serve the bootstrap template as a Flask app.

The Flaskerizer takes a bootstrap template that looks like this "out of the box" with Flask:

![picture alt](/readme_images/not_working_example.png)

and converts it to something that looks like this "out of the box" with Flask:

![picture alt](/readme_images/working_example.png)

## Dependencies

Flask: 0.12.1 or higher

## Setup and Operation

1. Clone the repo to your computer
2. Install dependencies by opening a terminal in top level directory of the repo and entering `$ pip install -r requirements.txt` 
3. Download your favorite bootstrap template from https://bootstrapmade.com/ .Note that there are two example templates in the repo (Folio_example and Sailor_example) from https://bootstrapmade.com/ that you can use if you don't want to download one. This program was designed only with templates from https://bootstrapmade.com/ in mind, but I would love to extend the flexibility of the program to work well with other bootstrap template sources (see issues) 
4. Open flaskerizer.py and edit the 'directory' argument of the 'structure_directory_object' to include the full path to the bootstrap template you downloaded (or the example one in the repo).
5. Run the program by opening a terminal in the top level directory of the repo and entering `$ python app.py` (this may vary slightly by environment)
6. View your website by opening the browser to your local address on port 5000 (i.e. http://127.0.0.1:5000) , Note: may have to enter http://127.0.0.1:5000/index.html to route to  website homepage.
7. You may need to clear your browser's cache to view the website properly

## How it works

The Flasker has two main classes:
* `StructureDirectory()`

* `WriteApp()`

**The StructureDirectory class**

The StructureDirectory class makes the typical Flask project folder structure in the top level directory of the repo. This includes making a 'static' folder that will contain all the front end files from the bootstrap template (css, javascript, etc.) and a 'templates' folder that will contain all the HTML files from the bootstrap template. The StructureDirectory class takes the directory of the bootstrap template as an argument. 

The StructureDirectory class has two main methods:

`migrate_static`:

The migrate_static method creates a 'static' folder in the top level directory of the repo. All the folders from the bootstrap template directory will be copied to the newly made 'static' folder in the top level directory of the repo. The assumption is made that all folders in the bootstrap template contain the front end information that belongs in the 'static' folder like css, javascript, images, etc. This may not always be the case, but I think often it is. 

`parse_html`:

The parse_html method creates a 'templates' folder in the top level directory of the repo. The string content of all the HTML files in the top level directory of the bootstrap template then parsed for any links that references the content placed in the 'static' folder by the migrate_static method. If any links are found, they are modified to reflect the correct structure of the Flask application. This avoids broken links that would otherwise incorrectly reference files in the 'static' folder. Once the HTML files are parsed and corrected, they are written to the newly made 'templates' folder in the top level directory of the repo. 

**The WriteApp class**


The WriteApp class has one main method:

`write_app`:

The write_app method automatically writes a python script 'app.py' with the necessary instructions to launch a Flask app of the bootstrap template. This method writes the import statements, instantiates the 'app' object from the Flask class, and writes a main loop to run the app. This method also detects the HTML files in the 'templates' folder and writes the corresponding routes to these HTML files. If any of the HTML files are named for an HTTP status code, the write_app method generates an error handling route for that file. This assumes that any HTML file with an HTTP status code in it's name reflects an error, which I think is usually true. 

## Running the tests

Tests have been written for the StructureDirectory and WriteApp classes. 

**To run the tests for StructureDirectory:** 

open a terminal in the top level directory of the repo and enter `$ python test_structure_directory.py` (this may vary slightly by environment)

**To run the tests for test_write_app.py:** 

open a terminal in the top level directory of the repo and enter `$ python test_write_app.py` (this may vary slightly by environment)

I am aware that test_structure_directory.py is not currently passing, please see issues. 







