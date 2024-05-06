import environ
from pathlib import Path
import os
from datetime import timedelta

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api1',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'rest_framework_simplejwt',
    'djoser',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DRF
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

REST_USE_TWT = True
SITE_ID = 1
# Djoserの設定
DJOSER = {
    'LOGIN_FIELD': 'username',  # ログインに使用するフィールド。デフォルトは'username'。
    'SERIALIZERS': {
        # カスタムシリアライザーを使用したい場合は設定します。
        # 'user_create': 'your_project.serializers.CustomUserCreateSerializer',
        # 'user': 'your_project.serializers.CustomUserSerializer',
        # 'current_user': 'your_project.serializers.CustomCurrentUserSerializer',
        'token_create': 'djoser.serializers.TokenCreateSerializer',  # トークン生成のシリアライザー
    },
    'TOKEN_MODEL': 'rest_framework_simplejwt.tokens.AccessToken',  # JWTトークンのモデル
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}/',
    'USERNAME_RESET_CONFIRM_URL': 'username/reset/confirm/{uid}/{token}/',
    'ACTIVATION_URL': 'activate/{uid}/{token}/',
    'SEND_ACTIVATION_EMAIL': False,
    'SOCIAL_AUTH_TOKEN_STRATEGY': 'djoser.social.token.jwt.TokenStrategy',
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': [SECRET_KEY],
    'LOGIN_REDIRECT_URL': '/',  # ログイン後にリダイレクトされるURLを指定
    # その他のDjoser設定を追加できます
}

# django-rest-framework-simplejwt
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),  # JWTトークンを受け取る認証ヘッダータイプ
    'TOKEN_TYPE_CLAIM': 'typ',
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),  # アクセストークンの有効期間
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # リフレッシュトークンの有効期間
    # その他のSIMPLE_JWT設定を追加できます
}

CORS_ALLOWED_ORIGINS = [
'http://127.0.0.1:3000',
]
# CORSの許可
CORS_ALLOW_ALL_ORIGINS: True

AUTH_USER_MODEL = 'api1.CustomUser'