#!/usr/bin/python3
# coding: utf-8

#import matplotlib.pyplot as plt
import numpy as np
import pickle
import os
import re
#from scipy.optimize import lsq_linear
#from scipy.optimize import least_squares
from scipy import optimize

classdict = {"_1_" : u"n",
             "_2_" : u"t",
             "_3_" : u"ɪ",
             "_4_" : u"s",
             "_5_" : u"ə",
             "_6_" : u"r",
             "_7_" : u"l",
             "_8_" : u"k",
             "_9_" : u"z",
             "_10_" : u"aɪ",
             "_11_" : u"f",
             "_12_" : u"iː",
             "_13_" : u"ɑː",
             "_14_" : u"d",
             "_15_" : u"ɛ",
             "_16_" : u"v",
             "_17_" : u"m",
             "_18_" : u"b",
             "_19_" : u"ɔː",
             "_20_" : u"ð",
             "_21_" : u"eɪ",
             "_22_" : u"p",
             "_23_" : u"æ",
             "_24_" : u"w",
             "_25_" : u"oʊ",
             "_26_" : u"uː",
             "_27_" : u"ɡ",
             "_28_" : u"ɒ",
             "_29_" : u"j",
             "_30_" : u"θ",
             "_31_" : u"ɪər",
             "_32_" : u"h",
             "_33_" : u"ŋ",
             "_34_" : u"ʌ",
             "_35_" : u"dʒ",
             "_36_" : u"tʃ",
             "_37_" : u"ʃ",
             "_38_" : u"aʊ",
             "_39_" : u"ɜː",
             "_40_" : u"ɛər",
             "_41_" : u"ʊ",
             "_42_" : u"oɪ",
             "_43_" : u"ʒ",
             "_44_" : u"ɔːr",
             "_45_" : u"sil" ,
             "_46_" : u'_a' ,
             "_47_" : u'_ä' ,
             "_48_" : u'_aa' ,
             "_49_" : u'_ää' ,
              "_50_" : u'_ae' ,
              "_51_" : u'_äe' ,
              "_52_" : u'_ai' ,
              "_53_" : u'_äi' ,
              "_54_" : u'_ao' ,
              "_55_" : u'_au' ,
              "_56_" : u'_äy' ,
              "_57_" : u'_b' ,
              "_58_" : u'_d' ,
              "_59_" : u'_e' ,
              "_60_" : u'_ea' ,
              "_61_" : u'_eä' ,
              "_62_" : u'_ee' ,
              "_63_" : u'_ei' ,
              "_64_" : u'_eo' ,
              "_65_" : u'_eu' ,
              "_66_" : u'_ey' ,
              "_67_" : u'_f' ,
              "_68_" : u'_g' ,
              "_69_" : u'_h' ,
              "_70_" : u'_hh' ,
              "_71_" : u'_i' ,
              "_72_" : u'_ia' ,
              "_73_" : u'_iä' ,
              "_74_" : u'_ie' ,
              "_75_" : u'_ii' ,
              "_76_" : u'_io' ,
              "_77_" : u'_iu' ,
              "_78_" : u'_j' ,
              "_79_" : u'_k' ,
              "_80_" : u'_kk' ,
              "_81_" : u'_l' ,
              "_82_" : u'_ll' ,
              "_83_" : u'_m' ,
              "_84_" : u'_mm' ,
              "_85_" : u'_n' ,
              "_86_" : u'_ng' ,
              "_87_" : u'_ngng' ,
              "_88_" : u'_nn' ,
              "_89_" : u'_o' ,
              "_90_" : u'_ö' ,
              "_91_" : u'_oa' ,
              "_92_" : u'_oe' ,
              "_93_" : u'_oi' ,
              "_94_" : u'_öi' ,
              "_95_" : u'_oo' ,
              "_96_" : u'_öö' ,
              "_97_" : u'_ou' ,
              "_98_" : u'_öy' ,
              "_99_" : u'_p' ,
              "_100_" : u'_pp' ,
              "_101_" : u'_r' ,
              "_102_" : u'_rr' ,
              "_103_" : u'_s' ,
              "_104_" : u'_ss' ,
              "_105_" : u'_t' ,
              "_106_" : u'_tt' ,
              "_107_" : u'_u' ,
              "_108_" : u'_ua' ,
              "_109_" : u'_ue' ,
              "_110_" : u'_ui' ,
              "_111_" : u'_uo' ,
              "_112_" : u'_uu' ,
              "_113_" : u'_v' ,
              "_114_" : u'_y' ,
              "_115_" : u'_yä' ,
              "_116_" : u'_yi' ,
              "_117_" : u'_yö' ,
              "_118_" : u'_yy' }

phonedict = {}
for key in classdict.keys():
    phonedict[ classdict[key] ] = int(key.replace('_',''))


