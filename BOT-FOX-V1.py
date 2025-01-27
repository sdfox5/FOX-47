import re
import time
import socket
import threading
import select
import requests
import random
import os
import sys
####################################
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_MAGENTA = "\033[95m"
COLOR_CYAN = "\033[96m"
COLOR_WHITE = "\033[97m"
COLOR_RESET = "\033[0m"
COLOR_BOLD = "\033[1m"
COLOR_UNDERLINE = "\033[4m"
####################################
print(f"""{COLOR_BOLD}{COLOR_CYAN} 
.#######..#######.##.....#....#######.########.##.......########
.##......##.....#..##...##...##.....#.##.....#.##....##.##....##
{COLOR_BLUE}.##......##.....#...##.##....##.....#.##.....#.##....##.....##..
.######..##.....#....###.....##.....#.########.##....##....##...
{COLOR_MAGENTA}.##......##.....#...##.##....##.....#.##.....#.########...##....
.##......##.....#..##...##...##.....#.##.....#.......##...##....
.##.......#######.##.....#....#######.########.......##...##....

{COLOR_YELLOW}⇾  Version: 1.0 | By: @fox, AND MY FAMILY CODEX TEAM⇽
{COLOR_YELLOW}⇾  Authentication: {COLOR_GREEN}bot:bot{COLOR_RESET}
{COLOR_YELLOW}⇾Tool Name: {COLOR_RED}{COLOR_UNDERLINE}FOX-OB47{COLOR_RESET}
""")
####################################
username = "bot"
password = "bot"
SOCKS5_VERSION = 5
server_list = []
op = None
MainC = None
spam_emote = False
spamm = False
back_normal = False
back_spam = False
yt = None
####################################
def get_random_color():
    color = random.choice([
        "[cُ][bَ][FF0000]",
        "[cُ][bَ][00FF00]",
        "[cُ][bَ][0000FF]",
        "[cُ][bَ][FFFF00]",
        "[cُ][bَ][FFA500]",
        "[cُ][bَ][800080]",
        "[cُ][bَ][808080]",
        "[cُ][bَ][FFD700]",
        "[cُ][bَ][00FFFF]",
        "[cُ][bَ][FF1493]",
        "[cُ][bَ][8A2BE2]",
        "[cُ][bَ][A52A2A]",
        "[cُ][bَ][DC143C]",
        "[cُ][bَ][00CED1]",
        "[cُ][bَ][FF4500]",
        "[cُ][bَ][2E8B57]",
        "[cُ][bَ][ADFF2F]",
        "[cُ][bَ][4682B4]",
        "[cُ][bَ][40E0D0]",
        "[cُ][bَ][DA70D6]",
        "[cُ][bَ][F4A460]",
        "[cُ][bَ][FF6347]",
        "[cُ][bَ][7FFF00]",
        "[cُ][bَ][BA55D3]",
        "[cُ][bَ][FF69B4]",
        "[cُ][bَ][E9967A]",
    ])
    return color
