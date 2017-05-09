# another_rnn_phone_classifier
Yet another reboot of the phone classifier for kids' language learning game.


## Dependencies

* SPTK
* Tensor Flow 0.10.?

Easiest in anaconda. My conda env is called tensorflow3 and I activate it with command '''source activate tensorflow3'''. 

Just sayin'.

```
+--------------------------------------------------------+
|        Preprocess labels and generate recipes          |
|        (for example see preprocess_kaldi_labels        |
+--------------------------+-----------------------------+
                           |
                           |
+--------------------------+-----------------------------+
|                                                        |
|   Feature extraction wrapper:                          |
|   feature_extraction_speeconkids_alldata.py            |
|                                                        |
|     +--------------------------------------------------+-+
|     |  Feature extraction script:                        |
|     |  dnnutil/preprocessing.py                          |
|     |                                                    |
|     |  +---------------------------------------------+   |
|     |  |  Normalise levels and add noise:            |   |
|     |  |  preprocess_speecon_and_add_babble.sh       |   |
|     |  +---------------------+-----------------------+   |
|     |                        |                           |
|     |  +---------------------+-----------------------+   |
|     |  |  FFT and Mel-binning:                       |   |
|     |  |  extract_8000hz_melbin26_with_start_end.sh  |   |
|     |  +---------------------+-----------------------+   |
|     |                        |                           |
|     |  +---------------------+-----------------------+   |
|     |  |  Segmentation                               |   |
|     |  +---------------------+-----------------------+   |
|     |                        |                           |
|     |  +---------------------+-----------------------+   |
|     |  |  Pickling                                   |   |
|     |  +---------------------------------------------+   |
|     |                                                    |
|     +--------------------------------------------------+-+
|                                                        |
+---------------------------+----------------------------+
                            |
                            |
+---------------------------+----------------------------+
|                                                        |
|   Classifier training:                                 |
|   rnn_training_37melbin_4x1000_test-2.py               |
|                                                        |
|     +---------------------------------------------+    |
|     |  Load pickles                               |    |
|     +---------------------+-----------------------+    |
|                           |                            |
|     +---------------------+-----------------------+    |
|     |  Z-Normalise training and test data         |    |
|     +---------------------+-----------------------+    |
|                           |                            |
|     +---------------------+-----------------------+    |
|     |  Initialise DNN network                     |    |
|     +---------------------+-----------------------+    |
|                           |                            |
|     +---------------------+-----------------------+    |
|     |  Update parameters for 40000 batches        |    |
|     +---------------------+-----------------------+    |
|                           |                            |
|     +---------------------+-----------------------+    |
|     |  Compute devel scores and save model        |    |
|     |  parameters every 2000 batches              |    |
|     +---------------------------------------------+    |
|                                                        |
+---------------------------+----------------------------+
                            |
                            |
+---------------------------+----------------------------+
|                                                        |
|   Classifier testing:                                  |
|   test_rnn4x1000.py                                    |
|                                                        |
|     +---------------------------------------------+    |
|     |  Load test data pickles                     |    |
|     +---------------------+-----------------------+    |
|                           |                            |
|     +---------------------+-----------------------+    |
|     |  Z-Normalise with training data statistics  |    |
|     +---------------------+-----------------------+    |
|                           |                            |
|     +---------------------+-----------------------+    |
|     |  Evaluate batch by batch and save results   |    |
|     +---------------------------------------------+    |
|                                                        |
+---------------------------+----------------------------+
                            |
                            |
+---------------------------+----------------------------+
|   Compute scoring matrices:                            |
|   scoring_system_with_matrix.py                        |
|     +---------------------------------------------+    |
|     |  Load test results                          |    |
|     +---------------------+-----------------------+    |
|                           |                            |
|     +---------------------+-----------------------+    |
|     |  Compute least squares fit for phonetic     |    |
|     |  confusion matrices to scoring              |    |
|     +---------------------+-----------------------+    |
+---------------------------+----------------------------+
                            |
                            |
+---------------------------+----------------------------+
|   Set up scoring service in TCP port                   |
|   serving/serve.sh                                     |
+--------------------------------------------------------+
```
