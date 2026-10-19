# conduit-realworld-automation-framework
Automation framework API integrations, backend + frontend, DB (Python, Pytest, Playwright, Allure)

Building docker container conduit-db
- docker build -f DockerFile.postgresql -t postgresql-conduit-db .

Running docker container conduit-db
- docker run -d --name conduit-db -p 5432:5432 postgresql-conduit-db
