import os
import subprocess
import webbrowser
import pyautogui
from datetime import datetime

class SystemControllerLinux:
    """Comandos do sistema operacional para Linux."""

    def __init__(self):
        self.command_map = {
            # comandos do sistema
            "desligar": self.shutdown,
            "reiniciar": self.restart,
            "cancelar": self.cancel_shutdown,
            "suspender": self.suspend,

            # navegação web
            "fechar navegador": self.close_browser,
            "abrir navegador": self.open_browser,
            "abrir youtube": lambda: self.open_website("https://www.youtube.com"),
            "abrir google": lambda: self.open_website("https://www.google.com"),
            "abrir github": lambda: self.open_website("https://www.github.com"),
            "abrir gmail": lambda: self.open_website("https://mail.google.com"),
            "abrir linkedin": lambda: self.open_website("https://www.linkedin.com"),
            "abrir whatsapp": lambda: self.open_website("https://web.whatsapp.com"),
            "abrir instagram": lambda: self.open_website("https://www.instagram.com"),
            "abrir facebook": lambda: self.open_website("https://www.facebook.com"),
            "abrir twitter": lambda: self.open_website("https://www.twitter.com"),
            "abrir netflix": lambda: self.open_website("https://www.netflix.com"),
            "abrir prime video": lambda: self.open_website("https://www.primevideo.com"),
            "abrir spotify": lambda: self.open_website("https://www.spotify.com"),

            # cotidiano
            "minimizar": self.minimize_all,
            "fechar janela": self.close_window,
            "calculadora": self.open_calculator,
            "bloco de notas": self.open_text_editor,
            "explorador": self.open_explorer,
            "vs code": self.open_vscode,
            "print screen": self.screenshot,
            "que horas são": self.tell_time,
            "que dia é hoje": self.tell_date,
            "conte-me uma piada": self.tell_joke,
        }

    def execute_command(self, command):
        command = command.lower()
        for key, func in self.command_map.items():
            if key in command:
                return func()
        return "Error 404: Comando não encontrado."

    # ===== Comandos do sistema =====
    def shutdown(self):
        """Desliga o computador (Linux)."""
        os.system("shutdown now")
        return "Desligando o computador."

    def restart(self):
        """Reinicia o computador (Linux)."""
        os.system("reboot")
        return "Reiniciando o computador."

    def cancel_shutdown(self):
        """Cancela desligamento/reinício (Linux)."""
        os.system("shutdown -c")
        return "Desligamento ou reinício cancelado."

    def suspend(self):
        """Suspende o computador (Linux)."""
        os.system("systemctl suspend")
        return "Colocando o computador em suspensão."

    # ===== Navegação web =====
    def open_browser(self):
        """Abre o navegador padrão."""
        webbrowser.open("https://www.google.com")
        return "Abrindo o navegador."

    def close_browser(self):
        """Fecha navegadores comuns no Linux."""
        # Aqui fecha navegadores mais comuns, adapte conforme necessário
        os.system("pkill firefox")
        os.system("pkill chrome")
        os.system("pkill chromium")
        os.system("pkill brave")
        return "Navegadores fechados."

    def open_website(self, url):
        webbrowser.open(url)
        return f"Abrindo o site: {url}"

    # ===== Programas comuns =====
    def minimize_all(self):
        """Minimiza todas as janelas (usando wmctrl)."""
        # É preciso ter o wmctrl instalado para isso funcionar
        os.system("wmctrl -k on")
        return "Janelas minimizadas."

    def close_window(self):
        """Fecha a janela ativa."""
        pyautogui.hotkey("alt", "f4")
        return "Janela fechada."

    def open_calculator(self):
        """Abre a calculadora padrão (gnome-calculator)."""
        subprocess.Popen(["gnome-calculator"])
        return "Abrindo a calculadora."

    def open_text_editor(self):
        """Abre o editor de texto padrão (gedit)."""
        subprocess.Popen(["gedit"])
        return "Abrindo o editor de texto."

    def open_explorer(self):
        """Abre o explorador de arquivos padrão (nautilus)."""
        subprocess.Popen(["nautilus"])
        return "Abrindo o explorador de arquivos."

    def open_vscode(self):
        """Abre o Visual Studio Code."""
        subprocess.Popen(["code"])
        return "Abrindo o VS Code."

    # ===== Ferramentas úteis =====
    def screenshot(self):
        """Tira um print da tela usando pyautogui."""
        filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        pyautogui.screenshot(filename)
        return f"Captura de tela salva como {filename}."

    def tell_time(self):
        now = datetime.now().strftime("%H:%M:%S")
        return f"Agora são {now}."

    def tell_date(self):
        today = datetime.now().strftime("%d/%m/%Y")
        return f"Hoje é {today}."

    def tell_joke(self):
        return "Por que o livro foi ao médico? Porque estava com dor de cabeça... de tanto pensar!"
