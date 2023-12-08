# Weather_App.github.io

A responsive weather app that provides real-time weather information for cities worldwide. Built using HTML, CSS, and Django for the backend. Hosted on AWS with Nginx as the server and Gunicorn for handling HTTP requests.


**Features**

**Responsive Design:** The app is designed to be accessible and usable across various devices and screen sizes.
**City Coverage:** Provides weather reports for cities all around the world.
**AWS Hosting:** The app is hosted on Amazon Web Services (AWS) for reliable and scalable server infrastructure.
**Nginx and Gunicorn:** Uses Nginx as the web server and Gunicorn as the application server to handle HTTP requests efficiently.


Getting Started
Prerequisites
Python
Django 
Nginx 
Gunicorn 

**Installation**
Clone the repository:
bash
git clone https://github.com/your-username/weather-app.git

**Install dependencies:**
bash
pip install -r requirements.txt

**Run the Django migrations:**
bash
python manage.py migrate

**Start the Gunicorn server:**
bash
gunicorn weather_app.wsgi.application

**Configure Nginx to serve the app:**
nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static/ {
        root /path/to/your/app;
    }

    location /media/ {
        root /path/to/your/app;
    }
}

**Restart Nginx:**
bash
sudo service nginx restart

Link: Access the app in your browser at http://yourdomain.com.

**Contributing**
If you want to contribute to this project, please follow the contribution guidelines.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.

**Acknowledgments**
Thanks to OpenWeather for providing the weather data API.
Feel free to customize this template according to your project's specific details and structure. Include any additional information that might be helpful for users, such as API documentation, known issues, or troubleshooting tips.
