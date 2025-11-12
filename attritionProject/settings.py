from pathlib import Path

# =======================
# 📁 BASE DIRECTORY SETUP
# =======================
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / 'templates'

# =======================
# 🔐 SECURITY SETTINGS
# =======================
SECRET_KEY = 'django-insecure-3l5$w-us%)(lo8nm%f8=n8(#xt$-k)96ee_(o-hjm&lhs3tg6s'
DEBUG = False
ALLOWED_HOSTS = ['*']  # ✅ Allow all during development (restrict in production)

# =======================
# ⚙️ APPLICATIONS
# =======================
INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your custom apps
    'attrApp',

    # Crispy forms for better form styling
    'crispy_forms',
    'crispy_bootstrap4',
]

# Crispy Forms Configuration
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

# =======================
# 🌐 MIDDLEWARE
# =======================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =======================
# 🔗 URLS & WSGI
# =======================
ROOT_URLCONF = 'attritionProject.urls'
WSGI_APPLICATION = 'attritionProject.wsgi.application'

# =======================
# 🎨 TEMPLATES
# =======================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# =======================
# 🗄️ DATABASE
# =======================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# =======================
# 🔑 PASSWORD VALIDATION
# =======================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =======================
# 🌍 INTERNATIONALIZATION
# =======================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# =======================
# 📦 STATIC & MEDIA FILES
# =======================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# =======================
# 🆔 DEFAULTS
# =======================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

