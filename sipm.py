import numpy as np

class sipm(object):
    
    '''
    Create an arbritrary number of waveforms containing a 
    single positive-going pulse superposed on a random baseline.
    '''

    def __init__(this, 
                number_of_waveforms=1, 
                waveform_size=512,
                amplitude = 100.,
                decay_constant = -1.,
                pulse_position  = 256,
                baseline_offset = 0.,
                noise_amplitude = 10.,
                jitter_width=10
                ):
        this.number_of_waveforms = number_of_waveforms
        this.waveform_size = waveform_size
        this.pulse_position = pulse_position
        this.amplitude = amplitude 
        this.B = decay_constant
        this.baseline_offset = baseline_offset
        this.noise_amplitude = noise_amplitude
        this.jitter_width = jitter_width

    def __str__(this):
        '''
        Print ndarray with dictionaries of waveforms.
        @params: ndarray with waveforms.
        @return: None
        '''
        return str(this.waveform)

    def create_waveforms(this):
        ''' 
        Create a number of waveforms with random baseline and a single pulse.
        @params: all parameters initialized in *__init__*
        @return: ndarray with waveforms in a dictionary
        ''' 
        waveforms  = np.ndarray([], dtype="object")
        if isinstance(this.amplitude, list): 
            amplitudes = this.__generate_amplitudes()
            positions  = this.__generate_jitter()
            for amplitude, position in zip(amplitudes, positions):
                this.amplitude = amplitude 
                this.position  = position
                this.__generate_pulse()
                this.__generate_baseline()
                this.__generate_waveform()
                waveforms = np.append(waveforms, [this.waveform])
            this.waveform = waveforms
            return this.waveform
        else: 
            for i in range(0, this.number_of_waveforms):
                this.__generate_pulse()
                this.__generate_baseline()
                this.__generate_waveform()
                waveforms = np.append(waveforms, [this.waveform])
            this.waveform = waveforms
            return this.waveform
    
    def __generate_amplitudes(this):
        ''' 
        Create an array of random integers inside amplitude range.
        @params: min and max amplitude, number of waveforms.
        @return: array with random numbers for amplitudes
        '''
        return np.random.randint(this.amplitude[0], this.amplitude[1], size = this.number_of_waveforms)

    def __generate_jitter(this):
        ''' 
        Create an array of random integers around pulse position.
        @params: pulse position, jitter width and number of waveforms.
        @return: array with random numbers for pulse positions
        '''
        return np.random.randint(this.pulse_position-this.jitter_width//2, high=this.pulse_position+this.jitter_width//2, size = this.number_of_waveforms)

    def __generate_pulse(this):
        '''
        Create tail of pulse as an expontial decay.
        @params: initial amplitude _A_ and decay constant _B_
        @return: array of size 200 with signal's tail
        '''
        A = this.amplitude 
        B = this.B
        sample_number = np.arange(0, 200)
        sample_value  = A*np.exp(B*sample_number)
        print(max(sample_value))
        mask = np.where(sample_value>0.)
        this.pulse = {"number":sample_number[mask], "value":sample_value[mask]}

    def __generate_baseline(this):
        '''
        Generate with random numbers as electronic-noise baseline.
        @params: baseline offset and noise amplitude
        @return: array with random numbers
        '''
        waveform_size = this.waveform_size
        sample_number = np.arange(0, waveform_size, 1)
        sample_value = np.random.randint(this.baseline_offset-this.noise_amplitude, high=this.baseline_offset+this.noise_amplitude, size=waveform_size)
        this.baseline = {"number":sample_number, "value":sample_value}

    def __generate_waveform(this):
        '''
        Combine pulse and baseline into a waveform.
        @params: size, pulse and baseline
        @return: dictionary with sample number and value
        '''
        pulse = this.pulse
        baseline = this.baseline
        pulse_position = this.pulse_position
        waveform = baseline["value"]
        imax = len(pulse["number"])
        # print("in function: ", max(pulse["value"]))
        if imax > imax + len(baseline["value"]): imax = len(baseline["value"])
        for i_pulse in range(0, imax):
            i_waveform = pulse_position + i_pulse
            if (i_waveform >= pulse_position):
                waveform[i_waveform] = waveform[i_waveform] + pulse["value"][i_pulse]
            else:
                waveform[i_waveform] = baseline["value"][i_waveform]
        this.waveform = {"number":np.arange(0,len(baseline["value"])), "value":waveform}