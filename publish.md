# Publish

- `python3 setup.py sdist bdist_wheel` (if you not have setuptools and wheel, run `pip3 install setuptools wheel`)

- `twine upload dist/*`  (if you not have twine, run `pip3 install twine`)

- input the your API token in cmd, if you not have a api token

## Run the script manually

`python3 update_version.py; git add -A; git commit -m"update version name"; git push; python3 setup.py sdist bdist_wheel; twine upload dist/*`

## Use github action

This action supports PyPI's [trusted publishing]
implementation, which allows authentication to PyPI without a manually
configured API token or username/password combination. To perform
[trusted publishing] with this action, your project's
publisher must already be [configured on PyPI].

[trusted publishing]: https://docs.pypi.org/trusted-publishers/
[configured on PyPI]: https://docs.pypi.org/trusted-publishers/adding-a-publisher/
