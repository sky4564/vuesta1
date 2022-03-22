# vuesta1

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## server setup

### step1 백엔트 프로젝트 폴더로 이동
```
cd backend
```

### step2 가상환경 진입 후 최신화를 합니다 (pull 받고 npm install 하는것처럼) 
```
pipenv shell

pipenv install
```

### step3 sqlite 장착시기키 db(sqlite3)와 장고앱을 연결합니다. (step2와 같은 맥락임)
```
python manage.py makemigrations

python manage.py. migrate
```

### step4 서버를 실행합니다.
```
python manage.py runserver
```
