import zipfile


def extract_archive(archivepath, dest_folder):
    """
    simple function for extracting zip files
    :param archivepath: get the file from a given directory
    :param dest_folder: extract the files in the destination folder
    :return:
    """

    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_folder)                 # extracting the files in destination folder


# cross-checking if the function is working fine
if __name__ == '__main__':
    extract_archive('C:\\Users\\SAM\\Desktop\\Python_Programs\\files_extractor_app\\files\\compressed\\compressed.zip',
                    'C:\\Users\\SAM\\Desktop\\Python_Programs\\files_extractor_app\\files\\zipped')
