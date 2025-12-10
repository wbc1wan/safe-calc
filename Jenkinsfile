pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Check Python') {
            steps {
                sh '''
                python3 --version
                pip3 --version
                '''
            }
        }

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/wbc1wan/my_calculator.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                python3 -m venv ${VENV_DIR}
                ${VENV_DIR}/bin/pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                if [ -f requirements.txt ]; then
                    ${VENV_DIR}/bin/pip install -r requirements.txt
                fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                ${VENV_DIR}/bin/pip install pytest pytest-cov junit-xml
                ${VENV_DIR}/bin/pytest --junitxml=results.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'results.xml'
            echo 'Pipeline finished.'
        }
    }
}
