from conans import ConanFile, CMake
import os


class YoutubeListDownloaderConan(ConanFile):
    name = "youtube_list_downloader"
    version = "1.0.1"
    license = "MIT"
    author = "Linus Kloeckner (linus.kloeckner@googlemail.com)"
    url = "https://github.com/Linux13524/YoutubeListDownloader"
    description = "Multiplatform library for downloading Youtube content"
    topics = ("youtube", "download", "video", "playlist", "channel")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    requires = "boost/1.66.0@conan/stable", "cpr/1.3.0@linux13524/stable", \
               "youtube_decipher/1.0.1@linux13524/testing", "sqlitecpp/2.2.0@bincrafters/stable"
    generators = "cmake"
    exports_sources = "package/*"

    def build(self):
        cmake = CMake(self)
        os.mkdir("build")
        cmake.configure(source_folder="package")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder="package")
        cmake.install()


    def package_info(self):
        LIB_POSTFIX = "-d" if self.settings.build_type == "Debug" else ""
        self.cpp_info.libs = ["YoutubeListDownloader" + LIB_POSTFIX]
