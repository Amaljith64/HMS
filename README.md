# HomeToHome - Your One-Stop Solution for Room Booking

Welcome to the HomeToHome project, a fully-featured room booking website that utilizes the latest technologies to deliver an exceptional user experience. Our website, hosted on Amazon Web Services (AWS) using nginx as a proxy server, can be accessed at [https://hometohome.ml](https://hometohome.ml) and our source code can be found on our GitHub repository [https://github.com/Amaljith64/HMS.git](https://github.com/Amaljith64/HMS.git)

## Technology Stack
The following technologies were used to develop and maintain the HomeToHome project:
* Python
* Django
* HTML, CSS, Bootstrap
* PostgreSQL
* Razorpay (Payment Gateway)
* PayPal (Payment Gateway)
* Twilio (OTP Verification)
* AWS (Web Hosting)
* Nginx (Web Server)
* JavaScript
* HTMX

## Project Features

### User Side
- User registration and login with OTP verification
- Search available rooms with check-in and check-out dates
- Search and filter options
- Pagination
- View room details
- Wishlist rooms
- Review rating system
- Referral system
- Wallet for users
- Coupons
- Download invoice as PDF
- Cancel booking option
- Order history and status
- Multiple payment options (Razorpay, PayPal, and Pay at Hotel)

### Admin Side
- Chart and graph report
- Booking history and status with cancellation, check-in, and check-out options
- User management with block/unblock options
- Add, edit, and delete rooms
- Category management
- Offer management
- Coupon management
- Sales report with download option

## Getting Started

To run the project locally, please follow these steps:
1. Clone the repository: `git clone https://github.com/Amaljith64/HMS.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Create a PostgreSQL database and update the settings in `settings.py`
4. Run the migration: `python manage.py makemigrations` and `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Run the development server: `python manage.py runserver`


## Screenshots


![Prolancer Screenshot](https://amaljith64.github.io/Amaljithportfolio/assets/img/Project%201.png)

## Contribution

We welcome contributions to the HomeToHome project. If you are interested in contributing, please follow these guidelines:
1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Commit your changes and push to your branch
4. Create a pull request for review

## Support

For any questions or feedback, please reach out to us via the contact information provided on our website or open an issue on the repository. We hope you enjoy using HomeToHome!
