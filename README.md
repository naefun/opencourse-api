# opencourse-api
API for opencourse-api project

## To deploy locally:
### 1. Install requirements:  
- docker
- python3
- pipenv
```
pip install pipenv
```

### 2. Install dependencies
```
pipenv install
```

### 3. Deploy the mongo containers
```
docker-compose up
```

### 4. Deploy the api
```
./dev-bootstrap.sh
```
