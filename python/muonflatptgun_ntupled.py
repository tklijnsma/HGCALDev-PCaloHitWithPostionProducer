# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: SingleMuPt1000_pythia8_cfi --conditions auto:phase2_realistic_T14 -n 10 --era Phase2C8_timing_layer_bar --eventcontent FEVTDEBUG --relval 9000,100 -s GEN,SIM --datatier GEN-SIM --beamspot HLLHC --geometry Extended2026D41 --no_exec --fileout file:step1.root
import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing("analysis")
options.register(
    'MuonPt',
    10000.,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Energy in MeV used for the muon gun"
    )
options.register(
    'EminFineTrack',
    .5,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Minimum energy in MeV for which secondary tracks in Calo will be saved"
    )
options.register(
    'EminFinePhoton',
    .5,
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
options.outputFile = 'hgcalhistoryntuple.root'
options.maxEvents = 2
options.parseArguments()


# from Configuration.Eras.Era_Phase2C8_timing_layer_bar_cff import Phase2C8_timing_layer_bar
# process = cms.Process('SIM',Phase2C8_timing_layer_bar)

from Configuration.Eras.Era_Phase2C8_cff import Phase2C8
process = cms.Process('SIM',Phase2C8)


# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D41Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2026D41_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedHLLHC_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

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
process.g4SimHits.CaloSD.UseFineCaloID = cms.bool(True)
process.g4SimHits.DoFineCalo = cms.bool(True)
process.g4SimHits.CaloTrkProcessing.EminFineTrack = cms.double(options.EminFineTrack)
process.g4SimHits.CaloTrkProcessing.EminFinePhoton = cms.double(options.EminFinePhoton)

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
        MinPt = cms.double(options.MuonPt - 0.01),
        MaxPt = cms.double(options.MuonPt + 0.01),
        # ParticleID = cms.vint32(211), # Pions
        ParticleID = cms.vint32(-13), # Muons
        ),
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring()
        ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('single mu pt {0}'.format(int(options.MuonPt)))
    # psethack = cms.string('single pi pt 1000')
    )

process.PCaloHitWithPositionProducer = cms.EDProducer("PCaloHitWithPositionProducer")

process.HistoryNTupler = cms.EDAnalyzer(
    "HistoryNTupler",
    PCaloHitWithPositionTag = cms.InputTag("PCaloHitWithPositionProducer"),
    # SimTrackTag = cms.InputTag("simTracksInput"),
    # SimVertexTag = cms.InputTag("simVerticesInput")
    )

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.produce_calohitswithposition_step = cms.Path(process.PCaloHitWithPositionProducer)
process.ntuple_step = cms.Path(process.HistoryNTupler)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule(
    process.generation_step,
    process.genfiltersummary_step,
    process.simulation_step,
    process.produce_calohitswithposition_step,
    process.ntuple_step,
    process.endjob_step,
    )

from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.generator)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
