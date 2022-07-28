#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 20,10


# In[1]:


predicted_cost_of_cultivation = pd.DataFrame(index = ['2021-01-01','2022-01-01','2023-01-01','2024-01-01','2025-01-01','2026-01-01'])
predicted_cost_of_production = pd.DataFrame(index = ['2021-01-01','2022-01-01','2023-01-01','2024-01-01','2025-01-01','2026-01-01'])
predicted_cost_of_operation = pd.DataFrame(index = ['2021-01-01','2022-01-01','2023-01-01','2024-01-01','2025-01-01','2026-01-01'])
predicted_income = pd.DataFrame(index = ['2021-01-01','2022-01-01','2023-01-01','2024-01-01','2025-01-01','2026-01-01'])
predicted_quantity = pd.DataFrame(index = ['2021-01-01','2022-01-01','2023-01-01','2024-01-01','2025-01-01','2026-01-01'])
predicted = pd.DataFrame(index = ['2021-01-01','2022-01-01','2023-01-01','2024-01-01','2025-01-01','2026-01-01'])


# In[2]:


input_data = input("Enter crop: ")


# In[3]:


area = int(input("Enter area in hectare: "))


# In[4]:


yield_p = int(input("Enter yield in quintal: "))


# In[6]:


if input_data == 'Jute':
    data = pd.read_excel("Jute.xlsx",index_col=0)
elif input_data == 'Arhar':
    data = pd.read_excel("Arhar.xlsx",index_col=0)
elif input_data == 'Bajra':
    data = pd.read_excel("Bajra.xlsx",index_col=0)
elif input_data == 'Coconut':
    data = pd.read_excel("Coconut.xlsx",index_col=0)
elif input_data == 'Cotton':
    data = pd.read_excel("Cotton.xlsx",index_col=0)
elif input_data == 'Jowar':
    data = pd.read_excel("Jowar.xlsx",index_col=0)
elif input_data == 'Moong':
    data = pd.read_excel("MOONG.xlsx",index_col=0)
elif input_data == 'Nigerseed':
    data = pd.read_excel("Nigerseed.xlsx",index_col=0)
elif input_data == 'Onion':
    data = pd.read_excel("Onion.xlsx",index_col=0)
elif input_data == 'Paddy':
    data = pd.read_excel("Paddy.xlsx",index_col=0)
elif input_data == 'Potato':
    data = pd.read_excel("Potato.xlsx",index_col=0)
elif input_data == 'Sesamum':
    data = pd.read_excel("Sesamum.xlsx",index_col=0)
elif input_data == 'Sunflower':
    data = pd.read_excel("Sunflower.xlsx",index_col=0)
elif input_data == 'Wheat':
    data = pd.read_excel("Wheat.xlsx",index_col=0)


# In[7]:


data.head()


# In[8]:


data.info()


# In[9]:


data = data.transpose()


# In[10]:


data.index


# In[11]:


data.index = pd.to_datetime(data.index)
predicted_cost_of_cultivation.index = pd.to_datetime(predicted_cost_of_cultivation.index)
predicted_cost_of_production.index = pd.to_datetime(predicted_cost_of_production.index)
predicted_cost_of_operation.index = pd.to_datetime(predicted_cost_of_operation.index)
predicted_income.index = pd.to_datetime(predicted_income.index)
predicted_quantity.index = pd.to_datetime(predicted_quantity.index)


# In[12]:


data.head()


# In[13]:


data.info()


# In[14]:


#!pip install pmdarima


# In[15]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 0], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[16]:


train = data.iloc[0:, 0]


# In[17]:


train


# In[18]:


data


# In[19]:


stepwise_model.fit(train)


# In[20]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[21]:


future_forecast


# In[22]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of A1_1'])
future_forecast.head()


# In[23]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[24]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[25]:


predicted_cost_of_cultivation['A1'] = future_forecast.values*area
predicted_cost_of_cultivation


# In[26]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 1], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[27]:


train = data.iloc[0:, 1]


# In[28]:


train


# In[29]:


stepwise_model.fit(train)


# In[30]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[31]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of A2_1'])
future_forecast.head()


# In[32]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[33]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[34]:


predicted_cost_of_cultivation['A2'] = future_forecast.values*area
predicted_cost_of_cultivation


# In[35]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 2], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[36]:


train = data.iloc[0:, 2]


# In[37]:


train


# In[38]:


stepwise_model.fit(train)


# In[39]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[40]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of B1_1'])
future_forecast.head()


# In[41]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[42]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[43]:


predicted_cost_of_cultivation['B1'] = future_forecast.values*area
predicted_cost_of_cultivation


# In[44]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 3], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[45]:


train = data.iloc[0:, 3]


# In[46]:


train


# In[47]:


stepwise_model.fit(train)


# In[48]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[49]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of B2_1'])
future_forecast.head()


# In[50]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[51]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[52]:


predicted_cost_of_cultivation['B2'] = future_forecast.values*area
predicted_cost_of_cultivation


# In[53]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 4], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[54]:


train = data.iloc[0:, 4]


# In[55]:


train


# In[56]:


stepwise_model.fit(train)


