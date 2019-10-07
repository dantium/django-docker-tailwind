"""
Setup envs for dev environment
"""

import secrets
import shutil


def get_random_string():
    return secrets.token_urlsafe(16)


def set_key_random(file_path, key):
    secret = get_random_string()

    with open(file_path, 'r+') as config_file:
        file_contents = config_file.read().replace(key, secret, 1)
        config_file.seek(0)
        config_file.write(file_contents)
        config_file.truncate()


def copy_dev_env():
    env_template = '.env.template'
    env_file = '.env'
    shutil.copyfile(env_template, env_file)
    set_key_random(env_file, '__DJANGO_SECRET_KEY__')
    set_key_random(env_file, '__POSTGRES_PASSWORD___')


def main():
    copy_dev_env()


if __name__ == "__main__":
    main()
