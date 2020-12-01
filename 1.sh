sudo rm /etc/nginx/sites-enabled/*
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

sudo rm /etc/gunicorn.d/*
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/ask.conf /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart
#﻿sudo /etc/init.d/mysql start﻿
git config --global user.email "grustem@gmail.com"
git config --global user.name "grustem"
