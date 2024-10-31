##########################DUMMY###############################################################
Encabezado = """<?xml version="1.0" encoding="UTF-8"?>
<SequenceQueue version='2.6'>
<GuideDeviation enabled='false'>2</GuideDeviation>
<GuideStartDeviation enabled='false'>2</GuideStartDeviation>
<HFRCheck enabled='false'>
<HFRDeviation>0</HFRDeviation>
<HFRCheckAlgorithm>0</HFRCheckAlgorithm>
<HFRCheckThreshold>10</HFRCheckThreshold>
<HFRCheckFrames>1</HFRCheckFrames>
</HFRCheck>
<RefocusOnTemperatureDelta enabled='false'>1</RefocusOnTemperatureDelta>
<RefocusEveryN enabled='false'>60</RefocusEveryN>
<RefocusOnMeridianFlip enabled='false'/>"""

final = "</SequenceQueue>"

Target = """<Job>
<Exposure>Tiempo_aqui</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>Filtro_aqui</Filter>
<Type>Light</Type>
<Count>Repetir_aqui</Count>
<Delay>0</Delay>
<TargetName>nombre_aqui</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%t_%F_%E</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<ReomteDirectory>/home/tucan/data</ReomteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>"""

Bias = """<Job>
<Exposure>30</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>V</Filter>
<Type>Bias</Type>
<Count>Repetir_aqui</Count>
<Delay>0</Delay>
<TargetName>nombre_aqui</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>"""

Dark = """<Job>
<Exposure>Tiempo_aqui</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>Ha</Filter>
<Type>Dark</Type>
<Count>5</Count>
<Delay>0</Delay>
<TargetName>nombre_aqui</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F_%E</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>\n"""


domeflat = """<?xml version="1.0" encoding="UTF-8"?>
<SequenceQueue version='2.6'>
<GuideDeviation enabled='false'>2</GuideDeviation>
<GuideStartDeviation enabled='false'>2</GuideStartDeviation>
<HFRCheck enabled='false'>
<HFRDeviation>0</HFRDeviation>
<HFRCheckAlgorithm>0</HFRCheckAlgorithm>
<HFRCheckThreshold>10</HFRCheckThreshold>
<HFRCheckFrames>1</HFRCheckFrames>
</HFRCheck>
<RefocusOnTemperatureDelta enabled='false'>1</RefocusOnTemperatureDelta>
<RefocusEveryN enabled='false'>60</RefocusEveryN>
<RefocusOnMeridianFlip enabled='false'/>
<Job>
<Exposure>1</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>0</Temperature>
<Filter>empty</Filter>
<Type>Bias</Type>
<Count>20</Count>
<Delay>1</Delay>
<TargetName>domeflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>15</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>0</Temperature>
<Filter>empty</Filter>
<Type>Flat</Type>
<Count>1</Count>
<Delay>1</Delay>
<TargetName>domeflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>1</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>0</Temperature>
<Filter>empty</Filter>
<Type>Bias</Type>
<Count>2</Count>
<Delay>1</Delay>
<TargetName>domeflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>90</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>0</Temperature>
<Filter>B</Filter>
<Type>Flat</Type>
<Count>4</Count>
<Delay>1</Delay>
<TargetName>domeflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>40</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>0</Temperature>
<Filter>V</Filter>
<Type>Flat</Type>
<Count>4</Count>
<Delay>1</Delay>
<TargetName>domeflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>1</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>0</Temperature>
<Filter>empty</Filter>
<Type>Bias</Type>
<Count>2</Count>
<Delay>1</Delay>
<TargetName>domeflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>40</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>0</Temperature>
<Filter>R</Filter>
<Type>Flat</Type>
<Count>4</Count>
<Delay>1</Delay>
<TargetName>domeflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>600</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>0</Temperature>
<Filter>I</Filter>
<Type>Flat</Type>
<Count>4</Count>
<Delay>1</Delay>
<TargetName>domeflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>1</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>0</Temperature>
<Filter>empty</Filter>
<Type>Bias</Type>
<Count>2</Count>
<Delay>1</Delay>
<TargetName>domeflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>1200</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>0</Temperature>
<Filter>Ha</Filter>
<Type>Flat</Type>
<Count>4</Count>
<Delay>1</Delay>
<TargetName>domeflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>1500</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>0</Temperature>
<Filter>U</Filter>
<Type>Flat</Type>
<Count>4</Count>
<Delay>1</Delay>
<TargetName>domeflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>1</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>0</Temperature>
<Filter>empty</Filter>
<Type>Bias</Type>
<Count>20</Count>
<Delay>1</Delay>
<TargetName>domeflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
</SequenceQueue>"""

