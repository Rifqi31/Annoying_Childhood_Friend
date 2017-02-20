 
label chapter_1:

    #Lisa

    play music koridor_sekolah fadeout 1.0 fadein 1.0

    scene bg koridor with squares

    n "Sekolah berlangsung seperti biasanya."

    n "Kami,{w} maksudku...."

    n "Aku, Ivan, Arthur, dan Karin menjadi pusat perhatian seperti biasanya."

    n "Kami memiliki wajah yang menarik perhatian karena kami keturunan orang asing."

    n "Terlihat tatapan kagum dari mereka saat kami berjalan masuk ke sekolah."

    n "Dan terjadi lagi."

    n "Seorang gadis menghentikan kami berdua."

    n "Menghentikan aku dan Arthur."

#Show Arthur kaget1

    show arthur_normal at my_near with dissolve

    n "Dia menatap kagum pada Arthur dan berkata."


    #Another girl
    c "“Kak Arthur......”"

    pause 0.5

    hide arthur_normal at my_near

    show arthur_kaget at my_near
    
    c "“Aku menyukaimu!! Kumohon terima aku!”"

    n "Teriak gadis tersebut memasang wajah memerah yang lucu."

    hide arthur_kaget at my_near

    show arthur_senyum at my_near
    
    with dissolve

    n "Arthur hanya tersenyum."

    n "Lalu secara perlahan dia memegang kepala gadis tersebut dan mengusap lembut kepalanya."

    hide arthur_senyum at my_near

    #Arthur

    show arthur_segan2 at my_near

    a "“Maaf, aku tidak bisa.”"

    a "“Kamu kelas satu, kan?”"

    a "“Lebih baik kamu gunakan waktumu untuk belajar, biar nanti tidak kesulitan.”"

    c "“Y-ya...”"

    n "Wajah gadis itu memerah terlihat sangat terkejut."

    n "Bukan terkejut karena ditolak."

    n "Tetapi terkejut kagum karena mendengar perkataan Arthur yang mengkhawatirkan dirinya."

    hide arthur_segan2 at my_near with dissolve

    #bell masuk sekolah

    play sound "<from 1 to 7.5>sfx/classbell.wav"

    with dissolve

    n "Setelah kejadian yang menarik perhatian tersebut, aku dan Arthur pergi ke kelas masing-masing."

    n "Aku sekelas dengan teman masa kecilku yang mengesalkan."

    n "Sedangkan Arthur sekelas dengan Karin, rival terberatku."


    play sound walking_fast

    with dissolve

    n "Aku berjalan cukup cepat melewati lorong sekolah."

    n "Mustahil bagiku untuk berlari karena kondisi tubuhku ini."

    #show ivan_bersiul with dissolve

    n "Aku hanya terus berjalan cukup cepat dan melirik sinis teman masa kecilku dibelakang."

    show ivan_bersiul normal with dissolve

    n "Dia berjalan pelan sambil bersiul cukup merdu."

    #Lisa
    l "“Kenapa kamu tidak lari saja? Apa kamu sedang mengasihaniku?”"

    hide ivan_bersiul normal

    show ivan_tablo normal

    i "“Haah?!”"

    hide ivan_tablo normal

    show ivan_kesel normal

    i "“Un-untuk apa aku melakukan hal itu?!”"

    i "“Aku hanya malas dengan pelajaran matematika.”"

    hide ivan_kesel normal

    show ivan_sebel normal

    i "“Bukan berarti aku berjalan pelan karenamu!”"

    l "“Jawabnya biasa ajah.”"

    l "“Aku bertanya dengan baik-baik kok! Kenapa kamu harus berteriak seperti itu!!”"

    hide ivan_sebel normal

    show ivan_ngeledek normal


    n "Ivan hanya tersenyum sombong sambil menunjuk jam tangan miliknya."

    n "Dia seolah-olah mengatakan kalau 'kamu akan terlambat!'"


    hide ivan_ngeledek normal with dissolve


    n "Melihat hal tersebut, aku mengurungkan niatku untuk berdebat dengannya."

    play sound walking_fast

    n "Aku menaikan kecepatan kakiku untuk melangkah pergi ke kelas."

    n "Berbeda denganku yang merasa khawatir, Ivan hanya tersenyum lalu berjalan kembali."

    n "Dia tidak mengubah kecepatan jalannya."

    play sound walking_fast

    n "Aku tidak peduli dengannya dan terus berjalan cukup cepat."


    #dikelas

    play music kelas fadeout 1.0 fadein 1.0

    scene bg kelas with fade

    n "Aku berharap dapat sampai di kelas dengan tepat waktu."

    n "Tapi sayang guru sudah ada di dalam dan hukuman sudah siap datang padaku."

    n "Aku berdiri di depan kelas, dan mendapatkan teguran dari Pak Andi."


    #Lisa

    #Pak Guru
    g "“Lisa, kamu telat 2 menit.”"

    g "“Rumahmu kan dekat, kenapa bisa sampai terlambat?!”"

    l "“An-anu, Pak. Soalnya”"

    g "“Rok kamu juga kotor, sebenarnya apa yang kamu lakukan tadi pagi.”"

    n "Geram kesal Pak Andi melihatku."

    n "Aku benar-benar malu."

    n "Terdengar tertawaan kecil dari teman-temanku yang melihat rokku."

    n "Ini semua salahnya."

    n "Salah Ivan yang mendorongku hingga membuat rokku kotor seperti ini."

    g "“Lisa, aku tau kamu ini sangat pintar. Tapi tolong sikapmu itu.”"

    #Lisa
    l "“Ini bukan salah Lisa Pak!"

    l "Ivan yang tiba-tiba mendorongku hingga aku terjatuh!!”"

    n "Teriak kesalku saat itu."

    show ivan_kesel at my_near with dissolve

   
    i "“Itu tidak sengaja! Sudah kubilang kalau aku tergelincir, kan?!”"

    n "Secara bersamaan juga, Ivan masuk ke kelas dan membantah perkataanku."

    l "“Pembohong! Kamu pasti sengaja, kan?!”"

    g "“Ivan!! Kamu terlambat 5 menit, dan juga.......”"

    g "“Jadi ternyata kamu yang menyebabkan Lisa terlambat yah?!”"

    hide ivan_kesel at my_near

    show ivan_kaget at my_near

    i "“Haaah?!”"


    hide ivan_kaget at my_near

    show ivan_kesel at my_near


    i "“Lisa terlambat karena ulah Arthur, dia malah berdiam diri menunggunya.”"

    l "“Iya Pak, dia yang membuatku terlambat!!”"


    hide ivan_kesel at my_near

    show ivan_marah at my_near

    i "“Li....{w} saaa!”"

    l "“Lihat Pak! Dia mulai mengancamku!!”"

    g "“Baiklah kalau begitu, Lisa cepat duduk di kursimu!”"

    hide ivan_marah at my_near

    show ivan_tablo at my_near

    g "“Dan Ivan...”"

    hide ivan_tablo at my_near

    show ivan_kaget at my_near

    g "“Berdiri diluar kelas! Sekarang!!”"

    n "Geram sangat kesal Pak Andi."

    hide ivan_kaget at my_near

    show ivan_marah at my_near

    i "“Kenapa hanya aku yang dihukum?! Dia juga terlam –”"

    hide ivan_marah at my_near

    show ivan_kesel at my_near

    n "Ivan mencoba membela dirinya sendiri."

    n "Tapi langsung terdiam dan menatap kesal ke arahku yang berjalan menuju tempat duduk."

    l "“Bleee...”"
    
    n "Saat Ivan melihatku, aku langsung memasang wajah menghina padanya."

    hide ivan_kesel at my_near
    

    with dissolve

    n "Sedangkan dia hanya bergeram kesal sambil berjalan menuju pintu keluar."


    show ivan_kesel at my_near
   

    with dissolve

   


    i "“Baiklah! Aku keluar!!”"

    i "“Paling tidak biarkan aku memakai jaketku!”"

    i "“Diluar sangat dingin!”"

    n "Teriak kesal Ivan sambil menyimpan tas dan keluar membawa jaketnya."

    hide ivan_kesel at my_near with dissolve

    n "Aku tau ini."

    n "jika dia terdesak seperti itu."

    n "Dia pasti akan menerima hukuman Pak Andi."

    n "Lagipula dia juga tidak suka matematika, sudah dipastikan kalau dia ingin menunggu di luar kelas."

    n "Tapi aku lupa kalau di luar cuacanya cukup dingin."

    n "Apa aku terlalu berlebihan?"

    n "Apa jangan-jangan dia merasa kesal karena kelakukanku ini?"

    n "Sepertinya aku harus meminta maaf padanya nanti."



    #waktu istirahat

    #bell bunyi istirahat

    play sound "<from 1 to 7.5>sfx/classbell.wav"

    scene bg koridor with fade

    play music koridor_sekolah fadeout 1.0 fadein 1.0


    n "Bel masuk dari istirahat telah berbunyi."

    n "Aku tidak percaya ini."

    n "Dia benar-benar mengesalkan!"

    n "Aku mencoba meminta maaf padanya."

    n "Pada Ivan."

    n "Tapi coba apa yang dia katakan?!"