# In[57]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[58]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of C1_1'])
future_forecast.head()


# In[59]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[60]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[61]:


predicted_cost_of_cultivation['C1'] = future_forecast.values*area
predicted_cost_of_cultivation


# In[62]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 5], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[63]:


train = data.iloc[0:, 5]


# In[64]:


train


# In[65]:


stepwise_model.fit(train)


# In[66]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[67]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of C2_1'])
future_forecast.head()


# In[68]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[69]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[70]:


predicted_cost_of_cultivation['C2'] = future_forecast.values*area
predicted_cost_of_cultivation


# In[71]:


output1 = pd.ExcelWriter('predicted_cost_of_cultivation.xlsx')


# In[72]:


predicted_cost_of_cultivation.to_excel(output1)


# In[73]:


output1.save()


# In[74]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 7], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[75]:


train = data.iloc[0:, 7]


# In[76]:


train


# In[77]:


stepwise_model.fit(train)


# In[78]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[79]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of A1_2'])
future_forecast.head()


# In[80]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[81]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[82]:


predicted_cost_of_production['A1_'] = future_forecast.values*yield_p
predicted_cost_of_production


# In[83]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 8], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[84]:


train = data.iloc[0:, 8]


# In[85]:


train


# In[86]:


stepwise_model.fit(train)


# In[87]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[88]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of A2_2'])
future_forecast.head()


# In[89]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[90]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[91]:


predicted_cost_of_production['A2_'] = future_forecast.values*yield_p
predicted_cost_of_production


# In[92]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 9], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[93]:


train = data.iloc[0:, 9]


# In[94]:


train


# In[95]:


stepwise_model.fit(train)


# In[96]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[97]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of B1_2'])
future_forecast.head()


# In[98]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[99]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[100]:


predicted_cost_of_production['B1_'] = future_forecast.values*yield_p
predicted_cost_of_production


# In[101]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 10], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[102]:


train = data.iloc[0:, 10]


# In[103]:


train


# In[104]:


stepwise_model.fit(train)


# In[105]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[106]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of B2_2'])
future_forecast.head()


# In[107]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[108]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[109]:


predicted_cost_of_production['B2_'] = future_forecast.values*yield_p
predicted_cost_of_production


# In[110]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 11], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[111]:


train = data.iloc[0:, 11]


# In[112]:


train


# In[113]:


stepwise_model.fit(train)


# In[114]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[115]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of C1_2'])
future_forecast.head()


# In[116]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[117]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[118]:


predicted_cost_of_production['C1_'] = future_forecast.values*yield_p
predicted_cost_of_production


# In[119]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 12], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[120]:


train = data.iloc[0:, 12]


# In[121]:


train


# In[122]:


stepwise_model.fit(train)


# In[123]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[124]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of C2_2'])
future_forecast.head()


# In[125]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[126]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[127]:


predicted_cost_of_production['C2_'] = future_forecast.values*yield_p
predicted_cost_of_production


# In[128]:


output2 = pd.ExcelWriter('predicted_cost_of_production.xlsx')


# In[129]:


predicted_cost_of_production.to_excel(output2)


# In[130]:


output2.save()


# In[131]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 15], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[132]:


train = data.iloc[0:, 15]


# In[133]:


train


# In[134]:


stepwise_model.fit(train)


# In[135]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[136]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of Value of Main Product (Rs./Hectare)'])
future_forecast.head()


# In[137]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[138]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[139]:


predicted_income['Value of Main Product (Rs./Hectare)'] = future_forecast.values*area
predicted_income


# In[140]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 16], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[141]:


train = data.iloc[0:, 16]


# In[142]:


train


# In[143]:


stepwise_model.fit(train)


# In[144]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[145]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of Value of By- Product (Rs./Hectare)'])
future_forecast.head()


# In[146]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[147]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[148]:


predicted_income['Value of By- Product (Rs./Hectare)'] = future_forecast.values*area
predicted_income


# In[149]:


output3 = pd.ExcelWriter('predicted_income.xlsx')


# In[150]:


predicted_income.to_excel(output3)


# In[151]:


output3.save()


# In[152]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 18], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[153]:


train = data.iloc[0:, 18]


# In[154]:


train


# In[155]:


stepwise_model.fit(train)


# In[156]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[157]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of Human Labour'])
future_forecast.head()


# In[158]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[159]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[160]:


predicted_cost_of_operation['Human Labour'] = future_forecast.values*area
predicted_cost_of_operation


# In[161]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 19], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[162]:


train = data.iloc[0:, 19]


# In[163]:


train


# In[164]:


stepwise_model.fit(train)


# In[165]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[166]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of Animal Labour'])
future_forecast.head()


# In[167]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[168]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[169]:


predicted_cost_of_operation['Animal Labour'] = future_forecast.values*area
predicted_cost_of_operation


# In[170]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 20], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[171]:


train = data.iloc[0:, 20]


# In[172]:


train


# In[173]:


stepwise_model.fit(train)


# In[174]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[175]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of Machine Labour'])
future_forecast.head()


# In[176]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[177]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[178]:


