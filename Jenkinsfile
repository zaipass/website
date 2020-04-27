pipeline {
    agent {
        node {
            checkout scm
            docker.image('mysql:v1').withRun('-e "MYSQL_ROOT_PASSWORD=mysql" -p 3387:3306') { c ->
                docker.image('mysql:v1').inside("--link ${c.id}:db") {
                    /* Wait until mysql service is up */
                    sh 'while ! mysqladmin ping -hdb --silent; do sleep 1; done'
                }
                docker.image('python:3.7').inside("--link ${c.id}:db") {
                    /*
                     * Run some tests which require MySQL, and assume that it is
                     * available on the host name `db`
                     */
                    sh 'pip install -r requirements.txt' 
                    sh 'python manage.py makemigrations'
                    sh 'python manage.py migrate'
                    sh 'python manage.py runserver'
                }
            }
        } 
    } 
    
    // 
    // stages {
    //     stage('Test-MYSQL') { 
    //         agent {
    //             docker {
    //                 image 'mysql:v1' 
    //                 args '-name db_web'
    //                 args '-p 3387:3306'
    //             }
    //         }
    //         steps {
    //             sh 'mysql -V' 
    //         }
    //     }
    //     stage('Test-Build') { 
    //         agent {
    //             docker {
    //                 image 'python:3.7' 
    //                 args '-link db_web'
    //             }
    //         }
    //         steps {
    //             sh 'pip install -r requirements.txt' 
    //             sh 'python manage.py makemigrations'
    //             sh 'python manage.py migrate'
    //             sh 'python manage.py runserver'
    //         }
    //     }
    // }
}