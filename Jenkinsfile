pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        sh '''echo "pylint --rcfile=pylint.conf base"
echo Unit Testing...'''
      }
    }

    stage('Build') {
      steps {
        sh '''mkdir django
mv $(ls --ignore=django --ignore=nginx_dockerfile --ignore=django_dockerfile) django
cd django
tar -zcvf Django.tar.gz ./*
cp Django.tar.gz ../django_dockerfile
cd ../django_dockerfile
echo docker build -t django:v1 .
cd ../nginx_dockerfile
echo docker build -t nginx:v1 .'''
      }
    }

    stage('Clean') {
      steps {
        sh '''rm -rf ./*
echo docker builder prune -f'''
      }
    }

  }
}