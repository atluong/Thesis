from pydub import AudioSegment
from pydub.utils import make_chunks
import os, subprocess

samples = int(3/0.04)
max_chunk = 7500
chunk_len = 40

myaudio = AudioSegment.from_file("test_1.wav", "wav")
chunks = make_chunks(myaudio, chunk_len)

for i, chunk in enumerate(chunks):
    chunk_name = "test_chunk{0}.wav".format(i)
    print ("exporting {}".format(chunk_name))
    chunk.export(chunk_name, format="wav")    

for i in range(max_chunk):
    print ("i = {}".format(i))
    for j in range(samples):    
        index = i + j        
        if j is 0:
            if i >= max_chunk - 2:
                sound1 = AudioSegment.from_wav('test_chunk%s.wav' % (index-1))
                sound2 = AudioSegment.from_wav('test_chunk%s.wav' % (index-2)) 
                sound = sound1 + sound2
                break
            else:
                sound = AudioSegment.from_wav('test_chunk%s.wav' % index) 
        else:       
            if index >= max_chunk:
                break
            else:
                sound = sound + AudioSegment.from_wav('test_chunk%s.wav' % index)
    
        combined = sound
        combined.export("test_test.wav", format="wav")        
        
    os.chdir(r"/home/andy/scripts/opensmile-2.3.0/bin/linux_x64_standalone_libstdc6")
    FNULL = open(os.devnull, 'w')     
    args = r"./SMILExtract -C /home/andy/scripts/opensmile-2.3.0/config/gemaps/eGeMAPSv01a.conf -I /home/andy/scripts/features/test_test.wav -O /home/andy/scripts/features/test_1.csv"
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=True)    
    os.chdir(r"/home/andy/scripts/features")  

myaudio = AudioSegment.from_file("test_2.wav", "wav")
chunks = make_chunks(myaudio, chunk_len)

for i, chunk in enumerate(chunks):
    chunk_name = "test_chunk{0}.wav".format(i)
    print ("exporting {}".format(chunk_name))
    chunk.export(chunk_name, format="wav")    

for i in range(max_chunk):
    print ("i = {}".format(i))
    for j in range(samples):    
        index = i + j        
        if j is 0:
            if i >= max_chunk - 2:
                sound1 = AudioSegment.from_wav('test_chunk%s.wav' % (index-1))
                sound2 = AudioSegment.from_wav('test_chunk%s.wav' % (index-2)) 
                sound = sound1 + sound2
                break
            else:
                sound = AudioSegment.from_wav('test_chunk%s.wav' % index) 
        else:       
            if index >= max_chunk:
                break
            else:
                sound = sound + AudioSegment.from_wav('test_chunk%s.wav' % index)
    
        combined = sound
        combined.export("test_test.wav", format="wav")        
        
    os.chdir(r"/home/andy/scripts/opensmile-2.3.0/bin/linux_x64_standalone_libstdc6")
    FNULL = open(os.devnull, 'w')     
    args = r"./SMILExtract -C /home/andy/scripts/opensmile-2.3.0/config/gemaps/eGeMAPSv01a.conf -I /home/andy/scripts/features/test_test.wav -O /home/andy/scripts/features/test_2.csv"
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=True)    
    os.chdir(r"/home/andy/scripts/features")  

myaudio = AudioSegment.from_file("test_3.wav", "wav")
chunks = make_chunks(myaudio, chunk_len)

for i, chunk in enumerate(chunks):
    chunk_name = "test_chunk{0}.wav".format(i)
    print ("exporting {}".format(chunk_name))
    chunk.export(chunk_name, format="wav")    

for i in range(max_chunk):
    print ("i = {}".format(i))
    for j in range(samples):    
        index = i + j        
        if j is 0:
            if i >= max_chunk - 2:
                sound1 = AudioSegment.from_wav('test_chunk%s.wav' % (index-1))
                sound2 = AudioSegment.from_wav('test_chunk%s.wav' % (index-2)) 
                sound = sound1 + sound2
                break
            else:
                sound = AudioSegment.from_wav('test_chunk%s.wav' % index) 
        else:       
            if index >= max_chunk:
                break
            else:
                sound = sound + AudioSegment.from_wav('test_chunk%s.wav' % index)
    
        combined = sound
        combined.export("test_test.wav", format="wav")        
        
    os.chdir(r"/home/andy/scripts/opensmile-2.3.0/bin/linux_x64_standalone_libstdc6")
    FNULL = open(os.devnull, 'w')     
    args = r"./SMILExtract -C /home/andy/scripts/opensmile-2.3.0/config/gemaps/eGeMAPSv01a.conf -I /home/andy/scripts/features/test_test.wav -O /home/andy/scripts/features/test_3.csv"
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=True)    
    os.chdir(r"/home/andy/scripts/features")  

