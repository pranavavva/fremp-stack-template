# FReMP Stack Template

The FReMP stack is a fullstack web framework comprising of **F**lask, **Re**act, **M**ongoDB, and **P**ython 

- Frontend
    - React (TypeScript)
    - Redux (TypeScript) via Redux Toolkit
    - Axios (for HTTP requests)
    - Yarn (package manager)
- Backend
    - Python
    - Flask
    - Flask ReSTful
    - Flask MongoEngine
    - pipenv (package manager + virtual environment)
- Database
    - MongoDB

## Developement

To get started with development, follow the instructions below:

### Frontend

```bash
$ cd frontend
$ yarn install
$ yarn start
```

### Backend

```bash
$ cd backend
$ pipenv install
$ pipenv run flask run --no-debugger # debugger not needed since we are only serving an API
```

### MongoDB

Configure your database connection in `backend/.env`. This `.env` file should _not_ be checked in to version control. The sample file (`.env.sample`) assumes you have a local MongoDB instance running on `mongodb://localhost:271017/` and accessing the `test` database. `.env` files should be used in development only. The API server `backend/wsgi.py` will look for environment variables named the following for MongoDB connection configuration:

- `MONGODB_DB` - Database name
- `MONGODB_HOST`
- `MONGODB_PORT`
- `MONGODB_USERNAME`
- `MONGODB_PASSWORD`

Of these 5 environment variables, only the first three are required.

## Deployment

There are many ways to deploy a FReMP-stack web application. This stack aims to be unopinionated in terms of deployment choices. Regardless of the hosting solution (DigitalOcean, Heroku, AWS, etc.), the build steps are essentially the same. However, this does assume that you have configured the MongoDB connection environment variables (described above) as application secrets or otherwise provide them to the app via environment variables. _Remember, you should not check in `.env` to version control._


```bash
# build the frontend (React app)
$ cd frontend
$ yarn build

# serve the backend using gunicorn
$ cd ../backend
$ gunicorn wsgi:app # configure ports using `-b <host port>:<app port>` and temp dir using `--worker-tmp-dir /path/to/tmp/dir` as needed
```
