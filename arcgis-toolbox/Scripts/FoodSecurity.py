#Import modulesimport sysimport osimport numpy as npimport pandas as pdimport pygalimport arcpyimport eeimport datetimearcpy.env.overwriteOutput = Truearcpy.env.outputCoordinateSystem = arcpy.SpatialReference(3857)def plotFAO(df, iso_code, fao_indicator, itemCodeFS, countrySelection, outputLocation):	arcpy.AddMessage("in fao function")	#Select the appropriate indicator	df_selected = df[df["Item Code"] == itemCodeFS]		#color code for plots	customColorStyle = pygal.style.Style(colors = ['#D35400', '#979A9A', '#797D7F', '#5F6A6A', '#515A5A'], title_font_size = 18)		if itemCodeFS == 21010:		#Create the line chart plot		line_chart = pygal.Line(title = u"Average Dietary Energy Supply Adequacy - \n" + countrySelection, x_title = "End Year of '3-Year Average'", y_title = "% - 3-Year Average", style = customColorStyle, show_dots = False, stroke_style = {'width': 3}, show_minor_y_labels = True)		#line_chart.x_labels = map(str, range(2001, 2018))				arcpy.AddMessage("made it here")				#Get just the Value column for the country of interest and the country groupings		country_series = df_selected.loc[df_selected["ISO_code"] == iso_code, "Value"]				arcpy.AddMessage("made it here2")				#Some countries have no data for some indicators		if country_series.isnull().values.all():			arcpy.AddMessage(countrySelection + " has no data for this food security indicator.")			return None				if country_series.iloc[0] >= 0:			country_series = country_series			xlabels = range(2001, 2018)		else:			years = range(2001, 2018)			strippedDF = pd.DataFrame({'values': country_series, 'year': years})			arcpy.AddMessage("God Damn It")			strippedDF = strippedDF[np.isfinite(strippedDF['values'])]			arcpy.AddMessage("Fuck!")			country_series = strippedDF['values']			years = strippedDF['year']			arcpy.AddMessage("Fuckoff")			arcpy.AddMessage("Get fucked")			xlabels = years			arcpy.AddMessage(xlabels)			arcpy.AddMessage(country_series)				arcpy.AddMessage("made it here3")				low_income_series = df_selected.loc[df_selected["ISO_code"] == "lowestIncome", "Value"]				arcpy.AddMessage("made it here4")				mid_lower_income_series = df_selected.loc[df_selected["ISO_code"] == "midLowerIncome", "Value"]				arcpy.AddMessage("made it here5")				mid_upper_income_series = df_selected.loc[df_selected["ISO_code"] == "midUpperIncome", "Value"]				arcpy.AddMessage("made it here6")				high_income_series = df_selected.loc[df_selected["ISO_code"] == "uppermostIncome", "Value"]				arcpy.AddMessage("made it here7")				#Add Pd Series to the line chart		line_chart.add(countrySelection, country_series)				arcpy.AddMessage("made it here8")				line_chart.add("Low-Income", low_income_series)				arcpy.AddMessage("made it here9")				line_chart.add("Lower-Middle-Income", mid_lower_income_series)				arcpy.AddMessage("made it here10")				line_chart.add("Upper-Middle-Income", mid_upper_income_series)				arcpy.AddMessage("made it here11")				line_chart.add("High-Income", high_income_series)				arcpy.AddMessage("made it here12")				#Add x labels		#xlabels = range(2001, 2018)		line_chart.x_labels = map(str, xlabels)				#Output the plot		line_chart.render_to_file(os.path.join(outputLocation, 'FAO_plot.svg'))				arcpy.AddMessage("should have outputted something")		if itemCodeFS == 21011:		#Creat the line chart plot		line_chart = pygal.Line(title = u"Average Value of Food Production - \n" + countrySelection, x_title = "End Year of '3-Year Average'", y_title = "Constant International Dollars Per Person - 3-Year Average", style = customColorStyle, show_dots = False, stroke_style = {'width': 3}, show_minor_y_labels = True)		line_chart.x_labels = map(str, range(2001, 2018))		#Get just the Value column for the country of interest and the country groupings		country_series = df_selected.loc[df_selected["ISO_code"] == iso_code, "Value"]		#Some countries have no data for some indicators		if country_series.isnull().values.all():			arcpy.AddMessage(countrySelection + " has no data for this food security indicator.")			return None		low_income_series = df_selected.loc[df_selected["ISO_code"] == "lowestIncome", "Value"]		mid_lower_income_series = df_selected.loc[df_selected["ISO_code"] == "midLowerIncome", "Value"]		mid_upper_income_series = df_selected.loc[df_selected["ISO_code"] == "midUpperIncome", "Value"]		high_income_series = df_selected.loc[df_selected["ISO_code"] == "uppermostIncome", "Value"]		#Add Pd Series to the line chart		line_chart.add(countrySelection, country_series)		line_chart.add("Low-Income", low_income_series)		line_chart.add("Lower-Middle-Income", mid_lower_income_series)		line_chart.add("Upper-Middle-Income", mid_upper_income_series)		line_chart.add("High-Income", high_income_series)		#Output the plot		line_chart.render_to_file(os.path.join(outputLocation, 'FAO_plot.svg'))		if itemCodeFS == 21012:		#Creat the line chart plot		line_chart = pygal.Line(title = u"Share of Dietary Energy Supply Derived from Cereals, Roots, and Tubers - \n" + countrySelection, x_title = "End Year of '3-Year Average'", y_title = "% - 3-Year Average", style = customColorStyle, show_dots = False, stroke_style = {'width': 3}, show_minor_y_labels = True)		line_chart.x_labels = map(str, range(2001, 2018))		#Get just the Value column for the country of interest and the country groupings		country_series = df_selected.loc[df_selected["ISO_code"] == iso_code, "Value"]		#Some countries have no data for some indicators		if country_series.isnull().values.all():			arcpy.AddMessage(countrySelection + " has no data for this food security indicator.")			return None		low_income_series = df_selected.loc[df_selected["ISO_code"] == "lowestIncome", "Value"]		mid_lower_income_series = df_selected.loc[df_selected["ISO_code"] == "midLowerIncome", "Value"]		mid_upper_income_series = df_selected.loc[df_selected["ISO_code"] == "midUpperIncome", "Value"]		high_income_series = df_selected.loc[df_selected["ISO_code"] == "uppermostIncome", "Value"]		#Add Pd Series to the line chart		line_chart.add(countrySelection, country_series)		line_chart.add("Low-Income", low_income_series)		line_chart.add("Lower-Middle-Income", mid_lower_income_series)		line_chart.add("Upper-Middle-Income", mid_upper_income_series)		line_chart.add("High-Income", high_income_series)		#Output the plot		line_chart.render_to_file(os.path.join(outputLocation, 'FAO_plot.svg'))		if itemCodeFS == 21013:		#Creat the line chart plot		line_chart = pygal.Line(title = u"Average Protein Supply - \n" + countrySelection, x_title = "End Year of '3-Year Average'", y_title = "Grams per Capita per Day - 3-Year Average", style = customColorStyle, show_dots = False, stroke_style = {'width': 3}, show_minor_y_labels = True)		line_chart.x_labels = map(str, range(2001, 2018))		#Get just the Value column for the country of interest and the country groupings		country_series = df_selected.loc[df_selected["ISO_code"] == iso_code, "Value"]		#Some countries have no data for some indicators		if country_series.isnull().values.all():			arcpy.AddMessage(countrySelection + " has no data for this food security indicator.")			return None		low_income_series = df_selected.loc[df_selected["ISO_code"] == "lowestIncome", "Value"]		mid_lower_income_series = df_selected.loc[df_selected["ISO_code"] == "midLowerIncome", "Value"]		mid_upper_income_series = df_selected.loc[df_selected["ISO_code"] == "midUpperIncome", "Value"]		high_income_series = df_selected.loc[df_selected["ISO_code"] == "uppermostIncome", "Value"]		#Add Pd Series to the line chart		line_chart.add(countrySelection, country_series)		line_chart.add("Low-Income", low_income_series)		line_chart.add("Lower-Middle-Income", mid_lower_income_series)		line_chart.add("Upper-Middle-Income", mid_upper_income_series)		line_chart.add("High-Income", high_income_series)		#Output the plot		line_chart.render_to_file(os.path.join(outputLocation, 'FAO_plot.svg'))		if itemCodeFS == 21014:		#Creat the line chart plot		line_chart = pygal.Line(title = u"Average Supply of Protein of Animal Origin - \n" + countrySelection, x_title = "End Year of '3-Year Average'", y_title = "Grams per Capita per Day - 3-Year Average", style = customColorStyle, show_dots = False, stroke_style = {'width': 3}, show_minor_y_labels = True)		line_chart.x_labels = map(str, range(2001, 2018))		#Get just the Value column for the country of interest and the country groupings		country_series = df_selected.loc[df_selected["ISO_code"] == iso_code, "Value"]		#Some countries have no data for some indicators		if country_series.isnull().values.all():			arcpy.AddMessage(countrySelection + " has no data for this food security indicator.")			return None		low_income_series = df_selected.loc[df_selected["ISO_code"] == "lowestIncome", "Value"]		mid_lower_income_series = df_selected.loc[df_selected["ISO_code"] == "midLowerIncome", "Value"]		mid_upper_income_series = df_selected.loc[df_selected["ISO_code"] == "midUpperIncome", "Value"]		high_income_series = df_selected.loc[df_selected["ISO_code"] == "uppermostIncome", "Value"]		#Add Pd Series to the line chart		line_chart.add(countrySelection, country_series)		line_chart.add("Low-Income", low_income_series)		line_chart.add("Lower-Middle-Income", mid_lower_income_series)		line_chart.add("Upper-Middle-Income", mid_upper_income_series)		line_chart.add("High-Income", high_income_series)		#Output the plot		line_chart.render_to_file(os.path.join(outputLocation, 'FAO_plot.svg'))		if itemCodeFS == 21016:		#Creat the line chart plot		line_chart = pygal.Line(title = u"Rail-Lines Density - \n" + countrySelection, x_title = "Year", y_title = "Density per 100 Square Kilometer of Land Area", style = customColorStyle, show_dots = False, stroke_style = {'width': 3}, show_minor_y_labels = True)		line_chart.x_labels = map(str, range(2000, 2017))		#Get just the Value column for the country of interest and the country groupings		country_series = df_selected.loc[df_selected["ISO_code"] == iso_code, "Value"]		#Some countries have no data for some indicators		if country_series.isnull().values.all():			arcpy.AddMessage(countrySelection + " has no data for this food security indicator.")			return None		low_income_series = df_selected.loc[df_selected["ISO_code"] == "lowestIncome", "Value"]		mid_lower_income_series = df_selected.loc[df_selected["ISO_code"] == "midLowerIncome", "Value"]		mid_upper_income_series = df_selected.loc[df_selected["ISO_code"] == "midUpperIncome", "Value"]		high_income_series = df_selected.loc[df_selected["ISO_code"] == "uppermostIncome", "Value"]		#Add Pd Series to the line chart		line_chart.add(countrySelection, country_series)		line_chart.add("Low-Income", low_income_series)		line_chart.add("Lower-Middle-Income", mid_lower_income_series)		line_chart.add("Upper-Middle-Income", mid_upper_income_series)		line_chart.add("High-Income", high_income_series)		#Output the plot		line_chart.render_to_file(os.path.join(outputLocation, 'FAO_plot.svg'))		if itemCodeFS == 22013:		#Creat the line chart plot		line_chart = pygal.Line(title = u"Gross Domestic Product per Capita, PPP - \n" + countrySelection, x_title = "Year", y_title = "Constant 2011 International Dollars", style = customColorStyle, show_dots = False, stroke_style = {'width': 3}, show_minor_y_labels = True)		line_chart.x_labels = map(str, range(2000, 2017))		#Get just the Value column for the country of interest and the country groupings		country_series = df_selected.loc[df_selected["ISO_code"] == iso_code, "Value"]		#Some countries have no data for some indicators		if country_series.isnull().values.all():			arcpy.AddMessage(countrySelection + " has no data for this food security indicator.")			return None		low_income_series = df_selected.loc[df_selected["ISO_code"] == "lowestIncome", "Value"]		mid_lower_income_series = df_selected.loc[df_selected["ISO_code"] == "midLowerIncome", "Value"]		mid_upper_income_series = df_selected.loc[df_selected["ISO_code"] == "midUpperIncome", "Value"]		high_income_series = df_selected.loc[df_selected["ISO_code"] == "uppermostIncome", "Value"]		#Add Pd Series to the line chart		line_chart.add(countrySelection, country_series)		line_chart.add("Low-Income", low_income_series)		line_chart.add("Lower-Middle-Income", mid_lower_income_series)		line_chart.add("Upper-Middle-Income", mid_upper_income_series)		line_chart.add("High-Income", high_income_series)		#Output the plot		line_chart.render_to_file(os.path.join(outputLocation, 'FAO_plot.svg'))		if itemCodeFS == 21004:		#Creat the line chart plot		line_chart = pygal.Line(title = "Prevalence of Undernourishment - \n" + countrySelection, x_title = "End Year of '3-Year Average'", y_title = "% - 3-Year Average", style = customColorStyle, show_dots = False, stroke_style = {'width': 3}, show_minor_y_labels = True)		line_chart.x_labels = map(str, range(2001, 2018))		#Get just the Value column for the country of interest and the country groupings		country_series = df_selected.loc[df_selected["ISO_code"] == iso_code, "Value"]		#Some countries have no data for some indicators		if country_series.isnull().values.all():			arcpy.AddMessage(countrySelection + " has no data for this food security indicator.")			return None		low_income_series = df_selected.loc[df_selected["ISO_code"] == "lowestIncome", "Value"]		mid_lower_income_series = df_selected.loc[df_selected["ISO_code"] == "midLowerIncome", "Value"]		mid_upper_income_series = df_selected.loc[df_selected["ISO_code"] == "midUpperIncome", "Value"]		high_income_series = df_selected.loc[df_selected["ISO_code"] == "uppermostIncome", "Value"]		#Add Pd Series to the line chart		line_chart.add(countrySelection, country_series)		line_chart.add("Low-Income", low_income_series)		line_chart.add("Lower-Middle-Income", mid_lower_income_series)		line_chart.add("Upper-Middle-Income", mid_upper_income_series)		line_chart.add("High-Income", high_income_series)		#Output the plot		line_chart.render_to_file(os.path.join(outputLocation, 'FAO_plot.svg'))		if itemCodeFS == 21023:		#Creat the line chart plot		line_chart = pygal.Line(title = "Depth of the Food Deficit - \n" + countrySelection, x_title = "End Year of '3-Year Average'", y_title = "Kilocalories per Capita per Day", style = customColorStyle, show_dots = False, stroke_style = {'width': 3}, show_minor_y_labels = True)		line_chart.x_labels = map(str, range(2001, 2018))		#Get just the Value column for the country of interest and the country groupings		country_series = df_selected.loc[df_selected["ISO_code"] == iso_code, "Value"]		#Some countries have no data for some indicators		if country_series.isnull().values.all():			arcpy.AddMessage(countrySelection + " has no data for this food security indicator.")			return None		low_income_series = df_selected.loc[df_selected["ISO_code"] == "lowestIncome", "Value"]		mid_lower_income_series = df_selected.loc[df_selected["ISO_code"] == "midLowerIncome", "Value"]		mid_upper_income_series = df_selected.loc[df_selected["ISO_code"] == "midUpperIncome", "Value"]		high_income_series = df_selected.loc[df_selected["ISO_code"] == "uppermostIncome", "Value"]		#Add Pd Series to the line chart		line_chart.add(countrySelection, country_series)		line_chart.add("Low-Income", low_income_series)		line_chart.add("Lower-Middle-Income", mid_lower_income_series)		line_chart.add("Upper-Middle-Income", mid_upper_income_series)		line_chart.add("High-Income", high_income_series)		#Output the plot		line_chart.render_to_file(os.path.join(outputLocation, 'FAO_plot.svg'))def distToMkt(poi, pop_polygon, outputLocation):	arcpy.AddMessage("in distance function")	#Convert the AOI to a point that's stored in memory	out_src_point = r"in_memory\src_point"	aoiCentroid = arcpy.FeatureToPoint_management(poi, out_src_point)	#Determine if centroid is in a Projected Coordinate System or a Geographic Coordinate System	#This is necessary when executing the Near tool.	SR = arcpy.Describe(aoiCentroid).spatialReference	if SR.type == "Projected":		arcpy.Near_analysis(in_features = aoiCentroid, near_features = pop_polygon, location = "LOCATION", method = "PLANAR")	elif SR.type == "Geographic":		arcpy.Near_analysis(in_features = aoiCentroid, near_features = pop_polygon, location = "LOCATION", method = "GEODESIC")	else:		arcpy.AddMessage("Did not recognize projection.")	#Read the first row of the AOI Centroid shapefile. This row specifies the distance to the nearest	#urban center with a population greater than 1,000 people per sq km.	with arcpy.da.SearchCursor(aoiCentroid, ["NEAR_DIST", "NEAR_X", "NEAR_Y"]) as cursor:		for row in cursor:			dist = row[0]			x_loc = row[1]			y_loc = row[2]			break	#Output distance to nearest urban center as well as the lat and long of the urban center.	dist_3dec = float("{0:.3f}".format(dist))	dist_km = dist_3dec / 1000	#Write the output to a text file	f = open(os.path.join(outputLocation, "DistanceToUrban.txt"), "w")	f.write("DISTANCE TO NEAREST URBAN CENTER \n")	f.write('Note: An urban center is defined as a location where population density is greater than or equal to 1,000 people per sq km. \n')	f.write('This is the definition used by the OECD. Citation: OECD (2012), Redefining "Urban": A New Way to Measure Metropolitan Areas, OECD Publishing. \n')	f.write('\nThe distance to the nearest urban center is: ' + str(dist_3dec) + ' meters (' + str(dist_km) + ' km). \n')	f.write('The longitude and latitude of this urban center in meters is (' + str(x_loc) + ', ' + str(y_loc) + ').')	f.close()def earthEngine(poi, outputLocation):	ee.Initialize()	arcpy.AddMessage("in earth engine function")	#Change projection to WGS1984	wgs = arcpy.SpatialReference(4326)	arcpy.Project_management(poi, os.path.join(arcpy.env.scratchFolder, "POI_layer_wgs.shp"), wgs)	poi_reproj = os.path.join(arcpy.env.scratchFolder, "POI_layer_wgs.shp")		#Create GEE object for point of interest	desc = arcpy.Describe(poi_reproj)	xmin = desc.extent.XMin	ymin = desc.extent.YMin	poiObject = ee.Geometry.Point([xmin, ymin])		#The CHIRPS data only spans from 50 degrees S to 50 degrees N,	#so exit earthEngine function if POI is placed outside of range	if ymin > 49.999 or ymin < -49.999:		arcpy.AddMessage("Point was placed outside geographic range of CHIRPS rainfall data (50 degrees South-50 degrees North). Pick a point between 50 deg S and 50 deg N to return rainfall information.")		return None		#CHIRPS image collection	chirps = ee.ImageCollection('UCSB-CHG/CHIRPS/DAILY')		#Set the time period over which images will be captured.	#Only rainfall from the past year will be reported.	now = datetime.datetime.now()	endYr = now.year	endMo = now.month	endDy = now.day	stYr = endYr - 1	stMo = endMo	stDy = endDy	#Create variables that will be used to iterate through each day of the year	years = range(stYr, endYr + 1)	endMoRange = endMo + 13	months = range(endMo, endMoRange)	#Set date in EE format	startdate = ee.Date.fromYMD(stYr, stMo, 1)	enddate = ee.Date.fromYMD(endYr, endMo, 1)	#Filter CHIRPS by day	Pchirps = chirps.filterDate(startdate, enddate).sort('system:time_start').select('precipitation')		#Method to calculate monthly precipitation sum	def calcMonthlySum(imageCollection):		mylist = ee.List([])		for m in months:			if m <= 12:				mo = m				yr = years[0]				w = imageCollection.filter(ee.Filter.calendarRange(yr, yr, 'year')).filter(ee.Filter.calendarRange(mo, mo, 'month')).sum()				mylist = mylist.add(w.set('system:time_start', str(mo) + '/' + str(yr)))			else:				mo = m - 12				yr = years[1]				w = imageCollection.filter(ee.Filter.calendarRange(yr, yr, 'year')).filter(ee.Filter.calendarRange(mo, mo, 'month')).sum()				mylist = mylist.add(w.set('system:time_start', str(mo) + '/' + str(yr)))		return ee.ImageCollection.fromImages(mylist)		#Call function to calculate monthly rainfall	monthlyChirps = ee.ImageCollection(calcMonthlySum(Pchirps))		#Limit output to the point of interest	monthlyChirps2 = monthlyChirps.getRegion(poiObject,24000,"epsg:4326").getInfo()		#Create pandas dataframe to plot	df = pd.DataFrame(monthlyChirps2, columns = monthlyChirps2[0])	df2 = df[1:]	df2[['id']] = df2[['id']].apply(pd.to_numeric)	collapseDF = df2.groupby('id').agg({'precipitation': np.sum, 'time': 'first'})		#Plot the Precipitation Series from the dataframe	precipSeries = collapseDF["precipitation"]	blue = pygal.style.Style(colors = ('blue', ))	bar_chart = pygal.Bar(title = u"Monthly Precipitation", x_title = "Date", y_title = "Millimeters", style = blue)		bar_chart.add("Precipitation", precipSeries)		timeSeries = collapseDF["time"]	timeList = timeSeries.tolist()	bar_chart.x_labels = timeList		bar_chart.render_to_file(os.path.join(outputLocation, 'Rainfall.svg'))def FoodSecurity():	#FAO Data	fao_csv = "C:\\Users\\Paul McCord\\Google Drive\\Toolbox\\Tool_First\\FoodSecurity\\Content_Post052418\\Data_Tabular\\FAOSTAT\\fao_clean.csv"	#Country ISO codes	country_iso_csv = "C:\\Users\\Paul McCord\\Google Drive\\Toolbox\\Tool_First\\FoodSecurity\\Content_Post052418\\Data_Tabular\\country_codes\\FAO_Area_Export.csv"	#SEDAC Population Polygon	#This polygon represents locations where pop density is 1,000 people per sq km or greater.	#This is the definition of an urban area used by the OECD.	pop_polygon = "D:\\GIS_ToolDevelopment\\FoodSecurity\\SEDAC_PopCount\\Processing\\SEDAC_popCount_reclass_polygon_over1000.shp"	#Set tool parameters	#Local variables	out_src_FeatureSet = r"in_memory\src_feature_set"	#User specified parameters	src_FeatureSet = arcpy.GetParameterAsText(0)	countrySelection = arcpy.GetParameterAsText(1)	fao_indicator = arcpy.GetParameterAsText(2)	outputLocation = arcpy.GetParameterAsText(3)	try:		#Save the Feature Set to Feature Layer		arcpy.MakeFeatureLayer_management(src_FeatureSet, out_src_FeatureSet)		poi = arcpy.CopyFeatures_management(out_src_FeatureSet, os.path.join(arcpy.env.scratchFolder, "POI_layer.shp"))				#Obtain the country ISO code to avoid formatting problems with country name		df_iso = pd.read_csv(country_iso_csv)		countryDF = df_iso[df_iso["Area"] == countrySelection]		iso_code = countryDF["ISO_code"].iloc[0]		arcpy.AddMessage("Executing food security functions for location of interest within " + countrySelection)				#Obtain the Item Code and Item Description selected by the user		if fao_indicator == "Average dietary energy supply adequacy (%) (3-year average)":			itemCodeFS = 21010		if fao_indicator == "Average value of food production (constant I$ per person) (3-year average)":			itemCodeFS = 21011		if fao_indicator == "Share of dietary energy supply derived from cereals, roots and tubers (%) (3-year average)":			itemCodeFS = 21012		if fao_indicator == "Average protein supply (g/capita/day) (3-year average)":			itemCodeFS = 21013		if fao_indicator == "Average supply of protein of animal origin (g/capita/day) (3-year average)":			itemCodeFS = 21014		if fao_indicator == "Rail-lines density (per 100 square km of land area)":			itemCodeFS = 21016		if fao_indicator == "Gross domestic product per capita, PPP (constant 2011 international $)":			itemCodeFS = 22013		if fao_indicator == "Prevalence of undernourishment (%) (3-year average)":			itemCodeFS = 21004		if fao_indicator == "Depth of the food deficit (kcal/capita/day) (3-year average)":			itemCodeFS = 21023				#Select FAO Food Security information of interest		df = pd.read_csv(fao_csv, dtype = {"Area": "S100", "Area Code": "f8", "Element": "S25", "Element Code": "f8", "Flag": "S25", 											"Flag Description": "S25", "ISO_code": "S25", "Item": "S150", "Item Code": "i4", "Unit": "S25", 											"Value": "f8", "Year": "S25", "Year Code": "f8", "YearEnd": "i4"})				#Run the Food Security Analysis functions		plotFAO(df, iso_code, fao_indicator, itemCodeFS, countrySelection, outputLocation)		distToMkt(poi, pop_polygon, outputLocation)		earthEngine(poi, outputLocation)	except Exception:		e = sys.exc_info()[1]		arcpy.AddError('An error occurred: {}'.format(e.args[0]))	if __name__ == '__main__':	FoodSecurity()	del pygal