####################################
def send_msg_clan(replay, packet):
	replay  = replay.encode('utf-8')
	replay = replay.hex()
	hd = packet[0:8]
	packetLength = packet[8:10] #
	paketBody = packet[10:32]
	pyloadbodyLength = packet[32:34]#
	pyloadbody2 = packet[34:64]
	if "googleusercontent" in str(bytes.fromhex(packet)):
		pyloadlength = packet[64:68]#
		pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
		Tipy = packet[int(int(len(pyloadtext))+68):]
	elif "https" in str(bytes.fromhex(packet)) and "googleusercontent" not in str(bytes.fromhex(packet)):
		pyloadlength = packet[64:68]#
		pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
		Tipy = packet[int(int(len(pyloadtext))+68):]
		print(bytes.fromhex(pyloadlength))
	else:
		pyloadlength = packet[64:66]#
		pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
		Tipy = packet[int(int(len(pyloadtext))+66):]
	NewTextLength = (hex((int(f'0x{pyloadlength}', 16) - int(len(pyloadtext)//2) ) + int(len(replay)//2))[2:])
	if len(NewTextLength) ==1:
		NewTextLength = "0"+str(NewTextLength)
	NewpaketLength = hex(((int(f'0x{packetLength}', 16) - int(len(pyloadtext)//2) ) - int(len(pyloadlength))) + int(len(replay)//2) + int(len(NewTextLength)))[2:]
	NewPyloadLength = hex(((int(f'0x{pyloadbodyLength}', 16) - int(len(pyloadtext)//2)) -int(len(pyloadlength)) )+ int(len(replay)//2) + int(len(NewTextLength)))[2:]
	st_pack = hd + NewpaketLength +paketBody + NewPyloadLength +pyloadbody2+NewTextLength+ replay + Tipy
	return st_pack
#############################################
def send_likes_id(user_id):
    url = f"https://smartclownxfreefireinfo.vercel.app/like?uid={user_id}&server_name=sea1&key=1925045198"
    response = requests.get(url)
    like = response.json()
    return {
        "LikesGivenByAPI": f"{get_random_color()}LIKES BY API: {like.get('LikesGivenByAPI')}",
        "LikesbeforeCommand": f"{get_random_color()}LIKES BEFOR: {like.get('LikesbeforeCommand')}",
        "LikesafterCommand": f"{get_random_color()}LIKES AFTER: {like.get('LikesafterCommand')}",
        "UID": f"{get_random_color()}PLAYER UID: {like.get('UID')}"
    }
#############################################
def all_info_id(user_id):
    url = f"https://scaninfo.net/infofreefire/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            r = response.json()
            return {
    "Account Avatar": f"{get_random_color()}Avatar Image: {r.get('Account Avatar Image', 'N/A')}",
    "Account Banner": f"{get_random_color()}Banner Image: {r.get('Account Banner Image', 'N/A')}",
####################################
    "Account Booyah Pass": f"{get_random_color()}Booyah Pass: {r.get('Account Booyah Pass', 'N/A')}",
    "Account Booyah Pass Badges": f"{get_random_color()}Booyah Pass Badges: {r.get('Account Booyah Pass Badges', 'N/A')}",
    "Account Celebrity Status": f"{get_random_color()}Celebrity Status: {r.get('Account Celebrity Status', 'N/A')}",
    "Account Character ID": f"{get_random_color()}Character ID: {r.get('Account Character ID', 'N/A')}",
####################################
    "Account Create": f"{get_random_color()}Create Time: {r.get('Account Create Time (GMT 0530)', 'N/A')}",
####################################
    "Account Evo Badge": f"{get_random_color()}Evo Access Badge: {r.get('Account Evo Access Badge', 'N/A')}",
    "Account Honor Score": f"{get_random_color()}Honor Score: {r.get('Account Honor Score', 'N/A')}",
    "Account Language": f"{get_random_color()}Language: {r.get('Account Language', 'N/A')}",
####################################
    "Account Last": f"{get_random_color()}Last Login: {r.get('Account Last Login (GMT 0530)', 'N/A')}",
#################INFO - V1#####################
    "Account Level": f"{get_random_color()}Level: {r.get('Account Level', 'N/A')}",
    "Account Likes": f"{get_random_color()}Likes: {r.get('Account Likes', 'N/A')}",
    "Account Name": f"{get_random_color()}PLAYER NAME: {r.get('Account Name', 'N/A')}",
    "Account Recent OB": f"{get_random_color()}Recent OB: {r.get('Account Recent OB', 'N/A')}",
    "Account Region": f"{get_random_color()}Region: {r.get('Account Region', 'N/A')}",
    "Account Signature": f"{get_random_color()}Signature: {r.get('Account Signature', 'N/A')}",
    "Account UID": f"{get_random_color()}PLAYER UID: {r.get('Account UID', 'N/A')}",
    "Account XP": f"{get_random_color()}XP: {r.get('Account XP', 'N/A')}",
#############################################
    "BR Rank Points": f"{get_random_color()}BR Rank Points: {r.get('BR Rank Points', 'N/A')}",
    "CS Rank Points": f"{get_random_color()}CS Rank Points: {r.get('CS Rank Points', 'N/A')}",
    "Equipped Items": f"{get_random_color()}Equipped Items: {r.get('Equipped Items', {})}",
#############################################
    "Public Craftland Maps": f"{get_random_color()}Craftland Maps: {r.get('Public Craftland Maps', {})}"
}
####################################
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return {
                "error": "Invalid JSON response"
            }
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return {
            "error": f"Failed to fetch data: {response.status_code}"
        }
####################################
def get_status(user_id):
    try:
        r = requests.get(f'https://ff.garena.com/api/antihack/check_banned?lang=en&uid={user_id}')
        if "0" in r.text:
            return f"{get_random_color()}▶PLAYER STATUS: {get_random_color()} Account Clear!"
        else:
            return "{get_random_color()}▶PLAYER STATUS: {get_random_color()} Account Ban!"
    except Exception as e:
        return f"Error checking status: {e}"
def get_player_info(user_id):
    try:
        cookies = {
            '_ga': 'GA1.1.2123120599.1674510784',
            '_fbp': 'fb.1.1674510785537.363500115',
            '_ga_7JZFJ14B0B': 'GS1.1.1674510784.1.1.1674510789.0.0.0',
            'source': 'mb',
            'region': 'MA',
            'language': 'ar',
            '_ga_TVZ1LG7BEB': 'GS1.1.1674930050.3.1.1674930171.0.0.0',
            'datadome': '6h5F5cx_GpbuNtAkftMpDjsbLcL3op_5W5Z-npxeT_qcEe_7pvil2EuJ6l~JlYDxEALeyvKTz3~LyC1opQgdP~7~UDJ0jYcP5p20IQlT3aBEIKDYLH~cqdfXnnR6FAL0',
            'session_key': 'efwfzwesi9ui8drux4pmqix4cosane0y',
        }
        headers = {
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Origin': 'https://shop2game.com',
            'Referer': 'https://shop2game.com/app/100067/idlogin',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'accept': 'application/json',
            'content-type': 'application/json',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'x-datadome-clientid': '20ybNpB7Icy69F~RH~hbsvm6XFZADUC-2_--r5gBq49C8uqabutQ8DV_IZp0cw2y5Erk-KbiNZa-rTk1PKC900mf3lpvEP~95Pmut_FlHnIXqxqC4znsakWbqSX3gGlg',
        }
        json_data = {
            'app_id': 100067,
            'login_id': f'{user_id}',
            'app_server_id': 0,
        }
        response = requests.post(
            'https://shop2game.com/api/auth/player_id_login',
            cookies=cookies,
            headers=headers,
            json=json_data
        )
        if response.status_code == 200:
            player_info= response.json()
            return {
                 "region": f"{get_random_color()}⏯PLAYER REGION: {get_random_color()}{player_info['region']}",
                "nickname": f"{get_random_color()}⏭PLAYER NAME: {get_random_color()}{player_info['nickname']}"
}
        else:
            return f"Failed to fetch player info: {response.status_code}"
    except Exception as e:
        return f"Error fetching player info: {e}"
####################################
def handle_client(connection):
    try:
        version, nmethods = connection.recv(2)
        methods = get_available_methods(nmethods, connection)
        if 2 not in set(methods):
            connection.close()
            return
        connection.sendall(bytes([SOCKS5_VERSION, 2]))
        if not verify(connection):
            return
        version, cmd, _, address_type = connection.recv(4)
        if address_type == 1:
            address = socket.inet_ntoa(connection.recv(4))
        elif address_type == 3:
            domain_length = connection.recv(1)[0]
            domain = connection.recv(domain_length).decode('utf-8')
            address = socket.gethostbyname(domain)
        port = int.from_bytes(connection.recv(2), 'big', signed=False)
        port2 = port
        remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            remote.connect((address, port))
        except Exception as e:
            print(f"Failed to connect to remote: {e}")
            connection.close()
            return
        serverlog(address, port)
        bind_address = remote.getsockname()
        addr = int.from_bytes(socket.inet_aton(bind_address[0]), 'big', signed=False)
        port = bind_address[1]
        reply = b"".join([
            SOCKS5_VERSION.to_bytes(1, 'big'),
            int(0).to_bytes(1, 'big'),
            int(0).to_bytes(1, 'big'),
            int(1).to_bytes(1, 'big'),
            addr.to_bytes(4, 'big'),
            port.to_bytes(2, 'big')
        ])
        connection.sendall(reply)
        exchange_loop(connection, remote, port2)
    except Exception as e:
        print(f"ERROR IN handle_client: {e}")
####################################
def verify(connection):
    try:
        version = connection.recv(1)[0]
        username_len = connection.recv(1)[0]
        username_received = connection.recv(username_len).decode('utf-8')
        password_len = connection.recv(1)[0]
        password_received = connection.recv(password_len).decode('utf-8')
        if username_received == username and password_received == password:
            connection.sendall(bytes([version, 0]))
            return True
        connection.sendall(bytes([version, 0xFF]))
        connection.close()
        return False
    except Exception as e:
        print(f"ERROR IN verify: {e}")
        return False
####################################
def get_available_methods(nmethods, connection):
    try:
        return [connection.recv(1)[0] for _ in range(nmethods)]
    except Exception as e:
        print(f"ERROR IN get_available_methods: {e}")
        return []
####################################
def serverlog(address, port):
    server_info = f"{address}:{port}"
    if server_info not in server_list:
        server_list.append(server_info)
####################################
def exchange_loop(client, remote, port):
    global codes, op, MainC, spamm
    if port == 39699:
        MainC = client
    try:
        while True:
            r, _, _ = select.select([client, remote], [], [])
            if client in r:
                dataC = client.recv(4096)
                if '0515' in dataC.hex()[0:4] and len(dataC.hex()) >= 141 :
                    data_join=dataC
                if remote.send(dataC) <= 0:
                    break
            if remote in r:
                dataS = remote.recv(4096)
###########FOR SHOW ALL COMMNDES#############
                if b"@START" in dataS:
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}WELL GUSY THIS IS MY FIRST BOT MADE BY FOX", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤCODEX TEAMㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
#################MENU 1######################
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤMENU V1:ㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤFOR GET INFO TO UID:ㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤUSE: /INFO_V1+IDㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤUSE: ㅤ/INFO_V2+IDㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤUSE: /INFO_V3+IDㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤUSE: /INFO_V4+IDㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤFOR GET LIKES TO UID:ㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤUSE: /LIKES+IDㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))               
                    time.sleep(2)
##################MENU 2#####################
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤMENU V2:ㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤEMOTE USE:ㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤUSE: /FX1ㅤ>>>>>>ㅤ/FX9ㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤUSE: /FX_1ㅤ>>>>>>ㅤ/FX_5ㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤEMOTEEVO GUN MAX:ㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤUSE: /F_1ㅤ>>>>>>ㅤ/F_7ㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤEMOTE LVL100:ㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤUSE: /FOX-LVL100ㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤNEW BOT ENTRE SQUAD FOR SEE BRO!!!:ㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤSPAM RANDOM EMOTEㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤUSE: /RNDㅤㅤFOR STOP: /-RNDㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤSPAM EMOTEㅤEVO DRAGON:ㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤUSE: /CDXㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    time.sleep(2)
#################MENU 3######################
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤMENU V4:ㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤTEXT STYLE NEW!ㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤUSE: /FOX-STYLEㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤSPAM INVITION!!ㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤUSE: /INVㅤㅤㅤONLYN 15 INV!!!", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤSPAM MESSAGE ANTIBAN!!ㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤUSE: /@S EXML: @S hiㅤㅤ", dataS.hex())))
                    time.sleep(2)
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤ COLORING MESSAGE!ㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤ AVAILABLE COLORSㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR REDㅤㅤUSE: /@FOX-Rㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR GreenㅤㅤUSE: /@FOX-Gㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR BlueㅤㅤUSE: /@FOX-Bㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR YellowㅤㅤUSE: /@FOX-Yㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR orange ㅤㅤUSE: /@FOX-Oㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR B Violet ㅤㅤUSE: /@FOX-Vㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR GreyㅤㅤUSE: /@FOX-GYㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR GoldenㅤㅤUSE: /@FOX-GDㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR HeavenlyㅤㅤUSE: /@FOX-CYㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR light pinkㅤㅤUSE: /@FOX-PKㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR Dark purpleㅤㅤUSE: /@FOX-DVㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR  BrownㅤㅤUSE: /@FOX-BRㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR  ScarletㅤㅤUSE: /@FOX-CRㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR TurquoiseㅤㅤUSE: /@FOX-TQㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR reddish orangeㅤㅤUSE: /@FOX-ORㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR Dark greenㅤㅤUSE: /@FOX-DGㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR light yellow ㅤㅤUSE: /@FOX-LYㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR Light blue ㅤㅤUSE: /@FOX-LBㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR  TurquoiseㅤㅤUSE: /@FOX-TZㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}COLOR  Light purple ㅤㅤUSE: /@FOX-LVㅤㅤ", dataS.hex())))
 #################MENU 6######################
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤMENU V5:ㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))                    
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤLAG YOUR ACCOUNT!!?:ㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤUSE: / LAG:ㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤADD YOUTUBERS!:ㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤUSE: / FOX-YT:ㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤMENU V6:ㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤ SPY AND DESTROY SQUAD:ㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤUSE: @FOX-SPY:ㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤFOR STOP SPY:ㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤUSE: #FOX-STOP:ㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤBY CODEX TEAMㅤㅤ", dataS.hex())))
                elif b"@LOVE" in dataS:
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}Okay guys I think everyone knows what's going on", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}Palestine we wish we could help them but we can't", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}So we will just pray to God to set them free.", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}And also for my friends", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}Congratulations to the Syrians", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}on the liberation of Syria", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤFREE PALESTINEㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤKONOZ I LOVE YOU❤️ㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                pack = dataS.hex()
                try:
                    if b"@FOX-R" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d52(.*?)28', pack)[0])).decode('utf-8', errors='ignore')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][FF0000]{idd}", pack)))
                    if b"@FOX-G" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d47(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][00FF00]{idd}", pack)))
                    if b"@FOX-Y" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d59(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][FFFF00]{idd}", pack)))
                    if b"@FOX-V" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d56(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][800080]{idd}", pack)))
                    if b"@FOX-B" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d42(.*?)28', pack)[0])).decode('utf-8')                   
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][0000FF]{idd}", pack)))
                    if b"@FOX-O" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d4f(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][FFA500]{idd}", pack)))
                    if b"@FOX-GY" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d4759(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][808080]{idd}", pack)))
                    if b"@FOX-GD" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d4744(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][FFD700]{idd}", pack)))
                    if b"@FOX-CY" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d4359(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][00FFFF]{idd}", pack)))
                    if b"@FOX-PK" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d504b(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][FF1493]{idd}", pack)))
                    if b"@FOX-DV" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d4456(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][8A2BE2]{idd}", pack)))
                    if b"@FOX-BR" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d4252(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][A52A2A]{idd}", pack)))
                    if b"@FOX-CR" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d4352(.*?)28', pack)[0])).decode('utf-8')                   
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][DC143C]{idd}", pack)))
                    if b"@FOX-TQ" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d5451(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][00CED1]{idd}", pack)))
                    if b"@FOX-OR" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d4f52(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][FF4500]{idd}", pack)))
                    if b"@FOX-DG" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d4447(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][2E8B57]{idd}", pack)))
                    if b"@FOX-LY" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d4c59(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][ADFF2F]{idd}", pack)))
                    if b"@FOX-LB" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d4c42(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][4682B4]{idd}", pack)))
                    if b"@FOX-TZ" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d545a(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][40E0D0]{idd}", pack)))
                    if b"@FOX-LV" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d4c56(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][DA70D6]{idd}", pack)))
                    if b"@FOX-BGD" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d4244(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][F4A460]{idd}", pack)))
                    if b"@FOX-TM" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d5450(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][FF6347]{idd}", pack)))
                    if b"@FOX-LM" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d4c4d(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][7FFF00]{idd}", pack)))
                    if b"@FOX-MV" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d4d56(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][BA55D3]{idd}", pack)))
                    if b"@FOX-HK" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d4854(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][FF69B4]{idd}", pack)))
                    if b"@FOX-LOR" in dataS:
                        idd = (bytes.fromhex(re.findall(r'40464f582d4f52(.*?)28', pack)[0])).decode('utf-8')
                        client.send(bytes.fromhex(send_msg_clan(f"[cُ][bَ][E9967A]{idd}", pack)))
                except:
                    pass
