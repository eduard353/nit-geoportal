import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'SECRET_KEY'  # Используйте свой ключ

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', '0.0.0.0']

if os.name == 'nt':
    import platform

    OSGEO4W = r"C:\OSGeo4W"
    if '64' in platform.architecture()[0]:
        OSGEO4W += "64"
    assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['GDAL_DATA'] = "C:\Program Files\GDAL\gdal-data"  # OSGEO4W + r"\share\gdal"
    os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
    os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']
    GDAL_LIBRARY_PATH = r'C:\OSGeo4W64\bin\gdal301.dll'
    GEOS_LIBRARY_PATH = r'C:\OSGeo4W64\bin\geos_c.dll'
    os.environ['GDAL_DATA'] = r"C:\OSGeo4W64\share\epsg_csv"

# Application definition

INSTALLED_APPS = [
    'grappelli',
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'leaflet',
    'nitmap.apps.NitmapConfig',
    'colorfield',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'newgeo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'newgeo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# Параметры подключения к БД берутся из системных переменных
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('POSTGRES_DB'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'PORT': os.getenv('POSTGRES_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'static/dist'),
)

LEAFLET_CONFIG = {
    # 'TILES':  'static/Tiles/{z}/{x}/{y}.png', # локально расположенные файлы карт
    # Онлайн сервис карт
    'TILES': 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    # локальный сервис карт
    # 'TILES':  'http://localhost:8080/styles/basic-preview/{z}/{x}/{y}.png',
    'DEFAULT_CENTER': (54.872, 69.139),  # Координаты центра карты по умолчанию
    'DEFAULT_ZOOM': 12,
    'MIN_ZOOM': 12,
    'MAX_ZOOM': 17,
    'RESET_VIEW': False,
    # Список плагинов Leaflet
    'PLUGINS': {
        'groupedlayercontrol': {
            'css': 'dist/leaflet.groupedlayercontrol.min.css',
            'js': 'dist/leaflet.groupedlayercontrol.min.js',
            'auto-include': True,
        },
        'MarkerCluster': {
            'css': ['dist/MarkerCluster.css', 'dist/MarkerCluster.Default.css'],
            'js': ['dist/leaflet.markercluster.js', ],
            'auto-include': True,
        },
        'leaflet-search': {
            'css': 'dist/leaflet-search.src.css',
            'js': 'dist/leaflet-search.src.js',
            'auto-include': True,
        },
        'locationlist': {
            'css': 'dist/leaflet.locationlist.css',
            'js': 'dist/leaflet.locationlist.js',
            'auto-include': True,
        },
        'Leaflet.Icon.Glyph': {

            'js': 'dist/Leaflet.Icon.Glyph.js',
            'auto-include': True,
        },
        'sector': {

            'js': 'dist/leaflet.sector.js',
            'auto-include': True,
        },
        'leaflet.ajax': {

            'js': 'dist/leaflet.ajax.js',
            'auto-include': True,
        },
    }
}

GRAPPELLI_ADMIN_TITLE = 'ГЕОПОРТАЛ СК ОЦИТ'

X_FRAME_OPTIONS = 'SAMEORIGIN'