myaudio = AudioSegment.from_file("test_4.wav", "wav")
chunks = make_chunks(myaudio, chunk_len)

for i, chunk in enumerate(chunks):
    chunk_name = "test_chunk{0}.wav".format(i)
    print ("exporting {}".format(chunk_name))
    chunk.export(chunk_name, format="wav")    

for i in range(max_chunk):
    print ("i = {}".format(i))
    for j in range(samples):    
        index = i + j        
        if j is 0:
            if i >= max_chunk - 2:
                sound1 = AudioSegment.from_wav('test_chunk%s.wav' % (index-1))
                sound2 = AudioSegment.from_wav('test_chunk%s.wav' % (index-2)) 
                sound = sound1 + sound2
                break
            else:
                sound = AudioSegment.from_wav('test_chunk%s.wav' % index) 
        else:       
            if index >= max_chunk:
                break
            else:
                sound = sound + AudioSegment.from_wav('test_chunk%s.wav' % index)
    
        combined = sound
        combined.export("test_test.wav", format="wav")        
        
    os.chdir(r"/home/andy/scripts/opensmile-2.3.0/bin/linux_x64_standalone_libstdc6")
    FNULL = open(os.devnull, 'w')     
    args = r"./SMILExtract -C /home/andy/scripts/opensmile-2.3.0/config/gemaps/eGeMAPSv01a.conf -I /home/andy/scripts/features/test_test.wav -O /home/andy/scripts/features/test_4.csv"
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=True)    
    os.chdir(r"/home/andy/scripts/features")  

myaudio = AudioSegment.from_file("test_5.wav", "wav")
chunks = make_chunks(myaudio, chunk_len)

for i, chunk in enumerate(chunks):
    chunk_name = "test_chunk{0}.wav".format(i)
    print ("exporting {}".format(chunk_name))
    chunk.export(chunk_name, format="wav")    

for i in range(max_chunk):
    print ("i = {}".format(i))
    for j in range(samples):    
        index = i + j        
        if j is 0:
            if i >= max_chunk - 2:
                sound1 = AudioSegment.from_wav('test_chunk%s.wav' % (index-1))
                sound2 = AudioSegment.from_wav('test_chunk%s.wav' % (index-2)) 
                sound = sound1 + sound2
                break
            else:
                sound = AudioSegment.from_wav('test_chunk%s.wav' % index) 
        else:       
            if index >= max_chunk:
                break
            else:
                sound = sound + AudioSegment.from_wav('test_chunk%s.wav' % index)
    
        combined = sound
        combined.export("test_test.wav", format="wav")        
        
    os.chdir(r"/home/andy/scripts/opensmile-2.3.0/bin/linux_x64_standalone_libstdc6")
    FNULL = open(os.devnull, 'w')     
    args = r"./SMILExtract -C /home/andy/scripts/opensmile-2.3.0/config/gemaps/eGeMAPSv01a.conf -I /home/andy/scripts/features/test_test.wav -O /home/andy/scripts/features/test_5.csv"
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=True)    
    os.chdir(r"/home/andy/scripts/features")  

myaudio = AudioSegment.from_file("test_6.wav", "wav")
chunks = make_chunks(myaudio, chunk_len)

for i, chunk in enumerate(chunks):
    chunk_name = "test_chunk{0}.wav".format(i)
    print ("exporting {}".format(chunk_name))
    chunk.export(chunk_name, format="wav")    

for i in range(max_chunk):
    print ("i = {}".format(i))
    for j in range(samples):    
        index = i + j        
        if j is 0:
            if i >= max_chunk - 2:
                sound1 = AudioSegment.from_wav('test_chunk%s.wav' % (index-1))
                sound2 = AudioSegment.from_wav('test_chunk%s.wav' % (index-2)) 
                sound = sound1 + sound2
                break
            else:
                sound = AudioSegment.from_wav('test_chunk%s.wav' % index) 
        else:       
            if index >= max_chunk:
                break
            else:
                sound = sound + AudioSegment.from_wav('test_chunk%s.wav' % index)
    
        combined = sound
        combined.export("test_test.wav", format="wav")        
        
    os.chdir(r"/home/andy/scripts/opensmile-2.3.0/bin/linux_x64_standalone_libstdc6")
    FNULL = open(os.devnull, 'w')     
    args = r"./SMILExtract -C /home/andy/scripts/opensmile-2.3.0/config/gemaps/eGeMAPSv01a.conf -I /home/andy/scripts/features/test_test.wav -O /home/andy/scripts/features/test_6.csv"
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=True)    
    os.chdir(r"/home/andy/scripts/features")  

