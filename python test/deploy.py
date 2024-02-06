from sshcheckers import ssh_checkout, upload_files
import yaml
with open ('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

def deploy():
    res = []
    upload_files(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")}', f'{data.get("folder_in")}{data.get("file")}.deb', f'{data.get("folder_user")}{data.get("file")}.deb')
    res.append(ssh_checkout(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")} | sudo -S dpkg -i {data.get("folder_user")}{data.get("file")}.deb'
                            "Настраивается пакет"))
    res.append(ssh_checkout(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")} | sudo -S dpkg -s {data.get("file")}.deb',
                            "Status: install ok installed"))
    return all(res)

if deploy():
    print("Деплой успешен")
else:
    print("Ошибка деплоя")
