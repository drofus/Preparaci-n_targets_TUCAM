

def dummy():

    target_esq = """<?xml version="1.0" encoding="UTF-8"?>
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
    <Exposure>tiempo_exp</Exposure>
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
    <Filter>filtro</Filter>
    <Type>Light</Type>
    <Prefix>
    <RawPrefix>Target_name</RawPrefix>
    <FilterEnabled>1</FilterEnabled>
    <ExpEnabled>1</ExpEnabled>
    <TimeStampEnabled>0</TimeStampEnabled>
    </Prefix>
    <Count>cantidad_imagenes</Count>
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
    </Job>
    </SequenceQueue>
    """

    flats_esq = """<?xml version="1.0" encoding="UTF-8"?>
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
    <Exposure>tiempo_exp</Exposure>
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
    <Filter>filtro</Filter>
    <Type>Flat</Type>
    <Prefix>
    <RawPrefix></RawPrefix>
    <FilterEnabled>0</FilterEnabled>
    <ExpEnabled>1</ExpEnabled>
    <TimeStampEnabled>0</TimeStampEnabled>
    </Prefix>
    <Count>5</Count>
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
    </Job>
    </SequenceQueue>
    """

    darks_esq = """<?xml version="1.0" encoding="UTF-8"?>
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
    <Exposure>tiempo_exp</Exposure>
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
    <Type>Dark</Type>
    <Prefix>
    <RawPrefix></RawPrefix>
    <FilterEnabled>0</FilterEnabled>
    <ExpEnabled>1</ExpEnabled>
    <TimeStampEnabled>0</TimeStampEnabled>
    </Prefix>
    <Count>5</Count>
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
    </Job>
    </SequenceQueue>
    """

    #creación de un archivo Dummy de targets
    with open(r'Target_dummy.esq', 'w') as file: 
        file.write(target_esq) 

    #creación de un archivo Dummy de Flat
    with open(r'Flat_dummy.esq', 'w') as file: 
        file.write(flats_esq)

    #creación de un archivo Dummy de Dark
    with open(r'Dark_dummy.esq', 'w') as file:
        file.write(darks_esq)