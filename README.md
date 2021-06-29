# ShortMe (Node technologies task)
## _simple url shortner_
create shorten URLs using shortme django based project

## Required modules
- virtualenv
- Django
- Django Rest framework
- rest-framework-swagger

thats all for installing  

## Installation


Install the dependencies.

```sh
pip install virtualenv django==2.2.14 djangorestframework rest-framework-swagger
```

## Setup project on local


clone project from github.
```sh
https://github.com/shivagangula/shortme.git
```
go main project directory
```sh
cd shortme
```
start makemigrations, migrate, createsuperuser
```sh
python manage.py makemigrtions
python manage.py migrate
python manage.py createsuperuser
```
now start django server

```sh
python manage.py runserver
```
```sh
http://127.0.0.1:8000/
```

use can see swagger ui after hitting


#### Using Shortme API
In swagger UI you can see one post endpoint
```sh
http://127.0.0.1:8000/api/v1/csu/
```
after hitting endpoint in browser or swagger UI. you should provied original/long url as parameter with json format like
```sh
{"original_url":"http://www.google.com"}
```
Note : `you must provied absoulte url` example: 
`www.google.com is not valid.`
`https://www.google.com is vaild `

after posting it will return shortner url like
```sh
http://127.0.0.1:8000/Gtdsg5
```
copy nd past it in browser it will redirect to original url



## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
