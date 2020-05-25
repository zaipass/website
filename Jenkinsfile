pipeline {
    agent none
    triggers {
        pollSCM('H/1 * * * *')
    }
    environment {
        ENV_WEBSITE = '/root/env'
    }
    stages {
        stage('Test-Build') {
            agent {
                docker {
                    image 'python:3.7'
                    args '--link=demo --network=website -p 8088:8000 -dit --name=web_demo'
                }
            }
            steps {
                sh 'echo "what"'
                // sh 'pip install -r requirements.txt'
                // sh 'python manage.py makemigrations'
                // sh 'python manage.py migrate'
                // sh 'uwsgi --ini /home/Documents/GitHub/website/uwsgi.ini'
            }
        }
        stage('Push-Build') {
            agent any
            steps {
                sh '''
                    virtualenv ${ENV_WEBSITE}/website
                    source ${ENV_WEBSITE}/website/bin/activate
                    pip install -r requirements.txt
                    uwsgi --ini uwsgi.ini
                    echo "success"
                '''
                // rm -rf ${ENV_WEBSITE}/website
                //
                // uwsgi --ini /home/Documents/GitHub/website/uwsgi.ini
            }
        }
    }
}
