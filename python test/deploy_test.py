import os
import shutil
import zipfile
from sshcheckers import ssh_checkout, upload_files
import  yaml
import pytest
with open ('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

def test_deploy():
    res = []
    upload_files(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")}', f'{data.get("folder_in")}{data.get("file")}.deb', f'{data.get("folder_user")}{data.get("file")}.deb')
    res.append(ssh_checkout(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")} | sudo -S dpkg -i {data.get("folder_user")}{data.get("file")}.deb'
                            "Настраивается пакет"))
    res.append(ssh_checkout(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")} | sudo -S dpkg -s {data.get("file")}.deb',
                            "Status: install ok installed"))
    assert all(res)

def test_archive():
    temp_dir = os.path.join(os.getcwd(), 'temp_dir')
    os.makedirs(temp_dir)
    file_м = os.path.join(temp_dir, 'file_м.txt')
    with open(file_м, 'w') as f:
        f.write('Test file_m')
    file_n = os.path.join(temp_dir, 'file_n.txt')
    with open(file_n, 'w') as f:
        f.write('Test file_n')
    archive_name = os.path.join(temp_dir, 'test_archive.zip')
    with zipfile.ZipFile(archive_name, 'w') as zip_file:
        zip_file.write(file_м, arcname=os.path.basename(file_м))
        zip_file.write(file_n, arcname=os.path.basename(file_n))
    assert os.path.exists(archive_name)
    extract_dir = os.path.join(temp_dir, 'extracted_files')
    with zipfile.ZipFile(archive_name, 'r') as zip_file:
        zip_file.extractall(extract_dir)
    assert os.path.exists(os.path.join(extract_dir, 'file_m.txt'))
    assert os.path.exists(os.path.join(extract_dir, 'file_n.txt'))

    with open(os.path.join(extract_dir, 'file_m.txt'), 'r') as f:
        assert f.read() == 'Test file_m'
    with open(os.path.join(extract_dir, 'file_n.txt'), 'r') as f:
        assert f.read() == 'Test file_n'
    shutil.rmtree(temp_dir)

def test_delete():
 assert ssh_checkout(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")} | sudo -S dpkg -s {data.get("file")}.deb',
                            "Удаляется")

if __name__ == '__main__':
    pytest.main(['-vv'])