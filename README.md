# AGV-Test
The Code takes some data from excell files and plot them



AGV  with suit:

Explanation: AGV nin suit üzerindeki montajı ve doldurma süreleri ölçülecektir.
Sistem kurulduktan sonra 70 psi basınç  altında 200-180-170-160-150 strokları kullanılarak ilk önce 0 dan 5 psig yekadar çıkılacak sonra 5psig den 0 psig ye geri dönülecektir. Bu aralıkta süreler ölçülecek ve hangi stroke da istenilen basınca kaç saniyede geliyor bu bilgiler kayıt altına alınacaktır 

Scope: Belirli bir stroke değeri veriyorum ve garment deki basımç değerini ölçüyorum ve bu basınç değerine kaç sn de çıkıyor buna bakıyorum.
a-)Kaç saniyede istenilen basıncı dolduruyo, kaç saniyede o basıncı boşaltıyor
b-)Kaç saniyede ready pressure’a geliyor ,5psi geldikten sonra kaç saniyede 

Önemli Notlar: Plug-1 de bazı ölçü değişiklikleri oldu Plug-2 takıldı yapılan değişiklikler kayıt altına alındı .Plug-2 den elimizde iki tane var birini AGV ye taktık.
#Plug_1 verilerini kulanmıyoruz, daha iyi bir plug revize edilerek montaja takıldı.


08.08.2024 : At this day, As we fill the garment the exhoust time is really long , it should be much more shorter, we'll make some revision 
for some parts

09.08.2024: Tuday we send a spring haousing part to make the hole length deeper (from3,5mm to 5,5 mm). with this there is no air leakage from AGV, but stroke values is changed (from 400 to 200)

12.08.2024: şimdi ready pressure ile testler yapıldı ama 0,2 psi için 230-250 strokeları arasında bu basınç garment de sabit kalabiliyor.
0.2-5 psi ya istenilen strokelarda kaç saniyede dolduruyor buna bakıyoruz. ama boşaltma kısmında ilk 600'e gidip tamamen boşaltıyoruz sonra 240 stroga gidip 0.2 psi yı garment içinde sabit tutuyoruz. Çünkü full doldurup stroğu 240 a çektiğimde çok ama çok yavaş bir şekilde boşaltıyor. Kodlar Python Projectin içinde.

Bir hata oluştu. 210 stroğu devamlı verdiğimde  yaklaşık 7.63 psig ye kadar gidiyor. Her bir stroğun yaklaşık kaç psig de durguğunun hesaplanması lazım.
Aynı zamanda 210 stroğun 7.63 psi’ya ulaşması oldukça fazla zaman almakta bu sürenin çok kısa olması gerek. 


