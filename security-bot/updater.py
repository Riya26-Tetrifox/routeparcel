from packaging.requirements import Requirement
import os

def update_package(package, fixed_version):
    if not fixed_version:
        return

    temp_file = "requirements_tmp.txt"

    with open("requirements.txt", "r") as f, open(temp_file, "w") as temp:
        for line in f:
            stripped = line.strip()

            try:
                req = Requirement(stripped)
                pkg_name = req.name
            except:
                temp.write(line)
                continue

            if pkg_name == package:
                temp.write(f"{package}=={fixed_version}\n")
                print(f"Updated {package} to {fixed_version}")
            else:
                temp.write(line)

    os.replace(temp_file, "requirements.txt")


