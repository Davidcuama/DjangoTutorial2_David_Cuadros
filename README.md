# DjangoTutorial2_David_Cuadros# Online Store – Tutorial de Modelos en Django

Proyecto base para la entrega del tutorial de **Django (modelos, factories, seeds, vistas, formularios y plantillas)**. 
Sigue el flujo del documento de clase: crea el modelo `Product`, un `Comment` relacionado, pobla con `factory_boy` y muestra datos desde la base.

> Proyecto probado con **Django 5.x** y **SQLite**. Si usas **Python 3.13**, se recomienda **Django 5.1+**.

---

##  Características clave
- **Modelos**
  - `Product(name, price, description?, created_at, updated_at)`
  - `Comment(product -> FK a Product, description)`
- **Seeds con factory_boy**: `python manage.py seed_products` (crea 8 productos aleatorios).
- **Vistas**
  - Listado: `/products/` (precio en rojo si `price > 2000`)
  - Detalle: `/products/<id>/` (incluye comentarios con `product.comment_set.all`)
  - Crear: `/products/create/` (validación: `price > 0`, redirige a `/product-created/`)
- **Plantillas** con Bootstrap 5: `base.html`, `index.html`, `show.html`, `create.html`, `created_ok.html`
- **Rutas listas** en `pages/urls.py` e inclusión en `onlinestore/urls.py`

---

## Estructura relevante
```
<repo-root>/
├─ manage.py
├─ requirements.txt
├─ onlinestore/
│  ├─ settings.py
│  └─ urls.py            ← incluye 'pages.urls'
└─ pages/
   ├─ models.py          ← Product, Comment
   ├─ forms.py           ← ModelForm para Product
   ├─ views.py           ← Index, Show, Create
   ├─ urls.py            ← /, /products/, /products/<id>/, /products/create/, /product-created/
   ├─ factories.py       ← ProductFactory (Faker)
   ├─ management/
   │  └─ commands/
   │     └─ seed_products.py
   └─ templates/pages/
      ├─ base.html
      ├─ index.html
      ├─ show.html
      ├─ create.html
      └─ created_ok.html
```

---

## Requisitos
- Python 3.10+ (recomendado)
- **Django 5.x**
  - Si usas **Python 3.13**, instala: `pip install "Django>=5.1,<6"`
- `factory_boy` y `Faker` (incluidos en `requirements.txt`)

Instala dependencias:
```bash
pip install -r requirements.txt
```

---

## Configuración inicial
1. Verifica que `'pages'` esté en `INSTALLED_APPS` dentro de `onlinestore/settings.py`.
2. Crea y aplica migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. (Opcional) Pobla datos de ejemplo:
   ```bash
   python manage.py seed_products
   ```

---

## Ejecutar el servidor
```bash
python manage.py runserver
```

Rutas útiles:
- **Listado**: `http://127.0.0.1:8000/products/`
- **Crear**: `http://127.0.0.1:8000/products/create/`
- **Detalle**: `http://127.0.0.1:8000/products/1/`
- **Éxito**: `http://127.0.0.1:8000/product-created/`

---

##  Comentarios
El tutorial sugiere crear comentarios ligados a un producto:
- Opción A: usar **Django Admin**:
  ```bash
  python manage.py createsuperuser
  ```
  Luego entra a `/admin/` y crea `Comment` con `product_id` existente.
- Opción B: editar `db.sqlite3` y añadir filas en la tabla `pages_comment` con un `product_id` válido.

En `show.html` se listan con:
```django
{% for comment in product.comment_set.all %}
  - {{ comment.description }}<br>
{% endfor %}
```

---

## Troubleshooting rápido
**Error:** `OperationalError: no such table: pages_product`  
**Causa:** migraciones no aplicadas.  
**Solución:**
```bash
python manage.py makemigrations pages
python manage.py migrate
```
Si persiste:
```bash
python manage.py showmigrations pages
```
- Si dice “(no migrations)”, revisa `pages/models.py` y vuelve a correr `makemigrations` + `migrate`.
- Confirma que estás en el **mismo directorio** que contiene el `manage.py` correcto.
- Si usas **Python 3.13**, actualiza Django: `pip install "Django>=5.1,<6"`

**Plan B (resetear solo el app `pages`, si quedó enredado):**
```bash
python manage.py migrate pages zero
# borra 00xx_*.py dentro de pages/migrations dejando __init__.py
python manage.py makemigrations pages
python manage.py migrate
```

---

## Créditos
- Estructura basada en el **tutorial de clase de Django (modelos)**.
- Autor: David Cuadros (entrega académica).