#############################################
                if b"/INFO_V1+" in dataS:
                         try:
                             parts = dataS.split(b"/INFO_V1+")
                             if len(parts) > 1:
                                 user_id = parts[1].split(b"\x28")[0].decode("utf-8")
                                 b = all_info_id(user_id)
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}NEGGA WAIT I'M SEARCH FOR INFO V1....", dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(b["Account Name"], dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(b["Account Level"], dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(b["Account Likes"], dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(b["Account XP"], dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(b["Account Region"], dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(b["Account Recent OB"], dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤBY CODEX TEAMㅤㅤ", dataS.hex())))
                         except Exception as e:
                             print(f"Error processing /INFO_V1+ command: {e}")
                             client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}Error processing request.", dataS.hex())))
#############################################
                elif b"/INFO_V2+" in dataS:
                         try:
                             parts = dataS.split(b"/INFO_V2+")
                             if len(parts) > 1:
                                 user_id = parts[1].split(b"\x28")[0].decode("utf-8")
                                 b = all_info_id(user_id)
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}NEGGA WAIT I'M SEARCH FOR INFO V2..", dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                                 time.sleep(1)
                                 client.send(bytes.fromhex(send_msg_clan(b["Account Banner"], dataS.hex())))
                                 time.sleep(1)
                                 client.send(bytes.fromhex(send_msg_clan(b["Account Avatar"], dataS.hex())))
                                 time.sleep(1)
                                 client.send(bytes.fromhex(send_msg_clan(b["Account Evo Badge"], dataS.hex())))
                                 time.sleep(1)
                                 client.send(bytes.fromhex(send_msg_clan(b["Account Honor Score"], dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(b["Account Character ID"], dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤBY CODEX TEAMㅤㅤ", dataS.hex())))
                         except Exception as e:
                             print(f"Error processing /INFO_V2+ command: {e}")
                             client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}Error processing request.", dataS.hex())))
#############################################;
                elif b"/INFO_V3+" in dataS:
                         try:
                             parts = dataS.split(b"/INFO_V3+")
                             if len(parts) > 1:
                                 user_id = parts[1].split(b"\x28")[0].decode("utf-8")
                                 b = all_info_id(user_id)
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}NEGGA WAIT I'M SEARCH FOR INFO V3..", dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(b["Account Create"], dataS.hex())))
                                 time.sleep(1)
                                 client.send(bytes.fromhex(send_msg_clan(b["Account Language"], dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(b["Account Last"], dataS.hex())))
                                 time.sleep(1)
                                 client.send(bytes.fromhex(send_msg_clan(b["Public Craftland Maps"], dataS.hex())))
                                 time.sleep(1)
                                 client.send(bytes.fromhex(send_msg_clan(b["Account Character ID"], dataS.hex())))
                                 time.sleep(1)
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤBY CODEX TEAMㅤㅤ", dataS.hex())))
                         except Exception as e:
                             print(f"Error processing /INFO_V3+ command: {e}")
                             client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}Error processing request.", dataS.hex())))
#############################################
                elif b"/INFO_V4+" in dataS:
                         try:
                             parts = dataS.split(b"/INFO_V4+")
                             if len(parts) > 1:
                                 user_id = parts[1].split(b"\x28")[0].decode("utf-8")
                                 b = all_info_id(user_id)
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}NEGGA WAIT I'M SEARCH FOR INFO V4..", dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(b["BR Rank Points"], dataS.hex())))
                                 time.sleep(1)
                                 client.send(bytes.fromhex(send_msg_clan(b["CS Rank Points"], dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(b["Account Booyah Pass"], dataS.hex())))
                                 time.sleep(1)
                                 client.send(bytes.fromhex(send_msg_clan(b["Account Booyah Pass Badges"], dataS.hex())))
                                 time.sleep(1)
                                 client.send(bytes.fromhex(send_msg_clan(b["Account Celebrity Status"], dataS.hex())))
                                 time.sleep(1)
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤBY CODEX TEAMㅤㅤ", dataS.hex())))
                         except Exception as e:
                             print(f"Error processing /INFO_V3+ command: {e}")
                             client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}Error processing request.", dataS.hex())))
#############################################
                elif b"/LIKES+" in dataS:
                         try:
                             parts = dataS.split(b"/LIKES+")
                             if len(parts) > 1:
                                 user_id = parts[1].split(b"\x28")[0].decode("utf-8")
                                 b = send_likes_id(user_id)
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}NEGGA WAIT I'M SEARCH FOR INFO V1....", dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(b["LikesGivenByAPI"], dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(b["LikesbeforeCommand"], dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(b["LikesafterCommand"], dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(b["UID"], dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                                 client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤBY CODEX TEAMㅤㅤ", dataS.hex())))
                         except Exception as e:
                             print(f"Error processing /LIKES+ command: {e}")
                             client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}Error processing request.", dataS.hex())))
#############################################
                elif b"/LAG" in dataS:
                    for i in range (3000000000000000):
                        client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ]Close the game quickly", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ]CODEX STARTED......", dataS.hex())))
