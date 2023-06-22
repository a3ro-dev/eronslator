import googletrans
import speech_recognition
import gtts
from audioplayer import AudioPlayer
import os
import datetime
import time
import platform

langc = ('''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
Languages supported:

>>  af: afrikaans,
>>  sq: albanian,
>>  am: amharic,
>>  ar: arabic,
>>  hy: armenian,
>>  az: azerbaijani,
>>  eu: basque,
>>  be: belarusian,
>>  bn: bengali,
>>  bs: bosnian,
>>  bg: bulgarian, 
>>  ca: catalan,
>>  ceb: cebuano,
>>  ny: chichewa,
>>  zh-cn: chinese (simplified),
>>  zh-tw: chinese (traditional),
>>  co: corsican,
>>  hr: croatian,
>>  cs: czech,
>>  da: danish,
>>  nl: dutch,
>>  en: english,
>>  eo: esperanto,
>>  et: estonian,
>>  tl: filipino,
>>  fi: finnish,
>>  fr: french,
>>  fy: frisian,
>>  gl: galician,
>>  ka: georgian,
>>  de: german,
>>  el: greek,
>>  gu: gujarati,
>>  ht: haitian creole,
>>  ha: hausa,
>>  haw: hawaiian,
>>  iw: hebrew,
>>  he: hebrew,
>>  hi: hindi,
>>  hmn: hmong,
>>  hu: hungarian,
>>  is: icelandic,
>>  ig: igbo,
>>  id: indonesian,
>>  ga: irish,
>>  it: italian,
>>  ja: japanese,
>>  jw: javanese,
>>  kn: kannada,
>>  kk: kazakh,
>>  km: khmer,
>>  ko: korean,
>>  ku: kurdish (kurmanji),
>>  ky: kyrgyz,
>>  lo: lao,
>>  la: latin,
>>  lv: latvian,
>>  lt: lithuanian,
>>  lb: luxembourgish,
>>  mk: macedonian,
>>  mg: malagasy,
>>  ms: malay,
>>  ml: malayalam,
>>  mt: maltese,
>>  mi: maori,
>>  mr: marathi,
>>  mn: mongolian,
>>  my: myanmar (burmese),
>>  ne: nepali,
>>  no: norwegian,
>>  or: odia,
>>  ps: pashto,
>>  fa: persian,
>>  pl: polish,
>>  pt: portuguese,
>>  pa: punjabi,
>>  ro: romanian,
>>  ru: russian,
>>  sm: samoan,
>>  gd: scots gaelic,
>>  sr: serbian,
>>  st: sesotho,
>>  sn: shona,
>>  sd: sindhi,
>>  si: sinhala,
>>  sk: slovak,
>>  sl: slovenian,
>>  so: somali,
>>  es: spanish,
>>  su: sundanese,
>>  sw: swahili,
>>  sv: swedish,
>>  tg: tajik,
>>  ta: tamil,
>>  te: telugu,
>>  th: thai,
>>  tr: turkish,
>>  uk: ukrainian,
>>  ur: urdu,
>>  ug: uyghur,
>>  uz: uzbek,
>>  vi: vietnamese,
>>  cy: welsh,
>>  xh: xhosa,
>>  yi: yiddish,
>>  yo: yoruba,
>>  zu: zulu   




------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------          
''')



AppName = 'Eronslator'
Developer = 'Aero'
Version = '2.0.1'
Machine = platform.uname()
Translation = googletrans.Translator()
Recognition = speech_recognition.Recognizer()
Clear = lambda: os.system('cls')
Now = datetime.datetime.now()
Time = Now.strftime("%H_%M_%S")




print('--------------------------------')
print(f'Welcome To {AppName}')
print(f'''
        App Version: {Version}
        Developer: {Developer}
      
        Operating System: {Machine.system}_{Machine.release}
        Hardware: {Machine.machine} {Machine.processor}''')
print('Checking For Microphones')

print('If Microphone Is Not Detected')
print('Helpful Links')
print('''
         MacOs: https://www.howtogeek.com/682514/microphone-not-working-on-a-mac-heres-how-to-fix-it 
         Windows: https://support.microsoft.com/en-us/windows/fix-microphone-problems-5f230348-106d-bfa4-1db5-336f35576011
         Linux (Ubuntu): https://candid.technology/ubuntu-microphone-not-working/ 
          ''')
print('Getting Ready To Listen')
print('--------------------------------')



time.sleep(5)




while(True):
            print('Press CTRL+C to exit')
            
            try:
                with speech_recognition.Microphone() as Source:
                    print('I am Ready to Listen')
                    
                    print('I am Listening...')
                    
                    v = Recognition.listen(Source)
                    
                    i = Recognition.recognize_google(v)


                    
                    to = input("Enter Language Code To Which Your Input Should Be Translated: \n")
                    
                    t = Translation.translate(i, dest=to)
                    
                    Clear()
                    
                    
                with open(f"files/{t.src}_{to}_{Time}.txt", "x", encoding="utf-8") as f: #type: ignore
                    f.write(f'''
        Source: {i}
        Source Language: {t.src} 
                    
        Translated Output: {t.text}
        Translated Language: {t.dest}
        Translated Output Pronunciation: {t.pronunciation}
                            ''')
                    v_ot = gtts.gTTS(t.text, lang=to)
                    v_ot.save(f"files/{t.src}_{to}_{Time}.mp3")
                    wee = f"{t.src}_{to}_{Time}"
                    AudioPlayer(f"files/{wee}.mp3").play(block=True)
            
            except Exception as e:
                print("Please Run The Program Again As The Program Landed Into An Error")
                
                
                
                print(f"Error: {e}")