calib = """<?xml version="1.0" encoding="UTF-8"?>
<SequenceQueue version='2.6'>
<GuideDeviation enabled='false'>2</GuideDeviation>
<GuideStartDeviation enabled='false'>2</GuideStartDeviation>
<HFRCheck enabled='false'>
<HFRDeviation>0</HFRDeviation>
<HFRCheckAlgorithm>0</HFRCheckAlgorithm>
<HFRCheckThreshold>10</HFRCheckThreshold>
<HFRCheckFrames>1</HFRCheckFrames>
</HFRCheck>
<RefocusOnTemperatureDelta enabled='false'>1</RefocusOnTemperatureDelta>
<RefocusEveryN enabled='false'>60</RefocusEveryN>
<RefocusOnMeridianFlip enabled='false'/>
<Job>
<Exposure>240</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>X</Filter>
<Type>Bias</Type>
<Count>20</Count>
<Delay>1</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>15</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>Ha</Filter>
<Type>Flat</Type>
<Count>12</Count>
<Delay>1</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F_%E</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>1</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>U</Filter>
<Type>Bias</Type>
<Count>2</Count>
<Delay>1</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>10</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>U</Filter>
<Type>Flat</Type>
<Count>12</Count>
<Delay>0</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F_%E</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>1</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>B</Filter>
<Type>Bias</Type>
<Count>2</Count>
<Delay>1</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>4</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>B</Filter>
<Type>Flat</Type>
<Count>5</Count>
<Delay>0</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F_%E</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>5</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>B</Filter>
<Type>Flat</Type>
<Count>5</Count>
<Delay>0</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F_%E</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>7</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>B</Filter>
<Type>Flat</Type>
<Count>5</Count>
<Delay>0</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F_%E</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>10</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>B</Filter>
<Type>Flat</Type>
<Count>3</Count>
<Delay>0</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F_%E</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>7</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>V</Filter>
<Type>Flat</Type>
<Count>5</Count>
<Delay>1</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F_%E</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>10</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>V</Filter>
<Type>Flat</Type>
<Count>10</Count>
<Delay>1</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F_%E</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>1</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>R</Filter>
<Type>Bias</Type>
<Count>4</Count>
<Delay>14</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>10</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>R</Filter>
<Type>Flat</Type>
<Count>10</Count>
<Delay>5</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F_%E</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>15</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>I</Filter>
<Type>Flat</Type>
<Count>5</Count>
<Delay>5</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F_%E</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>25</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>I</Filter>
<Type>Flat</Type>
<Count>5</Count>
<Delay>5</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F_%E</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>20</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>X</Filter>
<Type>Flat</Type>
<Count>10</Count>
<Delay>1</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>1</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>X</Filter>
<Type>Bias</Type>
<Count>10</Count>
<Delay>1</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>30</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>X</Filter>
<Type>Dark</Type>
<Count>3</Count>
<Delay>1</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%E</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>60</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>X</Filter>
<Type>Dark</Type>
<Count>3</Count>
<Delay>1</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%E</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>10</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>X</Filter>
<Type>Flat</Type>
<Count>1</Count>
<Delay>1</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>120</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>X</Filter>
<Type>Dark</Type>
<Count>3</Count>
<Delay>1</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%E</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
<Job>
<Exposure>1</Exposure>
<Format>Mono</Format>
<Encoding>FITS</Encoding>
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
<Temperature force='false'>-25</Temperature>
<Filter>X</Filter>
<Type>Bias</Type>
<Count>20</Count>
<Delay>1</Delay>
<TargetName>skyflat</TargetName>
<GuideDitherPerJob>0</GuideDitherPerJob>
<FITSDirectory>/home/tucan/data</FITSDirectory>
<PlaceholderFormat>/%t/%T_%F</PlaceholderFormat>
<PlaceholderSuffix>4</PlaceholderSuffix>
<UploadMode>1</UploadMode>
<RemoteDirectory>/home/tucan/data</RemoteDirectory>
<Properties>
</Properties>
<Calibration>
<PreAction>
<Type>1</Type>
</PreAction>
<FlatDuration dark='false'>
<Type>Manual</Type>
</FlatDuration>
</Calibration>
</Job>
</SequenceQueue>"""
######################################CODIGO###################################################################################
import os

