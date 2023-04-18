metros=float(input('informe o valor em metros'))
converterKilometros=metros/1000
converterHectometros=metros/100
converterDecametros=metros/10
converterDecimetros=metros*10
converterCentimetros=metros*100
converterMilimetros=metros*1000
print('A medida de {}m convertido(s) são {:}km'.format(metros, converterKilometros)),
print('A medida de {}m convertido(s) são {:}hm'.format(metros, converterHectometros)),
print('A medida de {}m convertido(s) são {:}dam.'.format(metros, converterDecametros)),
print('A medida de {}m convertido(s) são {:.0f}dm.'.format(metros, converterDecimetros)),
print('A medida de {}m convertido(s) são {:.0f}cm.'.format(metros, converterCentimetros)),
print('A medida de {}m convertido(s) são {:.0f}mm.'.format(metros, converterMilimetros)),
