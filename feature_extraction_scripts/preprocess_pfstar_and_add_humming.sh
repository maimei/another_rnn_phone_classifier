#!/bin/bash
#
#  $1 scp file (train/eval/valid) 
#  $2 target location for a wav file
#  $3 output rate (resample!)
#  $4 humming normalisation
#  $5 speech normalisation

# Hard coded babble noise file location:
noisefile=/teamwork/t40511_asr/c/noisex92/audio_wav/volvo.wav
noisedursamples=3763687

tmpspeechfile=/dev/shm/noise.wav
tmpnoisefile=/dev/shm/speech.wav


sox $1 -t wav -r 16000 -c 1 -b 16 --encoding signed-integer $tmpspeechfile speed $3 norm $5

speechdursamples=`soxi -s $tmpspeechfile`

sox $noisefile -r 16000 -c 1 -b 16 $tmpnoisefile trim `shuf -i 0-$(( $noisedursamples - $speechdursamples )) -n 1`s ${speechdursamples}s norm $4

sox -m $tmpnoisefile $tmpspeechfile -t raw -r 8000 -c 1 -b 16 --encoding signed-integer $2

rm $tmpspeechfile
rm $tmpnoisefile


