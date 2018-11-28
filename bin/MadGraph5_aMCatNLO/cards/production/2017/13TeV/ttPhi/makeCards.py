import os

procTemplate = open("/cms/heindl/2018/Signal_Gridpacks/ttPhi_Cards/proc_card.dat")
procCard = procTemplate.read()
procTemplate.close()
custoTemplate = open("/cms/heindl/2018/Signal_Gridpacks/ttPhi_Cards/customizecards.dat")
custoCard = custoTemplate.read()
custoTemplate.close()
modelTemplate = open("/cms/heindl/2018/Signal_Gridpacks/ttPhi_Cards/extramodels.dat")
modelCard = modelTemplate.read()
modelTemplate.close()
runTemplate = open("/cms/heindl/2018/Signal_Gridpacks/ttPhi_Cards/run_card_2016.dat")
runCard = runTemplate.read()
runTemplate.close()


mass_list = [("5","5.000000e+00","9.947184e-04"),("10","1.000000e+01","1.989437e-03"),("15","1.500000e+01","2.984155e-03"),("20","2.000000e+01","3.978874e-03"),("25","2.500000e+01","4.973592e-03"),("30","3.000000e+01","5.968310e-03"),("40","4.000000e+01","7.957747e-03"),("50","5.000000e+01","9.947184e-03"),("60","6.000000e+01","1.193662e-02"),("70","7.000000e+01","1.392606e-02"),("75","7.500000e+01","1.492078e-02"),("80","8.000000e+01","1.591549e-02"),("90","9.000000e+01","1.790493e-02"),("100","1.000000e+02","1.989437e-02"),("105","1.050000e+02","2.088909e-02"),("125","1.250000e+02","2.486796e-02"),("150","1.500000e+02","2.984155e-02"),("200","2.000000e+02","3.978874e-02"),("250","2.500000e+02","4.973592e-02"),("300","3.000000e+02","6.012567e-02"),("350","3.500000e+02","2.005429e-01")]

