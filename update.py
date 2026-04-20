import os
import subprocess
import time



#============================================= DEF'S OPÇÃO 1 =================================================================#"

def Syu():
    barra(); print("\033[38;5;208m             ----- Updating System -----  \033[0m"); barra(); time.sleep(0.4)
    comandos = [
    ("yay", ["yay", "-Syu"]),
    ("flatpak", ["flatpak", "update", "-y"]),
    ("clear yay cache", ["yay", "-Scc", "--noconfirm"]),
    ("clear pacman cache", ["sudo", "pacman", "-Scc", "--noconfirm"]),
    ("clear orphans", "sudo pacman -Rns $(pacman -Qtdq)")
    ]

    for nome, cmd in comandos:
        try:
            subprocess.run(cmd, shell=isinstance(cmd, str), check=True)
            print(f"[ok] {nome}")
        except subprocess.CalledProcessError:
            print(f"[erro] {nome}")



#============================================= DEF'S OPÇÃO 2 =================================================================#"

def speedtest_cli():
    audio_dangan_foward()
    print("\n\033[1;32mChecking speedtest-cli Instalation...\033[0m")
    subprocess.run("pacman -Qq speedtest-cli >/dev/null || sudo pacman -S --noconfirm speedtest-cli", shell=True)
    print("\033[1;32m Inicializing Speedtest...\n\033[0m")
    subprocess.run(["speedtest-cli"])
    confirmation()

def restart_network():
    audio_dangan_foward()
    print("\n\033[1;32mRestarting Network Manager...\033[0m")
    subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])
    print("\n\033[1;32mWifi conection restarted.\033[0m")
    confirmation()

def ip_info():
    audio_dangan_foward()
    print("\n\033[1;38;5;120m--- IP INFO ---\033[0m")
    try:
        ip = subprocess.check_output(
            r"ip route get 1.1.1.1 | grep -oP 'src \K\S+'",
            shell=True
        ).decode().strip()
        print(f"Local IP: {ip}")
    except:
        print("Local IP: Unable to get it.")
    confirmation()
#============================================= DEF'S OPÇÃO 3 =================================================================#"


def download_utilitaries():
    audio_dangan_foward();
    comando = '''
    sudo pacman -S --needed yay python xorg-server curl speedtest-cli libreoffice-fresh git python-pip python thunderbird kitty nemo vlc flatpak zip fuse2 &&

    yay -S --needed shortwave &&

    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo &&
    flatpak install -y flathub io.github.brunofin.Cohesion org.localsend.localsend_app com.brave.Browser app.ytmdesktop.ytmdesktop io.missioncenter.MissionCenter io.github.kolunmi.Bazaar'''

    try:
        subprocess.run(comando, shell=True, check=True)
        print("Instalation Over.")
    except subprocess.CalledProcessError:
        print("Error Durring Instalation.")

