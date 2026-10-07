# Historical experimental archive; preserved with minimal cleanup.
import os, csv, requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ConfirmedCases
# HospitalizedCases
# Deaths


# ct_csv_headers 	= ["State","Date","ConfirmedCases","HospitalizedCases","Deaths","cases_age0_9","cases_age10_19","cases_age20_29","cases_age30_39","cases_age40_49","cases_age50_59","cases_age60_69","cases_age70_79","cases_age80_Older","COVID-19 Tests Reported"]
# key_to_chart 	= "ConfirmedCases"
# key_to_chart 	= "HospitalizedCases"
# key_to_chart 	= "Deaths"
# current_headers = ct_csv_headers
# csv_file 		= "ct.csv"



state_csv = [
	{
		"zip": "00000",
		"type": "state",
		"title": "Tenessee",
		"url": "https://www.tn.gov/content/dam/tn/health/documents/cedep/novel-coronavirus/datasets/Public-Dataset-Daily-Case-Info.XLSX",
		"headers": ["Date","TOTAL_CASES","NEW_CASES","TOTAL_CONFIRMED","NEW_CONFIRMED","POS_TESTS","NEG_TESTS","TOTAL_TESTS","NEW_TESTS","NEW_DEATHS","TOTAL_DEATHS","NEW_RECOVERED","TOTAL_RECOVERED","NEW_ACTIVE","TOTAL_ACTIVE","NEW_HOSP","TOTAL_HOSP"],
		"chart_keys": ["TOTAL_CASES", "NEW_CASES", "TOTAL_CONFIRMED", "POS_TESTS", "NEW_DEATHS", "NEW_ACTIVE", "TOTAL_DEATHS", "NEW_RECOVERED", "NEW_HOSP", "TOTAL_HOSP"]
	},
	{
		"zip": "11385",
		"type": "state",
		"title": "New York",
		"url": "https://data.cityofnewyork.us/resource/rc75-m7u3.csv",
		"headers": ["Date","CASE_COUNT","HOSPITALIZED_COUNT","DEATH_COUNT"],
		"chart_keys": ["date_of_interest","case_count","hospitalized_count","death_count"]
	}
] 

# tenn_csv_headers 	= 
# key_to_chart 		= "TOTAL_CASES"
# key_to_chart 		= "NEW_CASES"
# key_to_chart 		= "TOTAL_CONFIRMED"
# key_to_chart 		= "POS_TESTS"
# key_to_chart 		= "NEW_DEATHS"
# key_to_chart 		= "NEW_ACTIVE"
# key_to_chart 		= "TOTAL_DEATHS"
# key_to_chart 		= "NEW_RECOVERED"
# key_to_chart 		= "NEW_HOSP"
# key_to_chart 		= "TOTAL_HOSP"
# current_headers 	= tenn_csv_headers
# csv_file 			= "tenn.csv"




# nyc_csv_headers 	= 
# key_to_chart 		= 
# key_to_chart 		= 
# key_to_chart 		= 
# current_headers 	= nyc_csv_headers
# csv_file 			= "nyc.csv"
key_to_chart 	= ""
rsi_intervals	= []
plot_colors 	= []


def test_get(url):
	a = requests.get(url)
	print(a)
	if "200" in str(a):
		b = a.content
		print("URL == "+str(b))
		print("URL == "+str(a))
		return b

