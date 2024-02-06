# SORTA-WASTE

SORTA WASTE is a web-based application designed to connect waste producers with waste reusers and recyclers, while also enabling users to sort their waste effectively. Whether you're a household, business, or organization, SORTA WASTE provides a platform to manage waste responsibly and contribute to environmental sustainability.

## Overview

SORTA WASTE is a web-based application designed to bridge the gap between waste producers and waste reusers/recyclers. The platform offers features such as waste sorting guidance, waste collection scheduling, and a marketplace for buying and selling recyclable materials. By facilitating communication and collaboration among stakeholders, SORTA WASTE aims to promote waste reduction, reuse, and recycling initiatives.

## Key Features

- **Waste Sorting Guide**: Provides users with guidance on how to properly sort different types of waste, including recyclables, organics, and hazardous materials.

- **Waste Collection Scheduling**: Enables users to schedule waste collection services based on their location and waste disposal needs.

- **Marketplace**: Offers a marketplace where users can buy and sell recyclable materials, fostering a circular economy and promoting resource conservation.

- **Community Engagement**: Facilitates community engagement through forums, events, and educational resources aimed at raising awareness about waste management and environmental sustainability.

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python, Django
- Database: MySQL
- Authentication: Django Authentication System

## Installation and Usage

To run this project locally, follow these steps:

```bash
# Clone the repository to your local machine
git clone [repository URL]

# Navigate to the project directory
cd sorta-waste

# Set up a virtual environment (optional but recommended)
python -m venv venv

# For Linux/Mac
source venv/bin/activate

# For Windows
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create a superuser (admin account)
python manage.py createsuperuser

# Start the development server
python manage.py runserver
