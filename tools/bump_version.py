import os
import tomlkit
import datetime

PYPROJECT_TOML_PATH = os.environ.get('PYPROJECT_TOML_PATH')
GITHUB_OUTPUT = os.environ.get('GITHUB_OUTPUT')

with open(PYPROJECT_TOML_PATH, 'r+') as f:
    doc = tomlkit.parse(f.read())
    current_version = doc['project']['version']
    # Append a developmental suffix to the version.
    # The format 'YYYY.MM.DD' doesn't work well with PEP 440's .devN, so we use a timestamp.
    # A format like 'YYYY.MM.DD.devTIMESTAMP' is more robust.
    dev_version = f'{current_version}.dev{datetime.datetime.now(datetime.UTC).strftime("%Y%m%d%H%M%S")}'
    doc['project']['version'] = dev_version
    f.seek(0)
    f.write(tomlkit.dumps(doc))
    f.truncate()
print(f'Bumping version from {current_version} to {dev_version} for TestPyPI release.')
print(f'BUMPED_VERSION={dev_version}', file=open(GITHUB_OUTPUT, 'a'))
