import FWCore.ParameterSet.Config as cms

l1ParamMuons = cms.EDProducer("FastL1MuonProducer",
    # Set the following to false if you want to use the default CLHEP
    # random engine
    UseTRandomEngine = cms.bool(True),
    # Muons
    MUONS = cms.PSet(
        # The muon simtrack's must be taken from there
        simModule = cms.InputTag("famosSimHits","MuonSimTracks"),
        MaxEta = cms.double(2.4),
        # Simulate  only simtracks in this eta range
        MinEta = cms.double(-2.4)
    )
)