## Efek fade flashback

    with fade
    
    show ivan_sebel at my_near with dissolve

    i "“Jangan ge’er.”"

    i "“Aku menuruti perintah Pak Andi bukan karenamu!”"

    i "“Aku hanya malas mengikuti pelajarannya.”"

    i "“Em.......”"

    hide ivan_sebel at my_near

    show ivan_tablo at my_near

    i "“Tapi perasaan aku sudah mengatakan ini padamu?”"

    hide ivan_tablo at my_near

    show ivan_senyum at my_near

    i "“Apa cuman imajinasiku saja yah, ahahahaha!”"

    hide ivan_senyum at my_near with dissolve

    n "Lalu Ivan berjalan ke arah kantin bersama teman dekatnya, Hadi."

    n "Kekhawaktiranku padanya benar-benar sebuah penyesalan terberatku."

    n "Aku benar-benar menyesal karena sudah mengkhawatirkannya."

    n "Dan serius, ada apa dengan sikapnya itu?"

    n "Kenapa dia sangat menyebalkan."

    n "Apa dia memperlakukan gadis lainnya seperti itu?"

    n "Jika benar, pantas saja dia tidak laku-laku."

    n "Sifatnya itu benar-benar mengesalkan."

    n "Dia tidak pernah mengerti perasaan seorang gadis!!"


    #bell masuk
    play sound "<from 1 to 7.5>sfx/classbell.wav"
    play music sesuatu fadeout 1.0 fadein 1.0

    scene bg kelas with fade

    n "Akhirnya kita memasuki pelajaran terakhir."

    n "Setelah ini aku akan menemuinya."

    n "Menemui Arthur."

    n "Aku akan mengungkapkan perasaanku padanya."

    n "Mentalku sudah kuat."

    n "Aku sudah siap menerima kabar terburuk dari mulutnya."

    #end of chapter 1

    jump chapter_2