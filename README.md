# 📚 Book Catalog API

## 🔍 Project Overview
This project is a RESTful Book Catalog API developed as part of the DevOps Diploma Capstone Assignment. The application allows users to create, read, update, and delete books. The backend is built using Django REST Framework, containerized using Docker, and deployed on Kubernetes via Helm. CI/CD is handled through GitHub Actions.

---

## 🔗 API Usage Examples

### Base URL:
```
http://localhost:8000/api/books/
```

### Endpoints:
| Method | URL | Description |
|--------|-----|-------------|
| GET | /api/books/ | List all books |
| POST | /api/books/ | Create a new book |
| GET | /api/books/{id}/ | Retrieve a specific book |
| PUT | /api/books/{id}/ | Update a book |
| PATCH | /api/books/{id}/ | Partially update a book |
| DELETE | /api/books/{id}/ | Delete a book |

### Example JSON for POST:
```json
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "isbn": "9780132350884",
  "published_date": "2008-08-01"
}
```

---

## 🛠 Local Build and Run Instructions

### 1. Clone the Repository:
```bash
git clone https://github.com/yourusername/book-catalog-api.git
cd book-catalog-api
```

### 2. Set up Virtual Environment (Optional):
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the Server:
```bash
python manage.py migrate
python manage.py runserver
```

---

## 🐳 Docker Instructions

### Build and Run Docker Locally:
```bash
docker-compose up --build
```

### Apply Migrations in Container:
```bash
docker-compose exec web python manage.py migrate
```

---

## 🤖 CI/CD Pipeline (GitHub Actions)

- The workflow is triggered on every push to `main`
- It performs the following steps:
  - Install Python and dependencies
  - Run Django unit tests
  - Log in to Docker Hub
  - Build and push Docker image
  - Configure kubectl and helm
  - Deploy the image to Kubernetes using Helm

### Secrets Used:
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`
- `DOCKER_IMAGE_NAME`
- `KUBE_CONFIG_DATA`

---

## ☸️ Kubernetes and Helm Setup Instructions

### Helm Chart Structure:
```
helm/
  Chart.yaml
  values.yaml
  templates/
    deployment.yaml
    service.yaml
    ingress.yaml (optional)
```

### Manual Deployment (Local Docker Desktop Kubernetes):
```bash
helm upgrade --install book-catalog ./helm ^
  --set image.repository=yourdockerhub/book-catalog ^
  --set image.tag=latest
```

### Accessing Locally:
```bash
kubectl port-forward svc/book-catalog 8000:8000
```
Visit: http://localhost:8000/api/books/