##################EMOTES#####################
                elif b'/FX1' in dataS and '1200' in dataS.hex()[0:4]:
                        pack = dataS.hex() 
                        client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ] EMOTE 1", pack)))
                        id = dataS.hex()[12:22]
                        dor = "050000002008*100520162a1408*1088b3bbb1032a0608*"
                        raks = dor.replace('*', id)
                        MainC.send(bytes.fromhex(raks))
                elif b'/FX2' in dataS and '1200' in dataS.hex()[0:4]:
                        client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ] EMOTE 2", dataS.hex())))
                        id = dataS.hex()[12:22]
                        dor = "050000002008*100520162a1408*10aefcbab1032a0608*"
                        raks = dor.replace('*', id)
                        MainC.send(bytes.fromhex(raks))
                elif b'/FX3' in dataS and '1200' in dataS.hex()[0:4]:
                        pack = dataS.hex() 
                        client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ] EMOTE 3", pack)))
                        pack = dataS.hex()
                        id = dataS.hex()[12:22]
                        dor = "050000002008*100520162a1408*109cfbb8b1032a0608*"
                        raks = dor.replace('*', id)
                        MainC.send(bytes.fromhex(raks))
                elif b'/FX4' in dataS and '1200' in dataS.hex()[0:4]:
                        pack = dataS.hex()
                        client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ] EMOTE 4", pack)))
                        id = dataS.hex()[12:22]
                        dor = "050000002008*100520162a1408*109284bbb1032a0608*"
                        raks = dor.replace('*', id)
                        MainC.send(bytes.fromhex(raks))
                elif b'/FX5' in dataS and '1200' in dataS.hex()[0:4]:
                        pack = dataS.hex() 
                        client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ] EMOTE 5", pack)))
                        id = dataS.hex()[12:22]
                        dor = "050000002008*100520162a1408*10bbfbb8b1032a0608*"
                        raks = dor.replace('*', id)
                        MainC.send(bytes.fromhex(raks))
                elif b'/FX6' in dataS and '1200' in dataS.hex()[0:4]:
                        pack = dataS.hex()
                        client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ] EMOTE 6", pack)))
                        id = dataS.hex()[12:22]
                        dor = "050000002008*100520162a1408*10dcc2bbb1032a0608*"
                        raks = dor.replace('*', id)
                        MainC.send(bytes.fromhex(raks))
                elif b'/FX7' in dataS and '1200' in dataS.hex()[0:4]:
                        pack = dataS.hex() 
                        client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ] EMOTE 7", pack)))
                        id = dataS.hex()[12:22]
                        dor = "050000002008*100520162a1408*10d2c2bbb1032a0608*"
                        raks = dor.replace('*', id)
                        MainC.send(bytes.fromhex(raks))
                elif b'/FX8' in dataS and '1200' in dataS.hex()[0:4]:
                        pack = dataS.hex()
                        client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ] EMOTE 8", pack)))
                        pack = dataS.hex()
                        id = dataS.hex()[12:22]
                        dor = "050000002008*100520162a1408*109bfbb8b1032a0608*"
                        raks = dor.replace('*', id)
                        MainC.send(bytes.fromhex(raks))
                elif b'/FX9' in dataS and '1200' in dataS.hex()[0:4]:
                        pack = dataS.hex() 
                        client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ] EMOTE 9", pack)))
                        id = dataS.hex()[12:22]
                        dor = "050000002008*100520162a1408*1098fbb8b1032a0608*"
                        raks = dor.replace('*', id)
                        MainC.send(bytes.fromhex(raks))
                elif b"/FX_1" in dataS and '1200' in dataS.hex()[0:4]:
                            client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ] EMOTE 1", dataS.hex())))
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*10ca9bbbb1032a0608*"
                            raks = dor.replace('*', id)
                            MainC.send(bytes.fromhex(raks))
                elif b"/FX_2" in dataS and '1200' in dataS.hex()[0:4]:
                            pack = dataS.hex()
                            client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ] EMOTE 2", pack)))
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*10ca9bbbb1032a0608*"
                            raks = dor.replace('*', id)
                            MainC.send(bytes.fromhex(raks))
                elif b"/FX_3" in dataS and '1200' in dataS.hex()[0:4]:
                            pack = dataS.hex()
                            client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ] EMOTE 3", pack)))
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*109e84bbb1032a0608*"
                            raks = dor.replace('*', id)
                            MainC.send(bytes.fromhex(raks))
                elif b"/FX_4" in dataS and '1200' in dataS.hex()[0:4]:
                            pack = dataS.hex()
                            client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ] EMOTE 4", pack)))
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*109684bbb1032a0608*"
                            raks = dor.replace('*', id)
                            MainC.send(bytes.fromhex(raks))
                elif b"/FX_5" in dataS and '1200' in dataS.hex()[0:4]:
                            pack = dataS.hex()
                            client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ] EMOTE 5", pack)))
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*10d6c2bbb1032a0608*"
                            raks = dor.replace('*', id)
                            MainC.send(bytes.fromhex(raks))
                elif b"/F_1" in dataS:
                            pack = dataS.hex()
                            client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ]WEAPON EMOTE 1", pack)))
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*10fffab8b1032a0608*"
                            raks = dor.replace('*', id)
                            MainC.send(bytes.fromhex(raks))
                elif b"/F_2" in dataS:
                            pack = dataS.hex()
                            client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ]WEAPON EMOTE 2", pack)))
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*10ff8bbbb1032a0608*"
                            raks = dor.replace('*', id)
                            MainC.send(bytes.fromhex(raks))
                elif b"/F_3" in dataS:
                            pack = dataS.hex()
                            client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ]WEAPON EMOTE 3", pack)))
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*1095fbb8b1032a0608*"
                            raks = dor.replace('*', id)
                            MainC.send(bytes.fromhex(raks))
                elif b"/F_4" in dataS:
                            pack = dataS.hex()
                            client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ]WEAPON EMOTE 4", pack)))
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*108bfbb8b1032a0608*"
                            raks = dor.replace('*', id)
                            MainC.send(bytes.fromhex(raks))
                elif b"/F_5" in dataS:
                            pack = dataS.hex()
                            client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ]WEAPON EMOTE 5", pack)))
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*10edbabbb1032a0608*"
                            raks = dor.replace('*', id)
                            MainC.send(bytes.fromhex(raks))
                elif b"/F_6" in dataS:
                            pack = dataS.hex()
                            client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ]WEAPON EMOTE 6", pack)))
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*10a2fbb8b1032a0608*"
                            raks = dor.replace('*', id)
                            MainC.send(bytes.fromhex(raks))
                elif b"/F_7" in dataS:
                            pack = dataS.hex()
                            client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ]WEAPON EMOTE 7", pack)))
                            id = dataS.hex()[12:22]
                            dor = "050000002008*100520162a1408*1084fbb8b1032a0608*"
                            raks = dor.replace('*', id)
                            MainC.send(bytes.fromhex(raks))
#################SPAM EMOTE##################
                elif b"/CDX" in dataS:
                    pack = dataS.hex()
                    client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ]SPAM EMOTE STARTED..", pack)))
                    for _ in range(50):
                         id = dataS.hex()[12:22]
                         dor = "050000002008*100520162a1408*10fffab8b1032a0608*"
                         raks = dor.replace("*", id)
                         MainC.send(bytes.fromhex(raks))
                         time.sleep(2)
###############RANDOM EMOTE ################
                elif b"/RND" in dataS and "1200" in dataS.hex()[0:4]:
                    spam_emote = True
                    pack = dataS.hex()
                    client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ]SPAM RANDOM EMOTE STARTED..", dataS.hex())))
                    emotes = [
                    "050000002008*100520162a1408*10fffab8b1032a0608*",
                    "050000002008*100520162a1408*10edbabbb1032a0608*",
                    "050000002008*100520162a1408*10a2fbb8b1032a0608*",
                    "050000002008*100520162a1408*1084fbb8b1032a0608*",
                    "050000002008*100520162a1408*1098fbb8b1032a0608*",
                    "050000002008*100520162a1408*109684bbb1032a0608*",
                    "050000002008*100520162a1408*10d6c2bbb1032a0608*",
                    "050000002008*100520162a1408*10ff8bbbb1032a0608*",
                    "050000002008*100520162a1408*10fffab8b1032a0608*",
                    "050000002008*100520162a1408*1084fbb8b1032a0608*",
                    "050000002008*100520162a1408*10a2fbb8b1032a0608*",
                    "050000002008*100520162a1408*10edbabbb1032a0608*",
                    "050000002008*100520162a1408*108bfbb8b1032a0608*",
                    "050000002008*100520162a1408*1095fbb8b1032a0608*",
                    "050000002008*100520162a1408*10ff8bbbb1032a0608*",
                    "050000002008*100520162a1408*10d6c2bbb1032a0608*",
                    "050000002008*100520162a1408*109684bbb1032a0608*",
                    "050000002008*100520162a1408*109e84bbb1032a0608*",
                    "050000002008*100520162a1408*1098fbb8b1032a0608*",
                    "050000002008*100520162a1408*109bfbb8b1032a0608*",
                    "050000002008*100520162a1408*10d2c2bbb1032a0608*",
                    "050000002008*100520162a1408*10dcc2bbb1032a0608*",
                    "050000002008*100520162a1408*10bbfbb8b1032a0608*",
                    "050000002008*100520162a1408*109284bbb1032a0608*",
                     "050000002008*100520162a1408*109cfbb8b1032a0608*",
                     "050000002008*100520162a1408*10aefcbab1032a0608*",
                     "050000002008*100520162a1408*1088b3bbb1032a0608*"
    ]   
                    while spam_emote:
                        id = dataS.hex()[12:22]
                        dor = random.choice(emotes)
                        raks = dor.replace("*", id)
                        MainC.send(bytes.fromhex(raks))
                        time.sleep(2)
                elif b"@-RND" in dataS:
                    spam_emote = False
                    pack = dataS.hex()
                    client.send(bytes.            fromhex(send_msg_clan("[cُ][bَ][00ffffَ]SPAM RANDOM EMOTE ST;OPPED..", dataS.hex())))                
#############emote packet lvl100#################
                elif b'/FOX-LVL100' in dataS:
                        pack = dataS.hex() 
                        client.send(bytes.fromhex(send_msg_clan("[cُ][bَ][00ffffَ] EMOTE LVL100", pack)))
                        id = dataS.hex()[12:22]
                        dor = "050000002008*100520162a1408aae2cafb0210d7c2bbb1032a0608*"
                        raks = dor.replace('*', id)
                        MainC.send(bytes.fromhex(raks))
###########new bot emote in ente squad!!############
#                elif  '0500' in dataS.hex()[0:4] and '0515' in dataC.hex()[0:4]:
#                        time.sleep(10)
#                        pack = dataS.hex() 
#                        print("new group!...")
#                        id = dataS.hex()[12:22]
#                        dor = "050000002008*100520162a1408aae2cafb0210c1cabbb1032a0608*"
#                        raks = dor.replace('*', id)
#                        MainC.send(bytes.fromhex(raks))
#############################################
                if b"@SPAM_BACK" in dataS:
                    pack = dataS.hex()
                    client.send(bytes.fromhex(send_msg_clan("[00FF00][b][c] SPAMM BACK STARTED...", pack)))
                    pack = dataS.hex()
                    back_spam= True
                    threading.Thread(target=fox_spam_back , args=(data_join,op)).start()
                if b"@NORMAL_BACK" in dataS:
                    pack = dataS.hex()
                    client.send(bytes.fromhex(send_msg_clan("[00FF00][b][c]BACK STARTED...", pack)))
                    pack = dataS.hex()
                    back_normal = True
                    threading.Thread(target=fox_back, args=(data_join, op)).start()