myaudio = AudioSegment.from_file("test_7.wav", "wav")
chunks = make_chunks(myaudio, chunk_len)

for i, chunk in enumerate(chunks):
    chunk_name = "test_chunk{0}.wav".format(i)
    print ("exporting {}".format(chunk_name))
    chunk.export(chunk_name, format="wav")    

for i in range(max_chunk):
    print ("i = {}".format(i))
    for j in range(samples):    
        index = i + j        
        if j is 0:
            if i >= max_chunk - 2:
                sound1 = AudioSegment.from_wav('test_chunk%s.wav' % (index-1))
                sound2 = AudioSegment.from_wav('test_chunk%s.wav' % (index-2)) 
                sound = sound1 + sound2
                break
            else:
                sound = AudioSegment.from_wav('test_chunk%s.wav' % index) 
        else:       
            if index >= max_chunk:
                break
            else:
                sound = sound + AudioSegment.from_wav('test_chunk%s.wav' % index)
    
        combined = sound
        combined.export("test_test.wav", format="wav")        
        
    os.chdir(r"/home/andy/scripts/opensmile-2.3.0/bin/linux_x64_standalone_libstdc6")
    FNULL = open(os.devnull, 'w')     
    args = r"./SMILExtract -C /home/andy/scripts/opensmile-2.3.0/config/gemaps/eGeMAPSv01a.conf -I /home/andy/scripts/features/test_test.wav -O /home/andy/scripts/features/test_7.csv"
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=True)    
    os.chdir(r"/home/andy/scripts/features")  

myaudio = AudioSegment.from_file("test_8.wav", "wav")
chunks = make_chunks(myaudio, chunk_len)

for i, chunk in enumerate(chunks):
    chunk_name = "test_chunk{0}.wav".format(i)
    print ("exporting {}".format(chunk_name))
    chunk.export(chunk_name, format="wav")    

for i in range(max_chunk):
    print ("i = {}".format(i))
    for j in range(samples):    
        index = i + j        
        if j is 0:
            if i >= max_chunk - 2:
                sound1 = AudioSegment.from_wav('test_chunk%s.wav' % (index-1))
                sound2 = AudioSegment.from_wav('test_chunk%s.wav' % (index-2)) 
                sound = sound1 + sound2
                break
            else:
                sound = AudioSegment.from_wav('test_chunk%s.wav' % index) 
        else:       
            if index >= max_chunk:
                break
            else:
                sound = sound + AudioSegment.from_wav('test_chunk%s.wav' % index)
    
        combined = sound
        combined.export("test_test.wav", format="wav")        
        
    os.chdir(r"/home/andy/scripts/opensmile-2.3.0/bin/linux_x64_standalone_libstdc6")
    FNULL = open(os.devnull, 'w')     
    args = r"./SMILExtract -C /home/andy/scripts/opensmile-2.3.0/config/gemaps/eGeMAPSv01a.conf -I /home/andy/scripts/features/test_test.wav -O /home/andy/scripts/features/test_8.csv"
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=True)    
    os.chdir(r"/home/andy/scripts/features")  

myaudio = AudioSegment.from_file("test_9.wav", "wav")
chunks = make_chunks(myaudio, chunk_len)

for i, chunk in enumerate(chunks):
    chunk_name = "test_chunk{0}.wav".format(i)
    print ("exporting {}".format(chunk_name))
    chunk.export(chunk_name, format="wav")    

for i in range(max_chunk):
    print ("i = {}".format(i))
    for j in range(samples):    
        index = i + j        
        if j is 0:
            if i >= max_chunk - 2:
                sound1 = AudioSegment.from_wav('test_chunk%s.wav' % (index-1))
                sound2 = AudioSegment.from_wav('test_chunk%s.wav' % (index-2)) 
                sound = sound1 + sound2
                break
            else:
                sound = AudioSegment.from_wav('test_chunk%s.wav' % index) 
        else:       
            if index >= max_chunk:
                break
            else:
                sound = sound + AudioSegment.from_wav('test_chunk%s.wav' % index)
    
        combined = sound
        combined.export("test_test.wav", format="wav")        
        
    os.chdir(r"/home/andy/scripts/opensmile-2.3.0/bin/linux_x64_standalone_libstdc6")
    FNULL = open(os.devnull, 'w')     
    args = r"./SMILExtract -C /home/andy/scripts/opensmile-2.3.0/config/gemaps/eGeMAPSv01a.conf -I /home/andy/scripts/features/test_test.wav -O /home/andy/scripts/features/test_9.csv"
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=True)    
    os.chdir(r"/home/andy/scripts/features")      