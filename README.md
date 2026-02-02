# E-Commerce Platform (Django Backend) — PDF-aligned implementation

This repository contains the **Django backend** for an e-commerce web application aligned strictly to:

- `kavia-docs/CodeWiki/Specs/Analysis/e-commerce-pdf-requirements-extraction.md`
- `kavia-docs/CodeWiki/Specs/ArchitectureSpecs/e-commerce-system-architecture-pdf-aligned.md`

The PDF describes a **server-rendered Django application** (HTML/CSS/JS/Bootstrap) with Django Admin, not a REST API.

## Implemented features (as described in the PDF)
- Home page product listing (image, name, price)
- Search (navbar)
- Register / Login / Logout
- Product detail page (features + reviews)
- Reviews: allow writing a review only if user has ordered that product (conservative enforcement per architecture doc)
- Cart (logged-in only): add items, increase/decrease quantities
- Checkout: delivery details + payment mode, place order, display generated Order ID, empty cart after successful checkout
- Track order: lookup by Order ID and display order details/status
- Change password
- Contact forms:
  - Logged-in: message only
  - Guest: name, email, phone, message
- Django Admin: manage products, features, orders, reviews, contact messages, etc.

## Run locally (development)

### 1) Create venv and install deps
```bash
cd django_backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Configure environment
Copy `.env.example` to `.env` and set values.

### 3) Migrate + create admin user
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4) Run server
```bash
python manage.py runserver 0.0.0.0:8000
```

Then open:
- App: `http://localhost:8000/`
- Admin: `http://localhost:8000/admin/`

## Notes / Non-goals (out of scope per PDF)
- No payment gateway integration
- No categories/discounts/inventory management
- No password reset / email verification (not specified in PDF)
- No external notifications (email/SMS) (not specified in PDF)

Task completed: backend repo README updated and aligned to PDF-derived scope.
