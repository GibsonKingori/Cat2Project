# E-Commerce Django Project

## Overview
A Django-based e-commerce project that models `Customer` and `Order` relationships. Each customer can place multiple orders.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GibsonKingori/Cat2Project.git
   cd Cat2Project
Set up a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a superuser (for admin access):

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Access the admin panel:

URL: http://127.0.0.1:8000/admin
Login with your superuser credentials.