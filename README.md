# CICLOH #

** API de CICLOH: creada con DRF, agregamos Swagger para
 documentar sus endpoints. **

### Índice ###

1. Instalación.
2. Ejecutar.
3. Swagger - API docs.
4. Code Style.
5. Crear/Cargar fixtures de datos.
6. Ejecutar Tests.


### 1. Instalación ###

- **Crear el virtualenv con Python3.7**
- **Clonar el Proyecto.**
- **Instalar las dependencias:** `pip install -r requirements.txt`
- **Migrate:** `python manage.py migrate`
- **Crear superuser:** `python manage.py createsuperuser`

### 2. Ejecutar ###

- **Activar el virtualvenv:** `/path/to/virtualvenv/activate`
- **Ejecutar el servidor:** `python manage.py runserver`
- **Ir al navegador:** `http://127.0.0.1:8000`, `http://localhost:8000/admin`

### 3. Swagger - API docs ###
- **Swagger:** `http://127.0.0.1:8000/swagger`


### 4. Code Style ###

**Para verificar que el código cumpla con PEP8 se puede ejecutar pycodestile.**
**Para esto hay que posicionarse en la raíz del proyecto y ejecutar lo siguiente:**

`pycodestyle .`

**Para este chequeo podemos excluir archivos y directorios:**

`pycodestyle . --exclude=migrations,venv,settings`


### 5. Crear/Cargar fixtures de datos ###

- Ejecutar: `python manage.py dumpdata --format=json products > fixtures/products.json`
- `json products`: indica el formato (json) y la app (products), y luego con el simbolo `>`
   se indica la ruta donde se alojará `fixtures/` y el nombre del archivo `products.json`
- Para cargar esos datos, ejecutar: `python manage.py loaddata fixtures/model_name.json`


### 6. Ejecutar Tests ###

- Ejecutar: python manage.py test