#print(phonedict)

class_def = {
"sil" : {"count" : 6611, "probability" :0.04628649220995, "sqrt_probability" :0.2151429576118, "class" :45},
"P" : {"count" : 306, "probability" :1, "sqrt_probability" :1, "class" :44},
"Z" : {"count" : 311, "probability" :0.98392282958199, "sqrt_probability" :0.99192884300336, "class" :43},
"Å" : {"count" : 344, "probability" :0.88953488372093, "sqrt_probability" :0.94315156985552, "class" :42},
"U" : {"count" : 497, "probability" :0.61569416498994, "sqrt_probability" :0.78466181568236, "class" :41},
"W" : {"count" : 501, "probability" :0.61077844311377, "sqrt_probability" :0.78152315583978, "class" :40},
"ö" : {"count" : 573, "probability" :0.53403141361257, "sqrt_probability" :0.73077452994242, "class" :39},
"å" : {"count" : 601, "probability" :0.50915141430948, "sqrt_probability" :0.71354846668568, "class" :38},
"S" : {"count" : 641, "probability" :0.47737909516381, "sqrt_probability" :0.69092625884663, "class" :37},
"C" : {"count" : 746, "probability" :0.41018766756032, "sqrt_probability" :0.64045895072231, "class" :36},
"J" : {"count" : 757, "probability" :0.40422721268164, "sqrt_probability" :0.63578865409949, "class" :35},
"A" : {"count" : 958, "probability" :0.31941544885177, "sqrt_probability" :0.56516851367692, "class" :34},
"N" : {"count" : 958, "probability" :0.31941544885177, "sqrt_probability" :0.56516851367692, "class" :33},
"H" : {"count" : 963, "probability" :0.31775700934579, "sqrt_probability" :0.56369939626169, "class" :32},
"R" : {"count" : 1050, "probability" :0.29142857142857, "sqrt_probability" :0.53984124650546, "class" :31},
"T" : {"count" : 1057, "probability" :0.28949858088931, "sqrt_probability" :0.53805072334243, "class" :30},
"j" : {"count" : 1132, "probability" :0.27031802120141, "sqrt_probability" :0.5199211682567, "class" :29},
"Y" : {"count" : 1354, "probability" :0.22599704579025, "sqrt_probability" :0.47539146583658, "class" :28},
"g" : {"count" : 1420, "probability" :0.21549295774648, "sqrt_probability" :0.46421219043287, "class" :27},
"u" : {"count" : 1621, "probability" :0.18877236273905, "sqrt_probability" :0.4344794157829, "class" :26},
"o" : {"count" : 1648, "probability" :0.18567961165049, "sqrt_probability" :0.4309055716169, "class" :25},
"w" : {"count" : 1675, "probability" :0.18268656716418, "sqrt_probability" :0.42741849183696, "class" :24},
"ä" : {"count" : 1742, "probability" :0.17566016073479, "sqrt_probability" :0.41911831352828, "class" :23},
"p" : {"count" : 1773, "probability" :0.17258883248731, "sqrt_probability" :0.41543812112914, "class" :22},
"E" : {"count" : 1807, "probability" :0.16934144991699, "sqrt_probability" :0.41151117836213, "class" :21},
"D" : {"count" : 1819, "probability" :0.16822429906542, "sqrt_probability" :0.4101515562148, "class" :20},
"O" : {"count" : 1843, "probability" :0.16603364080304, "sqrt_probability" :0.4074722577097, "class" :19},
"b" : {"count" : 2129, "probability" :0.14372945044622, "sqrt_probability" :0.379116671285, "class" :18},
"m" : {"count" : 2177, "probability" :0.140560404226, "sqrt_probability" :0.37491386240842, "class" :17},
"v" : {"count" : 2227, "probability" :0.13740458015267, "sqrt_probability" :0.37068123792913, "class" :16},
"e" : {"count" : 2298, "probability" :0.1331592689295, "sqrt_probability" :0.36490994632855, "class" :15},
"d" : {"count" : 2410, "probability" :0.12697095435685, "sqrt_probability" :0.35632983927374, "class" :14},
"a" : {"count" : 2582, "probability" :0.11851278079009, "sqrt_probability" :0.34425685293119, "class" :13},
"I" : {"count" : 2608, "probability" :0.11733128834356, "sqrt_probability" :0.3425365503761, "class" :12},
"f" : {"count" : 2690, "probability" :0.11375464684015, "sqrt_probability" :0.33727532794462, "class" :11},
"Ä" : {"count" : 2795, "probability" :0.10948121645796, "sqrt_probability" :0.33087945910552, "class" :10},
"z" : {"count" : 3066, "probability" :0.09980430528376, "sqrt_probability" :0.31591819397394, "class" :9},
"k" : {"count" : 3292, "probability" :0.09295261239368, "sqrt_probability" :0.30488130869845, "class" :8},
"l" : {"count" : 3619, "probability" :0.08455374412821, "sqrt_probability" :0.2907812650915, "class" :7},
"r" : {"count" : 3630, "probability" :0.08429752066116, "sqrt_probability" :0.29034035313948, "class" :6},
"Q" : {"count" : 4684, "probability" :0.06532877882152, "sqrt_probability" :0.25559495069645, "class" :5},
"s" : {"count" : 4867, "probability" :0.06287240599959, "sqrt_probability" :0.25074370580254, "class" :4},
"i" : {"count" : 5140, "probability" :0.05953307392996, "sqrt_probability" :0.24399400388116, "class" :3},
"t" : {"count" : 5996, "probability" :0.05103402268179, "sqrt_probability" :0.22590711073755, "class" :2},
"n" : {"count" : 6811, "probability" :0.04492732344736, "sqrt_probability" :0.21196066485875, "class" :1},
}



