import struct, json, os

try:
    os.mkdir("amb")

except:
    pass

try:
    os.makedirs("amb/jd14")

    print('The directories have been made.')
    
    input('Insert your ckd files in amb/jd14 and then run the tool again to deserialize the tapes.')

except:
    pass

for tpl in os.listdir("amb/jd14"):
    if tpl.endswith('.tpl.ckd'):
        print('deserializing '+tpl)
        ambtpl={
    "__class": "Actor_Template",
    "WIP": 0,
    "LOWUPDATE": 0,
    "UPDATE_LAYER": 0,
    "PROCEDURAL": 0,
    "STARTPAUSED": 0,
    "FORCEISENVIRONMENT": 0,
    "COMPONENTS": [{
            "__class": "SoundComponent_Template",
            "soundList": [{
                    "__class": "SoundDescriptor_Template",
                    "name": "",
                    "volume": 0,
                    "category": "amb",
                    "limitCategory": "",
                    "limitMode": 0,
                    "maxInstances": 1,
                    "files": [],
                    "serialPlayingMode": 0,
                    "serialStoppingMode": 0,
                    "params": {
                        "__class": "SoundParams",
                        "loop": 0,
                        "playMode": 1,
                        "playModeInput": "",
                        "randomVolMin": 0,
                        "randomVolMax": 0,
                        "delay": 0,
                        "randomDelay": 0,
                        "pitch": 1,
                        "randomPitchMin": 1,
                        "randomPitchMax": 1,
                        "fadeInTime": 0,
                        "fadeOutTime": 0,
                        "filterFrequency": 0,
                        "filterType": 2,
                        "transitionSampleOffset": 0
                    },
                    "pauseInsensitiveFlags": 0,
                    "outDevices": 4294967295,
                    "soundPlayAfterdestroy": 0
                }
            ]
        }
    ]
}

        m=open("amb/jd14/"+tpl,"rb")
        m.read(96)
        ambcount=struct.unpack('>I',m.read(4))[0]
        for amb in range(ambcount):
            amb_path_len=struct.unpack('>I',m.read(4))[0]
            amb_path=m.read(amb_path_len).decode('utf-8')
            amb_file_len=struct.unpack('>I',m.read(4))[0]
            amb_file=m.read(amb_file_len).decode('utf-8')
            amb_zlib=m.read(4)
            m.read(4)
            ambtpl["COMPONENTS"][0]["soundList"][0]["files"].append(amb_path.replace('jd5','maps')+amb_file)

        json.dump(ambtpl,open("amb/"+tpl,"w"))