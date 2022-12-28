pipeline {
    agent any

    stages {
        stage('preinstall') {
            steps {
                echo 'staring the install process'
                sh "sudo apt-get update"
            }
        }
    
        stage('install') {
            steps {
                sh "sudo apt-get install -y apache2"
            }
        }

        stage('copyfiles') {
            steps {
                sh "sudo cp -r * /var/www/html"
                echo 'hello world'
                
            }
        }
    }
}
