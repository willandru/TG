import pygds as g
d = g.
()
minf_s = sorted(d.GetSupportedSamplingRates()[0].items())[0]
d.SamplingRate, d.NumberOfScans = minf_s
for ch in d.Channels:
 ch.Acquire = True
d.SetConfiguration()
data = d.GetData(d.SamplingRate)