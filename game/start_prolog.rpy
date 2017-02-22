
label start_prolog:

   #Prolog
    scene white with Dissolve(1.0)

    $ renpy.pause(2.0, hard=True)

    stop music fadeout 3.0

    play sound opendoor_morning

    play sound walking_morning

    scene black with dissolve
    
    n "Aku perlahan membuka pintu rumahku."

    n "Lalu berjalan cukup pelan menuju sekolah."

    show langit with dissolve

    n "Langit yang berwarna biru muda."

    n" Udara yang cukup dingin."

    n "Mengiringi kepergianku untuk terus melangkahkan kakiku ke sekolah."

    hide langit with dissolve
    play sound birds

    ## masukan CG disini
    show lisa_cg with dissolve:

        #show from bottom
        xalign 0.0 yalign 1.0

        #move to top with 1.0 seconds
        linear 2.5 yalign 0.0


    
    n "Namaku Lisa Angelic."

    n "Aku bisa terbilang populer karena kecantikanku. Dan karena gen dari orang tuaku yang berasal dari negara Inggris."

    n "Bahkan beberapa lelaki pernah memintaku untuk menjadi kekasih mereka."

    n "Tapi sayangnya aku menolak mereka."

    
    hide lisa_cg

    show lisa_cg2

    n "Alasannya tentu saja karena aku sudah mempunyai lelaki yang aku suka."

    hide lisa_cg2 with dissolve

    scene bg jalanan_baru2 with dissolve

    play sound walking_morning

    n "Aku berjalan melewati beberapa gedung tinggi yang biasa dipanggil apartemen."

    n "Aku berjalan pelan tidak ingin terburu-buru."

    n "Kulihat jam tangan yang berada ditangan kananku menunjukan bahwa waktu masih cukup pagi."

    play sound birds

    n "Kicauan beberapa burung di lingkunganku terdengar sangat merdu."

    n "Seolah-olah mereka sedang bernyanyi untukku."

    n "Untuk sesaat aku hanya berdiam diri."

    l "“Aku masih memiliki banyak waktu untuk pergi ke sekolah.”"

    scene black with fade 
    
    n "Aku memejamkan mataku."

    n "Menghirup udara segar di pagi hari."

    n "Aku menyukuri karunia Tuhan yang Dia berikan padaku."

    play sound walking_fast

    n "Aku beryukur bisa hidup sampai saat ini."

    play sound hit_body

    
    with Shake((0, 0, 0, 0), 0.5, dist=15)

    l "“...!!!”"

    scene bg jalanan_baru2 with fade

    play music prolog fadeout 1.0 fadein 1.0

    n "Disaat aku sedang merasakan nikmatnya suasana pagi hari."

    n "Disaat aku sedang merasakan ketenangan jiwaku ini."

    n "Tiba-tiba dalam sekejap tubuhku terdorong oleh seseorang di belakangku."

    n "Dia mendorongku hingga terjatuh ke tanah."

    show ivan_senyum at my_near

    with dissolve



    i "“Maaf Lisa, aku tergelincir!!”"

    n "Jika dia benar-benar tergelincir, tentu saja aku bisa memaafkannya."

    n "Tapi nadanya itu!"

    n "Dia seakan-akan sengaja mendorongku hingga aku terjatuh seperti ini."

    l "“Pembohong!”"

    l "“Kamu hanya mengusiliku lagi, kan?!”"

    i "“Ahahahaha, ketauan yah? Padahal –“"


    
    hide ivan_senyum at my_near

    play sound pecah

    show ivan_kaget behind vas_bunga at my_near, Shake(None, 1.0, dist=5)


    n "Perkataan lelaki tersebut terhentikan karena dia menghindari sesuatu yang jatuh diatasnya."

    #clip pot
    
    show vas_bunga with dissolve

    n "Sebuah vas bunga jatuh tepat diatas lelaki tersebut."

    n "Tapi untung saja dia dapat menghindari vas bunga tersebut dengan cepat."

    n "Wajahnya benar-benar terlihat ketakutan."

    n "Aku hanya bisa tertawa kecil melihat wajahnya."

    hide vas_bunga  with dissolve

    hide ivan_kaget at my_near

    #Ivan
    show ivan_marah at my_near

    i "“Ke-kenapa kamu malah tertawa!”"

    #Lisa
    l "“Ahahahahaha, rasakan itu Ivan!”"

    l "“Itu karma dari Tuhan karena telah usil kepadaku!”"

    #Ivan
    i "“I-itu tidak lucu!”"

    i "“Bagaimana kalau vas itu mengenai kepalaku!”"

    #Lisa
    l "“Entahlah. Mungkin kepalamu hanya akan bocor...”"

    n "Aku tersenyum."

    n "Lalu berdiri, dan membersihkan rokku yang kotor."

    ## show bg cinema


    show cinema with dissolve

    show ivan_normal at my_near with dissolve


    n "Lelaki yang berada didepanku ini bernama Ivan."

    n "Dia teman masa kecilku."

    n "Entah sejak kapan aku benar-benar tidak pernah mengerti dengan jalan pikirannya."

    n "Dia benar-benar sangat mengangguku dengan alasan yang tidak jelas seperti tadi."
    
    n "Dia juga satu-satunya temanku yang mengetahui kondisiku, kondisi tubuhku yang lemah."
    
    n "Tapi meski dia mengetahui kondisi tubuhku ini, dia tetap bersikap seperti biasanya padaku."
    
    n "Dia seakan-akan berpura-pura tidak tau tentang kondisiku ini."

    hide cinema with dissolve

    #Ivan
    hide ivan_normal at my_near

    show ivan_marah at my_near


    i "“Apa kamu menginginkan itu?!“"

    i "“Apa kamu menginginkan kepalaku pecah?“"

    #Lisa
    l "“Mungkin saja, jika –“"


    anonim "“Lisa! Ivan...!”"

    hide ivan_marah at my_near with dissolve


    show arthur_normal far at my_left
    show karin_normal far at my_right

    with dissolve

    n "Tiba-tiba terlihat seorang lelaki yang cukup jauh dibelakang kami."

    n "Dia berteriak memotong perkataanku."


    hide arthur_normal far at my_left
    hide karin_normal far at my_right

    with dissolve

    n "Aku sudah tau siapa yang berteriak."
    
    n "Aku bisa tau orang tersebut hanya dengan mendengar suaranya saja."
    
    n "Alasannya tentu saja karena aku sangat menyukai lelaki tersebut."

    with dissolve

    show cinema with dissolve

    show arthur_normal at my_near with dissolve

    ## show bg cinema


    n "Arthur Ryuuki."

    n "Lelaki  yang sangat populer disekolahku."

    n "Lelaki cukup tinggi dengan senyuman yang menawan."

    n "Memiliki rambut hitam yang indah, dan kedua bola mata yang berwarna coklat."
    
    n "Dari hal itu sudah dapat dipastikan kalau dia keturunan dari benua berbeda."

    n "Yakni Eropa dan Asia."
    
    n "Selain tampan dia benar-benar baik dan sangat perhatian terhadap orang lain."

    hide cinema with dissolve

    hide arthur_normal at my_near

    with dissolve

    show ivan_sebel at my_near with dissolve


    i "“Ohh ohhhh, datang mas populer.”"

    ## show bg cinema

    n "Ya, tentu saja sifat Arthur sangat berkebalikan dengan teman masa kecilku ini."

    n "Ivan terkadang memasang wajah yang menyebalkan saat Arthur datang mendekatiku."
    
    n "Tidak hanya itu saja."

    n "Dia bahkan pernah memukul beberapa lelaki yang hampir berpacaran denganku."
    
    n "Aku benar-benar tidak mengerti apa yang dia pikirkan saat itu."
    
    n "Kenapa dia selalu menghalangi kebahagiaanku?!"


    hide ivan_sebel at my_near

    show ivan_tablo at my_near


    l "“Awas jika kamu membuat masalah lagi!”"

    n "Aku tidak ingin Ivan menghancurkan jalan cintaku kali ini."

    hide ivan_tablo at my_near

    show ivan_marah at my_near

    i "“Berisik, ayo kita pergi! Kita hampir terlam –“"

    l "“Apa yang kamu katakan?! Kita harus menunggu Art –“"

    hide ivan_marah at my_near with dissolve

    #Karin
    show karin_normal at my_near

    with dissolve

    k "“Ivan!!”"

    n "Aku tidak menyadari keberadaan gadis tersebut."
    
    n "Saat Arthur berteriak, aku hanya fokus memperhatikannya dan tidak melirik yang lainnya."

    hide karin_normal at my_near with dissolve

    show ivan_ngeledek at my_near with dissolve

    i "“Ciee, rivalnya datang”"

    n "Aku hanya melirik sinis Ivan."

    n "Wajahnya saat ini benar-benar membuatku kesal." 
    
    n "Dia terlihat bahagia saat aku terbakar cemburu seperti ini."


    hide ivan_ngeledek at my_near

    show ivan_senyum at my_near

    i "“Yooo Karin!!”"

    n "Ivan berteriak membalas teriakan gadis tersebut."

    n "Gadis yang berjalan bersama dengan Arthur."


    hide ivan_senyum at my_near

    show cinema with dissolve

    show karin_normal at my_near with dissolve

    n "Karin Viona."

    n "Gadis cantik keturunan Rusia ini merupakan rivalku."
    
    n "Bukan rival karena kepopuleran di sekolah, tetapi karena Arthur."
    
    n "Aku tidak tau perasaanya pada Arthur."

    n "Tapi dia benar-benar sangat dekat dengan Arthur."
    
    n "Mereka bagaikan sepasang kekasih bagiku."

    hide cinema with dissolve

    hide karin_normal at my_near

    #show ivan
    show ivan_senyum at my_near


    hide ivan_senyum at my_near
    with dissolve

    show arthur_segan2 at my_near
    with dissolve


    a "“Maaf membuat kalian menunggu.”"

    n "Sementara aku berpikir tentang hubungan Arhur dan Karin."

    n "Tanpa aku sadari kalau mereka sudah berada di dekat kami."


    hide arthur_segan2 at my_near
    with dissolve


    show ivan_marah at my_near

    i "“Memang benar kamu membuat kami menunggu!”"

    i "“Apa tidak bisa lebih cepa –”"

    hide ivan_marah at my_near


    show ivan_kaget at my_near, Shake(None, 1.0, dist=5)

    play sound hit_body

    l "“Ti-tidak apa kok!”"

    l "“Berangkat bersama-sama kan lebih seru!”"

    n "Aku tersenyum sambil menginjak kaki Ivan."

    n "Aku menginjak kakinya sekuat tenagaku hingga dia memasang wajah yang kesakitan."

    hide ivan_kaget at my_near

    show ivan_marah at my_near

    i "“Sa-sakit! Apa yang kamu---”"

    hide ivan_marah at my_near

    show ivan_kaget at my_near

    l "“Ayo kita berangkat!”"

   
    hide ivan_kaget at my_near

    show ivan_kesel at my_near


    n "Kembali lagi perkataan Ivan terpotong olehku."


    n "Aku langsung menarik lengan Arthur."

    hide ivan_kesel at my_near

    with dissolve

    show karin_marah at my_near with dissolve


    n "Untuk sekilas, kulihat tatapan yang tidak mengenakan dari Karin."

    n "Saat aku menarik tangan Arthur."

    n "Dia benar-benar menatapaku dengan tatapan yang seolah-olah sedang menahan amarahnya."

    n "Tapi aku tidak takut dengan tatapanya!"

    n "Aku akan membuat Arthur menjadi milikku!"


    hide karin_marah at my_near with dissolve

    with dissolve


    play sound walking_morning

    n "Kami berjalan ke sekolah secara berpasangan."

    n "Aku dengan Arthur.{w} Karin dengan Ivan."

    n "Tekanan udara menjadi semakin berat."

    n "Aku ingin melihat suasana disekitar Ivan dan Karin."

    n "Aku menolehkan kepalaku ke belakang."


    with fade

    show ivan_kesel normal at my_left

    show karin_marah normal at my_right

    with dissolve



    n "Terlihat tatapan yang tajam dari mereka berdua ke arahku."

    n "Ok, aku bisa mengerti alasan Karin menatap tajam diriku."

    n "Tapi kenapa Ivan juga menatapku seperti itu?"

    n "Apa dia cemburu padaku?!"

    n "Apa dia menyukaiku?"

    n "Ahahaha..."

    n "Anggapan tersebut merupakan anggapan terakhir yang aku berikan pada Ivan."

    n "Dia mustahil menyukai gadis yang selalu ia ganggu."

    n "Gadis sepertiku hanya ia anggap sebagai mainan untuk leluconnya."



    n "Satu-satunya yang terpikirkan olehku adalah."

    n "Dia ingin menggagalkan jalan cintaku lagi?"

    n "Sebenarnya seberapa mengesalkannya anak ini!"

    n "Kenapa dia sangat senang melihatku menderita?!"

    n "Aku harus bergerak cepat!"

    n "Banyak orang yang menghalangi jalan cintaku kali ini."


    hide ivan_kesel normal at left

    hide karin_marah normal at right

    with dissolve

    n "Pulang sekolah nanti aku harus mengatakannya."

    n "Aku harus mengatakan..."

    n "Kalau aku menyukai Arthur."
 

    jump chapter_1