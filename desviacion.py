import statistics

def Burbuja():
    data = {
        "100":{
            "python":[0.0010008811950683594, 0.0010020732879638672, 0.0010271072387695312, 0.0, 0.0],
            "go": [0.00000000,0.00000000,0.00000000,0.00000000,0.00000000],
            "c++":[0,0,0,0,0]
        },
        "1000":{
            "python":[0.037178993225097656,0.036226749420166016,0.03662562370300293,0.0373682975769043,0.038233280181884766],
            "go": [0.00102880,0.00052130,0.00057700,0.00070460,0.00051530],
            "c++":[0.004, 0.007, 0.002, 0.003, 0.002]
        },
        "2000":{
            "python":[
                0.1538560390472412,
                0.15029239654541016,
                0.1523423194885254,0.1520230770111084,
                0.15146136283874512,
                0.1506340503692627],
            "go": [0.00204330,0.00203110,0.00233800,0.00211940,0.00219080,0.00218980],
            "c++":[0.018,0.009,0.009,0.019,0.008]
        },
        "3000":{
            "python":[0.34778785705566406,0.34961891174316406,0.35141801834106445,0.3505208492279053,0.3498845100402832],
            "go": [0.00537580,0.00497970,0.00536170,0.00545980,0.00543340],
            "c++":[0.021,0.038, 0.029, 0.022, 0.021]
        },
        "4000":{
            "python":[0.621971845626831,0.6218409538269043,0.6201591491699219,0.628286600112915,0.6271505355834961],
            "go": [0.00987680,0.00987290,0.00975550,0.00992860,0.01037360],
            "c++":[0.040,0.042,0.050,0.040,0.041]
        },
        "5000":{
            "python":[0.9839315414428711,0.9931068420410156,0.9747231006622314,0.9844639301300049,0.9850730895996094],
            "go": [0.01693110,0.01688450,0.01794880,0.01711600,0.01685490,0.01711960],
            "c++":[0.069,0.073,0.067,0.070,0.065]
        },
        "6000":{
            "python":[1.4234092235565186,1.4021174907684326,1.4301645755767822,1.4243261814117432,1.412588357925415],
            "go": [0.02475810,0.02559820,0.02730380,0.02541390,0.02548190,0.02490020],
            "c++":[0.095,0.0116,0.098,0.0103,0.0100]
        },
        "7000":{
            "python":[1.9419589042663574,1.9417517185211182,1.9583630561828613,1.9828827381134033,1.928908348083496],
            "go": [0.03642260,0.03612240,0.03663100,0.03747850,0.03747230,0.03725890],
            "c++":[0.0162,0.0147,0.0138,0.0145,0.0136]
        },
        "8000":{
            "python":[2.5540218353271484,2.540436267852783,2.529750347137451,2.540461301803589,2.6394948959350586],
            "go": [0.05054890,0.05005430,0.04997630,0.04945820,0.05008710],
            "c++":[0.0194,0.0189,0.0191,0.0175,0.0183]
        },
        "9000":{
            "python":[3.248283863067627,3.2027547359466553,3.255760669708252,3.23628830909729,3.21126127243042],
            "go": [0.06705440,0.06580350,0.06682920,0.06614340,0.06613560],
            "c++":[0.0238,0.0239,0.0248,0.0235,0.0230]
        },
        "10000":{
            "python":[4.034560918807983,4.07691216468811,4.0297136306762695,4.0210301876068115,4.021560907363892],
            "go": [0.08800090,0.08642440,0.08571630,0.08577340,0.08745870],
            "c++":[0.0313,0.0319,0.0326,0.0343,0.0310]
        },
        "20000":{
            "python":[16.485239028930664,16.84360909461975,16.668872117996216,16.965672731399536,16.93165349960327],
            "go": [0.40473670,0.40217700,0.40243930,0.40124730,0.40505270],
            "c++":[1.356,1.347,1.353,1.336,1.354]
        },
        "30000":{
            "python":[39.16671323776245,38.81782627105713,38.952004194259644,38.803635358810425,38.819942474365234],
            "go": [0.95203200,0.95418960,0.94948280,0.95452160,0.94961770],
            "c++":[2.888,2.842,2.808,2.786,2.797]
        },
        "40000":{
            "python":[69.65759587287903,71.0185022354126,70.74218225479126,70.09642457962036,70.18778610229492],
            "go": [1.74900400,1.74403420,1.74984090,1.74631490,1.75002140],
            "c++":[4.853,4.787,4.782,4.757,4.766]
        },
        "50000":{
            "python":[113.15143203735352,115.35443115234375,113.47874712944031,114.17569375038147,114.82878184318542],
            "go": [2.76123520,2.76114680,2.75986180,2.76253060,2.76137000],
            "c++":[7.476,7.384,7.433,7.421,7.399]
        }
    }
    for key in data:
        print('============')
        print('CANTIDAD:',key)
        for key2 in data[key]:
            print('Lenguaje:',key2)
            # Calcula la media
            mean = statistics.mean(data[key][key2])

            # Calcula la desviación estándar para una muestra
            std_deviation = statistics.stdev(data[key][key2])
            print(">>Media:", mean)
            print(">>Desviación estándar:", std_deviation)
            print("")
    