def plot_data(filename, current_headers, key_to_chart, rsi_intervals):
	global colors
	# csv_data 		= pd.read_csv(filename, names=["Date", "ConfirmedCases", "HospitalizedCases", "Deaths"], header=None)
	csv_data 		= pd.read_csv(filename, names=current_headers, header=None)
	# print(csv_data["Date"])
	csv_data 		= csv_data.iloc[1:]
	print(csv_data)
	csv_data.index 	= csv_data["Date"]
	csv_data.drop(csv_data["Date"])
	# csv_data.drop(csv_data["State"])
	colors 			= ["#00ff00", "#00ccff", "#ff00ff", "#ff1100", "#dd1100"]
	# intervals 		= [7, 20, 50]
	intervals 		= [2, 7, 14, 21, 28]
	# rsi_intervals 	= [5, 7, 14, 21, 28]
	# rsi_intervals 	= [2, 7, 14, 21, 28, 56]
	# rsi_intervals 	= [1, 2, 7, 20, 50, 100]
	df 				= csv_data
	# print(df.dtypes)
	df.assign(key_to_chart=pd.to_numeric(df[key_to_chart], errors='coerce'))

	###################################################################### 
	###################################################################### 
	
	# plt.plot(df[key_to_chart],label="current", color="#000000")

	###################################################################### 
	###################################################################### 

	# try:
	# 	print(rsi)

	# 	fig1 = plt.figure()
	# 	ax1 = fig1.add_subplot(111)
	# 	ax1.plot( df["Date"], rsi, label='mode 01' )
	# except:
	# 	pass

	###################################################################### 
	###################################################################### 

	plt.rcParams['axes.facecolor'] = 'black'
	plot_colors 	= ["#00ff00", "#ffeeee", "#ffbbbb", "#ff8888", "#ff3333", "#ff0000"]

	for a, b in enumerate(rsi_intervals):
		# try:	
		# indicator = test_rsi(df, rsi_intervals[a])
		indicator 	= moving_averages(df, rsi_intervals[a])
		df 			= indicator[1]
		indicator 	= indicator[0]
		# print(df)
		# 
		asdf = df
		# print(asdf)
		print(df)
		plt.plot(asdf["sma_"+str(rsi_intervals[a])],label=str("avg_of_avg_rsi"), color=plot_colors[a])
			# plt.plot(rsi,label=str("rsi"), color=colors[a])
		# except:
		# 	pass	
	# plt.plot(avg_rsi(df),label=str("rsi"), color="#ffffff")
	
	# print(get_std(avg_rsi(df)))
	# plot_intervals 	= [2, 5, 7, 10, 20, 50]
	plot_intervals 	= [5, 10, 20, 50]

	# for a, b in enumerate(plot_intervals):
	# 	asdf = avg_avg_rsi(avg_rsi(df), b)
	# 	print(asdf)
	# 	plt.plot(asdf,label=str("avg_of_avg_rsi"), color=plot_colors[a])

	# asdf = avg_avg_rsi(avg_rsi(df), 5)
	# plt.plot(asdf,label=str("avg_of_avg_rsi"), color="#00ffff")

	# asdf = avg_avg_rsi(avg_rsi(df), 7)
	# plt.plot(asdf,label=str("avg_of_avg_rsi"), color="#ffffff")
	
	# asdf = avg_avg_rsi(avg_rsi(df), 10)
	# plt.plot(asdf,label=str("avg_of_avg_rsi"), color="#aa55ff")
	
	# asdf = avg_avg_rsi(avg_rsi(df), 20)
	# plt.plot(asdf,label=str("avg_of_avg_rsi"), color="#ffff00")
	
	# asdf = avg_avg_rsi(avg_rsi(df), 50)
	# plt.plot(asdf,label=str("avg_of_avg_rsi"), color="#ff0000")

	# plt.plot(get_std(avg_rsi(df)),label=str("std"), color="#ffff00")


	###################################################################### 
	###################################################################### 
	###################################################################### 
	###################################################################### 
	###################################################################### 
	###################################################################### 
	###################################################################### 
	# ERROR PLOTS THAT WORK
	###################################################################### 
	# y = np.array(avg_rsi(df))
	# x = np.array(df["Date"])
	# e = np.power(y, 2)
	# plt.errorbar(x, y, e, linestyle='None', marker='^')
	###################################################################### 
	# ERROR PLOTS THAT WORK
	###################################################################### 
	# x = np.array(avg_rsi(df))
	# y = np.power(x, 2)
	# e = np.array([1.5, 2.6, 3.7, 4.6, 5.5])
	# plt.errorbar(x, y, e, linestyle='None', marker='^')

	###################################################################### 
	###################################################################### 
	###################################################################### 
	###################################################################### 
	
	# error = 0.05 + 0.1 * x
	# lower_error = 0.4 * error
	# upper_error = error
	# asymmetric_error = [lower_error, upper_error]

	# fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)
	# ax0.errorbar(x, y, yerr=error, fmt='-o')
	# ax0.set_title('variable, symmetric error')

	# ax1.errorbar(x, y, xerr=asymmetric_error, fmt='o')
	# ax1.set_yscale('log')

	###################################################################### 
	###################################################################### 
	###################################################################### 
	###################################################################### 
	###################################################################### 
	######################################################################

	# for a, b in enumerate(intervals):
	# 	try:	
	# 		df 	= marketcap_moving_average(df, intervals[a])
	# 		plt.plot(df["sma_"+str(intervals[a])],label="sma_"+str(intervals[a]), color=colors[a])
	# 	except:
	# 		pass	

	######################################################################
	######################################################################

	plt.title(filename.replace("-", " ").replace("test.csv", "").title())
	# print(df)
	plt.show()

