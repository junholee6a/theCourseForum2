
# theCourseForum2
[![Build Status](https://travis-ci.com/thecourseforum/theCourseForum2.svg?branch=master)](https://travis-ci.com/thecourseforum/theCourseForum2)

2020 Django rewrite of theCourseForum website

[Staging](http://thecourseforum-staging.herokuapp.com/) | [Dev](http://thecourseforum-dev.herokuapp.com/)

# MacOS and Linux Setup
1. Install git, docker, and docker-compose
    - https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
    - https://docs.docker.com/install/
    - https://docs.docker.com/compose/install/
2. `git clone https://github.com/thecourseforum/theCourseForum2.git`
3. Go into the `theCourseForum2/` folder and then run these commands to start your Docker container:
    - *`cp .env.example .env`
    - `docker build .`
    - `docker-compose up`
4. Download a copy of the database from https://drive.google.com/open?id=1ubiiOj-jfzoBKaMK6pFEkFXdSqMuD-22
    - put this into the `theCourseForum2/` folder
5. While your container is still running, open a second terminal, cd into `theCourseForum2/`, and run the following command to set up your database (you may need to run it 3 times)*:
    - *`cat april7.sql | docker exec -i tcf_db psql -U tcf_django tcf_db`
6. Go to http://localhost:8000 and make sure it works!

\*This method can also work if you have a version of Windows that is supported by Docker Desktop — i.e. Windows 10 Pro, Enterprise, or Education, but NOT Home (the most common version). However, you'll have to run `cp` and `cat` in a bash shell (ex. Powershell) because those commands don't exist in CMD.

# Alternative Setup (Windows and MacOS if above failed)
0. [Install Vagrant](https://www.vagrantup.com/intro/getting-started/install.html)
1. `git clone https://github.com/thecourseforum/theCourseForum2.git`
2. Go into the `theCourseForum2/` folder and then run `vagrant up` to start a VM.
3. After that's booted, run `vagrant ssh` to run commands inside the VM.
4. `cd /vagrant`
5. Start at step 3 in normal setup. You may have to prefix all docker commands with `sudo` (e.g. `sudo docker-compose up`).
6. Go to http://127.0.0.1:8000 and make sure it works!
7. Run `vagrant` suspend when you're done to suspend the VM.

# Design Philosophies
- Thick models, thin views, thinner templates
    - most application logic should be in methods on model classes.
        - this ensures that the code can be reused easily anywhere the model is used and is way easier to test.
    - furthermore, you should avoid placing logic in templates.
        - e.g. don't filter lists in templates, filter them in the views.

# How to Contribute
1. Create a new branch to do your work in off of the `dev` branch.
    - `git pull`
    - `git checkout dev`
    - `git checkout -B your_branch_name`
2. Make your changes!
3. Write unit tests and put them in `tcf_website/tests/`
4. Lint and test locally before commit:
    - `./precommit`
    - Fix any problems indicated by tests or pylint.
4. Stage your changes with `git add .`
5. Commit with `git commit -m "Add X feature."`
6. Push! `git push`
7. Make a Pull Request to merge your changes back into `dev`.
8. Wait for all tests to pass.
9. Request an approver.
10. Wait to be approved and merged!

# Data migration plan from tCF 1.0 (total downtime: 2.5 hours)
1. Get latest copy of legacy db using `mysqldump` from DO instance.
2. Convert to sqlite using `legacy_db/mysql2sqlite`
    - Then put in `settings.py` as database `legacy`
3. `docker exec -it tcf_django bash` and then `python manage.py migrate_legacy_subdepartments`
4. `python manage.py load_all_semesters`
5. `python manage.py migrate_legacy_reviews`
6. `docker exec tcf_db pg_dump -U tcf_django -Fc tcf_db > dump.pgsql`
7. Test
    - Maybe crawl tCF and check that all viewable reviews are on the new system.
8. Upload to DigitalOcean DB.
    - `PGPASSWORD=$DB_PASS pg_restore -U $DB_USER -h $DB_HOST -p 25060 -d $DB_NAME < dump.pgsql`
    - You may have to run this command 3 times.

# New semester update plan
1. `python manage.py update_semester 2021 january`
    - fetches CSV from lous list
    - loads section data into database
        - update courses with new course info if available
        - create new instructors if needed

# TODO: Deploying to prod
- https://docs.djangoproject.com/en/3.0/howto/deployment/
