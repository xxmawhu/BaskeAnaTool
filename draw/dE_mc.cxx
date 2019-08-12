// Copyright (c) 2019-2-26 maxx
#include "bes3plotstyle_1.C"
void dE_mc(double a = 0) {
    SetStyle();
    gStyle->SetPadRightMargin(0.15);

    TChain chDpDm("sig");
    chDpDm.Add("../mode/sig.DpDm*.root");

    TChain chD0D0("sig");
    chD0D0.Add("../mode/sig.D0D0*.root");

    TChain chtt("sig");
    chtt.Add("../mode/sig.ditau*.root");

    TChain chgJ("sig");
    chgJ.Add("../mode/sig.gammaJpsi*.root");

    TChain chgP("sig");
    chgP.Add("../mode/sig.gammapsip*.root");

    TChain chnonD("sig");
    chnonD.Add("../mode/sig.nonDD*.root");

    TChain chqq("sig");
    chqq.Add("../mode/sig.qq*.root");

    TH1D* hsig = new TH1D("hsig", "#Delta E", 50, -0.1, 0.1);
    TH1D* hD0 = new TH1D("hD0", "#Delta E", 50, -0.1, 0.1);
    TH1D* hgJ = new TH1D("hgJ", "#Delta E", 50, -0.1, 0.1);
    TH1D* hgP = new TH1D("hgP", "#Delta E", 50, -0.1, 0.1);
    TH1D* hqq = new TH1D("hqq", "#Delta E", 50, -0.1, 0.1);
    TH1D* htt = new TH1D("htt", "#Delta E", 50, -0.1, 0.1);
    TH1D* hnonD = new TH1D("hnonD", "#Delta E", 50, -0.1, 0.1);
    chDpDm.Project("hsig", "deltaE", "");
    chD0D0.Project("hD0", "deltaE", "");
    chgJ.Project("hgJ", "deltaE", "");
    chgP.Project("hgP", "deltaE", "");
    chqq.Project("hqq", "deltaE", "");
    chtt.Project("htt", "deltaE", "");
    chnonD.Project("hnonD", "deltaE", "");
    hqq->Scale(1 / 7.5);
    hsig->Scale(1 / 10.0);
    htt->Scale(1 / 10.0);
    hD0->Scale(1 / 10.0);
    hnonD->Scale(1 / 10.0);
    hgJ->Scale(1 / 10.0);
    hgP->Scale(1 / 10.0);
    // hnonD, htt, hqq, hgP, hgJ, hD0, hsig
    htt->Add(hnonD);
    hgP->Add(htt);
    hgJ->Add(hgP);
    hD0->Add(hgJ);
    hqq->Add(hD0);
    hsig->Add(hqq);

    TCanvas* c = new TCanvas("c", "", 800, 600);
    hsig->GetXaxis()->SetTitle("#Delta E (GeV)");
    hsig->GetYaxis()->SetTitle("Events/4 MeV");
    // hsig->GetYaxis()->SetTitle("Events ( 20 MeV^{-1}c^{2})");
    FormatAxis(hsig->GetYaxis());
    FormatAxis(hsig->GetXaxis());
    hsig->SetMaximum(hsig->GetMaximum() / 0.8);
    hsig->SetMinimum(0.0);
    TGaxis* xaxis = reinterpret_cast<TGaxis*>(hsig->GetYaxis());
    xaxis->SetMaxDigits(3);

    hsig->SetMarkerSize(0.0);
    hqq->SetMarkerSize(0.0);
    hD0->SetMarkerSize(0.0);
    hgP->SetMarkerSize(0.0);
    hgJ->SetMarkerSize(0.0);
    htt->SetMarkerSize(0.0);
    hnonD->SetMarkerSize(0.0);

    hsig->SetFillColor(kRed);
    hsig->SetLineColor(kRed);
    hqq->SetFillColor(kOrange);
    hqq->SetLineColor(kOrange);
    hD0->SetFillColor(kOrange - 3);
    hD0->SetLineColor(kOrange - 3);
    hgP->SetFillColor(kTeal);
    hgP->SetLineColor(kTeal);
    hgJ->SetFillColor(kGreen + 1);
    hgJ->SetLineColor(kGreen + 1);
    htt->SetFillColor(kPink + 10);
    htt->SetLineColor(kPink + 10);
    hnonD->SetFillColor(kBlue);
    hnonD->SetLineColor(kBlue);

    hsig->Draw();
    hqq->Draw("same");
    hD0->Draw("same");
    hgP->Draw("same");
    hgJ->Draw("same");
    htt->Draw("same");
    hnonD->Draw("same");
    c->RedrawAxis();

    TLegend* leg = new TLegend(0.68, 0.6, 0.86, 0.85);
    leg->AddEntry(hsig, "D^{+}D^{-}");
    leg->AddEntry(hqq, "q#bar{q}");
    leg->AddEntry(hD0, "D^{0}#bar{D^{0}}");
    // leg->AddEntry(hgP   , "#gamma #psi");
    leg->AddEntry(hgJ, "#gamma J/#psi");
    leg->AddEntry(htt, "#tau#tau");
    leg->AddEntry(hnonD, "none-D#bar{D}");
    Format(leg);
    leg->Draw();
    // if you want draw an arrow , add the following statements
    // TArrow *arr = new TArrow(0,1000,0,0,0.01,">");
    // Format(arr);
    // arr->Draw();

    c->SaveAs("fig/deltaE.eps");
    c->SaveAs("fig/deltaE.png");
}
