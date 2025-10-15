pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Manthan-Kansagara/python-jenkins-practicals.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                bat "${env.PYTHON} -m pip install --upgrade pip"
                bat "${env.PYTHON} -m pip install -r requirements.txt"
                bat "${env.PYTHON} -m pip install pytest"
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                bat "${env.PYTHON} -m pytest --junitxml=report.xml"
            }
        }
    }

    post {
        always {
            echo 'Publishing test results...'
            junit '**/report.xml'
        }
    }
}
