import platform
from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="TBB:shared")

    if platform.system() == "Windows":
        for i in range(len(builder.items)):
            builder[i].options["TBB:shared"] = True

    builder.run()