def Menu():
     print("""******** 
            Bienvenido al menu de Generación de secuencia de la cámara Tucan.
            ********
            Menu:
        
        1) Generar un Target
        
        2) Generar un Calib
        
        3) Generar un DomeFlat
        
        4) Salir
        """)

def codigo():
    Menu()
    
    opc = int(input("seleccione una opcion\n"))
    nombre_directorio = "Secuencia de obsrvación"
    os.mkdir(nombre_directorio)

    while (opc > 0 and opc <= 4):

        if opc == 1:
            lista_dark_tiempo = []
            with open('Dummy.esq', 'w') as file:
                pass

            ################### Encabezado ##########################
            with open('Dummy.esq', 'a') as file:
                file.write(Encabezado)
                
            ####################### Relleno de secuencia ################################
            print(f"############## Target Nuevo ##############")
            Target_text = "nombre_aqui"
            filtro_text = "Filtro_aqui"
            Cantidad_imagenes_text = "Repetir_aqui"
            Exp_text = "Tiempo_aqui"

            print("---------------------------------------------")
            Target_name = input("Escribe el nombre de tu target")
            print("---------------------------------------------")
            filtro_name = input("elige el tipo de filtro (R,B,V,U,Ha,X):")
            print("---------------------------------------------")
            Cantidad_imagenes_name = input('¿cuantas imagenes van a tomar?:')
            print("---------------------------------------------")
            Exp_name = input('escribe el tiempo de exposición en segundos:')

            ################# Escribir ###########################
            with open('Dummy.esq', 'a') as file:
                file.write(Target)

            ################# Leer sobre lo mismo ###########################
            with open('Dummy.esq', 'r') as file:
                
                data_Target = file.read()

                data_Target = data_Target.replace(Target_text,Target_name)

            with open('Dummy.esq', 'w') as file:
                file.write(data_Target)

            with open('Dummy.esq', 'r') as file:
                
                data_Target = file.read()

                data_Target = data_Target.replace(filtro_text,filtro_name)

            with open('Dummy.esq', 'w') as file:
                file.write(data_Target)

            with open('Dummy.esq', 'r') as file:
                
                data_Target = file.read()

                data_Target = data_Target.replace(Cantidad_imagenes_text,Cantidad_imagenes_name)

            with open('Dummy.esq', 'w') as file:
                file.write(data_Target)

            with open('Dummy.esq', 'r') as file:
                
                data_Target = file.read()

                data_Target = data_Target.replace(Exp_text,Exp_name)

            with open('Dummy.esq', 'w') as file:
                file.write(data_Target)


            ####################################################################################

            lista_dark_tiempo.append(Exp_name)
            print("---------------------------------------------")
            pregunta = input("¿Vas a repetir el Target con otro filtro? (y/n)")

            if pregunta == "y" or pregunta == "Y" or pregunta == "yes":
                while True:
                    print("---------------------------------------------")
                    Cantidad_imagenes_name = input('¿cuantas imagenes van a tomar?:')
                    print("---------------------------------------------")
                    Exp_name = input('escribe el tiempo de exposición en segundos:')
                    print("---------------------------------------------")
                    filtro_name = input("elige el tipo de filtro (R,B,V,U,Ha,X):")

                    ################# Escribir ###########################
                    with open('Dummy.esq', 'a') as file:
                        file.write(Target)

                    ################# Leer sobre lo mismo ###########################
                    with open('Dummy.esq', 'r') as file:
                        
                        data_Target = file.read()

                        data_Target = data_Target.replace(Target_text,Target_name)
                    
                    with open('Dummy.esq', 'w') as file:
                        file.write(data_Target)

                    with open('Dummy.esq', 'r') as file:
                        
                        data_Target = file.read()

                        data_Target = data_Target.replace(filtro_text,filtro_name)

                    with open('Dummy.esq', 'w') as file:
                        file.write(data_Target)


                    with open('Dummy.esq', 'r') as file:
                        
                        data_Target = file.read()

                        data_Target = data_Target.replace(Cantidad_imagenes_text,Cantidad_imagenes_name)

                    with open('Dummy.esq', 'w') as file:
                        file.write(data_Target)


                    with open('Dummy.esq', 'r') as file:
                        
                        data_Target = file.read()

                        data_Target = data_Target.replace(Exp_text,Exp_name)

                    with open('Dummy.esq', 'w') as file:
                        file.write(data_Target)

                    ####################################################################################

                    lista_dark_tiempo.append(Exp_name)
                    print("---------------------------------------------")
                    pregunta = input("¿Vas a repetir el Target con otro filtro? (y/n)")
                    if pregunta == "n" or pregunta == "N" or pregunta == "no":
                        break



            lista_dark_tiempo = list(dict.fromkeys(lista_dark_tiempo))
            ##########################DARK######################################################

            for i in range(len(lista_dark_tiempo)):

                with open('Dummy.esq', 'a') as file:
                    file.write(Dark)

                with open('Dummy.esq', 'r') as file:
                    data_Dark = file.read()

                    data_Dark = data_Dark.replace(Exp_text, lista_dark_tiempo[i])

                with open('Dummy.esq', 'w') as file:
                    file.write(data_Dark)
                
                with open('Dummy.esq', 'r') as file:
                    data_Dark = file.read()

                    data_Dark = data_Dark.replace(Target_text, Target_name)
                
                with open('Dummy.esq', 'w') as file:
                    file.write(data_Dark)



            with open('Dummy.esq', 'a') as file:
                file.write(final)

            os.rename('Dummy.esq',f'{nombre_directorio}/{Target_name}_sec.esq')

            print("--------------------------------------------------------------------")
            print("Tu secuencia ha sido finalizada")
            print("--------------------------------------------------------------------")
            deseo = input("¿Deseas volver al menu? (y/n):")

            if deseo == "y":
                Menu()
                opc = int(input("seleccione una opcion\n"))
            else:
                print("----------------------------------------------------")
                print("Saliendo del programa ;)")
                break
#############################################################################################################################################        
        elif opc == 2:
            with open('Dummy.esq', 'w') as file:
                pass
            with open('Dummy.esq', 'a') as file:
                file.write(calib)
            
            os.rename('Dummy.esq',f'{nombre_directorio}/Calib_skyflat.esq')
            deseo = input("¿Deseas volver al menu? (y/n):")

            if deseo == "y":
                Menu()
                opc = int(input("seleccione una opcion\n"))
            else:
                print("----------------------------------------------------")
                print("Saliendo del programa ;)")
                break
####################################################################################################################################################
        elif opc == 3:
            with open('Dummy.esq', 'w') as file:
                pass
            with open('Dummy.esq', 'a') as file:
                file.write(domeflat)
            
            os.rename('Dummy.esq',f'{nombre_directorio}/Calib_skyflat.esq')
            deseo = input("¿Deseas volver al menu? (y/n):")

            if deseo == "y":
                Menu()
                opc = int(input("seleccione una opcion\n"))
            else:
                print("----------------------------------------------------")
                print("Saliendo del programa ;)")
                break
####################################################################################################################################################
        elif opc == 4:
            print("----------------------------------------------------")
            print("Saliendo del programa ;)")
            break
