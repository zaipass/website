pipeline {
    agent none
    stages {
        stage('Test-Build') { 
            agent {
                docker {
                    image 'python:3.7' 
                    args '--link=demo --network=website'
                }
            }
            steps {
                sh 'pip install -r requirements.txt' 
                sh 'python manage.py makemigrations'
                sh 'python manage.py migrate'
                sh 'python manage.py runserver'
            }
        }
    }
}