FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel --no-cache-dir
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]



# FROM python:3.11-slim-bookworm

# # Set working directory
# WORKDIR /app

# # Install only required system packages (update libc included)
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends libc6 libc-bin && \
#     rm -rf /var/lib/apt/lists/*

# # Copy dependencies first for caching
# COPY requirements.txt .

# # Upgrade pip and install Python packages
# RUN pip install --upgrade pip setuptools wheel --no-cache-dir && \
#     pip install --no-cache-dir -r requirements.txt

# # Copy project files
# COPY . .

# # Expose port and start app
# EXPOSE 8000
# CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]



# FROM python:3.11-slim
# RUN apt-get update && apt-get upgrade -y
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .
# EXPOSE 8000
# CMD ["uvicorn", "backend.main:app" , "--host","0.0.0.0","--port","8000"] 








# # -------- Stage 1: Builder --------
# FROM python:3.11.8-slim AS builder

# WORKDIR /app
# RUN pip install --upgrade jaraco.context==6.1.0 wheel==0.46.2

# # Install build dependencies
# RUN apt-get update && apt-get upgrade -y && \
#     apt-get install -y --no-install-recommends build-essential && \
#     rm -rf /var/lib/apt/lists/*

# # Upgrade pip
# RUN pip install --upgrade pip

# COPY requirements.txt .
# RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# # -------- Stage 2: Runtime --------
# FROM python:3.11-slim

# # Environment variables (good practice)
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# WORKDIR /app

# # Copy installed dependencies from builder
# COPY --from=builder /install /usr/local

# # Create non-root user safely
# RUN useradd -m appuser

# # Copy only necessary files
# COPY . .

# # Change ownership
# RUN chown -R appuser:appuser /app

# USER appuser

# EXPOSE 8000

# CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
