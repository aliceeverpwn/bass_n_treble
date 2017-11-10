[![Build Status][travis-img]][travis-url]
[![Coverage Status][coverall-img]][coverall-url]
[![Weppy Version](https://img.shields.io/badge/weppy-1.2.6-blue.svg)](https://github.com/gi0baro/weppy)


# Base N Treble
 
A [Weppy](http://weppy.org) application.

My first music jukebox server

## Run

**Requirements**:
- Python 3.6.1+

For virtualenv setup and activation:

```
virtualenv --python=$(which python3.6) env
. ./env/bin/activate
pip install -r requirements.txt
python run.py
```

Otherwise:

```
pip install -r requirements.txt
python run.py
```

***If pip fails on ubuntu, try `sudo apt-get install libyaml-dev libyaml-python3.6-dev`**

### Docker

To make your application available at ```http://localhost/```:

```
docker build -t base_n_treble .
docker run -it -p 80:8000 --rm --name base_n_treble base_n_treble
```


## Develop

Running in development mode will enable debug pages and
automatically create test users in multiple states.
Test users will be removed from the DB after stopping.

To start the app in development mode, do:

```
python run.py --dev
```

See ```base_n_treble/cli.py``` for cli commands. 

## Test

```
py.test -v -s --cov-report term-missing --cov=base_n_treble -r w tests
```


## License

[MIT](LICENSE) 2017 aliceeverpwn


[travis-img]: https://travis-ci.org/aliceeverpwn/base_n_treble.svg?branch=master
[travis-url]: https://travis-ci.org/aliceeverpwn/base_n_treble
[coverall-img]: https://coveralls.io/repos/github/aliceeverpwn/base_n_treble/badge.svg?branch=master
[coverall-url]: https://coveralls.io/github/aliceeverpwn/base_n_treble?branch=master
