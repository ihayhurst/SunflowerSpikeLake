## Docker containers as template for flask application / API ##
#### Ian M. Hayhurst 2020 09 25 ####


Python 3.8.6 Flask with uWSGI Nginx in Docker. (using docker-compose)
Idea is to reuse base for different apps i.e. For API dev  infront of Oracledb or similar

- Database module in python (oracle_cx in here as folk seemed keen on it)
- Redis added but not tested with placeholder app
- Hot code reload the flask/app is copied into the container but then mounted over with volume from host filesystem, uWSGI will reload if touch_to_reload file is 'touched'

#### TODO ####
- add celery and code task in demo app
- add AJAX style checking with redis if task complete


### Drawn from the inspirational articles: ###
- cx_oracle on docker:  https://www.youtube.com/watch?v=_wab4By7P78
- https://www.docker.com/blog/containerized-python-development-part-2/
- Carlos Tighe: Apache, mod_wsgi, flask, docker:  https://github.com/carlostighe/apache-flask
- Ivan Panshin: Nginx, gunicorn, flask, docker:  https://towardsdatascience.com/how-to-deploy-ml-models-using-flask-gunicorn-nginx-docker-9b32055b3d0
- Julian Nash: Nginx, uWSGI, flask,  docker:  https://pythonise.com/series/learning-flask/building-a-flask-app-with-docker-compose
