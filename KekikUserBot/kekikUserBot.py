# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from botAlani import kekikUserBot

from rich.console import Console
import sys
from pyrogram import __version__
from pyrogram.api.all import layer

konsol = Console()

def hata (yazi):
   konsol.print(yazi, style="bold red")
def bilgi (yazi):
   konsol.print(yazi, style="blue")
def basarili (yazi):
   konsol.print(yazi, style="bold green")
def onemli (yazi):
   konsol.print(yazi, style="bold cyan")
def soru (soru):
   return konsol.input(f"[bold yellow]{soru}[/]")
def logo ():
   surum = f"{str(sys.version_info[0])}.{str(sys.version_info[1])}"
   konsol.print(f"\t[bold blue]@kekikUserBot[/] [yellow]:bird:[/]\t[bold red]Python: [/][i]{surum}[/]")

logo()
basarili(f"kekikUserBot v{__version__} pyrogram tabanında çalışıyor, {layer} katman başlatıldı...")

if __name__ == '__main__':
   kekikUserBot.run()