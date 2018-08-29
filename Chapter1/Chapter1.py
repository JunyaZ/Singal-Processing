# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 17:20:58 2018

@author: ya000
"""
import thinkdsp 
import matplotlib.pyplot
import thinkplot as tp
import math
def signal(offset):
    cos_sig = thinkdsp.CosSignal(freq=1.0, amp=1.0, offset=offset)
    sin_sig = thinkdsp.SinSignal(freq=1.0, amp=1.0, offset=offset)
    cos_wave = cos_sig.make_wave(duration= 0.5, start=0, framerate=8000)
    sin_wave = sin_sig.make_wave(duration= 0.5, start=0, framerate=8000)

    period=  sin_sig.period
    cos_seg = cos_wave.segment (start= 0, duration=period*5)
    sin_seg = sin_wave.segment (start= 0, duration=period*5)

    sin_seg.plot()
    tp.show()
    cos_seg.plot()
    tp.show()



def step_4():
    Sin1 = thinkdsp.CosSignal(freq=261.63, amp=0.5, offset=0)
    Sin2= thinkdsp.CosSignal(freq=329.63, amp=0.5, offset=0)
    Sin3 = thinkdsp.CosSignal(freq=392.0, amp=0.5, offset=0)
    SumSignal = Sin1 + Sin2 + Sin3
    SumSignal_wave=  SumSignal.make_wave(duration= 3, start=0, framerate=8000)

    period =  SumSignal.period
    SumSignal_seg = SumSignal_wave.segment (start= 0, duration=period*5)
    SumSignal_seg.plot()
    tp.show()
    
    SumSignal_wave.write(filename='output.wav')


if __name__ == '__main__':
    signal(0)
    signal(math.pi/2)
    step_4()
