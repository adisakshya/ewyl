# CloudSEK EWYL

This repository cintain my solution to the CloudSEK Earn While You Learn (EWYL) Program

## Directory Structure

```
.
├── ./web_app
│   ├── .application.py
│   ├── .datastore/
│   │   └── .__init__.py
│   │   └── .create_datastore.py
│   │   └── .store_loader.py
│   │   └── .store/
│   │       ├── .bus_data.json
│   │       └── .data.json
│   ├── .static/
│   │   └── .css/
│   │       └── .styles.css
│   ├── .templates/
│   └   └── .index.html
├── ./CLI
│   ├── .setup.py
│   ├── .datastore/
│   │   └── .__init__.py
│   │   └── .create_datastore.py
│   │   └── .store_loader.py
│   │   └── .store/
│   │       └── .bus_data.json
│   │       └── .data.json
│   ├── .bin/
│   └   └── .vts_live_cli.py
├── ./requirements.txt
├── ./runtime.txt
├── ./README.md
├── ./LICENSE
└── ./.gitignore
```

## Cloning the repository

Run the following command to clone this repository and get into root directory
```
$ git clone https://github.com/adisakshya/ewyl.git && cd ewyl
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
