# PsicoCenter - Plataforma de Gestión de Psicólogos

Sistema de gestión de citas y psicólogos desarrollado con Django siguiendo los principios de Domain-Driven Design (DDD).

## Requisitos

- Python 3.8+
- Django 5.2+
- Pillow (para el manejo de imágenes)

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/psico-center.git
cd psico-center
```

2. Crear y activar entorno virtual:
```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Aplicar migraciones:
```bash
python manage.py migrate
```

5. Crear superusuario:
```bash
python manage.py createsuperuser
```

6. Iniciar el servidor:
```bash
python manage.py runserver
```

## Estructura del Proyecto

El proyecto sigue una arquitectura DDD con las siguientes capas:

- `domain/`: Entidades y reglas de negocio
- `application/`: Servicios y casos de uso
- `infrastructure/`: Implementaciones técnicas
- `interfaces/`: APIs y vistas

## Características

- Gestión de psicólogos
- Sistema de citas
- Panel de administración
- API REST

## Licencia

Este proyecto está bajo la Licencia MIT. 