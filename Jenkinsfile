pipeline {
    agent none 
    stages {
        stage('Test-MYSQL') { 
            agent {
                docker {
                    image 'mysql:v1' 
                    args '--name=db_web'
                    args '-p 3387:3306'
                }
            }
            steps {
                sh 'mysql -V' 
            }
        }
        stage('Test-Build') { 
            agent {
                docker {
                    image 'python:3.7' 
                    args '--link=db_web'
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