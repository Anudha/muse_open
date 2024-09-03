def get_properties(data):
  auto = sm.tsa.acf(y_crop, nlags=len(y_crop))
  peaks= find_peaks(auto)[0] # Find peaks of the autocorrelation. # if we choose next peak, do we get harmonics

  #use the first peak as the lag, this would give the highest frequency possible
  #lag = peaks[0]


  #use the lag of the most prominent peak to find the pitch
  prominences = peak_prominences(auto, peaks)[0] #input data here is auto, not the original sound signal  
  #print(type(prominences), prominences.shape)  # prominences is an ndarray  # shape is a tuple - 2 numbers, but only the first one has a value 
  ind = np.argmax(prominences)
  #print('checking', ind, len(peaks))
  lag=peaks[ind]



  pitch = sampling_frequency / lag # Transform lag into frequency. # lag = number of data points sampled (recorded) in one period of sound wave
  properties=[pitch, prominences.shape[0], prominences[ind]]  #frequency, number of peaks, prominence of the most prom peak
  #properties.extend(prominences.tolist()[:10])  # the most prominent peak, the number of peaks, prominence of the most prominent peak, # prominences of all peaks

  return properties
