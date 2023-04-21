# %%
import pandas as pd
import sqlalchemy

# %%
data = pd.read_csv("data/EnergySummary.csv")

# %%
a = "1,046,492	1,167,142	1,192,848	1,189,801	1,148,722	1,220,587	1,202,586	1,154,079	1,196,279	1,290,698	1,226,364	1,192,869	1,232,826	1,226,313	1,227,952	1,304,360	1,217,724	1,308,727	1,359,856	1,420,797	1,367,856	1,367,567	1,355,310	1,354,131	1,369,438	1,325,392	1,361,384	1,358,381	1,486,214	1,485,795	1,426,721	1,417,985	1,425,659	1,455,716	1,489,320	1,449,101	1,488,574	1,474,374	1,511,586	1,483,981	1,466,657	1,500,559	1,437,024	1,440,463	1,355,028	1,347,770	1,367,103	1,415,455	1,440,273	1,455,751	1,507,721"
a = a.split()
a = a[:]
Resid_total = pd.DataFrame(a)
Resid_total = Resid_total.T
Resid_total.rename(index={0:"ResidCA"},inplace=True)
Resid_total

# %%
data = pd.read_csv("dataCA/pr_CA.csv",index_col="MSN")
data = data[:]
data

# %%
data2 = data.drop(['Data_Status', 'State'],axis=1)
data2

# %%
Resid_total.columns = data2.columns
data3 = pd.concat([data2,Resid_total])
data3

# %%
import matplotlib.pyplot as mpl

# %%
a = "1,046,492	1,167,142	1,192,848	1,189,801	1,148,722	1,220,587	1,202,586	1,154,079	1,196,279	1,290,698	1,226,364	1,192,869	1,232,826	1,226,313	1,227,952	1,304,360	1,217,724	1,308,727	1,359,856	1,420,797	1,367,856	1,367,567	1,355,310	1,354,131	1,369,438	1,325,392	1,361,384	1,358,381	1,486,214	1,485,795	1,426,721	1,417,985	1,425,659	1,455,716	1,489,320	1,449,101	1,488,574	1,474,374	1,511,586	1,483,981	1,466,657	1,500,559	1,437,024	1,440,463	1,355,028	1,347,770	1,367,103	1,415,455	1,440,273	1,455,751	1,507,721"
a = a.split()
a = a[:]
Resid_total = pd.DataFrame(a)
Resid_total = Resid_total.T
Resid_total.rename(index={0:"ResidCA"},inplace=True)
Resid_total
Resid_total.columns = data2.columns
data3 = pd.concat([data2,Resid_total])

a = "13,728,645	14,210,554	14,861,651	14,919,481	14,651,895	14,814,536	15,417,206	15,663,022	16,143,315	15,813,447	15,731,634	15,247,535	15,497,034	15,399,060	15,920,721	16,041,775	15,951,750	16,228,823	17,132,762	17,775,513	16,930,638	17,401,226	17,331,937	18,209,357	18,093,506	18,508,903	19,500,508	18,957,636	18,941,595	19,535,978	20,384,790	20,026,646	20,763,207	21,080,842	21,042,686	21,574,410	20,631,559	21,489,150	21,635,346	21,052,360	21,860,325	21,345,572	19,828,618	21,018,102	21,418,020	20,586,481	20,157,650	19,861,744	21,486,929	21,042,063	20,520,596																																																				"
a = a.split()
a = a[:]
Resid_total = pd.DataFrame(a)
Resid_total = Resid_total.T
Resid_total.rename(index={0:"ResidUS"},inplace=True)
Resid_total.columns = data2.columns
data3 = pd.concat([data3,Resid_total])
data3

# %%
Resid_total = pd.read_excel('/Users/zhuojiaodong/share/stats170/project/dataCA/use_tot_sector.xlsx', sheet_name='Residential Sector',header=2)
Resid_total

# %%

engine = sqlalchemy.create_engine('postgresql://postgres:Qwer1234@localhost:5432/EnergyPrediction')


# %%
table_name = 'Resid_consumption'
Resid_total.to_sql(table_name, engine, if_exists='replace', index=False)


# %%
Commercial_total = pd.read_excel('/Users/zhuojiaodong/share/stats170/project/dataCA/use_tot_sector.xlsx', 
                            sheet_name='Commercial Sector',header=2)
Industril_total = pd.read_excel('/Users/zhuojiaodong/share/stats170/project/dataCA/use_tot_sector.xlsx', 
                            sheet_name='Industrial Sector',header=2)
Transportation_total = pd.read_excel('/Users/zhuojiaodong/share/stats170/project/dataCA/use_tot_sector.xlsx', 
                            sheet_name='Transportation Sector',header=2)
Total_Consumption = pd.read_excel('/Users/zhuojiaodong/share/stats170/project/dataCA/use_tot_sector.xlsx', 
                            sheet_name='Total Consumption',header=2)


# %%
Commercial_total.to_sql("Commercial_total", engine, if_exists='replace', index=False)
Industril_total.to_sql("Industril_total", engine, if_exists='replace', index=False)
Transportation_total.to_sql("Transportation_total", engine, if_exists='replace', index=False)
Total_Consumption.to_sql("Total_Consumption", engine, if_exists='replace', index=False)



# %%
data

# %%
data.to_sql("price_ca",engine, if_exists="replace",index=True)

# %%
All = pd.read_csv('/Users/zhuojiaodong/share/stats170/project/dataCA/use_all_btu.csv')

# %%
All

# %%
All.to_sql("All",engine, if_exists="replace",index=True)

# %%
Coal = pd.read_excel('/Users/zhuojiaodong/share/stats170/project/dataCA/use_energy_source.xlsx', 
                            sheet_name='Coal',header=2)
Natural_Gas = pd.read_excel('/Users/zhuojiaodong/share/stats170/project/dataCA/use_energy_source.xlsx', 
                            sheet_name='Natural Gas',header=2)
Petroleum = pd.read_excel('/Users/zhuojiaodong/share/stats170/project/dataCA/use_energy_source.xlsx', 
                            sheet_name='Petroleum',header=2)
Nuclear = pd.read_excel('/Users/zhuojiaodong/share/stats170/project/dataCA/use_energy_source.xlsx', 
                            sheet_name='Nuclear',header=2)
Renew = pd.read_excel('/Users/zhuojiaodong/share/stats170/project/dataCA/use_energy_source.xlsx', 
                            sheet_name='Total Renewable Energy',header=2)

# %%
Coal.to_sql("Coal", engine, if_exists='replace', index=False)
Natural_Gas.to_sql("Natural_Gas", engine, if_exists='replace', index=False)
Petroleum.to_sql("Petroleum", engine, if_exists='replace', index=False)
Nuclear.to_sql("Nuclear", engine, if_exists='replace', index=False)
Renew.to_sql("Renew", engine, if_exists='replace', index=False)