def download_gaming():
    audio_dangan_foward();
    comando = '''
    sudo pacman -S --needed steam mangohud gamemode prismlauncher
    '''
    try:
        subprocess.run(comando, shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Cucumber")

def download_worktools():
    audio_dangan_foward()
    comando = '''
    sudo pacman -S --needed yay python nmap wget python-pip krita neofetch obs-studio vim vesktop pycharm-community-edition virtualbox virtualbox-host-modules-arch &&

    yay -S --needed ani-cli google-earth-pro &&

    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo &&
    flatpak install -y flathub com.visualstudio.code us.zoom.Zoom it.mijorus.gearlever com.github.tchx84.Flatseal
    '''

    try:
        subprocess.run(comando, shell=True, check=True)
        print("Instalation Over.")
    except subprocess.CalledProcessError:
        print("Error During Installation.")

def show_packages():
    print("\n=== UTILITARIES ===")
    print("pacman: yay, python, xorg-server,curl, libreoffice-fresh, git, python-pip, thunderbird, kitty, nemo, vlc, flatpak, zip, fuse2")
    print("yay: shortwave")
    print("flatpak: io.github.brunofin.Cohesion, org.localsend.localsend_app, com.brave.Browser, app.ytmdesktop.ytmdesktop, io.missioncenter.MissionCenter, io.github.kolunmi.Bazaar")

    print("\n=== GAMING ===")
    print("pacman: steam, mangohud, gamemode, prismlauncher")

    print("\n=== WORKTOOLS ===")
    print("pacman: yay, python, wget, python-pip, nmap, krita, neofetch, obs-studio, vim, vesktop, pycharm-community-edition, virtualbox, virtualbox-host-modules-arch")
    print("yay: ani-cli, google-earth-pro")
    print("flatpak: com.visualstudio.code, us.zoom.Zoom, it.mijorus.gearlever, com.github.tchx84.Flatseal")




#============================================= DEF'S OPÇÃO 4 =================================================================#"

def list_components():
    clear_console();      audio_components();   barra();                print("\033[1;38;5;208m                  --- COMPONENTS ---                          \033[0m");  barra()
    time_start= time.time();    os.system("inxi -F");   time_end=time.time();
    barra();print(f"\033[1;93mElapsed time: {time_start - time_end:.4f}\033[0m");barra();confirmation()

#============================================= DEF'S OPÇÃO 5 =================================================================#"

def power_menu():
    opc5_menu_print()
    opc = input("    \033[38;5;208mOption: \033[0m");


    if opc == "1":
        audio_fastfetch_down();opc = input("      \033[31mAre you sure \033[32m(y/n)\033[31m: \033[0m")
        if opc == "y":
            os.system("shutdown now")
        else:
            clear_console(); audio_dangan_foward_2();print("\033[1;32mReturning...\033[0m");time.sleep(0.7)
    elif opc == "2":
        audio_fastfetch_down(); opc = input("      \033[31mAre you sure \033[32m(y/n)\033[31m: \033[0m")
        if opc == "y":
            os.system("reboot")
        else:
            clear_console(); audio_dangan_foward_2();print("\033[1;32mReturning...\033[0m");time.sleep(0.7)
    elif opc == "3":
            audio_dangan_foward_2();os.system("systemctl suspend")
    else:
        audio_dangan_back();print("\033[1;32mReturning...\033[0m");time.sleep(0.7)





#============================================= DEF'S OPÇÃO 6 =================================================================#"

def run_ani_cli():
    try:
        subprocess.run(["ani-cli"], check=True)
    except FileNotFoundError:
        print("\033[1;31mError: ani-cli not installed.\033[0m")
        print("\033[1;32mReturning...\033[0m");time.sleep(1)
    except subprocess.CalledProcessError:
        print("\033[1;31mUnable to run ani-cli.\033[0m")
        print("\033[1;32mReturning...\033[0m");time.sleep(1)

#============================================= DEF'S OPÇÃO 7 =================================================================#"


def update_config_fish():
    origem = os.path.expanduser("~/c.OS_PyManager/Assets/etc/Apply_Console_Config.txt")
    destino = "/usr/share/cachyos-fish-config/cachyos-config.fish"

    try:
        with open(origem, "r") as f:
            conteudo = f.read()
        processo = subprocess.run(
            ["sudo", "tee", destino],
            input=conteudo,
            text=True
        )
        if processo.returncode == 0:
            print("Sucess!")
        else:
            print("Error")
    except Exception as e:
        print(f"Error: {e}")

def configure_kitty(destino=None):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        origem = os.path.join(base_dir, "Assets", "etc", "kitty.conf")

        if destino is None:
            destino = os.path.expanduser("~/.config/kitty/kitty.conf")

        with open(origem, "r") as f:
            conteudo = f.read()

        processo = subprocess.run(
            ["sudo", "tee", destino],
            input=conteudo,
            text=True,
            capture_output=True
        )

        if processo.returncode == 0:
            print("kitty.conf atualizado")
        else:
            print(f"Error: {processo.stderr}")

    except Exception as e:
        print(f"Error: {e}")

def open_kitty_conf():
    audio_dangan_foward_2()
    caminho = os.path.expanduser("~/.config/kitty/kitty.conf")
    subprocess.Popen(["kate", caminho])

#============================================= DEF'S OPÇÃO 8 =================================================================#"

def create_fastfetch():
    caminho_dir = os.path.expanduser("~/.config/fastfetch")
    os.makedirs(caminho_dir, exist_ok=True)

    caminho_arquivo = os.path.join(caminho_dir, "config.jsonc")
    template = os.path.join(
    os.path.expanduser("~"),
    "c.OS_PyManager",
    "Assets",
    "etc",
    "Apply_FastFetch.txt"
    )
    with open(template, "r", encoding="utf-8") as f:
        conteudo = f.read()
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo)