def avg_rsi(df):
	global rsi_intervals
	a = 1
	b = pd.Series(df["rsi_"+str(rsi_intervals[0])]) 
	while a < len(rsi_intervals):
		b += pd.Series(df["rsi_"+str(rsi_intervals[a])]) 
		a+=1
	return b/len(rsi_intervals)

def test_rsi(df, n):
	global key_to_chart
	print(type(n))
	print(df)
	print(df[key_to_chart])
	print(key_to_chart)
	df.drop(df["Date"])
	test 	= pd.Series(((df[key_to_chart] - pd.Series(df[key_to_chart].rolling(n, min_periods=n).min())) / (pd.Series(df[key_to_chart].rolling(n, min_periods=n).max()) - pd.Series(df[key_to_chart].rolling(n, min_periods=n).min()))) * 100, name="rsi_"+str(n))
	df 		= df.join(test) 
	return [test, df]
	# print(test)

def moving_averages(df, n):
	global key_to_chart
	# print(type(n))
	# print(df)
	# print(df[key_to_chart])
	# print(key_to_chart)
	# df.drop(df["Date"])
	test 	= pd.Series(df[key_to_chart].rolling(n, min_periods=n).mean(), name='sma_' + str(n))
	df 		= df.join(test) 
	return [test, df]
	# print(test)

def get_std(df):
	return pd.Series(df).std()

def marketcap_moving_average(df, n):
	compiled_sma 	= pd.Series(df[key_to_chart].rolling(n, min_periods=n).mean(), name='sma_' + str(n))
	df 				= df.join(compiled_sma)
	return df

def avg_avg_rsi(df, n):
	compiled_sma 	= pd.Series(df.rolling(n, min_periods=n).mean(), name='sma_' + str(n))
	return compiled_sma


# def init_plot():	
	# for a in os.listdir("./"):
		# if ".csv" in a:
			# plot_data(a)


def init():
	global key_to_chart
	global rsi_intervals
	global colors
	# rsi_intervals 	= [2, 7, 14, 21, 56, 75]
	# rsi_intervals 	= [5, 7, 14, 21, 28]
	plot_colors 	= ["#00ff00", "#ffffff", "#ffdddd", "#ffbbbb", "#ffaaaa", "#ff0000"]
	rsi_intervals 	= [1, 2, 3, 5, 7, 10]
	# rsi_intervals 	= [1, 2, 3, 5, 10, 20]
	# test_get(state_csv[1]["url"])
	location 		= state_csv[1]
	dataset 		= location["url"]
	current_headers = location["headers"]
	# key_to_chart	= location["chart_keys"][1]
	key_to_chart	= location["headers"][3]
	csv_file 		= dataset.split("/") 
	csv_file 		= csv_file[len(csv_file)-1] 
	# os.system("wget "+dataset)
	# init_plot()
	plot_data(csv_file, current_headers, key_to_chart, rsi_intervals)

init()