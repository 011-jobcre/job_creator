# ==========================================
# STAGE 1: Build CSS (Using Node.js)
# ==========================================
FROM node:20-slim AS css-builder
WORKDIR /build

# Only copy files needed to install libraries
COPY package*.json ./

# install tailwind and daisyui
RUN npm install tailwindcss @tailwindcss/cli daisyui@latest @tailwindcss/typography

# Copy source files for Tailwind build
COPY ./css_src/ ./backend/css_src/
COPY ./backend/templates ./backend/templates/

# Build CSS (Tailwind will find daisyui in node_modules)
RUN npx tailwindcss -i ./backend/css_src/input.css -o ./output.css --minify

# ==========================================
# STAGE 2: Runtime (Dành cho SQLite3 & Landing Page)
# ==========================================
FROM python:3.12-slim

WORKDIR /app

# Chỉ cài những thứ thực sự cần thiết
RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-openbsd \
    gettext \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy CSS từ Stage 1
COPY --from=css-builder /build/output.css ./backend/static/css/output.css

COPY . .

# 5. Set up User and Permissions
WORKDIR /app/backend
RUN useradd -m appuser && chown -R appuser /app
# Cấp quyền ghi đặc biệt cho file db (thường là db.sqlite3)
RUN touch db.sqlite3 && chown appuser:appuser db.sqlite3
COPY --chown=appuser:appuser /entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER appuser
EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBUG=False

ENTRYPOINT ["/entrypoint.sh"]