#############################################
                if b"/FOX-STYLE" in dataS:
                    pack = dataS.hex()
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}FUCK GARENA!!!",pack)))
                    time.sleep(0.5)
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}PALESTIN IS FREE",pack)))
                    time.sleep(0.5)
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}CODEX TEAM",pack)))
                    time.sleep(0.5)
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}FUCK ISRAEL",pack)))
                    time.sleep(0.5)
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}Get out quickly",pack)))
                    client.send(bytes.fromhex(send_msg_clan("تم اختراقك",pack)))
                    time.sleep(0.5)
                    client.send(bytes.fromhex(send_msg_clan("[b][c][FF0000] GET OUT [ffff00] ( •ิ_•ิ)",pack)))
                    time.sleep(0.5)
                    client.send(bytes.fromhex(send_msg_clan("[FF0000]ඞ[FFFF00]ඞ[00FF00]ඞ[00FFFF]AMONG US",pack)))
                    time.sleep(0.5)
                    client.send(bytes.fromhex(send_msg_clan("[b][c][ffff00] ㉿ [00FF00] EASY KILL 〄",pack)))
                    time.sleep(0.5)
                    client.send(bytes.fromhex(send_msg_clan("[bْ][cْ][ffd319ْ]Ⓥ[00FF00ْ]",pack)))
                    client.send(bytes.fromhex(send_msg_clan(f"[b][c][FF9933]❚█══[ffd319] GYM [FF9933]══█❚",pack)))
                    time.sleep(0.5)
                    client.send(bytes.fromhex(send_msg_clan(f"[b][c][E1D9D1] UNKNOWN BRAIN [FF00FF] ♪♫♬",pack)))
                    time.sleep(0.5)
                    client.send(bytes.fromhex(send_msg_clan(f"[b][c][FFFFFF]ME ဗီူ╯[Ff0200]❤ [00FF00]╰ဗီူYOU",pack)))
                    time.sleep(0.5)
                    client.send(bytes.fromhex(send_msg_clan("""[ffffff]  ●[Ff0200] ♥[ffffff]●
/█\/▓\[FFFF00] A❤️L""",pack)))
                    time.sleep(0.5)
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}CODEX TEAM COMING",pack)))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}DARK WEB",pack)))
                    time.sleep(0.5)
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}CODEX TEAM COMING IN 2025",pack)))
                    time.sleep(0.5)
                    client.send(bytes.fromhex(send_msg_clan(f"[B][C][OOFFOD] WELCOME[FFOOOO]TOMY[FFFFOO]PROFILE",pack)))
#############################################
                if spamm and '0515' in dataC.hex()[0:4]:
                    for _ in range(9999999999):
                        remote.send(dataC)
                        time.sleep(0.05)
                if b"/INV" in dataS:
                    spamm = True
                    pack = dataS.hex()
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤSPAMM STARTEDㅤ", pack)))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤBY CODEX TEAMㅤㅤ", dataS.hex())))
#############################################
                if b"@S " in dataS:
                    pack = dataS.hex()
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤSPAM ANTIBAN STARTED!!ㅤㅤ", pack)))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤBY CODEX TEAMㅤㅤ", dataS.hex())))
                    spam = True
                    threading.Thread(target=spam_antiban, args=(client, dataS)).start()
                if b"@-S" in dataS:
                    spam = False
#############################################
                if b"@FOX-SPY" in dataS:
                    pack = dataS.hex()
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤ You are hidden, shut up!!ㅤㅤ", pack)))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤBY CODEX TEAMㅤㅤ", dataS.hex())))
                    print("send packet..")
                    MainC.send(bytes.fromhex("0503000001d01fb578313150905babcef51dd24ed75fd0a24b024bd1429646114bc22e604afd35a96fbc48710b2d9cfec4378287ec829e33a78608fd2dd138d4d24a19c00fbfdc9f15c77ff86d638b34de95bd886e3075e82d3f4a3888f9b6943463022c43fb90e229f0eaf8a788f6f766d891d99eb2c37b277144923212810b3c80d1c521790154ed270f5241adc136f2a22816e0bc84fcaf79386b27559de966aa788c184d35bbbfaa03a5f08746f8db0e73b2c91ec4515d61f689a0cad30a7cbd6c325151e879dabc43d506b3240abe41bc0d6b4416c18f68ef4af2d04c381be6bf586f6b25727c0c85c03a579137e4a6c602ef6d833dabdab3eba3a5266e5a4731fbfb1720b60f124cd8fd4fa26cc7a9fb6e0a218d8809f57b204d22fa97520aeb99007c7b71c709e53ecc688c9963e0786909152fa93f06dc93085468dae34e1609f33f7dee228fb058c6efd6846b50ac54db0aebb8f5bc2f6751f9e2886dbab41cbaf5a1d8cd88e6c13a2a2a56b613a2d32179dc3f781493a5027322ac0cb1a2d3c79d49fb12ed26230e1561df43d315a27be17b5debdba757803305252b5443f3d77cd319dde9c49a72c636d93d02bdd9597168f378aa6e41d0fd545abf8bc0883f3dac11ea27166683c7111a0f329bf6b6a5"))
                if b"#FOX-STOP" in dataS:
                    pack = dataS.hex()
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤ SPY BOT STOPED!!!!ㅤㅤ", pack)))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤBY CODEX TEAMㅤㅤ", dataS.hex())))
                    client.close()
                    remote.close()
                    restart_script()
