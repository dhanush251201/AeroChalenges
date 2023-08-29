pm2 delete all
cd /Users/dhanush/Documents/D/college/sem7/deploy/GuardianFlight
pm2 start --name 'guardian' 'gunicorn --bind 127.0.0.1:7100 guardian:app'
cd ../inspect
pm2 start --name 'inspect' 'gunicorn --bind 127.0.0.1:7101 app:app'
cd ../SQLI
pm2 start --name 'SQLI' 'gunicorn --bind 127.0.0.1:7102 app:app'
cd ../webhunt
pm2 start --name 'webhunt' 'gunicorn --bind 127.0.0.1:7103 webhunt:app'


scp -i /Users/dhanush/Downloads/aero.pem ubunut@ec2-13-233-16-102.ap-south-1.compute.amazonaws.com:/home/ubuntu -r '/Users/dhanush/Documents/D/college/sem7/deploy'