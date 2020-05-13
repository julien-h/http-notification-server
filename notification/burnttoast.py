import subprocess

def start():
    pass


def stop():
    pass


def notify(title, description=""):
    powershell_special_chars = str.maketrans({'"': '`"', '`': '``'})
    title = title.translate(powershell_special_chars)
    command = f'New-BurntToastNotification -Text "{title}"'
    
    if description:
        description = description.translate(powershell_special_chars)
        command = f'New-BurntToastNotification -Text ("{title}", "{description}")'
    
    subprocess.run([
        'powershell.exe',
        command,
    ])    
