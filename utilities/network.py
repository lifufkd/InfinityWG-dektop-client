##########################
#       Created By       #
#          SBR           #
##########################
import socket
import requests
##########################

##########################


def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        ip_address = response.json()['ip']
    except requests.RequestException as e:
        ip_address = 'No internet connection'
    return ip_address


def get_country_by_ip():
    try:
        response = requests.get('https://ipapi.co/json/')
        data = response.json()
        country = data.get('country_name')
        if country:
            return country
        else:
            return "-"
    except Exception as e:
        return "-"
