#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"
#include "FWCore/PluginManager/interface/ModuleDef.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h" 

#include <TTree.h>
#include <TLorentzVector.h>
 
#include <vector>
#include <memory>
#include <cmath>
#include <iostream>
#include <string>
#include <cstdlib>
using std::vector;

#include "RecoLocalCalo/HGCalRecAlgos/interface/RecHitTools.h"
#include "DataFormats/Common/interface/Ptr.h"
#include "DataFormats/Common/interface/View.h"
#include "SimDataFormats/CaloHit/interface/PCaloHitContainer.h"
#include "SimDataFormats/CaloHit/interface/PCaloHit.h"
#include "DataFormats/HGCALHistoryFormats/interface/PCaloHitWithPosition.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "SimDataFormats/Track/interface/SimTrack.h"
#include "SimDataFormats/Vertex/interface/SimVertex.h"
#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "SimDataFormats/Vertex/interface/SimVertexContainer.h"

#include <memory>
#include <vector>
#include <cstdlib>
#include <iostream>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "RecoLocalCalo/HGCalRecAlgos/interface/RecHitTools.h"

#include "DataFormats/Common/interface/Ptr.h"
#include "DataFormats/Common/interface/View.h"
#include "SimDataFormats/CaloHit/interface/PCaloHitContainer.h"
#include "SimDataFormats/CaloHit/interface/PCaloHit.h"
#include "DataFormats/HGCALHistoryFormats/interface/PCaloHitWithPosition.h"
#include "DataFormats/DetId/interface/DetId.h"



class HGCALGeomPrinter : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
    public:
        explicit HGCALGeomPrinter(const edm::ParameterSet&) {}
        ~HGCALGeomPrinter() {}
    private:
        hgcal::RecHitTools hgcalRecHitToolInstance_ ;
        void beginJob() override {}
        void doBeginRun_(const edm::Run&, const edm::EventSetup&) override;
        void analyze(const edm::Event&, const edm::EventSetup&) override;
        void doEndRun_(const edm::Run&, const edm::EventSetup&) override {}
        void endJob() override {}
    };

void HGCALGeomPrinter::doBeginRun_(const edm::Run&, const edm::EventSetup& iSetup) {
    hgcalRecHitToolInstance_ = hgcal::RecHitTools();
    hgcalRecHitToolInstance_.getEventSetup(iSetup);
    std::cout << "hgcalRecHitToolInstance_ is setup" << std::endl;
    }

void HGCALGeomPrinter::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
    std::cout << "hgcalRecHitToolInstance_ printer in analyze" << std::endl;
    hgcalRecHitToolInstance_.getEvent(iEvent);

    std::cout << "lastLayerEE() = " << hgcalRecHitToolInstance_.lastLayerEE() << std::endl;
    std::cout << "lastLayerFH() = " << hgcalRecHitToolInstance_.lastLayerFH() << std::endl;
    std::cout << "firstLayerBH() = " << hgcalRecHitToolInstance_.firstLayerBH() << std::endl;
    std::cout << "lastLayerBH() = " << hgcalRecHitToolInstance_.lastLayerBH() << std::endl;
    std::cout << "lastLayer() = " << hgcalRecHitToolInstance_.lastLayer() << std::endl;
    std::cout << "maxNumberOfWafersPerLayer() = " << hgcalRecHitToolInstance_.maxNumberOfWafersPerLayer() << std::endl;
    std::cout << "getScintMaxIphi() = " << hgcalRecHitToolInstance_.getScintMaxIphi() << std::endl;
    std::cout << "getGeometryType() = " << hgcalRecHitToolInstance_.getGeometryType() << std::endl;

    for (unsigned int i = 0; i < hgcalRecHitToolInstance_.lastLayer(); ++i) {
        GlobalPoint layerPos = hgcalRecHitToolInstance_.getPositionLayer(i);
        std::cout
            << "Layer " << i
            << ": x=" << layerPos.x()
            << " y=" << layerPos.y()
            << " z=" << layerPos.z()
            << std::endl
            ;
        }

    std::cout << "With nose=true:" << std::endl;
    std::cout << "lastLayerEE(true) = " << hgcalRecHitToolInstance_.lastLayerEE(true) << std::endl;
    std::cout << "lastLayer(true) = " << hgcalRecHitToolInstance_.lastLayer(true) << std::endl;
    std::cout << "maxNumberOfWafersPerLayer(true) = " << hgcalRecHitToolInstance_.maxNumberOfWafersPerLayer(true) << std::endl;

    for (unsigned int i = 0; i < hgcalRecHitToolInstance_.lastLayer(true); ++i) {
        GlobalPoint layerPos = hgcalRecHitToolInstance_.getPositionLayer(i, true);
        std::cout
            << "Layer " << i
            << ": x=" << layerPos.x()
            << " y=" << layerPos.y()
            << " z=" << layerPos.z()
            << std::endl
            ;
        }

    // std::cout << "Printing first 10 layers" << std::endl;
    // for (unsigned int i = 0; i < 10; ++i) {
    //     GlobalPoint layerPos = hgcalRecHitToolInstance_.getPositionLayer(i);
    //     std::cout
    //         << "Layer " << i
    //         << ": x=" << layerPos.x()
    //         << " y=" << layerPos.y()
    //         << " z=" << layerPos.z()
    //         << std::endl
    //         ;
    //     }
    }

DEFINE_FWK_MODULE(HGCALGeomPrinter);
