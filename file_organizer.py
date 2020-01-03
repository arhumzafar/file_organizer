import watchdog
import os
import json
import time
import shutil

# pip install watchdog so that these packages will work!
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
from time import gmtime, strftime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'az':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]
                    
                    year_exists = False
                    month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "/" +year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_destination_path = extensions_folders[extension] + "/" + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + "/" + month)
                        folder_destination_path = folder_destination_path + "/" + month


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)

extensions_folders = {
#No name
    'noname' : "/Users/az/Desktop/az/Other/Uncategorized",
#Audio
    '.aif' : "/Users/az/Desktop/az/Media/Audio",
    '.cda' : "/Users/az/Desktop/az/Media/Audio",
    '.mid' : "/Users/az/Desktop/az/Media/Audio",
    '.midi' : "/Users/az/Desktop/az/Media/Audio",
    '.mp3' : "/Users/az/Desktop/az/Media/Audio",
    '.mpa' : "/Users/az/Desktop/az/Media/Audio",
    '.ogg' : "/Users/az/Desktop/az/Media/Audio",
    '.wav' : "/Users/az/Desktop/az/Media/Audio",
    '.wma' : "/Users/az/Desktop/az/Media/Audio",
    '.wpl' : "/Users/az/Desktop/az/Media/Audio",
    '.m3u' : "/Users/az/Desktop/az/Media/Audio",
#Text
    '.txt' : "/Users/az/Desktop/az/Text/TextFiles",
    '.doc' : "/Users/az/Desktop/az/Text/Microsoft/Word",
    '.docx' : "/Users/az/Desktop/az/Text/Microsoft/Word",
    '.odt ' : "/Users/az/Desktop/az/Text/TextFiles",
    '.pdf': "/Users/az/Desktop/az/Text/PDF",
    '.rtf': "/Users/az/Desktop/az/Text/TextFiles",
    '.tex': "/Users/az/Desktop/az/Text/TextFiles",
    '.wks ': "/Users/az/Desktop/az/Text/TextFiles",
    '.wps': "/Users/az/Desktop/az/Text/TextFiles",
    '.wpd': "/Users/az/Desktop/az/Text/TextFiles",
#Video
    '.3g2': "/Users/az/Desktop/az/Media/Video",
    '.3gp': "/Users/az/Desktop/az/Media/Video",
    '.avi': "/Users/az/Desktop/az/Media/Video",
    '.flv': "/Users/az/Desktop/az/Media/Video",
    '.h264': "/Users/az/Desktop/az/Media/Video",
    '.m4v': "/Users/az/Desktop/az/Media/Video",
    '.mkv': "/Users/az/Desktop/az/Media/Video",
    '.mov': "/Users/az/Desktop/az/Media/Video",
    '.mp4': "/Users/az/Desktop/az/Media/Video",
    '.mpg': "/Users/az/Desktop/az/Media/Video",
    '.mpeg': "/Users/az/Desktop/az/Media/Video",
    '.rm': "/Users/az/Desktop/az/Media/Video",
    '.swf': "/Users/az/Desktop/az/Media/Video",
    '.vob': "/Users/az/Desktop/az/Media/Video",
    '.wmv': "/Users/az/Desktop/az/Media/Video",
#Images
    '.ai': "/Users/az/Desktop/az/Media/Images",
    '.bmp': "/Users/az/Desktop/az/Media/Images",
    '.gif': "/Users/az/Desktop/az/Media/Images",
    '.ico': "/Users/az/Desktop/az/Media/Images",
    '.jpg': "/Users/az/Desktop/az/Media/Images",
    '.jpeg': "/Users/az/Desktop/az/Media/Images",
    '.png': "/Users/az/Desktop/az/Media/Images",
    '.ps': "/Users/az/Desktop/az/Media/Images",
    '.psd': "/Users/az/Desktop/az/Media/Images",
    '.svg': "/Users/az/Desktop/az/Media/Images",
    '.tif': "/Users/az/Desktop/az/Media/Images",
    '.tiff': "/Users/az/Desktop/az/Media/Images",
    '.CR2': "/Users/az/Desktop/az/Media/Images",
#Internet
    '.asp': "/Users/az/Desktop/az/Other/Internet",
    '.aspx': "/Users/az/Desktop/az/Other/Internet",
    '.cer': "/Users/az/Desktop/az/Other/Internet",
    '.cfm': "/Users/az/Desktop/az/Other/Internet",
    '.cgi': "/Users/az/Desktop/az/Other/Internet",
    '.pl': "/Users/az/Desktop/az/Other/Internet",
    '.css': "/Users/az/Desktop/az/Other/Internet",
    '.htm': "/Users/az/Desktop/az/Other/Internet",
    '.js': "/Users/az/Desktop/az/Other/Internet",
    '.jsp': "/Users/az/Desktop/az/Other/Internet",
    '.part': "/Users/az/Desktop/az/Other/Internet",
    '.php': "/Users/az/Desktop/az/Other/Internet",
    '.rss': "/Users/az/Desktop/az/Other/Internet",
    '.xhtml': "/Users/az/Desktop/az/Other/Internet",
#Compressed
    '.7z': "/Users/az/Desktop/az/Other/Compressed",
    '.arj': "/Users/az/Desktop/az/Other/Compressed",
    '.deb': "/Users/az/Desktop/az/Other/Compressed",
    '.pkg': "/Users/az/Desktop/az/Other/Compressed",
    '.rar': "/Users/az/Desktop/az/Other/Compressed",
    '.rpm': "/Users/az/Desktop/az/Other/Compressed",
    '.tar.gz': "/Users/az/Desktop/az/Other/Compressed",
    '.z': "/Users/az/Desktop/az/Other/Compressed",
    '.zip': "/Users/az/Desktop/az/Other/Compressed",
#Disc
    '.bin': "/Users/az/Desktop/az/Other/Disc",
    '.dmg': "/Users/az/Desktop/az/Other/Disc",
    '.iso': "/Users/az/Desktop/az/Other/Disc",
    '.toast': "/Users/az/Desktop/az/Other/Disc",
    '.vcd': "/Users/az/Desktop/az/Other/Disc",
#Data
    '.csv': "/Users/az/Desktop/az/Programming/Database",
    '.dat': "/Users/az/Desktop/az/Programming/Database",
    '.db': "/Users/az/Desktop/az/Programming/Database",
    '.dbf': "/Users/az/Desktop/az/Programming/Database",
    '.log': "/Users/az/Desktop/az/Programming/Database",
    '.mdb': "/Users/az/Desktop/az/Programming/Database",
    '.sav': "/Users/az/Desktop/az/Programming/Database",
    '.sql': "/Users/az/Desktop/az/Programming/Database",
    '.tar': "/Users/az/Desktop/az/Programming/Database",
    '.xml': "/Users/az/Desktop/az/Programming/Database",
    '.json': "/Users/az/Desktop/az/Programming/Database",
#Executables
    '.apk': "/Users/az/Desktop/az/Other/Executables",
    '.bat': "/Users/az/Desktop/az/Other/Executables",
    '.com': "/Users/az/Desktop/az/Other/Executables",
    '.exe': "/Users/az/Desktop/az/Other/Executables",
    '.gadget': "/Users/az/Desktop/az/Other/Executables",
    '.jar': "/Users/az/Desktop/az/Other/Executables",
    '.wsf': "/Users/az/Desktop/az/Other/Executables",
#Fonts
    '.fnt': "/Users/az/Desktop/az/Other/Fonts",
    '.fon': "/Users/az/Desktop/az/Other/Fonts",
    '.otf': "/Users/az/Desktop/az/Other/Fonts",
    '.ttf': "/Users/az/Desktop/az/Other/Fonts",
#Presentations
    '.key': "/Users/az/Desktop/az/Text/Presentations",
    '.odp': "/Users/az/Desktop/az/Text/Presentations",
    '.pps': "/Users/az/Desktop/az/Text/Presentations",
    '.ppt': "/Users/az/Desktop/az/Text/Presentations",
    '.pptx': "/Users/az/Desktop/az/Text/Presentations",
#Programming
    '.c': "/Users/az/Desktop/az/Programming/C&C++",
    '.class': "/Users/az/Desktop/az/Programming/Java",
    '.dart': "/Users/az/Desktop/az/Programming/Dart",
    '.py': "/Users/az/Desktop/az/Programming/Python",
    '.sh': "/Users/az/Desktop/az/Programming/Shell",
    '.swift': "/Users/az/Desktop/az/Programming/Swift",
    '.html': "/Users/az/Desktop/az/Programming/C&C++",
    '.h': "/Users/az/Desktop/az/Programming/C&C++",
#Spreadsheets
    '.ods' : "/Users/az/Desktop/az/Text/Microsoft/Excel",
    '.xlr' : "/Users/az/Desktop/az/Text/Microsoft/Excel",
    '.xls' : "/Users/az/Desktop/az/Text/Microsoft/Excel",
    '.xlsx' : "/Users/az/Desktop/az/Text/Microsoft/Excel",
#System
    '.bak' : "/Users/az/Desktop/az/Text/Other/System",
    '.cab' : "/Users/az/Desktop/az/Text/Other/System",
    '.cfg' : "/Users/az/Desktop/az/Text/Other/System",
    '.cpl' : "/Users/az/Desktop/az/Text/Other/System",
    '.cur' : "/Users/az/Desktop/az/Text/Other/System",
    '.dll' : "/Users/az/Desktop/az/Text/Other/System",
    '.dmp' : "/Users/az/Desktop/az/Text/Other/System",
    '.drv' : "/Users/az/Desktop/az/Text/Other/System",
    '.icns' : "/Users/az/Desktop/az/Text/Other/System",
    '.ico' : "/Users/az/Desktop/az/Text/Other/System",
    '.ini' : "/Users/az/Desktop/az/Text/Other/System",
    '.lnk' : "/Users/az/Desktop/az/Text/Other/System",
    '.msi' : "/Users/az/Desktop/az/Text/Other/System",
    '.sys' : "/Users/az/Desktop/az/Text/Other/System",
    '.tmp' : "/Users/az/Desktop/az/Text/Other/System",
}

folder_to_track = "/Users/az/Desktop/myFolder"
folder_destination = "/Users/az/Desktop/newFolder"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try: 
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()