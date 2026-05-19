#!/bin/bash
# Dừng script nếu có lỗi xảy ra
set -e

# --- 1. XỬ LÝ DATABASE ---
# Vì dùng SQLite, ta không cần check cổng mạng (nc). 
# Chỉ cần đảm bảo file database tồn tại và chạy migrate.
echo "Checking SQLite database..."
python manage.py migrate --noinput

# --- 2. XỬ LÝ STATIC FILES & TRANSLATIONS ---
echo "Compiling translations..."
python manage.py compilemessages

echo "Collecting static files..."
python manage.py collectstatic --noinput

# --- 3. KIỂM TRA CHẾ ĐỘ CHẠY (DEV vs PROD) ---
if [ "$DEBUG" = "True" ] || [ "$DEBUG" = "1" ]; then
    echo "Running in DEVELOPMENT mode"
    # Dùng runserver để có Hot-reload khi sửa code
    exec python manage.py runserver 0.0.0.0:8000
    
else
    echo "Running in PRODUCTION mode"
    
    # Tạo superuser tự động nếu có yêu cầu (hữu ích khi deploy lần đầu)
    if [ "$CREATE_SUPERUSER" = "True" ] || [ "$CREATE_SUPERUSER" = "1" ]; then
        echo "Creating superuser..."
        # echo "Updating Database & Seeding..."
        # python manage.py loaddata ../gyomu_fixture.json || echo "No fixture found or already loaded."
        echo "Creating superuser (if not exists)..."
        python manage.py createsuperuser --noinput || echo "Superuser already exists."
    fi

    # Chạy Gunicorn cho môi trường thực tế (thay 'core' bằng tên thư mục chứa wsgi.py của bạn)
    echo "Starting Gunicorn..."
    exec gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3
fi