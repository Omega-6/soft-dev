from flask import Flask, render_template
import pandas as pd
import sys as sys

app = Flask(__name__)

@app.route('/')
def home():

    #inputs
    # wantedSow = "April, May"
    # wantedHarvest = "June, July"
    # location = "Chester Springs"
    # soilPh = 7.0
    # weather = 60.0
    # previousPlants = ["Peppers", "Eggplant", "Beets"]
    # soilNit = 40 #kg/ha
    # soilPho = 30 #kg/ha
    # soilPot = 55 #kg/ha
    # waterLevel = 350 #mm
    # rainfall = True
    # irrigated = True
    # groundwater = False 
    # surfacewater = False


    wantedSow = str(input("When do you want to plant your crops?"))
    wantedHarvest = str(input("When do you want to harvest your crops?"))
    location = str(input("Where is your farm located?"))
    soilPh = float(input("What is the pH of your soil?"))
    weather = float(input("What is the temperature currently"))
    previousPlantsInput = str(input("What plants have you planted in the last year?"))
    previousPlants = previousPlantsInput.split(", ")
    soilNit = int(input("What is the Nitrogen level of your soil(kg/ha)?"))
    soilPho = int(input("What is the Phospherous level of your soil(kg/ha)?"))
    soilPot = int(input("What is the Potasium level of your soil(kg/ha)?"))
    waterLevel = int(input("What is the water level of your soil(mm)?"))
    rainfall = bool(input("Do you get rainfall?"))
    irrigated = bool(input("Do you have irrigation?"))
    groundwater = bool(input("Do you have groundwater?")) 
    surfacewater = bool(input("Do you have surface water?"))


    #outputs
    plantPoints = {
        "Peas" : 0,
        "Fava Beans" : 0,
        "Onions" : 0,
        "Leeks" : 0,
        "Garlic" : 0,
        "Greens(Collards,Kale,Mustard)" : 0,
        "Turnips" : 0,
        "White Potatoes" : 0,
        "Cabbage" : 0,
        "Lettuce" : 0,
        "Radishes" : 0,
        "Beets" : 0,
        "Carrots" : 0,
        "Shallots" : 0,
        "Spinach" : 0,
        "Bok Choy" : 0,
        "Parsley" : 0,
        "Swiss Chard" : 0,
        "Celery" : 0,
        "Watermelons" : 0,
        "Winter Squash" : 0,
        "Melons" : 0,
        "Summer Squash" : 0,
        "Cucumbers" : 0,
        "Pumpkins" : 0,
        "Sweet Potatoes" : 0,
        "Okra" : 0,
        "Chinese Cabbage" : 0,
        "Sweet Corn" : 0,
        "Peanuts" : 0,
        "Lima Beans" : 0,
        "Beans (Bush,Pole,Shell,Dried)" : 0,
        "Black-Eyed Peas" : 0,
        "Eggplant" : 0,
        "Peppers" : 0,
        "Tomato" : 0,
        "Basil" : 0,
        "Gandules (Pigeon Peas)" : 0
    }
    sugPlants = []

    timeToCrops = pd.read_excel('data/timeToCrops.xlsx', engine='openpyxl') 
    waterToCrops = pd.read_excel('data/waterToCrops.xlsx', engine='openpyxl') 
    carbonFootprintReduction = pd.read_excel('data/carbonFootprintReduction.xlsx', engine='openpyxl') 
    composting = pd.read_excel('data/composting.xlsx', engine='openpyxl') 
    coverCrops = pd.read_excel('data/coverCrops.xlsx', engine='openpyxl') 
    cropRotationCycle = pd.read_excel('data/cropRotationCycle.xlsx', engine='openpyxl') 
    mulching = pd.read_excel('data/mulching.xlsx', engine='openpyxl') 
    nutrientsToCrops = pd.read_excel('data/nutrientsToCrops.xlsx', engine='openpyxl') 
    pestAndDiseasePrevention = pd.read_excel('data/pestAndDiseasePrevention.xlsx', engine='openpyxl') 
    phToCrops = pd.read_excel('data/phToCrops.xlsx', engine='openpyxl') 
    soilAmendments = pd.read_excel('data/soilAmendments.xlsx', engine='openpyxl') 
    timeToSowAndHarvest = pd.read_excel('data/timeToSowAndHarvest.xlsx', engine='openpyxl') 
    weatherToCrops = pd.read_excel('data/weatherToCrops.xlsx', engine='openpyxl') 
    weatherToSowAndHarvest = pd.read_excel('data/weatherToSowAndHarvest.xlsx', engine='openpyxl') 
   

    timeToCropsTable = timeToCrops.to_html(classes='table table-bordered')
    waterToCropsTable = waterToCrops.to_html(classes='table table-bordered')
    carbonFootprintReductionTable = carbonFootprintReduction.to_html(classes='table table-bordered')
    compostingTable = composting.to_html(classes='table table-bordered')
    coverCropsTable = coverCrops.to_html(classes='table table-bordered')
    cropRotationCycleTable = cropRotationCycle.to_html(classes='table table-bordered')
    mulchingTable = mulching.to_html(classes='table table-bordered')
    nutrientsToCropsTable = nutrientsToCrops.to_html(classes='table table-bordered')
    pestAndDiseasePreventionTable = pestAndDiseasePrevention.to_html(classes='table table-bordered')
    phToCropsTable = phToCrops.to_html(classes='table table-bordered')
    soilAmendmentsTable = soilAmendments.to_html(classes='table table-bordered')
    timeToSowAndHarvestTable = timeToSowAndHarvest.to_html(classes='table table-bordered')
    weatherToCropsTable = weatherToCrops.to_html(classes='table table-bordered')
    weatherToSowAndHarvestTable = weatherToSowAndHarvest.to_html(classes='table table-bordered')
  
   # print("Time to Crops Table:\n", timeToCrops)
   # print("Water to Crops Table:\n", waterToCrops)
    # phCrops = []
    # for ph in range(len(phToCrops)):
    #     #print(str(phToCrops.iloc[ph, 2]) + " - " + str(soilPh) + " - " + str(phToCrops.iloc[ph, 3]))
    #     if phToCrops.iloc[ph, 2] <= soilPh:
    #         if phToCrops.iloc[ph, 3] >= soilPh:
    #             #print(phToCrops.iloc[ph, 0])
    #             phCrops.append(phToCrops.iloc[ph, 0])
    # print("pH - ")
    # print(phCrops)

    phCrops = phToCrops[(phToCrops["Low pH Acceptable"] <= soilPh) & (phToCrops["High pH Acceptable"] >= soilPh)]

    print("ph")
    print(phCrops)


    #nutrients
    nitCrops = nutrientsToCrops[(nutrientsToCrops["Nitrogen (N) Low"] <= soilNit) & (nutrientsToCrops["Nitrogen (N) High"] >= soilNit)]
    phoCrops = nutrientsToCrops[(nutrientsToCrops["Phosphorus (P) Low"] <= soilPho) & (nutrientsToCrops["Phosphorus (P) High"] >= soilPho)]
    potCrops = nutrientsToCrops[(nutrientsToCrops["Potassium (K) Low"] <= soilPot) & (nutrientsToCrops["Potassium (K) High"] >= soilPot)]


    # for nit in range(len(nutrientsToCrops)):
    #     if nutrientsToCrops.iloc[nit, 1] <= soilNit:
    #         if nutrientsToCrops.iloc[nit, 2] >= soilNit:
    #             #print(phToCrops.iloc[nit, 0])
    #             nitCrops.append(nutrientsToCrops.iloc[nit, 0])
    print("Nitrogen - ")
    print(nitCrops)
    # for pho in range(len(nutrientsToCrops)):
    #     if nutrientsToCrops.iloc[pho, 3] <= soilPho:
    #         if nutrientsToCrops.iloc[pho, 4] >= soilPho:
    #             #print(phToCrops.iloc[pho, 0])
    #             phoCrops.append(nutrientsToCrops.iloc[pho, 0])
    print("Phosphorus - ")
    print(phoCrops)
    # for pot in range(len(nutrientsToCrops)):
    #     if nutrientsToCrops.iloc[pot, 5] <= soilPot:
    #         if nutrientsToCrops.iloc[pot, 6] >= soilPot:
    #             #print(phToCrops.iloc[pot, 0])
    #             potCrops.append(nutrientsToCrops.iloc[pot, 0])
    print("Potasium - ")
    print(potCrops)

    waterAmountCrops = waterToCrops[(waterToCrops["Min Water (mm)"] <= waterLevel) & (waterToCrops["Max Water (mm)"] >= waterLevel)]
    # for waterAmount in range(len(waterToCrops)):
    #     #print(str(waterToCrops.iloc[waterAmount, 1]) + " - " + str(waterLevel) + " - " + str(waterToCrops.iloc[waterAmount, 2]))
    #     if waterToCrops.iloc[waterAmount, 1] <= waterLevel:
    #         if waterToCrops.iloc[waterAmount, 2] >= waterLevel:
    #             #print(waterToCrops.iloc[waterAmount, 0])
    #             waterAmountCrops.append(waterToCrops.iloc[waterAmount, 0])
    print("water amount - ")
    print(waterAmountCrops)

    rainfallCrops = pd.DataFrame()
    if rainfall == True:
            rainfallCrops = waterToCrops[waterToCrops["Rainfall"] == True]

        # for rain in range(len(waterToCrops)):
        #     #print(str(waterToCrops.iloc[rain, 1]) + " - " + str(waterLevel) + " - " + str(waterToCrops.iloc[rain, 2]))
        #     if waterToCrops.iloc[rain, 3] == rainfall:
        #         #print(waterToCrops.iloc[rain, 0])
        #         rainfallCrops.append(waterToCrops.iloc[rain, 0])
    
    print("rainfall - ")
    print(rainfallCrops)
    

    irrigatedCrops = pd.DataFrame()
    if irrigated == True:
        irrigatedCrops = waterToCrops[waterToCrops["Irrigated"] == True]

        # for irri in range(len(waterToCrops)):
        #     #print(str(waterToCrops.iloc[irri, 1]) + " - " + str(waterLevel) + " - " + str(waterToCrops.iloc[irri, 2]))
        #     if waterToCrops.iloc[irri, 4] == irrigated:
        #         #print(waterToCrops.iloc[irri, 0])
        #         irrigatedCrops.append(waterToCrops.iloc[irri, 0])
    
    print("irrigated - ")
    print(irrigatedCrops)

    groundwaterCrops = pd.DataFrame()
    if groundwater == True:
        groundwaterCrops = waterToCrops[waterToCrops["Groundwater"] == True]

        # for ground in range(len(waterToCrops)):
        #     #print(str(waterToCrops.iloc[ground, 1]) + " - " + str(waterLevel) + " - " + str(waterToCrops.iloc[ground, 2]))
        #     if waterToCrops.iloc[ground, 5] == groundwater:
        #         #print(waterToCrops.iloc[ground, 0])
        #         groundwaterCrops.append(waterToCrops.iloc[ground, 0])
    
    print("groundwater - ")
    print(groundwaterCrops)

    surfacewaterCrops = pd.DataFrame()
    if surfacewater == True:
        surfacewaterCrops = waterToCrops[waterToCrops["Surface Water"] == True]
        # for surface in range(len(waterToCrops)):
        #     #print(str(waterToCrops.iloc[surface, 1]) + " - " + str(waterLevel) + " - " + str(waterToCrops.iloc[surface, 2]))
        #     if waterToCrops.iloc[surface, 6] == surfacewater:
        #         #print(waterToCrops.iloc[surface, 0])
        #         surfacewaterCrops.append(waterToCrops.iloc[surface, 0])
    print("surfacewater - ")
    print(surfacewaterCrops)

    rainTypeCrops = pd.concat([rainfallCrops, irrigatedCrops, groundwaterCrops, surfacewaterCrops])
    rainTypeCrops = rainTypeCrops.drop_duplicates()
    # for rainType in range(len(waterToCrops)):
    #     if waterToCrops.iloc[rainType, 0] in rainfallCrops or waterToCrops.iloc[rainType, 0] in irrigatedCrops or waterToCrops.iloc[rainType, 0] in surfacewaterCrops or waterToCrops.iloc[rainType, 0] in groundwaterCrops:
    #             rainTypeCrops.append(waterToCrops.iloc[rainType, 0])
    print("rain Type - ")
    print(rainTypeCrops)
    # cropRotationCycle.columns = cropRotationCycle.columns.str.strip()
    cropRotationCycleCrops = []
    cropRotationCycleCropsTemp = []
    print(cropRotationCycle["Crops to Plant"])
    for prev in previousPlants:
        print(prev)
        cropRotationCycleCropsTemp.append(cropRotationCycle[cropRotationCycle["Crops to Plant"].str.contains(prev, case=False)])
        print(cropRotationCycleCropsTemp)
    print("crop rotataions - ")
    cropRotationCycleCropsYears = []
    for crcIndex in cropRotationCycleCropsTemp:
        cropRotationCycleCropsYears.append(crcIndex.iloc[0, 0])
    # print(cropRotationCycleCrops[0].iloc[0, 0])
    # print(cropRotationCycleCrops[1].iloc[0, 0])
    # print(cropRotationCycleCrops[2].iloc[0, 0])
    # print(cropRotationCycleCrops[3].iloc[0, 0])
    print(cropRotationCycleCropsYears)
    y1 = cropRotationCycleCropsYears.count("Year 1")
    y2 = cropRotationCycleCropsYears.count("Year 2")
    y3 = cropRotationCycleCropsYears.count("Year 3")
    y4 = cropRotationCycleCropsYears.count("Year 4")
    print(y1)
    print(y2)
    print(y3)
    print(y4)

    if y1 >= y2 and y1 >= y3 and y1 >= y4:
        splitCropsOfYears = cropRotationCycle.iloc[1, 2].split(", ")
        for yearIndex in splitCropsOfYears:
            cropRotationCycleCrops.append(yearIndex)
            print(cropRotationCycleCrops)
    if y2 >= y1 and y2 >= y3 and y2 >= y4:
        splitCropsOfYears = cropRotationCycle.iloc[2, 2].split(", ")
        for yearIndex in splitCropsOfYears:
            cropRotationCycleCrops.append(yearIndex)
            print(cropRotationCycleCrops)
    if y3 >= y1 and y3>= y2 and y3 >= y4:
        splitCropsOfYears = cropRotationCycle.iloc[3, 2].split(", ")
        for yearIndex in splitCropsOfYears:
            cropRotationCycleCrops.append(yearIndex)
            print(cropRotationCycleCrops)
    if y4 >= y1 and y4 >= y2 and y4 >= y3:
        splitCropsOfYears = cropRotationCycle.iloc[0, 2].split(", ")
        for yearIndex in splitCropsOfYears:
            cropRotationCycleCrops.append(yearIndex)
            print(cropRotationCycleCrops)
    print("sow - ")
    listOfSow = wantedSow.split(", ")

    # sowTimeCrops = []
    # for sowIndexer in listOfSow:
    #     sowTimeCrops.append(timeToSowAndHarvest[timeToSowAndHarvest["Sowing Time"].str.contains(sowIndexer, case=False)])    
    # print(sowTimeCrops)
    # print("harvest - ")

    sowTimeCrops = pd.DataFrame()
    for sowIndexer in listOfSow:
        tempDF = timeToSowAndHarvest[timeToSowAndHarvest["Sowing Time"].str.contains(sowIndexer, case=False)]
        sowTimeCrops = pd.concat([sowTimeCrops, tempDF])
    sowTimeCrops = sowTimeCrops.drop_duplicates()
    print(sowTimeCrops)

    print("harvest - ")
    listOfHarevst = wantedHarvest.split(", ")

    # harvestTimeCrops = []
    # for harvestIndexer in listOfHarevst:
    #     harvestTimeCrops.append(timeToSowAndHarvest[timeToSowAndHarvest["Harvest Time"].str.contains(harvestIndexer, case=False)])    
    # print(harvestTimeCrops)

    harvestTimeCrops = pd.DataFrame()
    for harvestIndexer in listOfHarevst:
        tempDF = timeToSowAndHarvest[timeToSowAndHarvest["Harvest Time"].str.contains(harvestIndexer, case=False)]
        harvestTimeCrops = pd.concat([harvestTimeCrops, tempDF])
    harvestTimeCrops = harvestTimeCrops.drop_duplicates()
    print(harvestTimeCrops)

    print(plantPoints)
    print("crc updating - ")
    for updatesCRC in cropRotationCycleCrops:
        plantPoints[updatesCRC] += 10
    print(plantPoints)

    print("ph updating - ")
    phCropsList = phCrops['Crop'].tolist()
    for updatesPh in phCropsList:
        plantPoints[updatesPh] += 8
    print(plantPoints)

    print("nit updating - ")
    nitCropsList = nitCrops['Crop'].tolist()
    for updatesNit in nitCropsList:
        plantPoints[updatesNit] += 10
    print(plantPoints)

    print("pot updating - ")
    potCropsList = potCrops['Crop'].tolist()
    for updatesPot in potCropsList:
        plantPoints[updatesPot] += 9
    print(plantPoints)

    print("pho updating - ")
    phoCropsList = phoCrops['Crop'].tolist()
    for updatesPho in phoCropsList:
        plantPoints[updatesPho] += 9
    print(plantPoints)

    print("water amount updating - ")
    waterAmountCropsList = waterAmountCrops['Crop'].tolist()
    for updatesWaterAmount in waterAmountCropsList:
        plantPoints[updatesWaterAmount] += 10
    print(plantPoints)

    print("water type updating - ")
    waterTypeCropsList = rainTypeCrops['Crop'].tolist()
    for updatesWaterType in waterTypeCropsList:
        plantPoints[updatesWaterType] += 7
    print(plantPoints)

    print("sow updating - ")
    sowTimeCropsList = sowTimeCrops['Crop Name'].tolist()
    for updatesSow in sowTimeCropsList:
        plantPoints[updatesSow] += 8
    print(plantPoints)

    print("harvest updating - ")
    harvestTimeCropsList = harvestTimeCrops['Crop Name'].tolist()
    for updatesHarvest in harvestTimeCropsList:
        plantPoints[updatesHarvest] += 7
    print(plantPoints)
    sortedPlantPoints = {k: v for k, v in sorted(plantPoints.items(), key=lambda item: item[1], reverse=True)}

    #sortedPlantPoints = list(sorted(plantPoints.keys()))
    print(sortedPlantPoints)
    for finalSuggestions in range(0, 7):
        sugPlants = list(sortedPlantPoints.keys())
        print(sugPlants)

    print("- = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = ")
    print(sugPlants[:7])


    return(sugPlants[:7])

if __name__ == '__main__':
    app.run(debug=True)
