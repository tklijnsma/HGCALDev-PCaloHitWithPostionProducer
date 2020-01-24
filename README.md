#  HGCALDev/PCaloHitWithPostionProducer

Requires DataFormats/HGCALHistoryFormats.

## Installation and running

```
cmsrel CMSSW_11_0_0_pre10
cd CMSSW_11_0_0_pre10/src
cmsenv
git clone https://github.com/tklijnsma/DataFormats-HGCALHistoryFormats.git DataFormats/HGCALHistoryFormats
git clone https://github.com/tklijnsma/HGCALDev-PCaloHitWithPostionProducer.git HGCALDev/PCaloHitWithPostionProducer
scram b -j 8
cmsRun HGCALDev/PCaloHitWithPostionProducer/python/SingleMuPt_pythia8_cfi_GEN_SIM_PCaloHitWithPosition.py
```