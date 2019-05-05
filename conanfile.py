
from conans import ConanFile, tools, Meson
import shutil
import os

class LibMPDClient(ConanFile):
    name = "libmpdclient"
    version = "2.16"

    url = "https://github.com/jgsogo/conan-libmpdclient"
    homepage = "https://github.com/MusicPlayerDaemon/libmpdclient"

    settings = "os", "arch", "compiler", "build_type"

    def source(self):
        url = "https://github.com/MusicPlayerDaemon/libmpdclient/archive/v{v}.tar.gz".format(v=self.version)
        tools.get(url)
        shutil.move("libmpdclient-{}".format(self.version), self.name)

    def build(self):
        meson = Meson(self)
        meson.configure(source_folder=os.path.join(self.source_folder, self.name), build_folder=self.build_folder)
        meson.build()

    def package(self):
        self.copy("*.h", dst="include", src=os.path.join(self.name, "include"))
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["mpdclient"]