#LOG_DIR='/tmp/tensorflow_logs/copy12-rnn384-d/'
LOG_DIR='../models/bidir_lstm_6x384_checkpoint_16000/'
checkpoint=16000

prediction_files={ 'native' : LOG_DIR + "players_native_y_and_prediction."+str(checkpoint),
                  'good': LOG_DIR + "players_good_y_and_prediction."+str(checkpoint),
                  'ok': LOG_DIR + "players_ok_y_and_prediction."+str(checkpoint),
                  'bad': LOG_DIR + "players_bad_y_and_prediction."+str(checkpoint) }


test_corpus = "fysiak-gamedata-2"
test_pickle_dir='../features/work_in_progress/'+test_corpus+'/pickles'

phone_pickles = { 'bad' : os.path.join(test_pickle_dir, 'disqualified-32smoothed_mspec66_and_f0_alldata.pickle2'),
                  'ok' : os.path.join(test_pickle_dir, 'some_stars-32smoothed_mspec66_and_f0_alldata.pickle2'),
                  'good' : os.path.join(test_pickle_dir, 'lots_of_stars-32smoothed_mspec66_and_f0_alldata.pickle2'),
                  'native' : os.path.join(test_pickle_dir, 'native_or_nativelike-32smoothed_mspec66_and_f0_alldata.pickle2') }

points_per_phone = { 'bad' : -2,
                     'ok' : 2,
                     'good' : 5,
                     'native' : 5 }

prediction_array = []
classes_array = []


numranks=7


ranking_array = np.zeros([2200, 45,120])
score_array = np.zeros([2200])

starts={}
stops={}

uttcounter = 0



for category in ['native', 'good', 'ok', 'bad' ]:
    
    starts[category]=uttcounter

    #class_and_post=np.loadtxt(posterior_files[category])
    #classes = class_and_post[:,0]
    #posteriors = class_and_post[:,1:]
    #posteriors = posteriors - np.min(posteriors, axis=1).reshape([-1,1])
    #posteriors = posteriors / np.sum(posteriors, axis=1).reshape([-1,1])


    class_and_pred=np.loadtxt(prediction_files[category])
    classes = class_and_pred[:,0]
    predictions = class_and_pred[:,1]

    prediction_array.append(predictions)
    classes_array.append(classes)
     
    data_and_classes = pickle.load( open(phone_pickles[category], 'rb'))
    details=data_and_classes['details']
    currentsourcefile = ''

    rowcounter = 0
    
    ranking_matrix = np.zeros([45,120])
    score_line = 0

    for line in details:
        [phone, something, value1, value2, value3, sourcefile] = line.split(' ')
        if currentsourcefile != sourcefile:                            
            #print (sourcefile)
            if (np.sum(np.abs(ranking_matrix)))>0:                
                ranking_array[uttcounter,:,:] = ranking_matrix/np.sum(ranking_matrix.reshape([-1]))
                score_array[uttcounter] =  points_per_phone[category] #score_line

            #print (ranking_matrix)
            #print (score_line)

            ranking_matrix = np.zeros([45,120])
            score_line = 0

            uttcounter += 1

            currentsourcefile = sourcefile

        if phone != "sil":
            [pre, phone, post] = re.split('\-|\+', phone)
            cl = class_def[phone]['class']
            phonebase = cl * numranks

            #row=posteriors[rowcounter,:]            
            guess = predictions[rowcounter]

            #print("%i\t%s\t%s\t%s" % ( rowcounter, phone,   classdict["_%i_" % classes[rowcounter] ], classdict["_%i_" % (guess)] ) )

            ranking_matrix[ cl, guess ] += 1
            
                
        rowcounter+=1
    #print(np.sum(ranking_array[0:40,:], axis=1))
    #print(score_array[0:40])
    stops[category]=uttcounter-1


