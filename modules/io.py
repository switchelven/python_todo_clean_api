# coding: utf-8
# standard imports
import os


class IO(object):
    @staticmethod
    def dir_exists(dir_path):
        return os.path.isdir(dir_path)

    @staticmethod
    def file_exists(file_path):
        return os.path.exists(file_path)

    @staticmethod
    def create_dir(dir_path):
        if not IO.dir_exists(dir_path):
            os.makedirs(dir_path)

    @staticmethod
    def get_sub_dir(dir_path):
        results = []
        if IO.dir_exists(dir_path):
            for f in os.listdir(dir_path):
                if os.path.isdir(dir_path + "/" + f):
                    results.append(f)
        return results

    @staticmethod
    def get_files(dir_path, extension=None):
        results = []
        if IO.dir_exists(dir_path):
            for f in os.listdir(dir_path):
                if os.path.isfile(dir_path + "/" + f) and (not extension or f.endswith("." + extension)):
                    results.append(f)
        return results
