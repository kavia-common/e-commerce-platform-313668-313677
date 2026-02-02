# Django Backend (Server-rendered) — PDF-aligned e-commerce

This Django project implements the e-commerce site described in the PDF-derived requirements and architecture documents:

- `kavia-docs/CodeWiki/Specs/Analysis/e-commerce-pdf-requirements-extraction.md`
- `kavia-docs/CodeWiki/Specs/ArchitectureSpecs/e-commerce-system-architecture-pdf-aligned.md`

## Apps
- `accounts`: register/login/logout/change password (+ optional profile fields)
- `catalog`: home listing, search, product detail (features + reviews)
- `reviews`: create reviews (only for users who have ordered the product)
- `cart`: persisted cart per logged-in user; add/increase/decrease
- `orders`: checkout (delivery + payment mode), create order id, track order by order id
- `contact`: guest and logged-in contact forms

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

## Admin
Open `/admin/` and add products (name, price, image) and features. Orders, reviews, and contact messages are visible in Django Admin.

## Notes on ambiguities
- Order status values are not specified in the PDF. This implementation stores a simple status field for tracking display and admin updates.
- Payment modes are not specified in the PDF. The system stores a selected payment mode string without integrating a payment gateway.