def configure_ascii():
    audio_dangan_foward_2()
    os.system("xdg-open ~/.config/fastfetch/ascii.txt")

def create_new_ascii():
    caminho = os.path.expanduser("~/.config/fastfetch/ascii.txt")
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    arte = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠶⣦⢀⢠⣔⡶⠖⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⣤⡴⣲⣽⣛⢺⣧⣄⡀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⡌⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⡿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡳⡀⠙⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠛⣾⣿⣿⣿⡟⡴⢹⣿⣿⣿⡟⡜⢿⣿⣿⣧⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⡄⣿⣿⡿⠋⠘⠛⢆⣽⡿⠏⠌⠚⠊⢿⣿⣿⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣧⢹⣿⡇⣿⠁⠀⣴⣬⣶⡇⠀⣼⠃⠈⢿⡇⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡻⣿⢹⣿⣾⣿⡿⢿⣷⣾⢟⡀⣼⢊⣸⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠣⢉⢙⢛⡛⠋⣭⡅⣞⣃⠃⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡴⠓⠠⣰⣆⠎⡀⠡⠧⡟⣎⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠰⡅⠠⠁⠁⣶⡇⢷⠶⢪⣶⡇⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀
⠀⠀⠀⠀⠀⢠⠇⠣⣀⠁⠂⠿⠧⠀⢂⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀
⠀⠀⠀⠀⡸⡁⠀⡀⠈⠉⠠⠐⡀⢀⠈⡻⣿⣇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀
⠀⠀⠀⢮⣈⠹⢷⢠⣬⣀⣁⣒⣤⢠⡶⡁⢿⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⢸⠷⣮⣭⢘⡛⣛⡛⠴⡈⠀⠀⢸⣿⣿⣿⣿⣿⣿⡯⢸⣿⡏⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠀⠀⡞⢻⠀⠀⠀⡗⠀⠀⣸⣿⣿⣿⣿⣿⡿⠁⣿⠟⠈⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠀⡸⠀⢸⠀⠀⢸⠀⢀⣼⣿⣿⣿⠿⠛⠀⠀⠜⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣀⣸⠀⠀⠀⢧⣀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

    with open(caminho, "w", encoding="utf-8") as f:
        f.write(arte)

#============================================= Menu's Print's =================================================================#"

