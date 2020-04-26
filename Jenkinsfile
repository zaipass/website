pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3-alpine' 
                }
            }
            steps {
                sh 'python manage.py makemigrations', 
                sh 'python manage.py migrate', 
                sh 'python manage.py runserver'
            }
        }
    }
}