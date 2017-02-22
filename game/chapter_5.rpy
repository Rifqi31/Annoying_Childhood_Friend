

label chapter_5:


    scene bg langit with dissolve

    show cinema with dissolve

    play music sesuatu fadeout 1.0 fadein 1.0

    n "Delapan hari sebelum operasi pendonoran, kami menjalani Ujian Nasional."

    n "Aku dan Arthur memilih universitas yang sama."

    n "Universitas ternama yaitu Havard."

    n "Entah kebetulan atau takdir."

    n "Kami sepakat untuk menentukan pilihan universitas kami disana."


    n "Sedangkan Karin dan Arthur akan tetap tinggal dikota ini."

    n "Kota Jakarta."

    n "Mereka berdua tidak mengatakan pada kami tentang pilihan universitasnya."

    hide cinema with dissolve

    hide langit with dissolve

    #lorong rumah sakit
    ## kasih efek pergantian layar yang menarik
    scene bg lorong_rm with pixellate
    
    play music sad_music fadeout 1.0 fadein 1.0


    n "Hingga hari penentuan pun akhirnya datang."

    n "Operasi pendonoran sumsum tulang untuk Arthur pun dilakukan."

    n "Mereka berdua,{w} Ivan dan Arthur memasuki ruang operasi."

    n "Terlihat seluruh keluarga besar Arthur berkumpul di lorong."

    n "Mereka terlihat mendoakan anggota keluarganya."


    with fade


    n "Berbanding terbalik dengan keluarga Arthur yang dikunjungi keluarganya."

    n "Tidak terlihat satu pun anggota keluarga dari Ivan yang datang."

    n "Kemana mereka?"

    n "Kemana orang tua Ivan?"

    n "Apa mereka terlalu sibuk karena urusan pekerjaan, hingga tidak sempat melihat aksi heroik anaknya?"


    with fade


    n "Akhirnya selesai."

    n "Operasi pendonoran pun selesai."

    n "Terlihat isak tangis bahagia dari keluarga Arthur yang memeluknya."

    n "Aku juga langsung spontan memeluknya."

    n "Aku langsung memeluk Arthur setelah diperbolehkan oleh dokter."

    n "Aku benar-benar bahagia saat ini."

    n "Aku sungguh bersyukur karena akhirnya Arthur sembuh total dari penyakitnya."


    n "Semua orang menangis bahagia."

    n "Tertawa bahagia mendengar kabar ini."

    n "Keluarga Arthur,{w} teman-teman Arthur,{w} dan seluruh siswa di sekolah kami."

    n "Benar-benar bahagia mendengar kabar tentang kesembuhan Arthur."


    n "Tapi hanya satu orang yang tidak tersenyum."

    n "Tidak terharu dengan kabar gembira ini."

    n "Dia datang terlambat dan hanya terus menundukan kepalanya."

    n "Dia bahkan belum masuk ke ruangan Arthur dirawat."


    show karin_marah far with dissolve


    n "Karin."

    n "Dia terlihat tidak bahagia atas kesembuhan Arthur."

    n "Aku mencoba menyapanya."

    n "Memberi tahu kambar gembira ini."

    n "Mungkin dia masih belum tau tentang kabar gembira ini."


    hide karin_marah far with fade

    show karin_marah at my_near with dissolve


    l "“Ka-Karin.”"

    l "“Kata dokter operasinya sukses!!”"

    l "“Sekarang Arthur –”"



    k "“Sudah tau.....{w} aku sudah tau itu.”"

    n "Jelas Karin pelan sambil berdiri dari tempat duduknya."

    hide karin_marah at my_near with dissolve

    n "Lalu dia berjalan melewatiku."

    n "Pandangannya benar-benar tidak mau melihatku."

    n "Dia seolah-olah tidak ingin melihatku saat ini."

    n "Aku sempat berpikir, ada apa dengannya?"

    n "Apa dia sebegitu membenciku?"

    n "Karin berjalan memasuki tempat dimana Arthur sedang berbaring."

    n "Dia memasuki ruangan secara paksa, meski perawat sudah mencegahnya."


    s "“Nyonya, kamu harus menunggu giliranmu!”"

    s "“Pasien tidak bisa dikunjungi oleh banyak orang –”"


    show karin_marah at my_near with dissolve


    k "“Aku hanya sebentar!!”"

    k "“Aku hanya mau mengucapkan kata selamat saja padanya.”"

    n "Lirik sinis Karin pada suster."

    s "“Ba-Baiklah!”"


    hide karin_marah at my_near with dissolve

    n "Perawat tersebut terlihat ketakutan."

    n "Setelah Karin mengucapkan selamat pada Arthur, dia bergegas keluar dari ruangan tersebut."

    n "Dia kembali berpapasan denganku."


    show karin_marah at my_near with dissolve


    k "“Apa balasanmu?”"

    l "“Eh?”"
    
    k "“Kamu bahkan tidak mengucapakan terima kasih padanya.”"

    n "Aku tersadar."

    n "Orang yang menyelamatkan Arthur adalah Ivan!"

    n "Aku harus mengucapkan terima kasih padanya."


    hide karin_marah at my_near with dissolve


    with fade


    play sound walking_fast


    n "Aku bergegas berlari menanyakan lokasi Ivan pada suster yang mengurus Arthur."

    n "Setelah mendapatkan informasi, aku lekas berlari menuju ruangan tempat Ivan di rawat."


    scene bg lorong_rm with fade

    n "Sesampainya disana, aku hanya terdiam terkejut."

    n "Benar-benar terkejut melihat suasana dingin disekitar ruangan tempat Ivan beristirahat."

    n "Jika lorong ruangan Arthur penuh dengan kehangatan orang-orang."

    n "Penuh dengan orang-orang yang mengucapkan selamat atas kesembuhannya."


    n "Sedangkan lorong ruangan Ivan terlihat sepi."

    n "Tidak ada satupun yang memberi penghargaan padanya."

    n "Tidak ada satu orang pun yang peduli dengan aksi heroiknya."

    n "Teman-temannya,{w} keluarganya,{w} bahkan aku sendiri melupakannya."

    n "Jika tidak di ingatkan oleh Karin."

    n "Aku mungkin akan larut dalam kebahagian dan melupakan Ivan."

    n "Apa keterlambatan Karin saat itu karena ini?"

    n "Karena dia mengucapkan terima kasih pada Ivan?"

    n "Karin bukan kekasih Arthur."

    n "Tapi dia bersikap layaknya seperti kekasihnya."

    n "Sedangkan aku kekasih Arthur."

    n "Malah belum mengucapkan terima kasih pada orang yang telah menyelamatkan Arthur."

    n "Benar-benar menyedihkannya diriku."

    #play pintu
    play sound opendoor_morning
    
    scene bg rumah_sakit with fade

    $ renpy.pause(1.0, hard=True)

    #show cg ivan tidur
    show iv_merem with dissolve:

        #show from bottom
        xalign 0.6 yalign 0.5

        #move to top with 1.0 seconds
        linear 2.5 yalign 0.0
    


    n "Aku perlahan membuka pintu ruangan tersebut dan kulihat dirinya terbaring tidak sadarkan diri."

    n "Dia tidak bergerak sedikitpun."

    hide iv_merem with dissolve

    n "Lalu kulihat suster yang memasang wajah sedih sambil membereskan peralatannya."


    l "“Suster.”"

    l "“Apa dia baik-baik saja?”"

    s "“Ohhh kamu mengenal anak ini?”"

    s "“Untunglahh...”"

    n "Senyum sedih suster tersebut."

    l "“Iya aku mengenalnya, memangnya kenapa?”"

    s "“Tidak apapa, bukankah dia pendonor yang menyelamatkan anak itu?”"

    l "“Iya dia orangnya.”"

    s "“Begitu....{w} sungguh menyedihkan yah?”"

    n "Suster tersebut kembali tersenyum sedih sambil melihat Ivan yang tidak bergerak sedikitpun."

    l "“Menyedihkan?”"

    l "“Kenapa bisa menyedihkan?”"

    s "“Semua orang mengucapkan selamat.”"

    s "“Mengunjunginya.”"

    s "“Berbondong-bondong datang ke ruangan yang mendapatkan donor darinya.”"

    s "“Tapi dia yang menyelamatkan anak itu, hanya mendapatkan dua tamu yang mengunjunginya.”"

    s "“Sungguh kasian...”"

    n "Suster tersebut sambil tersenyum sedih melihat Ivan."

    l "“Ma{w}-maaf.”"

    l "“Ak-aku terlalu larut dalam kebahagian hingga melupakannya.”"

    n "Aku menjawab sedih penjelasan suster tersebut."
    
    s "“Tak apa, paling tidak kamu datang, kan?”"
    
    n "Senyum Suster tersebut."

    l "“Iya.... apa boleh aku tetap disini.”"

    show iv_merem at naik with dissolve

    l "“Aku ingin menunggunya bangun dan mengucapkan terima kasih.”"

    hide iv_merem with dissolve

    n "Senyumku melihat suster tersebut."

    s "“Iya, itu lebih baik daripada dia sendirian disini.”"

    n "Jelas suster tersebut lalu berjalan keluar ruangan."


    #sinis
    #show ivan_marah sakit at my_near2 with dissolve#sakit

    ##jeda yang ngga bisa diklik
    #$ renpy.pause(3.0, hard=True)

    show iv_merem at naik with dissolve

    #jeda bebeapa detik
    $ renpy.pause(2.0, hard=True)

    show iv_bangun at naik with dissolve

    hide iv_merem

    #jeda lagi dikit
    $ renpy.pause(1.5, hard=True)

    show iv_normal at naik with dissolve

    hide iv_bangun 

    i "“Kamu disini?”"

    i "“Kenapa?”"

    i "“Seharusnya kamu bersamanya, kan?”"

    i "“Seharusnya kamu merayakan kesembuhan kekasihmu itu, kan?”"


    l "“Aku ingin berterima kasih padamu.”"

    l "“Terima kasih karena telah menyelamatkan hidup kekasihku.”"

    n "Aku menangis bahagia sambil menundukkan kepalaku."


    #hide ivan_marah sakit at my_near2

    #show ivan_kesel sakit at my_near2

    show iv_kesal at naik

    i "“Memang harus seperti itu!!”"

    i "“Benar-benar mengesalkan.”"


    i "“Kenapa aku tidak mendapatkan kunjungan disini?”"

    i "“Padahal aku yang sudah menyelamatkannya.”"

    #n "senyum kesal Ivan memejamkan matanya."


    l "“Kalau begitu, biar aku yang kasih tau mereka –”"

    #hide ivan_kesel sakit at my_near

    #show ivan_sebel sakit at my_near
    hide iv_kesal at naik

    show iv_normal

    i "“Tak apa.”"

    i "“Aku tidak ingin mereka menjengukku karena terpaksa.”"

    i "“Aku tidak ingin mereka mengunjungiku karena di ingatkan oleh orang lain.”"


    l "“Ma-maaf.”"

    l "“S-sebenarnya aku juga.”"

    l "“Aku di ingatkan oleh Karin.”"

    #hide ivan_sebel sakit at my_near

    #show ivan_marah sakit at my_near

    hide iv_normal
    show iv_marah at naik

    i "“Haah?!”"

    i "“Jadi kamu di ingatkan oleh Karin?!”"

    i "“Sialan –“"


    #hide ivan_marah sakit at my_near with dissolve

    scene black with dissolve

    n "Aku hanya menutup mata."

    n "Aku ketakutan karena akan mendapatkan amarah darinya lagi."

    n "Tapi tiba-tiba Ivan langsung menghentikan perkataanya."


    #scene bg rumah_sakit with fade

    #show ivan_senyum sakit at my_near with dissolve

    show iv_senang at naik with dissolve

    n "Ivan tersenyum melihatku."

    n "Senyuman tulus yang belum pernah aku lihat sebelumnya."

    i "“Lupakan......”"

    i "“Wajar jika kamu lupa.......”"

    i "“Kamu sudah punya seseorang yang berharga bagimu.”"

    i "“Aku bisa mengerti perasaan itu.”"

    l "“Ka-kamu tersenyum?”"

    l "“Lagipula apa kamu sudah menyukai seseorang?”"


    i "“Iya, tapi sayang cuman bertepuk sebelah tangan..... ahahaha.”"

    n "Ivan tertawa pelan sambil memejamkan matanya."

    l "“Siapa?!{w} Biar aku bantu –”"

    i "“Tidak perlu.”"

    i "“Aku tidak punya harapan untuk mendapatkannya.”"

    i "“Dia sudah bahagia dengan orang lain.”"

    n "Senyum Ivan sambil terus memejamkan matanya"

    l "“Tapi –”"

    #hide ivan_senyum sakit at my_near

    #show ivan_kesel sakit at my_near

    hide iv_senang
    show iv_marah at naik

    i "“Berisiknya!!”"

    i "“Jika aku bilang tidak perlu, ya tidak perlu!”"

    n "Geram kesal Ivan melihatku."

    l "“Bi-biasa ajah....{w} Aku kan cuman mau membantumu.”"



    n "Memang seperti Ivan yang biasanya."

    n "Dia cepat marah untuk alasan yang sepele seperti ini."

    n "Kenapa dia cepat marah?"

    n "Pantas saja orang yang menjenguknya hanya aku dan Karin."


    #hide ivan_kesel sakit at my_near

    #ivan memalingkan wajah

    #show ivan_sebel sakit at my_near

    show iv_normal at naik

    i "“Pergilah....”"

    i "“Temui lelaki itu.”"


    #n "Ivan memalingkan wajahnya."


    l "“Tapi –”"

    #hide ivan_sebel sakit at my_near

    #show ivan_marah sakit at my_near

    hide iv_normal

    show iv_marah at naik

    i "“Pergilah!”"

    l "“Ba-baiklah, aku pergi”"

    hide iv_marah with dissolve

    scene bg rumah_sakit with fade
    #hide ivan_marah sakit at my_near with dissolve

    n "Aku lekas berdiri."

    play sound walking_fast

    n "Dan berjalan cepat menuju pintu keluar karena tidak ingin mendapatkan amarah darinya."

    i "“Aahhhh..... tunggu Lisa!{w} Aku melupakan sesuatu yang penting.”"

    l "“Ap-apa?”"

    
    #show ivan_senyum sakit at my_near with dissolve

    show iv_normal at naik with dissolve

    n"Aku menghentikan langkahku, dan berbalik melihatnya."

    show iv_picik at naik

    hide iv_normal

    i "“Bukankah kamu bilang akan melakukan apapun jika aku mendonorkan sumsumku?”"

    #n "senyum licik Ivan melihatku."

    l "“Ak-aku memang mengatakan itu, tapi pelecehan seksual dilarang!”"

    n "Aku sambil menutupi tubuhku yang ketakutan."

    #hide ivan_senyum sakit at my_near

    #show ivan_kesel sakit at my_near

    show iv_marah at naik
    
    hide iv_picik

    i "“Oi oi, memangnya aku ini lelaki seperti apa dipikiranmu itu?”"

    n "Tanya Ivan mengeluh."

    l "“Lelaki mesum.”"

    l "“Penggangu.”"

    l "“Perusak hubungan orang lain!”"

    l "“Lelaki yang hanya mencari kesenangan duniawi!”"

    hide iv_marah

    show iv_kesal at naik

    i "“Jahatnya.....”"
    

    show iv_normal at naik

    hide iv_kesal

    i "“Tapi tenang saja, aku tidak melakukan hal itu kok.”"

    l "“Lalu maumu apa?”"

    l "“Cepat katakan, supaya hutang kita impas!”"

    i "“Baiklah.”"

    play music leaving_you fadeout 1.0 fadein 1.0

    show iv_serius at naik

    hide iv_normal

    i "“Dengarkan aku baik-baik.”"

    l "“Em.”"

    #hide ivan_tablo sakit at my_near

    #show ivan_sebel sakit at my_near

    
    i "“Aku ingin....”"

    #hide ivan_sebel sakit at my_near

    #show ivan_marah sakit at my_near

    show iv_normal at naik

    hide iv_serius

    i "“Setelah kami,{w} maksudku aku dan Arthur keluar rumah sakit....”"

    show iv_kesal at naik

    i "“Kamu harus melakukan sesuatu untukku!”"

    l "“Iya... apa itu?”"

    show iv_marah at naik

    i "“Menghilanglah dari kehidupanku!”"

    i "“Jangan ganggu kehidupanku lagi.”"

    i "“Dan jangan pernah temui aku lagi.”"

    i "“Hapus semua tentangku dalam ingatanmu.”"

    i "“Maka aku juga akan menghapus semua tentangmu dan ingatanku.”"

    hide iv_kesal

    l "“Eh?”"


    n "Aku hanya terdiam terkejut mendengar permintaan Ivan."

    n "Apa dia serius dengan apa yang dia katakan?"

    n "Apa dia serius ingin memutuskan ikatan pertemanan, mungkin persahabatan kami?"



    l "“Ka{w}-kamu pasti bercan –”"

    #hide ivan_marah sakit at my_near

    #show ivan_kesel sakit at my_near

    show iv_serius at naik
    hide iv_marah
    i "“Aku serius, keputusanku sudah bulat.{w} Aku –”"

    l "“Kenapa?!”"

    l "“Apa kamu membenciku?!”"

    #hide ivan_kesel sakit at my_near

    #show ivan_marah sakit at my_near

    show iv_marah at naik

    hide iv_serius

    i "“Coba kamu pilih.....{w} aku atau Arthur?”"

    l "“Kenapa kamu menanyakan hal it –”"

    show iv_kesal at naik

    i "“Kamu tidak bisa memilih, kan?”"
    show iv_marah at naik
    i "“Kamu terlalu baik Lisa!”"

    i "“Kamu bahkan masih ragu jka diberikan pilihan antara kekasihmu yang baik....”"

    i "“Dan teman masa kecilmu yang sering menggangumu.”"

    i "“Asal kamu tau saja.”"

    i "“Jika aku masih berhubungan denganmu, aku hanya akan menghancurkanmu.”"

    i "“Merusak hubungan kalian berdua.”"

    i "“Kamu pasti orang yang paling mengerti disini, Lisa.”"
    hide iv_kesal
    hide iv_marah

    l "“Tapi kan –”"

    hide iv_marah
    show iv_normal at naik
   
    i "“Itu permintaanku.”"

    hide iv_normal
    show iv_serius at naik

    i "“Setelah aku dan Arthur keluar dari rumah sakit.”"

    i "“Kita hanya orang asing.”"

    i "“Kita tidak mengenal satu sama lain, kamu mengerti?”"

    l "“Ba-baiklah, jika itu maumu.”"

    n "Jawabku menundukan kepala."

    show iv_normal at naik
    hide iv_serius

    i "“Satu hal lagi.”"

    l "“Ap-apa?”"

    i "“Sampai kapanpun, jangan pernah mencariku,{w} bahkan menemuiku!”"

    show iv_marah at naik

    hide iv_normal
    i "“Kamu harus menepati janji ini!”"

    l "“Baik aku mengerti!”"

    l "“Jika kamu ingin mengakhiri hubungan persahabatan kita....”"

    l "“Aku akan melakukannya!”"

    n "Geramku sangat kesal."

    n "Aku benar-benar kesal karena mendengar permintaan bodohnya itu."

    show iv_senang at naik
    hide iv_marah

    i "“Baguslah...”"

    n "Senyum tulus kembali dari Ivan."

    show iv_merem at naik with dissolve

    hide iv_senang

    n "Lalu tertidur memejamkan matanya."


    n "Aku tidak peduli lagi dengannya."

    n "Jika dia tidak ingin bertemu denganku lagi...."

    n "Aku tidak apa!"

    n "Lagipula dia hanya penggangu dalam hidupku."


    pause 1.0


    show langit2 with fade

    show cinema with dissolve

    play music sesuatu fadeout 1.0 fadein 1.0


    n "Beberapa minggu setelah mereka keluar dari rumah sakit."

    n "Aku dan Arthur akan segera pergi meninggalkan Indonesia, dan akan menuntut ilmu di negara asing."

    n "Dia saat-saat terakhir kepergian kami."

    n "Dia tidak datang."

    n "Ivan tidak datang melepas kepergian kami."

    n "Bahkan Karin juga tidak terlihat dalam rombongan yang mengantar kepergian kami."


    n "Sejak mereka..... {w} Arthur dan Ivan, keluar dari rumah sakit."

    n "Aku dan Ivan benar-benar sudah tidak saling bicara."

    n "Kami seolah-olah tidak mengenal satu sama lain."

    n "Sampai saat ini aku benar-benar tidak mengerti jalan pikirannya."

    n "Aku kira dia hanya bergurau soal keinginannya waktu itu,"

    n "Keinginan untuk memutuskan persahabatan kami."

    n "Tapi ternyata dia serius."

    n "Dia benar-benar serius melakukan hal tersebut."


    ## di jump yang ini baru masukan jeda
    jump chapter_6