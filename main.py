"""
/***************************************************************************
                           gundem-download - main.py
                             --------------------
        begin                : 2019-11-17
        copyright            : (C) 2019 by tsopenteam (Turkey)
        email                : tsopenteam@gmail.com
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   Bu program teknoseyir haftalık gündem değerlendirme podcastlerini     *
 *   indirmek için yapılmıştır.                                            *
 *   Tüm podcastleri tek seferde indirebilirsiniz.                         *
 *   İsterseniz sadece numarasını girdiğiniz podcasti indirebilirsiniz.    *
 *                                                                         *
 ***************************************************************************/
"""

try:

    ########################
    ###
    # Import Lib.
    import os
    import requests
    import json
    import urllib.request

    ###
    ########################


    ########################
    ###
    # Define Veriable
    directory = "podcasts"
    download_url = "https://raw.githubusercontent.com/tsopenteam/gundem/master/gundem.json"
    podcast_list = []

    ###
    ########################


    ########################
    ###
    # Define Methods
    
    def check_directory():
        if not os.path.exists(directory):
            os.makedirs(directory)
    

    def download_podcast_data_list():
        r = requests.get(download_url)
        r = json.loads(r.text)

        global podcast_list
        podcast_list = r["list"]

        print(f"Toplam Podcast : {len(podcast_list)}")
    

    def download_all_podcast():
        check_directory()
        download_podcast_data_list()

        print("Tüm podcast indirmesi başladı.")
        for item in podcast_list:
            podcast_name = f'gundem-{str(item["totalCount"])}-{item["year"]}-{str(item["count"])}.mp3'
            full_directory = f'{directory}/{podcast_name}'
            
            if not os.path.exists(full_directory):
                print(f'Podcast indiriliyor : {podcast_name}')
                
                opener = urllib.request.URLopener()
                opener.addheader('User-Agent', 'whatever')
                opener.retrieve(item["podcastLink"], full_directory)
            else:
                print(f'Podcast zaten var : {podcast_name}')
        
        print("Tüm podcast indirmesi bitti.")
    

    def download_single_podcast(podcast_number):
        check_directory()
        download_podcast_data_list()

        print("Podcast indirmesi başladı.")
        item = podcast_list[podcast_number-1]

        podcast_name = f'gundem-{str(item["totalCount"])}-{item["year"]}-{str(item["count"])}.mp3'
        full_directory = f'{directory}/{podcast_name}'
        
        if not os.path.exists(full_directory):
            print(f'Podcast indiriliyor : {podcast_name}')
            
            opener = urllib.request.URLopener()
            opener.addheader('User-Agent', 'whatever')
            opener.retrieve(item["podcastLink"], full_directory)
        else:
            print(f'Podcast zaten var : {podcast_name}')
        
        print("Podcast indirmesi bitti.")
            

    ###
    ########################


    ########################
    ###
    # Start and view
    title = """
     _       _                               _      
    | |_ ___| | ___ __   ___  ___  ___ _   _(_)_ __ 
    | __/ _ \ |/ / '_ \ / _ \/ __|/ _ \ | | | | '__|
    | ||  __/   <| | | | (_) \__ \  __/ |_| | | |   
     \__\___|_|\_\_| |_|\___/|___/\___|\__, |_|_|   
                                       |___/            

    """
    print(title)

    while True:
        
        command = input("\nTüm podcastleri indirmek için (e) yazın. \nSadece bir podcast indirmek için id yazın. \nÇıkmak için (x) \n--> ")

        if command.lower() == "e":
            download_all_podcast()
        elif command.isdigit():
            download_single_podcast(int(command))
        elif command.lower() == "x":
            break
        else:
            print("Geçersiz karakter !")

     ###   
     ########################   

except:
    # Hi Windows :)
    print("Bir şey oldu !")