predicted_cost_of_operation['Machine Labour'] = future_forecast.values*area
predicted_cost_of_operation


# In[179]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 21], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[180]:


train = data.iloc[0:, 21]


# In[181]:


train


# In[182]:


stepwise_model.fit(train)


# In[183]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[184]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of seed'])
future_forecast.head()


# In[185]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[186]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[187]:


predicted_cost_of_operation['Seed'] = future_forecast.values*area
predicted_cost_of_operation


# In[188]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 22], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[189]:


train = data.iloc[0:, 22]


# In[190]:


train


# In[191]:


stepwise_model.fit(train)


# In[192]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[193]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of Fertilizer & Manure'])
future_forecast.head()


# In[194]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[195]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[196]:


predicted_cost_of_operation['Fertilizer & Manure'] = future_forecast.values*area
predicted_cost_of_operation


# In[197]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 23], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[198]:


train = data.iloc[0:, 23]


# In[199]:


train


# In[200]:


stepwise_model.fit(train)


# In[201]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[202]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of Insecticides'])
future_forecast.head()


# In[203]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[204]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[205]:


predicted_cost_of_operation['Insecticides'] = future_forecast.values*area
predicted_cost_of_operation


# In[206]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 24], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[207]:


train = data.iloc[0:, 24]


# In[208]:


train


# In[209]:


stepwise_model.fit(train)


# In[210]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[211]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of Irrigation Charges'])
future_forecast.head()


# In[212]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[213]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[214]:


predicted_cost_of_operation['Irrigation Charges'] = future_forecast.values*area
predicted_cost_of_operation


# In[215]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 25], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[216]:


train = data.iloc[0:, 25]


# In[217]:


train


# In[218]:


stepwise_model.fit(train)


# In[219]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[220]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of Miscellaneous'])
future_forecast.head()


# In[221]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[222]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[223]:


predicted_cost_of_operation['Miscellaneous'] = future_forecast.values*area
predicted_cost_of_operation


# In[224]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 26], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[225]:


train = data.iloc[0:, 26]


# In[226]:


train


# In[227]:


stepwise_model.fit(train)


# In[228]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[229]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of Interest on Working Capital'])
future_forecast.head()


# In[230]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[231]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[232]:


predicted_cost_of_operation['Interest on Working Capital'] = future_forecast.values*area
predicted_cost_of_operation


# In[233]:


output4 = pd.ExcelWriter('predicted_cost_of_operation.xlsx')


# In[234]:


predicted_cost_of_operation.to_excel(output4)


# In[235]:


output4.save()


# In[236]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 27], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[237]:


train = data.iloc[0:, 27]


# In[238]:


train


# In[239]:


stepwise_model.fit(train)


# In[240]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[241]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction of Seed (Kg.)'])
future_forecast.head()


# In[242]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[243]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[244]:


predicted_quantity['Seed (Kg.)'] = future_forecast.values*area
predicted_quantity


# In[245]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 28], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[246]:


train = data.iloc[0:, 28]


# In[247]:


train


# In[248]:


stepwise_model.fit(train)


# In[249]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[250]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction Fertilizer (Kg. Nutrients)'])
future_forecast.head()


# In[251]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[252]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[253]:


predicted_quantity['Fertilizer (Kg. Nutrients)'] = future_forecast.values*area
predicted_quantity


# In[254]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 29], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[255]:


train = data.iloc[0:, 29]


# In[256]:


train


# In[257]:


stepwise_model.fit(train)


# In[258]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[259]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction Manure (Qtl.)'])
future_forecast.head()


# In[260]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[261]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[262]:


predicted_quantity['Manure (Qtl.)'] = future_forecast.values*area
predicted_quantity


# In[263]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 30], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[264]:


train = data.iloc[0:, 30]


# In[265]:


train


# In[266]:


stepwise_model.fit(train)


# In[267]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[268]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction Human Labour* (Man Hrs.)'])
future_forecast.head()


# In[269]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[270]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[271]:


predicted_quantity['Human Labour* (Man Hrs.)'] = future_forecast.values*area
predicted_quantity


# In[272]:


from pmdarima.arima import auto_arima
stepwise_model = auto_arima(data.iloc[0:, 31], start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


# In[273]:


train = data.iloc[0:, 31]


# In[274]:


train


# In[275]:


stepwise_model.fit(train)


# In[276]:


future_forecast = stepwise_model.predict(n_periods=6)


# In[277]:


future_forecast = pd.DataFrame(future_forecast,index = predicted.index,columns=['Prediction Animal Labour (Pair Hrs.)'])
future_forecast.head()


# In[278]:


x1 = train.index
y1 = train.values
x2 = future_forecast.index
y2 = future_forecast.values


# In[279]:


plt.plot(x2,y2,label = 'Predicted data')
plt.plot(x1,y1,label = 'Trained data')
plt.show


# In[280]:


predicted_quantity['Animal Labour (Pair Hrs.)'] = future_forecast.values*area
predicted_quantity


# In[281]:


output5 = pd.ExcelWriter('predicted_quantity.xlsx')


# In[282]:


predicted_quantity.to_excel(output5)


# In[283]:


output5.save()

