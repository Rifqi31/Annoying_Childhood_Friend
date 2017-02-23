


label last_scene:

  #cuplikan
 
    show langit2 with fade
    play music sesuatu fadeout 1.0 fadein 1.0

    n "Beberapa bulan, setelah Lisa dan yang lainnya mengunjungi makam Ivan."

    n "Terlihat seorang lelaki paruh baya yang sangat mirip dengan Ivan."

    n "Dia memakai sebuah jas rapih dan berdiri tepat dihadapan kuburan Ivan."

    scene bg batu nisan with fade

    n "Disampingnya terlihat gadis manis yang berumur empat tahun."

    n "Wajahnya sangat lucu dengan rambut lurus berwarna coklat sangat panjang yang mencapai lutut kakinya."


    child "“Papah, kenapa kita ke sini? Kemana mamah dan Haikal?”"

    n "Tanya gadis mungil tersebut sambil menarik pelan celana lelaki tersebut."


    man "“Hana.....{w} Mamahmu dan adikmu sudah pergi duluan ke pernikahan teman pamanmu.”"


    child "“Kalau begitu, paman dimana?”"

    child "“Kenapa dia tidak datang pada pernikahan temannya?”"


    man "“Dia sekarang tepat didepanmu, dia sudah beristirahat dengan tenang, sayang”"

    n "Senyum sang ayah memejamkan matanya."


    child "“Emmmm.”"

    n "Gadis kecil tersebut bergumam lucu seakan paham apa yang dikatakan oleh ayahnya."


    n "Sang ayah mulai membuka matanya, dan menatap tajam kuburan Ivan."

    n "Dia bergumam khawatir dalam hatinya."

    show cinema with dissolve

    man "“Jadi kutukan keluarga Aeldra itu benar adanya?”"

    man "“Aku tidak menyangka kalau adikku sendiri akan terkena kutukan ini.”"

    man "“Apa salah satu anakku juga akan mengalami takdir seperti ini.”"

    man "“Takdir seperti adikku.”"

    man "“Menerima takdir yang menyedihkan dari masa lalu keluarga Aeldra yang kelam.”"

    hide cinema with dissolve

    n "Lanjut lelaki tersebut berpikir sambil melirik khawatir anak perempuannya yang lucu."

    with fade
    
    call thanks

    return



label thanks:

    scene black with fade

    show hatur_nuhun:
        xpos 450 ypos 300

    with dissolve


init:
    image black = Solid((0,0,0))
    image hatur_nuhun = Text("{size=40}{color=#FFFFFF}Thanks for playing",text_align=0.5) 