# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: SingleMuPt1000_pythia8_cfi --conditions auto:phase2_realistic_T14 -n 10 --era Phase2C8_timing_layer_bar --eventcontent FEVTDEBUG --relval 9000,100 -s GEN,SIM --datatier GEN-SIM --beamspot HLLHC --geometry Extended2026D41 --no_exec --fileout file:step1.root
import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing("analysis")
options.register(
    'pt',
    10000.,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Energy in MeV used for the muon gun"
    )
options.register(
    'eminfine',
    10.0,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "fixme"
    )
options.register(
    'EminFineTrack',
    1.0,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Minimum energy in MeV for which secondary tracks in Calo will be saved"
    )
options.register(
    'EminFinePhoton',
    1.0,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Minimum energy in MeV for which secondary photons in Calo will be saved"
    )
options.register(
    'seed',
    1001,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "Generator seed"
    )
options.register(
    'outputGEN',
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "If set to True, outputs the GEN-level rather than a flat N-tuple."
    )
options.register(
    'debug',
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "If set to True, prints LogDebug and LogWarning for a few packages"
    )
options.register(
    'pdgid',
    -13,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "pdgid of primary particle, default muon"
    )
options.register(
    'storeAllTracksCalo',
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "If set to True, stores ALL Geant tracks in Calorimeters"
    )
options.register(
    'dofinecalo',
    True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Flag to control whether to activate fineCalo or not"
    )
options.register(
    'rundigi',
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Flag to control whether to run the digi steps"
    )
options.outputFile = 'default.root'
options.maxEvents = 1
options.parseArguments()

from time import strftime
if options.outputFile.startswith('default'):
    options.outputFile = options.outputFile.replace(
        'default',
        'event{seed}_pdgid{pdgid}_{pt}GeV_{date}_{finecalo}'.format(
            seed = options.seed,
            pdgid = abs(options.pdgid),
            pt = int(options.pt),
            date = strftime('%b%d'),
            finecalo = 'finecalo' if options.dofinecalo else 'nofine'
            )
        )

# from Configuration.Eras.Era_Phase2C8_timing_layer_bar_cff import Phase2C8_timing_layer_bar
# process = cms.Process('SIM',Phase2C8_timing_layer_bar)

from Configuration.Eras.Era_Phase2C8_cff import Phase2C8
process = cms.Process('SIM',Phase2C8)
# from Configuration.Eras.Era_Phase2C9_cff import Phase2C9
# process = cms.Process('SIM',Phase2C9)
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
# process.load('Configuration.EventContent.EventContent_cff')
# process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
# process.load('Configuration.Geometry.GeometryExtended2026D49_cff')
process.load('Configuration.Geometry.GeometryExtended2026D41Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2026D41_cff')
process.load("SimGeneral.MixingModule.mixNoPU_cfi")
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('Configuration.StandardSequences.VtxSmearedNoSmear_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.L1TrackTrigger_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_Fake2_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

# # import of standard configurations
# process.load('Configuration.StandardSequences.Services_cff')
# process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
# process.load('FWCore.MessageService.MessageLogger_cfi')
# process.load('Configuration.EventContent.EventContent_cff')
# process.load('SimGeneral.MixingModule.mixNoPU_cfi')
# process.load('Configuration.Geometry.GeometryExtended2026D41Reco_cff')
# process.load('Configuration.Geometry.GeometryExtended2026D41_cff')
# process.load('Configuration.StandardSequences.MagneticField_cff')
# process.load('Configuration.StandardSequences.Generator_cff')
# process.load('IOMC.EventVertexGenerators.VtxSmearedHLLHC_cfi')
# process.load('GeneratorInterface.Core.genFilterSummary_cff')
# process.load('Configuration.StandardSequences.SimIdeal_cff')
# process.load('Configuration.StandardSequences.EndOfProcess_cff')
# process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
# if options.rundigi:
#     process.load('Configuration.StandardSequences.Digi_cff')
#     process.load('Configuration.StandardSequences.SimL1Emulator_cff')
#     process.load('Configuration.StandardSequences.L1TrackTrigger_cff')
#     process.load('Configuration.StandardSequences.DigiToRaw_cff')

if options.debug:
    # Message logger setup
    process.load("FWCore.MessageLogger.MessageLogger_cfi")
    process.MessageLogger.infos = cms.untracked.PSet(placeholder = cms.untracked.bool(True))
    process.MessageLogger.cerr.threshold = "DEBUG"
    process.MessageLogger.cerr.FwkReport.limit = 0
    process.MessageLogger.cerr.FwkSummary.limit = 0
    process.MessageLogger.cerr.default.limit = 0
    categories = [
        # 'SimG4CoreApplication',
        # 'SimG4CoreGenerator',
        # 'HistoryNTupler',
        # 'CaloSim',
        # 'TrackInformation'
        'DoFineCalo'
        ]
    process.MessageLogger.categories.extend(categories)
    process.MessageLogger.debugModules = categories
    for cat in categories:
        setattr(
            process.MessageLogger.cerr, cat, 
            cms.untracked.PSet(
                optionalPSet = cms.untracked.bool(True),
                limit = cms.untracked.int32(10000000),
                )
            )

# reset all random numbers to ensure statistically distinct but reproducible jobs
from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
randHelper = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
randHelper.resetSeeds(options.seed)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
    )

