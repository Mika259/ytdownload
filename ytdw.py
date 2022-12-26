from pytube import YouTube
print("========================")
print("Muat Turun Video YouTube")
#Minta link dari user
link = input("Masukkan Link :")
#Manipulasi link
yt = YouTube(link)

#resolusi paling tinggi
rs = yt.streams.get_highest_resolution()
print("Muat Turun Video..")
rs.download()
print("Berjaya Muat Turun Video")
print("========================")
