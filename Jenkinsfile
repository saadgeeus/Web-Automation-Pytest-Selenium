pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/saadgeeus/Web-Automation-Pytest-Selenium.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --html=reports/test_report.html --self-contained-html'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'reports/test_report.html', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}
