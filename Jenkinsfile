pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout source code from SCM / Git
                checkout scm
            }
        }

        stage('Automated HTML Form Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m unittest test_form.py'
                    } else {
                        bat 'python -m unittest test_form.py'
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline run completed."
        }
        success {
            echo "All HTML form validation tests passed successfully!"
        }
        failure {
            echo "Validation tests failed. Required form fields are missing or invalid."
        }
    }
}