def MS():
    data = {
        "100":{
            "python":[0.001583099365234375,0.0,0.0,0.0,0.0010008811950683594],
            "go": [0.00000000,0.00000000,0.00000000,0.00051540,0.00051180],
            "c++":[0.0,0.0,0.0,0.0,0.0]
        },
        "1000":{
            "python":[0.0025725364685058594,0.0009748935699462891,0.0010294914245605469,0.0019762516021728516,0.001999378204345703],
            "go": [0.00000000,0.00000000,0.00000000,0.00000000,0.00054790],
            "c++":[0.0,0.0,0.0,0.0,0.0]
        },
        "2000":{
            "python":[0.003975868225097656,0.002143383026123047,0.0020079612731933594,0.0035066604614257812,0.003540515899658203],
            "go": [0.00000000,0.00000000,0.00000000,0.00050910,0.00053970],
            "c++":[0.001,0.003,0.00,0.00,0.00]
        },
        "3000":{
            "python":[0.00554347038269043,0.004595041275024414,0.004567384719848633,0.004034996032714844,0.004010200500488281],
            "go": [0.00000000,0.00000000,0.00000000,0.00051040,0.00054180],
            "c++":[0.001,0.001,0.001,0.001,0.001]
        },
        "4000":{
            "python":[0.0060002803802490234,0.007539272308349609,0.006922483444213867,0.005998134613037109,0.006025552749633789],
            "go": [0.00054100, 0.00046490, 0.00055860, 0.00050300, 0.00083770],
            "c++":[0.001,0.001,0.001,0.001,0.001]
        },
        "5000":{
            "python":[0.00803828239440918,0.008109331130981445,0.008570432662963867,0.009430408477783203,0.008509397506713867],
            "go": [0.00103940,0.00051170,0.00051690,0.00054350,0.00051340],
            "c++":[0.002,0.002,0.002,0.002,0.004]
        },
        "6000":{
            "python":[0.01210474967956543,0.011113166809082031,0.01054072380065918,0.010578393936157227,0.011240243911743164],
            "go": [0.00109040,0.00054330,0.00050430,0.00051640,0.00061230],
            "c++":[0.002,0.002,0.002,0.002,0.002]
        },
        "7000":{
            "python":[0.012325525283813477,0.012407779693603516,0.012600421905517578,0.013087987899780273,0.01257944107055664],
            "go": [0.00068900,0.00104860,0.00051940,0.00110970, 0.00102960],
            "c++":[0.003,0.003,0.003,0.006,0.003]
        },
        "8000":{
            "python":[0.015105962753295898,0.014763593673706055,0.01370692253112793,0.014080524444580078,0.014476776123046875],
            "go": [0.00107270,0.00102930,0.00105790,0.00052000,0.00111830],
            "c++":[0.003,0.003,0.003,0.004,0.003]
        },
        "9000":{
            "python":[0.016645431518554688,0.015980243682861328,0.017123699188232422,0.016512632369995117,0.017170190811157227],
            "go": [0.00094670,0.00103120,0.00103130,0.00105770,0.00108630],
            "c++":[0.004,0.004,0.004,0.004,0.004]
        },
        "10000":{
            "python":[0.019063711166381836,0.018088579177856445,0.019162416458129883,0.018083810806274414,0.01976490020751953],
            "go": [0.00124560,0.00105520,0.00106170,0.00113570,0.00114100],
            "c++":[0.004,0.004,0.004,0.005,0.004]
        },
        "20000":{
            "python":[0.04131889343261719,0.041648149490356445,0.04291868209838867,0.04225516319274902,0.04076194763183594],
            "go": [0.00270880,0.00269290,0.00204780,0.00213680,0.00259210],
            "c++":[0.009,0.009,0.009,0.015,0.009]
        },
        "30000":{
            "python":[0.06381916999816895,0.06476330757141113, 0.06329560279846191, 0.06561994552612305, 0.06386256217956543],
            "go": [0.00445660,0.00483050,0.00490650,0.00497270,0.00531180],
            "c++":[0.014,0.014,0.014,0.014,0.014]
        },
        "40000":{
            "python":[0.08920502662658691,0.08906912803649902,0.08745503425598145,0.08753323554992676,0.08848190307617188],
            "go": [0.00612290,0.00615520,0.00607240,0.00633690,0.00598900],
            "c++":[0.019,0.019,0.028,0.019,0.019]
        },
        "50000":{
            "python":[0.11091208457946777,0.11256170272827148,0.11292552947998047,0.1183016300201416,0.11500239372253418],
            "go": [0.00707870,0.00723410,0.00644080,0.00681530,0.00653180],
            "c++":[0.025,0.024,0.024,0.024,0.024]
        }
    }
    for key in data:
        print('============')
        print('CANTIDAD:',key)
        for key2 in data[key]:
            print('Lenguaje:',key2)
            # Calcula la media
            mean = statistics.mean(data[key][key2])

            # Calcula la desviación estándar para una muestra
            std_deviation = statistics.stdev(data[key][key2])
            print(">>Media:", mean)
            print(">>Desviación estándar:", std_deviation)
            print("")



Burbuja()