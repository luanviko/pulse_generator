# pulse_generator

Pulses generated by Silicon Photo-multipliers (SiPMs)
are characterized by a sharp rise-time 
followed by an exponential-like decay. 
This behaviour is due to the sudden surge of electric current 
generated by the photo-diode by a photon 
which is then suppressed by a quenching resistor.

This is a small library to simulate a SiPM pulse, 
with an ideal rise time (1-sample long) and 
an ideal tail (exponential decay). 
It is superposed on a baseline of random numbers, 
to simulate electronic noise.

![Example of waveform](/waveform.png)

Generating a pulse can be as simple as:

```
pulse_generator = sipm().create_waveforms()
```

or, if you want to generate 20 waveforms with amplitude between 20 and 30,

```
pulse_generator = sipm(number_of_waveforms=10, amplitude=[20, 30]).create_waveforms()
```

This is a list of parameters you can give **sipm**:
* **number_of_waveforms**: *integer* with the number of waveforms to be generated.
* **amplitude**: *float* or *list* (with minimum and maximum value of range) with the amplitude of the pulses.
* **decay_constant**: *float* telling how wide the pulses are.
* **pulse_position**: *int* with where the pulse is generated within the waveform.
* **jitter_width**: *int* width around **pulse_position**.
* **baseline_offset**: *float* electronic-noise centre line.
* **noise_amplitude**: *float* electronic-noise maximum value around baseline offset.


## References

Based on Numpy.