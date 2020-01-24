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


class PCaloHitWithPositionProducer : public edm::stream::EDProducer<> {
    public:
        explicit PCaloHitWithPositionProducer(const edm::ParameterSet&);
        ~PCaloHitWithPositionProducer() {}
    private:
        virtual void produce(edm::Event&, const edm::EventSetup&) override;
        void beginRun(const edm::Run&, const edm::EventSetup&) override;
        hgcal::RecHitTools hgcalRecHitToolInstance_ ;
        edm::EDGetTokenT<edm::View<PCaloHit>> hgcalEEHitsToken_;
        edm::EDGetTokenT<edm::View<PCaloHit>> hgcalHEfrontHitsToken_;
        edm::EDGetTokenT<edm::View<PCaloHit>> hgcalHEbackHitsToken_;
    };


PCaloHitWithPositionProducer::PCaloHitWithPositionProducer(const edm::ParameterSet& iConfig) :
    hgcalEEHitsToken_(consumes<edm::View<PCaloHit>>(edm::InputTag("g4SimHits", "HGCHitsEE"))),
    hgcalHEfrontHitsToken_(consumes<edm::View<PCaloHit>>(edm::InputTag("g4SimHits", "HGCHitsHEfront"))),
    hgcalHEbackHitsToken_(consumes<edm::View<PCaloHit>>(edm::InputTag("g4SimHits", "HGCHitsHEback")))
    {
    produces<std::vector<PCaloHitWithPosition>>();
    }


void PCaloHitWithPositionProducer::beginRun(const edm::Run&, const edm::EventSetup& iSetup) {
    hgcalRecHitToolInstance_ = hgcal::RecHitTools();
    hgcalRecHitToolInstance_.getEventSetup(iSetup);
    }


void PCaloHitWithPositionProducer::produce(edm::Event& iEvent, const edm::EventSetup&) {  
    std::unique_ptr< std::vector< PCaloHitWithPosition >> hitsWithPositions( new std::vector<PCaloHitWithPosition> );
    hgcalRecHitToolInstance_.getEvent(iEvent);

    std::vector<edm::EDGetTokenT<edm::View<PCaloHit>>> tokens = {
        hgcalEEHitsToken_,
        hgcalHEfrontHitsToken_,
        hgcalHEbackHitsToken_
        };

    for (edm::EDGetTokenT<edm::View<PCaloHit>> token : tokens ) {
        edm::Handle< edm::View<PCaloHit> > handle;
        iEvent.getByToken(token, handle);

        for (auto const & hit : handle->ptrs() ) {
            PCaloHitWithPosition hitWithPosition = PCaloHitWithPosition();
            hitWithPosition.setVars(&(*hit), &hgcalRecHitToolInstance_);
            hitsWithPositions->push_back(std::move(hitWithPosition));
            }
        }


    // edm::Handle< edm::View<PCaloHit> > hgcalHitsHandle;
    // iEvent.getByToken(hgcalHitsToken_, hgcalHitsHandle);


    // // for (auto const& hgcalHit : *(hgcalHitsHandle.product())) {
    // // for (auto const & hgcalHit : *hgcalHitsHandle) {
    // for (auto const & hgcalHit : hgcalHitsHandle->ptrs() ) {
    //     PCaloHitWithPosition hitWithPosition = PCaloHitWithPosition();
    //     hitWithPosition.setVars(&(*hgcalHit), &hgcalRecHitToolInstance_);
    //     hitsWithPositions->push_back(std::move(hitWithPosition));
    //     // std::cout << "Making DetId for hit\n";
    //     // DetId detId(hgcalHit->id());
    //     // std::cout << "Determining det of hit\n";
    //     // DetId::Detector det = detId.det();
    //     // if( det == DetId::HGCalEE ){
    //     //     std::cout << "Hit is HGCalEE\n";
    //     //     PCaloHitWithPosition hitWithPosition = PCaloHitWithPosition(hgcalHit);
    //     //     hitWithPosition.setPositionVars(&hgcalRecHitToolInstance_);
    //     //     hitsWithPositions->push_back(std::move(hitWithPosition));
    //     //     std::cout << "Created new PCaloHitWithPosition\n";            
    //     //     }
    //     // else {
    //     //     std::cout << "Hit is NOT HGCalEE\n";
    //     //     }
    //     }

    // Put the output back in the event
    iEvent.put(std::move(hitsWithPositions));
    }


//define this as a plug-in
DEFINE_FWK_MODULE(PCaloHitWithPositionProducer);