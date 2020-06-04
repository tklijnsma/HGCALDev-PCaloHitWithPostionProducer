#  HGCALDev/PCaloHitWithPostionProducer

Requires DataFormats/HGCALHistoryFormats.

## Installation

```
cmsrel CMSSW_11_1_0_pre6
cd CMSSW_11_1_0_pre6/src
cmsenv
git clone https://github.com/tklijnsma/DataFormats-HGCALHistoryFormats.git DataFormats/HGCALHistoryFormats
git clone https://github.com/tklijnsma/HGCALDev-PCaloHitWithPostionProducer.git HGCALDev/PCaloHitWithPostionProducer
scram b -j 8
```

## Running

For a GENSIM-level root file (to be used for e.g. further ntupling):

```
cmsRun HGCALDev/PCaloHitWithPostionProducer/python/SingleMuPt_pythia8_cfi_GEN_SIM_PCaloHitWithPosition.py
```

To use the [basic ntupler](plugins/HistoryNTupler.cc) included with the repo:

```
cmsRun muonflatptgun_ntupled.py
```

The configs have some command line options, defined at the top of the source files.
