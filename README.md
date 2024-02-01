# VPN Service

## VPN Service technical task solution

To run project you will need ot install Docker on your computer. 

Official link for downloading docker installed - [Docker](https://www.docker.com/products/docker-desktop/)

Pull image from Docker hub
```sh
docker pull nivankiv/vpn-service:latest
```

Start development server

```sh
docker run -p 8000:8000 nivankiv/vpn-service
```

Access the application [VPN Service (http://127.0.0.1:8000/)](http://127.0.0.1:8000/)

To brows application you can use existing user with VPN usage history or register new user:
   ```
   Username: user1
   Password: 1qazcde3
   ```

## Running a project locally

To run the project locally, follow these steps:

Fork repository and clone it to local computer
```
https://github.com/Naz-iv/vpn-service.git
```

Navigate to project folder and configure virtual environment
```
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

Create .env file with following environmental variables
```
DJANGO_SECRET_KEY=DJANGO_SECRET_KEY
DEBUG=False
```
Run Django development server of docker container whichever is more convenient
```
python manage.py runserver
---------------------------------------
or
---------------------------------------
docker build -t nivankiv/vpn-service .
docker run -p 8000:8000 nivankiv/vpn-service
```

To brows application you can use existing user with VPN usage history:
   ```
   Username: user1
   Password: 1qazcde3
   ```