import configparser
import os
import zipfile
import datetime


def main():
    now = datetime.datetime.now()
    config = ini_parser()
    zipname = "{}{}{}".format(os.path.basename(config.get('main', 'source')), now.strftime("%d%m%Y-%H%M%S"), ".zip")
    if config.get('main', 'type') == "NF":
        zipname = "{}_NF_{}{}".format(os.path.basename(config.get('main', 'source')), now.strftime("%d%m%Y-%H%M%S"), ".zip")
    zipf = zipfile.ZipFile("{}{}".format(config.get('main', 'dest'), zipname), 'w', zipfile.ZIP_DEFLATED)
    zipdir(config.get('main', 'source'), zipf)
    zipf.close()


def ini_parser():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


if __name__ == "__main__":
    main()
