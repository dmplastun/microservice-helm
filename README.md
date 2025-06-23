# 🧪 Микросервисное приложение на Kubernetes с Helm

Этот проект демонстрирует развертывание двух микросервисов (Node.js и Python API) в Minikube с использованием Helm и автоматизацией через GitHub Actions.

## 🛠 Основные технологии

- **Kubernetes** — оркестрация контейнеров  
- **Minikube** — локальный кластер Kubernetes  
- **Helm** — управление пакетами в Kubernetes  
- **Docker** — контейнеризация сервисов  
- **GitHub Actions** — автоматизация CI/CD  

## 📦 Структура проекта
```
.
├── nodejs-microservice/     # Node.js микросервис
├── python-api/              # Python Flask API
├── my-microservice-app/     # Helm чарт
└── .github/workflows/deploy.yml # CI/CD через GitHub Actions
```

## 🚀 Локальный запуск (для тестирования)

### 1. Установите зависимости

```bash
sudo apt update
sudo apt install -y docker.io kubectl minikube helm
```
### 2. Запустите Minikube
```bash
minikube start --driver=docker --container-runtime=docker
```
### 3. Соберите образы
```bash
cd nodejs-microservice
docker build -t nodejs-microservice:latest .
cd ..

cd python-api
docker build -t python-microservice:latest .
cd ..
```
### 4. Переключись на Docker Minikube и загрузи образы
```bash
eval $(minikube docker-env)
docker images | grep microservice
```
### 5. Разверните через Helm
```bash
cd my-microservice-app
helm dependency update
helm install my-release .
```
### 6. Проверьте работу
```bash
kubectl get pods
kubectl get services
```
### Откройте в браузере:
```bash
minikube service nodejs-service
minikube service python-service
```
## 🤖 CI/CD через GitHub Actions 

При каждом пуше в ветку main, будет выполняться: 

    Установка зависимостей
    Запуск Minikube
    Сборка Docker-образов
    Деплой через Helm
     

Файл: .github/workflows/deploy.yml 

## 🙌 Автор 

<p>🪪 dmplastun</p>
<p>📧 dmitrij.plastun@gmail.com</p> 
<p>🔗 https://github.com/dmplastun/microservice-helm</p>
