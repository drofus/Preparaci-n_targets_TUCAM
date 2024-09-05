import os

def dummy_bias():
    bias_esq = """<?xml version="1.0" encoding="UTF-8"?>
<SequenceQueue version='2.3'>
<CCD>FLI CCD</CCD>
<FilterWheel>FLI CFW</FilterWheel>
<GuideDeviation enabled='false'>2</GuideDeviation>
<GuideStartDeviation enabled='false'>2</GuideStartDeviation>
<Autofocus enabled='false'>0</Autofocus>
<RefocusOnTemperatureDelta enabled='false'>1</RefocusOnTemperatureDelta>
<RefocusEveryN enabled='false'>60</RefocusEveryN>
<RefocusOnMeridianFlip enabled='false'/>
<Job>
<Exposure>0</Exposure>
<Format></Format>
<Encoding></Encoding>
<Binning>
<X>1</X>
<Y>1</Y>
</Binning>
<Frame>
<X>0</X>
<Y>0</Y>
<W>3056</W>
<H>3056</H>
</Frame>
<Temperature force='false'>-25.00</Temperature>
<Filter>empty</Filter>
<Type>Bias</Type>
<Prefix>
<RawPrefix></RawPrefix>
<FilterEnabled>0</FilterEnabled>
<ExpEnabled>0</ExpEnabled>
<TimeStampEnabled>0</TimeStampEnabled>
</Prefix>
<Count>cantidad_exp</Count>
<Delay>0</Delay>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<UploadMode>0</UploadMode>
<Properties>
</Properties>
<Calibration>
<FlatSource>
<Type>Manual</Type>
</FlatSource>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
<PreMountPark>False</PreMountPark>
<PreDomePark>False</PreDomePark>
</Calibration>
</Job>"""
    #creación de un archivo Dummy de BIAS
    with open(r'Bias_dummy.esq', 'w') as file:
        file.write(bias_esq)

def Archivos_Bias(cantidad_name, cantidad_text):
    with open(r'Bias_dummy.esq', 'r') as file:
        
        #tiempo de exposición
        data_cantidad = file.read()
        data_cantidad = data_cantidad.replace(cantidad_name, cantidad_text)


    #Reemplazos de las palabras clave en los esq

    with open(r'Bias_dummy.esq', 'w') as file:
        file.write(data_cantidad)
