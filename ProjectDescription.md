# Deforestation Alert Prediction: Where are the world's forests at risk? 

###The Question

This exercise attempts to answer the following question:
*Can we predict the areas where large-scale forest clearing is most likely to occur next?* 

The model will be extrapolate forest cover trends within satellite-derived data for 500 meter by 500 meter pixels covering the entire humid tropics. In addition, the model will examine the average evolution of pixel neighborhoods to determine cluster effects of forest change. (Optional): Finally, the model will correlate the relationship between interest and exchange rates to determine if economic changes have impacted rates or location of deforestation in the past, and predict how these factors could drive forest change in the future. 

###The Data

My project draws on data produced by the [**FOrest Monitoring for Action**](https://github.com/wri/forma-clj "FORMA GitHub repo") algorithm, created by the World Resources Institute (WRI) and the Center For Global Development. The automated algorithm utilizes imagery from the Moderate Resolution Imaging Spectroradiometer (MODIS) on NASA's Aqua and Terra satellites to produce forest clearing "alerts" at a 16-day, 500 m resolution, beginning in December 2005. The algorithm combines three time series data sets[^f1]:

1. Normalized Difference Vegetation Index (NDVI) from the MODIs Terra 500m vegetation incides product
2. Rainfall data from the Precipitation Reconstruction over Land data set, and
3. Daily active fire detections identified by NASA's Fire Information and Resource Management System (FIRMS). 

The output is a continuous probability every 16 days which represents the likelihood that large-scale industrial clearing has occured within each 500 m pixel. I will utilize these probability time series as explanatory variables in order to predict individual pixel probabilities that will result from the next 1-3 iterations of the algorithm. 

I will train and test the prediction model for the provinces of **Riau, Sumatra, West and Central Kalimantan** in Indonesia, where preliminary accuracy assessments using higher resolution forest change data indicate high reliability for FORMA (Wheeler, Petersen and Harris, forthcoming). 

*NB: FORMA has an inherent 2-3 week lag, due to the time delay in the precipitation and NDVI data. Thus, a prediction for the next 16-days actually represents a picture of "right this moment." Similarly, a prediction of probabilities for the next 32 days represents the likelihood of clearing 16 days from "right this moment."* 

These forest clearing alerts are time-enabled and visualized as binary yes/no on the forest monitoring platform [Global Forest Watch](www.globalforestwatch.org), imposing a 50% probability minimum. However, the underlying continuous probabilities for each pixel are stored as ASCII files in a WRI Amazon S3 server, and will be accessed and utilized for this project. A sample data set has been uploaded to my GitHub repository [here](https://github.com/rachnp89/DAT5-Project/blob/master/data/sample_FORMA_prob.txt).

Historical interest and exchange data for Indonesia will be accessed via the [Trading Economics API](www.tradingeconomics.com).

[^f1]: To learn more about the FORMA algorithm and methodology, please see [(Hammer et al, 2014)](http://www.sciencedirect.com/science/article/pii/S0303243414000956)
 
###The Context
We're losing the world's forests at an alarming rate -- nearly 50 soccer fields per minute, according to the [latest data](http://www.wri.org/blog/2013/11/new-high-resolution-forest-maps-reveal-world-loses-50-soccer-fields-trees-minute). But prior to the advent of earth observation technologies, it was impossible to know -- at scale -- exactly where forests existed, how quickly they were changing and why. Recent technological developments, such as the availability of satellite data, including the USGS Landsat Archive, as well as decreasing computing costs, have enabled more real-time, accurate data about the world's natural resources. 

Countries are beginning to put this information into action. Brazil, for example, reduced deforestation rates in the Amazon by 70% since the 1980s, due in large part to its satellite monitoring systems. However, for many governments, investors and companies, even relatively recent data is insufficient . Many stakeholders require predictive insights, such as deforestation risk maps, that allow them to move from reactive measures to preventatives policies. These stakeholders include: 

1. **Governments**: Greenhouse gas emissions from land use change account for Under the [UN Framework Convention on Climate Change](http://unfccc.int/land_use_and_climate_change/redd/items/7377.php), countries can receive payments for preserving the carbon stored in forests. Howevever, these countries must prove "additionality" -- that is, demonstrate that in the absence of such payments and incentives, deforestation would have taken place. These countries require simple, cost-effective mechanisms to predict deforestation risk based on historical rates of change. A deforestation alert predictor could be a useful tool in 

2. **Bilateral and multilateral donors**:It's not easy -- or cheap -- being green. Many countries require significant incentives to shift the market signals away from exploiting their remaining primary forests. The Norwegian government alone has pledged, and in 2011 began to dispense, over [3.5 billion US dollars](http://www.cgdev.org/blog/norways-rainforest-billions-how-did-stars-align) in aid initiatives to halt tropical deforestation. The World Bank also allocates funds to programs aimed at preserving forests. These donor governments need to not only assess the efficacy of previous and ongoing interventions, but also target funds to regions that face the most risk of deforesting in the future. 

3. **Companies**: Commercial agricultural drives at least two-thirds of the world's deforestation. However, commodity giants such Nestle, Unilever, P&G, Mars, and others -- a group worth nearly [4 trillion US dollars](http://www.supply-change.org/) -- have pledged to reverse their role in habitat destruction. In order to comply with so-called "zero-deforestation commitments," these companies need to identify potentially high-risk areas to avoid when making sourcing and purchasing decisions. 

My forest clearing alert prediction model -- while limited in scope -- could leverage the underlying richness and complexity of the FORMA algorithm to predict the next output of probabilities, and thus areas experience high likelihood of deforestation in the future. These insights are critical to help us better identify, anticipate, and even prevent the negative impacts of forest loss. 

*Below, FORMA forest clearing alerts as visualized on Global Forest Watch.*   

![](http://i.imgur.com/0ZsFmzB.png)