# ---- MENU PRINCIPAL:
def main_menu_print():
    clear_console()
    print(f"\033[1;38;5;208m  ----< {time.strftime('%H:%M')} >----< Pinalto's CachyOS Manager >-------\033[0m"); barra()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mComplete System Update\033[0m                          |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mNetwork Tools\033[0m                          |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mSetup Options\033[0m                                   |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m4 ➜\033[0m \033[1;36mList Machine Components\033[0m                         |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m5 ➜\033[0m \033[1;36mPower Options\033[0m                                   |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m6 ➜\033[0m \033[1;36mAnime Player\033[0m                                    |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m7 ➜\033[0m \033[1;36mTerminal Options\033[0m                                |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m8 ➜\033[0m \033[1;36mFastFetch Options\033[0m                               |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mQuit\033[0m                                            |\033[0m")
    barra()

def opc2_menu_print():
    clear_console()
    print(f"\033[1;38;5;208m                 Configuration Menu...\033[0m"); barra()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mNetwork Speedtest\033[0m                               |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mRestart Wifi Network\033[0m                            |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mShow Local IP\033[0m                                   |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |\033[0m");   barra()


def opc3_menu_print():
    clear_console()
    print(f"\033[1;38;5;208m                 Setup Menu...\033[0m"); barra()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mDownload Utilitaries Packages\033[0m                   |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mDownload Gaming Packages\033[0m                        |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mDownload Worktools Packages\033[0m                     |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m4 ➜\033[0m \033[1;36mPackages Info:\033[0m                                  |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |\033[0m")
    barra()

def opc5_menu_print():
    audio_dangan_foward(); print("\033[38;5;208m             ----- Power Options -----  \033[0m"); barra()
    print(" |  \033[1;38;5;208m1 ➜\033[0m \033[1;36mPower Off\033[0m                                       |")
    print(" |                                                      |")
    print(" |  \033[1;38;5;208m2 ➜\033[0m \033[1;36mReboot\033[0m                                          |")
    print(" |                                                      |")
    print(" |  \033[1;38;5;208m3 ➜\033[0m \033[1;36mSuspend\033[0m                                         |")
    print(" |                                                      |")
    print(" |  \033[1;38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |")
    barra()

def opc7_menu_print():
    clear_console();audio_dangan_foward()
    print(f"\033[1;38;5;208m                 Terminal Menu...\033[0m"); barra()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mOpen Fish Terminal.conf\033[0m                         |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mSetup Custom Fish Terminal Config\033[0m               |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mOpen Kitty Terminal Conf\033[0m                        |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m4 ➜\033[0m \033[1;36mSetup Custom Kitty Terminal Conf\033[0m                |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m5 ➜\033[0m \033[1;36mKitty Themes\033[0m                                    |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |\033[0m")
    barra()

def opc8_menu_print():
    clear_console()
    print(f"\033[1;38;5;208m                 FastFetch Menu...\033[0m"); barra()
    print("\033[1m |  \033[38;5;208m1 ➜\033[0m \033[1;36mFastFetch\033[0m                                       |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m2 ➜\033[0m \033[1;36mOpen FastFetch Ascii.txt\033[0m                        |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m3 ➜\033[0m \033[1;36mSetup FastFetch Ascii Art\033[0m                       |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m4 ➜\033[0m \033[1;36mOpen Fastfetch.json\033[0m                             |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m5 ➜\033[0m \033[1;36mSetup Fastfetch json\033[0m                            |\033[0m")
    print("\033[1m |                                                      |\033[0m")
    print("\033[1m |  \033[38;5;208m0 ➜\033[0m \033[1;31mLeave\033[0m                                           |\033[0m")
    barra()


#============================================= SONS UI  ============================================================================
#    AVANÇAR
def audio_dangan_foward():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_audio = os.path.join(base_dir, "Assets", "Sounds", "audio_dangan_foward.flac")
    os.system(f'ffplay -nodisp -autoexit -loglevel quiet -af "volume=0.2" "{caminho_audio}" > /dev/null 2>&1 &')
def audio_dangan_foward_2():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_audio = os.path.join(base_dir, "Assets", "Sounds", "audio_dangan_foward_2.wav")
    os.system(f'ffplay -nodisp -autoexit -loglevel quiet -af "volume=0.2" "{caminho_audio}" > /dev/null 2>&1 &')
def audio_dangan_back():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_audio = os.path.join(base_dir, "Assets", "Sounds", "audio_dangan_back.flac")
    os.system(f'ffplay -nodisp -autoexit -loglevel quiet -af "volume=0.2" "{caminho_audio}" > /dev/null 2>&1 &')

#    FASTFETCH SFX
def audio_fastfetch_up():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_audio = os.path.join(base_dir, "Assets", "Sounds", "fastfetch_up.flac.mp3")
    os.system(f'ffplay -nodisp -autoexit -loglevel quiet "{caminho_audio}" > /dev/null 2>&1 &')
def audio_fastfetch_down():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_audio = os.path.join(base_dir, "Assets", "Sounds", "fastfetch_out.mp3")
    os.system(f'ffplay -nodisp -autoexit -loglevel quiet "{caminho_audio}" > /dev/null 2>&1 &')

#    MENU IN/OUT SFX
def audio_main_menu_leave():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_audio = os.path.join(base_dir, "Assets", "Sounds", "audio_main_menu_leave.wav")
    os.system(f'ffplay -nodisp -autoexit -loglevel quiet -af "volume=0.05" "{caminho_audio}" > /dev/null 2>&1 &')
def audio_main_menu_leave_2():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_audio = os.path.join(base_dir, "Assets", "Sounds", "audio_main_menu_leave_2.mp3")
    os.system(f'ffplay -nodisp -autoexit -loglevel quiet -af "volume=0.3" "{caminho_audio}" > /dev/null 2>&1 &')
def audio_main_menu_enter():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    audio1 = os.path.join(base_dir, "Assets", "Sounds", "audio_main_Menu_open_1.wav")
    audio2 = os.path.join(base_dir, "Assets", "Sounds", "audio_main_menu_open_2.wav")
    os.system(f'ffplay -nodisp -autoexit -loglevel quiet -af "volume=0.2" "{audio1}" > /dev/null 2>&1 &')
    time.sleep(0.2)
    os.system(f'ffplay -nodisp -autoexit -loglevel quiet -af "volume=0.2" "{audio2}" > /dev/null 2>&1 &')

#    COMPONENTS LISTING
def audio_components():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    audio1 = os.path.join(base_dir, "Assets", "Sounds", "audio_components_1.wav")
    audio2 = os.path.join(base_dir, "Assets", "Sounds", "audio_components_2.mp3")
    os.system(f'ffplay -nodisp -autoexit -loglevel quiet -af "volume=0.4" "{audio1}" > /dev/null 2>&1 &')
    os.system(f'ffplay -nodisp -autoexit -loglevel quiet -af "volume=0.2" "{audio2}" > /dev/null 2>&1 &')










#=============================================  Developer Menu  ===================================================================





def developer_menu():
    clear_console();      print(time.strftime("%H:%M"))
    print(f"==Developer Test Menu=====\n1 - audio_dangan_foward: \n2 - Audio_Dangan_Back:\n3 - Audio_Dangan_Foward_2:\n4 - Audio_Fastfetch_Down:\n5 - Audio_Fastfetch_up:\n6 - Audio_Main_Menu_Enter:\n7 - audio_main_menu_leave:\n8 - Components sqnc:\n9 - main_menu_leave_2")


    print("\033[31mTexto vermelho\033[0m")
    print("\033[32mTexto verde\033[0m")
    print("\033[1;34mAzul negrito\033[0m")
    print("\033[1;38;5;120m1 ==>\033[0m \033[1;38;5;120mDownload Utilitaries Packages\033[0m\n")
    print("\033[1;37m2 ==>\033[0m \033[1;37mDownload Gaming Packages\033[0m\n")
    print("\033[1;34m2 ==>\033[0m \033[1;34mDownload Gaming Packages\033[0m\n")
    print("\033[1;31mVermelho\033[0m")
    print("\033[1;32mVerde\033[0m")
    print("\033[1;33mAmarelo\033[0m")
    print("\033[1;34mAzul\033[0m")
    print("\033[1;35mMagenta\033[0m")
    print("\033[1;36mCiano (azul claro)\033[0m")
    print("\033[1;37mBranco\033[0m")
    print("\033[1;38;5;196mVermelho forte\033[0m")
    print("\033[1;38;5;208mLaranja\033[0m")
    print("\033[1;38;5;226mAmarelo vivo\033[0m")
    print("\033[1;38;5;46mVerde neon\033[0m")
    print("\033[1;38;5;120mVerde bebê\033[0m")
    print("\033[1;38;5;39mAzul claro vivo\033[0m")
    print("\033[1;38;5;27mAzul escuro forte\033[0m")
    print("\033[1;38;5;93mRoxo claro\033[0m")
    print("\033[1;38;5;201mRosa\033[0m")
    while True:
        opc = input("\033[38;5;208mOption: \033[0m")
        if opc == "1":
            audio_dangan_foward()
        elif opc == "2":
            audio_dangan_back()
        elif opc == "3":
            audio_dangan_foward_2()
        elif opc == "4":
            audio_fastfetch_up()
        elif opc == "5":
            audio_fastfetch_down()
        elif opc == "6":
            audio_main_menu_enter()
        elif opc == "7":
            audio_main_menu_leave()
        elif opc == "8":
            audio_components()
        elif opc == "9":
            audio_main_menu_leave_2()
        else:
            print("Saindo")
            time.sleep(0.2)
            break















#============================================= PEQUENAS DEF's ======================================================================

def barra():
    print("\033[1m#========================================================#\033[0m")

def clear_console():
    os.system("clear")

def fastfetch():
    os.system("fastfetch")

def confirmation():
    resposta = input("     \033[32mcontinue...\033[0m")
    audio_dangan_back()

def confirmation_power():
    return input("\033[31mAre you sure \033[32m(y/n)\033[31m: \033[0m").lower() == "y"

def leave_menu():
    audio_dangan_back();          print("\033[31mLeaving...\033[0m")

def all_done():
    audio_dangan_foward_2();    print("\033[32mAll Done!\033[0m");         time.sleep(1)













#============================================= MAIN NAVIGATOR ====================================================================================

def menu():
    cont1 = 0
    while cont1 == 0:
        main_menu_print()
        opc = input("    \033[1;38;5;208mOption: \033[0m")

#=== menu option 1

        if opc == "1":
            time_start = time.time()
            audio_dangan_foward();clear_console()
            Syu()
            audio_dangan_foward_2()

            time_end = time.time();barra();         print(f"\033[1;93mElapsed time: {time_start - time_end:.4f}\033[0m")
            barra();confirmation()

#=== menu option 2

        elif opc == "2":
            audio_dangan_foward()
            while True:

                opc2_menu_print();        opc = input("    \033[38;5;208mOption: \033[0m")
                if opc == "1":
                   speedtest_cli()
                elif opc == "2":
                    restart_network()
                elif opc == "3":
                    ip_info()
                else:
                    leave_menu();time.sleep(0.6);  break

#=== menu option 3

        elif opc == "3":
            audio_dangan_foward()
            clear_console()
            while True:

                opc3_menu_print()
                opc = input("    \033[38;5;208mOption: \033[0m")


                if opc == "1":
                    download_utilitaries()
                    all_done()

                elif opc == "2":
                    download_gaming()
                    all_done()
                elif opc == "3":
                    download_worktools()
                    all_done()

                elif opc == "4":
                    audio_dangan_foward();      show_packages();                        create_new_ascii()
                    audio_dangan_foward_2();    confirmation();

                elif opc == "0":
                    leave_menu();       time.sleep(0.6);            break
                else:
                    leave_menu();       time.sleep(0.6);            break

#=== menu option 4

        elif opc == "4":
            clear_console();  list_components()

#=== menu option 5

        elif opc == "5":
            clear_console(); power_menu()
#=== menu option 6
        elif opc == "6":
            audio_dangan_foward();run_ani_cli();audio_dangan_back()
#=== menu option 7
        elif opc == "7":
            while True:
                opc7_menu_print();
                opc = input("    \033[1;38;5;208mOption: \033[0m")
                if opc == "1":
                    audio_dangan_foward_2();   subprocess.run(["kate", "/usr/share/cachyos-fish-config/cachyos-config.fish"])
                elif opc == "2":
                    audio_dangan_foward();      update_config_fish()
                    all_done()

                elif opc == "3":
                    audio_dangan_foward();      open_kitty_conf()
                    all_done()

                elif opc == "4":
                        audio_dangan_foward();      configure_kitty()
                        all_done()
                elif opc == "5":
                    os.system("kitten themes");
                else:
                   leave_menu() ;   time.sleep(0.6);      break

#=== menu option 8
        elif opc == "8":
             while True:
                opc8_menu_print();        opc = input("    \033[38;5;208mOption: \033[0m")
                home = os.path.expanduser("~")

                if opc == "1":
                    audio_fastfetch_up(); fastfetch()
                    tungtung = input(":")
                    audio_fastfetch_down()

                elif opc == "2":
                    audio_dangan_foward_2()
                    configure_ascii()

                elif opc == "3":
                    audio_dangan_foward();      create_new_ascii()
                    all_done()

                elif opc == "4":
                    audio_dangan_foward_2()
                    config_fastfetch = os.path.join(home, ".config/fastfetch/config.jsonc")
                    subprocess.run(["kate", config_fastfetch])
                elif opc == "5":
                    audio_dangan_foward()
                    create_fastfetch()
                    all_done()
                else:
                    leave_menu;time.sleep(0.6);  break


#=== menu extras
        elif opc == "9":
            developer_menu()


        elif opc == "0":
            audio_main_menu_leave_2();     cont1 += 1;                print("      \033[31mGoodbye...\033[0m")
            time.sleep(0.8); clear_console()
        else:
            audio_main_menu_leave();   print("  \033[31mSelect Valid Option...\033[0m");   time.sleep(0.5)
#===================================================== MAIN ====================================================#"

def main():
    audio_main_menu_enter(); barra(); menu()

"#===================================================================================================================#"

main()
