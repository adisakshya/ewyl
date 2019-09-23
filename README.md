# CloudSEK EWYL

This repository contain my solution to challenge 1 of CloudSEK Earn While You Learn (EWYL) Program

## Directory Structure

```
.
├── ./web_app
│   ├── .web_app/application.py
│   ├── .web_app/datastore
│   │   └── .web_app/datastore/__init__.py
│   │   └── .web_app/datastore/create_datastore.py
│   │   └── .web_app/datastore/store_loader.py
│   │   └── .web_app/datastore/store
│   │       ├── .web_app/datastore/store/bus_data.json
│   │       └── .web_app/datastore/store/data.json
│   ├── .web_app/static
│   │   └── .web_app/static/css
│   │       └── .web_app/static/css/styles.css
│   ├── .web_app/templates
│   └   └── .web_app/templates/index.html
├── ./CLI
│   ├── .CLI/setup.py
│   ├── .CLI/datastore
│   │   └── .CLI/datastore/__init__.py
│   │   └── .CLI/datastore/create_datastore.py
│   │   └── .CLI/datastore/store_loader.py
│   │   └── .CLI/datastore/store
│   │       └── .CLI/datastore/store/bus_data.json
│   │       └── .CLI/datastore/store/data.json
│   ├── .CLI/bin
│   └   └── .CLI/bin/vts_live_cli.py
├── ./requirements.txt
├── ./runtime.txt
├── ./README.md
├── ./LICENSE
└── ./.gitignore
```

Web Application
- ```/web_app``` is the directory containing the web application.
  - ```/web_app/application.py``` is the main server file.
  - ```/web_app/datastore``` directory contain the utilities to manipulate the JSON response from [vtslive.in/nst](http://vtslive.in/nist/getMobilityData.php?L=smartgreencampus@nist&P=smart@nist).
    - ```/web_app/datastore/store``` has 2 JSON files.
      - ```/web_app/datastore/store/data.json``` is the raw response from [vtslive.in/nst](http://vtslive.in/nist/getMobilityData.php?L=smartgreencampus@nist&P=smart@nist).
      - ```/web_app/datastore/store/bus_data.json``` is the manipulated form of data.json.
    - ```/web_app/datastore/create_datastore.py``` reads raw response in data.json and creates the manipulated JSON file bus_data.json.
    - ```/web_app/datastore/store_loader.py``` acts as an interface between datastore and web application and is responsible for making the JSON data available for various functions.
  - ```/web_app/static/css``` holds the static css files.
  - ```/web_app/templates``` directory contain the HTML file for landing page.
  
Command Line Application
- ```/CLI``` is the directory containing the command line application.
  - ```/CLI/setup.py``` is the main setup file that installs the application.
  - ```/CLI/datastore``` directory contain the utilities to manipulate the JSON response from [vtslive.in/nst](http://vtslive.in/nist/getMobilityData.php?L=smartgreencampus@nist&P=smart@nist).
    - ```/CLI/datastore/store``` has 2 JSON files.
      - ```/CLI/datastore/store/data.json``` is the raw response from [vtslive.in/nst](http://vtslive.in/nist/getMobilityData.php?L=smartgreencampus@nist&P=smart@nist).
      - ```/CLI/datastore/store/bus_data.json``` is the manipulated form of data.json.
    - ```/CLI/datastore/create_datastore.py``` reads raw response in data.json and creates the manipulated JSON file bus_data.json.
    - ```/CLI/datastore/store_loader.py``` acts as an interface between datastore and web application and is responsible for making the JSON data available for various functions.
  - ```/CLI/bin``` holds all the executable scripts.
    - ```/CLI/bin/vts_live_cli.py``` script is the main application file.

## External Dependencies
```
- Click (for command line application)
- Flask (for web application)
- Reverse-Geo-Coder (for reverse geo coding)
```

## Cloning the repository

Run the following command to clone this repository and get into root directory
```
$ git clone https://github.com/adisakshya/ewyl.git && cd ewyl
```

## Setting up environment

Create and activate a virtual environment by running
```
$ virtualenv venv
$ source venv/Scripts/activate
```

## Execution Instructions

### Web Application

#### Step 1:

Get into web application directory by running following command on terminal/bash
```
$ cd web_app
```

#### Step 2:

Install requirements by running following command
```
$ pip install -r requirements.txt
```

#### Step 3: (Optional - as datastore is already created, cached from  [vtslive.in/nst](http://vtslive.in/nist/getMobilityData.php?L=smartgreencampus@nist&P=smart@nist))

Create datastore by running following commands
```
$ cd datastore
$ py create_datastore.py
```

#### Step 4:

Run the web application by
```
$ py application.py
```
Now the web application will be running on ```localhost``` on PORT 5000, in debug mode !

### Command Line Application

#### Step 1:

Get into CLI directory by running following command on terminal/bash
```
$ cd CLI
```

#### Step 2:

Install requirements by running following command
```
$ pip install -r requirements.txt
```

#### Step 3: (Optional - as datastore is already created, cached from  [vtslive.in/nst](http://vtslive.in/nist/getMobilityData.php?L=smartgreencampus@nist&P=smart@nist))

Create datastore by running following commands
```
$ cd datastore
$ py create_datastore.py
```

#### Step 4:

Install the command line application by
```
$ py setup.py install
```
Now the command line application is installed

#### Step 5:

Use command line application by commands following the below pattern
```
vts_live_cli.py <BUS_NUMBER>
```
This will return the bus details.