# Input source
process.source = cms.Source(
    "EmptySource",
    )

# Options for saving fine hits
print 'dofinecalo: ' + str(cms.bool(options.dofinecalo))
process.g4SimHits.CaloSD.DoFineCalo = cms.bool(options.dofinecalo)
process.g4SimHits.CaloTrkProcessing.DoFineCalo = cms.bool(options.dofinecalo)
process.g4SimHits.TrackingAction.DoFineCalo = cms.untracked.bool(options.dofinecalo)
process.g4SimHits.CaloSD.EMinFine = cms.double(options.eminfine)
# process.g4SimHits.CaloSD.UseFineCaloID = cms.bool(True)
# process.g4SimHits.CaloTrkProcessing.DoFineCalo = cms.bool(True)
# process.g4SimHits.CaloTrkProcessing.EminFineTrack = cms.double(options.EminFineTrack)
# process.g4SimHits.CaloTrkProcessing.EminFinePhoton = cms.double(options.EminFinePhoton)
# process.g4SimHits.CaloTrkProcessing.PutInHistoryAllTracksCalo = cms.bool(options.putInHistoryAllTracksCalo)
# process.g4SimHits.CaloTrkProcessing.StoreAllTracksCalo = cms.bool(options.storeAllTracksCalo)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
        ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
    )

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(options.outputFile)
    )

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('SingleMuPt1000_pythia8_cfi nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
    )

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T14', '')


process.generator = cms.EDFilter("Pythia8PtGun",
    PGunParameters = cms.PSet(
        AddAntiParticle = cms.bool(True),
        # MinEta = cms.double(-2.5),
        # MaxEta = cms.double(2.5),
        MinEta = cms.double(1.6),
        MaxEta = cms.double(2.8),
        MinPhi = cms.double(-3.14159265359),
        MaxPhi = cms.double(3.14159265359),
        MinPt = cms.double(options.pt - 0.01),
        MaxPt = cms.double(options.pt + 0.01),
        ParticleID = cms.vint32(options.pdgid),
        ),
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring()
        ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('single {0} pt {1}'.format(options.pdgid, int(options.pt)))
    # psethack = cms.string('single pi pt 1000')
    )

process.PCaloHitWithPositionProducer = cms.EDProducer("PCaloHitWithPositionProducer")

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.produce_calohitswithposition_step = cms.Path(process.PCaloHitWithPositionProducer)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)

if options.rundigi:
    process.digitisation_step = cms.Path(process.pdigi_valid)
    process.L1simulation_step = cms.Path(process.SimL1Emulator)
    process.L1TrackTrigger_step = cms.Path(process.L1TrackTrigger)
    process.digi2raw_step = cms.Path(process.DigiToRaw)

steps = (
    [
        process.generation_step,
        process.genfiltersummary_step,
        process.simulation_step,
        process.produce_calohitswithposition_step,        
        ]
    + ([
        process.digitisation_step,
        process.L1simulation_step,
        process.L1TrackTrigger_step,
        process.digi2raw_step,        
        ] if options.rundigi else [])
    + [
        process.endjob_step
        ]
    )
process.schedule = cms.Schedule(*steps)

# if options.debug:
#     process.preprocessorTagChecker = cms.EDAnalyzer("PreprocessorTagChecker")
#     process.preprocessor_checker_step = cms.Path(process.preprocessorTagChecker)
#     process.schedule.insert(0, process.preprocessor_checker_step)

if options.outputGEN:
    process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
        SelectEvents = cms.untracked.PSet(
            SelectEvents = cms.vstring('generation_step')
            # SelectEvents = cms.vstring('produce_calohitswithposition_step')
            ),
        dataset = cms.untracked.PSet(
            dataTier = cms.untracked.string('GEN-SIM'),
            filterName = cms.untracked.string('')
            ),
        fileName = cms.untracked.string(options.outputFile),
        outputCommands = process.FEVTDEBUGEventContent.outputCommands,
        splitLevel = cms.untracked.int32(0)
        )
    process.FEVTDEBUGoutput.outputCommands.extend([
        'keep *_PCaloHitWithPositionProducer_*_*',
        'keep SimTracks_*_*_*',
        'keep SimVertexs_*_*_*',
        'keep *_genParticles_*_*',
        'keep recoGenMETs_*_*_*',
        ])
    process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)
    process.schedule.append(process.FEVTDEBUGoutput_step)

elif not options.rundigi:
    process.HistoryNTupler = cms.EDAnalyzer(
        "HistoryNTupler",
        PCaloHitWithPositionTag = cms.InputTag("PCaloHitWithPositionProducer"),
        )
    process.ntuple_step = cms.Path(process.HistoryNTupler)
    process.schedule.insert(
        process.schedule.index(process.produce_calohitswithposition_step) + 1, process.ntuple_step
        )

print 'Final process.schedule:'
print process.schedule

from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
    getattr(process,path).insert(0, process.generator)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
