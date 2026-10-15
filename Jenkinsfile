
pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker --version'
                bat 'docker build -t student-management:1.0 .'
            }
        }

        stage('Deploy Application') {
            steps {
                bat 'docker rm -f student-management-app 2>NUL || ver >NUL'
                bat 'docker run -d --name student-management-app -p 5000:5000 student-management:1.0'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'docker ps'
            }
        }
    }
}