#############################################
                if b"/FOX-YT" in dataS:
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤADD YOUTUBERS SUCCESSFULLYㅤㅤㅤㅤ", dataS.hex())))
                    client.send(bytes.fromhex(send_msg_clan(f"{get_random_color()}ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ", dataS.hex()))) 
                    yout1 = b"\x06\x00\x00\x00{\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*o\x08\x81\x80\x83\xb6\x01\x1a)[00ff00]\xd8\xb5\xd8\xa7\xd8\xa6\xd8\xaf\xe3\x85\xa4\xd8\xa7\xd9\x84\xd8\xa8\xd9\x87\xd8\xa7\xd8\xa6\xd9\x85[00ff00]2\x02ME@N\xb0\x01\x13\xb8\x01\xdc)\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\tAO'-'TEAM\xf0\x01\x01\xf8\x01\xdc\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02F"
                    yout2 = b'\x06\x00\x00\x00|\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*p\x08\xd6\xd1\xb9(\x1a![00ff00]\xef\xbc\xa8\xef\xbc\xac\xe3\x85\xa4Hassone.[00ff00]2\x02ME@G\xb0\x01\x13\xb8\x01\xcf\x1e\xd8\x01\xcc\xd6\xd0\xad\x03\xe0\x01\xed\xdc\x8d\xae\x03\xea\x01\x1d\xef\xbc\xb4\xef\xbc\xa8\xef\xbc\xa5\xe3\x85\xa4\xef\xbc\xa8\xef\xbc\xa5\xef\xbc\xac\xef\xbc\xac\xe0\xbf\x90\xc2\xb9\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
                    yout3 = b'\x06\x00\x00\x00x\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*l\x08\xe9\xa7\xe9\x1b\x1a [00ff00]DS\xe3\x85\xa4WAJIHANO\xe3\x85\xa4[00ff00]2\x02ME@Q\xb0\x01\x14\xb8\x01\xca2\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x10.DICTATORS\xe3\x85\xa4\xe2\x88\x9a\xf0\x01\x01\xf8\x01\xc4\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02+'
                    yout4 = b'\x06\x00\x00\x00z\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*n\x08\xed\xd4\xa7\xa2\x02\x1a\x1f[00ff00]M8N\xe3\x85\xa4y\xe3\x85\xa4Fouad[00ff00]2\x02ME@O\xb0\x01\x13\xb8\x01\xa9#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xdb\xdb\x8d\xae\x03\xea\x01\x0cGREAT\xe2\x80\xbfWALL\xf0\x01\x01\xf8\x01b\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\r\xd8\x023\xe0\x02\xc1\xb7\xf8\xb1\x03'
                    yout5 = b"\x06\x00\x00\x00\x84\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*x\x08\xb6\xc0\xf1\xcc\x01\x1a'[00ff00]\xd9\x85\xd9\x84\xd9\x83\xd8\xa9*\xd9\x84\xd9\x85\xd8\xb9\xd9\x88\xd9\x82\xd9\x8a\xd9\x86[00ff00]2\x02ME@G\xb0\x01\x05\xb8\x01\x82\x0b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x15\xe9\xbf\x84\xef\xbc\xac\xef\xbc\xaf\xef\xbc\xb2\xef\xbc\xa4\xef\xbc\xb3\xe9\xbf\x84\xf0\x01\x01\xf8\x01>\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x05\xd8\x02\x0e"
                    yout6 = b'\x06\x00\x00\x00\x8e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x81\x01\x08\xeb\x98\x88\x8e\x01\x1a"[00ff00]OP\xe3\x85\xa4BNL\xe3\x85\xa4\xe2\x9a\xa1\xe3\x85\xa4*[00ff00]2\x02ME@R\xb0\x01\x10\xb8\x01\xce\x16\xd8\x01\x84\xf0\xd2\xad\x03\xe0\x01\xa8\xdb\x8d\xae\x03\xea\x01\x1f\xe1\xb4\x8f\xe1\xb4\xa0\xe1\xb4\x87\xca\x80\xe3\x85\xa4\xe1\xb4\x98\xe1\xb4\x8f\xe1\xb4\xa1\xe1\xb4\x87\xca\x80\xe2\x9a\xa1\xf0\x01\x01\xf8\x01A\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01\xe0\x02\xf3\x94\xf6\xb1\x03'
                    yout7 = b"\x06\x00\x00\x00\x8e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x81\x01\x08\xb0\xa4\xdb\x80\x01\x1a'[00ff00]\xd9\x85\xd9\x83\xd8\xa7\xd9\x81\xd8\xad\xd8\xa9.\xe2\x84\x93\xca\x99\xe3\x80\xb5..[00ff00]2\x02ME@T\xb0\x01\x13\xb8\x01\xfc$\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x1d\xef\xbc\xad\xef\xbc\xa1\xef\xbc\xa6\xef\xbc\xa9\xef\xbc\xa1\xe3\x85\xa4\xe2\x8e\xb0\xe2\x84\x93\xca\x99\xe2\x8e\xb1\xf0\x01\x01\xf8\x01\xdb\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0f\xd8\x02>"
                    yout8 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xfd\x8a\xde\xb4\x02\x1a\x1f[00ff00]ITZ\xe4\xb8\xb6MOHA\xe3\x85\xa42M[00ff00]2\x02ME@C\xb0\x01\n\xb8\x01\xdf\x0f\xd8\x01\xac\xd8\xd0\xad\x03\xe0\x01\xf2\xdc\x8d\xae\x03\xea\x01\x15\xe3\x80\x9dITZ\xe3\x80\x9e\xe1\xb5\x97\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf8\x01\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0e\xd8\x026'
                    yout9 = b'\x06\x00\x00\x00w\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*k\x08\xc6\x99\xddp\x1a\x1b[00ff00]HEROSHIIMA1[00ff00]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa8\xef\xbc\xa5\xef\xbc\xb2\xef\xbc\xaf\xef\xbc\xb3\xef\xbc\xa8\xef\xbc\xa9\xef\xbc\xad\xef\xbc\xa1\xef\xa3\xbf\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
                    yout10 = b'\x06\x00\x00\x00p\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*d\x08\xde\x91\xb7Q\x1a\x1c[00ff00]SH\xe3\x85\xa4SHIMA|M[00ff00]2\x02ME@R\xb0\x01\x14\xb8\x01\xe7C\xd8\x01\xdd\xd6\xd0\xad\x03\xe0\x01\xca\xdb\x8d\xae\x03\xea\x01\tSH\xe3\x85\xa4Team\xf8\x014\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02G\xe0\x02\x89\xa0\xf8\xb1\x03'
                    yout11 = b'\x06\x00\x00\x00h\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\\\x08\xa1\x9f\xb3\xf4\x01\x1a\x1b[00ff00]2JZ\xe3\x85\xa4POWER[00ff00]2\x02ME@M\xb0\x01\x13\xb8\x01\xa5(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xec\xdb\x8d\xae\x03\xf0\x01\x01\xf8\x01\x9a\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02.\xe0\x02\xb2\xe9\xf7\xb1\x03'
                    yout12 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\xaa\xe5\xa4\xe3\x01\x1a-[00ff00]\xe3\x85\xa4\xd8\xb4\xd9\x83\xd8\xa7\xd9\x8e\xd9\x83\xd9\x80\xd9\x8a\xe3\x80\x8e\xe2\x85\xb5\xe1\xb4\x98\xe3\x80\x8f[00ff00]2\x02ME@Q\xb0\x01\x13\xb8\x01\xf2*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xaf\xdb\x8d\xae\x03\xea\x01\x15\xe2\x80\xa2\xe3\x85\xa4\xe2\x93\x8b\xe2\x92\xbe\xe2\x93\x85\xe3\x85\xa4\xe2\x80\xa2\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02e\xe0\x02\xa0\xf1\xf7\xb1\x03'
                    yout13 = b'\x06\x00\x00\x00`\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*T\x08\xd2\xbc\xae\x07\x1a%[00ff00]SYBLUS\xe3\x85\xa4\xe4\xba\x97\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4[00ff00]2\x02ME@E\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
                    yout14 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xfd\x8b\xf4\xfa\x01\x1a$[00ff00]"\xd8\xaf\xd8\xb1\xd8\xa7\xd8\xba\xd9\x88\xd9\x86\xd9\x80\xd9\x88\xd9\x81"[00ff00]2\x02ME@F\xb0\x01\x13\xb8\x01\xec \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe1\xb4\x98\xe1\xb4\x84\xe1\xb5\x80\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\xb0\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x04\xd8\x02\t\xe0\x02\xf2\x94\xf6\xb1\x03'
                    yout15 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\x90\xf6\x87\x15\x1a"[00ff00]V4\xe3\x85\xa4RIO\xe3\x85\xa46%\xe3\x85\xa4zt[00ff00]2\x02ME@M\xb0\x01\x13\xb8\x01\x95&\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb1\xdd\x8d\xae\x03\xea\x01\x0e\xe1\xb4\xa0\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x8f\xd1\x95\xf0\x01\x01\xf8\x01\xe2\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02^\xe0\x02\x85\xff\xf5\xb1\x03'
                    yout16 = b'\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xaa\x84\xc1r\x1a\x1f[00ff00]SA777RAWI\xe3\x85\xa4\xe3\x85\xa4[00ff00]2\x02ME@N\xb0\x01\x13\xb8\x01\xc8\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x0cSA7RAWI\xe3\x85\xa4TM\xf0\x01\x01\xf8\x01\xfe\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\t\xd8\x02 '
                    yout17 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xe7\xbf\xb6\x8f\x01\x1a\x1c[00ff00]SVG.NINJA\xe2\xbc\xbd[00ff00]2\x02ME@I\xb0\x01\x13\xb8\x01\x94\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x85\xdb\x8d\xae\x03\xea\x01\x15\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4???\xe3\x85\xa4\xe3\x85\xa4\xf0\x01\x01\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02?'
                    yout18 = b"\x06\x00\x00\x00\x9d\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x90\x01\x08\xa8\xe8\x91\xd7\x01\x1a.[00ff00]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe4\xba\x97\xef\xbc\xb9\xef\xbc\xb4\xe3\x85\xa4[00ff00]2\x02ME@N\xb0\x01\x13\xb8\x01\x97'\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe2\x80\xa2\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93\xf0\x01\x01\xf8\x01\xab\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02@\xe0\x02\xe9\x80\xf8\xb1\x03"
                    yout19 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9b\x94\xaa\r\x1a\x1c[00ff00]FARAMAWY_1M.[00ff00]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01X\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
                    yout20 = b'\x06\x00\x00\x00p\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*d\x08\xde\x91\xb7Q\x1a\x1c[00ff00]SH\xe3\x85\xa4SHIMA|M[00ff00]2\x02ME@R\xb0\x01\x14\xb8\x01\xe7C\xd8\x01\xdd\xd6\xd0\xad\x03\xe0\x01\xca\xdb\x8d\xae\x03\xea\x01\tSH\xe3\x85\xa4Team\xf8\x014\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02G\xe0\x02\x89\xa0\xf8\xb1\x03'
                    yout21 = b'\x06\x00\x00\x00h\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\\\x08\xa1\x9f\xb3\xf4\x01\x1a\x1b[00ff00]2JZ\xe3\x85\xa4POWER[00ff00]2\x02ME@M\xb0\x01\x13\xb8\x01\xa5(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xec\xdb\x8d\xae\x03\xf0\x01\x01\xf8\x01\x9a\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02.\xe0\x02\xb2\xe9\xf7\xb1\x03'
                    yout22 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\xaa\xe5\xa4\xe3\x01\x1a-[00ff00]\xe3\x85\xa4\xd8\xb4\xd9\x83\xd8\xa7\xd9\x8e\xd9\x83\xd9\x80\xd9\x8a\xe3\x80\x8e\xe2\x85\xb5\xe1\xb4\x98\xe3\x80\x8f[00ff00]2\x02ME@Q\xb0\x01\x13\xb8\x01\xf2*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xaf\xdb\x8d\xae\x03\xea\x01\x15\xe2\x80\xa2\xe3\x85\xa4\xe2\x93\x8b\xe2\x92\xbe\xe2\x93\x85\xe3\x85\xa4\xe2\x80\xa2\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02e\xe0\x02\xa0\xf1\xf7\xb1\x03'
                    yout23 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xfd\x8b\xf4\xfa\x01\x1a$[00ff00]"\xd8\xaf\xd8\xb1\xd8\xa7\xd8\xba\xd9\x88\xd9\x86\xd9\x80\xd9\x88\xd9\x81"[00ff00]2\x02ME@F\xb0\x01\x13\xb8\x01\xec \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe1\xb4\x98\xe1\xb4\x84\xe1\xb5\x80\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\xb0\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x04\xd8\x02\t\xe0\x02\xf2\x94\xf6\xb1\x03'
                    yout24 = b'\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xaa\x84\xc1r\x1a\x1f[00ff00]AH\xe3\x85\xa4\xe3\x85\xa4[00ff00]2\x02ME@N\xb0\x01\x13\xb8\x01\xc8\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x0cSA7RAWI\xe3\x85\xa4TM\xf0\x01\x01\xf8\x01\xfe\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\t\xd8\x02 '
                    yout25 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xe7\xbf\xb6\x8f\x01\x1a\x1c[00ff00]SVG.NINJA\xe2\xbc\xbd[00ff00]2\x02ME@I\xb0\x01\x13\xb8\x01\x94\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x85\xdb\x8d\xae\x03\xea\x01\x15\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4???\xe3\x85\xa4\xe3\x85\xa4\xf0\x01\x01\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02?'
                    yout26 = b"\x06\x00\x00\x00\x9d\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x90\x01\x08\xa8\xe8\x91\xd7\x01\x1a.[00ff00]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe4\xba\x97\xef\xbc\xb9\xef\xbc\xb4\xe3\x85\xa4[00ff00]2\x02ME@N\xb0\x01\x13\xb8\x01\x97'\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe2\x80\xa2\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93\xf0\x01\x01\xf8\x01\xab\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02@\xe0\x02\xe9\x80\xf8\xb1\x03"
                    yout27 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9b\x94\xaa\r\x1a\x1c[00ff00]FARAMAWY_1M.[00ff00]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01X\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
                    yout28 = b"\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\xaa\xdd\xf1'\x1a\x1d[00ff00]BM\xe3\x85\xa4ABDOU_YT[00ff00]2\x02ME@G\xb0\x01\x13\xb8\x01\xd4$\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1d\xe2\x80\xa2\xc9\xae\xe1\xb4\x87\xca\x9f\xca\x9f\xe1\xb4\x80\xca\x8d\xe1\xb4\x80\xd2\x93\xc9\xaa\xe1\xb4\x80\xc2\xb0\xf0\x01\x01\xf8\x01\x8e\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x07\xd8\x02\x16"
                    yout29 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9a\xd6\xdcL\x1a-[00ff00]\xe1\xb4\x8d\xcd\xa1\xcd\x9co\xe3\x85\xa4\xef\xbc\xa8\xef\xbc\xa1\xef\xbc\xa6\xef\xbc\xa9\xef\xbc\xa4\xef\xbc\xa9[00ff00]2\x02ME@H\xb0\x01\x01\xb8\x01\xe8\x07\xea\x01\x15\xe1\xb4\x8d\xcd\xa1\xcd\x9co\xc9\xb4\xef\xbd\x93\xe1\xb4\x9b\xe1\xb4\x87\xca\x80\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
                    yout30 = b'\x06\x00\x00\x00v\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*j\x08\xb6\x92\xa9\xc8\x01\x1a [00ff00]\xef\xbc\xaa\xef\xbc\xad\xef\xbc\xb2\xe3\x85\xa4200K[00ff00]2\x02ME@R\xb0\x01\x13\xb8\x01\xc3(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\n3KASH-TEAM\xf8\x012\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x06\xd8\x02\x13\xe0\x02\x89\xa0\xf8\xb1\x03'
                    yout31 = b"\x06\x00\x00\x00\x92\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x85\x01\x08\xa2\xd3\xf4\x81\x07\x1a'[00ff00]\xd8\xb3\xd9\x80\xd9\x86\xd9\x80\xd8\xaf\xd8\xb1\xd9\x8a\xd9\x84\xd8\xa71M\xe3\x85\xa4[00ff00]2\x02ME@K\xb0\x01\x13\xb8\x01\xc1 \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1a\xef\xbc\xad\xef\xbc\xa6\xef\xbc\x95\xef\xbc\xb2\xef\xbc\xa8\xe3\x85\xa4\xe1\xb4\xa0\xc9\xaa\xe1\xb4\x98\xf0\x01\x01\xf8\x01\x8c\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0e\xd8\x024\xe0\x02\x87\xff\xf5\xb1\x03"
                    yout32 = b'\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\xc5\xcf\x94\x8b\x02\x1a\x18[00ff00]@EL9YSAR[00ffff]2\x02ME@P\xb0\x01\x13\xb8\x01\x86+\xd8\x01\xa2\xd7\xd0\xad\x03\xe0\x01\x89\xae\x8f\xae\x03\xea\x01\x1d-\xc9\xaa\xe1\xb4\x8d\xe1\xb4\x8d\xe1\xb4\x8f\xca\x80\xe1\xb4\x9b\xe1\xb4\x80\xca\x9fs\xe2\xac\x86\xef\xb8\x8f\xf8\x01j\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\xe2\x02\xe0\x02\x9f\xf1\xf7\xb1\x03'
                    yout33 = b'\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\xc5\xcf\x94\x8b\x02\x1a\x18[00ff00]@EL9YSAR[00ffff]2\x02ME@P\xb0\x01\x13\xb8\x01\x86+\xd8\x01\xa2\xd7\xd0\xad\x03\xe0\x01\x89\xae\x8f\xae\x03\xea\x01\x1d-\xc9\xaa\xe1\xb4\x8d\xe1\xb4\x8d\xe1\xb4\x8f\xca\x80\xe1\xb4\x9b\xe1\xb4\x80\xca\x9fs\xe2\xac\x86\xef\xb8\x8f\xf8\x01j\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\xe2\x02\xe0\x02\x9f\xf1\xf7\xb1\x03'
                    yout34 = b'\x06\x00\x00\x00x\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*l\x08\xa9\x81\xe6^\x1a\x1e[ffff00]GRINGO\xe3\x85\xa4CRONA[00ff00]2\x02ME@J\xb0\x01\x13\xb8\x01\xd8$\xd8\x01\xd8\xd6\xd0\xad\x03\xe0\x01\x92\xdb\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\xbc\x01'
                    yout35 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\xeb\x8d\x97\xec\x01\x1a&[00ff00]\xd8\xb9\xd9\x80\xd9\x85\xd9\x80\xd8\xaf\xd9\x86\xd9\x8a\xd9\x80\xd8\xaa\xd9\x80\xd9\x88[00ff00]2\x02ME@F\xb0\x01\x13\xb8\x01\xd3\x1a\xd8\x01\xaf\xd7\xd0\xad\x03\xe0\x01\xf4\xdc\x8d\xae\x03\xea\x01\rOSIRIS\xe3\x85\xa4MASR\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02\\\xe0\x02\xf4\x94\xf6\xb1\x03'
                    yout36 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\xb4\xff\xa3\xef\x01\x1a\x1c[00ff00]ZAIN_YT_500K[00ffff]2\x02ME@K\xb0\x01\x13\xb8\x01\xa3#\xd8\x01\xa2\xd7\xd0\xad\x03\xe0\x01\xbb\xdb\x8d\xae\x03\xea\x01\x1b\xe1\xb6\xbb\xe1\xb5\x83\xe1\xb6\xa4\xe1\xb6\xb0\xe3\x85\xa4\xe1\xb5\x97\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\\\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0b\xd8\x02('
                    yout37 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\x86\xa7\x9e\xa7\x0b\x1a([00ff00]\xe2\x80\x94\xcd\x9e\xcd\x9f\xcd\x9e\xe2\x98\x85\xef\xbc\xa2\xef\xbc\xac\xef\xbc\xb2\xef\xbc\xb8[00ff00]2\x02ME@d\xb0\x01\x13\xb8\x01\xe3\x1c\xe0\x01\xf2\x83\x90\xae\x03\xea\x01!\xe3\x85\xa4\xef\xbc\xa2\xef\xbc\xac\xef\xbc\xb2\xef\xbc\xb8\xe3\x85\xa4\xef\xbc\xb4\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xad\xe3\x85\xa4\xf8\x01u\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02Y\xe0\x02\xc1\xb7\xf8\xb1\x03'
                    yout38 = b'\x06\x00\x00\x00\x85\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*y\x08\xc3\xcf\xe5H\x1a([00ff00]\xe3\x85\xa4BEE\xe2\x9c\xbfSTO\xe3\x85\xa4\xe1\xb5\x80\xe1\xb4\xb5\xe1\xb4\xb7[00ff00]2\x02ME@Q\xb0\x01\x14\xb8\x01\xffP\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x15TIK\xe2\x9c\xbfTOK\xe1\xb5\x80\xe1\xb4\xb1\xe1\xb4\xac\xe1\xb4\xb9\xf0\x01\x01\xf8\x01\xc8\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02q'
                    yout39 = b'\x06\x00\x00\x00\x94\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x87\x01\x08\x97\xd5\x9a.\x1a%[00ff00]\xd8\xb9\xd9\x86\xd9\x83\xd9\x88\xd8\xb4\xe1\xb4\x80\xc9\xb4\xe1\xb4\x8b\xe3\x85\xa4[00ff00]2\x02ME@P\xb0\x01\x13\xb8\x01\xe8(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1f\xe1\xb4\x80\xc9\xb4\xe1\xb4\x8b\xe1\xb4\x9c\xea\x9c\xb1\xca\x9c\xe3\x85\xa4\xe1\xb4\x9b\xe1\xb4\x87\xe1\xb4\x80\xe1\xb4\x8d\xf0\x01\x01\xf8\x01\xb6\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\n\xd8\x02"\xe0\x02\xf2\x94\xf6\xb1\x03'
                    yout40 = b'\x06\x00\x00\x00\x8a\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*~\x08\xf7\xdf\xda\\\x1a/[00ff00]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\xa8\xef\xbc\xaf\xef\xbc\xad\xef\xbc\xb3\xef\xbc\xa9_\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93[00ff00]2\x02ME@P\xb0\x01\x13\xb8\x01\xb9*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\x8e\x0e\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02S\xe0\x02\xc3\xb7\xf8\xb1\x03'
                    yout41 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xb5\xdd\xec\x8e\x01\x1a%[00ff00]\xd8\xa7\xd9\x88\xd9\x81\xe3\x80\x80\xd9\x85\xd9\x86\xd9\x83\xe3\x85\xa4\xe2\x9c\x93[00ff00]2\x02ME@K\xb0\x01\x13\xb8\x01\xdd#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x18\xef\xbc\xaf\xef\xbc\xa6\xe3\x85\xa4\xef\xbc\xb4\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xad\xe3\x85\xa4\xf0\x01\x01\xf8\x01\xe8\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02Q'
                    yout42 = b'\x06\x00\x00\x00\x8b\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x7f\x08\x81\xf4\xba\xf8\x01\x1a%[00ff00]\xef\xbc\xa7\xef\xbc\xa2\xe3\x85\xa4\xef\xbc\xae\xef\xbc\xaf\xef\xbc\x91\xe3\x81\x95[00ff00]2\x02ME@N\xb0\x01\x0c\xb8\x01\xbd\x11\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb1\xdd\x8d\xae\x03\xea\x01\x1a\xef\xbc\xa7\xef\xbc\xb2\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xb4__\xef\xbc\xa2\xef\xbc\xaf\xef\xbc\xb9\xf8\x018\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02-\xe0\x02\x85\xff\xf5\xb1\x03'
                    yout43 = b'\x06\x00\x00\x00o\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*c\x08\xfb\x9d\xb9\xae\x06\x1a\x1c[00ff00]BT\xe3\x85\xa4BadroTV[00ff00]2\x02ME@@\xb0\x01\x13\xb8\x01\xe7\x1c\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x91\xdb\x8d\xae\x03\xea\x01\nBadro_TV_F\xf0\x01\x01\xf8\x01\x91\x1a\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\n\xd8\x02!'
                    yout44 = b"\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xc4\xe5\xe1>\x1a'[00ff00]\xd8\xb5\xd8\xa7\xd8\xa6\xd8\xaf~\xd8\xa7\xd9\x84\xd8\xba\xd9\x86\xd8\xa7\xd8\xa6\xd9\x85[00ff00]2\x02ME@J\xb0\x01\x14\xb8\x01\xceP\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x03Z7F\xf0\x01\x01\xf8\x01\xd0\x19\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\x9c\x01"
                    yout45 = b'\x06\x00\x00\x00\x85\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*y\x08\xfd\xa4\xa6i\x1a$[00ff00]\xd8\xb2\xd9\x8a\xd9\x80\xd8\xb1\xc9\xb4\xcc\xb67\xcc\xb6\xca\x80\xe3\x85\xa4[00ff00]2\x02ME@M\xb0\x01\x13\xb8\x01\xe1(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x19\xc2\xb7\xe3\x85\xa4\xe3\x85\xa4N\xe3\x85\xa47\xe3\x85\xa4R\xe3\x85\xa4\xe3\x85\xa4\xc2\xb7\xf0\x01\x01\xf8\x01\x8f\t\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02k'
                    yout46 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xcc\xb9\xcc\xd4\x06\x1a"[00ff00]\xd8\xa8\xd9\x88\xd8\xad\xd8\xa7\xd9\x83\xd9\x80\xd9\x80\xd9\x80\xd9\x85[00ff00]2\x02ME@9\xb0\x01\x07\xb8\x01\xca\x0c\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x11*\xef\xbc\x97\xef\xbc\xaf\xef\xbc\xab\xef\xbc\xa1\xef\xbc\xad*\xf0\x01\x01\xf8\x01\xad\x05\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
                    yout47 = b'\x06\x00\x00\x00e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*Y\x08\xe8\xbd\xc9b\x1a [00ff00]\xe3\x80\x8cvip\xe3\x80\x8dDR999FF[00ff00]2\x02ME@Q\xb0\x01\x10\xb8\x01\x94\x16\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xf0\x01\x01\xf8\x01\xa0\x04\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02+'
                    yout48 = b'\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\x86\xb7\x84\xf1\x01\x1a&[00ff00]\xd8\xa2\xd9\x86\xd9\x8a\xd9\x80\xd9\x80\xd9\x84\xd8\xa7\xce\x92\xe2\x92\x91\xe3\x85\xa4[00ff00]2\x02ME@Q\xb0\x01\x13\xb8\x01\x82)\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x13\xce\x92\xe2\x92\x91\xe3\x85\xa4MAFIA\xe3\x85\xa4\xef\xa3\xbf\xf0\x01\x01\xf8\x01\x95\x04\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02W'
                    yout49 = b'\x06\x00\x00\x00u\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*i\x08\xb4\xbe\xde\x83\x02\x1a [00ff00]SPONGEBOB!\xe3\x85\xa4\xe4\xba\x97[00ff00]2\x02ME@N\xb0\x01\x14\xb8\x01\x842\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x96\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\xbd\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02{'
                    yout50 = b'\x06\x00\x00\x00u\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*i\x08\xb4\xbe\xde\x83\x02\x1a [00ff00]SPONGEBOB!\xe3\x85\xa4\xe4\xba\x97[00ff00]2\x02ME@N\xb0\x01\x14\xb8\x01\x842\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x96\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\xbd\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02{'
                    yout51 = b'\x06\x00\x00\x00v\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*j\x08\xb8\xa6\x85\xc5\x01\x1a\x1b[00ff00]DARBKA\xe3\x85\xa41M[00ff00]2\x02ME@Q\xb0\x01\x13\xb8\x01\x90(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12LAST\xe2\x80\x8f\xe3\x85\xa4POWER\xe2\x9a\xa1\xf0\x01\x01\xf8\x01\x92\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02W'
                    MainC.send(yout1)
                    MainC.send(yout2)
                    MainC.send(yout3)
                    MainC.send(yout4)
                    MainC.send(yout5)
                    MainC.send(yout6)
                    time.sleep(0.5)
                    MainC.send(yout7)
                    time.sleep(0.5)
                    MainC.send(yout8)
                    time.sleep(0.5)
                    MainC.send(yout9)
                    time.sleep(0.5)
                    MainC.send(yout10)
                    time.sleep(0.5)
                    MainC.send(yout11)
                    time.sleep(0.5)
                    MainC.send(yout12)
                    time.sleep(0.5)
                    MainC.send(yout13)
                    time.sleep(0.5)
                    MainC.send(yout14)
                    time.sleep(0.5)
                    MainC.send(yout15)
                    time.sleep(0.5)
                    MainC.send(yout16)
                    time.sleep(0.5)
                    MainC.send(yout17)
                    time.sleep(0.5)
                    MainC.send(yout18)
                    MainC.send(yout19)
                    MainC.send(yout20)
                    MainC.send(yout21)
                    MainC.send(yout22)
                    MainC.send(yout23)
                    MainC.send(yout24)
                    MainC.send(yout25)
                    MainC.send(yout26)
                    MainC.send(yout28)
                    MainC.send(yout29)
                    MainC.send(yout30)
                    MainC.send(yout31)
                    MainC.send(yout32)
                    MainC.send(yout33)
                    MainC.send(yout34)
                    MainC.send(yout35)
                    MainC.send(yout36)
                    MainC.send(yout37)
                    MainC.send(yout38)
                    MainC.send(yout39)
                    MainC.send(yout40)
                    MainC.send(yout41)
                    MainC.send(yout42)
                    MainC.send(yout43)
                    MainC.send(yout44)
                    MainC.send(yout45)
                    MainC.send(yout46)
                    MainC.send(yout47)
                    MainC.send(yout48)
                    MainC.send(yout49)
                    MainC.send(yout50)
                    MainC.send(yout51) 
#############################################
#############################################
                if client.send(dataS) <= 0:
                    print("Failed to send data to client.")
                    break
    except Exception as e:
        print(f"ERROR IN exchange_loop: {e}")
##################SPAM BACK##################
def fox_spam_back(data_join, op):
        global back_spam
        while back_spam == True:
            for _ in range(1000):
                op.send(data_join)
                time.sleep(2.5)              
################RUTERN BACK##################
def fox_back(data_join, op):
        global back_normal
        while back_normal  == True:
             op.send(data_join)
             time.sleep(999.0) 
####################################
def spam_antiban(client, dataS):
        for _ in range(50):
            try:
                client.send(dataS)
                time.sleep(0.5)
            except Exception as e:
                print(f"Error in spam_antiban: {e}")
                break
#############################################
def restart_script():
    time.sleep(3)
    os.execl(sys.executable, sys.executable, *sys.argv)
################START BOT####################
def run(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        s.bind((host, port))
        s.listen()
        print(f"{COLOR_YELLOW}Proxy running on ⟩⟩ : {COLOR_MAGENTA}{COLOR_BOLD}{host}, {COLOR_BOLD}{port}")
        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=handle_client, args=(conn,))
            t.start()
    except Exception as e:
        print(f"ERROR IN run: {e}")
if __name__ == "__main__":
    run("127.0.0.1", 1080)