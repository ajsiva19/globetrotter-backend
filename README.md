# 🚀 globetrotter backend development

## 🚀 Running the Code Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/../l...git
   cd ..
   ```
2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **give .env variable**:
   ```bash
    POSTGRES_HOST=localhost
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_PORT=5432
    POSTGRES_DB=postgres
   ```

4. **Run the application**:
   ```bash
   uvicorn app.app:app --reload
   ```
5. **Access the API**:
   ```link
   http://localhost:8000/docs
   ```