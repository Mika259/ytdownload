try:
    from pytube import YouTube
except:
    print("try install 'pytube' command : pip install pytube ")
    exit()
print("========================")
print("Muat Turun Video YouTube")
#Minta link dari user
link = input("Masukkan Link :")
#Manipulasi link
try:
   yt = YouTube(link)
   user = input("Muat turun resolusi paling tinggi?(y/N)")
except:
   exit(f"Link yang dimasukkan bermasalah, sila cuba lagi.")
#resolusi paling tinggi
def dw():
    print("sedang memuat turun video !...")
    rs = yt.streams.get_highest_resolution()
    rs.download()
    print("Berjaya Muat Turun Video ✅")
print("========================")
if user == "y":
    dw()
else:
    exit()
