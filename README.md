# conduit-realworld-automation-framework
Automation framework API integrations, backend + frontend, DB (Python, Pytest, Playwright, Allure)

### 1. Database Postgresql service

   Building docker postgresql database image postgresql-conduit-db
- docker build -f DockerFile.postgresql -t postgresql-conduit-db .

 Running docker container conduit-db
- docker run -d --name conduit-db -p 5432:5432 postgresql-conduit-db

### 2. Isolated conduit app with sqlite

   Building docker isolated sqlite conduit app image sqlite-realworld-conduit-app
- docker build -f DockerFile.sqlite-realworld-conduit-app -t sqlite-realworld-conduit-app .

 Running docker docker isolated sqlite conduit app
- docker run -d --name sqlite-conduit-app -p 3000:3000 -p 3001:3001 sqlite-realworld-conduit-app