print("Row: %i"%uttcounter)

ranking_array = ranking_array[:uttcounter,:].reshape([-1, 120*45])
score_array = score_array[:uttcounter].reshape([-1,1])

print(score_array.shape)

bounds=np.zeros([45*120, 2])
bounds[:,1] = 5

#weights = lsq_linear(ranking_array, score_array, bounds=bounds)

def my_costfunc(x):
    return np.sum(
                   np.power(
                       #np.matmul( ranking_array, x.reshape([120,120])) - score_array.T
                       #(ranking_array * x.reshape([45,120]).sum(-1).sum(-1) - score_array.T
                       (ranking_array * x).sum(-1) - score_array.T
                        ,2 ))
    

all_samples = np.mod(np.arange(uttcounter), 10)
lsq_weight_array=np.zeros([10,45*120])

all_scores=[]


for testround in range(10):
    
    train_samples = np.where(all_samples != testround)[0]
    test_samples = np.where(all_samples == testround)[0]

    leave_one_out_ranking_array = ranking_array[train_samples,:]
    leave_one_out_score_array = score_array[train_samples]

    def my_least_squares_costfunc(x):
        #return ((ranking_array * x.reshape([45,120])).sum(-1).sum(-1) - score_array.T).reshape([-1])
        #return ((ranking_array * x).sum(-1) - score_array.T).reshape([-1])
        sum= np.abs((leave_one_out_ranking_array * x).sum(-1) - leave_one_out_score_array.T).reshape([-1])
        sum -= 1
        sum[sum<0] = 0
        return sum


    #weights = least_squares(ranking_array, score_array, bounds=bounds)


    if os.path.isfile(os.path.join( LOG_DIR, 
                                    'lsq_weights_%i'%testround)):
        lsq_weight_array[testround,:] = np.loadtxt(os.path.join( LOG_DIR, 
                                                                 'lsq_weights_%i'%testround)).reshape([-1])

    else:
        initguess = 0.01*np.random.rand(45,120)

        #print("initguess cost:")
        #print(my_costfunc(initguess))


        for i in range(45):        
            #print("setting %i to random" % (i*numranks) )
            initguess[ i, i ] = 5

        initguess=initguess.reshape([-1])

        #print("initguess least_sq_cost.shape:")
        #print(my_least_squares_costfunc(initguess).shape)

        lsq_bounds=[-1.99,9.99]

        endcondition=0.01
        #lsq_weights={'x':initguess}

        lsq_weights = optimize.least_squares(my_least_squares_costfunc, initguess, bounds=lsq_bounds, verbose=2, ftol=endcondition, xtol=endcondition)



        #print(lsq_weights)

        outf = open('/tmp/lsq_output_%i'%testround, 'wb')
        # Pickle the list using the highest protocol available.
        pickle.dump( lsq_weights , outf, protocol=pickle.HIGHEST_PROTOCOL)

        np.savetxt( os.path.join( LOG_DIR, 
                                  'lsq_weights_%i'%testround), lsq_weights['x'].reshape([45,120]))

        lsq_weight_array[testround,:] = lsq_weights['x']

    test_ranking_array = ranking_array[test_samples,:]
    test_score_array = score_array[test_samples]
    
    scores={}

    for category in ['good', 'ok', 'bad' ]:        
        target_score =  points_per_phone[category]        
        sub_test_samples = np.where(test_score_array == target_score)[0]        
        scores[category]= (lsq_weight_array[testround,:] * test_ranking_array[sub_test_samples,:]).sum(-1)
        
        print("round %i samples: %s\tmean: %0.2f\tstd: %0.2f" % (testround,
                                                                 category,
                                                                 np.mean(scores[category]),
                                                                 np.std(scores[category])))

    print ("------------")
    all_scores.append(scores)
    
if os.path.isfile(os.path.join(LOG_DIR, "lsq_weights")):
    mean_lsq_weights = np.loadtxt(os.path.join(LOG_DIR, "lsq_weights"))
else:
    mean_lsq_weights = np.mean(lsq_weight_array, axis=0)
    np.savetxt(os.path.join(LOG_DIR, "lsq_weights"), mean_lsq_weights)

scores={}
for category in ['good', 'ok', 'bad' ]:        
    

    target_score =  points_per_phone[category]        
    test_samples = np.where(score_array == target_score)[0]      

    test_ranking_array = ranking_array[test_samples]
    
    scores[category]= (mean_lsq_weights * test_ranking_array).sum(-1)
    
    print("            All: %s\tmean: %0.2f\tstd: %0.2f" % (
                                                             category,
                                                             np.mean(scores[category]),
                                                             np.std(scores[category])))
    
    
all_scores.append(scores)
