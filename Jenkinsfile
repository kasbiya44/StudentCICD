
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker --version'
                bat 'docker build -t student-management:1.0 .'
            }
        }

        stage('Deploy with Ansible') {
            steps {
                bat 'wsl -d Ubuntu -- ansible-playbook /home/kasbi/student-cicd/deploy.yml'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'docker ps'
            }
        }
    }
}
