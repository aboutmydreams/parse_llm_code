import re


def increment_version_string(version_string):
    parts = version_string.split(".")
    if len(parts) < 3:
        raise ValueError("Version string must have at least three parts")

    last_part = int(parts[-1])
    new_last_part = last_part + 1
    parts[-1] = str(new_last_part)

    return ".".join(parts)


def update_setup_py_version(setup_py_path):
    with open(setup_py_path, "r") as f:
        setup_py_content = f.read()
        f.close()

    version_pattern = r"version\s*=\s*['\"]([^'\"]+)['\"]"
    match = re.search(version_pattern, setup_py_content)

    if match:
        old_version = match.group(1)
        new_version = increment_version_string(old_version)
        filedata = setup_py_content.replace(old_version, new_version)
        with open(setup_py_path, "w") as f:
            f.write(filedata)
            f.close()
        print(f"Version updated to {new_version}")
        return new_version
    raise ValueError("Could not find version number in setup.py")


update_setup_py_version("./setup.py")