for mass in mass_list:
      print mass[0]+" ("+str(float(mass[1]))+", "+str(float(mass[2]))+")"
      newprocCard_S_2e = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiS_M-"+mass[0]+"_2e/ttPhiS_M-"+mass[0]+"_2e_proc_card.dat",'w+')
      newprocCard_S_2e_1 = procCard.replace("lepton","e")
      newprocCard_S_2e_2 = newprocCard_S_2e_1.replace("outputDir","ttPhiS_M-"+mass[0]+"_2e")
      newprocCard_S_2e.write(newprocCard_S_2e_2)
      newprocCard_S_2e.close()
      newprocCard_S_2mu = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiS_M-"+mass[0]+"_2mu/ttPhiS_M-"+mass[0]+"_2mu_proc_card.dat",'w+')
      newprocCard_S_2mu_1 = procCard.replace("lepton","mu")
      newprocCard_S_2mu_2 = newprocCard_S_2mu_1.replace("outputDir","ttPhiS_M-"+mass[0]+"_2mu")
      newprocCard_S_2mu.write(newprocCard_S_2mu_2)
      newprocCard_S_2mu.close()
      newprocCard_S_2tau = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiS_M-"+mass[0]+"_2tau/ttPhiS_M-"+mass[0]+"_2tau_proc_card.dat",'w+')
      newprocCard_S_2tau_1 = procCard.replace("lepton","ta")
      newprocCard_S_2tau_2 = newprocCard_S_2tau_1.replace("outputDir","ttPhiS_M-"+mass[0]+"_2tau")
      newprocCard_S_2tau.write(newprocCard_S_2tau_2)
      newprocCard_S_2tau.close()
      newprocCard_PS_2e = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiPS_M-"+mass[0]+"_2e/ttPhiPS_M-"+mass[0]+"_2e_proc_card.dat",'w+')
      newprocCard_PS_2e_1 = procCard.replace("lepton","e")
      newprocCard_PS_2e_2 = newprocCard_PS_2e_1.replace("outputDir","ttPhiPS_M-"+mass[0]+"_2e")
      newprocCard_PS_2e.write(newprocCard_PS_2e_2)
      newprocCard_PS_2e.close()
      newprocCard_PS_2mu = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiPS_M-"+mass[0]+"_2mu/ttPhiPS_M-"+mass[0]+"_2mu_proc_card.dat",'w+')
      newprocCard_PS_2mu_1 = procCard.replace("lepton","mu")
      newprocCard_PS_2mu_2 = newprocCard_PS_2mu_1.replace("outputDir","ttPhiPS_M-"+mass[0]+"_2mu")
      newprocCard_PS_2mu.write(newprocCard_PS_2mu_2)
      newprocCard_PS_2mu.close()
      newprocCard_PS_2tau = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiPS_M-"+mass[0]+"_2tau/ttPhiPS_M-"+mass[0]+"_2tau_proc_card.dat",'w+')
      newprocCard_PS_2tau_1 = procCard.replace("lepton","ta")
      newprocCard_PS_2tau_2 = newprocCard_PS_2tau_1.replace("outputDir","ttPhiPS_M-"+mass[0]+"_2tau")
      newprocCard_PS_2tau.write(newprocCard_PS_2tau_2)
      newprocCard_PS_2tau.close()

        
      newcustoCard_S_2e = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiS_M-"+mass[0]+"_2e/ttPhiS_M-"+mass[0]+"_2e_customizecards.dat",'w+')
      newcustoCard_S_2e_1 = custoCard.replace("PhiMass",mass[1])
      newcustoCard_S_2e_2 = newcustoCard_S_2e_1.replace("PhiWidth",mass[2])
      newcustoCard_S_2e_3 = newcustoCard_S_2e_2.replace("PhiStop","1.000000e+00")
      newcustoCard_S_2e_4 = newcustoCard_S_2e_3.replace("PhiPStop","0.000000e+00")
      newcustoCard_S_2e_5 = newcustoCard_S_2e_4.replace("PhiSele","1.000000e-01")
      newcustoCard_S_2e_6 = newcustoCard_S_2e_5.replace("PhiSmu","0.000000e+00")
      newcustoCard_S_2e_7 = newcustoCard_S_2e_6.replace("PhiStau","0.000000e+00")
      newcustoCard_S_2e_8 = newcustoCard_S_2e_7.replace("PhiPSele","0.000000e+00")
      newcustoCard_S_2e_9 = newcustoCard_S_2e_8.replace("PhiPSmu","0.000000e+00")
      newcustoCard_S_2e_10 = newcustoCard_S_2e_9.replace("PhiPStau","0.000000e+00")
      newcustoCard_S_2e.write(newcustoCard_S_2e_10)
      newcustoCard_S_2e.close()
      newcustoCard_S_2mu = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiS_M-"+mass[0]+"_2mu/ttPhiS_M-"+mass[0]+"_2mu_customizecards.dat",'w+')
      newcustoCard_S_2mu_1 = custoCard.replace("PhiMass",mass[1])
      newcustoCard_S_2mu_2 = newcustoCard_S_2mu_1.replace("PhiWidth",mass[2])
      newcustoCard_S_2mu_3 = newcustoCard_S_2mu_2.replace("PhiStop","1.000000e+00")
      newcustoCard_S_2mu_4 = newcustoCard_S_2mu_3.replace("PhiPStop","0.000000e+00")
      newcustoCard_S_2mu_5 = newcustoCard_S_2mu_4.replace("PhiSele","0.000000e+00")
      newcustoCard_S_2mu_6 = newcustoCard_S_2mu_5.replace("PhiSmu","1.000000e-01")
      newcustoCard_S_2mu_7 = newcustoCard_S_2mu_6.replace("PhiStau","0.000000e+00")
      newcustoCard_S_2mu_8 = newcustoCard_S_2mu_7.replace("PhiPSele","0.000000e+00")
      newcustoCard_S_2mu_9 = newcustoCard_S_2mu_8.replace("PhiPSmu","0.000000e+00")
      newcustoCard_S_2mu_10 = newcustoCard_S_2mu_9.replace("PhiPStau","0.000000e+00")
      newcustoCard_S_2mu.write(newcustoCard_S_2mu_10)
      newcustoCard_S_2mu.close()
      newcustoCard_S_2tau = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiS_M-"+mass[0]+"_2tau/ttPhiS_M-"+mass[0]+"_2tau_customizecards.dat",'w+')
      newcustoCard_S_2tau_1 = custoCard.replace("PhiMass",mass[1])
      newcustoCard_S_2tau_2 = newcustoCard_S_2tau_1.replace("PhiWidth",mass[2])
      newcustoCard_S_2tau_3 = newcustoCard_S_2tau_2.replace("PhiStop","1.000000e+00")
      newcustoCard_S_2tau_4 = newcustoCard_S_2tau_3.replace("PhiPStop","0.000000e+00")
      newcustoCard_S_2tau_5 = newcustoCard_S_2tau_4.replace("PhiSele","0.000000e+00")
      newcustoCard_S_2tau_6 = newcustoCard_S_2tau_5.replace("PhiSmu","0.000000e+00")
      newcustoCard_S_2tau_7 = newcustoCard_S_2tau_6.replace("PhiStau","1.000000e-01")
      newcustoCard_S_2tau_8 = newcustoCard_S_2tau_7.replace("PhiPSele","0.000000e+00")
      newcustoCard_S_2tau_9 = newcustoCard_S_2tau_8.replace("PhiPSmu","0.000000e+00")
      newcustoCard_S_2tau_10 = newcustoCard_S_2tau_9.replace("PhiPStau","0.000000e+00")
      newcustoCard_S_2tau.write(newcustoCard_S_2tau_10)
      newcustoCard_S_2tau.close()
      newcustoCard_PS_2e = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiPS_M-"+mass[0]+"_2e/ttPhiPS_M-"+mass[0]+"_2e_customizecards.dat",'w+')
      newcustoCard_PS_2e_1 = custoCard.replace("PhiMass",mass[1])
      newcustoCard_PS_2e_2 = newcustoCard_PS_2e_1.replace("PhiWidth",mass[2])
      newcustoCard_PS_2e_3 = newcustoCard_PS_2e_2.replace("PhiStop","0.000000e+00")
      newcustoCard_PS_2e_4 = newcustoCard_PS_2e_3.replace("PhiPStop","1.000000e+00")
      newcustoCard_PS_2e_5 = newcustoCard_PS_2e_4.replace("PhiSele","0.000000e+00")
      newcustoCard_PS_2e_6 = newcustoCard_PS_2e_5.replace("PhiSmu","0.000000e+00")
      newcustoCard_PS_2e_7 = newcustoCard_PS_2e_6.replace("PhiStau","0.000000e+00")
      newcustoCard_PS_2e_8 = newcustoCard_PS_2e_7.replace("PhiPSele","1.000000e-01")
      newcustoCard_PS_2e_9 = newcustoCard_PS_2e_8.replace("PhiPSmu","0.000000e+00")
      newcustoCard_PS_2e_10 = newcustoCard_PS_2e_9.replace("PhiPStau","0.000000e+00")
      newcustoCard_PS_2e.write(newcustoCard_PS_2e_10)
      newcustoCard_PS_2e.close()
      newcustoCard_PS_2mu = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiPS_M-"+mass[0]+"_2mu/ttPhiPS_M-"+mass[0]+"_2mu_customizecards.dat",'w+')
      newcustoCard_PS_2mu_1 = custoCard.replace("PhiMass",mass[1])
      newcustoCard_PS_2mu_2 = newcustoCard_PS_2mu_1.replace("PhiWidth",mass[2])
      newcustoCard_PS_2mu_3 = newcustoCard_PS_2mu_2.replace("PhiStop","0.000000e+00")
      newcustoCard_PS_2mu_4 = newcustoCard_PS_2mu_3.replace("PhiPStop","1.000000e+00")
      newcustoCard_PS_2mu_5 = newcustoCard_PS_2mu_4.replace("PhiSele","0.000000e+00")
      newcustoCard_PS_2mu_6 = newcustoCard_PS_2mu_5.replace("PhiSmu","0.000000e+00")
      newcustoCard_PS_2mu_7 = newcustoCard_PS_2mu_6.replace("PhiStau","0.000000e+00")
      newcustoCard_PS_2mu_8 = newcustoCard_PS_2mu_7.replace("PhiPSele","0.000000e+00")
      newcustoCard_PS_2mu_9 = newcustoCard_PS_2mu_8.replace("PhiPSmu","1.000000e-01")
      newcustoCard_PS_2mu_10 = newcustoCard_PS_2mu_9.replace("PhiPStau","0.000000e+00")
      newcustoCard_PS_2mu.write(newcustoCard_PS_2mu_10)
      newcustoCard_PS_2mu.close()
      newcustoCard_PS_2tau = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiPS_M-"+mass[0]+"_2tau/ttPhiPS_M-"+mass[0]+"_2tau_customizecards.dat",'w+')
      newcustoCard_PS_2tau_1 = custoCard.replace("PhiMass",mass[1])
      newcustoCard_PS_2tau_2 = newcustoCard_PS_2tau_1.replace("PhiWidth",mass[2])
      newcustoCard_PS_2tau_3 = newcustoCard_PS_2tau_2.replace("PhiStop","0.000000e+00")
      newcustoCard_PS_2tau_4 = newcustoCard_PS_2tau_3.replace("PhiPStop","1.000000e+00")
      newcustoCard_PS_2tau_5 = newcustoCard_PS_2tau_4.replace("PhiSele","0.000000e+00")
      newcustoCard_PS_2tau_6 = newcustoCard_PS_2tau_5.replace("PhiSmu","0.000000e+00")
      newcustoCard_PS_2tau_7 = newcustoCard_PS_2tau_6.replace("PhiStau","0.000000e+00")
      newcustoCard_PS_2tau_8 = newcustoCard_PS_2tau_7.replace("PhiPSele","0.000000e+00")
      newcustoCard_PS_2tau_9 = newcustoCard_PS_2tau_8.replace("PhiPSmu","0.000000e+00")
      newcustoCard_PS_2tau_10 = newcustoCard_PS_2tau_9.replace("PhiPStau","1.000000e-01")
      newcustoCard_PS_2tau.write(newcustoCard_PS_2tau_10)
      newcustoCard_PS_2tau.close()
        
        
      newmodelCard_S_2e = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiS_M-"+mass[0]+"_2e/ttPhiS_M-"+mass[0]+"_2e_extramodels.dat",'w+')
      newmodelCard_S_2e_1 = modelCard
      newmodelCard_S_2e.write(newmodelCard_S_2e_1)
      newmodelCard_S_2e.close()
      newmodelCard_S_2mu = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiS_M-"+mass[0]+"_2mu/ttPhiS_M-"+mass[0]+"_2mu_extramodels.dat",'w+')
      newmodelCard_S_2mu_1 = modelCard
      newmodelCard_S_2mu.write(newmodelCard_S_2mu_1)
      newmodelCard_S_2mu.close()
      newmodelCard_S_2tau = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiS_M-"+mass[0]+"_2tau/ttPhiS_M-"+mass[0]+"_2tau_extramodels.dat",'w+')
      newmodelCard_S_2tau_1 = modelCard
      newmodelCard_S_2tau.write(newmodelCard_S_2tau_1)
      newmodelCard_S_2tau.close()
      newmodelCard_PS_2e = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiPS_M-"+mass[0]+"_2e/ttPhiPS_M-"+mass[0]+"_2e_extramodels.dat",'w+')
      newmodelCard_PS_2e_1 = modelCard
      newmodelCard_PS_2e.write(newmodelCard_PS_2e_1)
      newmodelCard_PS_2e.close()
      newmodelCard_PS_2mu = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiPS_M-"+mass[0]+"_2mu/ttPhiPS_M-"+mass[0]+"_2mu_extramodels.dat",'w+')
      newmodelCard_PS_2mu_1 = modelCard
      newmodelCard_PS_2mu.write(newmodelCard_PS_2mu_1)
      newmodelCard_PS_2mu.close()
      newmodelCard_PS_2tau = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiPS_M-"+mass[0]+"_2tau/ttPhiPS_M-"+mass[0]+"_2tau_extramodels.dat",'w+')
      newmodelCard_PS_2tau_1 = modelCard
      newmodelCard_PS_2tau.write(newmodelCard_PS_2tau_1)
      newmodelCard_PS_2tau.close()
        
      newrunCard_S_2e = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiS_M-"+mass[0]+"_2e/ttPhiS_M-"+mass[0]+"_2e_run_card.dat",'w+')
      newrunCard_S_2e_1 = runCard
      newrunCard_S_2e.write(newrunCard_S_2e_1)
      newrunCard_S_2e.close()
      newrunCard_S_2mu = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiS_M-"+mass[0]+"_2mu/ttPhiS_M-"+mass[0]+"_2mu_run_card.dat",'w+')
      newrunCard_S_2mu_1 = runCard
      newrunCard_S_2mu.write(newrunCard_S_2mu_1)
      newrunCard_S_2mu.close()
      newrunCard_S_2tau = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiS_M-"+mass[0]+"_2tau/ttPhiS_M-"+mass[0]+"_2tau_run_card.dat",'w+')
      newrunCard_S_2tau_1 = runCard
      newrunCard_S_2tau.write(newrunCard_S_2tau_1)
      newrunCard_S_2tau.close()
      newrunCard_PS_2e = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiPS_M-"+mass[0]+"_2e/ttPhiPS_M-"+mass[0]+"_2e_run_card.dat",'w+')
      newrunCard_PS_2e_1 = runCard
      newrunCard_PS_2e.write(newrunCard_PS_2e_1)
      newrunCard_PS_2e.close()
      newrunCard_PS_2mu = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiPS_M-"+mass[0]+"_2mu/ttPhiPS_M-"+mass[0]+"_2mu_run_card.dat",'w+')
      newrunCard_PS_2mu_1 = runCard
      newrunCard_PS_2mu.write(newrunCard_PS_2mu_1)
      newrunCard_PS_2mu.close()
      newrunCard_PS_2tau = open("/cms/heindl/2018/Signal_Gridpacks/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/ttPhi_2016/ttPhiPS_M-"+mass[0]+"_2tau/ttPhiPS_M-"+mass[0]+"_2tau_run_card.dat",'w+')
      newrunCard_PS_2tau_1 = runCard
      newrunCard_PS_2tau.write(newrunCard_PS_2tau_1)
      newrunCard_PS_2tau.close()
        
        
exit(0)