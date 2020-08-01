#import library
import speech_recognition as sr
import os

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable

folder_name_1 = "Splits/audio_file2_00"
folder_name_2 = "Splits/audio_file2_0"
folder_name_3 = "Splits/audio_file2_"
f = open("Text_file.txt","w+")


# give the number of audio file chunks that you want to convert
n= 526

for i in range(0,n):
    if i<10:
        file_path = folder_name_1 + str(i) + ".wav"
        with sr.AudioFile(file_path) as source:
            audio_text = r.listen(source)
    elif i<100:
        file_path = folder_name_2 + str(i) + ".wav"
        with sr.AudioFile(file_path) as source:
            audio_text = r.listen(source)
    else:
        file_path = folder_name_3 + str(i) + ".wav"
        with sr.AudioFile(file_path) as source:
            audio_text = r.listen(source)
            
    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        
        # using google speech recognition
        text = r.recognize_google(audio_text)
        #print('Converting audio transcripts into text ...')
        #print(text)
        f.write(text+" ")

    except:
        print('Sorry.. run again...')
f.close()
