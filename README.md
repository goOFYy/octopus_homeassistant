# Octopus Homeassistant

# Introduction
    This is a small automation script to puld meter data from Octopus Energie's website ( if you have a smart Meter) and stores it in a MYSQL database ( MariaDB in home assistant)
# Setup
1. install Docker
2. Setup MariaDB On home Assistant ( or any MYSQL DB)
3. Generate Octopus Energy API keys and get the relevant Meter Info
4. From Auth.ini.example Create Auth.ini with the right Credentials and information
5. Docker build and run 
6. EVERY 30 minutes the database will be updated with latest info from Octopus (dating back to yesterday 00:00) 

NB: You can adjust how far you want to go back by manipulation the param in the URL in the api.PY file (period_from=)

# example 
    Here is an example of how i am using grafana to display the information in a graph on home assistant
    
![image](https://user-images.githubusercontent.com/12627412/131188958-a58974a4-794d-48d2-be7f-94b3174fb1ff.png)
