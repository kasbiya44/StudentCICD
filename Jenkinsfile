
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
        	 bat 'schtasks /Run /TN "\\StudentCICD-Ansible"'
        	 bat 'timeout /t 10 /nobreak'
        	 bat 'powershell -NoProfile -Command "if ((Get-ScheduledTaskInfo -			 TaskName StudentCICD-Ansible).LastTaskResult -ne 0) { exit 1 }"'
            }
        }
       
        stage('Verify Deployment') {
            steps {
                bat 'docker ps'
            }
        }
    }
}
