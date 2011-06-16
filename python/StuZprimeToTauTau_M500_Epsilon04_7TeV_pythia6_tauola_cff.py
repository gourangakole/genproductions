#Stueckelburg Z prime pythia6 card
import FWCore.ParameterSet.Config as cms
source = cms.Source("EmptySource")
from Configuration.Generator.PythiaUEZ2Settings_cfi import *
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
pythiaHepMCVerbosity = cms.untracked.bool(False),
maxEventsToPrint = cms.untracked.int32(0),
pythiaPylistVerbosity = cms.untracked.int32(1),
filterEfficiency = cms.untracked.double(1.),
comEnergy = cms.double(7000.0),
crossSection = cms.untracked.double(6.369e-3),
ExternalDecays = cms.PSet(
    Tauola = cms.untracked.PSet(
	TauolaPolar,
	TauolaDefaultInputCards
    ),
    parameterSets = cms.vstring('Tauola')
),
PythiaParameters = cms.PSet(
pythiaUESettingsBlock,
processParameters = cms.vstring(
'MSEL=0                  !turn off processes',
'MSTU(12)=12345          !no title page is written',
'MSUB(141)=1             !Turn on Drell-Yan SubProcess f+fbar-->gamma/Z0/Zp0, same as MSEL=21',
'PMAS(32,1)=500          !M_Zprime for Zprime',
'PARU(121)=0.00594853   ! g_v for d to Zp',
'PARU(122)=-0.0198789   ! g_a for d to Zp',
'PARU(123)=-0.0317759   ! g_v for u to Zp',
'PARU(124)=0.0198789   ! g_a for u to Zp',
'PARU(125)=0.0576033   ! g_v for e to Zp',
'PARU(126)=-0.0198789   ! g_a for e to Zp',
'PARU(127)=0.0198789   ! g_v for Nu_e to Zp',
'PARU(128)=0.0198789   ! g_a for Nu_e to Zp',
'PARJ(180)=0.00594853   ! g_v for s to Zp',
'PARJ(181)=-0.0198789   ! g_a for s to Zp',
'PARJ(182)=-0.0317759   ! g_v for c to Zp',
'PARJ(183)=0.0198789   ! g_a for c to Zp',
'PARJ(184)=0.0576033   ! g_v for mu to Zp',
'PARJ(185)=-0.0198789   ! g_a for mu to Zp',
'PARJ(186)=0.0198789   ! g_v for Nu_mu to Zp',
'PARJ(187)=0.0198789   ! g_a for Nu_mu to Zp',
'PARJ(188)=0.00594853   ! g_v for b to Zp',
'PARJ(189)=-0.0198789   ! g_a for b to Zp',
'PARJ(190)=-0.0301386   ! g_v for t to Zp',
'PARJ(191)=0.0123664   ! g_a for t to Zp',
'PARJ(192)=0.0576033   ! g_v for tau to Zp',
'PARJ(193)=-0.0198789   ! g_a for tau to Zp',
'PARJ(194)=0.0198789   ! g_v for Nu_tau to Zp',
'PARJ(195)=0.0198789   ! g_a for Nu_tau to Zp',
'MDCY(15,1)=0            ! sets tau stable - this is important (for tauola)!',
'MDME(289,1)=0    ! d dbar',
'MDME(290,1)=0    ! u ubar',
'MDME(291,1)=0    ! s sbar',
'MDME(292,1)=0    ! c cbar',
'MDME(293,1)=0    ! b bbar',
'MDME(294,1)=0    ! t tbar',
'MDME(295,1)=-1    ! 4th gen Q Qbar',
'MDME(296,1)=-1    ! 4th gen Q Qbar',
'MDME(297,1)=0    ! e e',
'MDME(298,1)=0    ! neutrino e e',
'MDME(299,1)=0    ! mu mu',
'MDME(300,1)=0    ! neutrino mu mu',
'MDME(301,1)=1    ! tau tau',
'MDME(302,1)=0    ! neutrino tau tau',
'MDME(303,1)=-1    ! 4th generation lepton l- l+',
'MDME(304,1)=-1    ! 4th generation neutrino nu nubar',
'MDME(305,1)=-1    ! W+ W-',
'MDME(306,1)=-1    ! H  charged higgs',
'MDME(307,1)=-1    ! Z0 gamma',
'MDME(308,1)=-1    ! Z0 h0',
'MDME(309,1)=-1    ! sm higgs',
'MDME(310,1)=-1    ! weird neutral higgs H0A0',
'MSTP(44)=3              !gamma/Z/Zp: 3=> Zp only'),
parameterSets = cms.vstring('pythiaUESettings','processParameters')
))
ProductionFilterSequence = cms.Sequence(generator)
